---
program: test_ipad_2026
tipo: forza_generale
data_inizio: 2026-08-06
data_fine_prevista: 2026-10-25
gara_target: null
mesocicli:
  - 01_estensiva
  - 02_intensiva
  - 03_taper
sedute_settimana: 4
1rm_iniziali:
  squat: 175
  panca: 125
  stacco: 190
obiettivi:
  - test del workflow plan-vs-actual da iPad (Obsidian + Fit)
  - rientro strutturato dopo periodo destrutturato — priorità: controllo motorio e continuità
  - milestone squat 4×6 @ 80 % (140 kg) entro fine mesociclo 01
note_metodologiche: >
  Impostazione AIF (fase estensiva → intensiva → taper). I 1RM iniziali sono
  stime storiche non recentemente verificate (vedi [[journal_2026_08_05_massimali]]);
  vanno usati come ordine di grandezza e ricalibrati settimana 1-2 con RPE reali
  ([[metodo_cresco_facile]]).
tags:
  - program
---

# Programma — Test iPad 2026 (forza generale, rientro strutturato)

## Contesto

- **Obiettivo generale**: testare in produzione il workflow di pianificazione + esecuzione da iPad (Obsidian + plugin Fit per sync GitHub), su un blocco di forza generale di 12 settimane pensato per un rientro dopo un periodo non strutturato.
- **Struttura**: 3 mesocicli da 4 settimane (12 settimane totali).
- **Frequenza**: 4 sedute/settimana (2 lower + 2 upper).
- **Riferimenti**: [[aif_master_2020_09_le_fasi_del_ciclo]], [[aif_master_2020_10_fase_estensiva]], [[aif_master_2020_11_fase_intensiva]], [[aif_master_2020_12_taper]], [[metodo_cresco_facile]].

## Mesocicli

| # | Nome | Fase | Data inizio | Data fine | Focus |
|---|---|---|---|---|---|
| 01 | Estensiva | controllo motorio + ricondizionamento | 2026-08-06 | 2026-09-02 | volume alto, IR 65-77,5 %, RPE 6-8 |
| 02 | Intensiva | progressione carichi | 2026-09-03 | 2026-09-30 | 77,5-87,5 %, RPE 7-9 |
| 03 | Taper | specificità pre-test massimale | 2026-10-01 | 2026-10-25 | -30 % volume, ricerca picco |

## Massimali di riferimento

| Alzata | 1RM iniziale (kg) | 1RM target (kg) | Data test iniziale | Fonte |
|---|---|---|---|---|
| Squat | 175 | 185 | 2026-08-05 (stima storica) | [[journal_2026_08_05_massimali]] |
| Panca | 125 | 130 | 2026-08-05 (stima storica) | [[journal_2026_08_05_massimali]] |
| Stacco | 190 | 200 | 2026-08-05 (stima storica) | [[journal_2026_08_05_massimali]] |

> [!warning] Massimali non verificati
> Sono valori calcolati mesi prima. La settimana 1 va usata per **ricalibrare** l'IR sui carichi reali usando RPE (metodo cresco facile). Se la sensazione RPE dei carichi target si discosta di ≥ 1 punto dal previsto, aggiornare i 1RM di riferimento nella tabella qui sopra.

## Regole del programma

- **RPE > 9 per 2 settimane consecutive** → deload -40 % volume la settimana successiva.
- **Dolore acuto** su un fondamentale → stop dell'alzata, non della seduta; sostituzione con variante meno stressante documentata in `note_metodologiche` del workout.
- **Salta seduta** → NON recuperare spostando in un altro giorno se richiede 3 sedute in 3 giorni consecutivi. Segna "seduta saltata" nel journal e prosegui.
- **Check bilancia**: lunedì mattina a digiuno, prima della seduta A. Documentare in `check_bilancia.md` nella stessa cartella journal del giorno.
- **Massimali**: NON testare 1RM reali durante mesociclo 01 e 02. Il test è nel taper (mesociclo 03).

## Diario delle modifiche al piano

| Data | Modifica | Motivazione |
|---|---|---|
| 2026-08-06 | Creazione del piano | Test workflow iPad + rientro strutturato |
