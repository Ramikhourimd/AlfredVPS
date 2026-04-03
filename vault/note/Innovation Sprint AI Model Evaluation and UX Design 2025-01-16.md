---
created: '2025-01-16'
description: Innovation team sprint meeting covering AI model comparison (O1 vs Gemini
  2.0 Flash), case manager UX screen design with DSM questionnaire tabs, Maccabi year-2
  tariff changes, Make.com automation pipelines, and onboarding of external advisor
  Yaron Goren.
janitor_note: LINK001 — Telia'z wikilinks are valid (YAML escaping false positive).
  Base view embed (related.base#All) references _bases/related.base which does not
  exist — create base file to enable dynamic views.
name: Innovation Sprint AI Model Evaluation and UX Design 2025-01-16
project: '[[project/Telia''z Innovation Program]]'
related:
- '[[conversation/Innovation Team AI Sprint Meeting 2025-01-16]]'
- '[[person/Rami Khouri]]'
- '[[person/Ahmed Masalha]]'
- '[[person/Li Yamin]]'
- '[[person/Yaron Goren]]'
- '[[person/Ohad Edri]]'
- '[[person/Shira]]'
- '[[person/Oren Taliaz]]'
- '[[person/Nadav Blatt]]'
- '[[person/Shachar]]'
- '[[project/Telia''z AI Clinical Platform]]'
- '[[project/Telia''z Clinic Israel]]'
- '[[org/Telia''z]]'
relationships: []
session: null
status: active
subtype: meeting-notes
tags: []
type: note
---

# Innovation Sprint: AI Model Evaluation and UX Design 2025-01-16

## Context

Innovation team sprint meeting held at the Telia'z clinic office on January 16, 2025. This was the first sprint meeting with newly onboarded external advisor Yaron Goren. The session covered three main workstreams: AI model evaluation, case manager screen redesign, and automation pipeline development.

## 1. AI Model Evaluation Framework

### Model Comparison Table

Rami walked through the evaluation spreadsheet structure for comparing AI-generated psychiatric summaries:

- **Models under test:** O1, O1 Med, Gemini 2.0 Flash
- **Evaluation criteria:** Latency (response time) and Accuracy (clinical quality)
- **Input data:** Transcript from psychiatrist sessions + patient questionnaire data
- **Output:** Generated psychiatric summary (status, discussion, recommendations)

The table is organized per patient with columns for each model's result, latency, and an accuracy score. Rami demonstrated that production data (O1 regular) has been running since month 17 (approximately July-August period), with earlier results being preview/test data.

### Evaluation Methodology

- Rami built a rubric-based evaluation framework where each summary section (Status, Discussion, Recommendations) is scored against defined criteria
- An LLM-based evaluator prompt assesses quality automatically
- Yaron raised an important methodological point: comparing models head-to-head (relative comparison) may capture information lost in standalone scoring. A model that looks like a "7" alone might look better or worse when directly compared to alternatives.
- Decision: Start with independent scoring but consider adding pairwise comparison

### Ideal Output Concept

- Each patient needs a "ground truth" ideal output for scoring
- Currently no gold standard example exists per patient — the psychiatrist's final edited summary serves as the closest reference
- Caveat raised by Yaron: the psychiatrist edits are influenced by what AI model they received (e.g., if they received O1 output, their edits may be biased toward O1 style)

### Chain of Thought Enhancement Pipeline

- After evaluation, underperforming prompts go through an Enhancement cycle
- The Enhancement prompt uses evaluation feedback to iteratively improve the generation prompt
- Rami reported that in previous prompt iterations, one cycle of Chain of Thought enhancement was sufficient to go from basic to near-final quality
- The system is designed to be autonomous: run evaluations over several days, monitor score improvement, and verify that improvements are meaningful

## 2. Case Manager UX Screen Design

### Questionnaire Structure

Li Yamin presented the case manager screen layout based on Rami's 13-topic questionnaire document:

- **Structure:** 13 main topics, each with sub-categories and individual questions
- **DSM section (Topic 5):** Contains approximately 10 sub-categories with symptom-related questions
- **Design approach:** Tab-based navigation instead of vertical scrolling list
- Each tab opens to reveal questions; case manager can navigate freely between topics (no forced sequential order)

### Key Design Decisions

- **Non-sequential navigation:** Case managers should be able to jump between topics based on patient conversation flow. If a patient starts talking about childhood, the case manager should open the childhood tab immediately.
- **Bookmark/flag feature:** Li proposed a marking system where case managers can flag topics to revisit later during the session
- **No fixed questions in UI:** All questions come from the prompt dynamically. The system sends questions per slot from the prompt, allowing Rami to change which questions appear without UI changes.
- **Follow-up questions:** When the questionnaire already has an answer for a topic (marked "likely answer"), the system generates a contextual follow-up question instead of the standard question
- **Team notes feature:** A separate internal comment panel where clinicians (psychiatrists, case managers, Renee) can leave notes about a patient that don't appear in official summaries

### Shira's Clinical Concern

Shira raised that psychiatrists sometimes re-ask symptom questions that case managers already covered, creating redundancy. Rami acknowledged this as a training issue (not a system design issue) and committed to addressing it separately through clinician guidance.

## 3. Maccabi Billing Tariff Changes

Oren raised that Maccabi HMO billing moved to year-2 pricing (a price increase from the initial contract year):

- The first year had one rate; from year 2 onward there is an uplift
- The clinic had not yet updated their billing to the new rate
- Li Yamin and Shira to verify when the anniversary date was and update billing in the Maccabi system accordingly
- The contract was signed in November, so the year-2 rate should already be in effect

## 4. Make.com Automation Pipeline

Rami demonstrated the Make.com automation flow for extracting and processing clinical data:

- **Data sources:** Google Drive (Transcript File Responses, Patient Test folders), Retool CRM
- **Pipeline steps:** Trigger on schedule → iterate over spreadsheet rows → find patient folder → extract log files → parse content → populate evaluation table
- **Current limitation:** File content extraction requires GPT parsing since Rami cannot write code for text parsing directly
- **Ahmad assigned** to build a cleaner version of the Make.com scenario

### Data Structure

- Patient data organized in Google Drive: `Transcript File Responses/Results/[Clinic]/[Patient]/`
- Each patient folder contains: transcripts, AI summaries (from various stages), logs, PDF exports
- Production O1 results identifiable from month 17 onward
- Psychiatrist-edited PDFs represent the "final" version (post-edit)

## 5. Triage/Case Manager Summary (Merkaz Chosen)

- Nadav Blatt wrote the initial triage questionnaire summary prompt over a year ago — it needs updating
- The triage system takes patient questionnaires and produces a summary to help route patients to appropriate clinicians
- Rami wants to design the output to subtly guide the case manager toward specific treatment recommendations (the "Doctor-Nurse Game" pattern Yaron referenced)
- This workstream deferred to the following week

## 6. Sprint Planning and Logistics

### Two-Week Sprint Deliverables

1. **Ahmad:** Populate evaluation table with O1 and Gemini 2.0 Flash results (latency + output), build Make.com automation
2. **Yaron:** Review clinical accuracy of AI summaries, begin working on evaluation methodology
3. **Li Yamin:** Continue building case manager UX screen with tab-based layout; coordinate with Lidar (Retool developer) on implementation feasibility

### Working Arrangement

- Yaron: Works remotely, needs email access and Google Drive/PromptHub permissions
- Ahmad: Works from office 2 days/week (Sunday + Thursday or Monday + Thursday)
- Yaron and Ahmad to coordinate directly; Rami will set up access permissions over the weekend

### UK Expansion Mention

Brief mention that the team also plans to meet with two psychiatrists for the UK market, and that CQC registration (UK clinical quality certification) is needed. Acquiring an existing clinic with CQC status was mentioned as an attractive shortcut.

## Related
![[related.base#All]]
