---
name: agent-builder
description: "A meta-skill that builds other skills. Given a concept for a new agent (e.g., a work counselor, a creative partner), this skill researches the role, designs a context-aware system prompt, identifies required resources and connectors, and scaffolds a complete, production-ready Manus skill. Triggers on: create a new agent, build a skill for, new agent concept."
---

# Agent Builder: A Skill for Building Skills

This skill provides a structured, repeatable workflow for creating new, high-quality Manus skills. It codifies the exact process used to build the `gravity-agent`, ensuring that every new skill is deeply researched, contextually aware, and production-ready.

When tasked with creating a new agent or skill, you MUST follow this five-phase workflow. Do not deviate.

## The Agent Building Workflow

| Phase | Description | Key Actions |
|---|---|---|
| **1. Deconstruct & Research** | Understand the agent concept and the user's operational context. | Query KB for user profile, search externally for domain best practices. |
| **2. Design Architecture** | Plan the skill's structure, prompts, and resources. | Define system prompt, identify required scripts/references, list connector dependencies. |
| **3. Construct the Skill** | Write all the necessary files for the skill. | `init_skill.py`, write `SKILL.md`, write `references/`, write `scripts/`. |
| **4. Test & Refine** | Validate the skill and ensure all components work as expected. | Test scripts, fix bugs, run `quick_validate.py`. |
| **5. Package & Deliver** | Create a summary document and deliver the final skill package. | Write a toolkit summary, use `message` to deliver all files. |

---

## Phase 1: Deconstruct & Research

Your first step is to become an expert on the requested agent AND the person you are building it for. Generic skills are useless. Your value comes from deep, context-specific understanding.

### 1a. Identify the User

**CRITICAL: Never assume who the user is.** Use the `taliaz-kb-query` skill to dynamically look up the user's profile. Query the following Supabase tables:

```
employees          → full_legal_name, job_title, employment_type
employee_roles     → description, is_primary (filter by employee_id)
responsibilities   → all responsibilities (filter by employee_id)
expertise_areas    → area, description, is_go_to_person (filter by employee_id)
speaker_memory     → style_markers, domain_markers, topic_profile (filter by speaker_name)
```

This gives you the user's role, responsibilities, expertise, communication style, and domain focus. This is the foundation for personalizing every agent you build.

### 1b. Deconstruct the Agent Concept

What is the core purpose of this new agent? What problem does it solve? What are the desired outputs?

### 1c. Understand Available Data & Knowledge

Read the following skills to understand what data sources the new agent can leverage:

| Skill to Read | What You Learn |
|---|---|
| `taliaz-kb-query/SKILL.md` | What knowledge is available in the KB (meetings, decisions, people, projects). |
| `taliaz-bigquery-sql/SKILL.md` | What quantitative data is available (patients, meetings, revenue, marketing). |

### 1d. External Domain Research

Use the `search` tool to find best practices, frameworks, and prompting techniques related to the agent's domain. Run at least 2-3 searches with different query angles. Visit the most relevant results for detailed information.

## Phase 2: Design Architecture

With a deep understanding of the agent's role and the user's context, design the skill's architecture.

1.  **Define the Core System Prompt**: This is the agent's constitution. It must define the agent's persona, core directive, and operating principles. It must reference the user's actual work context (role, domain, organization), not generic placeholders.

2.  **Identify Bundled Resources**: Consult `references/skill-output-template.md` for the standard structure. Determine what the skill needs:
    *   `scripts/`: For deterministic, repeatable actions.
    *   `references/`: For detailed instructions, protocols, or contextual guides.
    *   `templates/`: For boilerplate output formats.

3.  **List Connector Dependencies**: Consult `references/available-connectors.md` for the full inventory of available tools, skills, and MCPs. Select the minimum set required for this agent.

## Phase 3: Construct the Skill

1.  **Initialize the Skill**:
    ```bash
    python3 /home/ubuntu/skills/skill-creator/scripts/init_skill.py <new-skill-name>
    ```

2.  **Write the `SKILL.md` File**: Follow the template in `references/skill-output-template.md`. It must include: frontmatter with description and triggers, overview, system prompt, operating principles, usage instructions, and a resource table.

3.  **Write the Bundled Resources**: Create all reference files, scripts, and templates identified in Phase 2.

## Phase 4: Test & Refine

1.  **Test All Scripts**: Execute every script to ensure it runs without errors. Fix bugs and re-test.

2.  **Validate the Skill Structure**:
    ```bash
    python3 /home/ubuntu/skills/skill-creator/scripts/quick_validate.py <new-skill-name>
    ```

## Phase 5: Package & Deliver

1.  **Write a Toolkit Summary**: A separate Markdown file providing a high-level overview of the skill, its components, and how to use it.

2.  **Deliver the Final Package**: Use the `message` tool to deliver the `SKILL.md` file and all associated resources as attachments.
