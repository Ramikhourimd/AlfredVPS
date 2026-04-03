#!/usr/bin/env python3
"""
omi_to_alfred.py — Export Omi transcription sessions from omi.db into the
Alfred vault inbox as markdown input records.

Usage:
    python3 scripts/omi_to_alfred.py

The script is idempotent: it skips sessions that already have a file in the
inbox directory (matched by filename).
"""
from __future__ import annotations

import json
import os
import re
import sqlite3
import sys
from datetime import datetime, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

# Walk the omi user-data directory to find the real database (the top-level
# omi.db is an empty placeholder).
_OMI_BASE = Path.home() / "Library" / "Application Support" / "omi"
_DB_CANDIDATES = sorted(_OMI_BASE.rglob("omi.db"), key=lambda p: p.stat().st_size, reverse=True)
DB_PATH = next((p for p in _DB_CANDIDATES if p.stat().st_size > 0), None)
if DB_PATH is None:
    sys.exit("ERROR: Could not find a non-empty omi.db under " + str(_OMI_BASE))

VAULT_ROOT = Path(__file__).resolve().parent.parent        # …/Taliaz
INBOX_DIR = VAULT_ROOT / "inbox"

LOCAL_TZ = ZoneInfo("Asia/Jerusalem")

SLUG_MAX_LEN = 60


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def slugify(title: str) -> str:
    """Convert a title to a filename-safe slug.

    Replaces spaces with hyphens, strips characters that are not
    word-chars / hyphens / Unicode letters, and truncates to SLUG_MAX_LEN.
    """
    # Replace whitespace runs with a single hyphen
    slug = re.sub(r"\s+", "-", title.strip())
    # Remove characters that are not Unicode word chars or hyphens
    # (this keeps Hebrew, Arabic, Latin letters, digits, underscores, hyphens)
    slug = re.sub(r"[^\w\-]", "", slug, flags=re.UNICODE)
    # Collapse multiple hyphens
    slug = re.sub(r"-{2,}", "-", slug)
    # Strip leading/trailing hyphens
    slug = slug.strip("-")
    # Truncate
    if len(slug) > SLUG_MAX_LEN:
        slug = slug[:SLUG_MAX_LEN]
        # Don't end on a trailing hyphen after truncation
        slug = slug.rstrip("-")
    return slug


def format_filename(started_at: str, title: str) -> str:
    """Build the output filename from the UTC startedAt timestamp and title."""
    # Parse the DB timestamp (UTC)
    dt = _parse_db_datetime(started_at)
    ts_part = dt.strftime("%Y%m%d %H%M%S")
    slug = slugify(title)
    return f"omi_{ts_part}_{slug}.md"


def _parse_db_datetime(raw: str) -> datetime:
    """Parse a datetime string from the database.

    Handles both '2026-03-10 12:31:04.105' and '2026-03-10 12:31:04' forms.
    The DB stores UTC.
    """
    raw = raw.strip()
    for fmt in ("%Y-%m-%d %H:%M:%S.%f", "%Y-%m-%d %H:%M:%S"):
        try:
            return datetime.strptime(raw, fmt).replace(tzinfo=timezone.utc)
        except ValueError:
            continue
    raise ValueError(f"Cannot parse datetime: {raw!r}")


def utc_to_local(dt: datetime) -> datetime:
    """Convert a UTC datetime to Asia/Jerusalem."""
    return dt.astimezone(LOCAL_TZ)


def format_iso(dt: datetime) -> str:
    """Format as ISO-8601 without timezone suffix (for YAML frontmatter)."""
    return dt.strftime("%Y-%m-%dT%H:%M:%S")


def format_display_date(dt: datetime) -> str:
    """Human-readable date string for the body of the note."""
    return dt.strftime("%Y-%m-%d %H:%M:%S")


def parse_action_items(raw_json: str | None) -> list[str]:
    """Extract action-item descriptions from the JSON column."""
    if not raw_json or not raw_json.strip():
        return []
    try:
        items = json.loads(raw_json)
    except (json.JSONDecodeError, TypeError):
        return []
    descriptions = []
    for item in items:
        if isinstance(item, dict):
            desc = item.get("description", "").strip()
            if desc and not item.get("deleted", False):
                descriptions.append(desc)
    return descriptions


def build_transcript(segments: list[dict]) -> str:
    """Format transcript segments as speaker-labeled lines."""
    lines: list[str] = []
    for seg in segments:
        label = seg["speakerLabel"] or f"SPEAKER_{seg['speaker']}"
        text = (seg["text"] or "").strip()
        if text:
            lines.append(f"**{label}:** {text}")
    return "\n".join(lines)


