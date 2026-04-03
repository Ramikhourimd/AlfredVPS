---
alfred_tags:
- psychiatry/discrepancies
- operations/claims-vs-reality
claim_a: Most psychiatric patients should see their psychiatrist no more than once
  per month, implying a session-to-patient ratio at or below 1.0
claim_b: Clinic data shows psychiatrist session-to-patient ratio above 1.0 per month
created: '2026-02-26'
janitor_note: 'LINK001: Telia''z wikilinks are YAML escaping false positives (targets
  verified). Base view embed (learn-contradiction.base#Related) references missing
  _bases/ infrastructure — vault-wide gap, not per-file fixable. ORPHAN001: No inbound
  wikilinks — consider linking from related analysis or project notes.'
name: Psychiatrist Session-to-Patient Ratio Exceeds Expected Clinical Norms
project:
- '[[project/Telia''z Clinic Israel]]'
related:
- '[[note/Telia''z Strategic Goals and Clinical Sustainability Meeting 2025-12-04]]'
- '[[assumption/Monthly Patient Churn Rate Is Approximately 15 Percent]]'
- '[[assumption/Follow-Up Session Ratio at 15 Percent Is On Target]]'
relationships:
- confidence: 0.7
  context: Patient load and service rate metrics
  source: contradiction/Psychiatrist Session-to-Patient Ratio Exceeds Expected Clinical
    Norms.md
  target: contradiction/Same-Month Intake Conversion Rate May Understate Total Patient
    Service Rate.md
  type: related-to
- confidence: 0.8
  context: Staffing and workforce contradictions
  source: contradiction/Psychiatrist Session-to-Patient Ratio Exceeds Expected Clinical
    Norms.md
  target: contradiction/Workforce Stabilization Priority Conflicts With Concurrent
    Recruitment Urgency.md
  type: related-to
source_a: Standard psychiatric practice norms and Rami clinical judgement
source_b: Maccabi database analysis presented at 2025-12-04 strategic meeting
status: unresolved
type: contradiction
---

# Psychiatrist Session-to-Patient Ratio Exceeds Expected Clinical Norms

## Claim A

Standard psychiatric practice and Rami's clinical judgement indicate that most patients should not see a psychiatrist more than once per month. The expected session-to-patient ratio should be at or below 1.0 for psychiatrists (case managers having a higher ratio of 1.38 is considered normal).

## Claim B

Clinic data from the Maccabi database analysis shows that the psychiatrist session-to-patient ratio exceeds 1.0 per month. This was flagged as anomalous during the 2025-12-04 strategic goals meeting.

## Analysis

The team suspects this is a data methodology issue rather than a clinical practice problem. The most likely cause: the "active patient" denominator may not include new intakes processed in the same month, artificially inflating the ratio. If 50 new patients are seen but not counted in the denominator until the following month, the ratio would be skewed upward.

The team agreed to investigate the calculation methodology separately. Until resolved, this anomaly undermines confidence in the staffing projection model (which uses session-to-patient ratios to calculate required FTE).

## Resolution

Pending investigation of the Maccabi data calculation methodology. Need to verify: (1) how "active patients" is defined in the denominator, (2) when new intakes enter the active count, and (3) whether cancelled/rescheduled sessions inflate the numerator.

![[learn-contradiction.base#Related]]