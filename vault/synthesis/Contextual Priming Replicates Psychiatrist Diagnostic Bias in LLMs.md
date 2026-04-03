---
alfred_tags:
- llm/diagnostic-bias
- psychiatry/ptsd
- contextual-priming
cluster_sources:
- '[[project/Telia''z AI Diagnostic Research Paper]]'
- '[[person/Rami Khouri]]'
- '[[conversation/AI Diagnostic Paper Progress Meeting 2026-02-22]]'
confidence: high
created: '2026-02-22'
janitor_note: 'LINK001 — base view embeds (learn-synthesis.base#Sources, #Related)
  reference _bases/learn-synthesis.base which does not exist. Telia''z wikilinks are
  valid (YAML escaping false positive).'
name: Contextual Priming Replicates Psychiatrist Diagnostic Bias in LLMs
project:
- '[[project/Telia''z AI Diagnostic Research Paper]]'
related:
- '[[note/AI Diagnostic Paper Methodology and Results Discussion]]'
- '[[person/Dekkel Taliaz]]'
- '[[project/Telia''z Clinic Israel]]'
- '[[assumption/Questionnaire Alone Is a Weak Diagnostic Predictor]]'
relationships:
- confidence: 0.9
  context: Same priming bias replication
  source: synthesis/Contextual Priming Replicates Psychiatrist Diagnostic Bias in
    LLMs.md
  target: synthesis/Psychiatrist PTSD Diagnostic Bias Replicated by Contextual LLM
    Priming.md
  type: related-to
status: active
supports:
- '[[decision/Split AI Diagnostic Research Into Two Papers]]'
type: synthesis
---

# Contextual Priming Replicates Psychiatrist Diagnostic Bias in LLMs

## Insight

When an LLM is prompted as a psychiatrist and given contextual framing (post-war clinical setting), it replicates the same diagnostic bias observed in real psychiatrists — favoring PTSD diagnoses over MDD even when DSM symptom criteria better match depression. Without contextual priming, the same LLM correctly classifies symptoms as depression. This demonstrates that psychiatrist diagnostic bias is not just a human failing but a predictable response to contextual information that can be systematically studied and replicated in AI systems.

## Evidence

1. **Expert Agent (no context)**: When prompted as "you are a psychiatrist" and asked to diagnose strictly by DSM symptoms, the LLM classified insomnia as generic and, combined with anhedonia, predicted depression (MDD).

2. **Biased Expert Agent (with context)**: When given additional contextual framing about the post-war clinical setting, the same LLM re-tagged insomnia as "trauma-related insomnia" and shifted predictions toward PTSD.

3. **Ground truth alignment**: The biased agent's predictions more closely matched actual psychiatrist diagnoses — suggesting the psychiatrists themselves operated with similar contextual bias.

4. **PHQ/PCL correlation**: Previous analysis showed PHQ (depression) scores correlated with AI symptom extraction but PCL (PTSD) scores did not — supporting the interpretation that actual symptom profiles were more depressive than traumatic.

5. **DSM structural limitation**: The finding raises fundamental questions about whether DSM criteria are truly diagnostic tools or whether real-world diagnosis is inherently context-dependent.

## Implications

- Psychiatrists in specialized clinical settings (post-war, trauma centers) may systematically over-diagnose the conditions they expect to find
- LLMs can be used as controlled instruments to study diagnostic bias by toggling contextual priming on and off
- This finding has both clinical (treatment accuracy) and anthropological (diagnostic practice) significance
- The result is strong enough to warrant a dedicated paper (decided 2026-02-22)

## Applicability

- Psychiatric diagnostic practice and training
- AI-assisted clinical decision support systems
- Quality assurance in clinical diagnosis
- Broader research on cognitive bias in medical practice

![[learn-synthesis.base#Sources]]
![[learn-synthesis.base#Related]]