---
created: '2026-03-02'
description: Meeting notes on developing a Maccabi-branded brochure for Telem families
  of wounded soldiers, designing per-clinic referral tracking with unique QR codes/URLs,
  and reviewing outreach strategies across Israeli cities.
janitor_note: LINK001 — [[decision/Start Telem Family Services With Maccabi Before
  Clalit Expansion]] does not exist, no close matches found — needs manual creation
  or removal. LINK001 — related.base#All embed references _bases/related.base which
  does not exist — create base file to enable dynamic views. ORPHAN001 — no inbound
  links from other records.
name: Telem Wounded Soldiers Family Services Brochure and Tracking Plan 2025-11-16
project: '[[project/Telia''z Clinic Israel]]'
related:
- '[[conversation/Telem Brochure and Referral Tracking Meeting 2025-11-16]]'
- '[[org/Telem]]'
- '[[org/Telia''z]]'
- '[[org/Maccabi Healthcare Services]]'
- '[[person/Rami Khouri]]'
- '[[person/Ori Shukron]]'
- '[[person/Shachar]]'
- '[[person/Oren Taliaz]]'
- '[[person/Ziv]]'
- '[[person/Adiel Levin]]'
- '[[person/Adi Lavi]]'
- '[[decision/Start Telem Family Services With Maccabi Before Clalit Expansion]]'
relationships: []
session: null
status: active
subtype: meeting-notes
tags: []
type: note
---

# Telem Wounded Soldiers Family Services Brochure and Tracking Plan 2025-11-16

## Context

Meeting notes from a Telia'z team meeting on 2025-11-16. The team discussed building a brochure and referral tracking system for Telem — a military rehabilitation unit under the IDF Rehabilitation Division (Agaf HaShikum) — which channels families of wounded soldiers to psychiatric services via Israeli health funds.

## Brochure Requirements

### Target Audience
- Families of wounded soldiers eligible for psychiatric services through Telem
- Patients enrolled through Maccabi Healthcare Services specifically

### Branding
- The brochure must be **Maccabi-branded**, not Telem-branded
- This is a deliberate design choice: the brochure represents the healthcare service pathway, not the military unit
- Families should understand this as a Maccabi health service

### Content
- Explain what the psychiatric service is and what treatment looks like
- Clarify eligibility (families of wounded soldiers recognized by the Rehabilitation Division)
- Describe the screening/intake process
- Provide contact information and next steps

### Distribution
- Distributed through Telem's channels to eligible families
- Potentially distributed at Maccabi clinics in key cities
- Each distribution point gets a unique tracking link

## Referral Tracking System Design

### Goal
Track which outreach channel, clinic, and city generate referrals to measure brochure and campaign effectiveness.

### Mechanism
- **Unique URLs per clinic/city**: Each brochure version includes a distinct URL with tracking parameters
- **QR codes**: Physical brochures include QR codes that encode the unique URL
- **URL parameters**: Added to the existing Telia'z intake form URL (e.g., `?source=telem&city=ashdod&clinic=maccabi-ashdod`)
- **Dashboard integration**: Tracking data feeds into the existing patient referral dashboard

### Key Design Decisions
- One brochure template with variable QR codes per location
- Tracking parameters should identify: source (Telem), city, specific clinic/distribution point
- Data should be visible in the existing dashboard Shachar maintains

## City-by-City Outreach Status

| City | Status | Notes |
|------|--------|-------|
| Ashdod | Leading | Highest referral volumes |
| Ashkelon | Leading | Strong referral performance |
| Tel Aviv | Growing | Increasing patient intake |
| Afula | Planned | Outreach visits being scheduled |
| Other | Various | Ori conducting relationship-building visits |

## Key People

- **Amiad** — Manager of Telem unit (drives the brochure initiative)
- **Ori Shukron** — Handles field outreach and clinic visits
- **Shachar Segev** — Manages dashboard and data presentation
- **Rami Khouri** — Proposed tracking system design
- **Oren Taliaz** — Participated in prior Telem meeting
- **Ziv** — Asked about data and follow-up tracking

## Open Questions

1. What is the timeline for brochure production? (Roey asked during meeting)
2. Should the brochure extend to Clalit? (Decision: Maccabi first)
3. How to systematically track the impact of outreach interventions per city over time?
4. What tracking spreadsheet format should capture interventions and their downstream referral impact?

## Source

Conversation: [[conversation/Telem Brochure and Referral Tracking Meeting 2025-11-16]]

---
## Related
![[related.base#All]]
