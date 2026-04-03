---
alfred_tags:
- telia'z/restructuring
- clinic/operations
- innovation/program
cluster_sources:
- '[[note/Telia''z Team Meeting UK Launch Patient Capacity and Recruitment 2026-02-15]]'
- '[[note/Telia''z Team Meeting UK Launch and Operations Review 2026-02-15]]'
- '[[task/Launch UK Google Ads Campaign After Contract Signing]]'
- '[[task/Build UK Prescription and Scheduling Features]]'
- '[[task/Obtain UK Professional Insurance Quote]]'
- '[[task/Prepare UK Report Formats]]'
confidence: medium
created: '2026-02-26'
janitor_note: 'LINK001 — Teliaz wikilinks (note and project references) are YAML-escape
  false positives. Note targets confirmed valid: Teliaz Team Meeting UK Launch Patient
  Capacity and Recruitment 2026-02-15, Teliaz Team Meeting UK Launch and Operations
  Review 2026-02-15.'
name: UK Launch Has Multiple Converging Dependencies Creating Schedule Risk
project:
- '[[project/Telia''z UK Expansion]]'
related:
- '[[constraint/Leon Contract Signing Is Critical Path for All UK Launch Activities]]'
- '[[constraint/UK Professional Insurance Required Before Clinic Launch]]'
- '[[constraint/UK Clinic Launch Requires Prescription System Not Yet Built]]'
- '[[constraint/Google Ads UK Requires Separate Approval for Healthcare Campaigns]]'
- '[[constraint/UK Clinical Report Formats Require Adaptation From Israel Templates]]'
relationships:
- confidence: 0.75
  context: UK launch depends on clinic pipeline
  source: synthesis/UK Launch Has Multiple Converging Dependencies Creating Schedule
    Risk.md
  target: synthesis/Clinic Growth Pipeline Has Three Sequential Bottlenecks Blocking
    Scale.md
  type: depends-on
- confidence: 0.8
  context: UK launch depends on recruitment
  source: synthesis/UK Launch Has Multiple Converging Dependencies Creating Schedule
    Risk.md
  target: synthesis/Recruitment Pipeline Has Sequential Dependencies Creating Compounding
    Delays.md
  type: depends-on
status: draft
supports:
- '[[assumption/March 2026 UK System Launch Timeline Is Achievable]]'
type: synthesis
---

# UK Launch Has Multiple Converging Dependencies Creating Schedule Risk

## Insight

The UK clinic launch requires at least seven independent workstreams to converge within approximately six weeks (mid-February to end of March 2026). Each workstream has its own blockers, owners, and timelines, but all must complete before the clinic can operate. This creates a compounding schedule risk where a delay in any single workstream cascades to the launch date.

## Evidence

From the February 15 team meeting and associated tasks, the following parallel dependencies were identified:

1. **Leon contract signing** — blocks all marketing and patient flow activities
2. **UK professional insurance** — must be in place before operations (Li Yamin obtaining quote)
3. **Prescription system** — flagged by Stav as critical and "more complex than other backlog items"
4. **Scheduling feature** — not yet scoped, essential for patient experience
5. **Clinical report format adaptation** — needs Stav/Rami coordination
6. **Google Ads UK approval** — separate from Israel, adds lag time after campaign submission
7. **Case manager preparation** — Basem needs Basel coordination 2 weeks before launch

No single owner is tracking the convergence of all seven streams. Individual owners (Adiel for contract, Li for insurance, Stav for product, Adi for marketing) each manage their track, but cross-stream dependency mapping is informal.

## Implications

- The March 31 system launch target assumes all seven streams complete on time — any single failure delays launch
- Prescription and scheduling features are the highest technical risk (flagged as complex, not yet scoped)
- A formal project timeline with cross-dependency tracking would reduce the risk of silent delays
- The team may benefit from a weekly dependency review focused specifically on UK launch readiness

## Applicability

This pattern of converging dependencies is likely to repeat for any future international clinic launch (the dual-track CQC strategy, local insurance, local report formats, local marketing approval). The UK launch serves as a template for understanding what convergence looks like.