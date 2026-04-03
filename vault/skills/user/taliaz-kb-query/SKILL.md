---
alfred_tags:
- taliaz/knowledge-base
- data-ingestion
- protocols
description: Query Taliaz's organizational knowledge base to answer work-related questions.
  Uses Supabase KB as primary source, enriched with Gmail, Google Calendar, Google
  Drive, and Slack for comprehensive answers. Use this skill FIRST when asked about
  meetings, decisions, employees, projects, responsibilities, policies, skills, expertise,
  RACI assignments, communications (email/WhatsApp/Slack), external stakeholders,
  training, credentials, institutional knowledge, or any organizational data. Triggers
  on "What did we decide...", "Who is responsible for...", "Who owns...", "Who has
  skills in...", "What happened in the meeting...", "RACI for...", "Emails about...",
  "Slack discussions...", "Go-to person for...", or any factual question about Taliaz
  operations. Always query before answering work questions.
name: taliaz-kb-query
---

# Taliaz Knowledge Base Query Skill

Query the organizational knowledge base to answer work-related questions with accurate, up-to-date information from **multiple sources**.

## ⚠️ Multi-Source Query Framework (GSD)

**Great answers require Gathering from multiple Sources before Delivering.**

This skill queries not just the Supabase KB, but also enriches answers with context from Gmail, Google Calendar, Google Drive, and Slack. The right sources depend on the question type.

### Query Strategy

```
QUESTION RECEIVED
  → ROUTE to primary Supabase table(s)
  → DETERMINE if external enrichment needed
  → QUERY external sources (Gmail, Calendar, Drive, Slack) as appropriate
  → SYNTHESIZE answer from all sources
  → CITE where information came from
```

### Source Priority by Question Type

| Question Type | Primary (Supabase) | Enrichment Sources |
|---------------|--------------------|--------------------|
| **Meeting decisions** | `memory_l1_core`, `memory_l2_context_intent` | Gmail (agendas/follow-ups), Calendar (attendees), Slack (discussions) |
| **Project status** | `projects`, `project_raci` | Gmail (updates), Slack (channels), Drive (docs) |
| **Who is responsible** | `responsibilities`, `expertise_areas` | Calendar (recent meetings), Slack (activity) |
| **Recent communications** | `email_digests`, `whatsapp_ai_extractions` | Gmail (live threads), Slack (live messages) |
| **Employee info** | `employees`, `employee_roles` | Calendar (availability), Slack (profile) |
| **Documents/knowledge** | `documents`, `memory_l1_core` | Drive (live docs), Gmail (shared links) |
| **What's happening now** | `calendar_events`, `daily_summaries` | Calendar (live), Gmail (today), Slack (recent) |

---

## Connection Details (Supabase)

- **URL**: `https://biaxrsfkuubslzxlcqxq.supabase.co/rest/v1/`
- **API Key**: `eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJpYXhyc2ZrdXVic2x6eGxjcXhxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDIzODczNjQsImV4cCI6MjA1Nzk2MzM2NH0.LOGEr9WMq14W_PSvKd_CjLxJ1olk5SV7xWoBY1FXlRU`

## Query Execution (Supabase)

Use `scripts/query_supabase.py` to execute Supabase queries:

```bash
python3 scripts/query_supabase.py "<table_name>" "<select_columns>" "[filters_json]" "[options_json]"
```

**Options JSON** supports: `{"order": "column.desc", "limit": 10}`

## External Tools Reference

| Tool | Purpose | When to Use |
|------|---------|-------------|
| `search_gmail_messages` | Find email threads by topic, sender, date | Communications questions, meeting context, follow-ups |
| `read_gmail_thread` | Deep-read a specific email thread | When search finds relevant thread needing full context |
| `list_gcal_events` | Find calendar events, attendees, times | Meeting questions, scheduling, who was present |
| `fetch_gcal_event` | Get full details of a specific event | Deep-dive on a specific meeting |
| `google_drive_search` | Search Drive for documents | Document questions, finding related files |
| `google_drive_fetch` | Read a specific Google Doc | When a relevant doc is identified |
| `slack_search_public` | Search public Slack messages | Team discussions, informal decisions, updates |
| `slack_search_public_and_private` | Search all Slack (with user consent) | When public search misses, DM context needed |
| `slack_read_thread` | Deep-read a specific Slack thread | When search finds relevant discussion |
| `slack_read_channel` | Read recent messages from a channel | Channel activity, recent discussions |

### Google Drive Key Folders

| Folder | ID | Contents |
|--------|----|----------|
| **Taliaz Meeting Transcripts** | `1BdEsYy1K8ujqjegPAfcxUrW4rDhortRd` | All meeting transcript files |

