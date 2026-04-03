---
approved_by: []
based_on:
- '[[conversation/Clinic Platform Referral Form and System Issues Discussion 2025-11-10]]'
- '[[synthesis/Clinical System Complaints Cluster Around Data Loss and Authentication
  Not Performance]]'
challenged_by: []
confidence: high
created: '2026-03-10'
decided_by:
- '[[person/Rami Khouri]]'
janitor_note: 'Had double frontmatter — second YAML block in body contained populated
  values. Merged populated values into primary frontmatter. Body still contains the
  duplicate YAML block that should be manually removed. Also ORPHAN001: no inbound
  links — may need to be linked from related notes.'
name: Structured Complaint Collection Required Before R&D Escalation
project:
- '[[project/Telia''z AI Clinical Platform]]'
related:
- '[[task/Gather Secretary and Clinic Staff System Requirements]]'
session: null
source: Rami Khouri — directive to Shira during system issues discussion
source_date: '2025-11-10'
status: final
supports:
- '[[decision/Add Innovation Team Representative to Psychiatrist Communication Group]]'
tags: []
type: decision
---

---
type: decision
status: final
confidence: high
source: "Rami Khouri — directive to Shira during system issues discussion"
source_date: 2025-11-10
project: ["[[project/Telia'z AI Clinical Platform]]"]
decided_by: ["[[person/Rami Khouri]]"]
approved_by: []
based_on: ["[[conversation/Clinic Platform Referral Form and System Issues Discussion 2025-11-10]]", "[[synthesis/Clinical System Complaints Cluster Around Data Loss and Authentication Not Performance]]"]
supports: ["[[decision/Add Innovation Team Representative to Psychiatrist Communication Group]]"]
challenged_by: []
session:
related: ["[[task/Gather Secretary and Clinic Staff System Requirements]]"]
created: "2026-03-10"
tags: []
---

# Structured Complaint Collection Required Before R&D Escalation

## Context

Psychiatrists were reporting system complaints through informal WhatsApp channels with no structure or prioritization. Issues included slow Retool performance, deleted AI summaries, system freezing, and authentication lockouts. Without structured collection, R&D (Shachar) received fragmented, unprioritized reports making it difficult to allocate development resources effectively.

## Options Considered

1. **Continue ad-hoc WhatsApp reporting** — psychiatrists flag issues as they encounter them, Shachar responds reactively
2. **Structured complaint compilation** — designated person compiles a prioritized list before escalating to R&D

## Decision

Rami directed Shira to compile a structured, prioritized complaint list from psychiatrists before escalating to R&D. System complaints must be collected, deduplicated, and ranked by impact before being presented for development triage.

## Rationale

Ad-hoc complaints via WhatsApp create noise and make it impossible to identify which issues have the highest clinical and operational impact. A structured list enables Shachar to allocate contractor and development resources to the highest-value fixes. This also connects to adding a representative (Stav Zamir) to the psychiatrist communication group for direct visibility.

## Consequences

- Shira becomes the complaint intake point for psychiatrist system issues
- R&D receives actionable, prioritized input rather than scattered messages
- Creates a slight delay between complaint and escalation (collection period)
- Enables data-driven prioritization aligned with the three-track improvement framework

---
![[learn-decision.base#Based On]]

![[learn-decision.base#Related]]
