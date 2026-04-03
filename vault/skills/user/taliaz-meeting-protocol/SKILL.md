---
alfred_tags:
- taliaz/knowledge-base
- data-ingestion
- protocols
description: Generate structured meeting protocols from Taliaz/HealthyMind transcripts.
  Recognizes if a transcript is a Taliaz work meeting, extracts the meeting name and
  date, gathers organizational context from the KB, and produces a formal 9-section
  protocol document. Use when given a transcript and asked to "create a protocol",
  "write meeting minutes", "generate meeting summary", "protocol from transcript",
  or "process this meeting". Supports .txt, .md, .vtt, and .docx files.
name: taliaz-meeting-protocol
---

# Taliaz Meeting Protocol Generator

Transforms raw meeting transcripts into structured, professional protocols with 9 standardized sections. Handles the full pipeline: recognition, metadata extraction, speaker resolution, org context enrichment, and AI-powered protocol generation.

## Pipeline Overview

```
INPUT (transcript file)
  → Step 1: READ transcript (.txt, .md, .vtt, .docx)
  → Step 2: RECOGNIZE if Taliaz meeting (confidence scoring)
  → Step 3: EXTRACT metadata (title, date, project from filename + content)
  → Step 4: RESOLVE speakers (map labels to real names via aliases)
  → Step 5: GATHER org context (Supabase KB + external sources)
  → Step 6: GENERATE protocol via AI (OpenAI or Gemini)
  → Step 7: RENDER using template
OUTPUT (formatted protocol .md file)
```

## Quick Start

### Generate Protocol from File

```bash
python3 /home/ubuntu/skills/taliaz-meeting-protocol/scripts/generate_protocol.py <transcript_path>
```

### Analyze Only (Dry Run)

```bash
python3 /home/ubuntu/skills/taliaz-meeting-protocol/scripts/generate_protocol.py <transcript_path> --dry-run
```

### Custom Output Path

```bash
python3 /home/ubuntu/skills/taliaz-meeting-protocol/scripts/generate_protocol.py <transcript_path> -o /path/to/output.md
```

### Force Non-Taliaz Transcript

```bash
python3 /home/ubuntu/skills/taliaz-meeting-protocol/scripts/generate_protocol.py <transcript_path> --force
```

## When to Use This Skill

| Trigger | Action |
|---------|--------|
| "Create a protocol from this transcript" | Run full pipeline |
| "Generate meeting minutes" | Run full pipeline |
| "Is this a Taliaz meeting?" | Run with `--dry-run` |
| "Process this meeting transcript" | Run full pipeline |
| "Write a protocol for yesterday's meeting" | Fetch transcript from Drive first, then run pipeline |

## Step-by-Step Workflow (When Script Alone Is Not Enough)

The script handles most cases automatically. Use this manual workflow when you need to enrich context beyond what the script provides (e.g., cross-referencing calendar, Gmail, Slack).

### Step 1: Read the Transcript

The script supports `.txt`, `.md`, `.vtt`, and `.docx`. For Google Docs, first fetch via Drive:

```bash
rclone copy "manus_google_drive:Taliaz Meeting Transcripts/<filename>" /tmp/ --config /home/ubuntu/.gdrive-rclone.ini
```

### Step 2: Recognition (Automatic)

The script scores the transcript against Taliaz signals. See `references/taliaz_signals.md` for the full signal list and scoring logic.

| Confidence | Meaning |
|-----------|--------|
| ≥ 0.90 | Definitely Taliaz — proceed |
| 0.50–0.89 | Likely Taliaz — proceed with note |
| < 0.50 | Probably not Taliaz — ask user or use `--force` |

### Step 3: Metadata Extraction (Automatic + Manual Enrichment)

The script extracts date and title from the filename. For better accuracy, cross-reference with Google Calendar:

```
list_gcal_events(
  calendar_id="primary",
  time_min="YYYY-MM-DDT00:00:00+02:00",
  time_max="YYYY-MM-DDT23:59:59+02:00",
  query="[meeting title or participants]"
)
```

Use `meeting-classifier-v2` for recurring meeting identification — read its `references/meeting_registry.md` for the full registry.

### Step 4: Speaker Resolution (Automatic + KB Enrichment)

The script maps known aliases to canonical names. For unresolved SPEAKER_XX labels, query the KB:

```sql
SELECT speaker_name, canonical_name, role_hint FROM speaker_memory ORDER BY updated_at DESC;
```

### Step 5: Organizational Context (Automatic + External Sources)

The script queries Supabase for employee records and prior meetings. For richer protocols, also query:

**Gmail** — find agendas and follow-ups:
```
search_gmail_messages(q="subject:([meeting topic]) after:YYYY/MM/DD before:YYYY/MM/DD")
```

**Slack** — find pre/post-meeting discussions:
```
slack_search_public(query="[topic] after:YYYY-MM-DD")
```

**Google Drive** — find related transcripts:
```
rclone ls "manus_google_drive:Taliaz Meeting Transcripts/" --config /home/ubuntu/.gdrive-rclone.ini | grep "[topic]"
```

### Step 6: AI Generation (Automatic)

The script uses OpenAI (gpt-4o-mini) or Gemini (gemini-2.5-flash) to produce structured protocol content. The AI prompt is in `references/ai_prompt.md`.

### Step 7: Render (Automatic)

The protocol is rendered using `templates/protocol_template.md` with 9 sections:

1. Meeting Title
2. Date & Project
3. Attendees (with roles)
4. Background & Purpose
5. Agenda
6. Key Points Discussed
7. Decisions Made
8. Open Questions & Unresolved Issues
9. Next Steps / Action Items + Conclusion

## Protocol Sections Reference

| Section | What to Include | Source |
|---------|----------------|--------|
| **Attendees** | Full names with titles/roles | Speaker resolution + KB employees table |
| **Background** | Why the meeting was convened, organizational context | AI analysis + prior meetings |
| **Decisions** | Only committed decisions with clear ownership | AI extraction from transcript |
| **Open Questions** | Unresolved items grouped by theme | AI extraction |
| **Action Items** | Specific tasks with owner and description | AI extraction, grouped by person |

## Post-Protocol Actions (Optional)

After generating the protocol, consider:

1. **Ingest to KB**: Use `taliaz-doc-processor` to add the protocol to Supabase
2. **Distribute**: Share via Gmail or Slack to attendees
3. **Track action items**: Add follow-ups to Monday.com or calendar

## File Structure

```
taliaz-meeting-protocol/
├── SKILL.md                          (this file)
├── scripts/
│   └── generate_protocol.py          (main pipeline script)
├── references/
│   ├── taliaz_signals.md             (recognition signals & scoring)
│   └── ai_prompt.md                  (AI prompt templates)
└── templates/
    └── protocol_template.md          (output template with 9 sections)
```

## Requirements

| Dependency | Purpose | Required? |
|-----------|---------|----------|
| `OPENAI_API_KEY` | Protocol generation via GPT-4o-mini | One of these |
| `GEMINI_API_KEY` | Protocol generation via Gemini (fallback) | is required |
| `SUPABASE_URL` + `SUPABASE_KEY` | Organizational context queries | Optional (has defaults) |
| `python-docx` | Reading .docx files | Only for .docx input |