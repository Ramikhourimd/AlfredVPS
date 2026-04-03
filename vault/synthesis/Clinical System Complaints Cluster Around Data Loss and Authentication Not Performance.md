---
cluster_sources:
- '[[note/Clinic Platform Referral Form and System Performance Discussion 2025-11-10]]'
- '[[note/Retool System Prioritization and Data Access Discussion 2025-12-05]]'
- '[[note/Retool Prioritization and Data Access Discussion 2025-12-05]]'
- '[[constraint/Psychiatrist Authentication Issues Cause Repeated Workflow Disruptions]]'
- '[[task/Compile Prioritized System Complaint List for Clinical Staff]]'
confidence: medium
created: '2026-03-03'
janitor_note: LINK001 — Telia'z AI Clinical Platform wikilink is YAML escaping false
  positive (target likely exists). ORPHAN001 — No inbound links; synthesis record
  supports decision records and should be linked from project page.
name: Clinical System Complaints Cluster Around Data Loss and Authentication Not Performance
project:
- '[[project/Telia''z AI Clinical Platform]]'
related:
- '[[decision/Rebuild Clinic Management Platform from Scratch]]'
status: draft
supports:
- '[[decision/Three-Track Approach to Retool System Improvements]]'
- '[[decision/KPIs Are Primary Priority for Existing Retool System]]'
type: synthesis
---

# Clinical System Complaints Cluster Around Data Loss and Authentication Not Performance

## Insight

Across multiple sources documenting clinical staff complaints about the Retool platform, the highest-severity issues are data integrity failures and authentication lockouts — not performance or speed. Clinical summaries being deleted mid-writing (reported 3x by a single psychiatrist) and repeated authentication lockouts that force psychiatrists to restart sessions represent qualitatively different risks than slow page loads or delayed uploads. The pattern suggests prioritization should weight data integrity and access reliability above performance optimization.

## Evidence

- **2025-11-10 (Clinic Platform Discussion):** Shira relayed complaints including clinical summaries deleted mid-writing (3x by one psychiatrist), system freezing during sessions, slow page loads, and AI summary upload delays. The deletion issue was the most frequently reported and the most clinically impactful.
- **2025-12-05 (Retool Prioritization Discussion):** Shachar raised psychiatrist login lockouts from WhatsApp feedback. Rami confirmed authentication and KPIs as Track 1 critical priorities.
- **Existing constraint record:** Psychiatrist Authentication Issues Cause Repeated Workflow Disruptions — documents the ongoing access problem.
- **Task record:** Compile Prioritized System Complaint List — Shira tasked with creating a formal complaint registry, suggesting no systematic tracking exists.

## Implications

1. **Data integrity is a clinical safety issue, not just a UX problem.** Deleted clinical summaries mid-writing means lost clinical documentation that may need to be recreated from memory.
2. **Authentication lockouts waste billable session time.** When a psychiatrist is locked out during a patient session, both clinician and patient time is lost.
3. **Performance complaints (slow loads, delays) are tolerable annoyances** compared to data loss and access failures. Prioritization should reflect this severity hierarchy.
4. **The absence of formal complaint tracking** means the true frequency and severity distribution of these issues is unknown — the pattern observed is from informal channels only.

## Applicability

This pattern applies to the ongoing Retool maintenance (Track 1 of the three-track framework) and should inform the new system design (Track 2). The rebuilt platform must prioritize data persistence guarantees and authentication reliability over UI performance.
