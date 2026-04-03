---
alfred_tags:
- psychiatry/conference
- mental-health/clinical
- depression/treatment
created: '2026-03-02'
date: '2025-11-13'
description: 'Conference voice memo covering multiple substantive discussions: NLP
  sentiment analysis methodology for clinical outcome tracking, ethnic disparities
  in psychiatric hospitalization (Arab vs Jewish), Telia''z clinic scale (200 new
  patients/week, 6000 active, 10 psychiatrists, 20-min AI-prepared sessions), innovation
  plans (UK expansion, no-code tools, patient app with passive metrics/EMA), data
  valuation (~M), remote team management optimization, and AI for personalized medical
  education.'
janitor_note: LINK001 — Telia'z wikilinks in orgs/projects fields are valid (YAML
  escaping false positive). Base embed \![[related.base#All]] requires _bases/related.base
  which does not exist; create it to enable dynamic views. All person/org/project
  link targets verified as existing. ORPHAN001 — no inbound wikilinks; consider cross-referencing
  from related conference notes or project records.
location: '[[org/Rambam Medical Center]]'
name: Conference Discussion Sentiment Analysis Ethnic Disparities and Clinic Scale
  2025-11-13
orgs:
- '[[org/Rambam Medical Center]]'
- '[[org/Telia''z]]'
participants:
- '[[person/Rami Khouri]]'
project: null
projects:
- '[[project/Telia''z AI Diagnostic Research Paper]]'
- '[[project/Telia''z Clinic Israel]]'
- '[[project/Telia''z Innovation Program]]'
- '[[project/Telia''z UK Expansion]]'
related:
- '[[note/Conference Networking Conversation Military Service and Telia''z Overview
  2025-11-13]]'
- '[[task/Find NLP Outcome Scoring Literature for Transcript Analysis]]'
- '[[assumption/Text-Based Sentiment Analysis Outperforms Standardized Questionnaires
  for Clinical Outcome Tracking]]'
- '[[assumption/AI Text Analysis Can Detect Non-Verbal Cues at 95 Percent Accuracy
  From Text Alone]]'
- '[[assumption/Telia''z Clinical Data Valued at Approximately 20 Million Dollars]]'
relationships:
- confidence: 0.7
  context: Psychiatry conference topics
  source: note/Conference Discussion Sentiment Analysis Ethnic Disparities and Clinic
    Scale 2025-11-13.md
  target: note/History of Psychedelics in Psychiatry Lecture 2025-11-12.md
  type: related-to
- confidence: 0.7
  context: Psychiatry conference topics
  source: note/Conference Discussion Sentiment Analysis Ethnic Disparities and Clinic
    Scale 2025-11-13.md
  target: note/Psychiatric Teaching on Cognitive Risk Factors and Antipsychotic Impact
    2025-11-12.md
  type: related-to
- confidence: 0.7
  context: Psychiatry conference topics
  source: note/Conference Discussion Sentiment Analysis Ethnic Disparities and Clinic
    Scale 2025-11-13.md
  target: note/QEEG Brain Mapping and Neurostimulation Treatment Lecture 2025-11-12.md
  type: related-to
- confidence: 0.7
  context: Disparities and new psych treatments
  source: note/Conference Discussion Sentiment Analysis Ethnic Disparities and Clinic
    Scale 2025-11-13.md
  target: note/Voice Memo New Neurological Treatments and Cobenfy Discussion 2025-11-13.md
  type: related-to
session: null
source: voice_memo
source_language: he
status: active
subtype: learning
tags:
- sentiment-analysis
- ethnic-disparities
- telepsychiatry
- data-valuation
- passive-metrics
- EMA
- AI-education
- conference
type: note
---

## Context

Voice memo recorded at a professional psychiatric conference on 2025-11-13. Rami (Speaker 2) converses with a colleague (Speaker 1, likely a Rambam department affiliate) about multiple research and operational topics. This is one of several recordings from the same conference event.

## Sentiment Analysis Methodology for Clinical Outcome Tracking

Rami describes running sentiment analysis on all available clinical text data — transcriptions, summaries, and questionnaires — to develop a data-driven improvement metric that does not rely on traditional self-report instruments.

The approach divides analysis into three thematic dimensions:
1. **Quantitative**: Session length, time between follow-ups, questionnaire scores when available
2. **Clinical**: Clinical content extraction and categorization
3. **Linguistic sentiment**: Positive/negative word counts, recurrence patterns, thematic categories (e.g., return to work, mentions of friends/social connections)

Initial testing on ~700 patients shows this composite metric outperforms PCL, PHQ, and GAD standardized questionnaires for tracking patient improvement.

### Data Privacy Approach

GPT-4 is used to write Python code for the analysis libraries, but the actual data processing runs locally. The colleague notes this means the model is not exposed to patient data directly. Rami acknowledges that any non-local platform has its own terms of service, but notes they do not expose the data.

They also discuss using Claude for transcriptions, noting it is not local either.

## Ethnic Disparities in Psychiatric Hospitalization Research

