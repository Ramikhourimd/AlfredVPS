---
alfred_instructions: null
alfred_tags:
- suicidality/intake-protocol
- emergency-contact
- child-intake
assigned: null
blocked_by: []
created: '2025-11-10'
depends_on: []
description: null
due: null
janitor_note: 'LINK001 false positive: Telia''z wikilinks are YAML escaping artifacts
  — targets exist with single apostrophe. Base view embed (related.base#All) references
  _bases/related.base which does not exist — vault-wide structural gap. Non-schema
  fields org and owner present — human review needed.'
kind: task
name: Integrate Emergency Contact Field with Suicide Risk Assessment
org: '[[org/Telia''z]]'
owner: '[[person/Adiel Levin]]'
priority: high
project: '[[project/Telia''z Clinic Israel]]'
related:
- '[[conversation/Product Team Patient App and Risk Assessment Discussion 2025-11-10]]'
- '[[decision/Adopt Structured Five-Level Suicidal Risk Assessment Protocol]]'
- '[[person/Ori Shukron]]'
- '[[person/Shmulik]]'
- '[[asset/HealthyMind Platform]]'
relationships:
- confidence: 0.55
  context: Emergency contact logistics
  source: task/Integrate Emergency Contact Field with Suicide Risk Assessment.md
  target: task/Obtain Clalit South District Fax Number.md
  type: related-to
- confidence: 0.9
  context: Emergency contact protocol
  source: task/Integrate Emergency Contact Field with Suicide Risk Assessment.md
  target: task/Send Emergency Contact Protocol to Eitan.md
  type: related-to
- confidence: 0.8
  context: Suicide intake enhancements
  source: task/Integrate Emergency Contact Field with Suicide Risk Assessment.md
  target: task/Strengthen Suicidality Questions in Parent Intake Protocol.md
  type: related-to
run: null
status: todo
tags: []
type: task
---

# Integrate Emergency Contact Field with Suicide Risk Assessment

## Description

Add the emergency contact person field (from Ori Shukron's protocol) to the suicidality screening questionnaire intake flow. The field should appear alongside the risk assessment screening questions at the patient's first meeting with their case manager.

## Acceptance Criteria

- [ ] Ori forwards the emergency contact protocol to Eitan
- [ ] Emergency contact field added to the first-meeting questionnaire
- [ ] Field is one-time only (not recurring at every session)
- [ ] Shmulik completes final integration of risk assessment into the system
- [ ] End-to-end flow tested: screening questions + emergency contact at first meeting

## Technical Context

- Shmulik has the final integration piece — estimated half day of work
- Questionnaire has two parts: screening questions (first meeting only) and address (every meeting)
- Emergency contact fits with the first-meeting-only screening section
- Decision: prospective only — existing patients will not be asked retroactively

---
## Related
![[related.base#All]]