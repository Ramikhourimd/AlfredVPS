#!/usr/bin/env python3
"""
alfred_to_omi.py — Sync Alfred vault records into the Omi local database.

Reads markdown records from the vault (person, org, project, task, note,
decision, assumption, constraint, synthesis, contradiction, event, conversation)
and upserts them into the Omi `memories` table. Also syncs person/org records
into the knowledge graph (local_kg_nodes + local_kg_edges).

Idempotent: uses a content-hash stored in the memories `windowTitle` column
to skip unchanged records. Re-syncs if the file has been modified.

Usage:
    python3 scripts/alfred_to_omi.py           # full sync
    python3 scripts/alfred_to_omi.py --dry-run # preview only
"""
from __future__ import annotations

import hashlib
import json
import os
import re
import sqlite3
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

VAULT_ROOT = Path(__file__).resolve().parent.parent  # …/Taliaz

# Find the real (non-empty) omi.db
_OMI_BASE = Path.home() / "Library" / "Application Support" / "omi"
_DB_CANDIDATES = sorted(
    _OMI_BASE.rglob("omi.db"), key=lambda p: p.stat().st_size, reverse=True
)
DB_PATH = next((p for p in _DB_CANDIDATES if p.stat().st_size > 0), None)
if DB_PATH is None:
    sys.exit("ERROR: Could not find a non-empty omi.db under " + str(_OMI_BASE))

# Record type directories to sync
SYNC_DIRS: dict[str, str] = {
    "person": "person",
    "org": "organization",
    "project": "project",
    "task": "task",
    "note": "note",
    "decision": "decision",
    "assumption": "assumption",
    "constraint": "constraint",
    "synthesis": "synthesis",
    "contradiction": "contradiction",
    "event": "event",
    "conversation": "conversation",
    "account": "account",
    "asset": "asset",
}

# Category mapping for memories table
CATEGORY_MAP: dict[str, str] = {
    "person": "vault_person",
    "org": "vault_org",
    "project": "vault_project",
    "task": "vault_task",
    "note": "vault_note",
    "decision": "vault_decision",
    "assumption": "vault_assumption",
    "constraint": "vault_constraint",
    "synthesis": "vault_synthesis",
    "contradiction": "vault_contradiction",
    "event": "vault_event",
    "conversation": "vault_conversation",
    "account": "vault_account",
    "asset": "vault_asset",
}

# Marker prefix for vault-originated memories
SOURCE_TAG = "alfred_vault"

# We store a hash in windowTitle for change detection
HASH_PREFIX = "vault_hash:"


# ---------------------------------------------------------------------------
# YAML / Markdown Parsing (lightweight, no PyYAML dependency)
# ---------------------------------------------------------------------------

def parse_frontmatter(text: str) -> tuple[dict[str, Any], str]:
    """Parse YAML frontmatter and body from markdown text.

    Returns (frontmatter_dict, body_text). Uses a simple line-by-line parser
    to avoid requiring the pyyaml package.
    """
    lines = text.split("\n")
    if not lines or lines[0].strip() != "---":
        return {}, text

    fm_lines: list[str] = []
    body_start = 1
    found_end = False
    for i, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            body_start = i + 1
            found_end = True
            break
        fm_lines.append(line)

    if not found_end:
        return {}, text

    body = "\n".join(lines[body_start:]).strip()
    fm = _parse_yaml_simple("\n".join(fm_lines))
    return fm, body


def _parse_yaml_simple(raw: str) -> dict[str, Any]:
    """Minimal YAML parser for flat key-value frontmatter.

    Handles: strings, quoted strings, nulls, booleans, lists (inline and
    multi-line with '- ' prefix), and nested keys at depth 1.
    Only goes 1 level deep for lists. Good enough for vault frontmatter.
    """
    result: dict[str, Any] = {}
    current_key: str | None = None
    current_list: list[str] | None = None

    for line in raw.split("\n"):
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue

        # Check for list continuation
        if stripped.startswith("- ") and current_key is not None and current_list is not None:
            val = stripped[2:].strip().strip("'\"")
            current_list.append(val)
            result[current_key] = current_list
            continue

        # New key
        match = re.match(r'^([a-zA-Z_][\w_]*)\s*:\s*(.*)', line)
        if match:
            key = match.group(1)
            val_raw = match.group(2).strip()

            # Flush previous list
            current_key = key
            current_list = None

            if val_raw == "" or val_raw == "[]":
                # Could be start of a list or empty value
                current_list = []
                result[key] = current_list
            elif val_raw.lower() in ("null", "~"):
                result[key] = None
            elif val_raw.lower() in ("true", "yes"):
                result[key] = True
            elif val_raw.lower() in ("false", "no"):
                result[key] = False
            elif val_raw.startswith("[") and val_raw.endswith("]"):
                # Inline list
                items = [
                    s.strip().strip("'\"")
                    for s in val_raw[1:-1].split(",")
                    if s.strip()
                ]
                result[key] = items
            elif val_raw.startswith("'") and val_raw.endswith("'"):
                result[key] = val_raw[1:-1]
            elif val_raw.startswith('"') and val_raw.endswith('"'):
                result[key] = val_raw[1:-1]
            else:
                result[key] = val_raw
        else:
            # Unrecognized line — reset list context
            current_key = None
            current_list = None

    return result