---

## Question-to-Query Routing

### Meeting & Decision Questions
**Triggers**: "what did we decide", "meeting about", "discussed", "last week's meeting", "talked about"
**Supabase Tables**: 
- `memory_l1_core` (1,224 rows) — `source_file, Meeting_date, topics, events->decisions, events->summary, facts, category`
- `memory_l2_context_intent` — related projects/people context, follow-ups, risks

**External Enrichment** (RECOMMENDED):
```
# Find related email threads (agendas, follow-ups)
search_gmail_messages(q="subject:([meeting topic]) after:YYYY/MM/DD before:YYYY/MM/DD")

# Find the calendar event (attendees, exact time)
list_gcal_events(time_min="...", time_max="...", query="[topic]")

# Find Slack pre/post-meeting discussions
slack_search_public(query="[topic] after:YYYY-MM-DD before:YYYY-MM-DD")

# Find related transcripts in Drive
google_drive_search(
  api_query="'1BdEsYy1K8ujqjegPAfcxUrW4rDhortRd' in parents",
  semantic_query="[meeting topic]"
)
```

### Responsibility & Ownership Questions
**Triggers**: "who is responsible", "who owns", "who handles", "who manages", "whose job"
**Supabase Tables**: 
1. `responsibilities` (315 rows) — Primary responsibility assignments
2. `projects` — For project ownership via `owner_employee_id`
3. `expertise_areas` (152 rows) — Go-to person designations
4. `raci_assignment_rules` (13 rows) — Default RACI by domain

**External Enrichment** (optional):
- Slack: Check recent activity in relevant channels to confirm current ownership
- Calendar: Recent meetings with the person to verify active involvement

### RACI Questions
**Triggers**: "RACI for", "who is accountable", "who should be consulted", "who needs to be informed"
**Supabase Tables**:
1. `project_raci` (2,338 rows) — RACI assignments per project
2. `raci_assignment_rules` — Default rules by domain/category

### Employee & People Questions
**Triggers**: "who is [name]", "tell me about [person]", "contact for", "team members", "works in"
**Supabase Tables**:
1. `employees` (23 rows) — Core employee profiles
2. `employee_roles` (24 rows) — Role assignments with managers
3. `entities_normalized` (1,009 rows) — All people/orgs mentioned
4. `speaker_memory` (112 rows) — Speaker patterns from transcripts

**External Enrichment** (optional):
- Slack: `slack_search_users(query="[name]")` for Slack profile info
- Calendar: Recent meetings they attended
- Gmail: Recent email threads involving them

### Skills & Expertise Questions
**Triggers**: "who has skills in", "who knows", "expertise in", "proficient in", "experience with"
**Supabase Tables**:
1. `employee_skills` (190 rows) — Skill assignments
2. `expertise_areas` (152 rows) — Go-to designations
3. `employee_tools` (38 rows) — Tool proficiencies
4. `institutional_knowledge` (150 rows) — Critical knowledge areas

### Project Questions
**Triggers**: "current projects", "project status", "working on", "project owner"
**Supabase Tables**: 
1. `projects` (1,787 rows) — Project registry
2. `employee_projects` — Project assignments
3. `project_raci` — RACI assignments

**External Enrichment** (RECOMMENDED):
- Slack: Search project channels for recent updates
- Gmail: Recent project-related email threads
- Drive: Project documents and shared files

### Organizational Structure Questions
**Triggers**: "who reports to", "team structure", "department", "manager of"
**Supabase Tables**:
1. `departments` (6 rows)
2. `teams` (6 rows)
3. `employee_roles` — Has `direct_manager_id`, `department_id`, `team_id`
4. `job_titles` (28 rows)

### Communication/Email Questions
**Triggers**: "emails about", "email from", "recent communications", "sent email"
**Supabase Tables** (historical/processed):
1. `email_digests` (549 rows) — Processed emails with AI summaries
2. `email_attachments` (433 rows) — Attachment details
3. `email_entity_links` (732 rows) — Links to entities

**External Enrichment** (RECOMMENDED — for live/recent emails):
```
# Search live Gmail for current threads
search_gmail_messages(q="[topic or person] newer_than:7d")

# Read full thread for context
read_gmail_thread(thread_id="...")
```

### Slack Questions
**Triggers**: "Slack discussion", "what was said in Slack", "channel messages", "Slack thread about"
**Supabase Tables** (if synced):
- `slack_messages` — Historical synced messages

