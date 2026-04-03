---
alfred_tags:
- clinical-data/constraints
- ai-research/limitations
authority: Data quality review
created: '2026-02-26'
janitor_note: 'LINK001 — Telia''z project link is valid (YAML single-quote escaping
  false positive). Base view embeds (learn-constraint.base#Affected Projects, #Related)
  reference _bases/learn-constraint.base which does not exist. Create it to enable
  dynamic views. ORPHAN001 — no inbound wikilinks; consider linking from project/Telia''z
  AI Clinical Platform.'
location: []
name: Open Test Sessions Cannot Be Reliably Identified Without Manual Review
project:
- '[[project/Telia''z AI Clinical Platform]]'
related:
- '[[note/Product Meeting Report Logic API and AI Architecture 2026-02-25]]'
- '[[task/Clean Open and Test Sessions From Reports]]'
- '[[constraint/Clinical Dataset Contains Noise Requiring Statistical Cleaning]]'
source: Product meeting analysis
source_date: '2026-02-25'
status: active
tags: []
type: constraint
---

# Open Test Sessions Cannot Be Reliably Identified Without Manual Review

## Constraint

Sessions that were left open or created as test sessions during system setup cannot be reliably distinguished from legitimate clinical sessions through automated means. Their status (open, test, or genuinely incomplete) requires manual intervention to determine.

## Source

Identified during the product meeting on 2026-02-25 as part of the data quality discussion. These sessions contaminate reports and analytics.

## Implications

- Automated report generation will include false positives unless a manual review or tagging step is added
- The reporting pipeline needs either a manual review gate or heuristic-based filtering
- Historical data before March 10 is particularly affected (mostly test data per existing assumption)
- Affects accuracy of KPIs, session counts, and utilization metrics

## Expiry / Review

May be resolved once a session status tagging mechanism is implemented or after the initial dataset is manually cleaned.

![[learn-constraint.base#Affected Projects]]
![[learn-constraint.base#Related]]