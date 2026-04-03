---
alfred_tags:
- taliaz/knowledge-base
- data-ingestion
- protocols
description: Perform a forensic deep-check to find gaps between the Taliaz Supabase
  knowledge base and available raw data sources (Gmail, Google Drive transcripts,
  Slack). Use this skill whenever asked to "find gaps in the KB", "check what's missing
  from the database", "what hasn't been processed", "audit the KB", "how out of date
  is the KB", "find unprocessed meetings", "what meetings are missing", "catch up
  the knowledge base", or any request to compare what's in Supabase against what exists
  in Gmail, transcripts, or Slack. This skill produces a structured gap report showing
  exactly what data exists but hasn't been ingested yet, organized by source and date.
name: kb-gap-forensics
relationships:
- confidence: 0.7
  context: Doc ingest supports KB gap analysis
  source: skills/user/kb-gap-forensics/SKILL.md
  target: skills/user/taliaz-doc-processor/SKILL.md
  type: related-to
- confidence: 0.65
  context: Email ingest feeds KB forensics
  source: skills/user/kb-gap-forensics/SKILL.md
  target: skills/user/taliaz-email-ingest/SKILL.md
  type: related-to
- confidence: 0.95
  context: Complementary KB gap forensics & audit
  source: skills/user/kb-gap-forensics/SKILL.md
  target: skills/user/taliaz-kb-gap-audit/SKILL.md
  type: related-to
- confidence: 0.95
  context: KB gap ingest & forensics pipeline
  source: skills/user/kb-gap-forensics/SKILL.md
  target: skills/user/taliaz-kb-gap-ingest/SKILL.md
  type: related-to
- confidence: 0.75
  context: Forensics supports KB queries
  source: skills/user/kb-gap-forensics/SKILL.md
  target: skills/user/taliaz-kb-query/SKILL.md
  type: supports
- confidence: 0.55
  context: Gap forensics for meeting protocols
  source: skills/user/kb-gap-forensics/SKILL.md
  target: skills/user/taliaz-meeting-protocol/SKILL.md
  type: related-to
- confidence: 0.8
  context: Forensics aids protocol auditing
  source: skills/user/kb-gap-forensics/SKILL.md
  target: skills/user/taliaz-protocol-auditor/SKILL.md
  type: related-to
- confidence: 0.7
  context: Identifies gaps for protocol writing
  source: skills/user/kb-gap-forensics/SKILL.md
  target: skills/user/taliaz-protocol-writer/SKILL.md
  type: supports
- confidence: 0.8
  context: Gap forensics enhances research
  source: skills/user/kb-gap-forensics/SKILL.md
  target: skills/user/taliaz-research/SKILL.md
  type: supports
- confidence: 0.7
  context: Transcript ingest for KB gaps
  source: skills/user/kb-gap-forensics/SKILL.md
  target: skills/user/taliaz-transcript-ingest/SKILL.md
  type: related-to
---

# KB Gap Forensics Skill

Systematically identifies data that exists in Gmail, Google Drive (transcripts), and Slack but has NOT been processed into the Taliaz Supabase knowledge base.

## Output

A **Gap Report** with:
- Last KB update date
- Total unprocessed items per source
- Prioritized list of missing documents/meetings
- Recommended ingestion order

---

## Phase 1: Establish KB Baseline

```sql
-- Last ingestion date per source
SELECT source_type, MAX(created_at) as last_ingested, COUNT(*) as total_records
FROM memory_l1_core GROUP BY source_type ORDER BY last_ingested DESC;

-- Last meeting processed
SELECT meeting_id, source_file, meeting_date, created_at
FROM meeting_metadata ORDER BY meeting_date DESC LIMIT 10;

-- Coverage by month
SELECT DATE_TRUNC('month', meeting_date) as month, COUNT(*) as meetings_processed
FROM meeting_metadata WHERE meeting_date > NOW() - INTERVAL '6 months'
GROUP BY month ORDER BY month DESC;
```

**Record:**
- `LAST_KB_DATE` = most recent meeting_date in meeting_metadata
- `LAST_INGESTION_DATE` = most recent created_at in memory_l1_core
- Set `SEARCH_START` = `LAST_KB_DATE` for all source scans below

---

## Phase 2: Scan Google Drive for Unprocessed Transcripts

