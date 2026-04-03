---
alfred_tags:
- psychiatry/suicide-risk
- clinical-supervision/acute
- risk-protocols
based_on:
- '[[note/Clinical Supervision - Suicidal Risk Assessment and Military Reporting Protocols]]'
confidence: medium
created: '2026-02-26'
janitor_note: 'LINK001: All Telia''z wikilinks verified as valid — scanner false positives
  from YAML apostrophe escaping. Base view embeds (learn-assumption.base) are not
  broken links. ORPHAN001: No inbound wikilinks detected — new record, may need linking
  from related records.'
name: Case Managers Need Structured Supervision Framework for Acute Risk Assessment
project:
- '[[project/Telia''z Clinic Israel]]'
related:
- '[[constraint/Rami Cannot Serve as Full-Time Clinic Medical Director]]'
- '[[assumption/District Model Requires Dedicated Medical Director]]'
- '[[constraint/Medical Director Must Be Licensed Physician]]'
relationships:
- confidence: 0.95
  context: Both address acute supervision structure needs
  source: assumption/Case Managers Need Structured Supervision Framework for Acute
    Risk Assessment.md
  target: constraint/Acute Clinical Supervision Depends on Single-Clinician Ad Hoc
    Availability.md
  type: related-to
- confidence: 0.8
  context: Framework covers enhanced risk protocols
  source: assumption/Case Managers Need Structured Supervision Framework for Acute
    Risk Assessment.md
  target: constraint/Military-Connected Patients With Weapon Access Require Enhanced
    Risk Protocols.md
  type: related-to
- confidence: 0.85
  context: Framework ensures legal-standard risk documentation
  source: assumption/Case Managers Need Structured Supervision Framework for Acute
    Risk Assessment.md
  target: constraint/Suicidal Risk Documentation Must Demonstrate Maximum Assessment
    Effort for Legal Protection.md
  type: related-to
- confidence: 0.75
  context: Alerts support risk supervision process
  source: assumption/Case Managers Need Structured Supervision Framework for Acute
    Risk Assessment.md
  target: constraint/On-Call Alert Chain Has No Automated Fallback When Manual Steps
    Fail.md
  type: related-to
source: Clinical supervision call — Selina requesting guidance from Rami
source_date: '2025-12-01'
status: active
type: assumption
---

# Case Managers Need Structured Supervision Framework for Acute Risk Assessment

## Claim

Case managers at Telia'z Clinic Israel lack a formalized framework for handling acute psychiatric risk (suicidality, danger to self/others) and currently rely on ad-hoc phone consultations with Rami Khouri for clinical guidance. A structured supervision protocol is needed for the clinic to scale safely.

## Basis

On 2025-12-01, case manager Selina called Rami for urgent guidance on a suicidal patient with military connections and weapon access. The call revealed that Selina was anxious, unsure of the assessment hierarchy, and had no documented protocol to follow. Rami provided an improvised teaching session covering the full risk assessment framework (ideation → thoughts → intention → plan → act), point-in-time assessment principles, and military reporting requirements. This level of supervision cannot scale with Rami as the sole clinical supervisor.

## Evidence Trail

- 2025-12-01: Selina's urgent supervision call — no protocol existed, relied entirely on Rami's availability
- The clinical teaching content (assessment hierarchy, point-in-time principles, military reporting) represents knowledge that should be codified into a protocol

## Impact

- Without a structured framework, case managers may delay or mishandle acute risk situations when Rami is unavailable
- The planned Medical Director hire (30% position) must include establishing clinical supervision protocols as a deliverable
- Scaling the case manager team (currently projected to need ~21 case managers) amplifies the risk of unstructured supervision
- Military/security patients with weapon access represent a specific high-risk subpopulation requiring explicit handling procedures

![[learn-assumption.base#Depends On This]]
![[learn-assumption.base#Related]]