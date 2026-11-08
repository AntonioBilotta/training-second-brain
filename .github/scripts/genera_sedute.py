#!/usr/bin/env python3
"""Genera i file di seduta di un microciclo a partire da programma.yaml.

Cartella di uscita: raw/journal/<anno prima seduta>/da <prima data> a <ultima data> <programma>/
dove <programma> è il nome della cartella del programma senza la data (es. self_vena_aif).

Uso:  python3 .github/scripts/genera_sedute.py <cartella_programma> <microciclo> [--rigenera]
Non sovrascrive un file esistente. Con --rigenera sovrascrive SOLO i file ancora
intatti (stato: pianificata e nessuna serie spuntata); quelli già usati da iPad non si toccano.
"""
import sys, datetime, pathlib, yaml

GIORNI = ["lun", "mar", "mer", "gio", "ven", "sab", "dom"]
MESI = ["gen", "feb", "mar", "apr", "mag", "giu", "lug", "ago", "set", "ott", "nov", "dic"]


def r25(x):
    return round(x / 2.5) * 2.5


def kg(x):
    return (f"{x:.1f}".rstrip("0").rstrip(".")).replace(".", ",")


def riscaldamento(cfg, carico, alzata):
    out = []
    if alzata in ("squat", "panca"):
        out.append("- [ ] bilanciere × 10 *(risc.)*")
    for frac, reps in cfg["riscaldamento"]:
        w = r25(carico * frac)
        if w > 20:
            out.append(f"- [ ] {kg(w)} × {reps} *(risc.)*")
    return out


def blocco(cfg, b, mc, wk_in_mc, settimana):
    i = mc - 1
    t = b["tipo"]
    lines = [f"## {b['nome']}"]
    c = b.get("carichi", [None] * 4)[i] if b.get("carichi") else None
    if b.get("risc") and c:
        lines += riscaldamento(cfg, c, b.get("alzata"))
    if t == "volume":
        reps = cfg["reps_volume"][wk_in_mc]
        lines += [f"- [ ] {kg(c)} × {reps}"] * b["serie"]
    elif t == "larsen":
        reps = cfg["reps_larsen"][wk_in_mc]
        lines += [f"- [ ] {kg(c)} × {reps}"] * b["serie"]
    elif t == "fisso":
        lines += [f"- [ ] {kg(c)} × {b['reps']}"] * b["serie"]
    elif t == "intensita":
        rpe = cfg["rpe_singola"][wk_in_mc]
        lines.append(f"- [ ] singola @{rpe} → kg:: ")
        lines += [f"- [ ] {kg(c)} × 2"] * b["serie"]
        lines += ["", "> [!note] Freno: se le doppie superano RPE 7, −5 % in questa seduta."]
    elif t == "stacco_fermo":
        var = "fermo a 1 cm da terra" if settimana <= 6 else "fermo al ginocchio"
        lines[0] += f" — {var}"
        lines += [f"- [ ] {kg(c)} × {b['reps']}"] * b["serie"]
    elif t == "tempo_bench":
        lines += ["- [ ] bilanciere × 10 *(risc.)*", "- [ ] riscaldamento a salire *(risc.)*",
                  "- [ ] singola @6 → kg:: ", "- [ ] 2 @RPE 6 → kg:: ", "- [ ] 2 @RPE 6 → kg:: "]
    elif t == "rpe":
        ind = f" (indicativo {kg(b['indicativo'])})" if b.get("indicativo") else ""
        lines += [f"- [ ] {b['reps']} @RPE {b['rpe']}{ind} → kg:: "] * b["serie"]
    elif t == "compl":
        ced = "@8-9 (rientro)" if settimana == 1 else "@10 cedimento"
        lines += [f"- [ ] 8-10 {ced} → kg:: "] * b["serie_ced"]
        lines += ["- [ ] 8-10 @8 → kg:: "] * b["serie_8"]
    elif t == "spalla":
        lines[0] += " (mai a cedimento)"
        lines += ["- [ ] face pull", "- [ ] push-up plus", "- [ ] Y-T-W", "- [ ] stretching pettorale minore"]
    lines.append("")
    if t not in ("compl", "spalla"):
        lines.append("rpe:: ")
    lines.append("note:: ")
    return "\n".join(lines)


def main(prog_dir, mc, rigenera=False):
    root = pathlib.Path(prog_dir).resolve().parents[2].parent  # vault root
    cfg = yaml.safe_load(open(pathlib.Path(prog_dir) / "programma.yaml"))
    start = cfg["start_date"]
    if isinstance(start, str):
        start = datetime.date.fromisoformat(start)
    prog_name = pathlib.Path(prog_dir).resolve().name.split("_", 1)[1]
    sedute = []
    for wk_in_mc, settimana in enumerate(cfg["microcicli"][mc]):
        lunedi = start + datetime.timedelta(weeks=settimana - 1)
        for g, off in cfg["giorni"].items():
            sedute.append((wk_in_mc, settimana, g, lunedi + datetime.timedelta(days=off)))
    d0, d1 = min(s[3] for s in sedute), max(s[3] for s in sedute)
    out_dir = root / "raw" / "journal" / str(d0.year) / f"da {d0.isoformat()} a {d1.isoformat()} {prog_name}"
    creati, saltati = [], []
    for wk_in_mc, settimana in enumerate(cfg["microcicli"][mc]):
        lunedi = start + datetime.timedelta(weeks=settimana - 1)
        for g, off in cfg["giorni"].items():
            d = lunedi + datetime.timedelta(days=off)
            gio = cfg["giornate"][g]
            path = out_dir / f"{d.isoformat()} W{settimana} {g}.md"
            if path.exists():
                old = path.read_text(encoding="utf-8")
                intatto = "stato: pianificata" in old and "- [x]" not in old.lower()
                if not (rigenera and intatto):
                    saltati.append(path.name)
                    continue
            fm = (f"---\ntype: workout\nprogram: {cfg['program']}\ndate: {d.isoformat()}\n"
                  f"settimana: {settimana}\nmicrociclo: {mc}\ngiornata: {g}\n"
                  f"stato: pianificata        # pianificata | fatta | spostata | saltata\n"
                  f"data_effettiva:\ndurata_min:\n---\n")
            head = (f"# W{settimana} · {g} — {gio['titolo']}\n\n"
                    f"{GIORNI[d.weekday()]} {d.day} {MESI[d.month-1]} {d.year} · MC{mc}, settimana {wk_in_mc+1} di {len(cfg['microcicli'][mc])}\n\n"
                    "> Spunta le serie fatte; se cambi carico o ripetizioni correggi il numero sulla riga.\n")
            body = "\n\n".join(blocco(cfg, b, mc, wk_in_mc, settimana) for b in gio["blocchi"])
            tail = "\n\n## Note seduta\nnote:: \n"
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(fm + head + "\n" + body + tail, encoding="utf-8")
            creati.append(path.name)
    print("cartella:", out_dir.relative_to(root))
    print("creati:", *creati, sep="\n  ")
    if saltati:
        print("già esistenti (non toccati):", *saltati, sep="\n  ")


if __name__ == "__main__":
    main(sys.argv[1], int(sys.argv[2]), "--rigenera" in sys.argv)
