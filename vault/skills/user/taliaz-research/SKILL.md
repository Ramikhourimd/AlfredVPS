---
alfred_tags:
- taliaz/knowledge-base
- data-ingestion
- protocols
description: Research and synthesize organizational knowledge from Taliaz's scattered
  sources of truth (meeting transcripts, Google Drive documents, Gmail, Calendar).
  Use when asked questions about Taliaz decisions, policies, project status, people
  responsibilities, what was discussed in meetings, or any organizational knowledge
  that requires searching historical records. Triggers on queries like "What did we
  decide about...", "What's our approach to...", "Who handles...", "What's the status
  of...", "What did [person] say about...", or any question requiring institutional
  memory.
name: taliaz-research
---

# Taliaz Organizational Research

Research and synthesize answers from Taliaz's organizational knowledge sources.

## Primary Data Source

**Google Drive Folder:** `Taliaz Meeting Transcripts`
- Folder ID: `1BdEsYy1K8ujqjegPAfcxUrW4rDhortRd`
- Contains: Meeting transcripts (Google Docs), organized by category

### Folder Structure & Topics

| Folder | Search for queries about... |
|--------|---------------------------|
| `01_Strategy_and_Leadership` | Company direction, OKRs, strategic decisions, board matters |
| `02_Clinical_Operations` | Patient workflows, clinical protocols, assessments, ADHD, treatments |
| `04_Partnerships_and_Contracts` | Maccabi, UK expansion, CQC, external partners, contracts |
| `05_HR_Finance_Legal` | Hiring, salaries, legal matters, compliance |
| `07_Stakeholder_OneOnOnes` | Individual meetings, 1:1s, personal discussions |
| `09_Personal_Development` | Training, career growth, coaching |
| `dekel/` | Meetings with/about Dekel Taliaz |
| `Oren/` | Meetings with/about Oren Taliaz |
| `lifelogs/` | Limitless pendant recordings, informal conversations |
| Root level | Cross-functional meetings, team syncs |

## Research Workflow

### Step 1: Parse the Query

Identify:
- **Topic domain** → which subfolder(s) to search
- **People mentioned** → search by name (Hebrew and English)
- **Time scope** → filter by date if specified
- **Query type** → fact lookup vs. synthesis vs. timeline

### Step 2: Search Strategy

1. **Start with semantic search** in the transcripts folder:
   ```
   google_drive_search(
     api_query="'1BdEsYy1K8ujqjegPAfcxUrW4rDhortRd' in parents",
     semantic_query="[user's question]"
   )
   ```

2. **If topic is clear**, search specific subfolder first

3. **Search in both Hebrew and English** — transcripts contain both languages

4. **For person-specific queries**, also search:
   - Person's dedicated folder if exists (dekel/, Oren/)
   - Their name in Hebrew: See references/people.md for name mappings

### Step 3: Read & Synthesize

1. **Fetch full transcript** using `google_drive_fetch` for relevant docs
2. **Extract relevant sections** — look for speaker names and timestamps
3. **Cross-reference** if topic spans multiple meetings
4. **Note conflicting information** across sources

### Step 4: Format Response

```markdown
## [Answer Title]

[Synthesized answer in 2-3 paragraphs]

### Key Points
- Point 1
- Point 2

### Sources
- [Meeting name | Date](link) — [brief context of what was discussed]
- [Meeting name | Date](link) — [brief context]

### Gaps/Conflicts
- [Note any missing information or contradictions found]
```

## Transcript Format Notes

Transcripts use two speaker formats:
- **Named:** `Stav Zamir (44.09):` or `ראמי (00:05:23):`
- **Anonymous:** `Speaker 1 00:00:00`

When searching by person, use both English and Hebrew names.

## Secondary Sources

When transcripts don't have the answer, also search:

1. **Gmail** — for decisions made via email, commitments, agreements
2. **Calendar** — for meeting context, attendees, timing
3. **General Drive** — for formal documents, SOPs, presentations

## Important Context

- Transcripts are from Rami Khouri's Limitless Pendant recordings
- Not all organizational meetings are captured — only those Rami attended
- Recent transcripts may not be fully processed yet
- For person roles and responsibilities, see `references/people.md`