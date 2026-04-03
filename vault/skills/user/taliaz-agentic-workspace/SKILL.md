---
alfred_tags:
- taliaz/agentic-workspaces
- employee-personalization
description: 'Build a complete, personalized agentic workspace for any Taliaz employee.
  Orchestrates four skills (employee-profiler, job-guide, optica-guide, toolkit-generator)
  into a single pipeline that produces a self-contained workspace directory with profile,
  role spec, job guide, OPTICA map, AI agent toolkit, and quick-start materials. One
  command, one employee, one complete workspace. Triggers on: build workspace for,
  create agentic workspace, workspace for, set up workspace, employee workspace, full
  workspace for, onboard.'
name: taliaz-agentic-workspace
relationships:
- confidence: 0.8
  context: Semantically related Taliaz skills
  source: skills/user/taliaz-agentic-workspace/SKILL.md
  target: skills/user/taliaz-employee-profiler/SKILL.md
  type: related-to
- confidence: 0.8
  context: Semantically related Taliaz skills
  source: skills/user/taliaz-agentic-workspace/SKILL.md
  target: skills/user/taliaz-job-guide/SKILL.md
  type: related-to
- confidence: 0.8
  context: Semantically related Taliaz skills
  source: skills/user/taliaz-agentic-workspace/SKILL.md
  target: skills/user/taliaz-optica-guide/SKILL.md
  type: related-to
- confidence: 0.8
  context: Semantically related Taliaz skills
  source: skills/user/taliaz-agentic-workspace/SKILL.md
  target: skills/user/taliaz-toolkit-generator/SKILL.md
  type: related-to
---

# Taliaz Agentic Workspace Builder

Build a complete, personalized agentic workspace for any Taliaz employee with a single command. This is the master orchestrator that wraps all four profiling skills into one end-to-end pipeline.

## Core Directive

> "I am the Taliaz Agentic Workspace Builder. My purpose is to create a single, self-contained workspace that gives every employee everything they need to excel with AI assistance. I orchestrate four specialized skills into one seamless pipeline: profile the person, guide their excellence, map their governance, and arm them with AI agents. The result is a workspace that is immediately useful on day one and grows with the employee over time."

## What Gets Built

A single command produces a workspace directory with **5 organized folders** containing:

| Folder | Contents | Source Skill |
|--------|----------|-------------|
| `01-profile/` | Employee Profile (15 sections) + Role Specification (10 sections) + raw data | `taliaz-employee-profiler` |
| `02-job-guide/` | "How to Nail Your Job" guide (11 sections) + curated resources | `taliaz-job-guide` |
| `03-optica-guide/` | Personalized OPTICA framework map (97 checklists) + role mapping | `taliaz-optica-guide` |
| `04-toolkit/` | 3-8 AI agent skills + MCP integration guide + analysis | `taliaz-toolkit-generator` |
| `05-quick-start/` | Getting started guide + daily checklist + key contacts | This skill |

Plus a **README.md** master index and **workspace_manifest.json** for machine readability.

## Pipeline Architecture

```
                    ┌─────────────────────┐
                    │   Employee Name     │
                    └─────────┬───────────┘
                              │
                    ┌─────────▼───────────┐
                    │  Stage 1: EXTRACT   │  taliaz-employee-profiler
                    │  Profile + Role Spec│  → 15+ Supabase tables
                    └─────────┬───────────┘
                              │ profile JSON
                    ┌─────────▼───────────┐
                    │  Stage 2: GUIDE     │  taliaz-job-guide
                    │  Job Guide          │  → Perplexity API resources
                    └─────────┬───────────┘
                              │
                    ┌─────────▼───────────┐
                    │  Stage 3: OPTICA    │  taliaz-optica-guide
                    │  OPTICA Map         │  → 13-step framework mapping
                    └─────────┬───────────┘
                              │
                    ┌─────────▼───────────┐
                    │  Stage 4: TOOLKIT   │  taliaz-toolkit-generator
                    │  AI Agent Skills    │  → 8 archetype scoring
                    └─────────┬───────────┘
                              │
                    ┌─────────▼───────────┐
                    │  Stage 5: ASSEMBLE  │  This skill
                    │  Workspace Dir      │  → Copy + organize
                    └─────────┬───────────┘
                              │
                    ┌─────────▼───────────┐
                    │  Stage 6: DOCS      │  This skill
                    │  README + Quick-Start│  → Navigation + onboarding
                    └─────────┬───────────┘
                              │
                    ┌─────────▼───────────┐
                    │  Complete Workspace  │
                    │  /home/ubuntu/       │
                    │  workspaces/{name}/  │
                    └─────────────────────┘
```

## Workflow

### Step 1: Run the Orchestrator

```bash
cd /home/ubuntu/skills/taliaz-agentic-workspace
python3 scripts/build_workspace.py "Employee Name"
```

