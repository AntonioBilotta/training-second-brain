#!/usr/bin/env python3
"""Genera i file di seduta di un microciclo da un programma training-program/v1.

Specifica dei formati: progetto TrainingApp, docs/formats.md (programma training-program/v1,
seduta training-session/v1). Il vecchio formato a checklist si genera con genera_sedute_v1.py.

Programma letto: <cartella_programma>/programma.v2.yaml se esiste, altrimenti programma.yaml;
in entrambi i casi deve dichiarare `format: training-program/v1`.
Cartella di uscita: raw/journal/<anno prima seduta>/da <prima data> a <ultima data> <programma>/
dove <programma> è il nome della cartella del programma senza la data (es. self_vena_aif).

Uso:  python3 .github/scripts/genera_sedute.py <cartella_programma> <microciclo> [--rigenera]
<microciclo> è il numero progressivo attraverso i blocchi (nel programma in corso il taper è 5).
Non sovrascrive un file esistente. Con --rigenera sovrascrive SOLO i file ancora intatti
(status: planned e nessuna serie segnata nella colonna ✓); quelli già usati da iPad non si toccano.
"""
import sys, datetime, pathlib, re
from decimal import Decimal, ROUND_FLOOR
import yaml

FORMAT = "training-program/v1"
WEEKDAYS = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
GIORNI = ["lun", "mar", "mer", "gio", "ven", "sab", "dom"]
MESI = ["gen", "feb", "mar", "apr", "mag", "giu", "lug", "ago", "set", "ott", "nov", "dic"]
EMPTY_BAR = 20
ISTRUZIONI = ("> Ogni riga riporta il previsto. Scrivi `x` in ✓ quando fai la serie; "
              "se cambi carico, ripetizioni o RPE correggi la cella. R = riscaldamento.")


# --- programma -------------------------------------------------------------------------------

def arrotonda(x, passo):
    """Multiplo di `passo` più vicino; a metà per difetto (86,25 → 85 con passo 2,5)."""
    q = Decimal(str(x)) / Decimal(str(passo))
    f = q.to_integral_value(rounding=ROUND_FLOOR)
    if q - f > Decimal("0.5"):
        f += 1
    return float(f * Decimal(str(passo)))


def nelle_settimane(spec, settimana):
    if spec is None:
        return True
    spec = str(spec)
    if "-" in spec:
        a, b = spec.split("-")
        return int(a) <= settimana <= int(b)
    return int(spec) == settimana


def microcicli(cfg):
    """[(numero progressivo, blocco, indice nel blocco, settimane)] attraverso tutti i blocchi."""
    out, n = [], 0
    for blocco in cfg["blocks"]:
        for i, settimane in enumerate(blocco["microcycles"]):
            n += 1
            out.append((n, blocco, i, settimane))
    return out


def valore(v, m, k):
    if isinstance(v, dict):
        if "per_week" in v:
            return v["per_week"][k]
        if "per_microcycle" in v:
            return v["per_microcycle"][m]
        raise ValueError(f"valore variabile non riconosciuto: {v}")
    return v


def serie(cfg, es, settimana, m, k):
    """Righe della tabella di un esercizio: riscaldamento (R) e serie allenanti (W)."""
    passo = cfg.get("rounding", 2.5)
    righe, ids = [], {}
    for gruppo in es["sets"]:
        if not nelle_settimane(gruppo.get("weeks"), settimana):
            continue
        load = gruppo.get("load", {})
        kg = rpe = pct = rif = None
        if "of" in load:
            rif = (load["of"], load["pct"])
        elif "pct" in load:
            pct = valore(load["pct"], m, k)
            kg = arrotonda(cfg["training_maxes"][es.get("max", es["exercise"])] * pct / 100, passo)
        elif "kg" in load:
            kg = float(valore(load["kg"], m, k))
        if "rpe" in load:
            rpe = str(valore(load["rpe"], m, k))
            if load.get("hint_kg"):
                kg = float(load["hint_kg"])
        for _ in range(gruppo["count"]):
            righe.append(dict(tipo="W", kg=kg, pct=pct, rip=str(valore(gruppo["reps"], m, k)),
                              rpe=rpe, rif=rif, calcolato=kg is not None and rpe is None))
        if "id" in gruppo:
            ids[gruppo["id"]] = len(righe)
    for r in righe:
        if r["rif"]:
            r["rif_riga"] = ids[r["rif"][0]]
    risc = []
    if es.get("warmup"):
        schema = cfg["warmups"][es["warmup"]]
        if schema.get("empty_bar_reps"):
            risc.append(dict(tipo="R", kg=float(EMPTY_BAR), rip=str(schema["empty_bar_reps"])))
        base = next((r["kg"] for r in righe if r["calcolato"]), None)
        if base is None:
            risc.append(dict(tipo="R", kg=None, rip="", libero=True))
        else:
            for passo_risc in schema["steps"]:
                w = arrotonda(base * passo_risc["pct"] / 100, passo)
                if w > EMPTY_BAR:
                    risc.append(dict(tipo="R", kg=w, rip=str(passo_risc["reps"])))
    return risc + righe


