---
authority: Academic peer review standards
created: '2026-03-11'
janitor_note: 'LINK001 — Telia''z wikilinks are valid (YAML escaping false positive).
  Assumption wikilink is valid (multiline scanner wrapping false positive). Base view
  embeds (learn-constraint.base#Affected Projects, #Related) reference _bases/learn-constraint.base
  which does not exist — systemic vault issue, embeds preserved. ORPHAN001 — no inbound
  links; consider linking from project/Telia''z AI Diagnostic Research Paper.'
name: NLP Transcript Extraction Methodology Requires Published Literature Precedent
project:
- '[[project/Telia''z AI Diagnostic Research Paper]]'
related:
- '[[task/Find NLP Outcome Scoring Literature for Transcript Analysis]]'
- '[[assumption/Text-Based Sentiment Analysis Outperforms Standardized Questionnaires
  for Clinical Outcome Tracking]]'
- '[[decision/Use Per-Symptom Scoring Instead of Composite Score]]'
source: Task assignment and methodology discussion
source_date: '2025-11-13'
status: active
type: constraint
---

# NLP Transcript Extraction Methodology Requires Published Literature Precedent

## Constraint

The AI diagnostic pipeline's NLP-based approach to extracting per-symptom clinical indicators from free-text therapy session transcripts cannot be presented in the research paper without citing published methodological precedent. The methodology section must reference established literature on NLP analysis of psychotherapy transcripts, thematic analysis methods for clinical outcome measurement, and/or validated scoring instruments derived from session text.

## Source

Academic publishing standards require methodological grounding in prior work. The research team explicitly identified this gap when assigning Noam to search for NLP outcome scoring literature (task created 2025-11-13). Rami's pipeline already functions technically, but lacks the academic validation layer needed for peer review.

## Implications

- Paper submission is blocked until literature review is complete and relevant citations are identified
- If no suitable published precedent exists, the team may need to frame their approach as novel methodology — which requires additional validation steps and potentially a separate methods paper
- Noam's thematic analysis background is being leveraged to bridge traditional psychotherapy research methods with the AI pipeline approach
- The literature search scope includes: NLP analysis of psychotherapy transcripts, thematic analysis for clinical outcomes, sentiment analysis in mental health, and language model-based clinical extraction

## Expiry / Review

Active until Noam delivers the literature summary. If adequate citations are found, this constraint is satisfied and can be marked expired. If not, the constraint escalates to a methodological challenge requiring team discussion.

![[learn-constraint.base#Affected Projects]]
![[learn-constraint.base#Related]]
