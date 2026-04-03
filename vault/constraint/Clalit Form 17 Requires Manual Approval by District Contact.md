---
alfred_tags:
- partnerships/clalit/constraints
authority: Clalit Health Services
created: '2025-11-09'
janitor_note: 'LINK001 — Telia''z wikilink is valid (YAML escaping false positive).
  Base view embeds (learn-constraint.base#Affected Projects, #Related) reference _bases/learn-constraint.base
  which does not exist — vault-wide infrastructure gap. Embeds preserved per policy.'
name: Clalit Form 17 Requires Manual Approval by District Contact
project:
- '[[project/Telia''z Clinic Israel]]'
related:
- '[[org/Clalit Health Services]]'
- '[[note/Clalit Partnership Operational Planning 2025-11-09]]'
- '[[conversation/Clalit Partnership Operational Planning Meeting 2025-11-09]]'
- '[[process/Clinic Israel Patient Intake Flow]]'
related_to: '[[person/Michal Boguz]]'
relationships:
- confidence: 0.65
  context: Clalit approval and volume constraints
  source: constraint/Clalit Form 17 Requires Manual Approval by District Contact.md
  target: constraint/Clalit Partnership Patient Volume Ceiling Unknown.md
  type: related-to
source: Clalit internal authorization process
source_date: '2025-11-09'
status: active
type: constraint
---

# Clalit Form 17 Requires Manual Approval by District Contact

## Constraint

The Clalit partnership contact (Tzachi/Eli) insists on personally approving each Form 17 referral authorization. Unlike Maccabi where Form 17 was automatic upon questionnaire completion, Clalit's process requires manual internal approval before patients can receive Telia'z services. The contact also hints at wanting to approve follow-up treatment after intake assessment.

## Source

Identified during Telia'z preparation meeting (2025-11-09) based on multiple prior conversations with the Clalit contact, who repeatedly emphasized his role in approving Form 17 internally.

## Implications

- Creates a potential bottleneck in patient flow — SLA for approval turnaround is unknown
- Patients must not be referred to Telia'z before Form 17 is approved (lesson learned from Maccabi)
- The contact's desire for control may limit the volume of patients that can be processed
- Team proposed a 1-2 month pilot where the contact approves follow-ups, transitioning to automatic flow afterward
- Follow-up sessions may require separate approval cycles, unlike the bundled commitment model at Maccabi

## Expiry / Review

Review after initial pilot period (1-2 months). May be relaxed once trust is established with the Clalit contact.

![[learn-constraint.base#Affected Projects]]
![[learn-constraint.base#Related]]



## Update (2025-11-10)

Per the [[conversation/Clalit South Referral System Setup Meeting 2025-11-10]], this constraint applies specifically to **treatment subscriptions** only. **Diagnostic subscriptions** bypass this constraint as Form 17 is auto-generated. The district contacts for approval are Tzachi and [[person/Michal Boguz]]. The team decided to [[decision/Clalit South Pilot Starts With Diagnostic Subscriptions Only|start with diagnostic subscriptions only]] to avoid this bottleneck during the pilot.