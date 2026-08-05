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
- `programs/` — **piani di allenamento** (immutabili una volta bloccati). Un sottofolder per programma con nome `snake_case` (es. `raw/programs/pl_prep_2026q4/`), contenente:
  - `README.md` — metadati del programma (obiettivi, date, mesocicli, 1RM iniziali).
  - `mesociclo_XX.md` — uno per mesociclo, con target `settimana × giornata` per le fondamentali e i complementari.
- `articles/` — articoli divulgativi o scientifici singoli (un file per articolo).
- `podcasts/` — appunti/trascrizioni di episodi podcast (un file per episodio).
- `courses/` — materiale strutturato di corsi, manuali o programmi multi-scheda. Un sottofolder per corso, con nome `snake_case` (es. `raw/courses/programmazione_forza_<autore>/`). Ogni sottofolder può contenere più file (PDF, note, slide) e opzionalmente un `README.md` con metadati del corso (autore, data, argomenti, licenza).
- `assets/` — immagini e allegati binari referenziati dalle pagine wiki (utili per materiale non legato a una giornata specifica).

### Templates

I seed per popolare `raw/` senza dover ricordare a memoria frontmatter e sezioni vivono in `.github/templates/` (meta, non contenuto wiki). Vanno **copiati** nella destinazione e poi editati.

| Template | Copia in | Uso |
|---|---|---|
| `raw_program_readme.md` | `raw/programs/<program>/README.md` | Uno per programma. |
| `raw_mesociclo.md` | `raw/programs/<program>/mesociclo_XX.md` | Uno per mesociclo. |
| `raw_workout.md` | `raw/journal/YYYY/YYYY-MM-DD/workout.md` | Uno per seduta. |
| `raw_check_bilancia.md` | `raw/journal/YYYY/YYYY-MM-DD/check_bilancia.md` | Quando misuri la composizione corporea. |

La modifica di un template va discussa nel plan e riflessa in questa istruzione + nelle pagine wiki già ingerite che ne dipendono.

### Pattern plan-vs-actual (programmi di allenamento)

Il flusso di allenamento è separato in due layer che rimangono sincronizzati tramite frontmatter:

- **Plan** → `raw/programs/<program>/{README.md, mesociclo_XX.md}` — prescrizioni target, immutabili una volta bloccato il mesociclo (le modifiche vanno tracciate nel diario delle modifiche dentro `README.md`).
- **Actual** → `raw/journal/YYYY/YYYY-MM-DD/workout.md` — esecuzione reale, con carichi/serie/RPE effettivi e note di seduta.

Il workout referenzia il piano tramite i campi frontmatter `program`, `mesociclo`, `settimana`, `giornata`. Questa separazione permette a `@wiki-reader` di rispondere a query che incrociano piano e esecuzione (es. *aderenza al target*, *scostamenti sistematici*, *milestone raggiunti/mancati*).

Ingest tipico:

- All'apertura di un nuovo mesociclo: `/wiki-ingest raw/programs/<program>/mesociclo_XX.md` → nuova source page + eventuale entità/concetto dedicato al programma.
- Dopo ogni seduta: `/wiki-ingest raw/journal/YYYY/YYYY-MM-DD/workout.md` → nuova source page journal.

## No ad-hoc changes

Modify `wiki/` **only** through the defined roles:

- `@wiki-maintainer` for INGEST (adding sources, updating derived pages).
- `@wiki-reader` for QUERY (may archive substantive answers in `wiki/analysis/`).
- `@wiki-auditor` for LINT (may repair frontmatter; may not edit page content).

Every change must be tracked in `wiki/log.md`. Do not fix small errors in passing — flag them for the next lint pass.

## Language

Write all wiki content in italian.
