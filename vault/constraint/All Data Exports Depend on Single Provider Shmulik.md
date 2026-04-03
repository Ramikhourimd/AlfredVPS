---
alfred_tags:
- clinical-data/constraints
- ai-research/limitations
authority: Telia'z organizational data access structure
created: '2026-03-03'
janitor_note: LINK001 flagged on [[project/Telia'z AI Diagnostic Research Paper]]
  is a false positive — apostrophe in Telia'z is valid vault content, not a YAML escaping
  issue. No action needed.
name: All Data Exports Depend on Single Provider Shmulik
project:
- '[[project/Telia''z AI Diagnostic Research Paper]]'
related:
- '[[conversation/AI Diagnostic Paper Methodology Review Meeting 2026-02-22]]'
- '[[conversation/AI Diagnostic Paper Progress Meeting 2026-02-22]]'
- '[[task/Investigate Dataset Size Discrepancy Between Excel Exports]]'
- '[[task/Request Segmented Timing Data From Shmulik]]'
- '[[task/Get 8-Column Timing Breakdown From Shmulik]]'
- '[[task/Prepare Eight Column Timing Data Export]]'
- '[[person/Shmulik]]'
- '[[contradiction/Patient Dataset Record Count Discrepancy Between Exports]]'
source: Multiple task records and meeting conversations from 2026-02-22
source_date: '2026-02-22'
status: active
type: constraint
---

# All Data Exports Depend on Single Provider Shmulik

## Constraint

All patient data exports required for the AI diagnostic research paper must be obtained through Shmulik. No other team member has been identified as having the access or capability to generate these database exports.

## Source

Multiple task records and conversations from the 2026-02-22 research meetings reference Shmulik as the sole data provider. Tasks including dataset reconciliation, timing data segmentation (8-column breakdown), and outlier-cleaned exports all list Shmulik as the required action party.

## Implications

Any data request creates a sequential dependency on Shmulik's availability and workload. Multiple concurrent data requests (8-column timing breakdown, dataset discrepancy investigation, cleaned outlier data) compete for one person's bandwidth. This bottleneck affects the paper's timeline, particularly when new analysis requirements emerge during review meetings. The dataset record count discrepancy (6,041 vs ~5,700) also requires Shmulik's investigation.

## Expiry / Review

Active until paper publication or until additional team members gain data export capability.