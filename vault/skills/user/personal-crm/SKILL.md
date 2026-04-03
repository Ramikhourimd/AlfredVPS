---
name: personal-crm
description: Build and manage a personal CRM by scanning Gmail, Calendar, and Drive. Supports natural language queries, relationship health tracking, and follow-up reminders. Use to find contacts, analyze relationships, or get a summary of your network.
---

# Personal CRM

This skill builds and manages a personal Customer Relationship Management (CRM) system by automatically scanning your Gmail, Google Calendar, and Google Drive to discover contacts and interactions. It stores this information in a local SQLite database, enriches it with AI-powered profiling, and allows you to query your network using natural language.

## Core Features

- **Automatic Contact Discovery**: Scans Gmail and Google Calendar for contacts from the past year.
- **Noise Filtering**: Automatically identifies and filters out marketing emails, newsletters, and other noise.
- **AI-Powered Profiling**: Builds rich profiles for each contact, including their company, role, and how you know them.
- **Natural Language Query**: Ask questions like "who do I know at NVIDIA?" or "who haven't I talked to in a while?"
- **Relationship Health**: Scores relationships from 0-100 to flag stale connections.
- **Follow-up Reminders**: Create, snooze, and manage reminders to stay in touch.
- **Duplicate Detection**: Identifies potential duplicate contacts and suggests merges.
- **Document Linking**: Links relevant documents from your Google Drive to contacts.

## Main Workflow

Follow these steps to set up and use your Personal CRM. The database is stored locally at `~/.personal-crm/crm.db`.

### Step 1: Initial Scan & Enrichment

First, scan your accounts to populate the CRM. This command scans Gmail and Calendar for the past 12 months, then enriches the new contacts with AI-powered profiles and embeddings.

```bash
# Scan Gmail and Calendar
python3 /home/ubuntu/skills/personal-crm/scripts/crm_scanner.py --source all --months 12

# Enrich all new contacts
python3 /home/ubuntu/skills/personal-crm/scripts/crm_profiler.py --action enrich --limit 1000
```

### Step 2: Query Your CRM

Once your CRM is populated, you can ask natural language questions. The query engine will automatically determine whether to use semantic search, generate a SQL query, or perform a direct lookup.

```bash
# Find contacts by topic, company, or role
python3 /home/ubuntu/skills/personal-crm/scripts/crm_query.py "who do I know at Google working on AI?"

# Ask analytical questions
python3 /home/ubuntu/skills/personal-crm/scripts/crm_query.py "who haven't I talked to in over 6 months?"

# Look up a specific contact
python3 /home/ubuntu/skills/personal-crm/scripts/crm_query.py "tell me about jane@example.com"
```

### Step 3: Maintain Your CRM

Periodically run these commands to keep your CRM up-to-date.

```bash
# Update all relationship health scores
python3 /home/ubuntu/skills/personal-crm/scripts/crm_health.py --action update-scores

# Find and merge duplicate contacts
python3 /home/ubuntu/skills/personal-crm/scripts/crm_profiler.py --action dedup

# Scan Google Drive and link documents to contacts
python3 /home/ubuntu/skills/personal-crm/scripts/crm_docs.py --action scan
```

## All Commands

This skill is composed of several modules, each with its own set of commands.

### `crm_scanner.py`: Discover Contacts

- **Scan all sources**: `python3 scripts/crm_scanner.py --source all`
- **Scan only Gmail**: `python3 scripts/crm_scanner.py --source gmail --months 6`
- **Scan with a custom Gmail query**: `python3 scripts/crm_scanner.py --source gmail --gmail-query "from:example.com"`

### `crm_profiler.py`: Enrich and Deduplicate

- **Enrich new contacts**: `python3 scripts/crm_profiler.py --action enrich --limit 50`
- **Force re-enrichment of all contacts**: `python3 scripts/crm_profiler.py --action enrich --force`
- **Detect duplicates**: `python3 scripts/crm_profiler.py --action dedup`

### `crm_health.py`: Health & Reminders

- **Update all health scores**: `python3 scripts/crm_health.py --action update-scores`
- **List stale contacts (score < 30)**: `python3 scripts/crm_health.py --action stale --threshold 30`
- **Get AI-powered follow-up suggestions**: `python3 scripts/crm_health.py --action suggest`
- **Get a detailed report for a contact**: `python3 scripts/crm_health.py --action report --contact-id 123`
- **Create a reminder**: `python3 scripts/crm_health.py --action create-reminder --contact-id 123 --note "Follow up on proposal" --due "2026-03-15T09:00:00Z"`
- **List pending reminders**: `python3 scripts/crm_health.py --action list-reminders`

### `crm_query.py`: Natural Language Search

- **Ask a question**: `python3 scripts/crm_query.py "your question here"`
- **See raw JSON results**: `python3 scripts/crm_query.py "your question here" --raw`

### `crm_docs.py`: Link Google Drive Files

- **Scan root of Drive and link files**: `python3 scripts/crm_docs.py --action scan`
- **Scan specific Drive folders**: `python3 scripts/crm_docs.py --action scan --paths "Meetings/2025" "Projects/Alpha"`
- **Manually link a file**: `python3 scripts/crm_docs.py --action link --contact-id 123 --drive-path "path/to/your/doc.pdf"`
- **List documents for a contact**: `python3 scripts/crm_docs.py --action list --contact-id 123`

## Bundled Resources

- `scripts/crm_db.py`: Core database schema and helper functions.
- `scripts/crm_scanner.py`: Gmail and Calendar scanner.
- `scripts/crm_profiler.py`: Contact enrichment and deduplication engine.
- `scripts/crm_health.py`: Relationship health scoring and reminder management.
- `scripts/crm_query.py`: Natural language query engine.
- `scripts/crm_docs.py`: Google Drive document linker.
