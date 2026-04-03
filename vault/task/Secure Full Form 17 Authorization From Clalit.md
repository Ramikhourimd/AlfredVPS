---
alfred_instructions: null
assigned: null
blocked_by: []
created: '2025-11-09'
depends_on: []
description: Obtain full end-to-end Form 17 authorization from Clalit covering both
  intake (case manager + psychiatric sessions) and follow-up sessions. Clarify patient
  volume caps, approval SLA, and whether follow-up requires separate approval cycles.
due: null
janitor_note: 'LINK001 false positive: Telia''z wikilink is YAML escaping artifact.
  LINK001: verify if note/Clalit South Psychiatric Referral and Subscription System
  Design 2025-11-10 exists. Base view embed (related.base) references _bases/ file
  that does not exist — vault-wide structural gap. ORPHAN001: no inbound wikilinks.
  Non-schema field related_to present — human review needed.'
kind: task
name: Secure Full Form 17 Authorization From Clalit
priority: high
project: '[[project/Telia''z Clinic Israel]]'
related:
- '[[constraint/Clalit Form 17 Requires Manual Approval by District Contact]]'
- '[[conversation/Clalit Partnership Operational Planning Meeting 2025-11-09]]'
- '[[org/Clalit Health Services]]'
- '[[process/Clinic Israel Patient Intake Flow]]'
related_to: '[[note/Clalit South Psychiatric Referral and Subscription System Design
  2025-11-10]]'
relationships: []
run: null
status: todo
tags: []
type: task
---

# Secure Full Form 17 Authorization From Clalit

Obtain comprehensive Form 17 authorization that covers the full patient pathway — intake sessions (6 case manager + psychiatric intake) and follow-up sessions (4 follow-up + assessments). Clarify volume limits and approval turnaround.

## Context

The Clalit contact wants to personally approve each Form 17 and potentially each follow-up authorization. This creates an operational bottleneck that must be negotiated before scaling. Raised in [[conversation/Clalit Partnership Operational Planning Meeting 2025-11-09]].

## Key Questions to Resolve
- Is there a patient volume cap?
- What is the SLA for Form 17 approval?
- Are follow-up sessions covered in the initial Form 17 or require separate approval?
- Can the approval oversight be limited to a pilot period?

## Related
![[related.base#All]]

## Outcome

*Pending resolution from Clalit meeting.*



## Update (2025-11-10)

The [[conversation/Clalit South Referral System Setup Meeting 2025-11-10]] clarified that Form 17 for **diagnostic subscriptions** is auto-generated and does not require manual authorization. The team decided to [[decision/Clalit South Pilot Starts With Diagnostic Subscriptions Only|pilot with diagnostic subscriptions only]], effectively bypassing the Form 17 authorization bottleneck for the initial phase. Full Form 17 authorization for treatment subscriptions remains a future requirement.
