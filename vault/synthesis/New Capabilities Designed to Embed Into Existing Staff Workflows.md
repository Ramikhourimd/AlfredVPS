---
alfred_tags:
- telia'z/restructuring
- clinic/operations
- innovation/program
cluster_sources:
- '[[task/Add Secretary Tasks for Commitment Renewal Reminders]]'
- '[[task/Build Psychiatrist Feedback Survey for Summary Feature Baseline]]'
- '[[task/Investigate Patient Follow-Up Flow With Shira and Renee]]'
- '[[task/Gather Clinic Staff System Requirements]]'
confidence: medium
created: '2026-03-30'
name: New Capabilities Designed to Embed Into Existing Staff Workflows
project:
- '[[project/Telia''z AI Clinical Platform]]'
related:
- '[[synthesis/Platform Rebuild Requirements Distributed Across Stakeholders With
  No Central Repository]]'
- '[[decision/Combine Psychiatrist Satisfaction Survey With Feature Baseline Measurement]]'
status: draft
supports:
- '[[assumption/Secretary Pre-Session Call Workflow Can Absorb Renewal Reminders]]'
type: synthesis
---

# New Capabilities Designed to Embed Into Existing Staff Workflows

## Insight

Across multiple task records, a consistent design philosophy emerges: new capabilities are systematically embedded into existing staff workflows rather than creating parallel processes. This is not accidental — it reflects a deliberate strategy to minimize change management overhead and maximize adoption by piggybacking on routines staff already perform.

## Evidence

1. **Secretary renewal reminders** embed into the existing pre-session call workflow rather than creating a separate reminder system (task/Add Secretary Tasks for Commitment Renewal Reminders)
2. **Psychiatrist feedback survey** combines with baseline measurement rather than running separate instruments (task/Build Psychiatrist Feedback Survey for Summary Feature Baseline)
3. **Survey distribution** routes through Shira → Alice/Elis, leveraging the existing clinical communication chain rather than direct outreach
4. **Patient flow investigation** uses existing staff roles (Shira, Renee, Roy) as knowledge sources rather than building a formal documentation process
5. **Requirements gathering** interviews each stakeholder group in their existing context rather than running formal workshops

## Implications

- New feature designs should always identify which existing workflow they can attach to before proposing standalone processes
- Change management costs are systematically reduced because staff don't need to learn new routines
- Risk: if the host workflow is disrupted (e.g., secretaries stop making pre-session calls), all embedded capabilities fail simultaneously
- Feature specifications should document which existing workflow they embed into, not just what they do

## Applicability

This pattern applies to all operational feature design for the HealthyMind clinic platform. Any proposed new workflow should first be evaluated for embedding potential before being built as a standalone process.