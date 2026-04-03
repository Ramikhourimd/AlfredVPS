---
alfred_tags:
- healthcare/partnerships
- partnership/constraints
- governance/approvals
authority: Clalit Health Services system architecture
created: '2026-03-15'
name: Clalit Referral System Is Slower and Heavier Than Maccabi Requiring Platform
  Adaptation
project:
- '[[project/Telia''z Clinic Israel]]'
related:
- '[[note/Clalit South Psychiatric Referral and Subscription System Design 2025-11-10]]'
- '[[conversation/Clalit South Referral System Setup Meeting 2025-11-10]]'
- '[[task/Evaluate Platform Adaptation for Clalit Subscription Workflow]]'
- '[[constraint/Clalit Form 17 Requires Manual Approval by District Contact]]'
relationships:
- confidence: 0.6
  context: Shared partnership constraints
  source: constraint/Clalit Referral System Is Slower and Heavier Than Maccabi Requiring
    Platform Adaptation.md
  target: constraint/GP Confed Internal Governance Must Approve Partnership Before
    Execution.md
  type: related-to
- confidence: 0.6
  context: Shared partnership constraints
  source: constraint/Clalit Referral System Is Slower and Heavier Than Maccabi Requiring
    Platform Adaptation.md
  target: constraint/GP Confederation Commercial Agreement Is Hard Gate Before Partnership
    Progress.md
  type: related-to
source: Operational observation during Clalit South partnership setup
source_date: '2025-11-10'
status: active
type: constraint
---

# Clalit Referral System Is Slower and Heavier Than Maccabi Requiring Platform Adaptation

## Constraint

The Clalit Health Services referral and authorization system operates more slowly and with greater process overhead than the Maccabi system that Telia'z has been operating with. This difference requires platform adaptation to accommodate Clalit-specific workflows.

## Source

Identified during the Clalit South partnership setup meeting on 2025-11-10 and the preceding internal preparation on 2025-11-09.

## Implications

- The Telia'z platform, originally built around Maccabi workflows, may need technical modifications to handle Clalit's heavier process requirements
- Staff accustomed to Maccabi's pace may experience friction with Clalit's slower authorization cycles
- Dual-HMO operations require the platform to support both workflow patterns simultaneously
- Platform adaptation evaluation is underway (see linked task)

## Expiry / Review

Active as long as Clalit partnership is operational. May improve if Clalit modernizes their referral system.

![[learn-constraint.base#Affected Projects]]
![[learn-constraint.base#Related]]