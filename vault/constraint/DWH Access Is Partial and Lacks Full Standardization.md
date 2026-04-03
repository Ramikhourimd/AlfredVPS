---
alfred_tags:
- clinical-data/constraints
- ai-research/limitations
authority: Data architecture
created: '2026-02-25'
janitor_note: 'LINK001 — base view embeds (learn-constraint.base#Affected Projects,
  #Related) reference _bases/learn-constraint.base which does not exist yet. Create
  the base file to enable dynamic views. Telia''z wikilinks are valid — scanner false
  positive from YAML single-quote escaping.'
name: DWH Access Is Partial and Lacks Full Standardization
project:
- '[[project/Telia''z AI Clinical Platform]]'
related:
- '[[conversation/Product Meeting Report Logic API and AI Architecture]]'
- '[[note/Product Meeting Report Logic API and AI Architecture 2026-02-25]]'
- '[[decision/Implement Read-Only Shadow DB for Analytics]]'
- '[[conversation/Retool Improvements and Data Access Planning 2025-12-05]]'
- '[[conversation/Retool System Priorities and Data Access Discussion 2025-12-05]]'
source: Product meeting technical discussion
source_date: '2026-02-25'
status: active
type: constraint
---

# DWH Access Is Partial and Lacks Full Standardization

## Constraint

Access to datasets in the Data Warehouse (BigQuery/DWH) is incomplete and not fully standardized. Pricing tables and meeting views exist but their locations need verification. Large queries require pagination to prevent failures.

## Source

Technical discussion at product meeting revealing current DWH limitations.

## Implications

- Pricing data for clinic reports must be fetched from DWH via verified table/view paths
- All DWH queries need pagination support to avoid payload and timeout failures
- Cannot rely on DWH for real-time data needs — analytics only
- Engineering needs to verify and document available DWH tables

## Expiry / Review

Active until DWH access is fully documented and standardized APIs are in place.

![[learn-constraint.base#Affected Projects]]
![[learn-constraint.base#Related]]