# ---------------------------------------------------------------------------
# Content Building
# ---------------------------------------------------------------------------

def build_memory_content(
    record_type: str, fm: dict[str, Any], body: str, filepath: Path
) -> str:
    """Build a concise, searchable memory string from a vault record."""
    parts: list[str] = []

    name = fm.get("name") or fm.get("title") or filepath.stem
    parts.append(f"[{record_type.upper()}] {name}")

    desc = fm.get("description")
    if desc and isinstance(desc, str):
        parts.append(desc.strip())

    # For persons, add key fields
    if record_type == "person":
        email = fm.get("email")
        if email:
            parts.append(f"Email: {email}")
        phone = fm.get("phone")
        if phone:
            parts.append(f"Phone: {phone}")
        org = fm.get("org")
        if org and isinstance(org, str):
            org_clean = re.sub(r"\[\[.*?/?(.*?)\]\]", r"\1", org)
            parts.append(f"Org: {org_clean}")

    # For tasks, add status/priority
    if record_type == "task":
        status = fm.get("status")
        priority = fm.get("priority")
        if status:
            parts.append(f"Status: {status}")
        if priority:
            parts.append(f"Priority: {priority}")
        due = fm.get("due")
        if due:
            parts.append(f"Due: {due}")
        project = fm.get("project")
        if project and isinstance(project, str):
            proj_clean = re.sub(r"\[\[.*?/?(.*?)\]\]", r"\1", project)
            parts.append(f"Project: {proj_clean}")

    # For projects, add status and client
    if record_type == "project":
        status = fm.get("status")
        if status:
            parts.append(f"Status: {status}")
        client = fm.get("client")
        if client and isinstance(client, str):
            client_clean = re.sub(r"\[\[.*?/?(.*?)\]\]", r"\1", client)
            parts.append(f"Client: {client_clean}")

    # For decisions/assumptions/etc, add confidence
    if record_type in ("decision", "assumption", "constraint", "synthesis", "contradiction"):
        conf = fm.get("confidence")
        if conf:
            parts.append(f"Confidence: {conf}")
        status = fm.get("status")
        if status:
            parts.append(f"Status: {status}")

    # Add related links (cleaned)
    related = fm.get("related")
    if isinstance(related, list) and related:
        cleaned = []
        for r in related[:8]:  # Limit to 8 most important
            if isinstance(r, str):
                clean = re.sub(r"\[\[.*?/?(.*?)\]\]", r"\1", r)
                if clean:
                    cleaned.append(clean)
        if cleaned:
            parts.append(f"Related: {', '.join(cleaned)}")

    # Add body excerpt (first ~500 chars of actual content, skip headings)
    if body:
        body_lines = [
            l.strip()
            for l in body.split("\n")
            if l.strip() and not l.strip().startswith("#") and not l.strip().startswith("!")
        ]
        excerpt = " ".join(body_lines)[:500]
        if excerpt:
            parts.append(excerpt)

    return "\n".join(parts)


def extract_tags(fm: dict[str, Any], record_type: str) -> list[str]:
    """Extract tags for the memory record."""
    tags = ["vault", record_type]
    alfred_tags = fm.get("alfred_tags")
    if isinstance(alfred_tags, list):
        for t in alfred_tags:
            if isinstance(t, str):
                tags.append(t.split("/")[-1])  # Take last segment
    fm_tags = fm.get("tags")
    if isinstance(fm_tags, list):
        for t in fm_tags:
            if isinstance(t, str):
                tags.append(t)
    return list(dict.fromkeys(tags))  # Deduplicate preserving order


