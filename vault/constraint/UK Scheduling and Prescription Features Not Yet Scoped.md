---
alfred_tags:
- uk/scheduling
- uk/prescriptions
authority: Product development status
created: '2026-02-15'
janitor_note: 'LINK001 false positive: Telia''z wikilinks use valid YAML single-quote
  escaping; targets exist in vault. learn-constraint.base embeds reference _bases/learn-constraint.base
  which does not exist (systemic vault infrastructure gap).'
name: UK Scheduling and Prescription Features Not Yet Scoped
project:
- '[[project/Telia''z UK Expansion]]'
related:
- '[[conversation/Telia''z Team Meeting UK Launch Operations and Capacity 2026-02-15]]'
- '[[note/Telia''z Team Meeting UK Launch Operations and Recruitment 2026-02-15]]'
- '[[task/Define UK Prescription and Report Formats]]'
- '[[person/Stav Zamir]]'
relationships:
- confidence: 0.85
  context: Unscoped features compete for backlog
  source: constraint/UK Scheduling and Prescription Features Not Yet Scoped.md
  target: constraint/UK Product Features Compete for Shared Engineering Backlog With
    Israel.md
  type: part-of
source: Stav Zamir, team meeting 2026-02-15
source_date: '2026-02-15'
status: active
type: constraint
---

# UK Scheduling and Prescription Features Not Yet Scoped

## Constraint
The patient scheduling feature (allowing UK patients to see available appointment slots) and UK-specific prescription issuance are not yet designed or scoped. Stav flagged these as critical — patients must know they can get timely appointments, and prescriptions are essential for the UK clinical flow (unlike Israel where the assessment doesn't result in a prescription).

## Source
Product status update from Stav Zamir at team meeting 2026-02-15. The scheduling feature was not part of the original assessment scope; the prescription feature involves UK-specific regulations and possibly external system integration.

## Implications
- Added to development backlog for prioritization
- May delay the March 31 launch if scoping/development takes too long
- Workaround: Adiel noted there will be a natural gap between first patient contact and needing these features, allowing development time
- Shachar (VP R&D) requires completed specification before starting development

## Expiry / Review
Review at next development meeting. Target resolution before March 31 launch.

![[learn-constraint.base#Affected Projects]]
![[learn-constraint.base#Related]]