---
alfred_tags:
- taliaz/knowledge-base
- data-ingestion
- protocols
description: Process documents to extract organizational knowledge and populate Taliaz's
  Supabase knowledge base. Use when given any document (PDF, Word, TXT, VTT, MD, Google
  Doc) to extract and store information. Triggers on requests like "process this document",
  "extract info from this file", "add this to the knowledge base", "update Taliaz
  KB from this doc", or when receiving work documents like meeting transcripts, protocols,
  summaries, or notes.
name: taliaz-doc-processor
---

# Taliaz Document Processor

Extracts structured information from documents and populates the Taliaz Supabase knowledge base.

## ⚠️ GSD FRAMEWORK (3 Required Components)

**Perfect meeting ingestion requires ALL THREE:**

### 1. Context Agent (Pre-Processing)
```
BEFORE extraction:
→ Parse file title for date → cross-reference with Gmail & Calendar
→ Query speaker_memory for known speakers
→ Query entities_normalized for entity resolution
→ Query prior meetings for continuity
→ Search Gmail for related threads (agendas, follow-ups)
→ Search Google Calendar for matching events (attendees, times)
→ Search Google Drive (Taliaz Meeting Transcripts folder) for related docs
→ Search Slack for pre/post-meeting discussions
→ Build CONTEXT.json with resolved names + external context
```

### 2. Verification Agent (Post-Processing)  
```
AFTER each INSERT:
→ Run verification query
→ If ❌ FAIL: Fix and re-verify
→ If ✅ PASS: Proceed to next table
```

### 3. Completeness Gate (Final Check)
```
BEFORE reporting success:
→ Run gate query on ALL required tables
→ If BLOCKED: Trigger revision loop (max 3 iterations)
→ If PASS: Mark as processed
→ NEVER skip the gate
```

**Workflow:**
```
DATE RESOLVE → CONTEXT (DB + Gmail + Calendar + Drive + Slack) → EXTRACT → VERIFY → GATE → DONE
                  ↑                                                          ↓
                  └──────────────── REVISION LOOP (if failed) ───────────────┘
```

## CRITICAL: Complete Table Checklist

**ALWAYS update ALL relevant tables.** Use this checklist for every document processed:

### For Transcripts/Meetings (MANDATORY - all 7+ tables):

| # | Table | What to Extract | Required? |
|---|-------|-----------------|-----------|
| 1 | `memory_l1_core` | Facts, entities, topics, events | ✅ ALWAYS |
| 2 | `memory_l2_context_intent` | Context, follow-ups, risks, decisions | ✅ ALWAYS |
| 3 | `meeting_metadata` | Title, date, time, language, location | ✅ ALWAYS |
| 4 | `entities_normalized` | NEW people, projects, processes, orgs discovered | ✅ ALWAYS check |
| 5 | `entity_occurrences` | Link ALL entities (new + existing) to meeting | ✅ ALWAYS |
| 6 | `speaker_memory` | ALL speakers in transcript (not just one!) | ✅ ALWAYS |
| 7 | `responsibilities` | New/changed responsibilities mentioned | ⚠️ If mentioned |
| 8 | `institutional_knowledge` | Critical knowledge areas discussed | ⚠️ If mentioned |

### For Protocols/SOPs:

| # | Table | What to Extract | Required? |
|---|-------|-----------------|-----------|
| 1 | `responsibilities` | Role-based responsibilities | ✅ ALWAYS |
| 2 | `institutional_knowledge` | Process knowledge | ✅ ALWAYS |
| 3 | `expertise_areas` | Who knows what | ⚠️ If mentioned |
| 4 | `entities_normalized` | New processes, tools | ✅ ALWAYS check |

### For Summaries/Notes:

| # | Table | What to Extract | Required? |
|---|-------|-----------------|-----------|
| 1 | `memory_l1_core` | Facts, entities (lower confidence for notes) | ✅ ALWAYS |
| 2 | `memory_l2_context_intent` | Context, follow-ups | ✅ ALWAYS |
| 3 | `entities_normalized` | New entities discovered | ✅ ALWAYS check |
| 4 | `entity_occurrences` | Link entities to source | ✅ ALWAYS |

