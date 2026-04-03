---
created: '2026-02-25'
description: Comprehensive product meeting covering clinical report event logic standardization,
  API-first data architecture, AI summary orchestration design, monthly clinic reporting
  APIs, and psychiatry transcription workflow for Telia'z clinical platform.
janitor_note: LINK001 — Telia'z wikilinks are valid (YAML escaping false positive).
  Base view embed (related.base#All) references _bases/related.base which does not
  exist.
name: Product Meeting Report Logic API and AI Architecture 2026-02-25
project: '[[project/Telia''z AI Clinical Platform]]'
related:
- '[[person/Rami Khouri]]'
- '[[person/Shmulik]]'
- '[[org/Telia''z]]'
- '[[project/Telia''z Clinic Israel]]'
- '[[project/Telia''z AI Diagnostic Research Paper]]'
- '[[conversation/Product Meeting Report Logic API and AI Architecture]]'
relationships: []
session: null
status: active
subtype: meeting-notes
tags: []
type: note
---

# Product Meeting: Report Logic, API Integration, and AI Architecture for Summaries

## Context

Product and engineering meeting at Telia'z to align on the technical foundations of the clinical platform. The discussion spanned six major areas: report event logic, data quality, data architecture, API design, AI summary orchestration, and psychiatry transcription workflows.

## 1. Report Event Logic Standardization

Summary approval is identified through `approve` (Maccabi) or `send` (other clinic centers); `save` is not considered approval. Real production data begins around March 10 — prior events are mostly test data.

**Edit time measurement** is only reliable in real-time mode. Google Docs `modified` events are not valid start-of-editing markers.

## 2. Data Quality Issues

Multiple data quality problems identified:
- **Noise and contamination**: Unreasonable wait times and impossible patient ages in the dataset
- **Filtering approach**: Statistical thresholds / standard deviations for outlier removal; age-specific cleaning for impossible values
- **Open/test sessions**: Sessions left open or test sessions that were never closed; difficult to determine status without manual intervention
- Shmulik to provide a list of 22 patients with unreasonable ages and confirm report gaps under the new approval logic

## 3. Data Architecture and Performance

**Read-Only/Shadow DB** recommended as a separate layer for non-real-time analytical queries, reducing production load. Key elements:
- Synchronized replica for analytics
- Pagination for high-volume reads
- Scheduling large data pulls outside peak hours
- Monitoring and sync process management

**BigQuery/DWH** integration for pricing data — need to verify table/view locations for meeting pricing.

## 4. API-First Design

Strong preference for stable API endpoints over manual exports. Design principles:
- **Low-level entity APIs**: Get Patient, Get Meeting (with sub-resources: Transcript, Summary, Diagnosis, Prescription), Get Questionnaire
- **Pagination and payload limits** for all list endpoints
- **Authentication and authorization**: Per-API access controls, detailed logging, anomaly detection
- **Original + long summary API**: Returns both original and long-form summary by Meeting ID for comparison/scoring
- **Monthly report API**: All meetings for a month including Cancel/No-show, cancellation reasons, creation/scheduling times, therapist names
- **Available hours**: Explore pulling from calendar or automated monthly export

## 5. AI Summary Orchestration

- **Start simple**: Begin with a basic orchestrator without MCP (Model Context Protocol)
- **MCP later**: Reserve MCP for future chat/advanced orchestration needs
- **Trigger mechanism**: Webhooks as target mechanism; Start API as interim solution until webhook stabilization
- **Start API enrichment**: Add mandatory parameters — user ID, clinic, meeting type/ID
- **Output standardization**: Move to structured JSON with uniform section hierarchy; HTML alternative available if needed

## 6. Psychiatry Transcription Operations

- **Teams Captions**: Enable real-time with defined language setting during sessions
- **Transcript**: Enable as end-of-session backup
- **Local recorder**: Explore running a background local recorder to reduce friction
- **Goal**: Maximize automatic transcription, minimize manual steps

## 7. Configuration and International Readiness

- Questionnaire structure, conditions, and validations should be configurable without code changes
- Rami to build a configuration document for questionnaire schema
- Important for international clinic deployments

## Key Blockers

1. **Shmulik's report gaps**: Missing data and logic discrepancies between clinics
2. **Edit time measurement**: Cannot measure outside real-time mode
3. **Data noise**: Extreme wait times and impossible ages contaminating analytics
4. **System load**: Large data pulls risk production impact — needs scheduling and Shadow DB
5. **Webhook instability**: Currently unreliable, using Start API as interim
6. **DWH access**: Partial dataset access, no full standardization, needs pagination
7. **Security/privacy**: Multiple storage locations for sensitive data; preference for minimal storage

## Follow-Up Topics for Next Meeting

1. Review approved API call set with JSON examples, parameters, pagination, and end-to-end flow
2. Updated report with noise filtering — before/after comparison and metric impact
3. Load testing update and time window definitions for large pulls; Shadow DB status
4. Pilot demo: original vs long summary comparison (quality/gaps)
5. Shmulik report gaps resolution including impossible ages and open session cleanup
6. Final decision on JSON output standard and schema; mapping deterministic vs agentic flows
7. MCP model evaluation for chatbot integration; security/logging policy across APIs

## Related
![[related.base#All]]
