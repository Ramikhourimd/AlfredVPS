import streamlit as st
import streamlit_authenticator as stauth
import yaml
import os
import json
import subprocess
import requests
import google_connector as gc
import manus_connector as manus
import re
import glob
from datetime import datetime, timezone, timedelta
from pathlib import Path
from pymilvus import MilvusClient
from dotenv import load_dotenv
from yaml.loader import SafeLoader

VAULT_PATH = Path("/Users/ramikhouri/Desktop/Taliaz")
ALFRED_DIR = Path("/Users/ramikhouri/Desktop/Alfred")
CONVERSATIONS_DIR = VAULT_PATH / "conversation"

load_dotenv()
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

st.set_page_config(page_title="Alfred Dashboard", page_icon="🤖", layout="wide")

# ── Premium Dark Theme CSS ──────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

:root {
    --bg-primary: #0f1117;
    --bg-card: #1a1d2e;
    --bg-card-hover: #232740;
    --accent: #6366f1;
    --accent-glow: rgba(99, 102, 241, 0.15);
    --success: #10b981;
    --warning: #f59e0b;
    --danger: #ef4444;
    --text-primary: #e2e8f0;
    --text-secondary: #94a3b8;
    --border: #2d3148;
}

/* Global font */
html, body, [class*="css"] {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
}

/* Briefing Cards */
.briefing-card {
    background: linear-gradient(135deg, var(--bg-card) 0%, var(--bg-card-hover) 100%);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 1.2rem;
    margin-bottom: 0.8rem;
    transition: transform 0.2s ease, box-shadow 0.2s ease;
}
.briefing-card:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 25px rgba(0,0,0,0.3);
}
.briefing-card h4 {
    margin: 0 0 0.6rem 0;
    color: var(--text-primary);
    font-weight: 600;
}
.briefing-card .stat-value {
    font-size: 2rem;
    font-weight: 700;
    color: var(--accent);
    line-height: 1;
}
.briefing-card .stat-label {
    font-size: 0.8rem;
    color: var(--text-secondary);
    margin-top: 0.2rem;
}

/* Status badges */
.badge {
    display: inline-block;
    padding: 0.15rem 0.6rem;
    border-radius: 9999px;
    font-size: 0.75rem;
    font-weight: 600;
}
.badge-active { background: rgba(16,185,129,0.15); color: var(--success); }
.badge-warning { background: rgba(245,158,11,0.15); color: var(--warning); }
.badge-danger { background: rgba(239,68,68,0.15); color: var(--danger); }

/* Timeline item */
.timeline-item {
    display: flex;
    align-items: flex-start;
    gap: 0.8rem;
    padding: 0.6rem 0;
    border-bottom: 1px solid var(--border);
}
.timeline-item:last-child { border-bottom: none; }
.timeline-time {
    min-width: 60px;
    font-size: 0.85rem;
    font-weight: 600;
    color: var(--accent);
}
.timeline-content {
    font-size: 0.9rem;
    color: var(--text-primary);
}
.timeline-meta {
    font-size: 0.75rem;
    color: var(--text-secondary);
}

/* Quick action buttons */
.stButton > button {
    border-radius: 8px !important;
    font-weight: 500 !important;
    transition: all 0.2s ease !important;
}

/* Notification banner */
.notification-bar {
    background: linear-gradient(90deg, rgba(245,158,11,0.1) 0%, rgba(239,68,68,0.1) 100%);
    border: 1px solid rgba(245,158,11,0.3);
    border-radius: 10px;
    padding: 0.8rem 1.2rem;
    margin-bottom: 1rem;
}

/* Tab styling */
.stTabs [data-baseweb="tab-list"] {
    gap: 8px;
}
.stTabs [data-baseweb="tab"] {
    border-radius: 8px 8px 0 0;
    font-weight: 500;
}
</style>
""", unsafe_allow_html=True)

# ── Auth ────────────────────────────────────────────────────
with open(os.path.join(os.path.dirname(__file__), "credentials.yaml")) as f:
    auth_config = yaml.load(f, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    auth_config["credentials"],
    auth_config["cookie"]["name"],
    auth_config["cookie"]["key"],
    auth_config["cookie"]["expiry_days"],
)
authenticator.login()

if st.session_state.get("authentication_status") is False:
    st.error("Username or password is incorrect.")
    st.stop()
elif st.session_state.get("authentication_status") is None:
    st.warning("Please enter your username and password.")
    st.stop()

# ── Milvus ──────────────────────────────────────────────────
try:
    milvus = MilvusClient(uri=str(ALFRED_DIR / "data" / "milvus_lite.db"))
except Exception as e:
    st.error(f"Milvus connection failed: {e}")
    milvus = None

# ── Session state ───────────────────────────────────────────
if "messages" not in st.session_state:
    st.session_state.messages = []
if "pending_actions" not in st.session_state:
    st.session_state.pending_actions = []
if "pending_assistant_msg" not in st.session_state:
    st.session_state.pending_assistant_msg = None
if "chat_file" not in st.session_state:
    st.session_state.chat_file = None  # Path to current conversation file
if "chat_title" not in st.session_state:
    st.session_state.chat_title = None  # Auto-generated title
if "chat_started" not in st.session_state:
    st.session_state.chat_started = None  # Timestamp when chat began
if "resume_llm" not in st.session_state:
    st.session_state.resume_llm = False
if "qa_mode" not in st.session_state:
    st.session_state.qa_mode = False
if "active_tab" not in st.session_state:
    st.session_state.active_tab = "🏠 Home"

# ── Conversation persistence helpers ────────────────────────

def _get_recent_chat_files(limit=20):
    """Return a list of recent Alfred Chat conversation files, newest first."""
    pattern = str(CONVERSATIONS_DIR / "Alfred Chat*.md")
    files = glob.glob(pattern)
    files.sort(key=os.path.getmtime, reverse=True)
    return files[:limit]


def _extract_title_from_filename(filepath):
    """Extract a human-readable title from an Alfred Chat filename."""
    name = Path(filepath).stem  # e.g. "Alfred Chat — Project Planning 2026-03-03"
    # Remove the "Alfred Chat — " prefix if present
    if "—" in name:
        return name.split("—", 1)[1].strip()
    return name


def _parse_conversation_file(filepath):
    """Parse a vault conversation markdown file back into messages list."""
    try:
        content = Path(filepath).read_text("utf-8")
    except Exception:
        return []

    messages = []
    # Split on ### User or ### Alfred headers
    parts = re.split(r'^### (User|Alfred)\n', content, flags=re.MULTILINE)
    # parts = [preamble, "User", user_msg, "Alfred", alfred_msg, ...]
    i = 1
    while i < len(parts) - 1:
        role_label = parts[i].strip()
        msg_text = parts[i + 1].strip()
        if role_label == "User":
            messages.append({"role": "user", "content": msg_text})
        elif role_label == "Alfred":
            messages.append({"role": "assistant", "content": msg_text})
        i += 2

    return messages


def _build_frontmatter(title, started, message_count):
    """Build vault-compatible YAML frontmatter for a chat conversation."""
    today = datetime.now().strftime("%Y-%m-%d")
    started_date = started.strftime("%Y-%m-%d") if started else today
    return f"""---
