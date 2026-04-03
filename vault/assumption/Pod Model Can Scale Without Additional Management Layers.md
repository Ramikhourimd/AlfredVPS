---
alfred_tags:
- clinic/pod-model
- management/structure
- scaling/pods
created: '2026-02-25'
description: Teams of ~10 practitioners can be effectively managed by a pod lead (senior
  clinician with ~10 extra hours/month) without adding formal middle management layers.
  Pods are operational units that share clinical forums across pod boundaries.
janitor_note: LINK001 — base view embed (related.base#All) references _bases/related.base
  which does not exist. Create it to enable dynamic views. Telia'z wikilinks are valid
  (YAML escaping false positive). ORPHAN001 — no inbound wikilinks from other records.
name: Pod Model Can Scale Without Additional Management Layers
project: '[[project/Telia''z Organizational Restructuring]]'
relationships:
- confidence: 0.9
  context: Scaling needs optimal pod size
  source: assumption/Pod Model Can Scale Without Additional Management Layers.md
  target: assumption/Pod Structure of 10 Psychiatrists is Optimal Management Span.md
  type: depends-on
- confidence: 0.7
  context: Operational model scales flatly
  source: assumption/Pod Model Can Scale Without Additional Management Layers.md
  target: assumption/Pods Are Operational Units Not Clinical Governance Units.md
  type: related-to
status: active
type: assumption
---

# Pod Model Can Scale Without Additional Management Layers

## Assumption

As the clinic grows to 30+ psychiatrist positions and 50+ case managers, the pod model (groups of ~10 managed by a senior clinician pod lead) will provide sufficient management span without requiring additional formal management layers between pod leads and department heads.

## Risk If Wrong

If pods are insufficient, the clinic may experience coordination failures, quality inconsistencies, or pod lead burnout. Would require either adding a layer of management (pod group leads) or reducing pod size, both of which increase overhead.

## Validation

- Monitor pod lead workload and satisfaction
- Track clinical quality metrics per pod
- Assess coordination effectiveness through cross-pod forum participation
- Review at clinic size milestones (20, 30, 50 practitioners)

## Related
![[related.base#All]]