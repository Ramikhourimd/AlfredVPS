---
alfred_tags:
- finance/expenses
- reimbursement/constraints
authority: Oren Taliaz (CEO)
created: '2026-02-26'
janitor_note: 'LINK001 — Telia''z wikilinks are YAML escaping false positives (double
  apostrophe = valid single apostrophe). Base view embeds (learn-constraint.base#Affected
  Projects, #Related) reference _bases/learn-constraint.base which does not exist
  — vault-wide infrastructure issue, embeds preserved.'
name: Company Credit Card Transactions Require CEO-Level Authorization
project:
- '[[project/Telia''z Clinic Israel]]'
related:
- '[[note/Clinic Office Operations Fragment iPad Agreements and Credit Card 2025-12-04]]'
- '[[note/Clinic Office iPad Setup and Payment Processing 2025-12-04]]'
- '[[person/Oren Taliaz]]'
- '[[person/Shira]]'
relationships:
- confidence: 0.75
  context: Both constrain expense recovery
  source: constraint/Company Credit Card Transactions Require CEO-Level Authorization.md
  target: constraint/Older Business Expenses Only One-Third Recoverable Up to 3 Years.md
  type: related-to
- confidence: 0.7
  context: Linked expense policy burdens
  source: constraint/Company Credit Card Transactions Require CEO-Level Authorization.md
  target: constraint/Staff Reimbursement Delays Create Cash Flow Burden on Individual
    Employees.md
  type: related-to
source: Internal policy — observed during office operations discussion
source_date: '2025-12-04'
status: active
type: constraint
---

# Company Credit Card Transactions Require CEO-Level Authorization

## Constraint

The company Visa credit card (card prefix 4580) is registered under Oren Taliaz's name. Transactions on this card require his approval (ishur). Physical card access is limited to Shira and Basel. Staff who need to make purchases must contact Shira by phone or email. In the interim, at least one staff member has been paying from personal funds pending reimbursement.

## Source

Internal financial controls observed during the 2025-12-04 office operations discussion. The authorization chain was explicitly discussed when a payment needed processing.

## Implications

- Purchase requests create a bottleneck through Oren's approval queue
- Staff paying from personal funds creates reimbursement liability and cash flow burden on individuals
- Only Basel and Shira have physical card access — any purchase outside their availability is delayed
- This constraint may slow operational purchases (equipment, subscriptions, office supplies) during scaling

## Expiry / Review

Review when operational financial controls are formalized as part of the organizational restructuring. May be relaxed with delegated spending limits once Basel's operations manager role is fully established.

![[learn-constraint.base#Affected Projects]]
![[learn-constraint.base#Related]]