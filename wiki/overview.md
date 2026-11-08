---
type: overview
creation_date: 2026-08-04
update_date: 2026-11-08
related_sources: []
tags: []
---

# Overview — Strength training, Powerlifting, Conditioning, Iron Log

**Type:** personal · **Description:** Wiki dedicata ad allenamento con sovraccarichi, forza, ipertrofia e body building, powerlifting, prestazioni e dieta.

## Knowledge state

| Metric | Count |
|--------|-------|
| Sources (journal / articles / podcasts / courses) | 13 |
| Entities | 1 |
| Concepts | 14 |
| Recurring patterns | 4 |
| Active goals | 0 |
| Reflections | 0 |
| Analyses | 0 |

> [!note] Primo ingest — AIF Master 2020
> Il primo materiale ingerito è il corso **[[aif]] MASTER PROGRAMMAZIONE — Parma 2020** (ipertrofia e forza), spacchettato in 12 pagine `wiki/sources/aif_master_2020_*` (una per lezione). Impianto concettuale iniziale: [[programmazione]], [[microciclo]], [[parametri_allenamento]], [[intensita_relativa]], [[controllo_motorio]], le tre fasi ([[fase_estensiva]] · [[fase_intensiva]] · [[taper]]), le tre fondamentali ([[squat]] · [[panca_piana]] · [[stacco_da_terra]]) e i pattern [[alternanza_stressante_stimolante_rigenerante]], [[metodo_cresco_facile]], [[milestone]], [[dente_di_sega]].

## How to use this wiki

- **INGEST** — drop a journal entry, article, or podcast note under `raw/` then run:
  ```
  /wiki-ingest raw/journal/2026-07-14.md
  ```
- **QUERY** — ask a question, get a cited answer:
  ```
  @wiki-reader "your question"
  ```
- **LINT** — periodic health-check:
  ```
  /wiki-lint
  ```

Any evolution of structure (new page types, new folders, new conventions) must be documented in `.github/instructions/wiki-conventions.instructions.md`. The root `copilot-instructions.md` stays a signpost — do not grow it.

## Flusso allenamento (piano ↔ esecuzione)

I programmi seguono il pattern **plan-vs-actual**:

- **Piano** → `raw/programs/<program>/`: `companion.md` + binario del coach (legacy import) oppure `companion.md` + `programma.yaml` (programma scritto dall'utente, es. [[piano_self_vena_aif_2026]]). Immutabile una volta iniziato.
- **Esecuzione** → `raw/journal/YYYY/da <inizio> a <fine> <programma>/YYYY-MM-DD W<settimana> <giornata>.md` (una cartella per microciclo): file di seduta creati un microciclo alla volta da `.github/scripts/genera_sedute.py`, con serie da spuntare e campi `rpe::`/`note::`. Dettagli in `.github/instructions/wiki-conventions.instructions.md` § *Generatore delle sedute*.
- I workout fino al 2026-10-10 vengono dal plugin LiftOff, dismesso il 2026-11-08.

## iPad + git

Obsidian iOS è collegato al repo remoto con un plugin git. Il Mac genera le sedute e fa push; l'iPad fa pull prima di allenarsi, compila il file della seduta e fa commit + push. Un file di seduta, una volta generato, si modifica solo da iPad.

## Life areas tracked

_Health, career, relationships, finances, creative work, learning. Adjust to what you actually track._

## Active goals

_Goals currently being pursued. Each has its own page under `wiki/goals/` with status, milestones, and related sources._

## Recurring patterns

_Behavioral or emotional patterns observed across journal entries. Each has its own page under `wiki/patterns/`._

## Key insights

_Reflections and syntheses. Each has its own page under `wiki/reflections/`._

> [!important] Sensitive data
> This wiki may contain personal or sensitive information. Do not commit to a public git repo without review. Consider a local-only workflow or a private repo.

## Suggested first questions

- Quali sono i principi di programmazione che ricorrono nelle fonti che ho ingerito su forza e ipertrofia?
- Come si concilia l'obiettivo powerlifting (massimali di squat, bench, deadlift) con la ricerca di massa muscolare secondo le fonti presenti nella wiki?
- Che indicazioni ho raccolto su volume settimanale, intensità e frequenza per gruppo muscolare?
- Quali strategie dietetiche (bulk, cut, ricomposizione, timing dei nutrienti) sono documentate e in quali contesti sono raccomandate?
- Quali pattern ricorrenti emergono dal mio journal di allenamento su recupero, sonno e prestazione?

## God pages

_High-centrality hub pages in the wiki graph. Populated by `@wiki-auditor` at the first `/wiki-lint` pass._

## Git & team

This vault is a plain git repo of markdown files. To start versioning (recommend a **private** remote):

```
git init && git add . && git commit -m "init llm wiki"
```

The included `.gitignore` excludes Obsidian cache/workspace files and OS junk (`.DS_Store`, `Thumbs.db`). Everything else — including `.obsidian/` settings, `raw/`, and `wiki/` — is committed by default.