---

## Pre-Processing: Context Agent (REQUIRED)

**IMPORTANT:** Before extracting data, gather organizational context to enable accurate entity resolution.

### Context Agent Workflow

**Run BEFORE any extraction. This is Step 0.**

```
CONTEXT AGENT SEQUENCE:
1. SCAN document → extract raw names, projects, topics
2. DETERMINE DATE → parse file title + cross-reference Gmail & Calendar
3. QUERY speaker_memory → resolve known speakers
4. QUERY entities_normalized → resolve known entities  
5. QUERY employees → match to employee records
6. QUERY prior meetings → find continuity
7. SEARCH Gmail → find related email threads around the meeting date
8. SEARCH Google Calendar → find matching calendar events
9. SEARCH Google Drive → find related transcripts in Taliaz Meeting Transcripts folder
10. SEARCH Slack → find related discussions in relevant channels
11. BUILD context.json → structured resolution map with all sources
12. PROCEED to extraction with context loaded
```

### Step 0a: Quick Scan & Raw Extraction

```sql
-- Get known speakers for resolution
SELECT speaker_name, canonical_name, role_hint 
FROM speaker_memory 
ORDER BY updated_at DESC;

-- Get known entities for resolution
SELECT canonical_name, aliases, entity_type, inferred_role
FROM entities_normalized
WHERE entity_type IN ('person', 'project', 'organization');

-- Get employees for name matching
SELECT id, preferred_name, full_legal_name, job_title, work_email
FROM employees WHERE employment_status = 'active';
```

### Step 0a-bis: Date Determination (REQUIRED)

**The meeting date is critical for all downstream processing. Use multiple sources to determine it accurately.**

```
DATE DETERMINATION SEQUENCE:
1. PARSE file title → look for date patterns (YYYY-MM-DD, DD.MM.YYYY, month names, etc.)
2. CHECK file metadata → creation date, modification date
3. SEARCH Gmail → emails around candidate date with matching participants/topics
4. SEARCH Google Calendar → calendar events matching content/participants
5. CROSS-REFERENCE → confirm date from at least 2 sources when possible
6. SET meeting_date with confidence level
```

**File Title Parsing:**
- Common patterns: `Meeting_2025-01-15.vtt`, `Team Sync Jan 15`, `20250115_standup`
- Hebrew date formats: `15.1.25`, `15/01/2025`
- Descriptive: `Q4 Review December` → search calendar for Q4 review meetings

**Gmail Cross-Reference:**
```
search_gmail_messages(
  q="subject:([meeting title or key topic]) after:YYYY/MM/DD before:YYYY/MM/DD"
)
```
Look for:
- Meeting invitations or calendar notifications
- Pre-meeting emails with agendas
- Post-meeting follow-ups or summaries
- Participant names from the transcript in email threads

**Google Calendar Cross-Reference:**
```
list_gcal_events(
  calendar_id="primary",
  time_min="YYYY-MM-DDT00:00:00+02:00",  -- 2 days before candidate date
  time_max="YYYY-MM-DDT23:59:59+02:00",  -- 2 days after candidate date
  query="[meeting title or key participants]"
)
```
Look for:
- Events matching the meeting title
- Events with matching attendees
- Duration alignment with transcript length
- Extract exact start/end times for meeting_metadata

**Date Confidence Levels:**
| Sources Confirming | Confidence | Action |
|-------------------|------------|--------|
| File title + Calendar event | 0.95 | Use confirmed date |
| File title + Email thread | 0.90 | Use confirmed date |
| Calendar event only | 0.85 | Use with note |
| File title only | 0.70 | Use with note, flag for review |
| None found | 0.30 | Ask user or flag as unknown |

### Step 0b: External Context Sources (REQUIRED)

