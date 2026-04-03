---
authority: Telia'z Clinic IT infrastructure
created: '2026-03-07'
janitor_note: 'LINK001: Broken wikilinks to assumption/Automated AI Extraction Can
  Reliably Parse Unstructured Patient Google Docs and constraint/Key Demographic Variables
  Only Available Through NLP Extraction From Unstructured Text — these target files
  may not exist in the vault. ORPHAN001: This record has no inbound wikilinks from
  other vault files. Verify linked targets exist and consider linking from relevant
  notes or project records.'
name: Patient Clinical Records Stored as Individual Google Docs Files
project:
- '[[project/Telia''z AI Diagnostic Research Paper]]'
related:
- '[[assumption/Automated AI Extraction Can Reliably Parse Unstructured Patient Google
  Docs]]'
- '[[task/Extract Structured Patient Data Tables From Database]]'
- '[[task/Build Initial Patient Data Excel Table With Column Headers]]'
- '[[constraint/Key Demographic Variables Only Available Through NLP Extraction From
  Unstructured Text]]'
source: Telia'z Clinic document management system
status: active
type: constraint
---

# Patient Clinical Records Stored as Individual Google Docs Files

## Constraint

Each patient's complete clinical record at Telia'z Clinic is stored as an individual Google Doc file. Each document contains the full clinical record including: intake questionnaire responses, case manager session transcripts, case manager written notes, and AI-generated clinical summaries. This is the primary source format for the research data.

## Source

Telia'z Clinic's document management infrastructure. Rami referenced having "a folder of patient Google Docs files" during the 2025-11-11 meeting with Rivi.

## Implications

- Data extraction for research requires parsing unstructured Google Docs rather than querying a structured database
- Automated AI extraction is needed to convert documents to tabular research data at scale (~6000 records)
- The Google Docs format mixes structured content (questionnaire responses) with unstructured content (transcripts, notes) in a single document
- Bulk processing requires Google Docs API access or document export capability
- Data cannot be directly queried with SQL — it must first be extracted and structured
- This explains why demographic variables require NLP extraction rather than database queries

## Expiry / Review

This constraint reflects the current IT infrastructure. It would change if the clinic migrates to a structured EHR system, but no such migration has been discussed.
