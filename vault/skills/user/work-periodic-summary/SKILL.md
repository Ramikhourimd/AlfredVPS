---
name: work-periodic-summary
description: Generate comprehensive work status summaries and agendas for any time period. Triggers on "daily summary", "weekly summary", "what happened last X days/weeks", "work status", "agenda for today/week", "catch me up", "what do I need to focus on". Collects context from Google Calendar, Gmail (unanswered threads), and Google Drive meeting transcripts, then enriches with Taliaz KB from Supabase for people/project context.
---

# Work Periodic Summary Skill

Generate structured work summaries by aggregating data from Calendar, Gmail, Drive transcripts, and organizational KB.

## Supported Period Formats

Parse user queries for time periods:
- "daily" / "today" → last 24 hours
- "weekly" / "this week" → last 7 days
- "last N days/weeks/months" → calculated range
- "this month" / "last month" → calendar month
- "since Monday" / "since [date]" → from specified date

## Data Collection Workflow

Execute these steps in order:

### Step 1: Calculate Date Range

Convert the period query to RFC3339 timestamps for API calls.

### Step 2: Google Calendar

Use `list_gcal_events` with `time_min` and `time_max` for the period.

Collect:
- Meeting titles and times
- Attendees
- Meeting descriptions (for context on topics discussed)

### Step 3: Gmail - Unanswered Threads

Use `search_gmail_messages` with queries:
```
is:inbox is:unread -category:promotions -category:social
```

Then filter for threads where:
- User has not replied (check thread for outgoing messages)
- Needs attention/action

For each relevant thread, use `read_gmail_thread` to get full context.

Categorize by urgency:
- **High**: Contains "urgent", "ASAP", "deadline", or from key stakeholders
- **Medium**: Awaiting reply for 2+ days, or contains action requests
- **Low**: Informational, FYI threads

### Step 4: Google Drive - Meeting Transcripts

Use `google_drive_search` to find modified files:
```python
api_query = "'1BdEsYy1K8ujqjegPAfcxUrW4rDhortRd' in parents and modifiedTime > '{start_date}'"
```

Folder ID: `1BdEsYy1K8ujqjegPAfcxUrW4rDhortRd`

For relevant transcripts, use `google_drive_fetch` to read content.

### Step 5: Supabase KB Enrichment

Query the Taliaz KB for context on entities mentioned in emails/transcripts.

Use the `taliaz-kb-query` skill patterns:

**For recent decisions/meetings:**
```bash
python3 /mnt/skills/user/taliaz-kb-query/scripts/query_supabase.py memory_l1_core "source_file,Meeting_date,topics,events" '{"Meeting_date": "gte.[start_date]"}' '{"order": "Meeting_date.desc", "limit": 20}'
```

**For project context:**
```bash
python3 /mnt/skills/user/taliaz-kb-query/scripts/query_supabase.py projects "name,status,description,owner_employee_id" '{"status": "in.(Planning/Initiation,in_progress)"}'
```

**For entity context (people/orgs mentioned):**
```bash
python3 /mnt/skills/user/taliaz-kb-query/scripts/query_supabase.py entities_normalized "canonical_name,description,inferred_role" '{"canonical_name": "ilike.*[name]*"}'
```

Cross-reference names/projects from Gmail and transcripts with KB entries.

## Output Structure

Generate a structured report in this format:

```markdown
# Work Summary: [Period Description]
*Generated: [timestamp]*

## 📅 Period Overview
- **Date Range**: [start] to [end]
- **Meetings Held**: [count]
- **Transcripts Processed**: [count]
- **Emails Requiring Attention**: [count]

## 🗓️ Calendar Highlights
[List key meetings with brief notes on purpose/attendees]

## 📝 Meeting Transcripts Summary
[For each transcript in the period:]
- **[Meeting Name]** ([date])
  - Key decisions: [from KB events->decisions]
  - Action items: [from KB events->actions]
  - Open questions: [from KB events->open_questions]

## 📧 Action Required (by Urgency)

### 🔴 High Priority
[Threads needing immediate attention]
- **Subject**: [subject]
  - From: [sender]
  - Waiting since: [date]
  - Context: [brief summary]

### 🟡 Medium Priority
[Threads awaiting response]

### 🟢 Low Priority
[FYI/informational items]

## 🎯 Open Issues & Tasks
[Aggregated from KB events->actions and email action items]
- [ ] [Task description] - Owner: [name] - Source: [meeting/email]

## 📋 Suggested Agenda / Priorities
Based on the above:
1. [Most urgent item]
2. [Second priority]
3. [etc.]

## 🔗 KB Context
[Relevant background from Supabase on key topics/people/projects mentioned]
```

## Guidelines

1. **Parallel data collection**: Gather Calendar, Gmail, and Drive data concurrently when possible
2. **Smart deduplication**: Same topic in transcript and email? Merge into single item
3. **KB enrichment is additive**: Use KB to add context, not replace source data
4. **Urgency determination**: Prioritize based on:
   - Sender importance (leadership, key stakeholders)
   - Time waiting for response
   - Explicit urgency markers
   - Business impact indicators
5. **Actionable output**: Every section should inform decisions or next steps
6. **Hebrew handling**: Names may appear in Hebrew in transcripts - match against `aliases` in entities_normalized
