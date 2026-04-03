---
alfred_tags:
- taliaz/agentic-workspaces
- employee-personalization
description: 'Generate personalized OPTICA framework guide maps for Taliaz employees.
  Maps each employee''s role, responsibilities, and expertise to the 13-step OPTICA
  AI governance framework, producing a comprehensive guide with detailed checklists,
  step-by-step instructions, troubleshooting advice, escalation paths, and gate decision
  criteria. Consumes employee profiles from taliaz-employee-profiler. Triggers on:
  OPTICA guide for, create OPTICA map, AI governance guide, OPTICA checklist for,
  framework guide for, innovation guide for.'
name: taliaz-optica-guide
relationships:
- confidence: 0.8
  context: Semantically related Taliaz skills
  source: skills/user/taliaz-optica-guide/SKILL.md
  target: skills/user/taliaz-toolkit-generator/SKILL.md
  type: related-to
---

# Taliaz OPTICA Guide Map Generator

Generate personalized OPTICA framework guide maps for any Taliaz employee. Each guide maps the employee's specific role, responsibilities, and expertise to every step of the OPTICA AI governance framework, producing a comprehensive, actionable document that serves as their master guide for evaluating and deploying clinical AI solutions.

## Core Directive

> "I create OPTICA guides that transform a complex governance framework into a personalized, actionable roadmap. Every employee gets a guide that tells them exactly what THEY need to do at each step, how to do it, who to ask for help, and what to do when they're stuck. No generic framework documents — only personalized, role-specific guidance with detailed checklists."

## What is OPTICA?

**OPTICA** (Organizational PerspecTIve Checklist for AI solutions adoption) is Taliaz's disciplined, stage-gated framework for evaluating and deploying clinical AI solutions. It provides:

- **4 Phases**: Foundation → Feasibility → Validation → Integration
- **13 Steps** (A through M): Each with specific evidence requirements and gate decisions
- **6 Team Roles**: Clinical Expert, AI Solution Developer, Org Data Lead, MLOps Expert, Org AI Lead, Exec Sponsor
- **6 Evidence Artifacts**: Problem+Metrics, Alternatives Matrix, Data Fit, Model Card, Risk Register, Deployment+Monitoring Plan
- **Guiding Principle**: "Quality > speed. Stop early on showstoppers. Document everything."

See `references/optica-framework.md` for the complete framework reference.

## What the Guide Contains

The personalized guide includes these sections:

| Section | What It Provides |
|---------|-----------------|
| Executive Summary | OPTICA overview and the employee's personalized context |
| OPTICA Role Profile | Which OPTICA roles the employee maps to, with evidence |
| Involvement Map | Table showing involvement level (Owner/Primary/Contributor/Reviewer/Informed) for all 13 steps |
| Phase 1-4 Detailed Guide | For each step: description, gate question, personalized context, full checklist with how-to/troubleshooting/escalation |
| Evidence Artifacts Checklist | Tracking table for all required documents |
| Collaborative Team | Who fills each OPTICA role at Taliaz and how to engage them |
| Troubleshooting Guide | Common blockers and solutions, escalation paths |
| Quick Reference Card | Visual overview of the 4 phases and gate decisions |

Each checklist item includes:
1. **What to do** — Clear action item
2. **Why it matters** — Explanation of importance
3. **How to do it** — Step-by-step guidance specific to Taliaz
4. **If you're stuck** — Troubleshooting advice and escalation paths
5. **Evidence needed** — What artifact or documentation to produce
6. **Done criteria** — How to know the item is complete

## Workflow

Building an OPTICA guide involves these steps:

1. **Generate the employee profile** (prerequisite — use `taliaz-employee-profiler` skill)
2. **Map role to OPTICA** (run `map_role_to_optica.py`)
3. **Generate the guide** (run `generate_optica_guide.py`)
4. **Enrich and personalize** (add Taliaz-specific context, validate with user)
5. **Deliver the guide** (Markdown, optionally PDF)

### Step 1: Generate the Employee Profile

This skill depends on the `taliaz-employee-profiler` skill. If the profile JSON doesn't exist yet, generate it first:

```bash
cd /home/ubuntu/skills/taliaz-employee-profiler
python3 scripts/extract_employee_data.py "EmployeeName" > /tmp/{name}_data.json
```

### Step 2: Map Role to OPTICA

```bash
cd /home/ubuntu/skills/taliaz-optica-guide
python3 scripts/map_role_to_optica.py /tmp/{name}_data.json /tmp/{name}_optica_mapping.json
```

This script analyzes the employee's:
- Job title and role description
- Responsibilities (keyword matching against each OPTICA step)
- Expertise areas (domain matching)
- RACI assignments (project involvement patterns)
- Institutional knowledge areas

It produces a JSON mapping that identifies:
- Which OPTICA roles the employee fills (with confidence scores)
- Their involvement level in each of the 13 steps (OWNER/PRIMARY/CONTRIBUTOR/REVIEWER/INFORMED)
- The specific reasons for each mapping (traceable to profile data)

### Step 3: Generate the Guide

```bash
python3 scripts/generate_optica_guide.py /tmp/{name}_data.json /tmp/{name}_optica_mapping.json /tmp/{name}_optica_guide.md
```

### Step 4: Enrich and Personalize

After generating the base guide, enhance it with:

**Minimum enrichment** (always do):
- Review the OPTICA role mapping for accuracy — adjust involvement levels if needed
- Add specific names of Taliaz colleagues for each "Who Can Help" reference
- Validate that the personalized context sections are accurate

**Recommended enrichment** (do when time allows):
- Add examples from recent Taliaz AI projects to illustrate each step
- Reference specific Taliaz tools and systems (Monday.com boards, BigQuery dashboards, etc.)
- Include links to relevant Taliaz documents in Google Drive
- Add context from recent innovation meetings (search Gmail and Calendar)

**Advanced enrichment** (do when requested):
- Cross-reference with the employee's current AI projects from Monday.com
- Add project-specific checklists for active OPTICA evaluations
- Include timeline estimates based on Taliaz's historical project data

See `references/taliaz-context.md` for Taliaz-specific context for each OPTICA step.

### Step 5: Deliver

Deliver the guide as a Markdown file. If PDF is requested:
```bash
manus-md-to-pdf /tmp/{name}_optica_guide.md /tmp/{name}_optica_guide.pdf
```

## Bundled Resources

| Resource | Description |
|----------|-------------|
| `scripts/map_role_to_optica.py` | Maps employee profile to OPTICA roles and step involvement levels |
| `scripts/generate_optica_guide.py` | Generates the personalized guide with all checklists and guidance |
| `references/optica-framework.md` | Complete OPTICA framework reference (4 phases, 13 steps, 6 roles, 6 artifacts) |
| `references/taliaz-context.md` | Taliaz-specific context for each OPTICA step (who does what, tools, examples) |
| `references/checklist-templates.md` | Detailed checklist items per step with quality standards |

## Connector Dependencies

| Connector | Purpose | Required |
|-----------|---------|----------|
| `taliaz-employee-profiler` skill | Provides the employee profile JSON | Yes |
| Supabase KB (via `taliaz-kb-query`) | Employee data extraction | Yes (via profiler) |
| `gmail` MCP | Search for OPTICA-related communications | Optional |
| `google-calendar` MCP | Find innovation meetings and reviews | Optional |
| Google Drive (rclone) | Access OPTICA documents and templates | Optional |
| `monday-com` MCP | Cross-reference with active AI projects | Optional |