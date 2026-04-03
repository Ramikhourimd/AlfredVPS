---
name: meeting-classifier
description: Classify meeting transcripts by identifying which known recurring meeting they belong to, or suggest a logical new meeting name if unknown. Use when processing any meeting transcript, VTT file, or meeting notes to determine the meeting type. Triggers on requests like "what meeting is this", "classify this transcript", "identify meeting type", or automatically during transcript processing via taliaz-doc-processor. Returns structured meeting metadata including meeting_id, category, participants, and confidence score.
---

# Meeting Classifier

Identifies which known recurring meeting a transcript belongs to, or suggests a logical new meeting name.

## Classification Workflow

```
TRANSCRIPT → EXTRACT SIGNALS (speakers, language, topics, day/time)
          → MATCH AGAINST KNOWN MEETINGS (score each candidate)
          → HIGH (≥0.75): Return matched meeting
          → MEDIUM (0.50-0.74): Return match + flag for review
          → LOW (<0.50): Suggest new meeting name
```

## Known Meetings Registry (Active — February 2026)

### HealthyMind Clinical Operations
| meeting_id | Name | Day | Time | Participants | Topics |
|------------|------|-----|------|-------------|--------|
| `HM-RIVI-WEEKLY` | Meeting With Rivi | Tuesday | 12:30 | Rami, Rivi | UX, workflows, design |
| `HM-BASEL-WEEKLY` | Meeting with Basel | Thursday | 11:00 | Rami, Basel | Clinical ops, scheduling |
| `HM-STAV-WEEKLY` | Meeting with Stav | Thursday | 12:00 | Rami, Stav | Clinical quality, protocols |

### Taliaz Company Meetings
| meeting_id | Name | Day | Time | Participants | Topics |
|------------|------|-----|------|-------------|--------|
| `TLZ-RAMI-TAL-WEEKLY` | Weekly with Rami | Thursday | 10:30 | Rami, Dekel, Tal | Strategy, CEO sync |
| `TLZ-INNOVATION` | Innovation Team | Thursday | 13:00 | Rami, Yael+ | AI, product, research |
| `TLZ-LEADERSHIP-SYNC` | Leadership Sync | Sunday | 12:00 | Rami, Alex, Oren, Dekel | Cross-functional strategy |
| `TLZ-BACKLOG` | Backlog Review | Sunday | 14:00 | Rami, Dekel, Shachar, Roy, Yael | Product/sprint planning |
| `TLZ-RAMI-OHAD` | Rami-Ohad Meeting | Sunday | 16:00 | Rami, Ohad, Rivi | AI infra, architecture |

### Monthly
| meeting_id | Name | Schedule | Participants | Topics |
|------------|------|----------|-------------|--------|
| `HM-TEAM-SUPERVISION` | Monthly Team Supervision | Sunday (monthly) 20:00 | Ori + full clinical team | Clinical cases, supervision |

### Discontinued Meetings (for historical classification)
| meeting_id | Name | Participants | Ended |
|------------|------|-------------|-------|
| `HM-MGMT-WEEKLY` | HM Management Weekly | Rami, Elias, Shira, Ori, Eleanor, Basel | Dec 2025 |
| `HM-SHIRA-MGMT` | Shira's Management | Rami, Alex, Basel, Shira | Dec 2025 |
| `HM-RAMI-ELEANOR` | Rami & Eleanor 1:1 | Rami, Eleanor | Eleanor transition |
| `HM-RAMI-ELIAS` | Rami + Elias Clinical | Rami, Elias | Elias departure |
| `TLZ-MGMT-SUNDAY` | Management Meeting (Roy's Sunday) | Roy + management | Jan 2026 |

## Scoring Formula

```
score = (speaker_overlap * 0.35) + (day_match * 0.20) + (time_match * 0.10) +
        (language_match * 0.10) + (topic_match * 0.10) +
        (participant_count_match * 0.05) + (duration_match * 0.05) +
        (formality_match * 0.03) + (cross_reference_match * 0.02)

speaker_overlap = |detected_speakers ∩ known_participants| / |known_participants|
```

Day match: Exact = 1.0 | Off-by-1 = 0.3 | Unknown = 0.5 (neutral)
Time match: Within 30min = 1.0 | Within 2hr = 0.5 | Unknown = 0.5 (neutral)

## Output Format

```json
{
  "classification": {
    "meeting_id": "TLZ-RAMI-OHAD",
    "meeting_name": "Rami-Ohad Meeting",
    "confidence": 0.92,
    "confidence_level": "HIGH",
    "is_active": true,
    "is_new_suggestion": false
  },
  "signals": {
    "speakers_detected": ["Rami", "Ohad", "Rivi"],
    "day_of_week": "Sunday",
    "time_of_day": "16:00",
    "language": "Hebrew/English",
    "primary_topics": ["AI infrastructure", "Supabase"]
  }
}
```

For unknown meetings, generate a name using format `[CAT]-[TOPIC]-[QUALIFIER]`:
- `HM` = HealthyMind clinical/operational
- `TLZ` = Taliaz company/product
- `EXT` = External stakeholder
- `AD-HOC` = One-time meeting (include date)

## Speaker Name Aliases

| Canonical | Aliases |
|-----------|---------|
| Rami Khouri | רמי, Rami, ד"ר רמי |
| Rivi Adelman | ריבי, Rivi |
| Stav Zamir | סתיו, Stav |
| Ohad Edri | אוהד, Ohad |
| Basel | באסל, Basel |
| Dekel | דקל, Dekel |
| Yael | יעל, Yael |
| Alex | אלכס, Alex |
| Oren | אורן, Oren |
| Shachar | שחר, Shachar |
| Roy | רועי, Roy |
| Ori | אורי, Ori |
| Shira | שירה, Shira |
| Eleanor Khateeb | אלינור, Eleanor |

## Quick Fingerprints

| Meeting | Fingerprint |
|---------|-------------|
| Rivi Weekly | Rami+Rivi, Tuesday, UX/design |
| Basel Weekly | Rami+Basel, Thursday AM, clinical ops |
| Stav Weekly | Rami+Stav, Thursday noon, protocols |
| Weekly with Rami | Rami+Dekel+Tal, Thursday 10:30, strategy |
| Innovation Team | Rami+Yael+, Thursday 13:00, AI/product |
| Leadership Sync | Rami+Alex+Oren+Dekel, Sunday noon |
| Backlog Review | Rami+Dekel+Shachar+Roy+Yael, Sunday 14:00 |
| Rami-Ohad | Rami+Ohad+Rivi, Sunday PM, AI infra |
| Monthly Supervision | Ori+full team, Sunday evening |

## Calendar Cross-Reference Zoom Links

- Rivi meeting: `zoom.us/j/89546335237`
- Basel meeting: `zoom.us/j/88617172735`
- Weekly with Rami (Tal): `zoom.us/j/6263388158`
