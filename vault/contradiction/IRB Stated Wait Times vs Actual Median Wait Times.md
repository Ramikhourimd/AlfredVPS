---
alfred_tags:
- psychiatry/discrepancies
- operations/claims-vs-reality
claim_a: IRB submission stated approximately 3-5 day wait times for patients to see
  a case manager and psychiatrist
claim_b: Actual median wait times are 8 days to case manager and 16 days (8+8) to
  psychiatrist, with mean of 2 weeks and 25 days respectively
created: '2026-02-22'
janitor_note: LINK001 — Telia'z wikilinks valid (YAML escaping false positive). learn-contradiction.base
  embed references missing _bases/learn-contradiction.base — create it to enable dynamic
  views. LINK001 — person/Dekkel Khouri does NOT exist in vault. Nearest match may
  be person/Dekkel Taliaz (CEO). Human should verify correct person and fix the link.
name: IRB Stated Wait Times vs Actual Median Wait Times
project:
- '[[project/Telia''z AI Diagnostic Research Paper]]'
related:
- '[[conversation/AI Diagnostic Paper Research Meeting 2026-02-22]]'
- '[[note/AI Diagnostic Paper Methodology and Results Review 2026-02-22]]'
- '[[person/Noam]]'
- '[[person/Dekkel Khouri]]'
relationships:
- confidence: 0.98
  context: Nearly identical IRB wait time contradictions
  source: contradiction/IRB Stated Wait Times vs Actual Median Wait Times.md
  target: contradiction/IRB Stated Wait Times vs Actual Patient Wait Times.md
  type: related-to
- confidence: 0.75
  context: Clinical capacity and load discrepancies
  source: contradiction/IRB Stated Wait Times vs Actual Median Wait Times.md
  target: contradiction/Psychiatrist Session-to-Patient Ratio Exceeds Expected Clinical
    Norms.md
  type: related-to
- confidence: 0.7
  context: Service metric and wait time contradictions
  source: contradiction/IRB Stated Wait Times vs Actual Median Wait Times.md
  target: contradiction/Same-Month Intake Conversion Rate May Understate Total Patient
    Service Rate.md
  type: related-to
- confidence: 0.65
  context: Operational planning contradictions
  source: contradiction/IRB Stated Wait Times vs Actual Median Wait Times.md
  target: contradiction/Workforce Stabilization Priority Conflicts With Concurrent
    Recruitment Urgency.md
  type: related-to
- confidence: 0.85
  context: Both show unmet capacity commitments
  source: contradiction/IRB Stated Wait Times vs Actual Median Wait Times.md
  target: contradiction/Psychiatrist Hour Increase Commitments vs Observed Stagnation
    Pattern.md
  type: related-to
source_a: IRB application
source_b: Data export from Shmulik analyzed by Noam, 2026-02-22
status: unresolved
type: contradiction
---

# IRB Stated Wait Times vs Actual Median Wait Times

## Claim A

The IRB application stated that patients would see a case manager and psychiatrist within approximately 3-5 days of intake. Dekkel referenced this figure during the meeting.

## Claim B

Actual data analysis shows median wait of 8 days to case manager and 16 days to psychiatrist (8 days case manager + 8 additional days to psychiatrist). The mean is even higher (2 weeks and 25 days respectively) due to extreme outliers.

## Analysis

The discrepancy is significant — actual wait times are 2-5x what was stated in the IRB submission. Several factors may explain this:
- Extreme outliers (300+ day records) are likely technical errors inflating statistics
- Even after outlier cleaning, median is still 2-3x the IRB figure
- The figures in the IRB may have been aspirational or based on a different time period
- Need to check whether the IRB figure referred to a specific subset of patients

## Resolution

Unresolved. Must be addressed before paper publication. Options:
1. Report cleaned median data and note the discrepancy with IRB estimates
2. Investigate whether IRB figures apply to a specific patient cohort
3. Consult with ethics/IRB team about the discrepancy

![[learn-contradiction.base#Related]]