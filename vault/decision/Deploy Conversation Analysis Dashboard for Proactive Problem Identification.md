---
alfred_tags:
- healthcare/operations
- staff/issue-management
- proactive/problem-detection
approved_by: []
based_on:
- '[[note/Operational Processes and Haifa Office Planning Notes 2025-11-09]]'
challenged_by: []
confidence: medium
created: '2026-03-15'
decided_by:
- '[[person/Rami Khouri]]'
janitor_note: 'LINK001 — Telia''z wikilinks are valid (YAML single-quote escaping
  false positive). Base view embeds (learn-decision.base#Based On, #Related) reference
  _bases/learn-decision.base which does not exist — vault-wide infrastructure gap,
  embeds preserved. NOTE: Duplicate base view embeds at end of file — human should
  remove the second set.'
name: Deploy Conversation Analysis Dashboard for Proactive Problem Identification
project:
- '[[project/Telia''z Clinic Israel]]'
- '[[project/Telia''z Innovation Program]]'
related:
- '[[person/Rivi Idelman]]'
- '[[conversation/Operational Processes and Office Planning Discussion 2025-11-09]]'
relationships:
- confidence: 0.7
  context: Both enhance operational issue identification/reporting
  source: decision/Deploy Conversation Analysis Dashboard for Proactive Problem Identification.md
  target: decision/Empower Renee to Report Operational Issues Directly to Management.md
  type: related-to
session: null
source: Rami Khouri, Oren Taliaz, Dekkel Taliaz
source_date: '2025-11-09'
status: draft
supports:
- '[[decision/Build Frustration Detection Agent to Route Staff Issues Automatically]]'
tags: []
type: decision
---

# Deploy Conversation Analysis Dashboard for Proactive Problem Identification

## Context

Operational problems at Telia'z Clinic Israel were being surfaced reactively — staff had to report issues up the chain, where they often got bottlenecked through Shira. The team needed a mechanism to proactively identify and categorize problems without relying on manual reporting.

## Options Considered

1. **Manual review** — Managers periodically review meeting notes and communications for issues
2. **Structured reporting forms** — Staff submit issues through standardized forms
3. **Automated conversation analysis** — AI-powered dashboard that processes transcripts automatically

## Decision

Build and deploy an automated conversation analysis dashboard for Rivi Idelman. The tool analyzes conversation transcripts from clinic operations, identifies problems mentioned in conversations, assigns responsibility for each identified problem, and proposes solutions based on the analysis.

## Rationale

Automated transcript analysis shifts from reactive to proactive problem identification. Instead of waiting for problems to be reported up the chain, the dashboard surfaces them automatically from existing communication data. This is especially valuable in a remote telepsychiatry environment where informal hallway conversations don't happen.

## Consequences

- Problems are identified and categorized without requiring staff to formally report them
- Responsibility assignment creates accountability without manual triage
- The tool creates a data trail of recurring issues for pattern analysis
- Depends on quality of conversation transcription (mixed-language transcription remains a known constraint)
- This concept was later expanded into the broader Frustration Detection Agent proposal (2025-11-13)

![[learn-decision.base#Based On]]
![[learn-decision.base#Related]]

---
![[learn-decision.base#Based On]]

![[learn-decision.base#Related]]