**Query ALL available external sources to build comprehensive context.**

#### Gmail Context
```
search_gmail_messages(
  q="[key topics or participant names] after:YYYY/MM/DD before:YYYY/MM/DD"
)
```
Extract from email threads:
- **Pre-meeting agendas** → confirms topics, adds context to discussions
- **Action item follow-ups** → links decisions to outcomes
- **Participant lists** → helps resolve speakers
- **Attachments mentioned** → links to related documents

If a relevant thread is found, use `read_gmail_thread(thread_id=...)` to get full context.

#### Google Calendar Context
```
list_gcal_events(
  calendar_id="primary",
  time_min="[meeting_date - 1 day]",
  time_max="[meeting_date + 1 day]",
  query="[meeting topic or title]"
)
```
Extract from calendar events:
- **Exact meeting time** → for meeting_metadata start_time/end_time
- **Attendee list** → for speaker resolution
- **Meeting description/agenda** → for context enrichment
- **Recurring meeting info** → links to meeting series
- **Video call links** → confirms virtual meeting format

#### Google Drive Context (Taliaz Meeting Transcripts Folder)
```
google_drive_search(
  api_query="'1BdEsYy1K8ujqjegPAfcxUrW4rDhortRd' in parents",
  semantic_query="[key topics from document]"
)
```
Extract from related transcripts:
- **Prior meetings on same topics** → continuity tracking
- **Decisions referenced** → links to original context
- **Participant history** → speaker identification patterns

Also search broader Drive for related documents:
```
google_drive_search(
  api_query="fullText contains '[key topic or project name]'",
  semantic_query="[relevant context query]"
)
```

#### Slack Context
```
slack_search_public(
  query="[key topics or project names] after:YYYY-MM-DD before:YYYY-MM-DD"
)
```
Extract from Slack discussions:
- **Pre/post-meeting discussions** → additional context not in transcript
- **Shared links or documents** → related resources
- **Decision follow-ups** → outcome tracking
- **Channel context** → which teams are involved

For deeper context on specific threads:
```
slack_read_thread(channel_id="...", message_ts="...")
```

**Slack Channel Hints:** Search relevant channels based on meeting content:
- Product/R&D topics → search engineering/product channels
- Clinical topics → search clinical channels
- Business/strategy → search leadership channels

### Step 0c: Build CONTEXT.json

Before extraction, build a resolution map enriched with all sources:

```json
{
  "meeting_id": "generated-uuid",
  "source_file": "filename.vtt",
  "date_determination": {
    "meeting_date": "YYYY-MM-DD",
    "confidence": 0.95,
    "sources": {
      "file_title": "date extracted from filename",
      "calendar_event": "event_id or null",
      "email_thread": "thread_id or null"
    },
    "start_time": "HH:MM (from calendar if available)",
    "end_time": "HH:MM (from calendar if available)"
  },
  "resolved_speakers": {
    "SPEAKER_00": {"canonical": "Rami Khouri", "employee_id": "uuid", "role": "CMIO"},
    "SPEAKER_01": {"canonical": "Stav Zamir", "employee_id": "uuid", "role": "Clinical Lead"}
  },
  "known_entities": {
    "Academy": {"type": "project", "entity_id": "uuid"},
    "Maccabi": {"type": "organization", "entity_id": "uuid"}
  },
  "external_context": {
    "gmail": {
      "related_threads": ["thread_id_1", "thread_id_2"],
      "agenda_found": true,
      "key_context": "Pre-meeting email mentioned X, Y, Z"
    },
    "calendar": {
      "event_id": "calendar_event_id",
      "attendees": ["email1@taliaz.com", "email2@taliaz.com"],
      "description": "Meeting agenda from calendar"
    },
    "google_drive": {
      "related_transcripts": ["file_id_1", "file_id_2"],
      "related_documents": ["doc_id_1"]
    },
    "slack": {
      "related_messages": ["channel_id:message_ts"],
      "key_context": "Post-meeting discussion in #channel about topic X"
    }
  },
  "related_meetings": ["prior-meeting-id-1", "prior-meeting-id-2"],
  "unresolved": ["NewPerson", "UnknownProject"]
}
```

