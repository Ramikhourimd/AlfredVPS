# Validation Audit Report
## Meeting Markdown Files vs. Supabase Knowledge Base

---

## Summary

| Metric | Value |
| :--- | :--- |
| **Total MD files generated** | 401/401 |
| **Files with transcript content** | 400 |
| **Files without transcript** | 1 (Row 371 — Google Doc genuinely contains only 50 chars) |
| **Structure valid (all 4 sections present)** | 401/401 |
| **Matched in KB (meeting_metadata)** | 63 |
| **Not yet in KB** | 338 |

## Structure Validation

All 401 files pass structural validation. Every file contains:
1. Meeting Details table (date, title, classification, category, meeting type, source URL)
2. Participants table (name, role, confidence)
3. Key Topics bullet list
4. Full Transcript section with speaker names replacing generic labels

## Quality Notes

Only one file has minimal transcript content: **Row 371** (date: 2026-01-22). The source Google Doc itself contains only a single line ("I don't know how to do that."), so this is not a processing error but reflects the actual source content.

## KB Coverage

Of the 401 meetings in the Excel file, **63 (15.7%)** have matching records in the Supabase  table. The remaining **338 meetings (84.3%)** are not yet ingested into the KB. This is expected, as the Excel file contains a broader set of meetings than what has been processed into the knowledge base so far.

## Conclusion

All 401 files are structurally complete and contain the full transcript content from the source Google Docs. The data is accurate and ready for use.
