# Rivi Idelman — Complete AI Skills Toolkit

**Created:** March 19, 2026
**For:** Rivi Idelman, UX Lead, Innovation Team, Taliaz Health
**Total Skills:** 8 (5 from original blueprint + 3 new)

---

## Skills Overview

| # | Skill | Purpose | Trigger Examples |
|---|-------|---------|-----------------|
| 1 | **rivi-pa** | Proactive AI Partner — daily briefings, meeting prep, task prioritization | "daily brief", "what's next", "prepare me for my meeting" |
| 2 | **rivi-ux-expert** | UX & Clinical Insights Agent — deep domain queries, feedback analysis, research | "clinical feedback about X", "UX best practice for Y" |
| 3 | **rivi-workflow** | Workflow Automator — 5 recurring multi-step processes automated | "collect feedback", "run my weekly", "process research report" |
| 4 | **rivi-stakeholders** | Stakeholder Relationship Manager — tracks 8 key people, health monitoring | "who should I follow up with", "draft follow-up to Basel" |
| 5 | **rivi-knowledge** | Knowledge Curator & Transfer Agent — documents 3 critical undocumented areas | "quick capture", "help me document", "knowledge transfer" |
| 6 | **rivi-problem-framer** | Problem Definition Engine — OPPO methodology, scoring, backlog management | "frame this problem", "prioritize problems", "score this issue" |
| 7 | **rivi-training-creator** | Training Content Generator — video scripts, presentations, onboarding guides | "create training for X", "write video script", "onboarding guide" |
| 8 | **rivi-career-coach** | Career Development Agent — UX Lead → UX Manager transition tracker | "career conversation prep", "what skills should I develop" |

---

## Skill Details

### 1. rivi-pa — Proactive AI Partner

The central hub for Rivi's daily work. Understands her schedule (Sunday = innovation day, Tue/Wed = split clinical-innovation, Monday = 1:1 day) and tailors briefings accordingly. Enforces the 3-project maximum rule and the Feb 24, 2026 boundary agreement with Rami (redirect execution requests from others). Includes meeting prep workflows for the weekly 1:1 with Rami, Sunday strategic meeting with Ohad, and monthly clinic meeting with Ori.

**Files:** `SKILL.md` + `references/meeting-prep.md`

### 2. rivi-ux-expert — UX & Clinical Insights Agent

Deep domain query agent spanning 6 expertise areas: field insights and problem framing, user experience and needs discovery, UX design, concept design and innovation, UX and data assessment, and information management. Queries internal sources (KB, BigQuery, Gmail, Slack, Notion) and enriches with external research. Every answer follows a structured format: direct answer, internal evidence, external context, recommendation, and sources.

**Files:** `SKILL.md`

### 3. rivi-workflow — Workflow Automator

Automates 5 recurring workflows: (1) Clinical Feedback Collection and Categorization (Tue/Wed), (2) Weekly Task Prioritization and Reporting (Sunday), (3) Training Content Creation Pipeline, (4) Research Report Processing via NotebookLM, and (5) System Evaluation Feedback Loop. Each workflow has clear triggers, step-by-step procedures, and routing rules.

**Files:** `SKILL.md`

### 4. rivi-stakeholders — Stakeholder Relationship Manager

Manages relationships across 3 tiers: Tier 1 (Rami, Ohad, Basel — high-frequency, high-impact), Tier 2 (Stav, Yael, Clinical Staff — regular collaboration), and Tier 3 (Ori, Noam — periodic engagement). Tracks last interaction, open commitments, relationship health with configurable thresholds, and sentiment signals. Includes per-stakeholder engagement playbooks.

**Files:** `SKILL.md` + `references/stakeholder-playbooks.md`

### 5. rivi-knowledge — Knowledge Curator & Transfer Agent

Addresses Rivi's 3 high-priority undocumented knowledge areas: Clinic Feedback Data (4-6h effort), Clinical Needs Identification (3-4h), and IRB Research Data Management (2-3h). Provides three capture modes: Quick Capture (5-10 min), Deep Documentation Session (30-60 min guided interview), and Meeting Documentation (post-meeting). Includes a phased transfer plan with specific timelines.

**Files:** `SKILL.md` + `references/interview-guide.md`

### 6. rivi-problem-framer — Problem Definition Engine (NEW)

Rivi's most strategically important skill. Formalizes her unique ability to translate raw clinical pain into structured, AI-ready problem definitions. Uses the OPPO methodology (Observation → Pain Point → Problem → Opportunity) with a quantitative scoring framework (Frequency + Severity + Feasibility, /12). Includes a full problem definition template, quality criteria, and backlog management workflow.

**Files:** `SKILL.md` + `references/problem-template.md`

### 7. rivi-training-creator — Training Content Generator (NEW)

Manages the full training content pipeline for clinical staff. Covers 5 content types: UI explanation videos, feature walkthroughs, onboarding guides, training presentations, and quick reference cards. Includes a 7-step pipeline (identify → plan → draft → review → produce → distribute → track), writing guidelines for Hebrew clinical audience, and a video script template with Hebrew examples.

**Files:** `SKILL.md` + `references/video-script-template.md`

### 8. rivi-career-coach — Career Development Agent (NEW)

Supports Rivi's planned transition from UX Lead to UX Manager. Tracks progress across 5 transition dimensions (Scope, People, Strategy, Influence, Process) with a 1-5 rating scale. Includes a skill development roadmap (immediate, medium-term, ongoing), career conversation preparation workflow for discussions with Rami, and a curated learning resource library with credentials, books, communities, and tools.

**Files:** `SKILL.md` + `references/learning-resources.md`

---

## MCP Integrations Across All Skills

| MCP Server | Used By Skills |
|------------|---------------|
| `monday-com` | rivi-pa, rivi-workflow, rivi-stakeholders, rivi-problem-framer, rivi-training-creator |
| `notion` | rivi-pa, rivi-ux-expert, rivi-workflow, rivi-stakeholders, rivi-problem-framer, rivi-knowledge, rivi-career-coach |
| `slack` | rivi-pa, rivi-ux-expert, rivi-workflow, rivi-stakeholders, rivi-problem-framer |
| `supabase` | rivi-knowledge |
| `bigquery` | rivi-ux-expert, rivi-problem-framer |

---

## How Skills Work Together

The skills form an integrated ecosystem:

1. **rivi-workflow** collects clinical feedback → feeds into **rivi-problem-framer** for structured problem definitions
2. **rivi-problem-framer** identifies training gaps → triggers **rivi-training-creator** for content creation
3. **rivi-pa** uses **rivi-stakeholders** data for meeting prep and follow-up tracking
4. **rivi-knowledge** captures institutional knowledge that enriches **rivi-ux-expert** answers
5. **rivi-career-coach** tracks growth that **rivi-pa** surfaces in 1:1 prep with Rami
6. **rivi-ux-expert** provides research context that **rivi-problem-framer** uses for evidence-based framing
