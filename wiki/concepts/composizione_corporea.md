---
type: concept
creation_date: 2026-08-04
update_date: 2026-08-04
related_sources:
  - journal_2026_08_04_check_bilancia
tags:
  - composizione_corporea
  - bilancia_impedenziometrica
  - misurazione
---

# Composizione corporea

Pagina ancora per il vocabolario canonico delle metriche di composizione corporea rilevate tramite bilancia impedenziometrica (BIA — *bioelectrical impedance analysis*). Le fonti journal `check_bilancia_*` devono usare o mappare a questi termini.

## Metriche di base

- **Peso corporeo** — kg. Massa totale del soggetto in condizioni standardizzate (idealmente mattino, a digiuno, dopo minzione).
- **BMI** (*Body Mass Index*) — kg/m². $\text{BMI} = \text{peso} / \text{altezza}^2$. Non discrimina fra massa grassa e magra; in soggetti muscolarmente sviluppati sovrastima il "sovrappeso".
- **BMR** (*Basal Metabolic Rate*) — kcal/giorno. Metabolismo basale stimato: dispendio energetico a riposo, in condizioni di neutralità termica, digiuno post-assorbitivo. È il pavimento del fabbisogno energetico giornaliero.

## Adiposità

- **Percentuale grasso corporeo** (*body fat percentage*) — %. Massa grassa totale rispetto al peso.
- **Grasso sottocutaneo** — %. Frazione di massa grassa depositata sotto la pelle.
- **Grasso viscerale** — indice adimensionale (scala interna al produttore). Stima del grasso attorno agli organi addominali; correlato a rischio cardiometabolico. Non confondere con i kg di grasso sottocutaneo.

## Massa magra e muscolare

- **Massa magra** (*fat-free mass*, FFM) — kg. Peso corporeo al netto della massa grassa. Comprende muscoli, ossa, organi, acqua corporea. È distinta dalla sola massa muscolare.
  - Alcune bilance mostrano questa voce con label anomala "Perdita di grasso" — è un errore di traduzione, non un target di dimagrimento. Cfr. [[journal_2026_08_04_check_bilancia]].
- **Massa muscolare** — kg. Muscolatura totale (scheletrica + liscia + cardiaca, o solo scheletrica secondo il modello dell'algoritmo).
- **Percentuale muscolare** (*muscle rate*) — %. Rapporto massa muscolare / peso totale. In alcune bilance in italiano compare come "**Frequenza muscolare**" (traduzione statistica di *rate*).
- **Muscolo scheletrico** — % o kg. Frazione della sola muscolatura scheletrica sul peso totale; sottoinsieme della massa muscolare.
- **Massa ossea** — kg. Contenuto minerale osseo stimato. Cambia molto lentamente nel tempo.
- **Proteine** — %. Stima della quota proteica del corpo, per lo più contenuta nella massa muscolare e negli organi.

## Idratazione

- **Acqua corporea totale** (*total body water*) — %. Percentuale di acqua sul peso totale. Fortemente influenzata da orario della misurazione, sudorazione, pasti, carboidrati.

## Indicatori derivati

- **Età corporea** / **età biologica** — indice adimensionale calcolato dall'algoritmo del produttore combinando i parametri precedenti. Non coincide con l'età anagrafica; ha valore solo comparativo nel tempo, non assoluto.

## Cautele interpretative

- Ogni bilancia impedenziometrica applica un **algoritmo proprietario** che stima le voci non peso a partire dall'impedenza corporea, altezza, sesso, età. Valori assoluti tra bilance diverse **non sono direttamente confrontabili**.
- Le rilevazioni sono comparabili solo se **standardizzate**: stesso orario, stessa idratazione, stessa alimentazione precedente. Una singola misurazione è un punto, non un trend.
- Le fasce ("Alto", "Standard", "Eccellente", "Troppo alto") mostrate dalla bilancia derivano da tabelle interne al produttore, non da linee guida cliniche universali.
- Le label italiane di alcune bilance sono traduzioni imperfette dal cinese/inglese. Documentare label anomale nelle rispettive source page e mappare al vocabolario canonico di questa pagina.

## Cross-reference

- Fonti che citano queste metriche: [[journal_2026_08_04_check_bilancia]]