type: conversation
status: active
channel: chat
subject: "{title}"
participants:
- "[[person/Rami Khouri]]"
- Alfred (AI Assistant)
project: "[[project/Alfred Development]]"
org:
external_id:
message_count: {message_count}
last_activity: "{today}"
opened: "{started_date}"
created: "{started_date}"
forked_from:
fork_reason:
alfred_instructions:
related: []
relationships: []
tags:
- alfred/chat-memory
---"""


def _build_conversation_body(title, messages):
    """Build the markdown body from the messages list."""
    lines = [f"# {title}", "", "## Messages", ""]
    for msg in messages:
        if msg["role"] == "user":
            lines.append("### User")
            lines.append(msg["content"])
            lines.append("")
        elif msg["role"] == "assistant":
            lines.append("### Alfred")
            lines.append(msg["content"])
            lines.append("")
    return "\n".join(lines)


def save_conversation():
    """Save the current conversation to a vault markdown file."""
    if not st.session_state.messages:
        return

    # Initialize chat_started if needed
    if not st.session_state.chat_started:
        st.session_state.chat_started = datetime.now()

    title = st.session_state.chat_title or "Untitled Chat"
    started = st.session_state.chat_started
    date_str = started.strftime("%Y-%m-%d")
    safe_title = re.sub(r'[\\/:*?"<>|]', '', title)[:60]
    filename = f"Alfred Chat — {safe_title} {date_str}.md"
    filepath = CONVERSATIONS_DIR / filename

    # Count user+assistant messages only
    msg_count = sum(1 for m in st.session_state.messages if m["role"] in ("user", "assistant"))

    frontmatter = _build_frontmatter(title, started, msg_count)
    body = _build_conversation_body(f"Alfred Chat — {title}", st.session_state.messages)
    full_content = frontmatter + "\n\n" + body

    filepath.write_text(full_content, encoding="utf-8")
    st.session_state.chat_file = str(filepath)


def generate_title():
    """Ask the LLM to generate a short title for the conversation."""
    # Only generate after first exchange (at least 1 user + 1 assistant message)
    user_msgs = [m for m in st.session_state.messages if m["role"] == "user"]
    asst_msgs = [m for m in st.session_state.messages if m["role"] == "assistant"]
    if len(user_msgs) < 1 or len(asst_msgs) < 1:
        return

    # Don't regenerate if we already have a title
    if st.session_state.chat_title:
        return

    # Build a lightweight request for a title
    summary_msgs = [
        {"role": "system", "content": "Generate a short, descriptive title (3-7 words) for this conversation. Return ONLY the title, nothing else. No quotes."},
    ]
    for m in st.session_state.messages[:6]:  # First few messages are enough
        if m["role"] in ("user", "assistant"):
            summary_msgs.append({"role": m["role"], "content": m["content"][:200]})

    try:
        headers = {"Authorization": f"Bearer {OPENROUTER_API_KEY}", "Content-Type": "application/json"}
        body = {
            "model": "anthropic/claude-sonnet-4.6",
            "messages": summary_msgs,
            "max_tokens": 30,
        }
        resp = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=body, timeout=10)
        if resp.status_code == 200:
            title = resp.json()["choices"][0]["message"]["content"].strip().strip('"\'')
            if title and len(title) < 80:
                # If we already saved a file with "Untitled Chat", rename it
                old_file = st.session_state.chat_file
                st.session_state.chat_title = title
                save_conversation()  # Save with new title
                # Remove old untitled file if it exists and is different
                if old_file and Path(old_file).exists() and old_file != st.session_state.chat_file:
                    try:
                        Path(old_file).unlink()
                    except Exception:
                        pass
    except Exception:
        pass  # Title generation is non-critical


def load_conversation(filepath):
    """Load a conversation from a vault file into session state."""
    messages = _parse_conversation_file(filepath)
    if messages:
        st.session_state.messages = messages
        st.session_state.chat_file = filepath
        st.session_state.chat_title = _extract_title_from_filename(filepath)
        # Approximate start time from file mtime
        try:
            st.session_state.chat_started = datetime.fromtimestamp(os.path.getmtime(filepath))
        except Exception:
            st.session_state.chat_started = datetime.now()


def start_new_chat():
    """Reset session state for a fresh conversation."""
    st.session_state.messages = []
    st.session_state.pending_actions = []
    st.session_state.pending_assistant_msg = None
    st.session_state.resume_llm = False
    st.session_state.qa_mode = False
    st.session_state.chat_file = None
    st.session_state.chat_title = None
    st.session_state.chat_started = None


def get_memory_context():
    """Search Milvus for recent Alfred Chat conversations to inject as memory context."""
    if not milvus:
        return ""
    try:
        vec = get_embedding("Alfred chatbot conversation with Rami")
        results = milvus.search(
            collection_name="vault_embeddings", data=[vec], limit=5,
            output_fields=["record_type", "name"],
            filter='record_type == "conversation"',
        )
        if not results[0]:
            return ""

        memory_lines = []
        for res in results[0]:
            rel = res["id"]
            nm = res["entity"].get("name", rel)
            # Only include Alfred Chat conversations
            if "Alfred Chat" not in nm and "Alfred Chat" not in rel:
                continue
            fp = VAULT_PATH / rel
            try:
                content = fp.read_text("utf-8")
                # Extract just the messages section, truncated
                if "## Messages" in content:
                    msgs_part = content.split("## Messages", 1)[1][:800]
                    memory_lines.append(f"[{nm}]:\n{msgs_part.strip()}")
            except Exception:
                continue

        if memory_lines:
            return "\n\nYou have memory of previous conversations with Rami:\n" + "\n---\n".join(memory_lines[:3])
    except Exception:
        pass
    return ""


# ── Briefing Engine ─────────────────────────────────────────

@st.cache_data(ttl=300)  # Cache for 5 minutes
def get_calendar_today():
    """Fetch today's and tomorrow's calendar events."""
    try:
        events = gc.calendar_list_events(days_ahead=2, max_results=10)
        return events
    except Exception as e:
        return [{"error": str(e)}]


@st.cache_data(ttl=300)
def get_email_highlights():
    """Fetch unread and priority emails."""
    try:
        unread = gc.gmail_search("is:unread newer_than:3d", max_results=8)
        return unread
    except Exception as e:
        return [{"error": str(e)}]


def get_active_tasks():
    """Scan vault task records for active/in-progress tasks."""
    task_dir = VAULT_PATH / "task"
    tasks = []
    if not task_dir.exists():
        return tasks
    for f in task_dir.glob("*.md"):
        try:
            text = f.read_text("utf-8", errors="replace")[:1000]
            status = ""
            priority = ""
            deadline = ""
            m_status = re.search(r'^status:\s*(.+)$', text, re.MULTILINE)
            m_priority = re.search(r'^priority:\s*(.+)$', text, re.MULTILINE)
            m_deadline = re.search(r'^deadline:\s*(.+)$', text, re.MULTILINE)
            if m_status:
                status = m_status.group(1).strip().lower()
            if m_priority:
                priority = m_priority.group(1).strip()
            if m_deadline:
                deadline = m_deadline.group(1).strip()
            if status in ("active", "in-progress", "in_progress", "todo", "open", "pending"):
                tasks.append({
                    "name": f.stem,
                    "status": status,
                    "priority": priority,
                    "deadline": deadline,
                    "path": str(f.relative_to(VAULT_PATH)),
                })
        except Exception:
            continue
    # Sort: high priority first, then by deadline
    priority_order = {"critical": 0, "high": 1, "medium": 2, "low": 3, "": 4}
    tasks.sort(key=lambda t: (priority_order.get(t["priority"].lower(), 4), t["deadline"] or "9999"))
    return tasks[:20]


def get_vault_stats():
    """Get quick vault statistics."""
    stats = {}
    for rt in ["person", "org", "project", "task", "note", "decision", "assumption", "constraint", "synthesis", "contradiction", "conversation"]:
        d = VAULT_PATH / rt
        if d.exists():
            stats[rt] = len(list(d.glob("*.md")))
    return stats


def get_attention_items():
    """Get items that need attention: overdue tasks, contradictions, janitor issues."""
    items = []
    today = datetime.now().strftime("%Y-%m-%d")

    # Overdue tasks
    tasks = get_active_tasks()
    for t in tasks:
        if t["deadline"] and t["deadline"] < today and t["deadline"] != "":
            items.append({"type": "overdue", "icon": "⏰", "text": f"**Overdue task:** {t['name']} (deadline: {t['deadline']})", "severity": "danger"})

    # Recent contradictions
    contra_dir = VAULT_PATH / "contradiction"
    if contra_dir.exists():
        recent_contras = sorted(contra_dir.glob("*.md"), key=lambda f: f.stat().st_mtime, reverse=True)[:3]
        for c in recent_contras:
            age_days = (datetime.now() - datetime.fromtimestamp(c.stat().st_mtime)).days
            if age_days <= 7:
                items.append({"type": "contradiction", "icon": "⚡", "text": f"**Contradiction found:** {c.stem}", "severity": "warning"})

    # Janitor issues count
    janitor_state = ALFRED_DIR / "data" / "janitor_state.json"
    if janitor_state.exists():
        try:
            jdata = json.loads(janitor_state.read_text())
            sweeps = jdata.get("sweeps", {})
            if sweeps:
                last_sweep = list(sweeps.values())[-1]
                issue_count = last_sweep.get("issues_found", 0)
                if issue_count > 100:
                    items.append({"type": "janitor", "icon": "🧹", "text": f"**Janitor:** {issue_count:,} issues detected in last sweep", "severity": "warning"})
        except Exception:
            pass

    return items


def get_contextual_briefing_text():
    """Build a text summary of today's context for injection into the system prompt."""
    lines = ["\n## Today's Context (auto-injected)"]
    lines.append(f"**Date:** {datetime.now().strftime('%A, %B %d, %Y %I:%M %p')} (Israel Time)")

    # Calendar
    try:
        events = get_calendar_today()
        if events and not events[0].get("error"):
            lines.append(f"\n**📅 Today's Calendar ({len(events)} events):**")
            for e in events[:5]:
                start = e.get("start", "?")
                if "T" in start:
                    start = start[11:16]
                lines.append(f"- {start} — {e.get('summary', 'No title')}")
    except Exception:
        pass

    # Active tasks
    try:
        tasks = get_active_tasks()
        if tasks:
            lines.append(f"\n**📋 Active Tasks ({len(tasks)}):**")
            for t in tasks[:5]:
                p = f" [{t['priority']}]" if t['priority'] else ""
                d = f" (due: {t['deadline']})" if t['deadline'] else ""
                lines.append(f"- {t['name']}{p}{d}")
    except Exception:
        pass

    # Attention items
    try:
        attention = get_attention_items()
        if attention:
            lines.append(f"\n**⚠️ Needs Attention:**")
            for a in attention[:3]:
                lines.append(f"- {a['text']}")
    except Exception:
        pass

    return "\n".join(lines)


