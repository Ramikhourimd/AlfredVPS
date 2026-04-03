---
created: '2025-11-10'
description: null
janitor_note: 'LINK001 false positives: project/Telia''z Clinic Israel wikilink resolves
  correctly (YAML single-quote escaping). Base view embed (related.base#All) references
  _bases/related.base which does not exist — vault-wide gap. ORPHAN001: no inbound
  links, consider linking from project/Telia''z Clinic Israel or a conversation record.'
name: Patient App Launch and Risk Assessment Integration Meeting 2025-11-10
project: '[[project/Telia''z Clinic Israel]]'
related:
- '[[conversation/Product Team Patient App and Risk Assessment Discussion 2025-11-10]]'
- '[[asset/HealthyMind Platform]]'
- '[[decision/Adopt Structured Five-Level Suicidal Risk Assessment Protocol]]'
- '[[person/Rami Khouri]]'
- '[[person/Adiel Levin]]'
- '[[person/Noa Hinden]]'
- '[[person/Ori Shukron]]'
- '[[person/Rivi Idelman]]'
- '[[person/Dekkel Taliaz]]'
- '[[person/Shmulik]]'
- '[[person/Shira]]'
relationships: []
session: null
status: active
subtype: meeting-summary
tags: []
type: note
---

# Patient App Launch and Risk Assessment Integration Meeting 2025-11-10

## Summary

Product team meeting on 2025-11-10 covered two main topics: (1) patient-facing mobile app launch readiness concerns, and (2) suicide risk assessment feature integration with emergency contact protocol.

## Patient App Launch Concerns

Rami raised alarm that Dekkel Taliaz is pushing to launch the HealthyMind patient-facing app to all patients immediately without adequate preparation. The team identified several gaps:

1. **No summary downloads** — patients cannot download session summaries from the app
2. **No complaint handling protocol** — no defined process for patient complaints once the app is live
3. **UX not characterized** — nobody has comprehensively reviewed what patients actually see and can do in the app
4. **No secretary support protocol** — clinic secretaries (first contact for patient complaints) have no guidance on how to handle app-related issues
5. **No in-app support channel** — patients have no way to report issues from within the app itself

### Agreed Actions

- Involve Rivi Idelman for UX characterization and evaluation of the patient experience
- Characterize current app features: what patients can see, download, and do
- Determine what complaint pathways exist (in-app ticketing vs. calling the clinic)
- Build a support protocol for secretaries before broad rollout

## Suicide Risk Assessment and Emergency Contact

Eitan (Adiel Levin) confirmed the suicidality screening feature is nearly done. Shmulik has the final integration piece — estimated half a day of work to connect it to the system.

Key decision: the emergency contact person field (from Ori Shukron's protocol) will be bundled together with the risk assessment, placed at the same intake point. This is a one-time field filled at the first meeting with the case manager.

Shira raised whether to apply retroactively to existing patients — the decision was to apply prospectively only (new patients going forward).

### Questionnaire Structure (per Shachar)

- **Screening questions**: Three questions plus one additional — shown only at the first meeting with the case manager
- **Address field**: Shown before every meeting (recurring)
- **Emergency contact**: One-time, bundled with screening at first meeting

## Open Items

- Ori to send the emergency contact protocol to Eitan for implementation
- Rivi UX review of patient app before any broad rollout
- Secretary support protocol to be designed
- In-app support mechanism to be scoped

---
## Related
![[related.base#All]]
