---
cluster_sources:
- '[[conversation/Alfred Chat — Knowledge Base Q&A Session

  Knowledge Base Q&A Session Refin 2026-03-09]]'
- '[[contradiction/Rami Location Record Says Beirut But Phone Is Israeli]]'
- '[[constraint/Alfred Lacks Access Controls on Personal Data Disclosure]]'
confidence: medium
created: '2026-03-10'
janitor_note: 'LINK001 — conversation link has embedded newline in cluster_sources
  (filename contains linebreak). Target file exists but wikilink format is malformed.
  Base view embeds (learn-synthesis.base#Sources, #Related) reference _bases/learn-synthesis.base
  which does not exist — vault-wide infrastructure issue, embeds preserved. ORPHAN001
  — no inbound wikilinks; consider linking from project/Alfred Development.'
name: Interactive QA Audits Are an Effective Vault Curation Workflow
project:
- '[[project/Alfred Development]]'
status: draft
supports:
- '[[assumption/Alfred User Knowledge Derived From Vault Graph Not User Profile]]'
type: synthesis
---

# Interactive Q&A Audits Are an Effective Vault Curation Workflow

## Insight

A structured Q&A audit pattern — where Alfred systematically scans vault records, identifies data gaps or inconsistencies, then asks the user targeted questions to resolve them — is an effective method for improving vault data quality. The Knowledge Base Q&A Session on 2026-03-09 demonstrated this: Alfred found missing phone number, flagged a location contradiction (Beirut vs Israeli phone), and asked precise questions with clear options.

## Evidence

- The Q&A session identified a missing phone field in the person record and successfully collected it
- The session surfaced the Beirut/Israel location contradiction (already captured separately)
- The structured format (numbered questions, explicit options like "Share it / Don't store it / Not relevant") made it easy for the user to respond quickly
- One tool error occurred during the session (vault edit failed), showing the workflow needs resilient error handling

## Implications

- This pattern could be formalized as a recurring vault curation process
- Q&A audits complement automated curation by catching gaps that require human input
- The pattern should include graceful retry logic for tool failures mid-session
- Could be extended to audit cross-record consistency (not just single-record gaps)

## Applicability

- Alfred Development — as a core vault curation workflow
- Any project with person, org, or location records that may have incomplete data

![[learn-synthesis.base#Sources]]
![[learn-synthesis.base#Related]]
