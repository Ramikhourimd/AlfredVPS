---
name: psychiatric-letter-generator
description: Generates professional psychiatric session letters (intake or follow-up) in Hebrew. Consumes a session transcript, prior documents (intake/follow-up), and other medical records to produce a structured, aesthetically polished RTL PDF letter, including the doctor's stamp.
---

# Psychiatric Letter Generator Skill

This skill automates the creation of professional psychiatric summary letters in Hebrew, for both initial (intake) and follow-up sessions. It processes patient documents and a session transcript to generate a high-quality, right-to-left (RTL) formatted PDF, ready to be sent to the patient or other entities.

## Core Workflow

The process is broken down into five main steps. Follow them sequentially.

1.  **Analyze Inputs & Classify Session Type**: Read and understand the provided files to determine if this is an Intake or a Follow-up session.
2.  **Extract Doctor's Stamp**: Locate and extract the doctor's stamp/signature image from a previous document.
3.  **Synthesize Letter Content**: Extract key information from all source documents and synthesize it into a structured Markdown file (`letter_content.md`).
4.  **Generate PDF from Content**: Use a Python script and an HTML/CSS template to convert the Markdown content into a polished, RTL-formatted PDF.
5.  **Final Review**: Verify the generated PDF for correctness, formatting, and completeness.

---

### Step 1: Analyze Inputs & Classify Session Type

First, you must be provided with the necessary documents:
*   A transcript of the current session.
*   A previous document from the same doctor (e.g., `intake_summary.pdf`, `previous_follow_up.pdf`). This is crucial for classification and for extracting the stamp.
*   (Optional) Other medical records.

**Read all provided text-based documents (`.txt`, `.md`) and view PDF documents to understand their contents.**

**Classification Logic:**

*   **It is a Follow-up session if:**
    *   The user explicitly states it's a "follow-up" (מעקב).
    *   A previous document *written by the same doctor* is provided. Look for the doctor's name or stamp.
    *   The transcript contains phrases like "since our last meeting" or refers to past recommendations.
*   **It is an Intake session if:**
    *   The user explicitly states it's an "intake" (אינטייק) or "first meeting" (פגישה ראשונה).
    *   No prior documents from the same doctor are available.

The final letter's title and some section content will change based on this classification (e.g., "מכתב סיכום אינטייק" vs. "מכתב מעקב פסיכיאטרי").

### Step 2: Extract Doctor's Stamp

To ensure authenticity, the doctor's stamp must be included. It must be extracted from the prior document provided by the user.

1.  **Identify the source PDF**: This will be the previous intake or follow-up letter.
2.  **Run the extraction script**: Use the bundled Python script to automatically find and crop the stamp.

    ```bash
    # Usage: python <script_path> <source_pdf_path> <output_image_path>
    python /home/ubuntu/skills/psychiatric-letter-generator/scripts/extract_stamp.py /path/to/intake.pdf /home/ubuntu/stamp.png
    ```

3.  **Verify the output**: Use `file` tool with `view` action on `/home/ubuntu/stamp.png` to ensure the stamp was extracted cleanly. If it fails, you may need to revert to manual extraction using `pdf2image` and `Pillow` as was done previously.

### Step 3: Synthesize Letter Content

This is the core clinical reasoning step. Read through all the provided materials and synthesize the information into a single, comprehensive Markdown file named `/home/ubuntu/letter_content.md`.

The structure should follow the standard psychiatric letter format. Use the following Markdown template. **Fill in every section based on the source documents.**

````markdown
# Patient Name: [Patient's Full Name]
# Patient ID: [Patient's ID Number]
# Patient Age: [Patient's Age]
# Doctor Name: [Doctor's Full Name]
# Doctor Title: [Doctor's Title]
# Doctor Contact: [Doctor's Address | Phone | Email]
# Date: [Date of current session, DD/MM/YYYY]

---

## פרטים דמוגרפיים:
[Synthesized content...]

## סיבת פנייה:
[For Intake: Why the patient came initially. For Follow-up: Note that it's a follow-up and describe the reason for the current session, e.g., worsening of symptoms.]

## מחלה נוכחית וסימפטומים:
[Detailed description of current symptoms: anxiety, post-trauma, depression, functional impact, etc.]

## רקע אישי ופסיכיאטרי:
[History of treatment, previous diagnoses, family history.]

## תולדות חיים:
[Patient's life story, education, military service, work, relationships.]

## רקע גופני:
[Physical health, chronic illnesses, medications, test results.]

## בדיקה פסיכיאטרית (סטטוס):
[Mental status examination findings: appearance, behavior, speech, thought process, mood, affect, etc.]

## אבחנה:
*   **F43.1** – הפרעת דחק פוסט-טראומטית (PTSD)
*   **F41.2** – הפרעה משולבת דיכאונית-חרדתית
*   [Add/remove diagnoses with ICD-10 codes as appropriate]

## דיון וסיכום:
[Clinical summary and discussion, integrating all the information.]

## המלצות:

### 1. טיפול תרופתי:
*   **[Drug Name]**: [Dosage and instructions].
*   ...

### 2. חופשת מחלה:
*   [Recommendation for sick leave, including duration.]

### 3. המלצות למוסד האקדמי:
*   [Specific accommodations for the college/university.]

### 4. טיפול פסיכולוגי:
*   [Recommendation for therapy.]

### 5. המלצות נוספות:
*   [Lifestyle, behavioral recommendations.]

### 6. מעקב:
*   [Plan for the next follow-up meeting.]
````

### Step 4: Generate PDF from Content

Once `/home/ubuntu/letter_content.md` is complete and the stamp is at `/home/ubuntu/stamp.png`, use the `generate_pdf.py` script to create the final document.

This script reads the Markdown file, injects the content into a beautiful HTML template, and uses `weasyprint` with proper font handling to render a perfect RTL PDF.

```bash
# Usage: python <script_path> <content_md_path> <stamp_image_path> <output_pdf_path>
python /home/ubuntu/skills/psychiatric-letter-generator/scripts/generate_pdf.py /home/ubuntu/letter_content.md /home/ubuntu/stamp.png "מכתב_פסיכיאטרי.pdf"
```

**CRITICAL:** The script handles all the complexities of Hebrew PDF generation you dealt with previously:
*   Embedding Hebrew fonts (`Noto Sans Hebrew`).
*   Forcing RTL layout in the CSS.
*   Structuring the HTML for a professional look.
*   Placing the stamp correctly at the end of the document.

### Step 5: Final Review

Use the `file` tool with the `view` action to do a final quality check on the generated PDF (`מכתב_פסיכיאטרי.pdf`).

**Checklist:**
1.  Is the text entirely in Hebrew and correctly aligned to the right?
2.  Are all sections present and correctly populated?
3.  Does the document flow correctly across pages (e.g., no single line of a paragraph on a new page)?
4.  Is the doctor's stamp visible and correctly placed at the very end?
5.  Is the overall aesthetic professional and clean?

If there are any issues, you may need to debug by checking the source `letter_content.md` for errors or, in rare cases, adjusting the `templates/letter_template.html` file.