def render_briefing():
    """Render the full Daily Briefing command center."""
    now = datetime.now()
    greeting_hour = now.hour
    if greeting_hour < 12:
        greeting = "Good morning"
    elif greeting_hour < 17:
        greeting = "Good afternoon"
    else:
        greeting = "Good evening"

    st.markdown(f"## {greeting}, {st.session_state.get('name', 'Rami')} 👋")
    st.caption(f"📅 {now.strftime('%A, %B %d, %Y')} · {now.strftime('%I:%M %p')} Israel Time")

    # ── Notification Bar (Attention Items) ──
    attention = get_attention_items()
    if attention:
        with st.container():
            st.markdown('<div class="notification-bar">', unsafe_allow_html=True)
            for a in attention[:3]:
                st.markdown(f"{a['icon']} {a['text']}")
            st.markdown('</div>', unsafe_allow_html=True)

    # ── Quick Actions Row ──
    st.markdown("### ⚡ Quick Actions")
    qa1, qa2, qa3, qa4 = st.columns(4)
    with qa1:
        if st.button("📝 New Note", use_container_width=True):
            st.session_state.active_tab = "💬 Chat"
            st.session_state.messages.append({"role": "user", "content": "Create a new note for me. Ask me what it should be about."})
            st.session_state.resume_llm = True
            st.rerun()
    with qa2:
        if st.button("✅ New Task", use_container_width=True):
            st.session_state.active_tab = "💬 Chat"
            st.session_state.messages.append({"role": "user", "content": "Create a new task for me. Ask me about the title, priority, and deadline."})
            st.session_state.resume_llm = True
            st.rerun()
    with qa3:
        if st.button("📧 Draft Email", use_container_width=True):
            st.session_state.active_tab = "💬 Chat"
            st.session_state.messages.append({"role": "user", "content": "Help me draft an email. Ask me who it's for and what it should say."})
            st.session_state.resume_llm = True
            st.rerun()
    with qa4:
        if st.button("🔍 Deep Search", use_container_width=True):
            st.session_state.active_tab = "💬 Chat"
            st.session_state.messages.append({"role": "user", "content": "I want to do a deep search. Ask me what I'm looking for and search across the vault, Gmail, and Drive."})
            st.session_state.resume_llm = True
            st.rerun()

    st.markdown("---")

    # ── Main Briefing Grid ──
    col_cal, col_email = st.columns(2)

    # Calendar Column
    with col_cal:
        st.markdown("### 📅 Today's Schedule")
        events = get_calendar_today()
        if events and not events[0].get("error"):
            for e in events:
                start = e.get("start", "")
                time_str = start[11:16] if "T" in start else "All day"
                summary = e.get("summary", "No title")
                location = e.get("location", "")
                loc_str = f" · 📍 {location}" if location else ""
                attendees = e.get("attendees", [])
                att_str = f" · 👥 {len(attendees)}" if attendees else ""

                st.markdown(f"""
<div class="timeline-item">
    <div class="timeline-time">{time_str}</div>
    <div>
        <div class="timeline-content">{summary}</div>
        <div class="timeline-meta">{loc_str}{att_str}</div>
    </div>
</div>
""", unsafe_allow_html=True)
        else:
            err = events[0].get("error", "") if events else ""
            if err:
                st.caption(f"⚠️ Calendar unavailable: {err[:80]}")
            else:
                st.caption("No events today ✨")

    # Email Column
    with col_email:
        st.markdown("### 📧 Unread Emails")
        emails = get_email_highlights()
        if emails and not emails[0].get("error"):
            for em in emails[:6]:
                sender = em.get("from", "").split("<")[0].strip().strip('"')
                subject = em.get("subject", "(no subject)")
                snippet = em.get("snippet", "")[:80]
                st.markdown(f"""**{sender}**  
_{subject}_  
<span style="color: var(--text-secondary); font-size: 0.8rem;">{snippet}...</span>
""", unsafe_allow_html=True)
                st.markdown("<hr style='margin: 0.4rem 0; border-color: var(--border);'>", unsafe_allow_html=True)
        else:
            err = emails[0].get("error", "") if emails else ""
            if err:
                st.caption(f"⚠️ Gmail unavailable: {err[:80]}")
            else:
                st.caption("Inbox zero! 🎉")

    st.markdown("---")

    # ── Tasks & Vault Stats Row ──
    col_tasks, col_stats = st.columns([3, 2])

    with col_tasks:
        st.markdown("### 📋 Active Tasks")
        tasks = get_active_tasks()
        if tasks:
            for t in tasks[:8]:
                priority = t['priority'].lower()
                if priority in ('critical', 'high'):
                    badge_class = 'badge-danger'
                elif priority == 'medium':
                    badge_class = 'badge-warning'
                else:
                    badge_class = 'badge-active'
                p_badge = f'<span class="badge {badge_class}">{t["priority"]}</span>' if t['priority'] else ''
                d_str = f' · Due: {t["deadline"]}' if t['deadline'] else ''
                st.markdown(f"{p_badge} **{t['name']}**{d_str}", unsafe_allow_html=True)
        else:
            st.caption("No active tasks. Time to plan! 📝")

    with col_stats:
        st.markdown("### 📊 Vault Overview")
        stats = get_vault_stats()
        total = sum(stats.values())
        st.markdown(f'<div class="briefing-card"><div class="stat-value">{total:,}</div><div class="stat-label">Total Records</div></div>', unsafe_allow_html=True)

        # Mini stat grid
        top_types = sorted(stats.items(), key=lambda x: x[1], reverse=True)[:6]
        gcol1, gcol2 = st.columns(2)
        for i, (rtype, count) in enumerate(top_types):
            with gcol1 if i % 2 == 0 else gcol2:
                st.metric(rtype.title(), count)


