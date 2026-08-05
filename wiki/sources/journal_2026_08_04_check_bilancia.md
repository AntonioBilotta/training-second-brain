---
type: source
creation_date: 2026-08-04
update_date: 2026-08-04
source_date: 2026-08-04
related_sources: []
tags:
  - journal
  - check
  - bilancia_impedenziometrica
  - composizione_corporea
---

# Check bilancia — 2026-08-04

## Provenienza

- Screenshot bilancia: `raw/journal/2026/2026-08-04/IMG_E0D5EAB82E6E-1.jpeg`
- Note contestuali: `raw/journal/2026/2026-08-04/check-bilancia`
- Rilevazione: **21:01 del 04/08/2026**, prima di cena, in un **rest day**.
- Utente: Antonio Bilotta.

> [!note] Note metodologiche
> - Pesatura serale (non a digiuno) → i valori di acqua corporea e grasso corporeo sono influenzati dal pasto/idratazione della giornata; utili per andamento, meno per confronto assoluto con letture mattutine a digiuno.
> - Giornata di riposo → nessun bias da glicogeno post-workout.
> - L'"età corporea" (biological age da BIA) mostrata dalla bilancia = 38, l'età anagrafica reale è **36** (37 compiuti a ottobre 2026); si tratta di un indice calcolato dall'algoritmo, non dell'anagrafica.

## Metriche rilevate

| Label sul display | Valore | Fascia dichiarata |
|---|---|---|
| Peso | 87,7 kg | Troppo alto |
| BMI | 29,0 | Troppo alto |
| Grasso corporeo | 16,8 % | Alto |
| Frequenza muscolare | 79,0 % | Fitness |
| Perdita di grasso | 73,0 kg | Eccellente |
| Grasso sottocutaneo | 13,7 % | Standard |
| Grasso viscerale | 11,4 | Alto |
| Acqua del corpo | 60,1 % | Standard |
| Muscolo scheletrico | 53,7 % | Standard |
| Massa muscolare | 69,3 kg | Eccellente |
| Massa ossea | 3,6 kg | Standard |
| Proteine | 19,0 % | Eccellente |
| BMR | 1946 kcal | — |
| Età corporea | 38 | — (anagrafica reale: 36) |

Vocabolario canonico e definizioni: [[composizione_corporea]].

## Traduzione di due label anomale

Due voci del display usano etichette non standard rispetto al vocabolario italiano consolidato delle bilance smart (cfr. l'elenco parametri riportato da [SmartWorld](https://www.smartworld.it/migliori-bilance-pesapersone), che cita esplicitamente *"frequenza muscolare scheletrica"* e *"massa magra"* come voci ufficiali).

> [!note] Traduzione — "Frequenza muscolare 79,0 %"
> Corrisponde alla **percentuale muscolare** (in inglese *muscle rate*): rapporto tra massa muscolare totale e peso corporeo. Il termine *frequenza* nasce dalla resa del *rate* inglese/cinese in accezione statistica.
> Verifica aritmetica: 69,3 kg / 87,7 kg = 79,02 % ✓
> È voce **distinta** da "Muscolo scheletrico 53,7 %", che indica la sola muscolatura scheletrica come sottoinsieme della massa muscolare totale.

> [!note] Traduzione — "Perdita di grasso 73,0 kg"
> Corrisponde alla **massa magra** (*fat-free mass*, FFM): peso corporeo al netto della massa grassa. La label "Perdita di grasso" è una traduzione errata (probabilmente dal cinese *去脂体重*, letteralmente "peso de-grassato"): non indica un obiettivo di dimagrimento, ma una quantità corrente.
> Verifica aritmetica: 87,7 kg × (1 − 0,168) = 72,97 ≈ 73,0 kg ✓

## Interpretazione sintetica

- **Peso e BMI** classificati "troppo alto" dall'algoritmo standard; il BMI non discrimina fra massa grassa e massa muscolare, quindi in soggetto allenato è indicatore parziale.
- **% grasso 16,8 %** (fascia "Alto" secondo la bilancia) in un contesto di massa muscolare 69,3 kg (fascia "Eccellente") e proteine 19,0 % (fascia "Eccellente") suggerisce composizione con buon patrimonio muscolare.
- **Grasso viscerale 11,4** (adimensionale, scala interna al produttore, tipicamente ≤ 9 desiderabile, 10–14 elevato): unica voce esplicitamente segnalata come "Alto" tra i parametri di adiposità.
- **BMR 1946 kcal** è la stima del metabolismo basale a riposo; utile come baseline per il calcolo del fabbisogno calorico giornaliero.

Tutti i valori sono un **singolo punto** di misurazione: acquistano significato solo con serie temporale ripetuta.

## Cross-reference

- Concetto ancora: [[composizione_corporea]]