def valida(cfg):
    errori = []
    if cfg.get("format") != FORMAT:
        errori.append(f"format deve essere {FORMAT}")
    viste = set()
    for n, blocco, i, settimane in microcicli(cfg):
        for s in settimane:
            if s in viste or s > cfg["weeks"]:
                errori.append(f"settimana {s} ripetuta o oltre weeks")
            viste.add(s)
    for blocco in cfg["blocks"]:
        lungo = max(len(s) for s in blocco["microcycles"])
        for g in blocco["schedule"]:
            if g not in blocco["days"]:
                errori.append(f"{blocco['name']}: giornata {g} senza contenuto")
        for g, giornata in blocco["days"].items():
            for es in giornata["exercises"]:
                ids = []
                for gruppo in es["sets"]:
                    load = gruppo.get("load", {})
                    for v in (gruppo["reps"], load.get("pct"), load.get("kg"), load.get("rpe")):
                        if isinstance(v, dict) and len(v.get("per_week", [0] * lungo)) < lungo:
                            errori.append(f"{g} {es['label']}: per_week più corto del microciclo")
                        if isinstance(v, dict) and len(v.get("per_microcycle", blocco["microcycles"])) < len(blocco["microcycles"]):
                            errori.append(f"{g} {es['label']}: per_microcycle più corto dei microcicli")
                    if "of" in load and load["of"] not in ids:
                        errori.append(f"{g} {es['label']}: of punta a un id inesistente o successivo")
                    if "pct" in load and "of" not in load and es.get("max", es["exercise"]) not in cfg.get("training_maxes", {}):
                        errori.append(f"{g} {es['label']}: manca il massimale per la %")
                    if "id" in gruppo:
                        ids.append(gruppo["id"])
    if errori:
        sys.exit("programma non valido:\n  " + "\n  ".join(errori))


# --- seduta ----------------------------------------------------------------------------------

def kg(x):
    return "" if x is None else f"{x:g}".replace(".", ",")


def tabella(es, righe):
    intestazione = ["#", "Zavorra" if es.get("bodyweight") else "Kg", "%",
                    "Rip/lato" if es.get("per_side") else "Rip", "RPE", "✓"]
    celle, nr, nw = [], 0, 0
    for r in righe:
        if r["tipo"] == "R":
            nr += 1
            celle.append([f"R{nr}", "a salire" if r.get("libero") else kg(r["kg"]), "", r["rip"], "", ""])
        else:
            nw += 1
            carico = f"{kg(r['rif'][1])} % di #{r['rif_riga']}" if r["rif"] else kg(r["kg"])
            pct = "" if r["pct"] is None else kg(float(r["pct"]))
            celle.append([str(nw), carico, pct, r["rip"], r["rpe"] or "", ""])
    # Stile con cui Obsidian riformatta le tabelle: colonne di almeno 3 caratteri, "| --- |".
    larghezze = [max(3, len(h), *(len(c[i]) for c in celle)) for i, h in enumerate(intestazione)]
    riga = lambda cs: "| " + " | ".join(c.ljust(larghezze[i]) for i, c in enumerate(cs)) + " |"
    sep = "| " + " | ".join("-" * l for l in larghezze) + " |"
    return "\n".join([riga(intestazione), sep] + [riga(c) for c in celle])


