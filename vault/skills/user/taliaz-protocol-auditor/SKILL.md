---
alfred_tags:
- taliaz/knowledge-base
- data-ingestion
- protocols
description: 'Audits protocols produced by taliaz-protocol-writer to verify they are
  grounded in real Taliaz organizational data, not generic clinical knowledge. Calculates
  a "Grounding Score" based on 8 audit categories. Triggers on: audit protocol, validate
  protocol grounding, check protocol accuracy, is this protocol real, review protocol
  against KB.'
name: taliaz-protocol-auditor
---

# Taliaz Protocol Auditor

A quality assurance skill that audits protocols and SOPs, answering one critical question: **Is this document grounded in Taliaz's actual, living organizational reality, or is it generic?**

It runs a protocol through an 8-category audit, cross-referencing its claims against the Supabase KB, Slack, and other live data sources to produce a quantitative "Grounding Score" and a qualitative verdict.

## When to Use

- After `taliaz-protocol-writer` generates a new protocol draft.
- When reviewing an existing protocol for accuracy and relevance.
- When a user asks "is this protocol real?" or "does this reflect how we actually work?"

## How to Use

Run the main audit script on the protocol file:

```bash
python3 /home/ubuntu/skills/taliaz-protocol-auditor/scripts/audit_protocol.py [path_to_protocol.md]
```

The script will:
1.  Query the Supabase KB for all employees, responsibilities, systems, and known facts.
2.  Parse the protocol and extract all named entities, systems, and process steps.
3.  Run the 8 audit checks against the live data.
4.  Generate a detailed Markdown audit report in the same directory.

## Audit Categories & Scoring

The final Grounding Score is a weighted average of 8 category scores:

| Category | Description | Weight |
|---|---|---|
| 1. Entity Verification | Are the people and roles real and correctly assigned? | 20% |
| 2. System Verification | Are the technology systems and tools real? | 15% |
| 3. Workflow Verification | Does the process match what's documented in the KB? | 20% |
| 4. Org. Grounding | Does it use real names, channels, terms, and context? | 15% |
| 5. Regulatory Accuracy | Are legal/regulatory citations correct for Taliaz? | 10% |
| 6. Contradiction Check | Does it conflict with other known protocols or decisions? | 10% |
| 7. Hallucination Detection | Does it invent facts, stats, or entities? | 5% |
| 8. Completeness Check | Does it address known pain points and relevant context? | 5% |

## Output

The script outputs a detailed `[protocol_name]_audit_report.md` file with:

- **Overall Grounding Score**: 0-100%
- **Verdict**: `GROUNDED`, `PARTIALLY GROUNDED`, or `GENERIC`
- **Per-Category Scores**: Detailed breakdown of each of the 8 checks.
- **Findings**: A list of all CRITICAL, WARNING, and INFO issues, with direct quotes from the protocol and evidence from the KB or other sources.

This allows for rapid, evidence-based quality assurance of all organizational knowledge documentation.