---
alfred_tags:
- taliaz/knowledge-base
- data-ingestion
- protocols
description: Forensic gap analysis between Taliaz's Supabase knowledge base and live
  data sources (Gmail, Google Drive transcripts, Slack). Identifies un-ingested content
  by comparing what exists in the KB against what's available in each source. Use
  when asked to "find gaps in the KB", "what's missing from the database", "audit
  KB coverage", "check what hasn't been ingested", "compare KB to Gmail/Drive/Slack",
  or any request to assess KB completeness. Triggers on "gap analysis", "missing data",
  "KB audit", "what's not ingested", "coverage check".
name: taliaz-kb-gap-audit
---

# Taliaz KB Forensic Gap Audit

Compares the Supabase KB against three live data sources to identify un-ingested content and produce a prioritized gap report.

## Quick Start

### Run Full Audit
```bash
python3 /home/ubuntu/skills/taliaz-kb-gap-audit/scripts/audit_all.py \
  --after 2026-01-01 --before 2026-02-22
```

### Run Individual Audits

**Gmail only:**
```bash
python3 /home/ubuntu/skills/taliaz-kb-gap-audit/scripts/audit_gmail.py \
  --after 2026-01-01 --before 2026-02-22
```

**Transcripts only:**
```bash
python3 /home/ubuntu/skills/taliaz-kb-gap-audit/scripts/audit_transcripts.py
```

**Slack only:**
```bash
python3 /home/ubuntu/skills/taliaz-kb-gap-audit/scripts/audit_slack.py \
  --after 2026-01-01 --before 2026-02-22
```

### Skip Specific Audits
```bash
python3 /home/ubuntu/skills/taliaz-kb-gap-audit/scripts/audit_all.py \
  --after 2026-01-01 --before 2026-02-22 --skip slack
```

## How Each Audit Works

### 1. Gmail Gap Audit (`audit_gmail.py`)

**Match strategy**: 1:1 comparison by `gmail_message_id`.

```
Gmail (via MCP)                    Supabase (email_digests)
─────────────────                  ─────────────────────────
message_id: abc123    ──match?──>  gmail_message_id: abc123
```

Steps:
1. Fetch all `gmail_message_id` values from `email_digests` table
2. Search Gmail via MCP for work emails in the date range
3. Filter to work-related emails (domain + keyword matching)
4. Compare: Gmail IDs not found in `email_digests` = **gaps**

**Parameters:**
- `--after YYYY-MM-DD` — Start date (required)
- `--before YYYY-MM-DD` — End date (required)
- `--all-emails` — Include non-work emails in gap count
- `--output PATH` — Save JSON report (default: `/tmp/gmail_gap_report.json`)

**Work domains**: taliazhealth.com, healthymind.co.il, plaud.ai, taliaz.com, clalit.org.il, maccabi4u.co.il, meuhedet.co.il, leumit.co.il

### 2. Transcript Gap Audit (`audit_transcripts.py`)

**Match strategy**: Filename comparison (exact + fuzzy) against `memory_l1_core.source_file`.

```
Google Drive (via rclone)          Supabase (memory_l1_core)
─────────────────────────          ─────────────────────────
filename: meeting.docx  ──match?──> source_file: meeting.docx
```

Steps:
1. Fetch all `source_file` values from `memory_l1_core`
2. List all transcript files from Google Drive folder (root + category subfolders)
3. For each Drive file: try exact match, then fuzzy match (threshold 0.75)
4. Unmatched files = **gaps**

**Parameters:**
- `--root-only` — Only check root folder, skip subfolders
- `--output PATH` — Save JSON report (default: `/tmp/transcript_gap_report.json`)

**Drive folder**: `Taliaz Meeting Transcripts` (root + 9 category subfolders + Documents, Oren, dekel, lifelogs)

**File types**: .docx, .md, .vtt, .txt, .pdf

### 3. Slack Gap Audit (`audit_slack.py`)

**Match strategy**: Heuristic date-level cross-reference (no 1:1 mapping exists).

```
Slack (via MCP)                    Supabase (memory_l1_core)
───────────────                    ─────────────────────────
significant msg on 2026-01-15  ──> any KB entry for 2026-01-15?
```

Steps:
1. Fetch KB entries with `Meeting_date` in the date range
2. Search Slack for significant messages using 15 work-related queries (Hebrew + English)
3. Filter to significant messages (decisions, action items, summaries, files)
4. Cross-reference: dates with Slack activity but no KB entries = **date gaps**

**Parameters:**
- `--after YYYY-MM-DD` — Start date (required)
- `--before YYYY-MM-DD` — End date (required)
- `--output PATH` — Save JSON report (default: `/tmp/slack_gap_report.json`)

**Significance keywords**: decision, action item, agreed, approved, deadline, summary, meeting notes, החלטה, סיכום, פגישה, משימה, עדכון

## Output Format

Each audit produces a JSON report with:

```json
{
  "audit_type": "gmail|transcripts|slack|full_forensic",
  "audit_date": "ISO timestamp",
  "date_range": {"after": "...", "before": "..."},
  "gap_analysis": {
    "matched": 100,
    "missing_count": 25,
    "coverage_pct": 80.0
  },
  "missing_emails|missing_transcripts|uncovered_messages": [...]
}
```

The full audit (`audit_all.py`) produces a combined report with a summary table and prioritized ingestion recommendations.

## After Finding Gaps

Once gaps are identified, use the appropriate ingestion skill:

| Gap Type | Ingestion Skill | Command |
|----------|----------------|---------|
| Missing emails | `taliaz-email-ingest` | `python3 .../ingest_emails.py <result_file>` |
| Missing transcripts | `taliaz-transcript-ingest` | `python3 .../ingest_transcripts.py --date YYYY-MM-DD` |
| Missing Slack content | `taliaz-doc-processor` | Manual processing of significant threads |

## Requirements

- Supabase credentials: `SUPABASE_URL`, `SUPABASE_KEY`
- Gmail MCP configured (for Gmail audit)
- rclone configured with Google Drive (for transcript audit)
- Slack MCP configured (for Slack audit)

## References

- `references/kb-schema.md` — Full KB table schemas, source type distribution, Drive folder structure