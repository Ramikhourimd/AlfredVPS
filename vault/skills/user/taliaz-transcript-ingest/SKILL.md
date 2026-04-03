---
alfred_tags:
- taliaz/knowledge-base
- data-ingestion
- protocols
description: Ingest meeting transcripts from Google Drive folder into Taliaz's Supabase
  knowledge base with AI-powered analysis. Populates all relevant tables including
  memory_l1_core, memory_l2_context_intent, meeting_metadata, entity_occurrences,
  and speaker_memory. Triggers on "ingest transcripts", "process today's transcripts",
  "sync meeting transcripts from Drive".
name: taliaz-transcript-ingest
---

# Taliaz Transcript Ingestion (Enhanced)

Fetches meeting transcripts from Google Drive and populates **ALL relevant** Supabase knowledge base tables using AI-powered analysis.

## Quick Start

### Ingest Today's Transcripts
```bash
python3 /home/ubuntu/skills/taliaz-transcript-ingest/scripts/ingest_transcripts.py
```

### Ingest Specific Date
```bash
python3 /home/ubuntu/skills/taliaz-transcript-ingest/scripts/ingest_transcripts.py --date 2026-01-26
```

### Preview Without Inserting
```bash
python3 /home/ubuntu/skills/taliaz-transcript-ingest/scripts/ingest_transcripts.py --dry-run
```

## Tables Populated

| Table | What Gets Inserted |
|-------|-------------------|
| `memory_l1_core` | Main transcript record with metadata, entities, topics, events (decisions, actions, questions) |
| `memory_l2_context_intent` | Contextual analysis: primary/secondary intents, follow-ups, risks, related projects/people |
| `meeting_metadata` | Meeting title, date, participants, language, meeting type |
| `entity_occurrences` | Links transcripts to people, projects, organizations mentioned |
| `speaker_memory` | Updates speaker profiles with files they appeared in |

## AI-Powered Analysis

The script uses OpenAI GPT-4o-mini to extract:
- **Summary**: 2-3 sentence meeting summary
- **Category**: Clinical_Operations, Innovation_Technology, Research, HR_Recruitment, Strategy, Finance, International_Expansion, General
- **Meeting Type**: ops, strategy, 1on1, team, research, training, external
- **Primary Intent**: Main purpose of the meeting
- **Secondary Intents**: Other topics discussed
- **Decisions**: List of decisions made
- **Action Items**: Tasks with owner, description, due date
- **Open Questions**: Unresolved questions
- **Risks**: Identified risks or concerns
- **Follow-ups**: Items requiring follow-up with priority and status
- **Entities**: People, projects, organizations mentioned

If OpenAI API is unavailable, falls back to keyword-based analysis.

## Source Configuration

- **Google Drive Folder ID**: `1BdEsYy1K8ujqjegPAfcxUrW4rDhortRd`
- **File Types**: `.docx` files only
- **Scope**: Main folder only (subfolders are excluded)

## How It Works

1. **Lists files** from the Google Drive folder using rclone
2. **Filters by date** to only process transcripts from the target date
3. **Downloads** each transcript file
4. **Extracts text** from .docx format
5. **Analyzes with AI** to extract structured information
6. **Matches entities** against existing entity lookups
7. **Inserts records** to all relevant Supabase tables
8. **Creates entity occurrences** for tracking mentions
9. **Updates speaker memory** with appearance records

## Entity Matching

Uses `/home/ubuntu/entity_lookups.json` to match:
- **People**: Employees and known contacts
- **Projects**: Tracked projects
- **Organizations**: Partner organizations, clients

## Requirements

- rclone configured with Google Drive access
- Entity lookups file at `/home/ubuntu/entity_lookups.json`
- Supabase credentials (uses environment variables or defaults)
- OpenAI API key (optional, for AI analysis)

## Environment Variables

| Variable | Description |
|----------|-------------|
| `SUPABASE_URL` | Supabase project URL |
| `SUPABASE_KEY` | Supabase API key |
| `OPENAI_API_KEY` | OpenAI API key for AI analysis |
| `OPENAI_API_BASE` | OpenAI API base URL (optional) |

## Triggers

Use this skill when:
- "ingest today's transcripts"
- "process transcripts from [date]"
- "sync meeting transcripts"
- "add transcripts to knowledge base"
- "analyze meeting recordings"