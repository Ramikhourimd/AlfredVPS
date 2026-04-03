---
alfred_tags:
- employee/role-manuals
- personal/work-guides
created: '2026-03-19'
description: Comprehensive AI skills toolkit with 8 specialized agents built for Rivi
  Idelman covering daily work management, UX expertise, workflow automation, stakeholder
  tracking, knowledge curation, problem framing (OPPO), training content creation,
  and career development
name: Rivi Idelman Complete AI Skills Toolkit
project: '[[project/Telia''z Innovation Program]]'
related:
- '[[person/Rivi Idelman]]'
- '[[person/Rami Khouri]]'
- '[[person/Ohad Edri]]'
- '[[person/Basel Kanaaneh]]'
- '[[person/Stav Zamir]]'
- '[[person/Yael Marciano]]'
- '[[asset/Rivi Idelman AI Skills Toolkit]]'
- '[[project/Telia''z AI Clinical Platform]]'
relationships:
- confidence: 0.75
  context: Related skills and ops manuals
  source: note/Rivi Idelman Complete AI Skills Toolkit.md
  target: note/Stav Zamir Comprehensive Role and Operational Manual.md
  type: related-to
- confidence: 0.8
  context: AI toolkit aids general work manual
  source: note/Rivi Idelman Complete AI Skills Toolkit.md
  target: note/Ohad Edri Complete Work Manual.md
  type: supports
session: null
status: active
subtype: reference
tags: []
type: note
---

# Rivi Idelman Complete AI Skills Toolkit

## Overview

A set of 8 integrated AI agent skills designed specifically for Rivi Idelman in her role as UX Lead on the Innovation Team at [[org/Telia'z]]. Created on March 19, 2026 as part of the agentic workspace initiative. The toolkit addresses Rivi's daily operational needs, domain expertise, recurring workflows, relationship management, knowledge transfer gaps, problem definition methodology, training content creation, and career development tracking.

## Skills Inventory

### 1. rivi-pa — Proactive AI Partner
Central daily work hub. Tailors briefings to Rivi's weekly schedule: Sunday (innovation day), Tue/Wed (split clinical-innovation), Monday (1:1 day). Enforces the 3-project maximum rule and the Feb 24, 2026 boundary agreement with [[person/Rami Khouri]] (redirect execution requests from others). Includes meeting prep workflows for weekly 1:1 with Rami, Sunday strategic meeting with [[person/Ohad Edri]], and monthly clinic meeting with [[person/Ori Shukron]].

### 2. rivi-ux-expert — UX & Clinical Insights Agent
Deep domain query agent spanning 6 expertise areas: field insights and problem framing, user experience and needs discovery, UX design, concept design and innovation, UX and data assessment, and information management. Queries internal sources (KB, BigQuery, Gmail, Slack, Notion) and enriches with external research. Structured answer format: direct answer, internal evidence, external context, recommendation, sources.

### 3. rivi-workflow — Workflow Automator
Automates 5 recurring workflows:
1. Clinical Feedback Collection and Categorization (Tue/Wed)
2. Weekly Task Prioritization and Reporting (Sunday)
3. Training Content Creation Pipeline
4. Research Report Processing via NotebookLM
5. System Evaluation Feedback Loop

### 4. rivi-stakeholders — Stakeholder Relationship Manager
Manages relationships across 3 tiers:
- **Tier 1** (high-frequency, high-impact): [[person/Rami Khouri]], [[person/Ohad Edri]], [[person/Basel Kanaaneh]]
- **Tier 2** (regular collaboration): [[person/Stav Zamir]], [[person/Yael Marciano]], Clinical Staff
- **Tier 3** (periodic engagement): [[person/Ori Shukron]], [[person/Noam]]

Tracks last interaction, open commitments, relationship health with configurable thresholds, and sentiment signals.

### 5. rivi-knowledge — Knowledge Curator & Transfer Agent
Addresses 3 high-priority undocumented knowledge areas:
1. Clinic Feedback Data (4-6h effort)
2. Clinical Needs Identification (3-4h)
3. IRB Research Data Management (2-3h)

Three capture modes: Quick Capture (5-10 min), Deep Documentation Session (30-60 min guided interview), Meeting Documentation (post-meeting).

### 6. rivi-problem-framer — Problem Definition Engine (NEW)
Rivi's most strategically important skill. Formalizes her ability to translate raw clinical pain into structured, AI-ready problem definitions. Uses the OPPO methodology (Observation, Pain Point, Problem, Opportunity) with quantitative scoring (Frequency + Severity + Feasibility, /12). Includes problem definition template, quality criteria, and backlog management.

### 7. rivi-training-creator — Training Content Generator (NEW)
Manages full training content pipeline for clinical staff. Covers 5 content types: UI explanation videos, feature walkthroughs, onboarding guides, training presentations, and quick reference cards. 7-step pipeline: identify, plan, draft, review, produce, distribute, track. Writing guidelines for Hebrew clinical audience.

### 8. rivi-career-coach — Career Development Agent (NEW)
Supports Rivi's planned transition from UX Lead to UX Manager. Tracks progress across 5 transition dimensions (Scope, People, Strategy, Influence, Process) with 1-5 rating scale. Includes skill development roadmap and career conversation preparation for discussions with Rami.

## MCP Integrations

| MCP Server | Skills Using It |
|------------|----------------|
| Monday.com | rivi-pa, rivi-workflow, rivi-stakeholders, rivi-problem-framer, rivi-training-creator |
| Notion | rivi-pa, rivi-ux-expert, rivi-workflow, rivi-stakeholders, rivi-problem-framer, rivi-knowledge, rivi-career-coach |
| Slack | rivi-pa, rivi-ux-expert, rivi-workflow, rivi-stakeholders, rivi-problem-framer |
| Supabase | rivi-knowledge |
| BigQuery | rivi-ux-expert, rivi-problem-framer |

## Skill Ecosystem Integration

The 8 skills form an integrated ecosystem where outputs flow between them:
- **rivi-workflow** collects clinical feedback → feeds **rivi-problem-framer** for structured problem definitions
- **rivi-problem-framer** identifies training gaps → triggers **rivi-training-creator** for content creation
- **rivi-pa** uses **rivi-stakeholders** data for meeting prep and follow-up tracking
- **rivi-knowledge** captures institutional knowledge that enriches **rivi-ux-expert** answers
- **rivi-career-coach** tracks growth that **rivi-pa** surfaces in 1:1 prep with Rami
- **rivi-ux-expert** provides research context that **rivi-problem-framer** uses for evidence-based framing

## Related
![[related.base#All]]