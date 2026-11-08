# Templates

Seed files per popolare `raw/` senza dover ricordare a memoria frontmatter e struttura. Sono **template**, non contenuti wiki: vivono in `.github/` (meta) e vanno **copiati** in `raw/` prima dell'uso.

## Filosofia — plan vs actual

Il flusso di allenamento è separato in due layer:

- **Plan** (immutabile una volta iniziato il ciclo) → `raw/programs/YYYY/<program>/`. Pattern **legacy import**: `companion.md` + binario originale del coach (ODS/PDF/foglio). Pattern **native** (programma scritto dall'utente): `companion.md` + `programma.yaml`.
- **Actual** (una entry per seduta) → `raw/journal/YYYY/<cartella del periodo>/` (`da <inizio> a <fine> <programma>/` per un microciclo, `da <inizio> a <fine>/` senza programma):
  - **File singolo** per default. Per i programmi: `YYYY-MM-DD W<settimana> <giornata>.md`, creato da `.github/scripts/genera_sedute.py` con serie da spuntare. I workout storici fino al 2026-10-10 vengono da LiftOff (dismesso).
  - **Cartella** solo se hai più artefatti nello stesso giorno: `YYYY-MM-DD/` che contiene più `.md` (es. `check_bilancia.md`, `sonno.md`) più eventuali binari.

Nei file generati `program`, `settimana`, `microciclo` e `giornata` sono già nel frontmatter. Formato, regole di compilazione e flusso git: `.github/instructions/wiki-conventions.instructions.md` § *Generatore delle sedute*.

Il vantaggio: `@wiki-reader` può incrociare piano ↔ esecuzione (es. *"quante sedute ho completato al 100 % del target vs sotto?"*), cosa impossibile con Google Sheet monolitici. Nel pattern legacy import il log di esecuzione è spesso già dentro il binario originale (colonna `Done` in un ODS, ecc.) — durante l'ingest il maintainer estrae la compliance dal binario e la mette nella program detail wiki.

## File presenti

| Template | Copia in | Uso |
|---|---|---|
| `raw_program_companion.md` | `raw/programs/YYYY/<program>/companion.md` | Programma legacy import (fonte esterna monolitica). |
| `raw_check_bilancia.md` | `raw/journal/YYYY/<cartella del periodo>/YYYY-MM-DD_check_bilancia.md` | Quando misuri la composizione corporea. |

I **workout non hanno template da copiare**: li crea il generatore delle sedute da `programma.yaml`. Per un programma native si parte da `raw_program_companion.md` (con `coach: self`) e si affianca un `programma.yaml` sul modello di `raw/programs/2026/2026-11-09_self_vena_aif/programma.yaml`.

## Uso da iPad

Obsidian iOS collegato al repo via git. Le sedute arrivano già generate col pull: si aprono, si spuntano le serie, si compilano `rpe::`/`note::`. Per i template rimanenti (`raw_program_companion.md`, `raw_check_bilancia.md`), dentro Obsidian apri il file, `Copy all` → nuovo file nel path di destinazione, sostituisci i placeholder `<...>`. In alternativa, usa il plugin **Templater** o **Templates** (core Obsidian) puntato a questa cartella.

## Regola di modifica

I template evolvono lentamente. Ogni modifica va discussa nel plan: se cambia un campo frontmatter, va aggiornata anche `.github/instructions/wiki-conventions.instructions.md` e le pagine wiki già ingerite che ne dipendono.