### Step 0d: Search Prior Context (Supabase + Drive)

```sql
-- Find related prior meetings (same participants or topics)
SELECT meeting_id, source_file, Meeting_date, 
       metadata->'participants' as participants
FROM memory_l1_core
WHERE Meeting_date >= CURRENT_DATE - INTERVAL '30 days'
ORDER BY Meeting_date DESC
LIMIT 10;
```

Also search Google Drive transcripts folder:
```
google_drive_search(
  api_query="'1BdEsYy1K8ujqjegPAfcxUrW4rDhortRd' in parents",
  semantic_query="[key topics from document]"
)
```

### When to Gather Context

| Document Type | Context Required? | Why | External Sources |
|---------------|-------------------|-----|------------------|
| **transcript** | ✅ MANDATORY | Resolve speaker labels to real names | Gmail + Calendar + Drive + Slack |
| **notes** | ✅ MANDATORY | Clarify ambiguous references | Gmail + Drive + Slack |
| **unstructured** | ✅ MANDATORY | Resolve entity references | Gmail + Drive |
| **protocol** | ⚠️ If ambiguous | Only if references unclear | Drive + Slack |
| **summary** | ⚠️ If external | If from external source | Gmail + Drive |

### External Source Priority

| Source | Best For | When to Use |
|--------|----------|-------------|
| **Google Calendar** | Date/time confirmation, attendee lists | ✅ ALWAYS for transcripts |
| **Gmail** | Agendas, follow-ups, additional participants | ✅ ALWAYS for transcripts |
| **Google Drive** | Related transcripts, continuity | ✅ ALWAYS for any meeting content |
| **Slack** | Pre/post-meeting discussions, informal context | ⚠️ When topics need additional context |

---

## Processing Workflow

### Step 1: Extract Text

- **PDF**: Use Desktop Commander read_file or pdf skill
- **DOCX**: Use docx skill or pandoc  
- **Google Docs**: Use google_drive_fetch tool with document ID
- **VTT**: Parse directly, preserve speaker/timestamp structure
- **TXT/MD**: Read directly

### Step 2: Gather Context (for unstructured docs)

Use the taliaz-research skill workflow + external sources:

```
1. Determine date from file title + Gmail + Calendar (see Step 0a-bis)

2. Search transcripts folder for related discussions:
   google_drive_search(
     api_query="'1BdEsYy1K8ujqjegPAfcxUrW4rDhortRd' in parents",
     semantic_query="[key topics from document]"
   )

3. Search Gmail for related email threads:
   search_gmail_messages(
     q="[participant names or topics] after:YYYY/MM/DD before:YYYY/MM/DD"
   )

4. Search Calendar for matching events:
   list_gcal_events(
     time_min="[date-1d]", time_max="[date+1d]",
     query="[meeting title or participants]"
   )

5. Search Slack for related discussions:
   slack_search_public(
     query="[topics or project names] after:YYYY-MM-DD before:YYYY-MM-DD"
   )

6. For people mentioned, check:
   - Supabase employees table
   - entities_normalized table
   - references/taliaz-people.md
   - Calendar attendee lists
   - Email To/From/CC fields

7. For projects/topics, check:
   - Prior meeting transcripts
   - Supabase memory_l1_core for related facts
   - Slack channels for project discussions
   - Gmail for project-related threads
```

### Step 3: Classify Document Type

Analyze content for type indicators:
- Speaker patterns: SPEAKER_00:, [Name]:, timestamps → transcript
- Protocol markers: "Step 1", "Procedure", "Responsibility" → protocol
- Summary markers: "Key decisions", "Action items", "Summary" → summary
- Informal/incomplete → notes

### Step 4: Extract & Insert to PRIMARY Tables

#### 4a. memory_l1_core (transcripts/summaries/notes)

