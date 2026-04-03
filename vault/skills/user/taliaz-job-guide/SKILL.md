---
alfred_tags:
- taliaz/agentic-workspaces
- employee-personalization
description: 'Generate personalized ''How to Nail Your Job'' guides for Taliaz employees.
  Consumes employee profiles from taliaz-employee-profiler and produces comprehensive,
  actionable guides with curated resources, skill development roadmaps, stakeholder
  playbooks, communication tips, career growth paths, and quick wins. Uses Perplexity
  API for AI-powered resource research. Triggers on: job guide for, how to nail your
  job, create job guide, employee success guide, development guide for, role excellence
  guide, personalized guide for.'
name: taliaz-job-guide
relationships:
- confidence: 0.8
  context: Semantically related Taliaz skills
  source: skills/user/taliaz-job-guide/SKILL.md
  target: skills/user/taliaz-optica-guide/SKILL.md
  type: related-to
- confidence: 0.8
  context: Semantically related Taliaz skills
  source: skills/user/taliaz-job-guide/SKILL.md
  target: skills/user/taliaz-toolkit-generator/SKILL.md
  type: related-to
---

# Taliaz Job Guide Generator

Generate personalized "How to Nail Your Job" guides for Taliaz employees. Each guide is a comprehensive, actionable document that transforms an employee's profile data into practical guidance for excelling in their role.

## Core Directive

> "I create guides that make employees feel like they have a personal career coach. Every recommendation is specific to THEIR role, THEIR skills, THEIR gaps, and THEIR goals. No generic advice — only actionable, personalized guidance backed by curated resources."

## What the Guide Contains

The guide has 11 sections, each derived from the employee's profile data and enriched with AI-researched resources:

| # | Section | What It Provides |
|---|---|---|
| 1 | Your Role at a Glance | Crisp summary of role, scope, and key metrics |
| 2 | What "Nailing It" Looks Like | Concrete KRAs and success criteria |
| 3 | Master Your Core Responsibilities | Playbook for each primary responsibility |
| 4 | Skill Development Roadmap | Current inventory, gaps, and learning paths with resources |
| 5 | Tool Mastery Guide | Tools grouped by proficiency with advancement actions |
| 6 | Your Stakeholder Playbook | Relationship map with management strategies |
| 7 | Knowledge You Must Protect & Grow | Critical knowledge areas with transfer actions |
| 8 | Your Communication Playbook | Style-aware communication tips |
| 9 | Career Growth Path | Aspirations connected to concrete actions |
| 10 | Quick Wins & Power Moves | 5-8 achievable actions for the next 30 days |
| 11 | Your Personalized Resource Library | AI-curated books, courses, communities per domain |

## Workflow

Building a job guide involves these steps:

1. **Generate the employee profile** (prerequisite — use `taliaz-employee-profiler` skill)
2. **Research personalized resources** (run `research_resources.py`)
3. **Generate the guide** (run `generate_job_guide.py`)
4. **Enrich and enhance** (add narrative, validate, personalize)
5. **Deliver the guide** (Markdown, optionally PDF)

### Step 1: Generate the Employee Profile

This skill depends on the `taliaz-employee-profiler` skill. If the profile JSON doesn't exist yet, generate it first:

```bash
cd /home/ubuntu/skills/taliaz-employee-profiler
python3 scripts/extract_employee_data.py "EmployeeName" > /tmp/{name}_data.json
```

### Step 2: Research Personalized Resources

```bash
cd /home/ubuntu/skills/taliaz-job-guide
python3 scripts/research_resources.py /tmp/{name}_data.json /tmp/{name}_resources.json
```

This script:
- Extracts key domains from the profile (expertise areas, development goals, career aspirations, tool gaps)
- Deduplicates and prioritizes up to 12 domains
- Uses the Perplexity API (`SONAR_API_KEY`) to research specific resources for each domain
- Also researches general role-level resources (must-read books, frameworks, communities)
- Outputs a structured JSON with all recommendations

**If Perplexity API is unavailable:** The script outputs placeholder text. Manually research resources using web search for each domain area.

**Rate limiting:** The script includes 1-second delays between API calls. For 12 domains, expect ~2-3 minutes total.

### Step 3: Generate the Guide

```bash
python3 scripts/generate_job_guide.py /tmp/{name}_data.json /tmp/{name}_resources.json /tmp/{name}_job_guide.md
```

### Step 4: Enrich and Enhance

After generating the base guide, enhance it following `references/enrichment-strategies.md`:

**Minimum enrichment** (always do):
- Review each section for accuracy and completeness
- Add narrative context to the responsibilities section (not just tables)
- Verify resource links are current

**Recommended enrichment** (do when time allows):
- Gmail: Search for recent email patterns to validate responsibilities and stakeholder map
- Calendar: Check meeting patterns to validate role scope
- Add personalized "common pitfalls" based on institutional knowledge

**Optional enrichment** (do when requested):
- Slack: Channel activity for team involvement
- BigQuery: Operational metrics for clinical staff
- Manager input: Validate KRAs and success criteria

See `references/guide-sections.md` for detailed quality standards per section.

### Step 5: Deliver

Deliver the guide as a Markdown file. If PDF is requested:
```bash
manus-md-to-pdf /tmp/{name}_job_guide.md /tmp/{name}_job_guide.pdf
```

## Bundled Resources

| Resource | Description |
|---|---|
| `scripts/research_resources.py` | Uses Perplexity API to find personalized resources for each expertise area and skill gap |
| `scripts/generate_job_guide.py` | Generates the 11-section guide from profile JSON and resources JSON |
| `references/guide-sections.md` | Quality standards and enhancement tips for each of the 11 sections |
| `references/enrichment-strategies.md` | Strategies for enriching the guide with Gmail, Calendar, Slack, BigQuery data |

## Connector Dependencies

| Connector | Purpose | Required |
|---|---|---|
| `taliaz-employee-profiler` skill | Provides the employee profile JSON | Yes |
| Perplexity API (`SONAR_API_KEY`) | AI-powered resource research | Recommended |
| `gmail` MCP | Email pattern analysis for enrichment | Optional |
| `google-calendar` MCP | Meeting pattern analysis for enrichment | Optional |
| `slack` MCP | Channel activity for enrichment | Optional |
| `taliaz-bigquery-sql` skill | Operational metrics for clinical staff | Optional |