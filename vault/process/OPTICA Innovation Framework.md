---
area: Innovation
created: '2026-03-19'
depends_on: []
description: Taliaz 8-stage/13-step AI governance framework (Organizational PerspecTIve
  Checklist for AI solutions adoption) for evaluating and deploying clinical AI solutions.
  Established February 2026.
frequency: as-needed
governed_by: []
janitor_note: 'LINK001 — Telia''z wikilinks in related field are YAML single-quote
  escaping false positives (targets exist). Base view embeds (process.base#Dependencies,
  #Runs, #Notes) reference _bases/process.base which does not exist — vault-wide infrastructure
  gap, embeds preserved.'
name: OPTICA Innovation Framework
owner: '[[person/Ohad Edri]]'
related:
- '[[person/Ohad Edri]]'
- '[[person/Rami Khouri]]'
- '[[person/Rivi Idelman]]'
- '[[person/Stav Zamir]]'
- '[[project/Telia''z Innovation Program]]'
- '[[project/Telia''z AI Clinical Platform]]'
relationships: []
status: active
tags: []
type: process
---

# OPTICA Innovation Framework

Organizational PerspecTIve Checklist for AI solutions adoption — Taliaz's disciplined, stage-gated framework for evaluating and deploying clinical AI solutions. Established in the February 19, 2026 Innovation Team meeting.

**Guiding Principle:** Quality > speed. Stop early on showstoppers. Document everything.

## Phases and Steps

### Phase 1: Foundation — Is this the right problem?
- **Step A (Clinical Need):** Identify and validate the clinical problem
- **Step B (Alternatives):** Review existing solutions and benchmarks (Ohad OWNS)

### Phase 2: Feasibility — Can this work in our environment?
- **Step C (Population):** Analyze target population data for representation and bias
- **Step D (Input Data):** Assess data availability, quality, and integration (Ohad OWNS)
- **Step E (Output Data):** Define technical specifications for AI model output

### Phase 3: Validation — Does the solution work as intended?
- **Step F (Build + Validate):** Develop, validate, and document the AI model (Ohad OWNS)
- **Step G (Performance):** Analyze model performance against thresholds
- **Step H (Explainability):** Implement and document explainability methods
- **Step I (Regulation/Security/Privacy):** Ensure compliance with security and privacy standards

### Phase 4: Integration — How do we deploy and manage this responsibly?
- **Step J (Deployment Plan):** Design technical deployment and workflow integration (Ohad OWNS)
- **Step K (Monitoring Plan):** Design and implement monitoring for model performance and drift
- **Step L (Evaluation Plan):** Post-deployment evaluation design
- **Step M (Strategy Fit):** Final scale/pause/stop recommendation

## Evidence Artifacts Required
- Problem + Metrics Document
- Alternatives Matrix
- Data Fit Assessment
- Model Card
- Risk Register
- Deployment + Monitoring Plan
- Evaluation Report

## Dependencies
![[process.base#Dependencies]]

## Runs
![[process.base#Runs]]

## Notes
![[process.base#Notes]]



## Role Assignments — Stav Zamir

Stav holds four OPTICA roles (per February 2026 role manual):
- **Clinical Expert** (Relevance Score: 22) — Primary role
- **Org AI Lead** (Relevance Score: 9)
- **AI Solution Developer** (Relevance Score: 4)
- **Org Data Lead** (Relevance Score: 2)

**Step Ownership:** Stav OWNS Steps A (Clinical Need), B (Alternatives), E (Output Data), F (Build + Validate), and J (Deployment Plan).