```json
{
  "meeting_id": "unique-id-from-filename-or-generated",
  "source_file": "original-filename.ext",
  "metadata": {
    "title": "inferred or extracted title",
    "date": "YYYY-MM-DD (from date determination - Step 0a-bis)",
    "type": "transcript|summary",
    "language": "he|en|ar|mixed",
    "duration_minutes": 50,
    "participants": ["resolved full names from context + calendar attendees"],
    "related_meetings": ["prior meeting IDs from context search"],
    "date_source": "calendar|email|file_title|manual",
    "date_confidence": 0.95,
    "calendar_event_id": "optional - from calendar cross-reference",
    "related_email_threads": ["optional - gmail thread IDs"]
  },
  "entities": [
    {"name": "Canonical Name (resolved)", "type": "person", "context": "quote"}
  ],
  "topics": [
    {"topic": "topic with org context", "relevance": 0.8, "keywords": ["..."]}
  ],
  "events": [
    {"event": "description", "date": "YYYY-MM", "participants": ["names"]}
  ],
  "facts": [
    {"fact": "statement", "confidence": 0.9, "source_quote": "..."}
  ]
}
```

#### 4b. memory_l2_context_intent (transcripts/summaries)

```json
{
  "meeting_id": "same-as-l1",
  "related_projects": ["linked to known projects from context"],
  "related_people": ["resolved names"],
  "meeting_type": "planning|status|decision|brainstorm|1on1",
  "primary_intent": "main purpose (informed by prior meetings)",
  "secondary_intents": ["other purposes"],
  "follow_ups": [
    {"action": "task", "owner": "resolved name", "deadline": "date", "status": "pending"}
  ],
  "risks": ["identified risks"],
  "constraints": ["limitations mentioned"],
  "confidence": 0.85,
  "l2_json": { "key_decisions": [], "tensions_identified": [], "strategic_context": "" }
}
```

#### 4c. meeting_metadata (transcripts - REQUIRED)

```sql
INSERT INTO meeting_metadata (meeting_id, title, date, start_time, end_time, language)
VALUES (
  '[uuid from memory_l1_core]',
  'Meeting Title',
  'YYYY-MM-DD',
  'HH:MM:SS',
  'HH:MM:SS',
  'hebrew|english|arabic'
);
```

### Step 5: Entity Resolution & Creation

**CRITICAL: This is a TWO-PART step!**

#### 5a. Check for EXISTING entities first

```sql
-- Check if entity already exists
SELECT id, canonical_name, aliases FROM entities_normalized 
WHERE canonical_name ILIKE '%name%' OR '%name%' = ANY(aliases);

-- Check employees table
SELECT id, full_legal_name, preferred_name FROM employees 
WHERE full_legal_name ILIKE '%name%' OR preferred_name ILIKE '%name%';
```

#### 5b. Create NEW entities for anything not found

Insert new people, projects, processes, organizations discovered:

```sql
INSERT INTO entities_normalized (entity_type, canonical_name, aliases, description, inferred_role, confidence)
VALUES 
  ('person', 'Full Name', ARRAY['nickname', 'hebrew_name'], 'Description', 'Role', 0.85),
  ('project', 'Project Name', ARRAY['aliases'], 'Description', NULL, 0.9),
  ('process', 'Process Name', ARRAY['aliases'], 'Description', NULL, 0.85),
  ('organization', 'Org Name', ARRAY['aliases'], 'Description', NULL, 0.9);
```

#### 5c. Create entity_occurrences for ALL entities (REQUIRED!)

**Link EVERY entity mentioned to the meeting - both new AND existing:**

```sql
INSERT INTO entity_occurrences (entity_id, meeting_id, raw_name, entity_type, context_snippet)
VALUES 
  ('[entity_uuid]', '[meeting_id_string]', 'name as mentioned', 'person', 'Brief context of mention');
```

### Step 6: Speaker Memory (ALL Speakers!)

