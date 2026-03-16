"""Alfred MCP Server — Expose vault operations as MCP tools.

Run with:
    python alfred_mcp_server.py

Or register in Claude Desktop's config as a stdio transport.
"""

import subprocess
import json
from pathlib import Path

from mcp.server.fastmcp import FastMCP

# ── Config ──────────────────────────────────────────────────
VAULT_PATH = Path("/Users/ramikhouri/Desktop/Taliaz")
ALFRED_DIR = Path("/Users/ramikhouri/Desktop/Alfred")

RECORD_TYPES = [
    "person", "org", "project", "location", "account", "asset", "process",
    "task", "conversation", "input", "session", "note", "event", "run",
    "decision", "assumption", "constraint", "contradiction", "synthesis",
]

# ── MCP Server ──────────────────────────────────────────────
mcp = FastMCP("Alfred")


def _run_vault(args: list[str], stdin_text: str | None = None) -> str:
    """Run an `alfred vault` CLI command and return output."""
    cmd = ["alfred", "vault"] + args
    try:
        r = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=30,
            cwd=str(ALFRED_DIR),
            stdin=subprocess.PIPE if stdin_text else None,
            input=stdin_text,
        )
        output = r.stdout.strip() or r.stderr.strip()
        if r.returncode != 0:
            return f"ERROR: {output}"
        return output
    except Exception as e:
        return f"ERROR: {e}"


# ── Tools ───────────────────────────────────────────────────

@mcp.tool()
def vault_search(query: str, method: str = "grep") -> str:
    """Search vault files by content (grep) or filename pattern (glob).

    Args:
        query: The search term or glob pattern.
        method: Either 'grep' (content search) or 'glob' (filename pattern). Defaults to 'grep'.
    """
    return _run_vault(["search", f"--{method}", query])


@mcp.tool()
def vault_read(path: str) -> str:
    """Read the full content of a vault record.

    Args:
        path: Relative path to the record, e.g. 'person/John Smith.md'
    """
    file_path = VAULT_PATH / path
    if not file_path.exists():
        return f"ERROR: File not found: {path}"
    try:
        return file_path.read_text(encoding="utf-8")
    except Exception as e:
        return f"ERROR reading file: {e}"


@mcp.tool()
def vault_list(record_type: str) -> str:
    """List all vault records of a given type.

    Args:
        record_type: The type to list (e.g. 'person', 'task', 'project', 'note', 'org', 'decision').
    """
    if record_type not in RECORD_TYPES:
        return f"ERROR: Unknown type '{record_type}'. Valid types: {', '.join(RECORD_TYPES)}"
    return _run_vault(["list", record_type])


@mcp.tool()
def vault_edit(
    path: str,
    set_fields: dict[str, str] | None = None,
    append_fields: dict[str, str] | None = None,
    body_append: str | None = None,
) -> str:
    """Edit an existing vault record's frontmatter or body.

    Args:
        path: Relative path to the record, e.g. 'person/John Smith.md'.
        set_fields: Dict of frontmatter fields to set, e.g. {"status": "inactive", "role": "CEO"}.
        append_fields: Dict of list fields to append to, e.g. {"tags": "urgent"}.
        body_append: Text to append to the record body.
    """
    args = ["edit", path]
    if set_fields:
        for k, v in set_fields.items():
            args += ["--set", f"{k}={v}"]
    if append_fields:
        for k, v in append_fields.items():
            args += ["--append", f"{k}={v}"]
    if body_append:
        args += ["--body-append", body_append]
    if len(args) == 2:
        return "ERROR: No changes specified. Provide set_fields, append_fields, or body_append."
    return _run_vault(args)


@mcp.tool()
def vault_create(
    record_type: str,
    name: str,
    set_fields: dict[str, str] | None = None,
    body: str | None = None,
) -> str:
    """Create a new vault record.

    Args:
        record_type: Record type (e.g. 'person', 'task', 'note', 'project').
        name: Name/title of the new record.
        set_fields: Dict of frontmatter fields to set, e.g. {"status": "active", "priority": "high"}.
        body: Body content for the record.
    """
    if record_type not in RECORD_TYPES:
        return f"ERROR: Unknown type '{record_type}'. Valid types: {', '.join(RECORD_TYPES)}"
    args = ["create", record_type, name]
    if set_fields:
        for k, v in set_fields.items():
            args += ["--set", f"{k}={v}"]
    if body:
        args += ["--body-stdin"]
        return _run_vault(args, stdin_text=body)
    return _run_vault(args)


@mcp.tool()
def vault_delete(path: str) -> str:
    """Delete a vault record. Use only for garbage or test records.

    Args:
        path: Relative path to the record to delete, e.g. 'note/test test.md'.
    """
    return _run_vault(["delete", path])


@mcp.tool()
def vault_context() -> str:
    """Get a compact summary of the vault — record counts by type, recent activity, and structure."""
    return _run_vault(["context"])


@mcp.tool()
def alfred_status() -> str:
    """Get the current status of all Alfred daemons (Curator, Janitor, Distiller, Surveyor)."""
    cmd = ["alfred", "status"]
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=15, cwd=str(ALFRED_DIR))
        return r.stdout.strip() or r.stderr.strip()
    except Exception as e:
        return f"ERROR: {e}"


# ── Resources ───────────────────────────────────────────────

@mcp.resource("alfred://vault/types")
def list_record_types() -> str:
    """List all available vault record types."""
    return json.dumps(RECORD_TYPES)


