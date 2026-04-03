---
alfred_tags:
- taliaz/knowledge-base
- data-ingestion
- protocols
description: 'End-to-end protocol and SOP authoring engine for Taliaz HealthyMind.
  Produces precise, context-grounded, regulation-compliant clinical, operational,
  and governance protocols. Uses a 7-phase pipeline: scope, context gathering, regulatory
  cross-reference, drafting, gravity stress-test, validation, and publishing. Integrates
  live data from Supabase KB, Gmail, Slack, BigQuery, and Google Drive. Aligned with
  Israeli MOH, PPA, and HMO requirements. Triggers on: write protocol, create protocol,
  new SOP, draft SOP, protocol for, write a procedure for, formalize protocol, upgrade
  protocol, finalize SOP, book of procedures.'
name: taliaz-protocol-writer
---

# Taliaz Protocol Writer

Produces production-grade protocols and SOPs for Taliaz HealthyMind. Every protocol passes through a 7-phase pipeline that ensures it is grounded in organizational reality, compliant with Israeli regulations, and stress-tested before publication.

## When to Use This Skill

| Trigger | Action |
|---------|--------|
| "Write a protocol for X" | Full 7-phase pipeline |
| "Create an SOP for X" | Full 7-phase pipeline |
| "Upgrade/finalize the X protocol" | Start at Phase 2 (context) with existing draft as input |
| "What's the status of the X protocol?" | Read `references/protocol_registry.md`, query KB |
| "Review this protocol draft" | Start at Phase 5 (gravity) |

## Pipeline Overview

```
Phase 1: SCOPE    → Classify protocol, identify domain & regulatory context
Phase 2: CONTEXT  → Gather live org data (KB, Gmail, Slack, Drive, BigQuery)
Phase 3: REGULATE → Cross-reference Israeli MOH, PPA, HMO requirements
Phase 4: DRAFT    → Generate protocol using Taliaz SOP template
Phase 5: GRAVITY  → Stress-test against operational reality
Phase 6: VALIDATE → Run compliance checklist & cross-reference playbook
Phase 7: PUBLISH  → Finalize, version, optionally ingest to KB
```

---

## Phase 1: SCOPE

Classify the protocol request before writing anything.

**1.1 Identify the protocol domain:**

| Domain | Examples | Regulatory Weight |
|--------|----------|-------------------|
| Clinical | Intake, ADHD, suicide risk, prescribing, telemedicine | High — MOH, PPA, HMO |
| Operational/HR | Onboarding, scheduling, offboarding, compensation | Medium — labor law, privacy |
| Quality/Compliance | QA audit, data privacy, informed consent | High — PPA, MOH |
| Regulatory/HMO | Maccabi compliance, MOH reporting, IRB | Very High — external authority |
| Innovation/AI | Prompt governance, human-in-the-loop, AI deployment | High — PPA, MOH SaMD |

**1.2 Check the protocol registry:**

Read `references/protocol_registry.md` to determine:
- Does this protocol already exist? What is its current status?
- What SOP anchors already cover parts of this protocol?
- Who are the designated owners?
- What is the playbook decision (adopt now / controlled draft / convert / create new)?

**1.3 Determine the workflow path:**

- **New protocol** (status = "Pending / Mentioned Only") → Full pipeline, Phases 1–7
- **Upgrade existing draft** (status = "Partially Ready") → Gather existing content first, then Phases 2–7
- **Validate ready protocol** (status = "Ready") → Phases 5–6 only (gravity + validate)

---

## Phase 2: CONTEXT

Gather all available organizational context before writing. This is what makes protocols precise and grounded.

**2.1 Query Supabase KB** (use `taliaz-kb-query` skill):

```bash
# Search for existing protocol content, decisions, and discussions
python3 /home/ubuntu/skills/taliaz-kb-query/scripts/query_supabase.py "memory_l1_core" "source_file,Meeting_date,topics,events,facts,category" '{"topics": "ilike.%[protocol topic]%"}'

# Find responsible people
python3 /home/ubuntu/skills/taliaz-kb-query/scripts/query_supabase.py "responsibilities" "employee_id,responsibility_area,scope,authority_level" '{"responsibility_area": "ilike.%[topic]%"}'

# Check institutional knowledge
python3 /home/ubuntu/skills/taliaz-kb-query/scripts/query_supabase.py "institutional_knowledge" "knowledge_area,details,importance,source_employee_id" '{"knowledge_area": "ilike.%[topic]%"}'

# Check for past project attempts
python3 /home/ubuntu/skills/taliaz-kb-query/scripts/query_supabase.py "projects" "name,status,owner_employee_id,description" '{"name": "ilike.%[topic]%"}'
```

**2.2 Query external sources** (recommended for clinical and high-risk protocols):

- **Gmail**: `search_gmail_messages(q="[protocol topic] OR [Hebrew term]")`
- **Slack**: `slack_search_channels` with `query="[topic]"` and `channel_types="public_channel,private_channel"`
- **Google Drive**: `rclone ls "manus_google_drive:Protocols/" --config /home/ubuntu/.gdrive-rclone.ini`
- **BigQuery** (for data-backed protocols): Use `taliaz-bigquery-sql` skill for operational metrics

**2.3 Gather existing SOP content:**

If the protocol registry shows existing SOP anchors (e.g., SOP-CLIN-010, SOP-CRISIS-002), read the corresponding chapter content from `references/sop_chapters.md` to avoid contradicting or duplicating existing procedures.

---

## Phase 3: REGULATE

Cross-reference with the Israeli regulatory framework. Read `references/israeli_regulatory_framework.md` for the full reference.

**3.1 Mandatory compliance checks by domain:**

