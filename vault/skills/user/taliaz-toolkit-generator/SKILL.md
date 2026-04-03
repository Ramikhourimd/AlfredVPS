---
alfred_tags:
- taliaz/agentic-workspaces
- employee-personalization
description: 'Generates personalized AI agent skills and MCP integration guides for
  Taliaz employees. Analyzes employee profiles (from taliaz-employee-profiler), job
  guides (from taliaz-job-guide), and OPTICA maps (from taliaz-optica-guide) to produce
  a complete toolkit of 3-8 custom skills tailored to each employee''s role, responsibilities,
  and expertise. Triggers on: generate toolkit for, create skills for, build agents
  for, personalized toolkit, agent toolkit for, skill set for.'
janitor_note: FM001 — This is a skill definition file (SKILL.md), not a vault record.
  It uses its own frontmatter schema (name, description, alfred_tags) and does not
  require type/created fields. Scanner false positive — exclude skills/ from vault
  scans.
name: taliaz-toolkit-generator
---

# Taliaz Toolkit Generator

Generates a personalized set of AI agent skills and MCP integrations for any Taliaz employee. Consumes the employee's profile, job guide, and OPTICA map to produce production-ready skill files.

## Prerequisites

This skill depends on outputs from the employee profiling pipeline:

| Dependency | Required | Provides |
|------------|----------|----------|
| `taliaz-employee-profiler` | **Yes** | Profile JSON with responsibilities, expertise, tools, stakeholders, knowledge |
| `taliaz-job-guide` | Optional | Development areas, quick wins, KRAs |
| `taliaz-optica-guide` | Optional | OPTICA step ownership, governance roles |

If the profile JSON does not exist, run `taliaz-employee-profiler` first. If job guide or OPTICA map are missing, the toolkit will still generate but with less personalization.

## Workflow

### Step 1: Ensure Profile Exists

Check if the employee's profile JSON exists at `/tmp/{name}_data.json`. If not, run the profiler:

```bash
cd /home/ubuntu/skills/taliaz-employee-profiler
python3 scripts/extract_employee_data.py "{Employee Name}" /tmp/{name}_data.json
```

Also check for optional enrichment files:
- `/tmp/{name}_job_guide.md` — from `taliaz-job-guide`
- `/tmp/{name}_optica_guide.md` — from `taliaz-optica-guide`

### Step 2: Run the Analysis Engine

```bash
cd /home/ubuntu/skills/taliaz-toolkit-generator
python3 scripts/analyze_employee.py /tmp/{name}_data.json /tmp/{name}_analysis.json \
    [--job-guide /tmp/{name}_job_guide.md] \
    [--optica-guide /tmp/{name}_optica_guide.md]
```

This produces an analysis JSON with:
- Responsibility clusters and automation opportunities
- Expertise domains and go-to areas
- Archetype scores (which skills to generate)
- MCP recommendations (which integrations to configure)

### Step 3: Review Analysis Results

Read the analysis JSON and verify:
- The recommended skills make sense for the employee's role
- The archetype scores reflect the employee's actual responsibilities
- The MCP recommendations are appropriate

If needed, adjust the analysis JSON before proceeding.

### Step 4: Generate the Toolkit

```bash
python3 scripts/generate_toolkit.py /tmp/{name}_analysis.json /tmp/{name}_toolkit/
```

This generates:
- `toolkit_blueprint.md` — Master analysis and recommendations document
- `{name}-pa/` — Personal assistant skill (always generated)
- Additional skill directories based on archetype scores
- `mcp_integration_guide.md` — MCP configuration guide

### Step 5: Enrich Generated Skills

After generation, enrich the skills with live context:

1. **Query the KB** via `taliaz-kb-query` for recent meetings and decisions relevant to the employee
2. **Check Gmail** for communication patterns and key threads
3. **Review Calendar** for recurring meetings to add to the PA's daily ops
4. **Check Monday.com** for active projects to reference in skills

Add this context to the generated reference files to make them more specific and actionable.

### Step 6: Deliver the Toolkit

Present the complete toolkit to the user:
1. The toolkit blueprint (master analysis document)
2. Each generated skill's SKILL.md
3. The MCP integration guide
4. Summary of what was generated and why

## Skill Archetypes

Read `references/skill-archetypes.md` for detailed descriptions of each skill archetype, including:
- When each archetype is generated (scoring thresholds)
- What files each archetype produces
- Quality checks for each archetype
- Enrichment strategies

## MCP Configuration

Read `references/mcp-recommendations.md` for:
- Available MCPs and their capabilities
- Recommendation scoring logic
- Role-based defaults
- Usage notes and gotchas for each MCP

## Output Structure

```
/tmp/{name}_toolkit/
├── toolkit_blueprint.md          — Master analysis document
├── {name}-pa/                    — Personal assistant skill
│   ├── SKILL.md
│   └── references/
│       ├── daily-ops.md
│       ├── knowledge-data.md
│       └── communication.md
├── {name}-{archetype}/           — Additional skills (2-7 more)
│   ├── SKILL.md
│   └── references/
└── mcp_integration_guide.md      — MCP configuration guide
```

## Bundled Resources

| Resource | Description |
|----------|-------------|
| `scripts/analyze_employee.py` | Analysis engine — parses profile, scores archetypes, recommends MCPs |
| `scripts/generate_toolkit.py` | Toolkit generator — produces all skill files and documents |
| `references/skill-archetypes.md` | Detailed archetype descriptions and quality checks |
| `references/mcp-recommendations.md` | MCP recommendation logic and configuration guides |