@mcp.resource("alfred://vault/config")
def get_config() -> str:
    """Get the current Alfred configuration."""
    config_path = ALFRED_DIR / "config.yaml"
    if config_path.exists():
        return config_path.read_text(encoding="utf-8")
    return "Config file not found."


@mcp.resource("alfred://vault/stats")
def vault_stats() -> str:
    """Get vault statistics — file counts per type."""
    stats: dict[str, int] = {}
    for rt in RECORD_TYPES:
        type_dir = VAULT_PATH / rt
        if type_dir.is_dir():
            stats[rt] = len(list(type_dir.glob("*.md")))
        else:
            stats[rt] = 0
    return json.dumps(stats, indent=2)


# ── Google Workspace Tools ──────────────────────────────────

import sys
sys.path.insert(0, str(ALFRED_DIR))

try:
    import google_connector as gc
    GOOGLE_AVAILABLE = True
except Exception:
    GOOGLE_AVAILABLE = False


def _google_guard(func):
    """Wrap a Google function to handle missing credentials."""
    import functools
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if not GOOGLE_AVAILABLE:
            return "ERROR: Google connector not available. Run alfred_mcp_server.py from the Alfred directory."
        try:
            return func(*args, **kwargs)
        except Exception as e:
            return f"ERROR: {e}"
    return wrapper


@mcp.tool()
@_google_guard
def google_gmail_search(query: str, max_results: int = 10) -> str:
    """Search Gmail messages. Examples: 'from:boss@company.com', 'subject:meeting', 'newer_than:2d'.

    Args:
        query: Gmail search query (same syntax as Gmail search bar).
        max_results: Maximum number of results to return (default 10).
    """
    results = gc.gmail_search(query, max_results)
    return json.dumps(results, indent=2, ensure_ascii=False)


@mcp.tool()
@_google_guard
def google_gmail_read(message_id: str) -> str:
    """Read a specific Gmail message by ID (get the ID from gmail_search first).

    Args:
        message_id: The Gmail message ID to read.
    """
    result = gc.gmail_read(message_id)
    return json.dumps(result, indent=2, ensure_ascii=False)


@mcp.tool()
@_google_guard
def google_gmail_send(to: str, subject: str, body: str) -> str:
    """Send an email via Gmail.

    Args:
        to: Recipient email address.
        subject: Email subject line.
        body: Email body text.
    """
    return gc.gmail_send(to, subject, body)


@mcp.tool()
@_google_guard
def google_calendar_events(days_ahead: int = 7) -> str:
    """List upcoming calendar events for the next N days.

    Args:
        days_ahead: Number of days to look ahead (default 7).
    """
    events = gc.calendar_list_events(days_ahead)
    return json.dumps(events, indent=2, ensure_ascii=False)


@mcp.tool()
@_google_guard
def google_calendar_create(summary: str, start: str, end: str, description: str = "") -> str:
    """Create a new Google Calendar event.

    Args:
        summary: Event title.
        start: Start time as ISO datetime (e.g. '2026-03-04T09:00:00').
        end: End time as ISO datetime (e.g. '2026-03-04T10:00:00').
        description: Optional event description.
    """
    return gc.calendar_create_event(summary, start, end, description)


@mcp.tool()
@_google_guard
def google_drive_search(query: str) -> str:
    """Search Google Drive files by content or name.

    Args:
        query: Search query text.
    """
    results = gc.drive_search(query)
    return json.dumps(results, indent=2, ensure_ascii=False)


@mcp.tool()
@_google_guard
def google_drive_read(file_id: str) -> str:
    """Read the content of a Google Drive file (Google Docs exported as text, sheets as CSV).

    Args:
        file_id: The Google Drive file ID (get from drive_search).
    """
    return gc.drive_read(file_id)


# ── Manus AI Agent Tools ────────────────────────────────────

try:
    import manus_connector as mc
    MANUS_AVAILABLE = True
except Exception:
    MANUS_AVAILABLE = False


@mcp.tool()
def manus_create_task(prompt: str) -> str:
    """Delegate a complex task to the Manus AI agent (research, analysis, content generation). Returns a task ID.

    Args:
        prompt: Detailed task instructions for Manus to execute.
    """
    if not MANUS_AVAILABLE:
        return "ERROR: Manus connector not available."
    try:
        result = mc.create_task(prompt)
        return json.dumps(result, indent=2, ensure_ascii=False)
    except Exception as e:
        return f"ERROR: {e}"


@mcp.tool()
def manus_get_task(task_id: str) -> str:
    """Check the status and results of a Manus task.

    Args:
        task_id: The Manus task ID to check.
    """
    if not MANUS_AVAILABLE:
        return "ERROR: Manus connector not available."
    try:
        result = mc.get_task(task_id)
        return json.dumps(result, indent=2, ensure_ascii=False)
    except Exception as e:
        return f"ERROR: {e}"


@mcp.tool()
def manus_list_tasks(status: str | None = None, limit: int = 10) -> str:
    """List recent Manus tasks and their statuses.

    Args:
        status: Optional filter: queued, running, completed, failed.
        limit: Max results (default 10).
    """
    if not MANUS_AVAILABLE:
        return "ERROR: Manus connector not available."
    try:
        results = mc.list_tasks(status, limit)
        return json.dumps(results, indent=2, ensure_ascii=False)
    except Exception as e:
        return f"ERROR: {e}"


# ── Entry point ─────────────────────────────────────────────

if __name__ == "__main__":
    mcp.run()