**CRITICAL: Process EVERY speaker in the transcript, not just one!**

```sql
INSERT INTO speaker_memory (
  speaker_name,
  canonical_name,
  role_hint,
  languages_distribution,
  style_markers,
  domain_markers,
  topic_profile,
  files_appeared_in
) VALUES (
  'Speaker Label from Transcript',
  'Canonical Full Name',
  'Role/Title',
  '{"hebrew": 90, "english": 10}'::jsonb,
  '{"directive": true, "asks_questions": true}'::jsonb,
  '{"areas": ["domain1", "domain2"]}'::jsonb,
  '{"frequent_topics": ["topic1", "topic2"]}'::jsonb,
  '["meeting-id-1"]'::jsonb
)
ON CONFLICT (speaker_name) DO UPDATE SET
  files_appeared_in = speaker_memory.files_appeared_in || '["new-meeting-id"]'::jsonb,
  updated_at = now();
```

### Step 7: Extract Organizational Changes

#### 7a. New/Changed Responsibilities

If the meeting discusses role changes, new assignments, or responsibility transfers:

```sql
-- First get employee_id
SELECT id FROM employees WHERE preferred_name ILIKE '%name%';

-- Then insert responsibility
INSERT INTO responsibilities (employee_id, description, priority_order, is_primary, is_active)
VALUES ('[employee_uuid]', 'New responsibility description', 2, false, true);
```

#### 7b. Institutional Knowledge

If critical knowledge areas are discussed (processes, protocols, expertise):

```sql
INSERT INTO institutional_knowledge (employee_id, knowledge_area, description, criticality, transfer_status)
VALUES ('[employee_uuid]', 'Knowledge Area', 'Description of knowledge', 'high', 'in_progress');
```

### Step 8: Conflict Detection

For new data: insert directly.
For conflicts with existing data: insert to pending_review table.

```sql
INSERT INTO pending_review (source_file, target_table, extracted_data, conflict_reason, status)
VALUES ('filename', 'target_table', '{"data": "..."}'::jsonb, 'Reason for conflict', 'pending');
```

---

## POST-PROCESSING VERIFICATION (GSD-Style)

**⚠️ MANDATORY: Run verification queries after EVERY insert. Do not skip.**

### Step 9: Verification Queries (REQUIRED)

After completing all inserts, run this verification query to confirm success:

```sql
-- VERIFICATION QUERY: Run after processing each document
-- Replace [meeting_id] with the actual meeting_id used

WITH verification AS (
  SELECT 
    '[meeting_id]' as meeting_id,
    (SELECT COUNT(*) FROM memory_l1_core WHERE meeting_id = '[meeting_id]') as l1_count,
    (SELECT COUNT(*) FROM memory_l2_context_intent WHERE meeting_id = '[meeting_id]') as l2_count,
    (SELECT COUNT(*) FROM meeting_metadata WHERE meeting_id = '[meeting_id]') as metadata_count,
    (SELECT COUNT(*) FROM entity_occurrences WHERE meeting_id = '[meeting_id]') as entity_occ_count,
    (SELECT COUNT(DISTINCT speaker_name) FROM speaker_memory 
     WHERE files_appeared_in::text LIKE '%[meeting_id]%') as speakers_count
)
SELECT 
  meeting_id,
  CASE WHEN l1_count > 0 THEN '✅' ELSE '❌' END as l1_core,
  CASE WHEN l2_count > 0 THEN '✅' ELSE '❌' END as l2_context,
  CASE WHEN metadata_count > 0 THEN '✅' ELSE '❌' END as metadata,
  entity_occ_count as entity_occurrences,
  speakers_count as speakers,
  CASE 
    WHEN l1_count > 0 AND l2_count > 0 AND metadata_count > 0 
         AND entity_occ_count > 0 AND speakers_count > 0 
    THEN '✅ COMPLETE'
    ELSE '❌ INCOMPLETE - check missing tables'
  END as status
FROM verification;
```

### Verification Decision Tree

