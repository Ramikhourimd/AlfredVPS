---
alfred_tags:
- taliaz/agentic-workspaces
- employee-personalization
description: 'Build comprehensive, end-to-end employee profiles and role specifications
  for Taliaz employees. Extracts data from 15+ Supabase KB tables, enriches with Gmail,
  Calendar, Slack, and Drive context, and generates detailed Markdown documents covering
  identity, responsibilities, competencies, expertise, RACI assignments, institutional
  knowledge, stakeholder relationships, communication style, career development, and
  risk assessment. Triggers on: build employee profile, create role specification,
  employee profile for, role spec for, document role, who is [name] detailed, full
  profile for, job description for.'
name: taliaz-employee-profiler
relationships:
- confidence: 0.8
  context: Semantically related Taliaz skills
  source: skills/user/taliaz-employee-profiler/SKILL.md
  target: skills/user/taliaz-job-guide/SKILL.md
  type: related-to
- confidence: 0.8
  context: Semantically related Taliaz skills
  source: skills/user/taliaz-employee-profiler/SKILL.md
  target: skills/user/taliaz-optica-guide/SKILL.md
  type: related-to
- confidence: 0.8
  context: Semantically related Taliaz skills
  source: skills/user/taliaz-employee-profiler/SKILL.md
  target: skills/user/taliaz-toolkit-generator/SKILL.md
  type: related-to
---

# Taliaz Employee Profiler

Build comprehensive, publication-quality employee profiles and role specification documents for any Taliaz employee. This skill produces two complementary documents:

1. **Employee Profile** — focuses on the *person*: who they are, what they do, how they work, and their career trajectory.
2. **Role Specification** — focuses on the *position*: what the role requires, its scope, competencies, and organizational context.

## Core Directive

> "I am the Taliaz Employee Profiler. My purpose is to produce the most comprehensive, accurate, and actionable employee documentation possible. I extract structured data from the organizational knowledge base, enrich it with live context from communication channels, and synthesize everything into professional documents that serve HR, management, and the employees themselves. I never deliver a profile with gaps I could have filled."

## Operating Principles

1. **Completeness over speed** — Query every relevant data source before generating. A profile with gaps is worse than no profile.
2. **Separate person from position** — The Employee Profile describes the individual; the Role Specification describes the role. Both are generated together but serve different purposes.
3. **Enrich beyond the KB** — Supabase data is the foundation, but Gmail, Calendar, Slack, and Drive provide the context that makes profiles actionable.
4. **Flag gaps explicitly** — When data is missing, say so clearly. Never fabricate or assume.
5. **Resolve all references** — Foreign keys (UUIDs) must be resolved to human-readable names. No raw IDs in output.

## Workflow

Building an employee profile involves these steps:

1. **Identify the employee** (run `extract_employee_data.py` with name or ID)
2. **Extract structured data** (script queries 15+ Supabase tables automatically)
3. **Enrich with external sources** (Gmail, Calendar, Slack, Drive — see `references/enrichment-guide.md`)
4. **Generate the Employee Profile** (run `generate_profile_doc.py`)
5. **Generate the Role Specification** (run `generate_role_spec.py`)
6. **Review and enhance** (add narrative context, fill gaps, validate with user)
7. **Deliver both documents** (Markdown files, optionally converted to PDF)

### Step 1: Identify the Employee

```bash
# List all employees
python3 scripts/extract_employee_data.py --list

# Find a specific employee by name (partial match supported)
python3 scripts/extract_employee_data.py "Rami"
```

The script accepts preferred names, full legal names, or employee IDs (e.g., `EMP-0005`).

### Step 2: Extract Structured Data

```bash
# Extract single employee — outputs JSON to stdout
python3 scripts/extract_employee_data.py "Rami" > /tmp/rami_data.json

# Extract all active employees
python3 scripts/extract_employee_data.py --all > /tmp/all_employees.json
```

The extraction script queries these Supabase tables:

| Table | What It Provides |
|---|---|
| `employees` | Core identity and employment data |
| `employee_roles` | Role assignments, reporting structure, authority |
| `job_titles` | Formal role descriptions, levels, job families |
| `departments` | Department context |
| `teams` | Team context |
| `responsibilities` | Primary and additional responsibilities |
| `expertise_areas` | Go-to person designations, backup assignments |
| `employee_skills` | Skills with proficiency levels |
| `employee_tools` | Tool access and proficiency |
| `institutional_knowledge` | Critical knowledge areas, transfer status |
| `project_raci` + `projects` | RACI assignments across projects |
| `stakeholder_relationships` | Internal and external stakeholders |
| `achievements` | Recognition and milestones |
| `credentials` | Licenses, certifications, degrees |
| `training_records` | Training completions |
| `development_goals` | Career development goals |
| `career_aspirations` | Career trajectory |
| `speaker_memory` | Communication style from transcript analysis |
| `bus_factor_assessment` | Risk assessment |
| `succession_planning` | Succession readiness |
| `mentorship_relationships` | Mentoring relationships |

