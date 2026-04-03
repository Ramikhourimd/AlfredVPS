---
alfred_tags:
- telia'z/restructuring
- clinic/operations
- innovation/program
cluster_sources:
- '[[decision/Use Make.com for AI Model Evaluation Data Pipeline]]'
- '[[task/Build Staff Satisfaction Research Questionnaire]]'
- '[[task/Build Structured Employee Satisfaction Survey Instrument]]'
- '[[assumption/Automated Literature Review Pipeline Can Deliver Overnight Research
  Results]]'
confidence: medium
created: '2026-03-08'
janitor_note: 'LINK001 — Fixed: supports field wikilink corrected from "Structure
  Employee Experience Research Outputs as Academic Methodology" to "Structure Employee
  Experience Research as Academic Methodology" (extra word "Outputs" removed to match
  actual file). All other Telia''z wikilinks verified as YAML escaping false positives.
  Base view embeds (learn-synthesis.base) — systemic vault gap. ORPHAN001 — no inbound
  links.'
name: Innovation Program Automates Research Data Pipelines Rather Than Manual Analysis
project:
- '[[project/Telia''z Innovation Program]]'
related:
- '[[synthesis/Innovation Program Consistently Follows Research-First Pattern Before
  Building]]'
status: draft
supports:
- '[[decision/Structure Employee Experience Research as Academic Methodology]]'
type: synthesis
---

# Innovation Program Automates Research Data Pipelines Rather Than Manual Analysis

## Insight

Across every research workstream in the Innovation Program, Rami consistently builds automated data pipelines rather than relying on manual analysis. The AI model evaluation uses Make.com to extract patient data from Google Drive, run it through multiple AI models, and populate comparison spreadsheets. The staff satisfaction survey is designed around Google Sheets with automated processing to return structured findings. The literature review pipeline automates research question processing overnight. This is not coincidental — it represents a deliberate operational philosophy where research infrastructure is engineered for repeatability and scale before any analysis begins.

## Evidence

- **AI Model Evaluation**: Make.com automation extracts session data, routes through multiple AI models, populates evaluation tables (decision/Use Make.com for AI Model Evaluation Data Pipeline)
- **Staff Satisfaction Survey**: Google Sheets with "one research question per row" where "Rami will build automated processing to return structured findings" (task/Build Staff Satisfaction Research Questionnaire)
- **Literature Review**: Automated pipeline processes research questions from Google Sheets and returns literature review results overnight (assumption/Automated Literature Review Pipeline Can Deliver Overnight Research Results)

## Implications

- Research outputs are reproducible and scalable from first iteration
- Rami personally builds the automation tooling, creating a single-point dependency
- The pattern enables a small team (Rami + Rivi) to operate at research throughput levels that would normally require a larger team
- New research workstreams should expect an automation-build phase before data collection begins

## Applicability

Applies to all Innovation Program research and evaluation workstreams. Pattern should be considered when planning timelines — each new workstream requires upfront pipeline engineering before producing results.

![[learn-synthesis.base#Sources]]
![[learn-synthesis.base#Related]]