---
name: gravity-sop-creator
description: "Creates Standard Operating Procedures (SOPs) that are pre-emptively stress-tested against operational reality. Uses a two-pass system: draft the SOP, then apply a 'Gravity' critique to expose blind spots and flawed assumptions before finalizing. Triggers on: create SOP, new SOP, write a standard operating procedure, SOP for, gravity SOP."
---

# Gravity-Oriented SOP Creator

This skill implements a robust, two-pass methodology for creating Standard Operating Procedures (SOPs) that are not just documented, but are resilient and grounded in reality. It forces a critical examination of every procedure to ensure it can survive contact with the real world.

## Core Philosophy: Draft, Critique, Finalize

Traditional SOPs often fail because they represent an idealized state that ignores the complexities and constraints of the actual work environment. This skill prevents that failure by embedding a devil's advocate directly into the creation process.

The workflow consists of three mandatory phases:

1.  **Phase 1: Draft the SOP.** Based on the user's request, create a clear, comprehensive draft of the SOP using the provided `templates/sop-template.md`.
2.  **Phase 2: Apply Gravity.** Activate a rigorous critique of the draft. This is not a simple review; it is an attack on the SOP's weakest points, guided by the `references/gravity-critique-protocol.md`.
3.  **Phase 3: Revise and Finalize.** Incorporate the findings from the Gravity critique to create a hardened, realistic final version of the SOP.

---

## Workflow

### Phase 1: Draft the SOP

1.  **Understand the Goal:** Clarify with the user the specific process that needs to be documented. What problem does it solve? Who are the primary users of this SOP?
2.  **Use the Template:** Read and copy the contents of `templates/sop-template.md` to a new file (e.g., `/home/ubuntu/sop_draft_v1.md`).
3.  **Flesh out the Draft:** Fill in all sections of the template. Be specific and detailed. Define owners, missions, and step-by-step procedures. Identify key metrics and potential risks.

### Phase 2: Apply Gravity (Critique the Draft)

This is the most critical phase. You will now switch from author to critic. Your objective is to find every reason this SOP will fail in practice.

1.  **Load the Protocol:** Read `references/gravity-critique-protocol.md`. This is your guide for the critique.
2.  **Ground in Context:** Following the protocol, query the Taliaz Knowledge Base (`taliaz-kb-query`) and BigQuery (`taliaz-bigquery-sql`) to gather evidence. Compare the idealized process in the SOP draft with the messy reality of past projects, actual responsibilities, and quantitative data.
3.  **Run Pre-Mortem:** Execute the `scripts/pre-mortem.py` script, passing in the title and description of the SOP. This will help structure your thinking around failure modes.
4.  **Synthesize the Critique:** Write a formal critique document (`/home/ubuntu/sop_critique.md`). Follow the structure outlined in the critique protocol: Assumption Attacks, Blind Spots, Pre-Mortem Analysis, and the One Uncomfortable Question.

### Phase 3: Revise and Finalize

1.  **Review the Critique:** Analyze the findings from your Gravity critique.
2.  **Strengthen the SOP:** Revise the initial draft (`sop_draft_v1.md`) to address the identified weaknesses. This may involve:
    *   Adding explicit steps to handle exceptions and edge cases.
    *   Clarifying roles and responsibilities to match reality.
    *   Building in feedback loops and review checkpoints.
    *   Acknowledging known constraints and providing workarounds.
3.  **Deliver the Final Product:** Present the final, hardened SOP to the user, explaining how the Gravity critique process made it more robust.

---

## Bundled Resources

| Resource | Description |
| :--- | :--- |
| `templates/sop-template.md` | A standardized template for creating new SOPs, ensuring all key sections are included. |
| `references/gravity-critique-protocol.md` | The core protocol for the devil's advocate review, adapted from the Gravity Agent. |
| `scripts/pre-mortem.py` | A script to facilitate a structured pre-mortem analysis, identifying likely causes of failure. |
