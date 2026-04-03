---
alfred_tags:
- employee-experience/research
- clinical/innovation
created: '2026-03-17'
description: Innovation team meeting covering Rivi overtime compensation, case manager
  training gaps during Ori reserve duty, complex patient characterization framework
  presentation with traffic-light triage model, Manus AI tool training, Optica template
  workflow, KPI prioritization, and innovation department strategic vision for clinical
  AI agents
name: Innovation Team Meeting Clinical Workloads AI Tools and Complex Patient Framework
  2026-03-17
project: '[[project/Telia''z Innovation Program]]'
related:
- '[[person/Rivi Idelman]]'
- '[[person/Rami Khouri]]'
- '[[person/Ohad Edri]]'
- '[[person/Basel Kanaaneh]]'
- '[[person/Ori Shukron]]'
- '[[person/Stav Zamir]]'
- '[[org/Telia''z]]'
- '[[project/Telia''z Clinic Israel]]'
- '[[project/Telia''z AI Clinical Platform]]'
- '[[conversation/Innovation Team Meeting Clinical Workloads and AI Tools 2026-03-17]]'
- '[[task/Define Complex Patient Protocol Criteria]]'
- '[[decision/Require Literature Review Before Complex Patient Feature Development]]'
relationships: []
session: null
status: active
subtype: meeting-notes
tags: []
type: note
---

# Innovation Team Meeting: Clinical Workloads, AI Tools and Complex Patient Framework 2026-03-17

## Context

Weekly innovation team meeting between Rivi Idelman (researcher), Rami Khouri (innovation lead), and Ohad Edri (AI engineer). The meeting covered multiple operational and strategic topics spanning clinical workload management, employment contracts, training gaps, the complex patient characterization project, AI tooling, and innovation department strategy.

## 1. Rivi Overtime Compensation Issue

Rivi worked 1.5 extra clinical hours beyond her contracted 20 hours in February 2026 but was not compensated. The current employment contract does not clearly address overtime for clinical hours. Rami acknowledged this was a miss — Basel's automated payroll system cannot currently detect overtime automatically.

**Resolution:** Rivi will log extra hours via email to Basel. Rami will approve them as overtime. February will be retroactively compensated. Going forward, Rivi should note any hours beyond 20 in writing.

**Underlying tension:** Rivi opens extra time slots out of concern for her patients who otherwise wait months for follow-up appointments. This creates a conflict between patient care and contractual boundaries.

## 2. Patient Capacity and Follow-Up Bottleneck

Rivi raised that she continues receiving new intake patients despite having insufficient availability for follow-ups. Some patients wait 7+ months for their next appointment with her. She has been informally opening extra slots for continuity of care.

Rami suggested Rivi may need to stop accepting new patients entirely, since the intake-to-follow-up ratio is unsustainable without additional hours. Rivi acknowledged this is a systemic issue across the clinic, not unique to her.

**Connection to Basel's discharge model:** Rivi referenced Basel's patient lifecycle plan with expected discharge percentages at time intervals. She expressed concern that a time-limited treatment model could alienate staff who want long-term therapeutic relationships.

## 3. Case Manager Training Gaps

Rivi reported that psychiatrist training sessions are on hold due to reserve duty (milluim). More critically, case manager training and supervision under Ori Shukron has gaps:
- New employees (e.g., Muli Abrikan and others) reported they received no onboarding orientation to the clinic
- An Excel template for case presentations hasn't been redistributed to new joiners
- Ori hasn't sent out training reminders consistently

Rivi felt it wasn't her place to manage Ori but wanted to flag the issue. Rami agreed to raise it with Basel rather than intervening directly, preserving Basel's management authority.

## 4. Employment Contract Clause Concerns

Rivi flagged a clause in her employment contract requiring her to acknowledge familiarity with all relevant state laws, Maccabi/Clalit regulations, and policy changes. She is uncomfortable signing something she cannot realistically know.

Rami explained the practical meaning: the company commits to informing her of relevant regulations; she commits to following them. He invited Rivi to propose alternative wording that captures the same intent without the over-broad knowledge claim.

## 5. Optica Template and Notion Workflow Training

Rami demonstrated how to use the Optica innovation project template in Notion:
- Templates have two versions (long and short)
- Rivi should duplicate the template and fill in responses per chapter
- Projects should track through the Optica pipeline stages
- Rivi and Ohad/Stav should schedule a joint session to align on template usage

**Key takeaway:** All innovation projects must follow the Optica template framework. Rivi's complex patient project should be documented per chapters 1 and 2 of the full template.

## 6. Complex Patient Characterization Framework Presentation

