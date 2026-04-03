---
alfred_tags:
- alfred-os/core
- obsidian/system
- ai-assistant
janitor_note: FM001 — not a vault record. This is the project README. Should not have
  type/created frontmatter. Exclude from vault scanning.
relationships:
- confidence: 0.9
  context: Main readme and start note
  source: README.md
  target: Start Here.md
  type: related-to
- confidence: 0.7
  context: Overview links to core assumption
  source: README.md
  target: assumption/Person Record as Identity Anchor for System Bootstrap.md
  type: related-to
- confidence: 0.7
  context: Overview links to graph assump
  source: README.md
  target: assumption/Wikilink Graph Is Sufficient for All Record Relationships.md
  type: related-to
- confidence: 0.8
  context: Readme supports project dev
  source: README.md
  target: project/Alfred Development.md
  type: supports
---

# Alfred OS

A canonical Obsidian vault that functions as a unified operational system. An AI assistant ("Alfred") manages records, synthesizes briefings, and processes inline instructions.

## Quick Start

1. Open this folder as an Obsidian vault
2. Create a Person record for yourself in `person/`
3. Open `view/Home.md` and link your Person record as `owner:`
4. Create projects, tasks, and other records using the templates in `_templates/`
5. See `Start Here.md` for a full walkthrough

## What's Inside

- **20 record types** — project, task, session, conversation, input, person, org, location, note, decision, process, run, event, account, asset + the Learn system (assumption, constraint, contradiction, synthesis)
- **21 base view definitions** — live tables that auto-populate based on record links
- **Templates** for every record type
- **Architecture docs** in `_docs/`
- **3 views** — Home (personal), CRM (relationships), Task Manager (all work)

## Requirements

- Obsidian 1.8+ with the **Bases** core plugin enabled (included in config)