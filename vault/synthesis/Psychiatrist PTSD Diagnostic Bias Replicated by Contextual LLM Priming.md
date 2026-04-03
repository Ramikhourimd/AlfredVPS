---
alfred_tags:
- llm/diagnostic-bias
- psychiatry/ptsd
- contextual-priming
cluster_sources:
- '[[project/Telia''z AI Diagnostic Research Paper]]'
- '[[project/Telia''z Clinic Israel]]'
- '[[person/Rami Khouri]]'
confidence: medium
created: '2026-02-25'
janitor_note: 'LINK001 — broken link [[person/Dekkel Khouri]], possible match: [[person/Dekkel
  Taliaz]]. Needs human review to confirm correct target. Base view embeds (learn-synthesis.base#Sources,
  #Related) reference _bases/learn-synthesis.base which does not exist. Create it
  to enable dynamic views. Telia''z wikilinks are valid (YAML escaping false positive).'
name: Psychiatrist PTSD Diagnostic Bias Replicated by Contextual LLM Priming
project:
- '[[project/Telia''z AI Diagnostic Research Paper]]'
related:
- '[[conversation/AI Diagnostic Paper Methodology Review Meeting 2026-02-22]]'
- '[[note/AI Diagnostic Paper Research Meeting Notes 2026-02-22]]'
- '[[person/Dekkel Khouri]]'
- '[[person/Noam]]'
status: draft
type: synthesis
---

# Psychiatrist PTSD Diagnostic Bias Replicated by Contextual LLM Priming

## Insight

When an LLM agent analyzes patient symptoms using pure DSM criteria (the "Expert Agent"), it frequently diagnoses depression (MDD) rather than PTSD, because the available symptom evidence better matches depression criteria. However, human psychiatrists who met the same patients face-to-face predominantly diagnosed PTSD.

When the same LLM agent is given contextual priming — told it is a psychiatrist working in a post-war setting (the "Biased Agent") — it replicates the human psychiatrists' PTSD diagnostic pattern. This demonstrates that:

1. Psychiatrists carry a contextual bias, diagnosing PTSD based on population context rather than strictly on DSM symptom criteria
2. This bias can be artificially induced in LLMs through contextual priming
3. The DSM may be an imperfect diagnostic instrument in practice, with clinicians routinely overriding its criteria based on contextual knowledge

The mechanism is observable at the symptom level: the Expert Agent tags insomnia as general insomnia, while the Biased Agent tags the same symptom as "trauma-related insomnia" when given context. This reattribution cascades through the diagnostic reasoning.

## Evidence

- Questionnaire data correlates with PHQ (depression) but NOT with PCL (PTSD), suggesting symptom profiles actually match depression
- Expert Agent (no context) produces depression diagnoses from available symptoms
- Biased Agent (post-war context) produces PTSD diagnoses matching human psychiatrists
- Human psychiatrists diagnosed PTSD despite insufficient DSM PTSD criteria in the data
- The finding holds across the patient cohort studied (post-war Israeli patients)

## Implications

- This finding could be a standalone clinical/anthropological research paper
- Raises questions about DSM validity as a pure diagnostic tool vs. clinical heuristics
- Relevant for understanding how AI diagnostic tools should handle context vs. strict criteria
- Important for Telia'z psychiatrist awareness — not to change practice, but to be aware of the bias pattern

## Applicability

- Clinical AI diagnostic systems design (when to include vs exclude context)
- Psychiatric training and bias awareness
- DSM critique literature
- Post-conflict mental health research

![[learn-synthesis.base#Sources]]
![[learn-synthesis.base#Related]]