The colleague (Speaker 2 in early section, then shifts) describes a line of research at Rambam examining mental health, war, and ethnic disparities:

- **ER visits analysis**: All ER psychiatric visits from the past two years at Rambam, examining pre-war vs. war patterns
- **Suicide theory**: Hypothesis that suicidality decreases during war and increases after war
- **Jewish-Arab differences**: Different impact patterns between October 2023 (Gaza war, far from Haifa) vs. October 2024 (Lebanon war, rockets near Haifa)
- **Key published finding**: Arabs are hospitalized involuntarily more than Jews
  - Methodology: First-episode psychosis under age 40, examined immediate risk assessment, controlling for physician identity using linear mixed models (27 doctors)
  - The model controls for physician-level variation

### Interpretation

Two proposed explanations:
1. Arab doctors may not believe psychiatric hospitalization benefits their patients
2. Jewish doctors are less empathetically/culturally connected to Arab patients — described as "less connected culturally" rather than simply less empathetic

Additional finding: Younger female doctors (e.g., "Ari") tend to hospitalize young patients more readily.

## Telia'z Clinic Scale Overview

Rami describes the clinic operations to a conference attendee:

- **New patients**: 200 per week from Maccabi (health fund)
- **Active patients**: 6,000
- **Psychiatrists**: 10
- **Session duration**: 20 minutes
- **AI preparation**: Everything is AI-prepared — the psychiatrist receives all information from the system before seeing the patient, eliminating writing/documentation burden during the session
- **Bureaucracy**: Minimal — private company working with Maccabi; must meet NILs (standards) but not audited weekly
- **Growth**: Currently mostly in the south of Israel; estimated at less than 5% of potential Maccabi market

## Innovation and Data Collection Plans

### UK Expansion and No-Code Development
Rami mentions having "England now and innovation" — building out an innovation division. The approach involves:
- Taking people who are not from software backgrounds but have some development experience
- Building systems from scratch using no-code tools (Vibe coding, Label, Base44)
- Can stand up a system within a week
- Challenge: giving it technical robustness and integrating with software team

### Patient App and Passive Metrics
- Patient app already exists with potential for passive metric collection
- Conference reference: Someone at another conference collects phone data — screen time, phone usage, walking, GPS location — combined with clinical data
- **EMA (Ecological Momentary Assessment)**: Once or multiple times daily sampling, providing high-resolution therapeutic data
- Additional biometric data: heart rate, breathing, sleep — combinable with clinical data (episodes, medication)

### Wearable Distribution
A company distributed Garmin sport watches for free to patients for data collection. Rami notes they could potentially do similar with their patient population.

### Prospective Research Scale
- Traditional prospective research might recruit ~100 patients
- Telia'z can deploy to 5,000 patients via the app, all of whom use it as part of their care workflow

## Data Valuation

Rami states that their data alone is currently valued at approximately $20 million, described as "golden data." The product is becoming the data itself, not just the clinical service.

## Remote Team Management Insights

### Session Length Optimization
- Started with 40-minute sessions
- Discovered psychiatrists naturally shorten sessions over time (from 30 to ~27 minutes) without informing management
- Used this data-driven insight to propose incentive restructuring: "You earn 450 NIS/hour, you could earn 600 NIS/hour if you do more sessions at 25 minutes"
- Allows increasing throughput without needing to push reluctant clinicians

### Frustration Detection Agent
Rami describes an AI agent that monitors team frustration from staff meetings, proposes solutions, and routes issues to the right person (framework coordinator, clinical manager, or innovation team) — making problem resolution faster.

## AI Text Analysis Capabilities

Rami claims that language models can determine patient status including affect and eye contact from text analysis alone at approximately 95% accuracy. The marginal gain from processing video would only add ~2% accuracy, suggesting text-based analysis captures the vast majority of clinically relevant signals.

### Storage Considerations
- Currently not saving audio/video files to avoid bureaucratic overhead and storage costs
- Only summaries are retained, taken in real-time
- Patient consent requirements for recordings are a barrier
- Fast clinical flow is prioritized

## AI for Personalized Medical Education

Rami is beginning to provide training for residents (from the start of specialization, Stage 1), learning patterns of how individuals learn, and building personalized learning programs for each resident.

Tools mentioned:
- ChatGPT Teaching tools
- NotebookLM

Rami expresses surprise that large institutions have not yet adopted these AI-powered personalized education approaches. Notes that some countries have partnerships with OpenAI for all students.

## Rambam Department Structure

Discussion of the Rambam psychiatry department management:
- Current leadership: Lauren and Samar (replaced Roberto)
- Previous leadership pairs: Gretz and Kornit, Chaya and Kornit
- The department is described as "not really managed" — leadership keeps shifting
- Key active personnel: Yael (very active in influencing the department), Tom (psychologist, equally influential), Maureen (skilled manager who built a new unit)
- Recent change: Michal replaced Roy Dor as psychologist
- General assessment: The department oscillates without stable leadership

---
## Related
![[related.base#All]]