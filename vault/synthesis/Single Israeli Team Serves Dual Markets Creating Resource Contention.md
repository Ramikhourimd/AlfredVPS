---
alfred_tags:
- operations/israel-uk
- clinics/uk-expansion
- strategy/mvp
cluster_sources:
- '[[note/Telia''z Team Meeting UK Launch Patient Capacity and Recruitment 2026-02-15]]'
- '[[note/Telia''z Team Meeting UK Launch and Operations Review 2026-02-15]]'
- '[[task/Coordinate Israeli Case Manager Stopgap for UK Clinic]]'
- '[[task/Prepare UK Report Formats]]'
- '[[task/Define UK Prescription and Report Formats]]'
confidence: medium
created: '2026-03-03'
janitor_note: 'LINK001: Telia''z project wikilinks are valid — YAML single-quote escaping
  false positives. Base view embeds (learn-synthesis.base#*) reference _bases/ infrastructure
  not yet created (vault-wide gap). Note wikilinks verified present (both 2026-02-15
  meeting notes exist). ORPHAN001: no inbound links; consider linking from related
  constraint or project records.'
name: Single Israeli Team Serves Dual Markets Creating Resource Contention
project:
- '[[project/Telia''z UK Expansion]]'
- '[[project/Telia''z Clinic Israel]]'
related:
- '[[assumption/CMO Bandwidth Sufficient to Deliver All UK Clinical Specifications]]'
- '[[constraint/CMO Bandwidth Limits UK Clinical Pathway Design Progress]]'
relationships:
- confidence: 0.85
  context: Israel ops pattern replicated in UK
  source: synthesis/Single Israeli Team Serves Dual Markets Creating Resource Contention.md
  target: synthesis/UK Expansion Planning Replicates Israel Build-While-Flying Operational
    Pattern.md
  type: related-to
- confidence: 0.7
  context: Israel experience informs UK launch
  source: synthesis/Single Israeli Team Serves Dual Markets Creating Resource Contention.md
  target: synthesis/UK Launch Follows Deliberate Minimum Viable Clinic Strategy.md
  type: related-to
status: draft
supports:
- '[[constraint/CMO at Full Capacity Limits UK Clinical Design Bandwidth]]'
- '[[synthesis/UK Launch Has Multiple Converging Dependencies Creating Schedule Risk]]'
type: synthesis
---

# Single Israeli Team Serves Dual Markets Creating Resource Contention

## Insight

Across the February 2026 team meeting records, a clear pattern emerges: the same small Israeli team is simultaneously responsible for both Israel clinic operations and the UK market launch. This creates systematic resource contention that extends beyond the well-documented CMO capacity constraint to affect development, business development, operations, and clinical staffing.

## Evidence

- **Development (Stav Zamir):** UK-specific features (questionnaire, report formats, prescription system, admin views) are being added to the same product backlog that serves Israel platform development. No separate UK development team exists. UK items discussed in the regular 2:00 PM backlog meeting alongside Israel work.
- **Clinical Direction (Rami Khouri):** CMO defines clinical pathways, report formats, and SOPs for both Israel and UK simultaneously. Already flagged as at full capacity.
- **Business Development (Adiel Levin):** Manages Leon partnership, NHS CQC track, Susan/compliance conversations, and ongoing Israel business relationships concurrently.
- **Case Management (Bassem):** Identified as UK stopgap case manager while continuing Israeli case management duties. No additional headcount until UK patient volume is confirmed.
- **Operations (Li Yamin):** Handles UK insurance, Leon onboarding, and continuing Israel operational responsibilities.

## Implications

The dual-market resource model means any delay or escalation in Israel operations directly impacts UK launch readiness, and vice versa. This is not simply a scheduling risk (captured separately in convergence dependencies) but a structural organizational pattern where team capacity is the binding constraint across both markets. The March 31 launch date depends on this shared team delivering UK-specific work alongside their full Israel workload.

## Applicability

This pattern will likely repeat for any future international expansion (e.g., US, EU markets) unless Telia'z establishes dedicated country teams before launch. The current model works only if UK launch complexity remains low and Israel operations remain stable during the critical February-March 2026 window.

![[learn-synthesis.base#Sources]]
![[learn-synthesis.base#Related]]