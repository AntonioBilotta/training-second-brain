---
description: "Conventions for files in the LLM Wiki (`wiki/`) and sources in `raw/`. Covers YAML frontmatter, snake_case naming, Obsidian syntax (wikilinks, callouts), cross-reference discipline, and the `raw/` immutability rule. Auto-loaded when working on any file under wiki/** or raw/**."
applyTo: "wiki/**,raw/**"
---

# LLM Wiki — Conventions

These conventions apply to every file inside `wiki/` (LLM-maintained markdown) and `raw/` (immutable sources). They are auto-loaded by VS Code Copilot when working on matching files.

## Fundamental rule

**Never modify anything under `raw/`.** It is the user's immutable source of truth. Read from `raw/`; write only to `wiki/`.

## Wiki page format

Every page under `wiki/` (except `index.md` and `log.md`) must start with YAML frontmatter:

```yaml
---
type: entity | concept | source | analysis | goal | pattern | reflection
creation_date: YYYY-MM-DD   # date the page was created in the wiki
update_date: YYYY-MM-DD     # bumped on every edit
source_date: YYYY-MM-DD     # source pages only, optional: original publication date (used by lint stale-detection)
related_sources: []         # list of bare page names under wiki/sources/ (no `[[...]]` wrapping)
tags: []
---
```

`index.md` uses `type: index`; `log.md` has no frontmatter (append-only chronological log); `overview.md` uses `type: overview`.

> [!note] Date fields (`creation_date`, `update_date`, `source_date`) are written as ISO strings but a YAML parser (e.g. PyYAML `safe_load`) returns them as `datetime.date` objects, not strings. This is round-trip stable (ISO re-serializes identically). Consumers that compare dates should use date comparison, not string equality.

## Naming

- Use `snake_case` for all file names. Examples: `entity_name.md`, `key_concept.md`, `authentication_flow.md`.
- Use lowercase for tags and folder names.

## Obsidian conventions

- Internal links: `[[file_name]]` (no `.md` extension).
- Callouts: `> [!note]`, `> [!warning]`, `> [!important]`, `> [!tip]`.
- Contradictions between sources: `> [!warning] Contradiction: <detail>` on the affected page.
- Stale claims flagged by lint: `> [!warning] Stale: <detail>`.
- Images: place in `raw/assets/`, reference as `![[raw/assets/image_name.png]]`.
- Code blocks: use a language tag when possible (e.g. ` ```yaml `, ` ```bash `). Do not embed secrets, credentials, or API keys.

## Cross-reference discipline

- Always cite the source when writing a factual statement on a wiki page (link to the corresponding `wiki/sources/<name>` page).
- When updating a piece of data, check whether other pages report the same and update them together.
- When creating a page, add an entry to the appropriate section of `wiki/index.md` and append a line to `wiki/log.md`.

## Domain conventions

This wiki may contain personal or sensitive information. Treat all pages as personal-scope. When flagging emotional patterns, prefer descriptive language over diagnostic labels. Do not commit to a public git remote without review.

### `raw/` subfolders

- `journal/` — voci diario, una **cartella per giornata** con schema `raw/journal/YYYY/YYYY-MM-DD/` che contiene uno o più `.md` per tipo di entry:
  - `workout.md` — esecuzione della seduta (referenzia il piano via frontmatter).
  - `check_bilancia.md` — rilevazione bilancia impedenziometrica.
  - Altri `.md` liberi per note contestuali (es. `sonno.md`, `alimentazione.md`, `note_generiche.md`).
  - Eventuali allegati binari (screenshot, foto) restano nella stessa cartella-giornata.
- `programs/` — **piani di allenamento**, raggruppati per anno di inizio: `raw/programs/YYYY/YYYY-MM-DD_coach_slug_programma/`. Due pattern possibili:
  - **Native (authored nel wiki)**: programma scritto ex-novo usando i template. Struttura: `README.md` (metadati del programma) + `mesociclo_XX.md` (uno per mesociclo, con target `settimana × giornata` per fondamentali e complementari).
  - **Legacy import (fonte esterna)**: programma ricevuto in formato monolitico (ODS/PDF/foglio del coach). Struttura: `companion.md` (metadati + verdetto a posteriori + retest inline) + il binario originale (`.ods`, `.pdf`, ecc.) con il nome originale del file.
  I due pattern coesistono: usa native per programmi che scriverai giorno per giorno; usa legacy per programmi ricevuti già completi da un coach esterno.
