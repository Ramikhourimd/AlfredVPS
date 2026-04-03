---
alfred_tags:
- maccabi/commitments
- renewal/constraints
- retool/limitations
authority: Maccabi HMO billing requirements
created: '2026-02-26'
janitor_note: 'LINK001 — Telia''z wikilinks are valid (YAML apostrophe escaping false
  positive). Base view embeds (learn-constraint.base#Affected Projects, #Related)
  reference _bases/learn-constraint.base which does not exist — create base file to
  enable dynamic views. ORPHAN001 — no inbound wikilinks; consider linking from project/Telia''z
  Clinic Israel.'
name: Maccabi Commitment Validation Requires Manual Portal Check Against MADAC
project:
- '[[project/Telia''z Clinic Israel]]'
related:
- '[[note/Commitment Renewal Workflow and Feature Rollout Meeting 2025-01-12]]'
- '[[note/Clinic Commitment Renewal Process and Feature Training Discussion 2025-08-01]]'
- '[[constraint/Clinic Revenue Dependent on HMO Contracts With Maccabi and Clalit]]'
- '[[constraint/No System Support for Maccabi Commitment Renewals in Retool]]'
relationships:
- confidence: 0.85
  context: Both Maccabi commitment constraints
  source: constraint/Maccabi Commitment Validation Requires Manual Portal Check Against
    MADAC.md
  target: constraint/Maccabi Follow-Up Commitment Capped at 20 Sessions Per Cycle.md
  type: related-to
- confidence: 0.8
  context: Both highlight Maccabi commitment limitations
  source: constraint/Maccabi Commitment Validation Requires Manual Portal Check Against
    MADAC.md
  target: constraint/No System Support for Maccabi Commitment Renewals in Retool.md
  type: related-to
- confidence: 0.8
  context: Manual process due to workflow gap
  source: constraint/Maccabi Commitment Validation Requires Manual Portal Check Against
    MADAC.md
  target: constraint/No Commitment Renewal Workflow Exists in Retool.md
  type: related-to
- confidence: 0.75
  context: Manual workaround for entry lack
  source: constraint/Maccabi Commitment Validation Requires Manual Portal Check Against
    MADAC.md
  target: constraint/No Renewal Commitment Entry Mechanism Exists in Retool.md
  type: related-to
- confidence: 0.75
  context: Validation tied to entry point gap
  source: constraint/Maccabi Commitment Validation Requires Manual Portal Check Against
    MADAC.md
  target: constraint/No System Entry Point for Commitment Renewal Numbers.md
  type: related-to
source: Operational procedure identified in meetings
source_date: '2025-01-12'
status: active
type: constraint
---

# Maccabi Commitment Validation Requires Manual Portal Check Against MADAC

## Constraint

Every patient commitment (both initial and renewal) must be manually verified against the Maccabi MADAC portal by secretarial staff. Verification confirms:
- The commitment is valid and active
- Sufficient session balance remains
- The commitment is properly approved by Maccabi

Without this validation, sessions may be billed against invalid or insufficient commitments, creating revenue risk. There is no automated integration between the clinic's Retool system and the MADAC portal — each check is a manual login-and-verify process.

## Source

Documented in operational meetings between Rami and Shira (2025-01-12 and 2025-08-01). The validation process exists for initial commitments but was noted as not extending to renewals, creating a gap.

## Implications

- Each commitment check adds secretarial workload (estimated 2-5 minutes per patient)
- At scale (7,000+ patients), manual validation becomes a significant labor bottleneck
- No audit trail exists for validation — if a secretary skips the check, invalid commitments enter the system silently
- Renewal commitments are not validated at all because the system has no place to record them
- Billing disputes with Maccabi become harder to resolve without documented validation timestamps

## Expiry / Review

This constraint persists as long as Maccabi does not offer API-based commitment verification. Review if Maccabi introduces electronic validation capabilities or if the clinic builds automated screen-scraping validation.

![[learn-constraint.base#Affected Projects]]
![[learn-constraint.base#Related]]