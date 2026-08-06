# Templates

Seed files per popolare `raw/` senza dover ricordare a memoria frontmatter e struttura. Sono **template**, non contenuti wiki: vivono in `.github/` (meta) e vanno **copiati** in `raw/` prima dell'uso.

## Filosofia — plan vs actual

Il flusso di allenamento è separato in due layer:

- **Plan** (immutabile una volta bloccato) → `raw/programs/YYYY/<program>/`. Due pattern:
  - **Native** (programma scritto ex-novo nel wiki): `README.md` (metadati) + `mesociclo_XX.md` (uno per mesociclo, target per settimana × giornata).
  - **Legacy import** (programma ricevuto in formato monolitico da coach esterno, es. ODS/PDF): `companion.md` (metadati + verdetto a posteriori + retest inline) + il binario originale con il suo nome di origine.
- **Actual** (una entry per seduta) → `raw/journal/YYYY/YYYY-MM-DD/`
  - `workout.md` — esecuzione reale, referenzia il piano tramite frontmatter (`program`, `mesociclo`, `settimana`, `giornata`).
  - `check_bilancia.md` — rilevazione bilancia impedenziometrica (opzionale, quando fatta).
  - Altri `.md` liberi per note contestuali della giornata (es. `sonno.md`, `alimentazione.md`).

Il vantaggio: `@wiki-reader` può incrociare piano ↔ esecuzione (es. *"quante sedute ho completato al 100 % del target vs sotto?"*), cosa impossibile con Google Sheet monolitici. Nel pattern legacy import il log di esecuzione è spesso già dentro il binario originale (colonna `Done` in un ODS, ecc.) — durante l'ingest il maintainer estrae la compliance dal binario e la mette nella program detail wiki.

## File presenti

| Template | Copia in | Uso |
|---|---|---|
| `raw_program_readme.md` | `raw/programs/YYYY/<program>/README.md` | Programma native, uno per programma. |
| `raw_mesociclo.md` | `raw/programs/YYYY/<program>/mesociclo_XX.md` | Programma native, uno per mesociclo. |
| `raw_program_companion.md` | `raw/programs/YYYY/<program>/companion.md` | Programma legacy import (fonte esterna monolitica). |
| `raw_workout.md` | `raw/journal/YYYY/YYYY-MM-DD/workout.md` | Uno per seduta. |
| `raw_check_bilancia.md` | `raw/journal/YYYY/YYYY-MM-DD/check_bilancia.md` | Quando misuri la composizione corporea. |

## Uso da iPad

Working Copy + Obsidian iOS. Dentro Obsidian, apri il template, `Copy all` → nuovo file nel path di destinazione, sostituisci i placeholder `<...>`. In alternativa, usa il plugin **Templater** o **Templates** (core Obsidian) puntato a questa cartella.

## Regola di modifica

I template evolvono lentamente. Ogni modifica va discussa nel plan: se cambia un campo frontmatter, va aggiornata anche `.github/instructions/wiki-conventions.instructions.md` e le pagine wiki già ingerite che ne dipendono.