def content_hash(content: str) -> str:
    """SHA-256 hash of content for change detection."""
    return hashlib.sha256(content.encode("utf-8")).hexdigest()[:16]


# ---------------------------------------------------------------------------
# Knowledge Graph Helpers
# ---------------------------------------------------------------------------

def slugify(name: str) -> str:
    """Create a slug ID for KG nodes."""
    slug = re.sub(r"\s+", "-", name.strip().lower())
    slug = re.sub(r"[^\w\-]", "", slug, flags=re.UNICODE)
    slug = re.sub(r"-{2,}", "-", slug).strip("-")
    return slug[:60]


def upsert_kg_node(
    conn: sqlite3.Connection,
    node_id: str,
    label: str,
    node_type: str,
    aliases: list[str] | None = None,
) -> None:
    """Insert or update a knowledge graph node."""
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
    aliases_json = json.dumps(aliases) if aliases else None

    existing = conn.execute(
        "SELECT id FROM local_kg_nodes WHERE nodeId = ?", (node_id,)
    ).fetchone()

    if existing:
        conn.execute(
            """UPDATE local_kg_nodes
               SET label = ?, nodeType = ?, aliasesJson = ?, updatedAt = ?
               WHERE nodeId = ?""",
            (label, node_type, aliases_json, now, node_id),
        )
    else:
        conn.execute(
            """INSERT INTO local_kg_nodes (nodeId, label, nodeType, aliasesJson, createdAt, updatedAt)
               VALUES (?, ?, ?, ?, ?, ?)""",
            (node_id, label, node_type, aliases_json, now, now),
        )


def upsert_kg_edge(
    conn: sqlite3.Connection,
    source_id: str,
    target_id: str,
    label: str,
) -> None:
    """Insert a KG edge if it doesn't exist."""
    edge_id = f"{source_id}--{label}--{target_id}"
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")

    existing = conn.execute(
        "SELECT id FROM local_kg_edges WHERE edgeId = ?", (edge_id,)
    ).fetchone()

    if not existing:
        conn.execute(
            """INSERT INTO local_kg_edges (edgeId, sourceNodeId, targetNodeId, label, createdAt)
               VALUES (?, ?, ?, ?, ?)""",
            (edge_id, source_id, target_id, label, now),
        )


# ---------------------------------------------------------------------------
# Sync Logic
# ---------------------------------------------------------------------------

def collect_vault_files() -> list[tuple[str, Path]]:
    """Collect all markdown files from sync directories."""
    files: list[tuple[str, Path]] = []
    for dir_name in SYNC_DIRS:
        dir_path = VAULT_ROOT / dir_name
        if not dir_path.is_dir():
            continue
        for md_file in dir_path.rglob("*.md"):
            if md_file.name.startswith(".") or md_file.name == "Icon\r":
                continue
            files.append((dir_name, md_file))
    return files


def sync_memory(
    conn: sqlite3.Connection,
    record_type: str,
    filepath: Path,
    fm: dict[str, Any],
    body: str,
    dry_run: bool = False,
) -> str:
    """Sync a single vault record to the memories table.

    Returns: 'inserted', 'updated', 'skipped', or 'dry_run'.
    """
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
    rel_path = str(filepath.relative_to(VAULT_ROOT))
    memory_content = build_memory_content(record_type, fm, body, filepath)
    h = content_hash(memory_content)
    hash_tag = f"{HASH_PREFIX}{h}"
    category = CATEGORY_MAP.get(record_type, f"vault_{record_type}")
    tags = extract_tags(fm, record_type)
    tags_json = json.dumps(tags)
    name = fm.get("name") or fm.get("title") or filepath.stem
    created = fm.get("created") or now

    if isinstance(created, str) and len(created) == 10:
        created = f"{created}T00:00:00"

    # Check for existing record by source path
    existing = conn.execute(
        """SELECT id, windowTitle FROM memories
           WHERE source = ? AND contextSummary = ? AND deleted = 0""",
        (SOURCE_TAG, rel_path),
    ).fetchone()

    if existing:
        old_hash = existing[1] or ""
        if old_hash == hash_tag:
            return "skipped"
        if dry_run:
            return "dry_run"
        conn.execute(
            """UPDATE memories
               SET content = ?, category = ?, tagsJson = ?, headline = ?,
                   windowTitle = ?, updatedAt = ?
               WHERE id = ?""",
            (memory_content, category, tags_json, name, hash_tag, now, existing[0]),
        )
        return "updated"
    else:
        if dry_run:
            return "dry_run"
        conn.execute(
            """INSERT INTO memories
               (content, category, tagsJson, visibility, reviewed, manuallyAdded,
                source, contextSummary, windowTitle, headline, confidence,
                isRead, isDismissed, deleted, createdAt, updatedAt)
               VALUES (?, ?, ?, 'private', 0, 1, ?, ?, ?, ?, 0.9, 0, 0, 0, ?, ?)""",
            (memory_content, category, tags_json, SOURCE_TAG, rel_path,
             hash_tag, name, now, now),
        )
        return "inserted"


