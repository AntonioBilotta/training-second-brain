# Templates

Seed files per popolare `raw/` senza dover ricordare a memoria frontmatter e struttura. Sono **template**, non contenuti wiki: vivono in `.github/` (meta) e vanno **copiati** in `raw/` prima dell'uso.

## Filosofia — plan vs actual

Il flusso di allenamento è separato in due layer:

- **Plan** (immutabile una volta ricevuto il ciclo dal coach) → `raw/programs/YYYY/<program>/`. Solo pattern **legacy import**: `companion.md` (metadati + `weekly_pattern` + verdetto a posteriori + retest inline) + il binario originale con il suo nome di origine (ODS/PDF/foglio del coach).
- **Actual** (una entry per seduta o più file quando serve) → `raw/journal/YYYY/`:
  - **File singolo** per default: `YYYY-MM-DD <titolo>.md` — generato dal plugin **LiftOff** su iPad/Obsidian, contiene frontmatter con esercizi/set strutturati e tabelle markdown.
  - **Cartella** solo se hai più artefatti nello stesso giorno: `YYYY-MM-DD/` che contiene più `.md` (es. `check_bilancia.md`, `sonno.md`) più eventuali binari.

Al workout LiftOff aggiungi manualmente due campi frontmatter per abilitare il collegamento al piano:

- `program: <program_snake_case>` — obbligatorio.
- `giornata: <A|B|C|D>` — solo se la seduta è shiftata rispetto al `weekly_pattern` del piano (es. seduta del lunedì eseguita martedì).

`mesociclo` e `settimana` sono derivati automaticamente al momento dell'ingest da `date` + `program.start_date`; `giornata` da `weekday(date)` se non specificata.

Il vantaggio: `@wiki-reader` può incrociare piano ↔ esecuzione (es. *"quante sedute ho completato al 100 % del target vs sotto?"*), cosa impossibile con Google Sheet monolitici. Nel pattern legacy import il log di esecuzione è spesso già dentro il binario originale (colonna `Done` in un ODS, ecc.) — durante l'ingest il maintainer estrae la compliance dal binario e la mette nella program detail wiki.

## File presenti

| Template | Copia in | Uso |
|---|---|---|
| `raw_program_companion.md` | `raw/programs/YYYY/<program>/companion.md` | Programma legacy import (fonte esterna monolitica). |
| `raw_check_bilancia.md` | `raw/journal/YYYY/YYYY-MM-DD_check_bilancia.md` oppure `raw/journal/YYYY/YYYY-MM-DD/check_bilancia.md` | Quando misuri la composizione corporea. |

I **workout non hanno template**: li produce il plugin **LiftOff** su iPad/Obsidian direttamente in `raw/journal/`. Sul desktop apri il file generato, aggiungi `program:` (e opzionalmente `giornata:`) al frontmatter, poi passa all'ingest.

I template per il pattern "native" (programma scritto ex-novo con `README.md` + `mesociclo_XX.md`) sono stati rimossi: al momento tutti i programmi arrivano da coach esterni in formato monolitico. Se emergerà il bisogno di scriversi un programma da zero, si valuterà caso per caso.

## Uso da iPad

Working Copy + Obsidian iOS. Il plugin **LiftOff** è il modo canonico di generare i workout in `raw/journal/`. Per i template rimanenti (`raw_program_companion.md`, `raw_check_bilancia.md`), dentro Obsidian apri il file, `Copy all` → nuovo file nel path di destinazione, sostituisci i placeholder `<...>`. In alternativa, usa il plugin **Templater** o **Templates** (core Obsidian) puntato a questa cartella.

## Regola di modifica

I template evolvono lentamente. Ogni modifica va discussa nel plan: se cambia un campo frontmatter, va aggiornata anche `.github/instructions/wiki-conventions.instructions.md` e le pagine wiki già ingerite che ne dipendono.
