---
name: hebrew-pdf-generator
description: Generate professionally formatted Hebrew RTL PDF files from translated chapter markdown files, with full figure extraction from original English PDFs. Produces medical textbook styling with proper typography, tables, clinical vignettes, images, and section hierarchy. Use when asked to create a Hebrew PDF from a markdown chapter, format a translated chapter as PDF, generate a textbook-style Hebrew PDF, convert Hebrew markdown to PDF, or add figures/images from an original PDF to a Hebrew translation. Triggers on requests like "create PDF from chapter", "generate Hebrew PDF", "format this chapter as PDF", "textbook PDF", "convert markdown to Hebrew PDF", "add figures from original", "extract images from English PDF".
---

# Hebrew PDF Generator

Generate publication-quality Hebrew RTL PDFs from translated markdown chapter files, with optional figure extraction from original English PDFs. Designed for the Kaplan & Sadock translation project.

## Prerequisites

```bash
sudo apt-get install -y -qq fonts-noto-core fonts-noto-extra poppler-utils 2>/dev/null
pip3 show weasyprint >/dev/null 2>&1 || sudo pip3 install weasyprint
```

## Workflow Overview

Two workflows depending on whether the original English PDF with figures is available:

**Markdown only?** → Run `generate_hebrew_pdf.py` directly (Step 3 below).
**Original PDF available?** → Full pipeline: Extract → Map → Inject → Generate (Steps 1-4).

### Full Pipeline (with figures)

1. Extract figures from original PDF (`extract_and_inject_figures.py`)
2. Map figures to Hebrew markdown locations (edit manifest JSON)
3. Inject figures into Hebrew markdown (`extract_and_inject_figures.py --inject`)
4. Generate PDF (`generate_hebrew_pdf.py`)

### Step 1: Extract Figures

```bash
python /home/ubuntu/skills/hebrew-pdf-generator/scripts/extract_and_inject_figures.py \
  <original_pdf> <hebrew_md> <output_md> \
  --figures-dir <dir> --manifest <manifest.json>
```

| Argument | Required | Description |
|----------|----------|-------------|
| `original_pdf` | Yes | Original English PDF with figures |
| `hebrew_md` | Yes | Hebrew translated markdown |
| `output_md` | Yes | Path for enriched output markdown |
| `--figures-dir` | No | Directory for extracted images (default: `./figures/`) |
| `--manifest` | No | Path for JSON manifest (default: `./figure_manifest.json`) |
| `--min-size` | No | Min pixel dimension for real figures (default: 200) |

This extracts all images, filters artifacts, and generates a manifest JSON for mapping.

### Step 2: Map Figures

The manifest JSON contains an array of extracted figures. For each figure:

1. **View the original PDF** at the listed page to identify what the image is
2. **Fill in these fields** in the manifest:
   - `label`: Figure/table number (e.g., `"FIGURE 1-1"`, `"Table 1-12"`)
   - `caption_he`: Hebrew caption
   - `caption_en`: English attribution
   - `category`: `"figure"` or `"table_image"`
   - `insert_after`: Unique text snippet from the Hebrew markdown (the figure is inserted after the line containing this text)
   - OR `replace_placeholder`: Exact `![...]()` text to replace if the markdown already has a placeholder

For detailed mapping guidance, read `references/figure-mapping-guide.md`.

### Step 3: Inject Figures

```bash
python /home/ubuntu/skills/hebrew-pdf-generator/scripts/extract_and_inject_figures.py \
  <original_pdf> <hebrew_md> <output_md> \
  --manifest <manifest.json> --inject
```

### Step 4: Generate PDF

```bash
python /home/ubuntu/skills/hebrew-pdf-generator/scripts/generate_hebrew_pdf.py \
  <input_md> <output_pdf> [--chapter NUM] [--debug]
```

| Argument | Required | Description |
|----------|----------|-------------|
| `input_md` | Yes | Hebrew markdown (enriched with figures, or plain) |
| `output_pdf` | Yes | Output PDF path |
| `--chapter` | No | Chapter number (auto-detected from content/filename) |
| `--debug` | No | Save intermediate HTML for inspection |

## Expected Markdown Format

- `# Title` — Chapter title (H1). First H1 renders as chapter header; subsequent H1s with numbers (e.g., `# 1.2 ...`) render as sub-chapter headers; unnumbered H1s render as major section dividers
- `## Section` — Major sections (H2), bold blue
- `### Subsection` — Subsections (H3), lighter blue
- `### טבלה X-Y. Title` — Table titles (auto-detected by `טבלה` prefix)
- `| col1 | col2 |` — Markdown pipe tables with header separator
- `![alt text](/path/to/image.jpg)` — Images, rendered as centered figures with captions
- `*(באדיבות ...)` — Attribution lines, merged into preceding vignette box
- Clinical vignettes auto-detected by heuristic patterns
- `**Bold term.** Rest of paragraph` — Inline heading style

## Design Specification

- **Page**: A4, 2.2cm/2.5cm margins, page numbers at bottom center
- **Fonts**: Noto Serif Hebrew (body), Noto Sans Hebrew (headings, tables)
- **Colors**: Blue `#0077B6` headings, dark blue-gray `#4A6274` table headers
- **Chapter header**: 72pt number, 22pt title, blue rule (first H1 only)
- **Sub-chapter headers**: 36pt number, 18pt title (numbered H1s after the first)
- **Major sections**: 20pt title with blue top border (unnumbered H1s after the first)
- **Figures**: Centered, max-width 90%, with caption below
- **Clinical vignettes**: Light gray `#EBEEF2` background boxes
- **Tables**: Dark header with white text, alternating rows

## Batch Processing

```bash
for md in /path/to/hebrew_chapters/*.md; do
  base=$(basename "$md" .md)
  python /home/ubuntu/skills/hebrew-pdf-generator/scripts/generate_hebrew_pdf.py \
    "$md" "/path/to/output/${base}.pdf"
done
```

## Customization

Edit `templates/textbook.css` to modify visual design. Key CSS classes: `.chapter-number`, `.section-heading`, `.clinical-vignette`, `.data-table`, `.figure-container`, `.figure-image`, `.figure-caption`.

## Troubleshooting

**Missing fonts**: `sudo apt-get install -y fonts-noto-core fonts-noto-extra`

**pdfimages not found**: `sudo apt-get install -y poppler-utils`

**Figures not appearing**: Verify image paths in the markdown are absolute paths. Use `--debug` flag to inspect the HTML.

**Vignette not detected**: Wrap in blockquote (`>`) in the markdown source.

**Large tables cause blank pages**: Expected WeasyPrint behavior for print-quality output.

**Chapter number repeating**: Only the first H1 renders as a chapter header. Subsequent H1s render as sub-chapter or section headers. If the markdown has multiple `# N` headings, only the first gets the large number treatment.
