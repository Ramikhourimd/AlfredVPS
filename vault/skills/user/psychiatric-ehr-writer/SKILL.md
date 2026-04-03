---
name: psychiatric-ehr-writer
description: Write psychiatric EHR (Electronic Health Records) documentation for Dr. Rami Khouri's patients. Use this skill whenever asked to write, draft, create, or generate a psychiatric health record, clinical note, EHR, תיעוד פסיכיאטרי, רשומה רפואית, or any clinical documentation based on a patient file and/or meeting transcript. Triggers on requests like "write an EHR for this patient", "draft a clinical note", "document this session", "כתוב רשומה רפואית", "תעד את הפגישה", or any request combining a patient file + transcript + documentation task. Always use this skill when clinical documentation is involved — even if the user doesn't say "EHR" explicitly.
---

# Psychiatric EHR Writer

Generate structured psychiatric health records (EHR) for Dr. Rami Khouri's patients, in the patient's language (Hebrew/Arabic/English). Supports both **intake** and **followup** record types, with an optional **Decision Support Section (DSS)**.

---

## Step 1 — Gather Inputs

You need up to two things:
1. **Patient medical file / history** — provided as pasted text or attached PDF/image
2. **Meeting transcript** — provided as pasted text (optional at first)

### If NO transcript is provided:
Do **not** ask for one immediately. Instead, treat this as a **pre-session review request** — Dr. Khouri wants a structured overview of the patient before the meeting.

Produce a **Pre-Session Patient Review** (see Step 3b below), then end with:
> "כשתהיה מוכן, שלח את תמליל הפגישה ואוכל לכתוב את הרשומה הרפואית המלאה."
> *(When you're ready, send the meeting transcript and I'll draft the full EHR.)*

### If transcript IS provided (at any point):
Proceed to Step 2 and write the full EHR record.

---

## Step 2 — Language

**Always write the entire output in Hebrew (עברית)**, regardless of the language of the patient file, transcript, or any other input.

---

## Step 3b — Pre-Session Patient Review (no transcript)

Write a structured clinical review to help Dr. Khouri prepare for the session. All sections are narrative paragraphs — no bullets.

**1. סקירה דמוגרפית / Demographic Snapshot**
Full name, ID, age, gender, family status, occupation, living situation — written as a brief narrative sentence.

**2. היסטוריה פסיכיאטרית / Psychiatric History**
A chronological narrative of the patient's psychiatric journey: past diagnoses, hospitalizations, crisis events, significant turning points.

**3. טיפולים קודמים / Treatment History**
Narrative summary of past pharmacological and psychological treatments: what was tried, what worked, what didn't, reasons for changes.

**4. תרופות נוכחיות / Current Medications**
Current regimen written as a prose sentence, including doses if documented.

**5. נקודות מפתח קליניות / Key Clinical Themes**
A synthesizing paragraph identifying the most clinically significant patterns: recurring themes, risk factors, protective factors, treatment-resistant elements, and anything the psychiatrist should hold in mind during the session.

**6. שאלות פתוחות / Open Clinical Questions**
One paragraph noting gaps in the file, unresolved diagnostic questions, or areas worth exploring in the upcoming session.

