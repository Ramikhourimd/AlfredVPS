---
name: hebrew-pdf-extractor
description: Extract complex Hebrew text from PDFs (especially exams/forms) using a GPT-5.4 Vision-First Pipeline. Solves corrupted font encoding, RTL reversal, and character-level hallucinations. Use when asked to convert Hebrew PDFs to Markdown, extract text from Israeli medical/board exams, or fix corrupted digits/RTL text in PDFs.
---

# Hebrew PDF Extractor

This skill provides a comprehensive pipeline for extracting complex Hebrew text from PDFs, specifically designed to solve three major failure modes common in Israeli documents (medical exams, legal forms):

1. **Corrupted Font Encoding:** Digits and characters rendering incorrectly (e.g., `1` and `4` extracting as `0`).
2. **RTL Reversal:** Hebrew words mixed with English terms extracting in visual order instead of logical order.
3. **Character-Level Hallucinations:** Basic OCR confusing similar Hebrew letters (י vs ק, ה vs ח).

## Core Workflow

The extraction process involves three sequential steps:

1. **Extract Content (Vision-First)**
   Convert the PDF to high-resolution images and process page-by-page using GPT-5.4 Vision.
   ```bash
   python3 /home/ubuntu/skills/hebrew-pdf-extractor/scripts/extract_pdf.py <pdf_path> <output_json>
   ```

2. **Validate Extraction**
   Check the resulting JSON for completeness, missing items, or duplicates.
   ```bash
   python3 /home/ubuntu/skills/hebrew-pdf-extractor/scripts/validate_extraction.py <output_json> --expected <expected_count>
   ```

3. **Format to Markdown**
   Convert the structured JSON into a clean Markdown file with an HTML `<div>` wrapper to enforce proper RTL alignment in viewers.
   ```bash
   python3 /home/ubuntu/skills/hebrew-pdf-extractor/scripts/format_markdown.py <output_json> <output_md> --title "Document Title"
   ```

## Model Selection

By default, the extraction script uses `gpt-5.4` which provides the highest accuracy for Hebrew text. 

If you encounter API errors or need to optimize for cost, consult the model selection guide:
See [references/model-selection.md](/home/ubuntu/skills/hebrew-pdf-extractor/references/model-selection.md)

## Customizing the Extraction

The default system prompt is optimized for multiple-choice exams. For other document types, create a custom prompt file and pass it to the extraction script:

```bash
python3 /home/ubuntu/skills/hebrew-pdf-extractor/scripts/extract_pdf.py <pdf_path> <output_json> --prompt custom_prompt.txt
```

**Custom Prompt Requirements:**
- Must explicitly instruct the model to return a JSON array of objects.
- Must emphasize logical Unicode order for Hebrew text.
- Must warn against confusing similar Hebrew characters.

## Fallback Approach

If API-based vision models are completely unavailable, you can fall back to the legacy programmatic/OCR hybrid approach (pdfplumber + Tesseract + fuzzy merge). 

For instructions on this fallback method:
See [references/legacy-hybrid-approach.md](/home/ubuntu/skills/hebrew-pdf-extractor/references/legacy-hybrid-approach.md)