**Options:**
```bash
# Skip stages with existing outputs (faster for re-runs)
python3 scripts/build_workspace.py "Employee Name" --skip-existing

# Start from a specific stage (assumes previous stages done)
python3 scripts/build_workspace.py "Employee Name" --stage 3

# Custom output directory
python3 scripts/build_workspace.py "Employee Name" --output-dir /path/to/dir
```

The script runs all 6 stages sequentially, with progress tracking and error handling. Stages 2-4 are fault-tolerant — if one fails, the pipeline continues with reduced output.

### Step 2: Enrich with Live Context

After the automated pipeline completes, enrich the workspace with live data. See `references/enrichment-playbook.md` for detailed instructions.

**Minimum enrichment** (always do):
- **Gmail**: Search for recent emails involving the employee (last 30 days)
- **Calendar**: Check today's meetings and this week's schedule

**Recommended enrichment** (do when building detailed workspaces):
- **Monday.com**: Check active projects and tasks
- **Slack**: Search for recent channel activity
- **Google Drive**: Find recent meeting transcripts

**How to enrich:**
1. Query each source using the MCP tools
2. Add findings to the PA skill's reference files
3. Update the daily checklist with today's actual tasks
4. Add a "Current Focus" section to the README

### Step 3: Review and Validate

Review the generated workspace using `references/workspace-structure.md` quality checklist:

- [ ] README.md has accurate stats and navigation
- [ ] All 5 folders are populated with content
- [ ] Profile has 15 sections, no raw UUIDs
- [ ] Job guide has 11 sections with resources
- [ ] OPTICA guide has checklist items
- [ ] At least 3 toolkit skills generated
- [ ] Quick-start documents are personalized
- [ ] No placeholder or "Unknown" values in key fields

### Step 4: Deliver the Workspace

Present the workspace to the user with:
1. The README.md as the primary navigation document
2. A summary of what was generated (file counts, skill counts, key stats)
3. Attach the key documents: README, job guide, OPTICA guide, toolkit blueprint
4. Highlight any enrichment that was added
5. Note any gaps or areas that need manual input

## Handling Multiple Employees

To build workspaces for multiple employees:

```bash
# Build for specific employees
for name in "Rami" "Ohad" "Employee3"; do
    python3 scripts/build_workspace.py "$name"
done
```

Each workspace is fully independent and self-contained.

## Updating an Existing Workspace

To update a workspace after role changes:

```bash
# Full rebuild (overwrites everything)
python3 scripts/build_workspace.py "Employee Name"

# Incremental update (keeps existing outputs)
python3 scripts/build_workspace.py "Employee Name" --skip-existing
```

## Bundled Resources

| Resource | Description |
|----------|-------------|
| `scripts/build_workspace.py` | Master orchestrator — runs all 6 stages |
| `scripts/generate_workspace_docs.py` | Generates README, quick-start, manifest |
| `references/workspace-structure.md` | Workspace layout, quality checklist, regeneration guide |
| `references/enrichment-playbook.md` | How to enrich with Gmail, Calendar, Monday, Slack, Drive |

## Connector Dependencies

| Connector | Purpose | Required |
|-----------|---------|----------|
| `taliaz-employee-profiler` skill | Stage 1 — profile extraction | **Yes** |
| `taliaz-job-guide` skill | Stage 2 — job guide generation | **Yes** |
| `taliaz-optica-guide` skill | Stage 3 — OPTICA guide generation | **Yes** |
| `taliaz-toolkit-generator` skill | Stage 4 — toolkit generation | **Yes** |
| Supabase KB | Employee data (via profiler) | **Yes** |
| Perplexity API (`SONAR_API_KEY`) | Resource research (via job guide) | Recommended |
| `gmail` MCP | Email enrichment | Recommended |
| `google-calendar` MCP | Calendar enrichment | Recommended |
| `monday-com` MCP | Project enrichment | Optional |
| `slack` MCP | Channel enrichment | Optional |
| Google Drive (rclone) | Document enrichment | Optional |
| `bigquery` MCP | Operational metrics | Optional |

## Operating Principles

1. **One command, complete workspace** — The orchestrator handles everything. No manual steps required for the base workspace.
2. **Fault-tolerant pipeline** — If stages 2-4 fail, the pipeline continues. Only stage 1 (extraction) is mandatory.
3. **Enrichment is additive** — The automated pipeline produces a solid foundation. Enrichment makes it exceptional.
4. **Every file is personalized** — No generic templates. Every document is generated from the employee's actual data.
5. **Workspace is self-documenting** — The README serves as both navigation and summary. Any user can understand the workspace without external help.
6. **Regeneration is safe** — Workspaces can be rebuilt at any time without losing external context (enrichment should be re-applied).