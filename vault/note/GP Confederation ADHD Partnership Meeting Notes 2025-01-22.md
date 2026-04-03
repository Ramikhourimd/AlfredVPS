---
alfred_tags:
- healthcare/adhd
- partnerships/uk
- systems/case-management
created: '2026-02-26'
description: Comprehensive notes from in-person meeting between Telia'z leadership
  and GP Confederation Leeds to discuss ADHD telepsychiatry service partnership. Covers
  Israel proof of concept, proposed UK pathway, commercial model, clinical governance,
  and next steps.
janitor_note: LINK001 — Telia'z wikilinks (project/Telia'z UK Expansion, org/Telia'z)
  are valid — YAML double-apostrophe escaping false positive, targets exist. Base
  view embed (related.base#All) references _bases/related.base which does not exist
  — systemic vault infrastructure gap. Embed preserved per policy.
name: GP Confederation ADHD Partnership Meeting Notes 2025-01-22
project: '[[project/Telia''z UK Expansion]]'
related:
- '[[conversation/GP Confederation ADHD Service Partnership Meeting 2025-01-22]]'
- '[[org/GP Confederation Leeds]]'
- '[[org/Telia''z]]'
- '[[org/DigiSave]]'
- '[[person/Adiel Levin]]'
- '[[person/Jason Brook]]'
- '[[person/Rebecca Wilson]]'
- '[[person/Rami Khouri]]'
- '[[person/Alex Lellouche]]'
- '[[person/Jim Barwick]]'
- '[[person/Sean Rejabris]]'
- '[[person/Dr. Lucy Clemens]]'
- '[[person/Colin Glass]]'
relationships:
- confidence: 0.75
  context: ADHD initiatives and tech prioritization
  source: note/GP Confederation ADHD Partnership Meeting Notes 2025-01-22.md
  target: note/Retool Prioritization and Data Access Discussion 2025-12-05.md
  type: related-to
- confidence: 0.75
  context: ADHD initiatives and tech prioritization
  source: note/GP Confederation ADHD Partnership Meeting Notes 2025-01-22.md
  target: note/Retool System Prioritization and Data Access Discussion 2025-12-05.md
  type: related-to
- confidence: 0.85
  context: Shared ADHD partnership themes
  source: note/GP Confederation ADHD Partnership Meeting Notes 2025-01-22.md
  target: note/UK NHS ADHD Pathway Design and OMG Partnership 2025-07-03.md
  type: related-to
session: null
status: active
subtype: meeting-notes
tags: []
type: note
---

# GP Confederation ADHD Partnership Meeting Notes 2025-01-22

In-person meeting at GP Confederation offices in Leeds. Telia'z leadership presented their Israel-proven telepsychiatry model and proposed an ADHD service partnership with GP Confederation to serve the Leeds population and potentially Right to Choose referrals nationally.

## Context

Telia'z (trading as Healthy Mind for the clinical service) has been operating a virtual psychiatry clinic in Israel for ~2 years. The UK expansion effort was paused for ~18 months during the Israel-Gaza conflict, during which Telia'z pivoted to provide free psychiatric services to displaced populations. Now re-engaging with UK partners.

Prior relationship: Rebecca Wilson (DigiSave) helped Telia'z obtain DTAC compliance. Jason Brook (ICB Medical Director) connected Telia'z with GP Confederation. A previous virtual meeting with Jim Barwick happened before Christmas 2024.

## Israel Service Model Presented

Key statistics shared by Adiel:
- **2,700+ unique patients** in the last 12 months
- **9,600+ clinical sessions** delivered
- **3.5-day average** from first contact to seeing a psychiatrist
- **81.3% Net Promoter Score** (vs. ~53% healthcare benchmark)
- **800+ patients treated per month**
- **60% operational time savings** for psychiatrists
- **10 part-time psychiatrists** handling the entire volume
- **550% growth** over 12 months
- **2,000+ monthly sessions** as of the latest week
- Languages: Hebrew, Arabic, English, Russian

### Three-Step Workflow
1. **Digital questionnaire** — serves as triage (ASRS, DIVA for ADHD)
2. **Case manager session** (30-45 min) — psychologist, social worker, nurse practitioner, or junior psychiatrist conducts initial intake. AI transcribes and summarizes.
3. **Psychiatrist consultation** (30-60 min) — psychiatrist receives AI-generated summary and agenda recommendations. Reviews, diagnoses, creates treatment plan. AI generates final report in ~10 seconds post-session.

The AI system:
- Real-time transcription with no audio storage (privacy)
- Learns individual practitioner's writing style over time
- Algorithmic and traceable — not a black box
- Decision support only, never autonomous clinical decisions
- References from transcript and literature for all recommendations

## UK Partnership Model Discussed

### Proposed Structure
- GP Confederation would be the **CQC-registered provider** for the joint ADHD service
- Telia'z would operate **under GP Confed's CQC** (not as a subcontractor, but as embedded clinical/digital capability)
- Telia'z provides: psychiatry workforce (6-7 UK-registered psychiatrists ready), AI platform, clinical workflow
- GP Confed provides: CQC registration, local clinical governance, referral filtering/triage, local face-to-face capacity

### Two Revenue Streams
1. **Leeds-based referrals** — patients referred by Leeds GPs, filtered by Confed. Revenue share with percentage back to GP Confed.
2. **Right to Choose referrals** — patients from anywhere in England choosing this service. Different revenue split, potentially more favorable for Confed.

### Pricing Benchmark
- Low-end Right to Choose tariff: ~£360 for intake, ~£180 for follow-up (benchmarked against Psychiatry UK)
- Telia'z claims to be ~2x more cost-efficient than competitors due to technology
- Goal: deliver within existing NHS tariffs while returning percentage to GP Confed for local projects

## Key Concerns Raised

### From Dr. Lucy Clemens
- **Medication management**: Service must include starting medications, not just pass recommendations to GPs. Rami confirmed they do prescribing and titration.
- **Ongoing monitoring**: Annual reviews needed within the service model. Confirmed — Telia'z handles follow-ups for ~6 months then transitions to GP with re-referral option.
- **AI clinical decisions**: Concerned about AI making diagnostic decisions autonomously. Reassured that AI is decision-support only, with full traceability.
- **Profit motive**: Asked what Telia'z does with profits. Adiel shared the emotional backstory of providing free services during the conflict. Currently not profitable — reinvesting in technology.
- **Future-proofing for primary care**: NHS direction is moving ADHD management into primary care. Model needs to evolve to support GPs, nurses, pharmacists with psychiatrist supervision.

### From Sean Rejabris
- **Face-to-face preference**: ICB commissioners heavily weigh face-to-face services in procurement bids. Need to address this in the tender response.
- **NICE guidelines**: New digital/AI guidance for neurodevelopmental services released ~1 month prior. Need compliance verification.
- **UK registered body requirement**: CQC compliance requires UK-registered entities for subcontracted work. Resolved by working under Confed's CQC.
- **Workforce model**: UK model uses multi-professional diagnosis (not psychiatrist-only). Telia'z confirmed flexibility.

### From Jim Barwick
- **Why not DIY?**: GP Confed could theoretically build their own service. Counter: Telia'z solution is ready now, compliant, proven, scalable — speed to market advantage.
- **Why not other vendors?**: Market comparison needed. Rebecca asserted she's seen nothing comparable in the UK market.
- **Clinical governance**: Needs clear governance model for the joint service under CQC.
- **Revenue model**: Must make commercial sense — cost to local NHS within limits, revenue flowing back to Confed to support GP practices.

## Leeds ADHD Waiting List Context

Sean Rejabris revealed the Leeds ADHD waiting list is **25 years** at current referral rates. This shocked the Telia'z team and dramatically underscored the scale of the opportunity. Each year of new referrals adds approximately 23 more years to the backlog.

## Right to Choose Dynamics

- Right to Choose is enshrined in NHS legislation — cannot be capped per region
- It's bankrupting local ICBs because patients choose providers outside their local system, and the local ICB still pays
- Creating a local commissioned pathway with GP Confed could help manage this by:
  - Filtering out patients who don't need diagnosis
  - Keeping assessments local and virtual
  - Reducing unnecessary Right to Choose referrals to external providers

## Next Steps Agreed

1. **Virtual demo**: Sean requested a Teams demonstration of the Telia'z platform — sample reports, workflow walkthrough, AI capabilities
2. **Pathway design work**: Lucy and Sean to define clinical pathway requirements. Rebecca to spend a day with Confed team working through the model.
3. **Compliance review**: Rebecca to sit down and map out information governance, NICE compliance, and CQC integration requirements
4. **Commercial framework**: Jim to involve Director of Finance for revenue share modeling. Internal Confed governance processes for forming the partnership.
5. **Tender preparation**: Build the bid with technology and psychiatry supervision referenced (not necessarily naming Telia'z until contract won). Tender expected within 4 weeks.
6. **Neurodiversity tech showcase**: Sean mentioned a West Yorkshire-wide event the following week — potential opportunity for visibility.

## Notable Side Details

- Colin Glass (Leeds British Israeli Chamber of Commerce chair) attempted to meet with Adiel that evening — scheduling didn't work out
- Previous Telia'z UK work included a proof of concept with Ardash (LYCFT — Leeds and York Community Foundation Trust) in South Yorkshire/Sheffield
- Rami disclosed he personally has ADHD, which motivated the workflow optimization approach
- Rebecca's son Theodore (age 7) is on the ADHD waiting list — personal motivation for the partnership
- Telia'z raised ~$600K in 3 days after Oct 7 to fly back over 1,000 Israelis stranded abroad, then pivoted their private service to free mental health support

## Related
![[related.base#All]]