**External Enrichment** (PRIMARY — always use live tools):
```
# Search public channels
slack_search_public(query="[topic] after:YYYY-MM-DD")

# Search all channels (ask user consent)
slack_search_public_and_private(query="[topic]")

# Read specific channel
slack_read_channel(channel_id="...", limit=20)

# Read specific thread
slack_read_thread(channel_id="...", message_ts="...")
```

### WhatsApp Questions
**Triggers**: "WhatsApp", "group chat", "discussed in chat"
**Supabase Tables**:
1. `whatsapp_groups` (10 rows) — Group metadata
2. `whatsapp_messages` (26,833 rows) — Messages
3. `whatsapp_ai_extractions` (358 rows) — AI-extracted insights
4. `whatsapp_participants` (182 rows) — Participants

### Calendar & Scheduling Questions
**Triggers**: "when is", "meeting schedule", "upcoming meetings", "who was in the meeting"
**Supabase Tables** (historical):
- `calendar_events` (93 rows) — Synced calendar events

**External Enrichment** (PRIMARY — always use live tools):
```
# Upcoming events
list_gcal_events(
  calendar_id="primary",
  time_min="[now]",
  time_max="[end of range]"
)

# Find free time
find_free_time(
  calendar_ids=["primary", "other@email.com"],
  time_min="...", time_max="..."
)

# Specific event details
fetch_gcal_event(calendar_id="primary", event_id="...")
```

### External Stakeholder Questions
**Triggers**: "external contact", "vendor", "partner", "works with externally"
**Supabase Table**: `stakeholder_relationships` (36 rows)
**Filter**: `{"is_internal": "eq.false"}`

### Credentials & Training Questions
**Triggers**: "certifications", "licenses", "training completed", "qualifications"
**Supabase Tables**:
1. `credentials` — Licenses, certifications, degrees
2. `training_records` (1 row) — Training completions
3. `achievements` (15 rows) — Recognitions

### Document & Knowledge Questions
**Triggers**: "Google Drive", "documents about", "drive files", "find document"
**Supabase Table** (indexed):
- `documents` (341 rows) — Synced Drive docs with full-text search

**External Enrichment** (RECOMMENDED — for live/current docs):
```
# Search Drive for documents
google_drive_search(
  api_query="fullText contains '[topic]'",
  semantic_query="[what you're looking for]"
)

# Search meeting transcripts folder
google_drive_search(
  api_query="'1BdEsYy1K8ujqjegPAfcxUrW4rDhortRd' in parents",
  semantic_query="[topic]"
)

# Read a specific Google Doc
google_drive_fetch(document_ids=["doc_id"])
```

### Policy & Protocol Questions
**Triggers**: "policy on", "protocol for", "our approach to", "guidelines", "SOP"
**Supabase Table**: `memory_l1_core`
**Filters**: `{"source_type": "in.(protocol,document)"}` or search by category

**External Enrichment** (optional):
- Drive: Search for protocol/policy documents
- Slack: Search for policy announcements or discussions

---

## Table Reference

See `references/schema.md` for complete schema documentation of all 55 tables.

### Quick Table Reference by Domain

| Domain | Key Tables | Rows |
|--------|------------|------|
| **Core Knowledge** | `memory_l1_core`, `memory_l2_context_intent`, `meeting_metadata` | 1,224 / 521 / — |
| **People** | `employees`, `entities_normalized`, `speaker_memory` | 23 / 1,009 / 112 |
| **Org Structure** | `departments`, `teams`, `employee_roles` | 6 / 6 / 24 |
| **Skills** | `employee_skills`, `expertise_areas`, `employee_tools` | 190 / 152 / 38 |
| **Projects** | `projects`, `project_raci` | 1,787 / 2,338 |
| **Responsibilities** | `responsibilities`, `institutional_knowledge` | 315 / 150 |
| **Email** | `email_digests`, `email_attachments` | 549 / 433 |
| **WhatsApp** | `whatsapp_groups`, `whatsapp_messages`, `whatsapp_ai_extractions` | 10 / 26,833 / 358 |
| **Integrations** | `documents`, `calendar_events`, `slack_messages` | 341 / 93 / — |

---

## Supabase Query Patterns

### Pattern 1: Recent meetings on a topic
```bash
python3 scripts/query_supabase.py memory_l1_core "source_file,Meeting_date,events,topics" '{"Meeting_date": "gte.2024-12-01"}' '{"order": "Meeting_date.desc", "limit": 10}'
```

### Pattern 2: Find project owner
```bash
# Step 1: Get project
python3 scripts/query_supabase.py projects "id,name,owner_employee_id,status" '{"name": "ilike.*academy*"}'
# Step 2: Get owner name
python3 scripts/query_supabase.py employees "preferred_name,job_title,email" '{"id": "eq.[owner_id]"}'
```

