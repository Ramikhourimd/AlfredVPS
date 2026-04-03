---
alfred_tags:
- llm/diagnostic-bias
- psychiatry/ptsd
- contextual-priming
cluster_sources:
- '[[person/Rami Khouri]]'
- '[[person/Dekkel Taliaz]]'
- '[[note/AI Diagnostic Paper Methodology and Results Review 2026-02-22]]'
confidence: medium
created: '2026-02-22'
janitor_note: 'LINK001 — base view embeds (learn-synthesis.base#Sources, #Related)
  reference _bases/learn-synthesis.base which does not exist (vault-wide issue). Fixed:
  Dekkel Khouri → Dekkel Taliaz in cluster_sources. Telia''z wikilinks are valid (YAML
  escaping false positive). DUP001 — possible duplicate of synthesis/Contextual Priming
  Replicates Psychiatrist Diagnostic Bias in LLMs.md (note trailing s).'
name: Contextual Priming Replicates Psychiatrist Diagnostic Bias in LLM
project:
- '[[project/Telia''z AI Diagnostic Research Paper]]'
related:
- '[[conversation/AI Diagnostic Paper Research Meeting 2026-02-22]]'
- '[[project/Telia''z Clinic Israel]]'
- '[[decision/Split Bias Findings Into Separate Paper]]'
relationships:
- confidence: 0.95
  context: Near-identical titles on priming
  source: synthesis/Contextual Priming Replicates Psychiatrist Diagnostic Bias in
    LLM.md
  target: synthesis/Contextual Priming Replicates Psychiatrist Diagnostic Bias in
    LLMs.md
  type: related-to
- confidence: 0.9
  context: Same priming bias replication
  source: synthesis/Contextual Priming Replicates Psychiatrist Diagnostic Bias in
    LLM.md
  target: synthesis/Psychiatrist PTSD Diagnostic Bias Replicated by Contextual LLM
    Priming.md
  type: related-to
status: active
supports:
- '[[assumption/Psychiatrist PTSD Diagnostic Bias Driven by Contextual Priming]]'
type: synthesis
---

# Contextual Priming Replicates Psychiatrist Diagnostic Bias in LLM

## Insight

When an LLM diagnostic agent is given the same contextual framing that real psychiatrists have (post-war clinical setting), it replicates their diagnostic bias — shifting from symptom-accurate depression diagnoses to context-influenced PTSD diagnoses. This demonstrates that diagnostic bias can be artificially introduced and studied through contextual priming of language models.

## Evidence

1. **Unbiased Expert Agent** — LLM prompted as "you are a psychiatrist" analyzed symptoms and produced diagnoses that aligned with DSM criteria. Insomnia was classified generically and co-occurring symptoms (e.g., anhedonia) drove classification. Result: more MDD (depression) diagnoses.

2. **Biased Expert Agent** — Same LLM prompted as "you are a psychiatrist in a post-war context" tagged identical symptoms toward trauma. Insomnia became "trauma-related insomnia." Result: more PTSD diagnoses.

3. **Real Psychiatrist Diagnoses** — Actual psychiatrists working in the post-war clinical setting diagnosed predominantly PTSD. The biased agent's predictions matched real diagnoses better than the unbiased agent's predictions.

4. **PHQ Correlation** — PHQ depression scores correlated well with questionnaire-based predictions but not with PTSD measures (PCL-5), supporting that the symptom profile actually fits depression better.

## Implications

- Opens a novel research direction: using LLM agents to study and quantify human diagnostic bias
- Raises questions about whether DSM is truly used as a diagnostic tool or whether context overrides criteria
- Could be published as a standalone anthropological/psychiatric paper
- Has implications for AI diagnostic systems — they can both avoid and replicate human bias depending on prompting

## Applicability

- Directly applicable to the Telia'z AI diagnostic paper (assigned to Paper 2)
- Relevant to broader AI-in-psychiatry research community
- Potentially relevant to military/veteran mental health contexts globally
- Could inform clinical training about awareness of contextual diagnostic bias

![[learn-synthesis.base#Sources]]
![[learn-synthesis.base#Related]]