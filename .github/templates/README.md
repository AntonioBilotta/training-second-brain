# Templates

Seed files per popolare `raw/` senza dover ricordare a memoria frontmatter e struttura. Sono **template**, non contenuti wiki: vivono in `.github/` (meta) e vanno **copiati** in `raw/` prima dell'uso.

## Filosofia — plan vs actual

Il flusso di allenamento è separato in due layer:

- **Plan** (immutabile una volta bloccato) → `raw/programs/<program>/`
  - `README.md` — metadati del programma (obiettivi, date, mesocicli).
  - `mesociclo_XX.md` — target per settimana × giornata (uno per mesociclo).
- **Actual** (una entry per seduta) → `raw/journal/YYYY/YYYY-MM-DD/`
  - `workout.md` — esecuzione reale, referenzia il piano tramite frontmatter (`program`, `mesociclo`, `settimana`, `giornata`).
  - `check_bilancia.md` — rilevazione bilancia impedenziometrica (opzionale, quando fatta).
  - Altri `.md` liberi per note contestuali della giornata (es. `sonno.md`, `alimentazione.md`).

Il vantaggio: `@wiki-reader` può incrociare piano ↔ esecuzione (es. *"quante sedute ho completato al 100 % del target vs sotto?"*), cosa impossibile con Google Sheet monolitici.

## File presenti

| Template | Copia in | Uso |
|---|---|---|
| `raw_program_readme.md` | `raw/programs/<program>/README.md` | Uno per programma. |
| `raw_mesociclo.md` | `raw/programs/<program>/mesociclo_XX.md` | Uno per mesociclo. |
| `raw_workout.md` | `raw/journal/YYYY/YYYY-MM-DD/workout.md` | Uno per seduta. |
| `raw_check_bilancia.md` | `raw/journal/YYYY/YYYY-MM-DD/check_bilancia.md` | Quando misuri la composizione corporea. |

## Uso da iPad

Working Copy + Obsidian iOS. Dentro Obsidian, apri il template, `Copy all` → nuovo file nel path di destinazione, sostituisci i placeholder `<...>`. In alternativa, usa il plugin **Templater** o **Templates** (core Obsidian) puntato a questa cartella.

## Regola di modifica

I template evolvono lentamente. Ogni modifica va discussa nel plan: se cambia un campo frontmatter, va aggiornata anche `.github/instructions/wiki-conventions.instructions.md` e le pagine wiki già ingerite che ne dipendono.
