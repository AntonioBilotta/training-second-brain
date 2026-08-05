---
date: YYYY-MM-DD
program: <program_snake_case>
mesociclo: <01 | 02 | ...>
settimana: <1 | 2 | 3 | 4>
giornata: <A | B | C | D>
giornata_focus: <es. Lower forza — Squat>
fase: <estensiva | intensiva | taper | scarico>
durata_min: <numero>
sensazione_rpe: <1-10 — quanto è stata dura complessivamente>
sonno_ore: <numero, notte precedente>
peso_kg: <se pesato al mattino>
pre_workout_kcal: <opzionale>
tags:
  - journal
  - workout
---

# Workout — YYYY-MM-DD — <giornata_focus>

## Contesto

- **Programma**: `<program>` mesociclo `<XX>` settimana `<N>` giornata `<X>`
- **Orario**: <inizio - fine>
- **Luogo**: <palestra / home gym>
- **Stato di partenza**: <es. bene / affaticato / dolore residuo>

## Esercizi

| # | Esercizio | Target | Set | Carico (kg) | Rip | RPE | Note |
|---|---|---|---|---|---|---|---|
| 1 | Squat | 4×6 @ 77,5 % | 1 | | | | riscaldamento incrementale |
| 1 | Squat | | 2 | | | | |
| 1 | Squat | | 3 | | | | |
| 1 | Squat | | 4 | | | | |
| 2 | Stacco rumeno | 3×8 | 1 | | | | |
| 2 | | | 2 | | | | |
| 2 | | | 3 | | | | |
| 3 | Leg press | 3×10 | 1 | | | | |
| 3 | | | 2 | | | | |
| 3 | | | 3 | | | | |

Legenda:
- **Target** = prescrizione dal piano ([[<mesociclo>]]).
- **RPE** = *Rate of Perceived Exertion*, 1-10 (10 = massimale).
- Se ripetuta la scheda su più esercizi, ripetere il nome nella prima colonna solo per la prima serie di ogni blocco.

## Note di seduta

- <es. squat sensazione ottima, potevo caricare di più>
- <es. leg press: dolore ginocchio destro all'ultima serie, ridotto peso>
- <es. sostituito stacco rumeno con good morning per problema alla schiena>

## Rispetto del piano

- **Volume completato**: <es. 100 % / 90 % / rimodulato>
- **Scostamenti dal target**: <lista deviazioni intenzionali>

## Post-seduta

- Recupero soggettivo (1-10): <>
- Idratazione (litri): <>
- Aggiungere check bilancia domani? <sì / no>

## Cross-reference

- Piano: `raw/programs/<program>/mesociclo_XX.md`
- Seduta precedente: `raw/journal/YYYY/YYYY-MM-DD/workout.md`
