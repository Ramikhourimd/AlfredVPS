---
authority: Questionnaire instrument design
created: '2026-02-27'
janitor_note: 'LINK001 false positives: Telia''z wikilinks use YAML single-quote escaping
  (targets exist). Assumption link target verified to exist. ORPHAN001: no inbound
  links — consider linking from research paper project.'
location:
- '[[project/Telia''z Clinic Israel]]'
name: Questionnaire Instrument Structurally Limited to PHQ Depression Anxiety and
  PCL-5 PTSD Domains
project:
- '[[project/Telia''z AI Diagnostic Research Paper]]'
related:
- '[[assumption/Questionnaire Alone Is Insufficient Predictor for Full DSM Coverage]]'
- '[[assumption/Questionnaire Alone Is a Weak Diagnostic Predictor]]'
- '[[assumption/Questionnaire Is Not a Strong Predictive Tool for Full DSM Diagnoses]]'
- '[[assumption/Case Manager DSM-Oriented Questioning Makes Transcripts Stronger Diagnostic
  Source]]'
source: Instrument design — structured self-report covering only specific screening
  domains
source_date: '2026-02-22'
status: active
type: constraint
---

# Questionnaire Instrument Structurally Limited to PHQ Depression Anxiety and PCL-5 PTSD Domains

## Constraint

The patient intake questionnaire used at Telia'z Clinic contains questions covering only three primary diagnostic domains: depression (PHQ-based items), anxiety, and PTSD (PCL-5-based items). It includes limited coverage of sleep and eating disorders but does not contain screening criteria for the full DSM diagnostic spectrum (e.g., personality disorders, substance use disorders, bipolar, psychotic disorders).

## Source

This is a structural limitation of the questionnaire instrument itself, not a performance finding. The instrument was designed for initial intake screening in a post-war clinical context where depression, anxiety, and PTSD are the primary presenting concerns. Multiple meeting notes confirm this: "questionnaire primarily covers depression, anxiety, and PTSD symptoms" and "limited coverage for other diagnoses (sleep, eating disorders, etc.)."

## Implications

- The S1 (questionnaire-only) prediction agent can never achieve high diagnostic accuracy across all DSM categories — its ceiling is determined by instrument coverage, not model capability
- All existing assumptions about questionnaire weakness as a predictor are consequences of this structural constraint
- Any comparison between S1 and S2/S3 performance reflects instrument design, not just model quality
- Paper 1 must frame S1 limitations as a known instrument constraint, not an unexpected finding

## Expiry / Review

This constraint is permanent for the current study. Would change only if the clinic adopts a broader screening instrument (e.g., adding MINI or SCID-based items). Should be revisited if the clinic changes its intake questionnaire.