def render_analytics():
    """Render the Analytics / Vault Health page."""
    st.markdown("## 📊 Analytics & Vault Health")

    # Worker Status (expanded version)
    st.markdown("### ⚙️ Worker Daemons")
    try:
        daemon_running, tools_status, workers_list, data_dir = _load_worker_dashboard()
        status_text = "🟢 **Running**" if daemon_running else "🔴 **Stopped**"
        st.markdown(f"Daemon Status: {status_text}")

        wcols = st.columns(4)
        for i, w in enumerate(workers_list):
            with wcols[i]:
                tool_info = tools_status.get(w["key"], {})
                is_running = tool_info.get("status") == "running" and daemon_running
                dot = "🟢" if is_running else "⚪"
                restarts = tool_info.get("restarts", 0)
                st.markdown(f"{dot} **{w['icon']} {w['name']}**")
                if restarts > 0:
                    st.warning(f"Restarted {restarts}x")
                state_path = data_dir / w["state_file"]
                if state_path.exists():
                    try:
                        state_data = json.loads(state_path.read_text())
                        stats = w["stats"](state_data)
                        for label, value in stats.items():
                            st.caption(f"{label}: **{value}**")
                    except Exception:
                        st.caption("Can't read state")
    except Exception as e:
        st.error(f"Worker status error: {e}")

    st.markdown("---")

    # Vault Stats
    st.markdown("### 📁 Records by Type")
    stats = get_vault_stats()
    if stats:
        import pandas as pd
        df = pd.DataFrame(list(stats.items()), columns=["Type", "Count"]).sort_values("Count", ascending=False)
        st.bar_chart(df.set_index("Type"))

    # Recent vault activity
    st.markdown("### 🕐 Recent Vault Activity")
    recent_files = []
    for rt in ["note", "task", "decision", "conversation"]:
        d = VAULT_PATH / rt
        if d.exists():
            for f in d.glob("*.md"):
                try:
                    recent_files.append({"name": f"{rt}/{f.name}", "modified": datetime.fromtimestamp(f.stat().st_mtime)})
                except Exception:
                    continue
    recent_files.sort(key=lambda x: x["modified"], reverse=True)
    for rf in recent_files[:10]:
        age = _fmt_time(rf["modified"].astimezone(timezone.utc).isoformat())
        st.caption(f"📄 `{rf['name']}` — {age}")


# ── Sidebar ─────────────────────────────────────────────────

authenticator.logout("Logout", "sidebar")
st.sidebar.write(f"Welcome, **{st.session_state['name']}**")

st.sidebar.markdown("---")
st.sidebar.subheader("💬 Chat History")

if st.sidebar.button("📝 New Chat", use_container_width=True):
    start_new_chat()
    st.rerun()

if st.sidebar.button("🎯 Refine Knowledge Base", use_container_width=True, type="secondary"):
    start_new_chat()
    st.session_state.qa_mode = True
    welcome_msg = "Hello! I'm initiating a Q&A session to refine your knowledge base. I will audit existing records, find missing or contradictory data, and ask you specific questions to fill in the gaps. Let's start!"
    st.session_state.messages.append({"role": "assistant", "content": welcome_msg})
    st.session_state.resume_llm = True
    st.rerun()

recent_files = _get_recent_chat_files(15)
if recent_files:
    display_names = []
    for f in recent_files:
        title = _extract_title_from_filename(f)
        # Add date for context
        try:
            mtime = datetime.fromtimestamp(os.path.getmtime(f))
            date_label = mtime.strftime("%b %d")
        except Exception:
            date_label = ""
        display_names.append(f"{title}  ({date_label})")

    # Find current selection index
    current_idx = None
    if st.session_state.chat_file:
        for i, f in enumerate(recent_files):
            if os.path.abspath(f) == os.path.abspath(st.session_state.chat_file):
                current_idx = i
                break

    selected = st.sidebar.selectbox(
        "Recent conversations:",
        options=range(len(display_names)),
        format_func=lambda i: display_names[i],
        index=current_idx,
        placeholder="Select a conversation...",
    )

    if selected is not None and (current_idx is None or selected != current_idx):
        load_conversation(recent_files[selected])
        st.rerun()
else:
    st.sidebar.caption("No previous chats yet.")

st.sidebar.markdown("---")

# ── Worker Status Dashboard ─────────────────────────────────
st.sidebar.subheader("⚙️ Workers")

def _load_worker_dashboard():
    """Load worker status from workers.json and individual state files."""
    data_dir = ALFRED_DIR / "data"
    workers_file = data_dir / "workers.json"

    # Check if daemon is running
    daemon_info = {}
    if workers_file.exists():
        try:
            daemon_info = json.loads(workers_file.read_text())
        except Exception:
            pass

    daemon_pid = daemon_info.get("pid")
    daemon_running = False
    if daemon_pid:
        try:
            os.kill(daemon_pid, 0)  # Signal 0 = check if alive
            daemon_running = True
        except (ProcessLookupError, PermissionError):
            daemon_running = False

    tools_status = daemon_info.get("tools", {})

    # Worker definitions: name, state file, stat extractors
    workers = [
        {
            "name": "Curator",
            "icon": "📥",
            "state_file": "curator_state.json",
            "key": "curator",
            "stats": lambda d: {
                "Processed": len(d.get("processed", {})),
                "Last Run": _fmt_time(d.get("last_run")),
            }
        },
        {
            "name": "Janitor",
            "icon": "🧹",
            "state_file": "janitor_state.json",
            "key": "janitor",
            "stats": lambda d: {
                "Files": len(d.get("files", {})),
                "Sweeps": len(d.get("sweeps", {})),
                "Last Sweep": _fmt_time(_last_sweep_time(d)),
            }
        },
        {
            "name": "Distiller",
            "icon": "🧪",
            "state_file": "distiller_state.json",
            "key": "distiller",
            "stats": lambda d: {
                "Sources": len(d.get("files", {})),
                "Runs": len(d.get("runs", {})),
                "Last Run": _fmt_time(_last_distiller_run(d)),
            }
        },
        {
            "name": "Surveyor",
            "icon": "🔭",
            "state_file": "surveyor_state.json",
            "key": "surveyor",
            "stats": lambda d: {
                "Files": len(d.get("files", {})),
                "Clusters": len(d.get("clusters", {})),
                "Last Run": _fmt_time(d.get("last_run")),
            }
        },
    ]

    return daemon_running, tools_status, workers, data_dir


def _fmt_time(ts_str):
    """Format an ISO timestamp to a short relative/absolute label."""
    if not ts_str:
        return "Never"
    try:
        ts = datetime.fromisoformat(ts_str.replace("Z", "+00:00"))
        now = datetime.now(timezone.utc)
        delta = now - ts
        if delta.total_seconds() < 60:
            return "Just now"
        elif delta.total_seconds() < 3600:
            return f"{int(delta.total_seconds() / 60)}m ago"
        elif delta.total_seconds() < 86400:
            return f"{int(delta.total_seconds() / 3600)}h ago"
        else:
            return f"{int(delta.days)}d ago"
    except Exception:
        return ts_str[:10] if ts_str else "?"


def _last_sweep_time(d):
    """Get the timestamp of the last janitor sweep."""
    sweeps = d.get("sweeps", {})
    if isinstance(sweeps, dict) and sweeps:
        last_key = list(sweeps.keys())[-1]
        return sweeps[last_key].get("timestamp")
    return None


def _last_distiller_run(d):
    """Get the timestamp of the last distiller run."""
    runs = d.get("runs", {})
    if isinstance(runs, dict) and runs:
        last_key = list(runs.keys())[-1]
        return runs[last_key].get("timestamp")
    return None


try:
    daemon_running, tools_status, workers, data_dir = _load_worker_dashboard()

    # Daemon status indicator
    if daemon_running:
        st.sidebar.markdown("🟢 **Daemon Running**")
    else:
        st.sidebar.markdown("🔴 **Daemon Stopped**")

    for w in workers:
        tool_info = tools_status.get(w["key"], {})
        is_running = tool_info.get("status") == "running" and daemon_running
        status_dot = "🟢" if is_running else "⚪"
        restarts = tool_info.get("restarts", 0)
        restart_badge = f" ⚠️{restarts}" if restarts > 0 else ""

        # Load state file for stats
        state_path = data_dir / w["state_file"]
        stats = {}
        if state_path.exists():
            try:
                state_data = json.loads(state_path.read_text())
                stats = w["stats"](state_data)
            except Exception:
                stats = {"Error": "Can't read state"}

        # Render compact worker card
        with st.sidebar.expander(f"{status_dot} {w['icon']} {w['name']}{restart_badge}", expanded=False):
            for label, value in stats.items():
                st.caption(f"**{label}:** {value}")

