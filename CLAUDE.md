# Strength training, Powerlifting, Conditioning, Iron Log

Questa vault è una **LLM Wiki** (pattern Karpathy, vedi [`.github/karpathy_llm_wiki_pattern.md`](.github/karpathy_llm_wiki_pattern.md)). Questo file esiste perché Claude Code carica solo `CLAUDE.md`, non `AGENTS.md` né i file sotto `.github/` — quelli sono pensati per VS Code Copilot (`applyTo` glob-loading, chat-agent `@wiki-maintainer`/`@wiki-reader`/`@wiki-auditor`). Le regole sotto sono lo stesso contenuto, tradotto per il mio workflow a skill.

**Fonte di verità:** [`AGENTS.md`](AGENTS.md) e [`.github/instructions/wiki-conventions.instructions.md`](.github/instructions/wiki-conventions.instructions.md). Se questo file e quei due divergono, quelli vincono — segnalalo all'utente.

## Layout

- `raw/` — sorgenti **immutabili**. Scrive solo l'utente. **Non modificare mai** nulla sotto `raw/`. Unica eccezione: su richiesta dell'utente, `.github/scripts/genera_sedute.py` **crea** i file di seduta di un microciclo in `raw/journal/` (mai modifiche a file esistenti, salvo `--rigenera` su file intatti).
- `wiki/` — markdown LLM-maintained: `entities/`, `concepts/`, `sources/`, `analysis/`, `programs/`, più `index.md`, `log.md`, `overview.md`.
- `vault_path` autoritativo per le skill `wiki-*`: `/Users/antoniobilotta/Vaults/training-second-brain` (non rilevarlo camminando il filesystem).

## Mapping operazioni → skill

| Operazione | Skill da usare | Guardrail di dominio da applicare in aggiunta |
|---|---|---|
| INGEST (nuova fonte in `raw/`) | `wiki-ingest` | vedi §Maintainer |
| QUERY (domanda sulla wiki) | `wiki-query` | vedi §Reader |
| LINT (health-check) | `wiki-lint` | vedi §Auditor |

Non esistono i chat-agent `@wiki-maintainer/@wiki-reader/@wiki-auditor` fuori da Copilot: qui la "personalità di dominio" che loro applicano va rispettata a mano mentre uso le skill generiche.

## Convenzioni (sempre attive su `wiki/**` e `raw/**`)

- **Lingua: italiano** per tutto il contenuto wiki.
- Frontmatter YAML obbligatorio su ogni pagina (eccetto `index.md`/`log.md`): `type`, `creation_date`, `update_date`, `source_date` (solo sources), `related_sources`, `tags`.
- Naming `snake_case` per file, tag, cartelle.
- Wikilink `[[nome_file]]` (no `.md`), callout Obsidian `> [!note]`/`[!warning]`/`[!important]`/`[!tip]`; contraddizioni → `> [!warning] Contradiction: ...`; claim superati → `> [!warning] Stale: ...`.
- Ogni claim fattuale cita la fonte (`wiki/sources/<name>`); aggiornare un dato implica controllare e aggiornare le altre pagine che lo riportano.
- Ogni pagina nuova va registrata in `wiki/index.md` + una riga in `wiki/log.md`.
- **No ad-hoc changes**: non correggere errorini notati di passaggio — segnalarli per il prossimo lint invece di editarli al volo.

### Struttura `raw/`

- `journal/YYYY/` — voci diario e workout raggruppati per periodo: `da <inizio> a <fine> <programma>/` = un microciclo di programma (sedute `YYYY-MM-DD W<settimana> <giornata>.md`, create dal generatore e compilate da iPad); `da <inizio> a <fine>/` = periodo senza programma (workout liberi, note, misure). Nomi file sempre con la data come prefisso. Workout fino al 2026-10-10: plugin **LiftOff** (dismesso).
- `programs/YYYY/YYYY-MM-DD_coach_slug_programma/` — piani. Legacy import: `companion.md` + binario originale del coach. Native (scritto dall'utente): `companion.md` + `programma.yaml`.
- `articles/`, `podcasts/`, `courses/`, `assets/`.
- Template per popolare `raw/` in [`.github/templates/`](.github/templates/) (copiare, non editare in place).

### Pattern plan-vs-actual

- **Plan** → `raw/programs/<program>/{companion.md, binario | programma.yaml}`, immutabile una volta iniziato. `companion.md` porta `weekly_pattern` (weekday → giornata A/B/C/D).
- **Actual** → file di seduta in `raw/journal/`, creati dal generatore con `program`/`settimana`/`microciclo`/`giornata` già nel frontmatter. L'utente da iPad spunta le serie, corregge il numero sulla riga se cambia carico/rip, compila `rpe::`/`note::`/`stato`; seduta spostata → `stato: spostata` + `data_effettiva`, senza rinominare il file. Per workout storici/manuali i campi si derivano all'ingest da `date` + piano.
- **Ciclo di lavoro**: a ogni checkpoint di fine microciclo → ingest aggregato in `wiki/sources/journal_<program>_mc<N>.md` + aggiornamento plan-vs-actual nella program detail + generazione del microciclo successivo (Mac → push; iPad → pull). Dettagli: `.github/instructions/wiki-conventions.instructions.md` § *Generatore delle sedute*.

### Regola doppia-pagina per i programmi

Ogni sorgente sotto `raw/programs/**` produce **sempre due pagine**:
1. `wiki/sources/<slug>.md` — scheda bibliografica (standard, da `wiki-write-source-page`).
2. `wiki/programs/piano_<slug_ridotto>.md` — struttura dettagliata: 1RM ingresso/target/uscita, progressione settimanale, ausiliari, compliance se disponibile, cross-link a concetti/coach. **Va creata manualmente** dopo la source — dimenticarla riduce il programma a un semplice riferimento bibliografico, non interrogabile come struttura.

## §Maintainer (durante INGEST)

- Scrivere solo in `wiki/`, **mai in `wiki/analysis/`** (riservata alle query archiviate) e mai in `raw/`.
- Non inventare fatti: ogni scrittura deve risalire a una fonte `raw/` o a una pagina wiki già citata.
- Preferire linguaggio descrittivo a etichette diagnostiche per pattern emotivi/comportamentali (fatica, motivazione, recupero); non estrapolare diagnosi mediche/psicologiche dalle voci di diario.
- Redigere (omettere/anonimizzare) nomi di terzi (coach, training partner, familiari) se l'utente non ha dato consenso esplicito alla loro inclusione.
- Per i programmi: applicare sempre la regola doppia-pagina sopra.

## §Reader (durante QUERY)

- Mai inventare: se la risposta non è nella wiki né nelle fonti citate, dirlo e suggerire quale fonte colmerebbe il buco.
- Citare sempre con `[[nome_pagina]]`.
- Non modificare `raw/`; unico output scrivibile è l'archiviazione opzionale in `wiki/analysis/` (skill `wiki-write-analysis`, solo se l'utente approva/chiede `--archive`).

## §Auditor (durante LINT)

- Mai cancellare file unilateralmente: segnalare duplicati/orfani/pagine obsolete per approvazione.
- Mai creare nuove pagine di contenuto (compito del maintainer) né riscrivere prosa/ristrutturare contenuto.
- Può riparare solo frontmatter non ambiguo (`type`, `creation_date`, `update_date`, `related_sources`, `tags`) e aggiungere callout meta (`Contradiction:`, `Stale:`, `note`).

## Nota di privacy

Questa wiki può contenere informazioni personali o sensibili. Trattare ogni pagina come personal-scope. Non fare push su un remote pubblico senza revisione esplicita dell'utente.
