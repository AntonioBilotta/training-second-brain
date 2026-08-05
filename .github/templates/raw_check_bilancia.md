---
date: YYYY-MM-DD
orario: HH:MM
condizioni: <mattino_digiuno | sera_pre_cena | post_workout | altro>
giorno_tipo: <rest_day | training_day | post_gara>
screenshot: raw/journal/YYYY/YYYY-MM-DD/<nome_file>.jpeg
bilancia_modello: <es. Xiaomi Mi Body S400, Renpho Elis 1, ...>
tags:
  - journal
  - check
  - bilancia_impedenziometrica
  - composizione_corporea
---

# Check bilancia — YYYY-MM-DD

## Contesto

- **Data / orario**: YYYY-MM-DD HH:MM
- **Condizioni**: <mattino a digiuno / sera prima di cena / post-workout>
- **Giorno**: <rest day / dopo seduta X / gara>
- **Note**: <es. sonno insufficiente / dopo carboidrati / gonfiore percepito>

## Metriche

| Metrica canonica ([[composizione_corporea]]) | Label sul display | Valore | Fascia dichiarata |
|---|---|---|---|
| Peso | Peso | | |
| BMI | BMI | | |
| Percentuale grasso | Grasso corporeo | % | |
| Percentuale muscolare | Frequenza muscolare | % | |
| Massa magra | Perdita di grasso | kg | |
| Grasso sottocutaneo | Grasso sottocutaneo | % | |
| Grasso viscerale | Grasso viscerale | (adim.) | |
| Acqua corporea | Acqua del corpo | % | |
| Muscolo scheletrico | Muscolo scheletrico | % | |
| Massa muscolare | Massa muscolare | kg | |
| Massa ossea | Massa ossea | kg | |
| Proteine | Proteine | % | |
| BMR | BMR | kcal | |
| Età biologica | Età corporea | | |

> [!note] Label anomale del produttore
> Se la bilancia usa *"Frequenza muscolare"* al posto di *percentuale muscolare* e *"Perdita di grasso"* al posto di *massa magra*, mantenere entrambe le colonne (label sul display + metrica canonica) per fedeltà alla fonte. Verifica: `massa_muscolare / peso = percentuale_muscolare` e `peso × (1 - percentuale_grasso) = massa_magra`. Cfr. [[journal_2026_08_04_check_bilancia]].

## Cambio rispetto al check precedente

| Metrica | Precedente | Attuale | Δ | Δ % |
|---|---|---|---|---|
| Peso | | | | |
| % grasso | | | | |
| Massa muscolare | | | | |
| Massa magra | | | | |

Data check precedente: `raw/journal/YYYY/YYYY-MM-DD/check_bilancia.md`.

## Interpretazione soggettiva

- <es. calo peso di 0,4 kg, mantenuta massa muscolare → cut in linea>
- <es. sale la % di acqua ma non il peso → possibile deplezione glicogeno>