### Pattern 3: Get all responsibilities for a person
```bash
python3 scripts/query_supabase.py responsibilities "description,priority_order,is_primary" '{"employee_id": "eq.[emp_id]", "is_active": "eq.true"}' '{"order": "priority_order.asc"}'
```

### Pattern 4: Find go-to person for an area
```bash
python3 scripts/query_supabase.py expertise_areas "area,description,employee_id,backup_employee_id" '{"area": "ilike.*%topic%*", "is_go_to_person": "eq.true"}'
```

### Pattern 5: Search emails by topic (Supabase)
```bash
python3 scripts/query_supabase.py email_digests "subject,from_name,email_date,ai_summary,key_topics" '{"primary_category": "ilike.*clinical*"}' '{"order": "email_date.desc", "limit": 20}'
```

### Pattern 6: Get WhatsApp insights
```bash
python3 scripts/query_supabase.py whatsapp_ai_extractions "group_id,date_range_start,main_topics,decisions,follow_ups" '{}' '{"order": "date_range_end.desc", "limit": 10}'
```

### Pattern 7: RACI lookup
```bash
python3 scripts/query_supabase.py project_raci "employee_id,role,notes" '{"project_id": "eq.[project_id]"}'
```

### Pattern 8: Full-text search on documents
```bash
python3 scripts/query_supabase.py documents "name,content,modified_at" '{"content_tsv": "fts.medication"}' '{"limit": 10}'
```

---

## Cross-Source Query Patterns

### Pattern A: "What did we decide about X?" (Multi-Source)
```
1. Supabase: Query memory_l1_core for meetings with topic X
   → Get meeting dates, decisions, action items

2. Gmail: Search for email threads about X around those dates
   search_gmail_messages(q="[topic X] after:YYYY/MM/DD before:YYYY/MM/DD")
   → Get follow-up emails, implementation discussions

3. Slack: Search for Slack discussions about X
   slack_search_public(query="[topic X] after:YYYY-MM-DD")
   → Get informal discussions, updates

4. Synthesize: Combine KB decisions + email follow-ups + Slack updates
```

### Pattern B: "Who was in the meeting about X?" (Multi-Source)
```
1. Supabase: Query memory_l1_core for meeting, get metadata->participants
2. Calendar: list_gcal_events around that date with topic query
   → Get official attendee list from calendar
3. Supabase: Cross-reference with speaker_memory for actual speakers
4. Synthesize: Calendar attendees + actual speakers from transcript
```

### Pattern C: "What's the latest on project X?" (Multi-Source)
```
1. Supabase: Query projects table for status, owner
2. Supabase: Query memory_l1_core for recent meetings mentioning project
3. Gmail: Search for recent email threads about the project
   search_gmail_messages(q="[project name] newer_than:14d")
4. Slack: Search for recent Slack discussions
   slack_search_public(query="[project name] after:YYYY-MM-DD")
5. Drive: Search for related documents
   google_drive_search(api_query="fullText contains '[project name]'")
6. Synthesize: Status + recent meetings + email updates + Slack activity
```

### Pattern D: "What emails/messages about X?" (Live + Historical)
```
1. Supabase: Query email_digests for processed/historical emails
2. Gmail: Search for live/recent threads
   search_gmail_messages(q="[topic] newer_than:30d")
3. Slack: Search for related Slack messages
   slack_search_public(query="[topic]")
4. Supabase: Query whatsapp_ai_extractions for WhatsApp insights
5. Synthesize: Historical digests + live emails + Slack + WhatsApp
```

---

## Response Guidelines

1. **Always query first** — Don't rely on memory for work facts
2. **Use appropriate sources** — Route questions to the right Supabase tables AND external tools
3. **Enrich with external sources** — For meeting/project/communication questions, check Gmail, Calendar, Drive, and Slack
4. **Synthesize naturally** — Convert raw data from multiple sources into conversational answers
5. **Cite sources** — Mention the meeting, email thread, Slack channel, or document source
6. **Handle empty results** — If Supabase has no data, try external sources before reporting nothing found
7. **Multiple queries OK** — Complex questions may need 2-3 Supabase queries + external tool calls
8. **Join data manually** — Get IDs from one table, query another with those IDs
9. **Live vs historical** — For emails, calendar, Slack: prefer live tool queries for recent data; use Supabase for historical/processed data
10. **Ask before private search** — Use `slack_search_public` by default; only use `slack_search_public_and_private` with user consent