---
account: null
acquired: null
alfred_tags:
- clinic-israel/executive-dashboard
asset_type: software
cost: null
created: '2026-02-25'
description: HTML/CSS/JS prototype for Clinic Israel executive operations dashboard
  with four KPI cards, glass-morphism design, RTL Hebrew layout, and demo data
janitor_note: LINK001 — Telia'z wikilinks are valid (YAML escaping false positive).
  Base view embed (asset.base#Related) references _bases/asset.base which does not
  exist — vault-wide structural issue.
location: null
name: Clinic Executive Dashboard Variant B
owner: '[[person/Rami Khouri]]'
project: '[[project/Telia''z Clinic Israel]]'
related:
- '[[note/Clinic Israel Executive Dashboard Design Variant B]]'
- '[[decision/Four Core KPI Targets for Clinic Operations Dashboard]]'
- '[[asset/Clinic Israel Flow Dashboard]]'
- '[[asset/Clinic Flow Dashboard]]'
- '[[asset/Clinic Flow Dashboard v4]]'
relationships:
- confidence: 0.95
  context: Variant B of base dashboard
  source: asset/Clinic Executive Dashboard Variant B.md
  target: asset/Clinic Executive Dashboard.md
  type: related-to
- confidence: 0.9
  context: Israel version of Variant B
  source: asset/Clinic Executive Dashboard Variant B.md
  target: asset/Clinic Israel Executive Dashboard Variant B.md
  type: related-to
renewal_date: null
status: active
tags: []
type: asset
vendor: '[[org/Telia''z]]'
---

# Clinic Executive Dashboard Variant B

## Details

Static HTML prototype (single-file, no build dependencies) for the Clinic Israel executive operations dashboard. Tracks four core KPIs: intake conversion, attendance rate, case manager wait times, and appointment slot availability. Contains hardcoded demo data — requires API integration for production use.

- **Format:** Single HTML file with embedded CSS and JavaScript
- **Source file:** `inbox/processed/dashboard3.html`
- **Design variant:** B (implies at least one other variant exists)
- **Language:** Hebrew (RTL)

## Related
![[asset.base#Related]]