except Exception as e:
    st.sidebar.caption(f"Worker status unavailable: {e}")

st.sidebar.markdown("---")

# ── Header & Tabs ───────────────────────────────────────────
st.title("Alfred Dashboard 🤖")

tab_home, tab_chat, tab_analytics = st.tabs(["🏠 Home", "💬 Chat", "📊 Analytics"])

# Track which tab was clicked (for quick action redirects)
if st.session_state.get("active_tab") == "💬 Chat":
    # Reset after redirect
    st.session_state.active_tab = "🏠 Home"

# ── Tool definitions for OpenRouter ─────────────────────────
TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "vault_search",
            "description": "Search the vault for records matching a query. Returns the top 5 most similar records with their content.",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {"type": "string", "description": "The search query text"}
                },
                "required": ["query"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "vault_read",
            "description": "Read the full content of a specific vault record by its relative path.",
            "parameters": {
                "type": "object",
                "properties": {
                    "path": {"type": "string", "description": "Relative path to the record, e.g. 'person/John Smith.md'"}
                },
                "required": ["path"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "vault_list",
            "description": "List all vault records of a given type.",
            "parameters": {
                "type": "object",
                "properties": {
                    "record_type": {"type": "string", "description": "The record type to list, e.g. 'person', 'task', 'project', 'note', 'org', 'decision'"}
                },
                "required": ["record_type"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "vault_edit",
            "description": "Edit an existing vault record. Can set frontmatter fields, append to list fields, or append text to body. REQUIRES USER APPROVAL.",
            "parameters": {
                "type": "object",
                "properties": {
                    "path": {"type": "string", "description": "Relative path, e.g. 'person/John Smith.md'"},
                    "set_fields": {
                        "type": "object",
                        "description": "Fields to set in frontmatter, e.g. {\"status\": \"inactive\", \"role\": \"CEO\"}",
                        "additionalProperties": {"type": "string"}
                    },
                    "append_fields": {
                        "type": "object",
                        "description": "Fields to append to (list fields), e.g. {\"tags\": \"urgent\"}",
                        "additionalProperties": {"type": "string"}
                    },
                    "body_append": {"type": "string", "description": "Text to append to the record body"}
                },
                "required": ["path"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "vault_create",
            "description": "Create a new vault record. REQUIRES USER APPROVAL.",
            "parameters": {
                "type": "object",
                "properties": {
                    "record_type": {"type": "string", "description": "Record type: person, org, project, task, note, event, decision, assumption, constraint, etc."},
                    "name": {"type": "string", "description": "Name/title of the new record"},
                    "set_fields": {
                        "type": "object",
                        "description": "Frontmatter fields to set, e.g. {\"status\": \"active\", \"priority\": \"high\"}",
                        "additionalProperties": {"type": "string"}
                    },
                    "body": {"type": "string", "description": "Body content for the record"}
                },
                "required": ["record_type", "name"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "vault_delete",
            "description": "Delete a vault record. REQUIRES USER APPROVAL. Only use for garbage or test records.",
            "parameters": {
                "type": "object",
                "properties": {
                    "path": {"type": "string", "description": "Relative path to the record to delete"}
                },
                "required": ["path"]
            }
        }
    },
    # ── Google Workspace Tools ──────────────────────────────
    {
        "type": "function",
        "function": {
            "name": "gmail_search",
            "description": "Search Gmail messages. Uses Gmail search syntax (e.g. 'from:boss@company.com', 'subject:meeting', 'newer_than:2d', 'is:unread').",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {"type": "string", "description": "Gmail search query"},
                    "max_results": {"type": "integer", "description": "Max results (default 10)", "default": 10}
                },
                "required": ["query"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "gmail_read",
            "description": "Read the full content of a specific Gmail message by its ID (get IDs from gmail_search).",
            "parameters": {
                "type": "object",
                "properties": {
                    "message_id": {"type": "string", "description": "Gmail message ID"}
                },
                "required": ["message_id"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "gmail_send",
            "description": "Send an email via Gmail. REQUIRES USER APPROVAL.",
            "parameters": {
                "type": "object",
                "properties": {
                    "to": {"type": "string", "description": "Recipient email address"},
                    "subject": {"type": "string", "description": "Email subject"},
                    "body": {"type": "string", "description": "Email body text"}
                },
                "required": ["to", "subject", "body"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "calendar_events",
            "description": "List upcoming Google Calendar events for the next N days.",
            "parameters": {
                "type": "object",
                "properties": {
                    "days_ahead": {"type": "integer", "description": "Days to look ahead (default 7)", "default": 7}
                }
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "calendar_create",
            "description": "Create a new Google Calendar event. REQUIRES USER APPROVAL.",
            "parameters": {
                "type": "object",
                "properties": {
                    "summary": {"type": "string", "description": "Event title"},
                    "start": {"type": "string", "description": "Start time ISO format, e.g. '2026-03-04T09:00:00'"},
                    "end": {"type": "string", "description": "End time ISO format"},
                    "description": {"type": "string", "description": "Event description", "default": ""}
                },
                "required": ["summary", "start", "end"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "drive_search",
            "description": "Search Google Drive files by content or name.",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {"type": "string", "description": "Search query"}
                },
                "required": ["query"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "drive_read",
            "description": "Read the content of a Google Drive file (Docs exported as text, Sheets as CSV).",
            "parameters": {
                "type": "object",
                "properties": {
                    "file_id": {"type": "string", "description": "Google Drive file ID (from drive_search)"}
                },
                "required": ["file_id"]
            }
        }
    },
    # ── Manus AI Agent Tools ────────────────────────────────────
    {
        "type": "function",
        "function": {
            "name": "manus_task",
            "description": "Delegate a complex task to the Manus AI agent (research, analysis, content generation, data processing). Manus will autonomously plan and execute the task. REQUIRES USER APPROVAL.",
            "parameters": {
                "type": "object",
                "properties": {
                    "prompt": {"type": "string", "description": "Detailed task instructions for Manus to execute"}
                },
                "required": ["prompt"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "manus_status",
            "description": "Check the status and results of a previously created Manus task.",
            "parameters": {
                "type": "object",
                "properties": {
                    "task_id": {"type": "string", "description": "The Manus task ID to check"}
                },
                "required": ["task_id"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "manus_list",
            "description": "List recent Manus tasks and their statuses.",
            "parameters": {
                "type": "object",
                "properties": {
                    "status": {"type": "string", "description": "Filter by status: queued, running, completed, failed", "enum": ["queued", "running", "completed", "failed"]},
                    "limit": {"type": "integer", "description": "Max results (default 10)", "default": 10}
                }
            }
        }
    },
]

# ── Assistant-specific tools (task lifecycle + meeting prep) ─
ASSISTANT_TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "task_complete",
            "description": "Mark a vault task as completed. Sets status to 'done' and adds a completion timestamp. REQUIRES USER APPROVAL.",
            "parameters": {
                "type": "object",
                "properties": {
                    "task_name": {"type": "string", "description": "The task file name (without .md extension), e.g. 'Fix On-Call Examination Link to Show Correct Form'"}
                },
                "required": ["task_name"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "task_snooze",
            "description": "Snooze a task by updating its due date. Sets status to 'snoozed' with a new due date. REQUIRES USER APPROVAL.",
            "parameters": {
                "type": "object",
                "properties": {
                    "task_name": {"type": "string", "description": "The task file name (without .md extension)"},
                    "snooze_until": {"type": "string", "description": "New due date in YYYY-MM-DD format, e.g. '2026-04-07'"}
                },
                "required": ["task_name", "snooze_until"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "task_list_active",
            "description": "List all active/todo tasks from the vault, sorted by priority and due date. Returns structured task data.",
            "parameters": {
                "type": "object",
                "properties": {
                    "priority_filter": {"type": "string", "description": "Filter by priority: critical, high, medium, low", "enum": ["critical", "high", "medium", "low"]},
                    "limit": {"type": "integer", "description": "Max tasks to return (default 15)", "default": 15}
                }
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "meeting_prep",
            "description": "Prepare a comprehensive briefing for an upcoming meeting with a person. Searches the vault for their profile, recent emails, calendar events, and related notes/decisions. Returns a structured dossier.",
            "parameters": {
                "type": "object",
                "properties": {
                    "person_name": {"type": "string", "description": "Name of the person you're meeting with"},
                    "meeting_topic": {"type": "string", "description": "Optional topic or context for the meeting", "default": ""}
                },
                "required": ["person_name"]
            }
        }
    },
]

TOOLS = TOOLS + ASSISTANT_TOOLS

SYSTEM_PROMPT = """You are Alfred, a powerful and proactive AI personal assistant for Rami Khouri.

You go beyond simple chat — you anticipate needs, connect the dots across different data sources, and take initiative.

You have THREE main capabilities:

1. **Vault Operations** — The vault contains 5,000+ structured Markdown files (person, org, project, task, note, conversation, decision, assumption, constraint, contradiction, synthesis, etc.).
   Tools: vault_search, vault_read, vault_list, vault_edit, vault_create, vault_delete

2. **Google Workspace** — You can access Rami's Gmail, Google Calendar, and Google Drive.
   Tools: gmail_search, gmail_read, gmail_send, calendar_events, calendar_create, drive_search, drive_read

3. **Manus AI Agent** — You can delegate complex tasks (deep research, analysis, report generation, data processing) to Manus, an autonomous AI agent platform.
   Tools: manus_task (creates a task, requires approval), manus_status (check results), manus_list (list tasks)

Guidelines:
- Be conversational, helpful, and concise but thorough. You are a serious assistant, not a toy.
- When asked "what should I focus on?", use calendar_events + vault_list (tasks) + gmail_search to give a prioritized briefing.
- When discussing a person, proactively search for their vault record AND recent emails for full context.
- When the user asks about emails, use gmail_search. For calendar questions, use calendar_events.
- When the user asks a vault question, use vault_search or vault_read.
- For complex research or analysis that goes beyond the vault, use manus_task to delegate to Manus.
- If you need to ask the user questions to gather information, ask short, direct questions. **Cluster your questions** into groups of 3-5 at a time rather than asking one by one.
- Read tools execute immediately. Write tools (vault_edit, vault_create, vault_delete, gmail_send, calendar_create, manus_task) require user approval.
- Summarize information naturally — don't dump raw data.
- If you don't find relevant information, say so honestly.
- You have memory of past conversations — reference previous chats naturally when relevant.
- The user's timezone is Asia/Jerusalem (UTC+3).
- Today's date is """ + datetime.now().strftime("%A, %B %d, %Y") + """.

**Task Lifecycle:**
- When the user says a task is done (e.g., "mark X as done", "completed X"), use `task_complete`.
- When the user wants to postpone a task (e.g., "snooze X", "postpone X to next week"), use `task_snooze` with a concrete date.
- When the user asks "what tasks do I have?" or "what's on my plate?", use `task_list_active`.
- When the user has an upcoming meeting with someone, proactively offer to run `meeting_prep`.
- After completing a task, suggest the next highest-priority task to focus on."""

QA_MODE_PROMPT = """
CURRENT MODE: KNOWLEDGE BASE REFINEMENT Q&A
Your sole purpose right now is to refine and fix the knowledge base where data is missing or contradictory.

Rules for this mode:
1. First, use read tools to audit the vault (especially Person and Org records relevant to the user).
2. Look for EMPTY fields, CONTRADICTIONS, or obviously missing links.
3. Formulate smart, highly specific, CLOSE-ENDED questions (Yes/No).
4. Do NOT ask open-ended questions like "Tell me about...".
5. Phrase your questions to show you already know some context. Present the broken/missing data, then ask ONE question.
6. Provide an explicitly stated option for the user to answer "Not relevant" or "Not enough information".
7. Ask exactly ONE question at a time. Wait for the user's answer before asking the next.
8. Once you get an answer, queue the necessary write operations immediately without asking, then proceed to your next question.
"""

READ_TOOLS = {"vault_search", "vault_read", "vault_list", "gmail_search", "gmail_read", "calendar_events", "drive_search", "drive_read", "manus_status", "manus_list", "task_list_active", "meeting_prep"}
WRITE_TOOLS = {"vault_edit", "vault_create", "vault_delete", "gmail_send", "calendar_create", "manus_task", "task_complete", "task_snooze"}

# ── Tool execution ──────────────────────────────────────────

def get_embedding(text):
    resp = requests.post("http://localhost:11434/api/embeddings", json={"model": "nomic-embed-text", "prompt": text})
    return resp.json()["embedding"]

def run_vault_cmd(args, stdin_text=None):
    cmd = ["alfred", "vault"] + args
    env = {**os.environ, "ALFRED_VAULT_PATH": str(VAULT_PATH)}
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=30, cwd=str(ALFRED_DIR),
                           env=env,
                           stdin=subprocess.PIPE if stdin_text else subprocess.DEVNULL, input=stdin_text)
        return r.returncode == 0, (r.stdout.strip() or r.stderr.strip())
    except Exception as e:
        return False, str(e)

def exec_tool(name, args):
    """Execute a read-only tool and return the result as a string."""
    if name == "vault_search":
        if not milvus:
            return "Milvus is not connected."
        try:
            vec = get_embedding(args["query"])
            results = milvus.search(collection_name="vault_embeddings", data=[vec], limit=5,
                                    output_fields=["record_type", "name"])
            if not results[0]:
                return "No matching records found."
            lines = []
            for res in results[0]:
                rel = res["id"]
                nm = res["entity"].get("name", rel)
                tp = res["entity"].get("record_type", "?")
                fp = VAULT_PATH / rel
                try:
                    content = fp.read_text("utf-8")[:2000]
                except Exception:
                    content = "(unreadable)"
                lines.append(f"--- {nm} ({tp}) [{rel}] ---\n{content}")
            return "\n\n".join(lines)
        except Exception as e:
            return f"Search error: {e}"

    elif name == "vault_read":
        fp = VAULT_PATH / args["path"]
        try:
            return fp.read_text("utf-8")[:4000]
        except Exception as e:
            return f"Read error: {e}"

    elif name == "vault_list":
        record_type = args.get("record_type") or args.get("type", "person")
        record_type = str(record_type).lower()  # normalize to lower case

        ok, out = run_vault_cmd(["list", record_type])
        with open(ALFRED_DIR / "data" / "tool_debug.log", "a") as f:
            f.write(f"--- vault_list {record_type} ---\nok: {ok}\nout_len: {len(out)}\nout: {out[:300]}\n\n")

        if not ok:
            return f"List error: {out}"
        try:
            data = json.loads(out)
            results = data.get("results", [])
            lines = [f"Found {data.get('count', 0)} records of type '{record_type}':"]
            for i, r in enumerate(results[:50]): # Limit to 50 to avoid massive context
                lines.append(f"{i+1}. {r.get('name', '')} (Status: {r.get('status', 'none')}) - Path: {r.get('path', '')}")
            if len(results) > 50:
                lines.append(f"... and {len(results) - 50} more records.")
            lines.append("\nUse 'vault_read' with the exact Path above to inspect details.")
            return "\n".join(lines)
        except Exception as e:
            return f"Error parsing list output: {e}\nRaw output: {out[:500]}"

    # ── Google tools ──
    elif name == "gmail_search":
        try:
            results = gc.gmail_search(args["query"], args.get("max_results", 10))
            return json.dumps(results, indent=2, ensure_ascii=False)
        except Exception as e:
            return f"Gmail search error: {e}"

    elif name == "gmail_read":
        try:
            result = gc.gmail_read(args["message_id"])
            return json.dumps(result, indent=2, ensure_ascii=False)
        except Exception as e:
            return f"Gmail read error: {e}"

    elif name == "calendar_events":
        try:
            events = gc.calendar_list_events(args.get("days_ahead", 7))
            return json.dumps(events, indent=2, ensure_ascii=False)
        except Exception as e:
            return f"Calendar error: {e}"

    elif name == "drive_search":
        try:
            results = gc.drive_search(args["query"])
            return json.dumps(results, indent=2, ensure_ascii=False)
        except Exception as e:
            return f"Drive search error: {e}"

    elif name == "drive_read":
        try:
            return gc.drive_read(args["file_id"])
        except Exception as e:
            return f"Drive read error: {e}"

    # ── Manus tools ──
    elif name == "manus_status":
        try:
            result = manus.get_task(args["task_id"])
            return json.dumps(result, indent=2, ensure_ascii=False)
        except Exception as e:
            return f"Manus status error: {e}"

    elif name == "manus_list":
        try:
            results = manus.list_tasks(args.get("status"), args.get("limit", 10))
            return json.dumps(results, indent=2, ensure_ascii=False)
        except Exception as e:
            return f"Manus list error: {e}"

    # ── Task Lifecycle tools ──
    elif name == "task_list_active":
        try:
            tasks = get_active_tasks()
            pf = args.get("priority_filter")
            if pf:
                tasks = [t for t in tasks if t["priority"].lower() == pf.lower()]
            limit = args.get("limit", 15)
            tasks = tasks[:limit]
            if not tasks:
                return "No active tasks found" + (f" with priority '{pf}'" if pf else "") + "."
            lines = [f"Found {len(tasks)} active tasks:"]
            for i, t in enumerate(tasks, 1):
                p = f" [{t['priority']}]" if t['priority'] else ""
                d = f" (due: {t['deadline']})" if t['deadline'] else ""
                lines.append(f"{i}. {t['name']}{p}{d} — `{t['path']}`")
            return "\n".join(lines)
        except Exception as e:
            return f"Task list error: {e}"

    elif name == "meeting_prep":
        try:
            person = args["person_name"]
            topic = args.get("meeting_topic", "")
            dossier_parts = [f"# Meeting Prep Dossier: {person}"]
            if topic:
                dossier_parts.append(f"**Meeting Topic:** {topic}\n")

            # 1. Search vault for person record
            person_dir = VAULT_PATH / "person"
            person_file = None
            if person_dir.exists():
                for f in person_dir.glob("*.md"):
                    if person.lower().replace(" ", "-") in f.stem.lower().replace(" ", "-"):
                        person_file = f
                        break
                    if person.lower() in f.stem.lower():
                        person_file = f
                        break

            if person_file:
                content = person_file.read_text("utf-8", errors="replace")[:3000]
                dossier_parts.append(f"## 👤 Vault Profile\n```\n{content}\n```")
            else:
                dossier_parts.append(f"## 👤 Vault Profile\n*No person record found for '{person}'. Consider creating one.*")

            # 2. Search recent emails
            try:
                emails = gc.gmail_search(f"from:{person} OR to:{person}", max_results=5)
                if emails:
                    dossier_parts.append(f"## 📧 Recent Emails ({len(emails)} found)")
                    for em in emails[:5]:
                        sender = em.get("from", "")
                        subj = em.get("subject", "(no subject)")
                        snippet = em.get("snippet", "")[:120]
                        date = em.get("date", "")
                        dossier_parts.append(f"- **{subj}** — {sender} ({date})\n  _{snippet}_")
            except Exception:
                dossier_parts.append("## 📧 Recent Emails\n*Gmail unavailable*")

            # 3. Search vault for related notes, decisions, tasks
            if milvus:
                try:
                    search_query = f"{person} {topic}" if topic else person
                    vec = get_embedding(search_query)
                    results = milvus.search(collection_name="vault_embeddings", data=[vec], limit=5,
                                            output_fields=["record_type", "name"])
                    if results[0]:
                        dossier_parts.append(f"## 🔗 Related Vault Records")
                        for res in results[0]:
                            nm = res["entity"].get("name", "")
                            tp = res["entity"].get("record_type", "?")
                            rel_path = res["id"]
                            dossier_parts.append(f"- [{tp}] {nm} — `{rel_path}`")
                except Exception:
                    pass

            # 4. Recent calendar events with this person
            try:
                events = gc.calendar_list_events(days_ahead=14, max_results=20)
                related = [e for e in events if person.lower() in json.dumps(e).lower()]
                if related:
                    dossier_parts.append(f"## 📅 Upcoming Calendar Events")
                    for e in related[:5]:
                        start = e.get("start", "")
                        summ = e.get("summary", "No title")
                        dossier_parts.append(f"- {start[:16]} — {summ}")
            except Exception:
                pass

            return "\n\n".join(dossier_parts)
        except Exception as e:
            return f"Meeting prep error: {e}"

    return "Unknown tool."

def build_vault_cmd_args(name, args):
    """Build the alfred vault CLI args for a write tool."""
    if name == "vault_edit":
        cmd = ["edit", args["path"]]
        for k, v in args.get("set_fields", {}).items():
            cmd += ["--set", f"{k}={v}"]
        for k, v in args.get("append_fields", {}).items():
            cmd += ["--append", f"{k}={v}"]
        if args.get("body_append"):
            cmd += ["--body-append", args["body_append"]]
        return cmd, None

    elif name == "vault_create":
        cmd = ["create", args["record_type"], args["name"]]
        for k, v in args.get("set_fields", {}).items():
            cmd += ["--set", f"{k}={v}"]
        body = args.get("body")
        if body:
            cmd += ["--body-stdin"]
            return cmd, body
        return cmd, None

    elif name == "vault_delete":
        return ["delete", args["path"]], None

    return [], None

def describe_action(name, args):
    """Human-readable description of a write action."""
    if name == "vault_edit":
        parts = [f"**Edit** `{args['path']}`"]
        for k, v in args.get("set_fields", {}).items():
            parts.append(f"  Set `{k}` → `{v}`")
        for k, v in args.get("append_fields", {}).items():
            parts.append(f"  Append `{v}` to `{k}`")
        if args.get("body_append"):
            parts.append(f"  Append to body: _{args['body_append'][:80]}_")
        return "\n".join(parts)
    elif name == "vault_create":
        fields = args.get("set_fields", {})
        fstr = ", ".join(f"`{k}={v}`" for k, v in fields.items()) if fields else "defaults"
        return f"**Create** `{args['record_type']}/{args['name']}.md` with {fstr}"
    elif name == "vault_delete":
        return f"**Delete** `{args['path']}`"
    elif name == "gmail_send":
        return f"📧 **Send email** to `{args['to']}`\n  Subject: _{args['subject']}_\n  Body: _{args['body'][:120]}_"
    elif name == "calendar_create":
        return f"📅 **Create event** \"{args['summary']}\"\n  Start: `{args['start']}`\n  End: `{args['end']}`"
    elif name == "manus_task":
        return f"🤖 **Delegate to Manus AI**\n  Task: _{args['prompt'][:200]}_"
    elif name == "task_complete":
        return f"✅ **Mark task as done:** `{args['task_name']}`"
    elif name == "task_snooze":
        return f"⏰ **Snooze task:** `{args['task_name']}` until `{args['snooze_until']}`"
    return f"Unknown action: {name}"

# ── OpenRouter API call ─────────────────────────────────────

def call_llm(messages, tools=None):
    headers = {"Authorization": f"Bearer {OPENROUTER_API_KEY}", "Content-Type": "application/json"}
    body = {
        "model": "anthropic/claude-sonnet-4.6",
        "messages": messages,
        "reasoning": {"effort": "high"},
    }
    if tools:
        body["tools"] = tools
    resp = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=body)
    if resp.status_code != 200:
        err_msg = f"API error {resp.status_code}: {resp.text[:200]}"
        print(err_msg)
        return None, err_msg
    try:
        resp_json = resp.json()
        choice = resp_json["choices"][0]
        return choice["message"], None
    except Exception as e:
        print(f"Error parsing API response: {e}\nResponse text: {resp.text[:500]}")
        return None, f"Parsing error: {e}"

# ── Tab: Home (Daily Briefing) ──────────────────────────────
with tab_home:
    render_briefing()

# ── Tab: Analytics ──────────────────────────────────────────
with tab_analytics:
    render_analytics()

# ── Tab: Chat ───────────────────────────────────────────────
with tab_chat:
    if st.session_state.chat_title:
        st.caption(f"💬 {st.session_state.chat_title}")
    else:
        st.markdown("Chat with your vault. Alfred can **search**, **edit**, **create**, and **delete** records — with your approval.")

    for msg in st.session_state.messages:
        if msg["role"] in ("user", "assistant"):
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])

    # ── Handle pending write action ─────────────────────────────

    if st.session_state.get("pending_actions"):
        count = len(st.session_state.pending_actions)
        es = "s" if count > 1 else ""
        st.warning(f"⚡ **Alfred wants to perform {count} action{es}:**")

        for p in st.session_state.pending_actions:
            name = p["name"]
            args = p["args"]
            desc = describe_action(name, args).replace('\n', '\n  ')
            st.markdown(f"- {desc}")

        col1, col2 = st.columns(2)
        with col1:
            if st.button("✅ Approve All", use_container_width=True, type="primary"):
                # First, append the assistant message that spawned these tools
                if st.session_state.pending_assistant_msg:
                    st.session_state.messages.append(st.session_state.pending_assistant_msg)

                for p in st.session_state.pending_actions:
                    name = p["name"]
                    args = p["args"]
                    tool_call_id = p["tool_call_id"]

                    # Execute based on tool type
                    if name in {"vault_edit", "vault_create", "vault_delete"}:
                        cmd_args, stdin = build_vault_cmd_args(name, args)
                        ok, output = run_vault_cmd(cmd_args, stdin)
                        if ok:
                            result_msg = f"Done! `{name}` succeeded.\n```\n{output}\n```"
                        else:
                            result_msg = f"Failed to execute `{name}`: {output}"
                    elif name == "gmail_send":
                        try:
                            output = gc.gmail_send(args["to"], args["subject"], args["body"])
                            result_msg = output
                        except Exception as e:
                            result_msg = f"Failed to send email: {e}"
                    elif name == "calendar_create":
                        try:
                            output = gc.calendar_create_event(args["summary"], args["start"], args["end"], args.get("description", ""))
                            result_msg = output
                        except Exception as e:
                            result_msg = f"Failed to create event: {e}"
                    elif name == "manus_task":
                        try:
                            task = manus.create_task(args["prompt"])
                            task_id = task.get("task_id", "unknown")
                            result_msg = f"Manus task created! ID: `{task_id}` (status: {task.get('status', 'queued')})\n\nThe task is running in the background. Ask me to check the status with: *\"Check Manus task {task_id}\"*"
                        except Exception as e:
                            result_msg = f"Failed to create Manus task: {e}"
                    elif name == "task_complete":
                        task_path = f"task/{args['task_name']}.md"
                        completed_date = datetime.now().strftime("%Y-%m-%d")
                        cmd_args = ["edit", task_path, "--set", f"status=done", "--set", f"completed={completed_date}"]
                        ok, output = run_vault_cmd(cmd_args)
                        if ok:
                            result_msg = f"\u2705 Task '{args['task_name']}' marked as done! (completed: {completed_date})"
                        else:
                            result_msg = f"Failed to complete task: {output}"
                    elif name == "task_snooze":
                        task_path = f"task/{args['task_name']}.md"
                        snooze_date = args["snooze_until"]
                        cmd_args = ["edit", task_path, "--set", f"status=snoozed", "--set", f"due={snooze_date}"]
                        ok, output = run_vault_cmd(cmd_args)
                        if ok:
                            result_msg = f"\u23f0 Task '{args['task_name']}' snoozed until {snooze_date}"
                        else:
                            result_msg = f"Failed to snooze task: {output}"
                    else:
                        result_msg = f"Unknown write tool: {name}"

                    # Append the proper tool role message
                    st.session_state.messages.append({
                        "role": "tool",
                        "tool_call_id": tool_call_id,
                        "content": result_msg
                    })

                st.session_state.pending_actions = []
                st.session_state.pending_assistant_msg = None
                st.session_state.resume_llm = True
                save_conversation()
                st.rerun()
        with col2:
            if st.button("❌ Reject All", use_container_width=True):
                if st.session_state.pending_assistant_msg:
                    st.session_state.messages.append(st.session_state.pending_assistant_msg)

                for p in st.session_state.pending_actions:
                    st.session_state.messages.append({
                        "role": "tool",
                        "tool_call_id": p["tool_call_id"],
                        "content": "User rejected this action."
                    })
                st.session_state.pending_actions = []
                st.session_state.pending_assistant_msg = None
                st.session_state.resume_llm = True
                save_conversation()
                st.rerun()

# ── Chat input (outside tabs for persistence) ──────────────

prompt = st.chat_input("Ask Alfred a question...", key="chat_input")
should_run_llm = False

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    should_run_llm = True
elif st.session_state.get("resume_llm"):
    should_run_llm = True
    st.session_state.resume_llm = False

if should_run_llm:
    # Set chat_started on first message
    if not st.session_state.chat_started:
        st.session_state.chat_started = datetime.now()

    with st.spinner("Alfred is thinking..."):
        # Build system prompt with memory context
        memory_ctx = get_memory_context() if not st.session_state.chat_title else ""
        contextual_ctx = get_contextual_briefing_text()
        full_system = SYSTEM_PROMPT + contextual_ctx + memory_ctx
        
        if st.session_state.get("qa_mode"):
            full_system += "\n\n" + QA_MODE_PROMPT

        # Build conversation for the LLM (system + last 15 messages to ensure tool context isn't lost)
        llm_msgs = [{"role": "system", "content": full_system}]
        for m in st.session_state.messages[-15:]:
            msg_obj = {"role": m["role"], "content": m.get("content", "")}
            if "tool_calls" in m:
                msg_obj["tool_calls"] = m["tool_calls"]
            if "tool_call_id" in m:
                msg_obj["tool_call_id"] = m["tool_call_id"]
            llm_msgs.append(msg_obj)

        # Agentic loop: let the LLM call tools iteratively
        MAX_ROUNDS = 15
        for round_num in range(MAX_ROUNDS):
            print(f"Calling LLM, round {round_num}")
            reply, err = call_llm(llm_msgs, tools=TOOLS)
            if err:
                print(f"LLM Loop broken due to error: {err}")
                st.error(err)
                break

            # If LLM wants to call tool(s)
            tool_calls = reply.get("tool_calls")
            if tool_calls:
                # Add assistant message with tool calls to context
                llm_msgs.append(reply)

                # Render any text the LLM sent along with the tool calls
                text = reply.get("content", "")
                if text:
                    with st.chat_message("assistant"):
                        st.markdown(text)
                    visible_msg = {"role": "assistant", "content": text}
                    st.session_state.messages.append(visible_msg)

                has_write_tools = False
                pending_list = []

                for tc in tool_calls:
                    fn_name = tc["function"]["name"]
                    fn_args = json.loads(tc["function"]["arguments"]) if isinstance(tc["function"]["arguments"], str) else tc["function"]["arguments"]

                    if fn_name in READ_TOOLS:
                        # Execute read tools immediately
                        result = exec_tool(fn_name, fn_args)
                        llm_msgs.append({
                            "role": "tool",
                            "tool_call_id": tc["id"],
                            "content": result
                        })
                    elif fn_name in WRITE_TOOLS:
                        # Queue write tools for user approval
                        has_write_tools = True
                        pending_list.append({
                            "name": fn_name,
                            "args": fn_args,
                            "tool_call_id": tc["id"]
                        })
                    else:
                        llm_msgs.append({
                            "role": "tool",
                            "tool_call_id": tc["id"],
                            "content": f"Unknown tool: {fn_name}"
                        })

                if has_write_tools:
                    reply_copy = dict(reply)
                    reply_copy["content"] = ""
                    st.session_state.pending_assistant_msg = reply_copy
                    
                    st.session_state.pending_actions = pending_list
                    save_conversation()
                    st.rerun()

                # After processing read tools, loop back so LLM can use the results
                continue

            # No tool calls — LLM gave a final text answer
            text = reply.get("content", "")
            if text:
                with st.chat_message("assistant"):
                    st.markdown(text)
                st.session_state.messages.append({"role": "assistant", "content": text})

                # Auto-save conversation and generate title
                save_conversation()
                generate_title()
            break
        else:
            # Reached MAX_ROUNDS without breaking
            err_msg = "Alfred needed to think for too long and was paused. Try asking a more specific question."
            with st.chat_message("assistant"):
                st.markdown(err_msg)
            st.session_state.messages.append({"role": "assistant", "content": err_msg})
            
    st.rerun()

