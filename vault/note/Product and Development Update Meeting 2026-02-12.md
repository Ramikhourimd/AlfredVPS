---
created: '2026-02-12'
description: Comprehensive product backlog review between Rami and Rivi covering AI
  agents, KPI dashboards, patient file uploads, WhatsApp bot, complex patient protocols,
  and AI summary factual checking
janitor_note: 'LINK001: Telia''z wikilinks (project, org) are YAML escaping false
  positives (files exist). related.base#All embed references missing _bases/related.base
  — vault-wide gap.'
name: Product and Development Update Meeting 2026-02-12
project: '[[project/Telia''z AI Clinical Platform]]'
related:
- '[[conversation/Product Development Update Meeting 2026-02-12]]'
- '[[person/Rami Khouri]]'
- '[[person/Rivi Idelman]]'
- '[[org/Telia''z]]'
- '[[project/Telia''z Innovation Program]]'
- '[[project/Telia''z Clinic Israel]]'
- '[[person/Roy Shur]]'
- '[[person/Stav Zamir]]'
- '[[person/Shachar]]'
- '[[person/Shmulik]]'
- '[[person/Ohad Edri]]'
- '[[person/Basel Kanaaneh]]'
- '[[person/Dekkel Taliaz]]'
relationships: []
session: null
status: active
subtype: meeting-notes
tags: []
type: note
---

# Product and Development Update Meeting 2026-02-12

## Context

Biweekly product sync between Dr. Rami Khouri (Innovation / Clinical) and Rivi Idelman (Innovation Team Lead / Product). They reviewed the product backlog, discussed ongoing development workstreams, and aligned on priorities for the coming weeks.

## 1. Dashboard Status

- **Basel's financial dashboard** — Considered closed for now. Rami built a dashboard for Basel that includes percentage metrics (no-show, follow-up, etc.), but it is not intended for further development at this time. Only the payment-related data portion is being removed from the backlog.
- **KPI dashboards** — Roy Shur is working on defining KPIs, mapping them to database metrics, and identifying gaps. Some metrics exist in the database already; others will require new features or composite views (joining multiple entities). Shmulik may need to create additional database views when the KPI spec is ready.
- **Rivi to design frontend UX** — Rami asked Rivi to work with Roy on the frontend design and presentation of the KPI dashboard. The dashboard Rami demoed previously was a prototype only — Rivi should produce a proper UX spec. Rami will share the design documents (to-do list, implementation plan, tasks) for Basel's dashboard as a starting point.

## 2. AI Agents — File Upload Classification

- **Patient file upload feature** — Shmulik has nearly finished development. Rivi is now running tests. This is close to rollout.
- **File classification agent** — Rami proposed an AI agent that classifies and summarizes uploaded patient files (PDFs, images, etc.). This requires a preprocessing step (image/PDF to text conversion) before the content can be fed as additional input to the clinical summary agent.
- **API dependency** — The agent infrastructure needs APIs from Shachar's R&D team. Rami plans to meet Shachar on Sunday to figure out the technical approach. Once the Innovation team has its own agent infrastructure, it will be less dependent on Shachar for these tasks.
- **Backlog item exists** — "AI Agents for Upload File Classification and Summarization" is already in the backlog but not yet prioritized.

## 3. Case Manager (CM) Pilot

- Stav Zamir confirmed that the CM summary pilot has started.
- Agenda generation is not yet active — Rivi will check on status in her upcoming meeting at 2:30.
- Rami has not met with the CM team in two weeks, so status details are limited.

## 4. WhatsApp Bot / QA

- **Call transcription** — Amit (working with Shachar) has implemented call transcription capabilities via the external system.
- **Decision tree** — Amit is now developing the WhatsApp decision tree flow (menu-based navigation for appointment booking, changes, etc.).
- **Chatbot Q&A content** — Adi was primarily responsible; Shira reviewed and added comments this week. Content still needs redrafting before it is ready.

## 5. Complex Patient Protocols

Basel requested a feature to alert psychiatrists about complex patients. Rami outlined a comprehensive multi-phase approach:

### Definition Phase
- Literature review needed to define what constitutes a "complex" or "unsuitable" patient
- Internal data analysis to understand natural dropout patterns (when patients leave, at which stage, why)
- This analysis will inform the protocol design

### Clinical Checkpoint Flow
At each stage of the patient journey, the system will perform automated checks against the protocol criteria:

1. **Questionnaire stage** — Automated check. If flagged, patient sees recommendations and must sign an additional consent form to continue. If patient refuses to sign, they cannot proceed (their choice).
2. **Case manager stage** — Case manager explains recommendations verbally, records that they completed the checklist. If patient refuses consent, the Medical Director must be involved before the patient can be discharged.
3. **Psychiatry intake stage** — This is the natural decision point for discharge or continuation. Only a psychiatrist can formally discharge a patient.

### Key Design Principle
- Discharge can only happen after a medical examination (psychiatry intake)
- Even if flagged earlier (questionnaire, case manager), the patient cannot be discharged before reaching psychiatry
- This protects against premature patient loss and ensures medical oversight

### Impact on Operations
- Primary load reduction comes from reducing follow-up sessions, not intakes (patients are already in pipeline)
- This is a long-term development requiring protocol formalization first, then feature implementation

## 6. AI Summary Factual Checking — Color-Coded Approach

Rami proposed a factual checking layer for AI-generated clinical summaries with visual color coding:

- **Green** — Verified: content corroborated by transcript
- **Red** — Hallucination: content with no reference in transcript
- **Orange** — Interpretation: AI-generated inference or paraphrasing

### Implementation Plan
- Rami will build the factual-checking agent (working with Stav on prompts and Ohad on the technical build)
- The agent needs to receive transcript data from Shachar's system
- Once the agent produces color-coded output, Rivi will design the frontend presentation
- This approach was preferred over a confirmation popup because it requires no additional clicks from psychiatrists — they can see the reliability of each section while editing

### Prioritization
- Will be discussed in Sunday's backlog meeting; Rami expects Dekkel will also support this feature

## 7. Inter-Session Documentation

Rami identified a gap in the clinical platform: there is no way to document events that happen between sessions (e.g., a patient calls, a psychiatrist consults Rami about a case). Currently documentation is tied to meeting entities only.

**Proposed solution:** Add a new meeting type called "inter-session documentation" (between-appointment notes) — a free-text entity not attached to a scheduled session. This would allow psychiatrists to open a text box and save notes about between-session events directly in the patient record.

The internal task system was considered but rejected since tasks feed into a different workflow and don't appear as clinical documentation.

## Key Cross-Team Dependencies

| Dependency | From | To | Status |
|-----------|------|-----|--------|
| File upload classification API | Innovation | R&D (Shachar) | Rami meeting Sunday |
| Database views for KPIs | Innovation (Roy) | R&D (Shmulik) | Pending KPI spec |
| Factual check agent transcript access | Innovation | R&D (Shachar/Ohad) | Not started |
| WhatsApp decision tree | Amit | Shachar | In development |
| Chatbot Q&A content | Adi/Shira | Product | Needs redrafting |

## Related
![[related.base#All]]