Then close with a prompt for the transcript (in the patient's language).

---

## Step 4 — Determine Record Type

Search the patient file for any prior visit documented by **Dr. Rami Khouri (דר ראמי חורי / د. رامي خوري)**. Look for his name in previous records, signatures, or encounter notes.

- **If a prior record by Dr. Khouri exists** → write a **Followup Record**
- **If no prior record by Dr. Khouri exists** → write an **Intake Record**

---

## Step 5 — Write the Record

### CRITICAL FORMATTING RULE
**Every section must be a single flowing narrative paragraph. No bullet points. No numbered lists. No sub-headers within sections. Pure prose only.**

---

### FOLLOWUP RECORD — Section Structure

**1. פרטים אישיים / Personal Information**
Write as a short narrative sentence: full name, ID number, gender, age.

**2. רקע אישי קצר / Brief Personal Demographics**
One paragraph covering personal background: family status, occupation, living situation, relevant social context.

**3. סיכום פגישה קודמת / Recap of Last Visit with Dr. Khouri**
One paragraph summarizing the key points from the most recent prior visit documented by Dr. Khouri: presenting complaints, diagnoses raised, medications prescribed, and plan discussed.

**4. סיכום הפגישה הנוכחית / Summary of Current Meeting**
One detailed paragraph covering: subjective information reported by the patient, current symptoms, changes since last visit, medication response and side effects, relevant life changes.

**Mandatory elements to address explicitly in this paragraph:**
- **Suicidality**: state either that the patient reported suicidal ideation/intent/plan, or explicitly state that suicidal ideation was denied/absent
- **Psychosis**: state either that psychotic symptoms were present, or explicitly state that psychotic symptoms were denied/absent

**5. בדיקת מצב נפשי / Mental Status Examination**
One paragraph covering: appearance and behavior, mood and affect, speech, thought process and content, perceptual disturbances, cognition, insight and judgment.

**6. סיכום ודיון / Summary and Discussion**
One paragraph integrating the clinical picture: working diagnosis, clinical reasoning, response to treatment, relevant formulation.

**7. המלצות / Recommendations**
One narrative paragraph covering all of the following (weave them together as prose):
- **Psychopharmacological**: medications, doses, instructions, rationale
- **Psychological**: if mentioned in the transcript; omit if not
- **Social/occupational**: if mentioned in the transcript; omit if not
- **General medical**: if mentioned in the transcript; omit if not
- **Follow-up timing**: use what is stated in transcript; if not stated, default to 3 months

---

### INTAKE RECORD — Section Structure

Same sections as Followup, with these differences:

**3. רקע / Background** (replaces "Recap of Last Visit")
One thorough paragraph covering: reason for referral, psychiatric history (past diagnoses, hospitalizations, previous treatments), medical history, family psychiatric history, developmental history, social and occupational history, substance use.

**6. סיכום ודיון / Summary and Discussion**
More detailed than followup: include differential diagnosis, clinical formulation, risk assessment, and initial treatment rationale.

**7. המלצות / Recommendations**
More detailed than followup: include a clear treatment plan with rationale, not just brief instructions.

---

## Step 6 — Decision Support Section (DSS)

**Only include if explicitly requested by the user** (e.g., "add DSS", "include decision support", "add the clinical tips section").

If requested, add this section **after** the main record:

---

**⚕️ Decision Support — Personalized Clinical Insights**
*(This section is for the treating psychiatrist and is not part of the official medical record)*

Write **5 clinical insights/tips** tailored specifically to this patient's unique profile — integrating their demographics, background, symptom pattern, life context, and medical history. These should be actionable, non-obvious, and go beyond standard textbook recommendations. They may address psychopharmacology, psychotherapy modality fit, social interventions, lifestyle factors, cultural considerations, family dynamics, or any domain relevant to this patient's recovery.

Each insight is written as a flowing sentence or short paragraph — no bullets or numbers.

Then end with **one closing statement** addressed to the psychiatrist to use (or adapt) when speaking directly to the patient. It should:
- Make the patient feel genuinely seen and understood as an individual
- Offer real, specific hope grounded in their particular story
- Avoid clichés ("you're not alone", "things will get better") that feel generic
- Never sound patronizing or therapist-scripted

---

## Step 7 — Quality Checks Before Outputting

- [ ] Record type is correct (intake vs followup) based on Dr. Khouri's prior presence in the file
- [ ] All sections are narrative paragraphs — no bullets or lists anywhere
- [ ] Suicidality and psychosis are explicitly addressed in the Current Meeting section
- [ ] Language matches the patient's primary language
- [ ] DSS included only if requested
- [ ] Recommendations include follow-up timing (stated or defaulted to 3 months)