| Domain | Must Check |
|--------|-----------|
| Clinical | Patients' Rights Law (1996), MOH licensing, MOH Director General circulars, informed consent |
| Telemedicine | PPA telehealth data protection guidelines (2022/2024), platform security, patient location |
| Data/Privacy | Protection of Privacy Law (1981 + Amendment 13), Data Security Regulations (2017), Health Information Mobility Law (2024) |
| Mental Health | Mental Health Treatment Act, Community Mental Health Rehabilitation Law (2000), involuntary hospitalization |
| AI/SaMD | Medical Devices Law (2012) if AI outputs influence clinical decisions, PPA AI data processing |
| HMO-specific | Maccabi/Clalit contract terms, package entitlements, billing rules |

**3.2 Search for current regulatory updates:**

For clinical and regulatory protocols, always search the web for the latest MOH circulars and PPA guidelines:
```
Search: "Israel Ministry of Health [topic] circular 2025 2026"
Search: "משרד הבריאות [Hebrew topic] חוזר מנכל"
```

**3.3 Embed regulatory references** in the protocol's "Regulatory Basis" section citing specific laws, regulations, or guidelines.

---

## Phase 4: DRAFT

Generate the protocol using the Taliaz SOP template.

**4.1 Use the template:** Read and apply `templates/protocol_template.md`.

**4.2 Writing standards:**

- **Language**: English with Hebrew operational terms in parentheses (e.g., "intake session (אנטק)")
- **Specificity**: Use real names, real systems (Xano, Zoho CRM, BigQuery), real rates, real timelines from KB
- **No aspirational content**: Mark anything not yet implemented as [PLANNED] or [ASPIRATIONAL]
- **Cross-references**: Link to related SOPs by ID (e.g., "See SOP-CLIN-010")
- **Known issues**: Document system bugs, workarounds, constraints (Zoho email routing bug, Xano analytics freeze)
- **Compensation/rates**: Reference the current 4-tier table when relevant

**4.3 RACI assignment rules:**

Query KB for actual assignments. Default patterns:
- **Clinical**: Accountable = Shira (Clinical Director) or Rami (CMIO for AI/innovation); Informed = Dekel (CEO)
- **Operational**: Accountable = Basel (General Manager); Informed = Dekel
- **Quality/Compliance**: Accountable = Roy (COO); Informed = Dekel
- **Innovation/AI**: Accountable = Rami (CMIO); Informed = Dekel

---

## Phase 5: GRAVITY

Stress-test the draft against operational reality. **This phase is mandatory.**

**5.1 Deconstruct the draft:**

| Component | Question |
|-----------|----------|
| Problem | Does this protocol solve a real, documented problem? |
| Process | Are the steps executable with current systems and staff? |
| Assumptions | What must be true for this to work? Are those things actually true? |
| KPIs | Are the metrics measurable with current data infrastructure? |
| RACI | Do the assigned people actually have the authority and capacity? |

**5.2 Evidence-based challenges:**

- **Process conflicts**: Query KB for related protocols that might contradict this one
- **Role validation**: Query `responsibilities` and `expertise_areas` to confirm assignments
- **Resource reality**: Use BigQuery to check capacity assumptions
- **Historical precedent**: Check `projects` table for archived/failed attempts

**5.3 Run the pre-mortem:**

```bash
python3 /home/ubuntu/skills/taliaz-protocol-writer/scripts/pre_mortem.py "[Protocol Title]" "[One-sentence description]"
```

**5.4 Synthesize the critique** covering: verdict, assumption attacks, blind spots, pre-mortem, and one uncomfortable question. Revise the draft to address all findings.

---

## Phase 6: VALIDATE

Run the compliance and consistency checklist.

```bash
python3 /home/ubuntu/skills/taliaz-protocol-writer/scripts/validate_protocol.py "[path_to_protocol.md]"
```

The script checks three categories:

**Regulatory compliance**: Regulatory basis section present, patient consent addressed, data handling specified, emergency escalation defined, HMO rules included.

**Organizational consistency**: SOP ID format, RACI uses current employees, systems are current (Xano/BigQuery/Zoho), compensation rates match, no contradictions with existing SOPs, known issues documented, version control metadata present.

**Quality standards**: No unmarked aspirational content, exception handling defined (minimum 3 scenarios), KPIs are measurable, training requirements specified, review cadence defined.

---

## Phase 7: PUBLISH

**7.1 Version the document:**

```
Version: 1.0
Status: Controlled Draft | Validated | Ready
Date: [Current date]
Author: Dr. Rami Khouri, CMIO
Approved by: [Approver name and role]
Next review: [Date + 6 months]
```

**7.2 Save** as `/home/ubuntu/[protocol_name]_v1.0.md`

**7.3 Optional actions:**
- **Ingest to KB**: Use `taliaz-doc-processor` skill
- **Upload to Drive**: `rclone copy [file] "manus_google_drive:Protocols/" --config /home/ubuntu/.gdrive-rclone.ini`
- **Distribute via Slack**: Post to relevant channels
- **Add review reminder**: Create Google Calendar event for next review date

---

## Bundled Resources

| Resource | Purpose | When to Read |
|----------|---------|-------------|
| `references/protocol_registry.md` | All 40 protocols with status, owners, SOP anchors, playbook decisions | Phase 1 (always) |
| `references/israeli_regulatory_framework.md` | Israeli laws, regulations, guidelines for healthcare protocols | Phase 3 (clinical/regulatory) |
| `references/sop_chapters.md` | Summary of all 96 SOPs across 16 chapters | Phase 2 (checking existing anchors) |
| `templates/protocol_template.md` | Standardized Taliaz protocol template | Phase 4 (always) |
| `scripts/pre_mortem.py` | Structured pre-mortem analysis | Phase 5 (always) |
| `scripts/validate_protocol.py` | Automated validation checklist | Phase 6 (always) |