---
alfred_tags:
- taliaz/knowledge-base
- data-ingestion
- protocols
description: Ingest emails from Gmail into Taliaz's Supabase knowledge base. Use when
  asked to "ingest emails", "process today's emails", "add emails to database", "sync
  emails to KB", or any request to import email data. Triggers on "ingest yesterday's
  emails", "process emails from [date]", "sync my inbox", "add recent emails to knowledge
  base".
name: taliaz-email-ingest
---

# Taliaz Email Ingestion

Fetches emails from Gmail and populates the Taliaz Supabase knowledge base with structured data.

## Quick Start

### Step 1: Fetch Emails from Gmail
```bash
manus-mcp-cli tool call gmail_search_messages --server gmail \
  --input '{"q": "after:2026/01/26 before:2026/01/27", "max_results": 100}'
```
This saves results to `/tmp/manus-mcp/mcp_result_*.json`

### Step 2: Run Ingestion
```bash
python3 /home/ubuntu/skills/taliaz-email-ingest/scripts/ingest_emails.py <result_file.json>
```

### Example: Ingest Today's Emails
```bash
# Fetch today's emails
manus-mcp-cli tool call gmail_search_messages --server gmail \
  --input '{"q": "after:2026/01/26 before:2026/01/27", "max_results": 100}'

# Run ingestion (use the path from MCP output)
python3 /home/ubuntu/skills/taliaz-email-ingest/scripts/ingest_emails.py /tmp/manus-mcp/mcp_result_*.json
```

### Preview Without Inserting
```bash
python3 /home/ubuntu/skills/taliaz-email-ingest/scripts/ingest_emails.py <result_file.json> --dry-run
```

## Tables Populated

| Table | What Gets Inserted |
|-------|-------------------|
| `email_digests` | Main email record with metadata, content, category |
| `email_entity_links` | Links to mentioned people, projects, organizations |
| `entity_occurrences` | Entity mentions for tracking over time |
| `entities_normalized` | New entities discovered (if any) |

## Processing Pipeline

### 1. Fetch Emails
Uses Gmail MCP to search emails by date range.

### 2. Work Detection
Filters to work-related emails only:
- **Domain match**: taliazhealth.com, healthymind.co.il, plaud.ai
- **Keyword match**: clinic, patient, מטופל, קליניקה, meeting, פגישה, etc.

### 3. Categorization
Assigns category based on content:
- `Clinical_Operations` - Patient care, clinic ops
- `Innovation_Technology` - AI, automation, tech
- `Finance` - Budget, expenses
- `Analytics` - KPIs, metrics
- `Meetings` - Transcripts, scheduling
- `Research` - Studies, publications
- `HR` - Employee matters
- `Marketing` - Campaigns
- `General` - Other

### 4. Entity Extraction
Matches against known entities:
- **People**: From `entities_normalized` (person type)
- **Projects**: From `entities_normalized` and `projects` tables
- **Organizations**: From `entities_normalized` (organization type)

### 5. Database Insertion
Inserts to all relevant tables with proper linking.

## Entity Lookups

The script uses a cached lookup file for fast entity matching:
```
/home/ubuntu/entity_lookups.json
```

### Rebuild Lookups
If entities have been added to the database, rebuild the cache:
```bash
python3 /home/ubuntu/skills/taliaz-email-ingest/scripts/build_lookups.py
```

## Output Example

```
============================================================
TALIAZ EMAIL INGESTION
============================================================
Date range: 2026-01-25 to 2026-01-26
Entity lookups: 691 persons, 892 projects
------------------------------------------------------------
✓ ריבי - עדכון עבודה מהיום... (General, 4P)
✓ Re: למדדי KPI בנוגע לביטולים... (Clinical_Operations, 3P)
✓ [Plaud-AutoFlow] 01-25 פגישה... (Meetings, 5P)
⊘ Skipped (not work): 19bf5c93f308e8c0
============================================================
INGESTION SUMMARY
============================================================
Emails processed:        71
Emails inserted:         50
Skipped (existing):      8
Skipped (not work):      13
Entity links created:    200
Entity occurrences:      113
============================================================
```

## Manual Workflow

If the script is unavailable, follow these steps:

### Step 1: Fetch Emails via MCP
```bash
manus-mcp-cli tool call gmail_search_messages --server gmail \
  --input '{"q": "after:2026/01/25 before:2026/01/26", "max_results": 100}'
```

### Step 2: Process Each Email
For each email in the result:

1. **Check if work-related** - Match domain or keywords
2. **Skip if exists** - Query `email_digests` by `gmail_message_id`
3. **Categorize** - Match content against category keywords
4. **Extract entities** - Match against entity lookups
5. **Insert to `email_digests`**
6. **Insert to `email_entity_links`** - One row per entity
7. **Insert to `entity_occurrences`** - For people entities

### Step 3: Verify
```sql
SELECT COUNT(*) FROM email_digests WHERE email_date >= '2026-01-25';
SELECT COUNT(*) FROM email_entity_links WHERE created_at >= '2026-01-26';
```

## References

- `references/tables.md` - Full table schemas and field descriptions
- `scripts/ingest_emails.py` - Main ingestion script
- `scripts/build_lookups.py` - Entity lookup builder

## Troubleshooting

### "No emails found"
- Check date format: `YYYY-MM-DD`
- Verify Gmail MCP is configured
- Try broader date range

### "Entity lookups empty"
- Run `build_lookups.py` to rebuild cache
- Check Supabase connection

### "Duplicate key error"
- Email already exists in database
- Script automatically skips duplicates

### "Not work related"
- Email doesn't match Taliaz domains or keywords
- This is expected for personal emails