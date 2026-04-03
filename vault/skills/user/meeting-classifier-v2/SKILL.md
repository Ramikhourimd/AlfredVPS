---
name: meeting-classifier-v2
description: Classify meeting transcripts by identifying which known recurring meeting they belong to, or suggest a logical new meeting name if unknown. Use when processing any meeting transcript, VTT file, or meeting notes to determine the meeting type. Triggers on requests like "what meeting is this", "classify this transcript", "identify meeting type", or automatically during transcript processing via taliaz-doc-processor. Returns structured meeting metadata including meeting_id, category, participants, and confidence score.
---

# Meeting Classifier (v2)

This skill identifies which known recurring meeting a transcript belongs to. It uses a weighted scoring algorithm based on signals from the transcript, filename, and calendar data.

**Key Improvement in v2:** The volatile meeting and speaker data has been moved to reference files, making the core skill logic more stable and easier to maintain. The classification algorithm has also been significantly improved with higher-fidelity signals.

## When to Use

- When processing any meeting transcript (VTT, TXT, MD, Google Doc).
- As a pre-processing step for `taliaz-doc-processor` to populate meeting metadata.
- When a user asks "what meeting is this?" or "classify this transcript".

## Classification Workflow

1.  **Read Reference Data:** Load the latest meeting and speaker data from `references/meeting_registry.md` and `references/speaker_aliases.md`.
2.  **Extract Signals:** Parse the input transcript and its metadata to extract key classification signals.
3.  **Score Candidates:** Match the extracted signals against the known meetings from the registry and calculate a confidence score for each.
4.  **Decide & Output:** Based on the highest score, either classify the meeting or suggest a new name if confidence is low.

## Signal Extraction & Scoring

The algorithm calculates a confidence score (0.0–1.0) for each known meeting based on the following weighted signals.

### Primary Signals (High Weight)

<table header-row="true">
<tr>
<td>Signal</td>
<td>How to Extract</td>
<td>Weight</td>
</tr>
<tr>
<td>**Filename Match**</td>
<td>Parse meeting name from filename (e.g., "Innovation Team | Jan 15.docx").</td>
<td>0.40</td>
</tr>
<tr>
<td>**Zoom Link Match**</td>
<td>Cross-reference Zoom link from calendar/transcript with known links in registry.</td>
<td>0.40</td>
</tr>
<tr>
<td>**Speaker Overlap**</td>
<td>Match speaker names from transcript against known participant lists.</td>
<td>0.30</td>
</tr>
<tr>
<td>**Calendar Title Match**</td>
<td>Match transcript date/time to a calendar event and compare titles.</td>
<td>0.25</td>
</tr>
</table>

### Secondary Signals (Medium Weight)

<table header-row="true">
<tr>
<td>Signal</td>
<td>How to Extract</td>
<td>Weight</td>
</tr>
<tr>
<td>**Day of Week**</td>
<td>From filename, metadata, or calendar cross-reference.</td>
<td>0.15</td>
</tr>
<tr>
<td>**Time of Day**</td>
<td>From metadata or timestamps in transcript.</td>
<td>0.10</td>
</tr>
<tr>
<td>**Topics Discussed**</td>
<td>Keyword analysis of transcript content (e.g., clinical, product, AI).</td>
<td>0.10</td>
</tr>
</table>

### Scoring Formula

```
score = (filename_match * 0.40) +
        (zoom_link_match * 0.40) +
        (speaker_overlap * 0.30) +
        (calendar_title_match * 0.25) +
        (day_match * 0.15) +
        (time_match * 0.10) +
        (topic_match * 0.10)
```

*Note: The weights are designed to allow a strong signal (like a filename or Zoom link match) to create a high confidence score even if other signals are weak.* A simple average is taken if multiple primary signals are present.

## Decision Logic

<table header-row="true">
<tr>
<td>Score Range</td>
<td>Action</td>
</tr>
<tr>
<td>≥ 0.80</td>
<td>**High Confidence Match** — Classify as this meeting.</td>
</tr>
<tr>
<td>0.50–0.79</td>
<td>**Probable Match** — Classify but flag for user review.</td>
</tr>
<tr>
<td>< 0.50 for all</td>
<td>**Unknown** — Generate a suggested meeting name.</td>
</tr>
</table>

## Name Suggestion for Unknown Meetings

When no known meeting matches, generate a name using the format `[CATEGORY]-[PRIMARY_TOPIC]-[QUALIFIER]`.

-   **Categories:** `HM` (HealthyMind), `TLZ` (Taliaz), `EXT` (External), `AD-HOC`.
-   **Rules:** Use English, keep it concise, name 1:1s by participants, and name group meetings by topic.

## Output Format

Return a structured JSON object containing the classification, signals, and confidence score, as defined in the original skill.
