---
name: taliaz-kb-remedy
description: Step-by-step remediation of the Taliaz HealthyMind Supabase KB based on the Operation Clean Room forensic investigation. Guides execution of 10 remediation steps across 4 phases, with GPT-5.4 Pro audit gates between each step. Use when asked to fix the KB, remedy the KB, continue KB remediation, run next KB fix, or audit KB fix. Triggers on remedy KB, fix KB, KB remediation, next KB step, audit KB step.
---

# Taliaz KB Remedy

Guided remediation of the Taliaz Supabase KB based on the forensic investigation (Operation Clean Room, March 2026). Each step is executed, then audited by GPT-5.4 Pro before proceeding.

## Context

The forensic investigation found 34 critical issues. The KB is unreliable and poses privacy risks. Three root failures: (1) authoritative data never ingested properly, (2) AI-generated artifacts promoted to facts, (3) clinical data governance not enforced.

## Execution Protocol

### Before Each Step
1. Read the step details from `references/steps/step_NN.md`
2. Show the user what will be done and get confirmation
3. Take a pre-step snapshot (count affected rows)

### Executing a Step
1. Run the remediation SQL/code via Supabase MCP or REST API
2. Verify the fix by querying the affected tables
3. Save results to `/home/ubuntu/kb_forensic_investigation/remedy_log/step_NN_result.json`

### After Each Step (Audit Gate)
1. Collect before/after metrics
2. Send to GPT-5.4 Pro with the original recommendation for that step
3. GPT-5.4 Pro evaluates: PASS (proceed) or FAIL (investigate and retry)
4. Save audit result to `/home/ubuntu/kb_forensic_investigation/remedy_log/step_NN_audit.md`
5. Only proceed to next step on PASS

### GPT-5.4 Pro Audit Call Pattern
```python
from openai import OpenAI
client = OpenAI()
response = client.responses.create(
    model="gpt-5.4-pro",
    input=[{"role": "user", "content": audit_prompt}],
    reasoning={"effort": "medium"},
    max_output_tokens=100000,
)
result = response.output_text
```
Timeout: allow up to 10 minutes. GPT-5.4 Pro supports up to 100K output tokens. If empty output_text, retry once with same parameters.

## Remediation Steps

### Phase 1: Emergency Fixes (P0)

| Step | Title | Findings Addressed | Priority |
|------|-------|--------------------|----------|
| 01 | Quarantine clinical/patient data | F10, F13, F14, F21 | P0 |
| 02 | Fix employee identity layer | F1, F4, F15, F25, F26, F27, F28 | P0 |
| 03 | Quarantine fake projects | F7 | P0 |
| 04 | Fix orphaned entity references | F6, F20 | P0 |

### Phase 2: Structural Repairs (P1)

| Step | Title | Findings Addressed | Priority |
|------|-------|--------------------|----------|
| 05 | Unify meeting ID formats | F2, F17, F18, F19 | P1 |
| 06 | Fix null-shell records | F8, F9, F16, F22, F24, F29, F30, F31 | P1 |

### Phase 3: Pipeline Fixes (P2)

| Step | Title | Findings Addressed | Priority |
|------|-------|--------------------|----------|
| 07 | Purge non-work data | F11 | P2 |
| 08 | Fix action items | F8 | P2 |

### Phase 4: Quality Gates (P3)

| Step | Title | Findings Addressed | Priority |
|------|-------|--------------------|----------|
| 09 | Add integrity constraints and provenance | F5, F32, F33, F34 | P3 |
| 10 | Build observability dashboard | All | P3 |

## Tracking State

Maintain state in `/home/ubuntu/kb_forensic_investigation/remedy_state.json`:
```json
{
  "current_step": 1,
  "steps_completed": [],
  "steps_failed": [],
  "last_audit": null,
  "started_at": "2026-03-09T...",
  "phase": 1
}
```

Read this file at the start of every session to know where we left off.

## Supabase Connection

Use the Supabase REST API for reads:
```python
import os, requests
url = os.environ["SUPABASE_URL"]
key = os.environ["SUPABASE_KEY"]
headers = {"apikey": key, "Authorization": f"Bearer {key}", "Content-Type": "application/json"}
```

For SQL DDL or complex queries, use Supabase MCP:
```bash
manus-mcp-cli tool call execute_sql --server supabase --input '{"project_id": "biaxrsfkuubslzxlcqxq", "query": "..."}'
```

## Step Reference Files

Each step has a detailed file at `references/steps/step_NN.md` with:
- Exact SQL adapted to real Taliaz table/column names
- Pre-check queries (measure before)
- Post-check queries (verify after)
- Rollback instructions
- Audit prompt template for GPT-5.4 Pro

Read the step file before executing.

## Acceptance Criteria (from GPT-5.4 Pro)

KB should not return to service until:
- People: 95-100% of active employees matched to authoritative directory
- Meetings: every meeting tied to a canonical source event
- Integrity: near-zero orphan references in core tables
- Required fields: no records missing mandatory identity/source fields
- PHI/PII: 0 patient data in non-clinical org KB collections
- Lineage: every record traceable to source system + ingestion run
- Generated content: no AI-created "facts" without source grounding