def seduta(cfg, n, blocco, i, settimane, settimana, giorno, data):
    k = settimane.index(settimana)
    g = blocco["days"][giorno]
    fm = ["---", "type: workout", "format: training-session/v1", f"program: {cfg['id']}",
          f"date: {data.isoformat()}", f"week: {settimana}", f"microcycle: {n}", f"day: {giorno}"]
    if g.get("kind"):
        fm.append(f"kind: {g['kind']}")
    if g.get("optional"):
        fm.append("optional: true")
    fm += ["status: planned          # planned | done | moved | skipped", "actual_date:", "duration_min:", "---"]
    titolo_blocco = f"{blocco['title']} · " if blocco.get("title") else ""
    out = fm + [f"# W{settimana} · {giorno} — {g['title']}" + (" (facoltativa)" if g.get("optional") else ""), "",
                f"{GIORNI[data.weekday()]} {data.day} {MESI[data.month - 1]} {data.year} · {titolo_blocco}MC{n}, "
                f"settimana {k + 1} di {len(settimane)}", "", ISTRUZIONI, ""]
    if g.get("note"):
        out += [f"> [!note] {g['note']}", ""]
    for es in g["exercises"]:
        if not nelle_settimane(es.get("weeks"), settimana):
            continue
        out.append(f"## {es['label']}" + (" (opzionale)" if es.get("optional") else ""))
        esecuzione = es.get("execution")
        if any(gr.get("load", {}).get("hint_kg") for gr in es["sets"]):
            esecuzione = f"{esecuzione}; carico indicativo" if esecuzione else "carico indicativo"
        if esecuzione:
            out.append(f"*Esecuzione:* {esecuzione}")
        out += ["", tabella(es, serie(cfg, es, settimana, i, k)), ""]
        if es.get("note"):
            out += [f"> [!note] {es['note']}", ""]
        out += ["note:: ", ""]
    out += ["## Note seduta", "note:: ", ""]
    return "\n".join(out)


def intatto(testo):
    """Seduta mai compilata: status planned e nessuna cella ✓ valorizzata."""
    if not re.search(r"^status: planned\b", testo, re.M):
        return False
    for riga in testo.splitlines():
        celle = [c.strip() for c in riga.strip().strip("|").split("|")] if riga.startswith("|") else []
        if len(celle) > 1 and celle[0] not in ("#", "") and not set(celle[0]) <= {"-"} and celle[-1]:
            return False
    return True


# --- main ------------------------------------------------------------------------------------

def main(prog_dir, mc, rigenera=False):
    prog_dir = pathlib.Path(prog_dir).resolve()
    root = prog_dir.parents[3]  # vault root: <vault>/raw/programs/<anno>/<programma>
    file = prog_dir / "programma.v2.yaml"
    if not file.exists():
        file = prog_dir / "programma.yaml"
    cfg = yaml.safe_load(open(file, encoding="utf-8"))
    valida(cfg)
    start = cfg["start_date"]
    if isinstance(start, str):
        start = datetime.date.fromisoformat(start)
    trovato = [x for x in microcicli(cfg) if x[0] == mc]
    if not trovato:
        sys.exit(f"il microciclo {mc} non esiste nel programma ({len(microcicli(cfg))} microcicli)")
    n, blocco, i, settimane = trovato[0]
    sedute = []
    for settimana in settimane:
        lunedi = start + datetime.timedelta(weeks=settimana - 1)
        for giorno, wd in blocco["schedule"].items():
            sedute.append((settimana, giorno, lunedi + datetime.timedelta(days=WEEKDAYS.index(wd))))
    d0, d1 = min(s[2] for s in sedute), max(s[2] for s in sedute)
    nome = prog_dir.name.split("_", 1)[1]
    out_dir = root / "raw" / "journal" / str(d0.year) / f"da {d0.isoformat()} a {d1.isoformat()} {nome}"
    creati, saltati = [], []
    for settimana, giorno, data in sorted(sedute, key=lambda s: s[2]):
        path = out_dir / f"{data.isoformat()} W{settimana} {giorno}.md"
        if path.exists() and not (rigenera and intatto(path.read_text(encoding="utf-8"))):
            saltati.append(path.name)
            continue
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(seduta(cfg, n, blocco, i, settimane, settimana, giorno, data), encoding="utf-8")
        creati.append(path.name)
    print("programma:", file.relative_to(root))
    print("cartella:", out_dir.relative_to(root))
    print("creati:", *creati, sep="\n  ")
    if saltati:
        print("già esistenti (non toccati):", *saltati, sep="\n  ")


if __name__ == "__main__":
    main(sys.argv[1], int(sys.argv[2]), "--rigenera" in sys.argv)