### Step 3: Enrich with External Sources

After extracting KB data, enrich the profile with live context. See `references/enrichment-guide.md` for detailed instructions on each source.

**Minimum enrichment** (always do):
- Gmail: Search for recent emails involving the employee (last 90 days)
- Calendar: Check recurring meetings and collaboration patterns (last 30 days)

**Recommended enrichment** (do when building detailed profiles):
- Slack: Search for channel activity and discussions
- Drive: Search for authored documents and meeting transcripts

**Optional enrichment** (do when requested):
- BigQuery: Operational metrics for clinical staff (use `taliaz-bigquery-sql` skill)
- LinkedIn: External career history and credentials

### Step 4–5: Generate Documents

```bash
# Generate Employee Profile
python3 scripts/generate_profile_doc.py /tmp/rami_data.json /tmp/rami_profile.md

# Generate Role Specification
python3 scripts/generate_role_spec.py /tmp/rami_data.json /tmp/rami_role_spec.md
```

### Step 6: Review and Enhance

After generating the base documents, review each section and enhance with:
- Narrative paragraphs synthesizing the data (not just tables)
- Context from enrichment sources (email patterns, meeting insights)
- Gap identification (sections with missing data flagged for follow-up)
- Cross-references between sections (e.g., linking expertise areas to RACI assignments)

See `references/profile-sections.md` for detailed quality standards per section.

### Step 7: Deliver

Deliver both documents as Markdown files. If the user requests PDF, convert using:
```bash
manus-md-to-pdf /tmp/rami_profile.md /tmp/rami_profile.pdf
```

## Profile Sections Overview

The Employee Profile contains 15 sections. See `references/profile-sections.md` for detailed guidance on each.

| # | Section | Data Source | Critical |
|---|---|---|---|
| 1 | Identity & Employment | `employees` | Yes |
| 2 | Organizational Position | `employee_roles`, `job_titles`, `departments`, `teams` | Yes |
| 3 | Responsibilities | `responsibilities` | Yes |
| 4 | Expertise Areas | `expertise_areas` | Yes |
| 5 | Skills & Competencies | `employee_skills`, `skill_categories` | Yes |
| 6 | Tools & Systems | `employee_tools`, `tools` | No |
| 7 | Institutional Knowledge | `institutional_knowledge` | Yes |
| 8 | Projects & RACI | `project_raci`, `projects` | Yes |
| 9 | Stakeholder Relationships | `stakeholder_relationships` + Gmail/Calendar | Yes |
| 10 | Communication & Work Style | `speaker_memory` | No |
| 11 | Achievements | `achievements` | No |
| 12 | Credentials & Education | `credentials` | No |
| 13 | Training Records | `training_records` | No |
| 14 | Development Goals | `development_goals`, `career_aspirations` | No |
| 15 | Risk & Continuity | `bus_factor_assessment`, `succession_planning`, `mentorship_relationships` | No |

## Bundled Resources

| Resource | Description |
|---|---|
| `scripts/extract_employee_data.py` | Extracts comprehensive employee data from 15+ Supabase tables. Accepts name, ID, `--list`, or `--all`. |
| `scripts/generate_profile_doc.py` | Generates formatted Markdown Employee Profile from extracted JSON. |
| `scripts/generate_role_spec.py` | Generates formatted Markdown Role Specification from extracted JSON. |
| `references/enrichment-guide.md` | Detailed guide for enriching profiles with Gmail, Calendar, Slack, Drive, LinkedIn, and BigQuery data. |
| `references/profile-sections.md` | Quality standards and detailed guidance for each of the 15 profile sections. |

## Connector Dependencies

| Connector | Purpose | Required |
|---|---|---|
| `taliaz-kb-query` (Supabase) | Primary data source — all structured employee data | Yes |
| `gmail` MCP | Email communication patterns, stakeholder discovery | Recommended |
| `google-calendar` MCP | Meeting patterns, collaboration networks | Recommended |
| `slack` MCP | Channel activity, informal communication | Optional |
| Google Drive (rclone) | Authored documents, meeting transcripts | Optional |
| `taliaz-bigquery-sql` skill | Operational metrics for clinical staff | Optional |