def build_markdown(session: dict, segments: list[dict]) -> str:
    """Build the full markdown content for an input record."""
    started_utc = _parse_db_datetime(session["startedAt"])
    started_local = utc_to_local(started_utc)

    title = session["title"]
    source = session["source"] or "omi"
    category = session["category"] or "uncategorized"
    emoji = session["emoji"] or ""
    overview = (session["overview"] or "").strip()
    action_items = parse_action_items(session["actionItemsJson"])

    # --- YAML frontmatter ---
    iso_received = format_iso(started_local)
    iso_created = format_iso(started_local)

    tags_list = ["omi"]
    if category and category != "uncategorized":
        tags_list.append(category)

    tags_yaml = "\n".join(f"  - {t}" for t in tags_list)

    frontmatter = f"""---
type: input
status: unprocessed
input_type: transcript
source: omi
received: "{iso_received}"
created: "{iso_created}"
from: "Omi Recording"
category: {category}
omi_session_id: {session['id']}
tags:
{tags_yaml}
---"""

    # --- Body ---
    body_lines: list[str] = []
    body_lines.append(f"# {title}")
    body_lines.append("")
    body_lines.append(f"**Source:** Omi ({source})")
    body_lines.append(f"**Date:** {format_display_date(started_local)}")
    body_lines.append(f"**Category:** {category}")
    if emoji:
        body_lines.append(f"**Emoji:** {emoji}")
    body_lines.append("")

    # Summary
    body_lines.append("## Summary")
    body_lines.append("")
    if overview:
        body_lines.append(overview)
    else:
        body_lines.append("_No summary available._")
    body_lines.append("")

    # Action Items
    body_lines.append("## Action Items")
    body_lines.append("")
    if action_items:
        for item in action_items:
            body_lines.append(f"- [ ] {item}")
    else:
        body_lines.append("_No action items._")
    body_lines.append("")

    # Transcript
    body_lines.append("## Transcript")
    body_lines.append("")
    transcript = build_transcript(segments)
    if transcript:
        body_lines.append(transcript)
    else:
        body_lines.append("_No transcript segments._")
    body_lines.append("")

    return frontmatter + "\n\n" + "\n".join(body_lines)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    print(f"Database : {DB_PATH}")
    print(f"Inbox    : {INBOX_DIR}")
    print()

    if not INBOX_DIR.is_dir():
        sys.exit(f"ERROR: Inbox directory does not exist: {INBOX_DIR}")

    # Collect existing filenames in the inbox for idempotency check
    existing_files: set[str] = {f.name for f in INBOX_DIR.iterdir()}

    conn = sqlite3.connect(str(DB_PATH))
    conn.row_factory = sqlite3.Row

    # ------------------------------------------------------------------
    # Fetch eligible sessions
    # ------------------------------------------------------------------
    sessions = conn.execute("""
        SELECT
            ts.id,
            ts.startedAt,
            ts.finishedAt,
            ts.source,
            ts.language,
            ts.title,
            ts.overview,
            ts.emoji,
            ts.category,
            ts.actionItemsJson,
            ts.deleted,
            ts.discarded,
            COUNT(seg.id) AS seg_count
        FROM transcription_sessions ts
        LEFT JOIN transcription_segments seg ON seg.sessionId = ts.id
        GROUP BY ts.id
        ORDER BY ts.startedAt ASC
    """).fetchall()

    exported = 0
    skipped_existing = 0
    filtered_deleted = 0
    filtered_no_title = 0
    filtered_no_segments = 0

    for s in sessions:
        session = dict(s)

        # --- Filtering ---
        if session["deleted"] or session["discarded"]:
            filtered_deleted += 1
            continue

        title = (session["title"] or "").strip()
        if not title:
            filtered_no_title += 1
            continue

        if session["seg_count"] == 0:
            filtered_no_segments += 1
            continue

        # --- Idempotency: skip if file already exists ---
        filename = format_filename(session["startedAt"], title)
        if filename in existing_files:
            skipped_existing += 1
            continue

        # --- Fetch segments ---
        segments = conn.execute("""
            SELECT speaker, text, speakerLabel, isUser, personId
            FROM transcription_segments
            WHERE sessionId = ?
            ORDER BY segmentOrder ASC
        """, (session["id"],)).fetchall()
        segments = [dict(seg) for seg in segments]

        # --- Build and write ---
        content = build_markdown(session, segments)
        out_path = INBOX_DIR / filename
        out_path.write_text(content, encoding="utf-8")
        print(f"  EXPORTED  {filename}")
        exported += 1

    conn.close()

    # --- Summary ---
    total = len(sessions)
    print()
    print("=" * 60)
    print(f"Total sessions in DB        : {total}")
    print(f"Exported (new)              : {exported}")
    print(f"Skipped (already in inbox)  : {skipped_existing}")
    print(f"Filtered (deleted/discarded): {filtered_deleted}")
    print(f"Filtered (no title)         : {filtered_no_title}")
    print(f"Filtered (no segments)      : {filtered_no_segments}")
    print("=" * 60)


if __name__ == "__main__":
    main()