Rivi presented her research on defining "complex patients" for the clinic. Sources included psychiatrist feedback, WhatsApp/Slack group analysis, Manus AI literature review, and international clinic screening models.

### Core Problem
Psychiatrists face unpredictable complex cases in 30-minute telehealth slots without adequate preparation, documentation, or escalation pathways. This causes moral injury (treating below desired standard) and professional risk (licensing concerns).

### Key Definition
"Complex" is defined relative to the clinic's capabilities (telepsychiatry, remote, limited session time) — not objectively in clinical terms.

### Proposed Traffic-Light Triage Model (5 Dimensions)

**Dimension 1: Clinical Severity and History**
- Green: Moderate symptoms, no suicidality history
- Yellow: Prior voluntary hospitalizations, extensive treatment history
- Red: Involuntary hospitalizations, suicide attempts, active psychosis, frequent ER visits

**Dimension 2: Psychosocial Stability**
- Green: Stable housing, support network
- Yellow: Significant stressors, unstable housing
- Red: Homelessness, domestic violence, needs comprehensive rehabilitation

**Dimension 3: Patient Compliance and Engagement**
- Green: Willing to sign informed consent, participates actively
- Yellow: Partial compliance, substance use issues
- Red: Active untreated substance use, treatment refusal

**Dimension 4: Comorbidities**
- Green: Manageable psychiatric condition
- Yellow: Multiple psychiatric conditions or medical comorbidities requiring coordination
- Red: Complex multi-system medical issues with no communication pathway to other providers

**Dimension 5: Documentation and Technology Access**
- Green: Full documentation provided, tech-capable
- Yellow: Partial documentation gaps
- Red: Critical missing records, cannot use basic technology, language barrier requiring external interpreter

### Proposed Workflow
1. **Pre-screening questionnaires** flag high-risk scores automatically
2. **Green across all dimensions:** Standard intake with psychiatrist
3. **Yellow on any dimension:** Consult clinical director; extended 45-minute intake
4. **Red on any dimension:** Automatic flag; clinical director review; decision to accept with modifications or refer externally

### Action Items from Rami
- Research Israeli Patient Rights Law regarding withholding treatment for missing documentation (legal/ethical analysis needed)
- Complete full Optica template chapters 1 and 2 with comprehensive document
- Build a front-end prototype using Manus AI
- Present completed work to Rami, Adi (marketing), and Adiel (business) before moving to phase 2
- Monthly gate meetings with business and marketing stakeholders

## 7. Manus AI Tools Training

Rami trained Rivi on Manus AI connectors and skills:

**Active connectors for Rivi:**
- Internal data (first connector — company data)
- Google Gemini (LLM for cost savings)
- Browser (for live research with human intervention capability)
- Notion (for reading/writing project data)
- Slack (innovation team channels)
- Supabase (company knowledge base)
- Perplexity (on-demand for research, not auto-activated)

**Disconnected:** GitHub, Monday.com

**Key skills introduced:**
- **Skill Creator:** Build custom automated workflows
- **Creative Seeds:** Surrealist ideation tool — takes ideas through creative expansion then grounds them back in reality. ~50% hit rate but produces novel insights.
- **Gravity:** Post-mortem analysis tool — finds failure scenarios based on company knowledge base. Useful for stress-testing proposals.

**Workflow recommendation:** Use Creative Seeds first (ideation), then Gravity (critique), then finalize.

**Migration plan:** Rami plans to migrate from Manus to Claude Desktop for the team in the future.

## 8. KPI Discussion

Rivi wants to advance KPI work using validated questionnaires for patient satisfaction and staff satisfaction. She sees this as directly relevant to innovation work (measuring impact of changes).

Rami advised:
- KPIs should be broken into multiple sub-projects (clinical KPIs, operational KPIs, satisfaction KPIs)
- Complex patient project takes priority
- KPIs are important but should not be treated as a single monolithic project
- Maximum 3 active projects at a time for Rivi

## 9. Innovation Department Strategic Vision

Rami outlined the larger vision for the innovation department:
- Building a smart system that optimizes three domains: **collecting** clinical information, **analyzing** it, and **presenting** it to decision-makers
- Architecture: multiple AI agents working in parallel, some real-time during sessions, some running continuously in background
- Each innovation project (complex patient screening, KPIs, etc.) maps onto this spectrum
- Behind the chatbot: full live communication between all clinical actors
- Three agent archetypes: collector (gathers all data), analyzer (fastest/smartest processing), presenter (displays to decision-maker)

**Strategic framing:** Innovation team's responsibility extends beyond current operational needs — the goal is to create unique value that drives company valuation at exit. Operational fixes are R&D/product team's responsibility; innovation adds differentiated IP.

## Related
![[related.base#All]]