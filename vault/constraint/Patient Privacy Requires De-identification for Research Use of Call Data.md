---
authority: Healthcare privacy regulations
created: '2026-02-26'
janitor_note: 'LINK001 — Telia''z wikilink is YAML escaping false positive. Base view
  embeds (learn-constraint.base#Affected Projects, #Related) reference nonexistent
  _bases/learn-constraint.base — vault-wide infrastructure gap, embeds preserved.
  ORPHAN001 — no inbound links, consider linking from parent record.'
name: Patient Privacy Requires De-identification for Research Use of Call Data
project:
- '[[project/Telia''z Innovation Program]]'
related:
- '[[task/Explore Phone Call Transcription and De-identification Workflow]]'
- '[[person/Rivi Idelman]]'
source: Healthcare privacy regulations and clinical research ethics
status: active
type: constraint
---

# Patient Privacy Requires De-identification for Research Use of Call Data

## Constraint

Phone call recordings and transcriptions from clinical sessions cannot be used for innovation research purposes without first being de-identified. Any transcription workflow must include automatic de-identification as a mandatory step before data enters the research pipeline.

## Source

Healthcare privacy regulations governing patient data in clinical settings. Clinical research ethics require that identifiable patient information be removed or anonymized before use in research, quality improvement, or AI training contexts.

## Implications

- Transcription tooling must include or integrate with de-identification capabilities
- Manual transcription review may be needed to verify de-identification quality
- Limits the speed at which call data can flow into research workflows
- May affect transcription accuracy if de-identification removes clinically relevant context
- Tool selection for the transcription workflow is constrained to solutions that support or integrate with de-identification

## Expiry / Review

Ongoing — this is a permanent regulatory constraint. Review specific requirements when selecting transcription tools to ensure compliance with applicable privacy frameworks.

![[learn-constraint.base#Affected Projects]]
![[learn-constraint.base#Related]]