```
IF status = '✅ COMPLETE':
  → Report success with counts
  → Proceed to next document

IF status = '❌ INCOMPLETE':
  → Identify which table has 0 count
  → Re-run the INSERT for that table
  → Run verification again
  → Do NOT proceed until all tables show ✅
```

### Quick Verification Checks

**After memory_l1_core INSERT:**
```sql
SELECT meeting_id, source_file, jsonb_array_length(COALESCE(entities, '[]'::jsonb)) as entity_count,
       jsonb_array_length(COALESCE(topics, '[]'::jsonb)) as topic_count
FROM memory_l1_core WHERE meeting_id = '[meeting_id]';
-- Expected: 1 row with entity_count > 0, topic_count > 0
```

**After entity_occurrences INSERT:**
```sql
SELECT COUNT(*) as occurrence_count, COUNT(DISTINCT entity_id) as unique_entities
FROM entity_occurrences WHERE meeting_id = '[meeting_id]';
-- Expected: occurrence_count >= unique_entities, both > 0
```

**After speaker_memory INSERT/UPDATE:**
```sql
SELECT speaker_name, canonical_name, 
       jsonb_array_length(files_appeared_in) as appearance_count
FROM speaker_memory 
WHERE files_appeared_in::text LIKE '%[meeting_id]%';
-- Expected: Row count should match number of speakers in transcript
```

### Verification Report Template

After processing, output a verification report:

```
## Processing Complete: [filename]

| Table | Status | Count | Notes |
|-------|--------|-------|-------|
| memory_l1_core | ✅/❌ | N | entities: X, topics: Y |
| memory_l2_context_intent | ✅/❌ | N | follow_ups: X |
| meeting_metadata | ✅/❌ | N | date: YYYY-MM-DD |
| entities_normalized | ✅/❌ | N new | (existing: M) |
| entity_occurrences | ✅/❌ | N | linked to M entities |
| speaker_memory | ✅/❌ | N speakers | [list names] |
| responsibilities | ✅/❌ | N | (if applicable) |
| institutional_knowledge | ✅/❌ | N | (if applicable) |

**Overall Status**: ✅ VERIFIED / ❌ FAILED - [reason]
```

### Failure Recovery

If verification fails:

1. **Missing L1/L2**: Re-extract from document, re-insert
2. **Missing entity_occurrences**: Query entities from L1, create occurrences
3. **Missing speakers**: Re-parse transcript for speaker labels
4. **FK constraint errors**: Check entity_id/employee_id exists first

```sql
-- Debug: Find orphaned references
SELECT 'entity_occurrences' as table_name, entity_id 
FROM entity_occurrences eo
WHERE NOT EXISTS (SELECT 1 FROM entities_normalized WHERE id = eo.entity_id)
  AND meeting_id = '[meeting_id]';
```

### Completeness Gate (REQUIRED)

**A document is NOT "processed" until ALL of these pass:**

```sql
-- COMPLETENESS GATE QUERY
-- Returns 'PASS' only if all required tables have data

SELECT 
  CASE 
    WHEN l1 > 0 AND l2 > 0 AND meta > 0 AND occ > 0 AND spk > 0 
    THEN 'PASS ✅ - Document fully processed'
    ELSE 'BLOCKED ❌ - Missing: ' || 
      CASE WHEN l1 = 0 THEN 'L1 ' ELSE '' END ||
      CASE WHEN l2 = 0 THEN 'L2 ' ELSE '' END ||
      CASE WHEN meta = 0 THEN 'metadata ' ELSE '' END ||
      CASE WHEN occ = 0 THEN 'entity_occurrences ' ELSE '' END ||
      CASE WHEN spk = 0 THEN 'speakers ' ELSE '' END
  END as gate_status
FROM (
  SELECT 
    (SELECT COUNT(*) FROM memory_l1_core WHERE meeting_id = '[meeting_id]') as l1,
    (SELECT COUNT(*) FROM memory_l2_context_intent WHERE meeting_id = '[meeting_id]') as l2,
    (SELECT COUNT(*) FROM meeting_metadata WHERE meeting_id = '[meeting_id]') as meta,
    (SELECT COUNT(*) FROM entity_occurrences WHERE meeting_id = '[meeting_id]') as occ,
    (SELECT COUNT(*) FROM speaker_memory WHERE files_appeared_in::text LIKE '%[meeting_id]%') as spk
) counts;
```

