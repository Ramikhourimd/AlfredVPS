---
cluster_sources:
- '[[conversation/AI Diagnostic Paper Research Meeting 2026-02-22]]'
- '[[conversation/AI Diagnostic Paper Review Meeting 2026-02-22]]'
- '[[task/Investigate Dataset Size Discrepancy Between Excel Exports]]'
- '[[task/Request Segmented Timing Data From Shmulik]]'
- '[[task/Clean Timing Data Outliers and Reconcile Dataset Discrepancy]]'
- '[[task/Create Methodology Figures for Record Analysis Stage]]'
confidence: high
created: '2026-03-31'
name: Research Paper Delivery Bottlenecked by Sequential Single-Person Dependencies
project:
- '[[project/Telia''z AI Diagnostic Research Paper]]'
related:
- '[[decision/Noam Assigned as Paper Compilation Lead and Statistical Methodology
  Authority]]'
- '[[synthesis/Action Item Fragmentation Across Duplicate Meeting Documentation]]'
status: draft
supports:
- '[[constraint/All Data Exports Depend on Single Provider Shmulik]]'
type: synthesis
---

# Research Paper Delivery Bottlenecked by Sequential Single-Person Dependencies

## Insight

The research paper production pipeline has four sequential single-person dependencies, each of which must complete before the next can proceed. No step can be parallelized because each person's output is the next person's input:

1. **Shmulik** (data exports) → sole provider of patient data from the clinical backend
2. **Noam** (statistics/compilation) → sole person cleaning data, computing statistics, compiling the document
3. **Rami** (AI pipeline analysis) → sole architect and operator of the diagnostic pipeline
4. **Dekkel** (strategic decisions) → sole authority on paper scope, split decisions, and publication strategy

## Evidence

- Multiple tasks blocked waiting on Shmulik for data exports (8-column timing breakdown, dataset discrepancy investigation)
- Noam must clean outliers and reconcile dataset discrepancy before any further statistical analysis
- Rami's AI prediction analysis covers only ~3,000 of ~6,000 records — scaling requires Rami's time
- Dekkel makes scope decisions (two-paper split, bias deferral) that redirect everyone's work
- The 2026-02-22 meeting generated 5+ tasks, each assigned to a single person with no backup
- Duplicate meeting documentation (4+ separate notes for one meeting) suggests coordination overhead from this serial structure

## Implications

- Any single person's unavailability blocks the entire paper timeline
- The paper cannot be accelerated by adding resources — each role requires specific domain knowledge
- Risk mitigation requires cross-training or documentation of each person's methodology
- The most fragile link is Shmulik (data exports) since he was not present at the meeting and all downstream work depends on his output

## Applicability

This pattern likely applies to other Telia'z research initiatives and any multi-disciplinary academic paper where roles are not interchangeable. Understanding this bottleneck structure should inform realistic timeline planning for Paper 2 and any future publications.

![[learn-synthesis.base#Sources]]
![[learn-synthesis.base#Related]]