```
google_drive_search(
  api_query="'1BdEsYy1K8ujqjegPAfcxUrW4rDhortRd' in parents and modifiedTime > 'SEARCH_START'",
  order_by="modifiedTime desc",
  page_size=50,
  semantic_query="meeting transcript"
)
```

For each file returned, check if source_file exists in `meeting_metadata`:
```sql
SELECT COUNT(*) FROM meeting_metadata WHERE source_file ILIKE '%[filename]%';
```
If COUNT = 0 → **GAP FOUND**

---

## Phase 3: Scan Gmail for Unprocessed Meeting Content

```
search_gmail_messages(q="subject:(summary OR סיכום OR minutes OR action items) after:SEARCH_START")
search_gmail_messages(q="(meeting OR פגישה OR sync) has:attachment after:SEARCH_START")
search_gmail_messages(q="from:(@taliazhealth.com OR @healthymind.co.il) after:SEARCH_START is:unread")
```

For each thread, check if it maps to an existing `memory_l1_core` record. If not → **GAP FOUND**

---

## Phase 4: Scan Slack for Unprocessed Discussions

```
slack_search_public(query="after:SEARCH_START in:general", sort="timestamp")
slack_search_public(query="after:SEARCH_START in:innovation-team", sort="timestamp")
slack_search_public(query="after:SEARCH_START in:clinical", sort="timestamp")
slack_search_public(query="decision OR החלטה after:SEARCH_START", sort="timestamp")
slack_search_public(query="action item OR משימה after:SEARCH_START", sort="timestamp")
```

Decision-heavy threads (3+ replies or pinned) with no KB match → **GAP FOUND**

---

## Phase 5: Cross-Reference Calendar Events

```
list_gcal_events(
  calendar_id="primary",
  time_min="SEARCH_START T00:00:00+02:00",
  time_max="NOW() T23:59:59+02:00",
  max_results=50
)
```

For each event with 2+ attendees, check `meeting_metadata` by date and title. No match → **GAP FOUND**

---

## Phase 6: Compile Gap Report

```markdown
# 📊 KB Gap Report
**Generated:** [TODAY]
**KB Last Updated:** [LAST_KB_DATE]
**Gap Period:** [LAST_KB_DATE] → [TODAY] ([N] days)

## Summary

| Source | Available | Processed | GAPS |
|--------|-----------|-----------|------|
| Google Drive Transcripts | N | N | **N** |
| Gmail Threads | N | N | **N** |
| Slack Discussions | N | N | **N** |
| Calendar Events | N | N | **N** |
| **TOTAL** | **N** | **N** | **N** |

## 🔴 Unprocessed Transcripts (Google Drive)
| # | Filename | Date | Priority |
|---|----------|------|----------|
| 1 | [filename] | [date] | 🔴 High |

## 🟡 Unprocessed Email Threads (Gmail)
| # | Subject | Date | From | Priority |
|---|---------|------|------|----------|

## 🟠 Unprocessed Slack Discussions
| # | Channel | Topic | Date | Replies | Priority |
|---|---------|-------|------|---------|----------|

## 📅 Calendar Events with No KB Match
| # | Event | Date | Attendees | Priority |
|---|-------|------|-----------|----------|

## ✅ Recommended Ingestion Order
1. [Item 1] — reason why top priority
2. [Item 2] — ...

## Next Step
To ingest all gaps, trigger the `taliaz-doc-processor` skill for each transcript,
or run a batch ingestion session starting with the highest-priority items above.
```

---

## Priority Scoring Guide

| Factor | Weight | How to assess |
|--------|--------|---------------|
| **Recency** | 3x | More recent = higher priority |
| **Decision density** | 3x | Contains decisions/action items = high |
| **Attendee count** | 2x | More attendees = more organizational knowledge |
| **Topic criticality** | 2x | UK, CQC, team restructuring = high |
| **Source type** | 1x | Transcript > Email > Slack |

**Auto-tag as 🔴 HIGH** if:
- Contains "UK", "CQC", "restructuring", or external partners
- Attendees include Dekel, Basel, Rami
- Has 3+ action items or decisions mentioned
- Is a transcript from a recurring leadership meeting

---

## References

- Google Drive Transcripts Folder ID: `1BdEsYy1K8ujqjegPAfcxUrW4rDhortRd`
- Use `taliaz-doc-processor` skill to ingest identified gaps
- Use `taliaz-kb-query` skill to verify ingestion after processing