**Gate Rules:**
- If `BLOCKED` → Do NOT report success to user
- If `BLOCKED` → Trigger revision loop (re-extract missing data)
- If `PASS` → Mark document as processed, report success
- Never skip the gate check

### Revision Loop

When verification fails, execute this loop:

```
WHILE gate_status = 'BLOCKED':
  1. Identify missing table(s) from gate query
  2. Re-read relevant section of document
  3. Re-extract data for missing table
  4. INSERT missing data
  5. Run gate query again
  
MAX_ITERATIONS = 3
IF iterations > 3: 
  → Flag for manual review in pending_review table
  → Report partial success with list of failures
```

---

## Common Mistakes to Avoid

| Mistake | Why It Happens | How to Prevent |
|---------|----------------|----------------|
| Missing `entity_occurrences` | Not documented as separate step | Always link entities after creating them |
| Missing `meeting_metadata` | Table not in original workflow | Add immediately after L1 insert |
| Only one speaker in `speaker_memory` | Stop after first speaker | Count speakers, process ALL |
| Missing `responsibilities` | Not tied to transcript processing | Check for role/assignment discussions |
| Missing `institutional_knowledge` | Not tied to transcript processing | Check for process/knowledge discussions |
| Not checking existing entities | Insert duplicates | ALWAYS query before inserting |

---

## Known Taliaz Entities

See `references/taliaz-people.md` for complete directory with roles and aliases.

### Key People Summary

**Leadership:** Dekel (CEO/Chief Scientist), Oren (CFO), Alex (Strategy), Adiel (CBO), Roy (COO)

**Medical/Innovation:** Rami (CMO/Innovation), Stav (Clinical Expert), Rivi (UX/Solution Design), Ohad (AI/Tech)

**R&D/Product:** Shachar (VP R&D), Shmulik (Engineer), Lidar (IT), Yael (PM), Lee (Designer)

**Clinical Ops:** Basel (Director), Shira (Clinic Manager), Ori (Training/CS), Rana (Admin/Patient XP)

**Psychiatrists:** Elias (Clinical Director), Noa, Elinor (Eleanor) Khateeb, Ilya, Saeed

**Case Managers:** Basem, Stav, Rivi, Ori

### Projects
- UK Expansion / CQC Compliance
- Academy (psychiatric training)
- Human-Like Memory System
- HealthyMind Virtual Clinic
- Children's Clinic (Maccabi)
- Staff Compensation Restructuring
- Maccabi Tele-psychiatry Collaboration

---

## References

- `references/taliaz-people.md` - Complete people directory with roles and aliases
- `references/supabase-schema.md` - Table schemas and field descriptions
- Use `taliaz-research` skill for organizational context before processing

## External Tools Used

| Tool | Purpose | Key Parameters |
|------|---------|----------------|
| `search_gmail_messages` | Find related emails, agendas, follow-ups | `q` with date range + topics |
| `read_gmail_thread` | Deep-read relevant email threads | `thread_id` from search |
| `list_gcal_events` | Find matching calendar events, attendees, times | `time_min`, `time_max`, `query` |
| `google_drive_search` | Search Taliaz Meeting Transcripts folder | Folder ID: `1BdEsYy1K8ujqjegPAfcxUrW4rDhortRd` |
| `google_drive_fetch` | Read related Google Docs | `document_ids` |
| `slack_search_public` | Find related Slack discussions | `query` with date modifiers |
| `slack_read_thread` | Deep-read relevant Slack threads | `channel_id`, `message_ts` |