- `articles/` — articoli divulgativi o scientifici singoli (un file per articolo).
- `podcasts/` — appunti/trascrizioni di episodi podcast (un file per episodio).
- `courses/` — materiale strutturato di corsi, manuali o programmi multi-scheda. Un sottofolder per corso, con nome `snake_case` (es. `raw/courses/programmazione_forza_<autore>/`). Ogni sottofolder può contenere più file (PDF, note, slide) e opzionalmente un `README.md` con metadati del corso (autore, data, argomenti, licenza).
- `assets/` — immagini e allegati binari referenziati dalle pagine wiki (utili per materiale non legato a una giornata specifica).

### Templates

I seed per popolare `raw/` senza dover ricordare a memoria frontmatter e sezioni vivono in `.github/templates/` (meta, non contenuto wiki). Vanno **copiati** nella destinazione e poi editati.

| Template | Copia in | Uso |
|---|---|---|
| `raw_program_readme.md` | `raw/programs/YYYY/<program>/README.md` | Programma native, uno per programma. |
| `raw_mesociclo.md` | `raw/programs/YYYY/<program>/mesociclo_XX.md` | Programma native, uno per mesociclo. |
| `raw_program_companion.md` | `raw/programs/YYYY/<program>/companion.md` | Programma legacy import (fonte esterna). |
| `raw_workout.md` | `raw/journal/YYYY/YYYY-MM-DD/workout.md` | Uno per seduta. |
| `raw_check_bilancia.md` | `raw/journal/YYYY/YYYY-MM-DD/check_bilancia.md` | Quando misuri la composizione corporea. |

La modifica di un template va discussa nel plan e riflessa in questa istruzione + nelle pagine wiki già ingerite che ne dipendono.

### Pattern plan-vs-actual (programmi di allenamento)

Il flusso di allenamento è separato in due layer che rimangono sincronizzati tramite frontmatter:

- **Plan** → `raw/programs/<program>/{README.md, mesociclo_XX.md}` — prescrizioni target, immutabili una volta bloccato il mesociclo (le modifiche vanno tracciate nel diario delle modifiche dentro `README.md`).
- **Actual** → `raw/journal/YYYY/YYYY-MM-DD/workout.md` — esecuzione reale, con carichi/serie/RPE effettivi e note di seduta.

Il workout referenzia il piano tramite i campi frontmatter `program`, `mesociclo`, `settimana`, `giornata`. Questa separazione permette a `@wiki-reader` di rispondere a query che incrociano piano e esecuzione (es. *aderenza al target*, *scostamenti sistematici*, *milestone raggiunti/mancati*).

Ingest tipico:

- All'apertura di un nuovo mesociclo (pattern native): `/wiki-ingest raw/programs/YYYY/<program>/mesociclo_XX.md` → source page + eventuale program detail.
- All'arrivo di un programma monolitico da coach esterno (pattern legacy): `/wiki-ingest raw/programs/YYYY/<program>/companion.md` → source page + program detail (vedi regola doppia-pagina sotto).
- Dopo ogni seduta: `/wiki-ingest raw/journal/YYYY/YYYY-MM-DD/workout.md` → nuova source page journal.

### Regola doppia-pagina per programmi

Ogni sorgente sotto `raw/programs/**` produce **due pagine wiki**:

1. **`wiki/sources/<slug>.md`** — scheda bibliografica (metadati, key points, provenance, cross-link). Prodotta automaticamente da `wiki-write-source-page` nel workflow di ingest standard.
2. **`wiki/programs/piano_<slug_ridotto>.md`** — struttura dettagliata del piano: progressione settimanale (tabelle %/schemi/carichi calcolati sui 1RM di ingresso), compliance calcolata dall'eventuale log di esecuzione, ausiliari, cross-link ai concetti e all'entità coach.

Naming: la source usa il nome pieno del programma (es. `programma_11_francesco_valente_2024`), il piano usa il prefisso `piano_` con lo slug ridotto per evitare collisioni di wikilink (es. `piano_programma_11_valente_2024`). Precedente analogo pattern nel vault: [[barbell_squat_routine]] (pattern) vs [[aif_2019_barbell_squat_routine]] (source).

Senza la program detail il programma è solo un riferimento bibliografico e non risulta queryable come struttura (schemi, compliance, confronti con altri programmi). Il `@wiki-maintainer` deve produrre entrambe le pagine in ogni ingest di un programma.

## No ad-hoc changes

Modify `wiki/` **only** through the defined roles:

- `@wiki-maintainer` for INGEST (adding sources, updating derived pages).
- `@wiki-reader` for QUERY (may archive substantive answers in `wiki/analysis/`).
- `@wiki-auditor` for LINT (may repair frontmatter; may not edit page content).

Every change must be tracked in `wiki/log.md`. Do not fix small errors in passing — flag them for the next lint pass.

## Language

Write all wiki content in italian.
