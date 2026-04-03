---
alfred_tags:
- multi-agent/diagnostic-pipeline
- insights/patterns
cluster_sources:
- '[[note/AI Diagnostic Paper Research Meeting 2026-02-22]]'
- '[[note/AI Diagnostic Paper Review Meeting Notes 2026-02-22]]'
- '[[note/AI Diagnostic Paper Methodology and Results Discussion]]'
- '[[note/AI Diagnostic Paper Research Meeting Notes 2026-02-22]]'
confidence: medium
created: '2026-02-27'
janitor_note: LINK001 — Telia'z wikilinks use valid YAML single-quote escaping, not
  broken. learn-synthesis.base# embeds reference _bases/ files (may not exist yet).
  ORPHAN001 — draft synthesis with no inbound links; consider linking from project/Telia'z
  AI Diagnostic Research Paper or a related note.
name: LLM Approaches Progressively Replace Rule-Based Methods Across Pipeline Stages
project:
- '[[project/Telia''z AI Diagnostic Research Paper]]'
related:
- '[[assumption/Expert Persona Prompting Improves LLM Diagnostic Accuracy]]'
- '[[assumption/Questionnaire Extraction Is Purely Algorithmic Due to Structured Format]]'
relationships:
- confidence: 0.85
  context: LLM shift in arch emergence
  source: synthesis/LLM Approaches Progressively Replace Rule-Based Methods Across
    Pipeline Stages.md
  target: synthesis/Pipeline Architecture Emerged Through Iterative Failure Correction.md
  type: part-of
- confidence: 0.7
  context: LLM replacement aids clinical data superiority
  source: synthesis/LLM Approaches Progressively Replace Rule-Based Methods Across
    Pipeline Stages.md
  target: synthesis/Clinical Interaction Data Outperforms Self-Report Across Pipeline
    Stages.md
  type: supports
status: draft
supports:
- '[[decision/Switch Transcript Extraction From Rule-Based to LLM-Based]]'
- '[[decision/Abandon Non-LLM Fusion for LLM-Based Diagnostic Fusion]]'
type: synthesis
---

# LLM Approaches Progressively Replace Rule-Based Methods Across Pipeline Stages

## Insight

Across the multi-agent diagnostic pipeline, every stage that initially attempted a non-LLM (rule-based or algorithmic) approach was eventually replaced or supplemented by an LLM-based method — except where the data is already fully structured. This reveals a consistent pattern: unstructured or semi-structured clinical data requires LLM reasoning to extract meaningful diagnostic signal.

## Evidence

1. **Transcript extraction**: Started with strict rule-based parsing, switched to LLM-based extraction because rule-based approach was "too strict" and captured insufficient data.
2. **Diagnostic fusion**: Started with non-LLM fusion that simply selected one source's diagnosis rather than synthesizing across sources. Replaced with LLM-based fusion that reasons across all inputs.
3. **Expert persona**: Added LLM-as-psychiatrist stage that improved accuracy beyond raw fusion output.
4. **Questionnaire extraction**: The ONE stage that remained algorithmic — because questionnaire data is already fully structured with clear, codified rules.

## Implications

- The only reliable non-LLM extraction is from fully structured data (questionnaires with defined answer formats)
- For Paper 1, this progressive replacement narrative strengthens the methodology justification
- For future pipeline development, default to LLM-based approaches for any unstructured clinical data
- The pattern suggests that clinical reasoning (weighing symptoms, contextual interpretation) inherently requires language model capabilities

## Applicability

Applies to any clinical NLP pipeline working with semi-structured or unstructured medical data. The structured-data exception (questionnaires) may generalize to other fully codified clinical instruments.

![[learn-synthesis.base#Sources]]
![[learn-synthesis.base#Related]]