def sync_kg_entities(
    conn: sqlite3.Connection,
    record_type: str,
    fm: dict[str, Any],
    filepath: Path,
    dry_run: bool = False,
) -> int:
    """Sync person/org records to the knowledge graph. Returns count of ops."""
    if record_type not in ("person", "org"):
        return 0
    if dry_run:
        return 0

    name = fm.get("name") or filepath.stem
    node_id = slugify(name)
    node_type = "person" if record_type == "person" else "organization"

    aliases = [name.lower()]
    fm_aliases = fm.get("aliases")
    if isinstance(fm_aliases, list):
        for a in fm_aliases:
            if isinstance(a, str) and a:
                aliases.append(a.lower())

    upsert_kg_node(conn, node_id, name, node_type, aliases)
    ops = 1

    # Create edges for org relationships
    if record_type == "person":
        org_raw = fm.get("org")
        if org_raw and isinstance(org_raw, str):
            org_name = re.sub(r"\[\[.*?/?(.*?)\]\]", r"\1", org_raw).strip()
            if org_name:
                org_id = slugify(org_name)
                upsert_kg_node(conn, org_id, org_name, "organization", [org_name.lower()])
                upsert_kg_edge(conn, node_id, org_id, "works_at")
                ops += 2

    # Create edges from 'related' links
    related = fm.get("related")
    if isinstance(related, list):
        for r in related[:5]:
            if isinstance(r, str):
                target_name = re.sub(r"\[\[.*?/?(.*?)\]\]", r"\1", r).strip()
                if target_name:
                    target_id = slugify(target_name)
                    upsert_kg_edge(conn, node_id, target_id, "related_to")
                    ops += 1

    return ops


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    dry_run = "--dry-run" in sys.argv

    print(f"{'DRY RUN — ' if dry_run else ''}Alfred → Omi Vault Sync")
    print(f"Vault    : {VAULT_ROOT}")
    print(f"Database : {DB_PATH}")
    print()

    files = collect_vault_files()
    print(f"Found {len(files)} vault records across {len(SYNC_DIRS)} directories\n")

    conn = sqlite3.connect(str(DB_PATH))

    stats: dict[str, int] = {
        "inserted": 0,
        "updated": 0,
        "skipped": 0,
        "dry_run": 0,
        "errors": 0,
        "kg_ops": 0,
    }

    for record_type, filepath in files:
        try:
            text = filepath.read_text(encoding="utf-8")
            fm, body = parse_frontmatter(text)
            result = sync_memory(conn, record_type, filepath, fm, body, dry_run)
            stats[result] += 1

            if result in ("inserted", "updated"):
                rel = str(filepath.relative_to(VAULT_ROOT))
                print(f"  {result.upper():8s}  {rel}")

            # KG sync for persons/orgs
            kg = sync_kg_entities(conn, record_type, fm, filepath, dry_run)
            stats["kg_ops"] += kg

        except Exception as e:
            stats["errors"] += 1
            print(f"  ERROR    {filepath.name}: {e}", file=sys.stderr)

    if not dry_run:
        conn.commit()
    conn.close()

    # --- Summary ---
    total = sum(v for k, v in stats.items() if k != "kg_ops" and k != "errors")
    print()
    print("=" * 60)
    print(f"Total records processed  : {total}")
    print(f"  Inserted (new)         : {stats['inserted']}")
    print(f"  Updated (changed)      : {stats['updated']}")
    print(f"  Skipped (unchanged)    : {stats['skipped']}")
    if dry_run:
        print(f"  Would sync             : {stats['dry_run']}")
    print(f"  Errors                 : {stats['errors']}")
    print(f"Knowledge graph ops      : {stats['kg_ops']}")
    print("=" * 60)


if __name__ == "__main__":
    main()
