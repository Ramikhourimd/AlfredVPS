---
based_on:
- '[[task/Investigate Patient Follow-Up Flow With Shira and Renee]]'
- '[[conversation/Patient Data Research and AI Summary Quality Meeting 2025-11-11]]'
confidence: medium
created: '2026-03-30'
janitor_note: LINK001 — Telia'z AI Clinical Platform wikilink is valid (YAML escaping
  false positive). synthesis/Platform Rebuild Requirements record exists and link
  is valid. ORPHAN001 — no inbound wikilinks, consider linking from project or task
  records.
name: Automatic Patient Communications Not Fully Mapped by Any Single Team Member
project:
- '[[project/Telia''z AI Clinical Platform]]'
related:
- '[[assumption/Staff Interviews Can Reconstruct Complete Patient Experience Flow]]'
- '[[synthesis/Platform Rebuild Requirements Distributed Across Stakeholders With
  No Central Repository]]'
source: Implied by Rami directing Rivi to investigate the full patient experience
  flow
source_date: '2025-11-11'
status: active
type: assumption
---

# Automatic Patient Communications Not Fully Mapped by Any Single Team Member

## Claim

No single person on the team has a complete picture of all automatic communications sent to patients — questionnaires, messages, notifications, and reminders. This knowledge is distributed across Shira (overall workflow), Renee (between-session experience), and Roy (follow-up questionnaires), requiring a deliberate multi-person investigation to reconstruct.

## Basis

Rami directed Rivi to conduct a multi-step investigation: start with Shira for the full workflow map, then Renee for inter-session patient experience, then Roy for follow-up questionnaires, and finally experience the flow herself as a pseudo-patient. If any single person held this knowledge, the investigation wouldn't require this sequence. The very structure of the task reveals the knowledge gap.

## Evidence Trail

- 2025-11-11: Task created for Rivi to investigate full patient flow across multiple staff members

## Impact

- New platform design risks replicating or missing automatic communications if this mapping isn't completed first
- AI agents processing patient data may miss context from automated touchpoints they don't know about
- Patient experience quality depends on these communications being coherent end-to-end
