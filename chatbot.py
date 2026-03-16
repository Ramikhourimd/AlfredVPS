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
from datetime import datetime
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

# ── Header ──────────────────────────────────────────────────
st.title("Alfred Interactive Dashboard 🤖")
if st.session_state.chat_title:
    st.caption(f"💬 {st.session_state.chat_title}")
else:
    st.markdown("Chat with your vault. Alfred can **search**, **edit**, **create**, and **delete** records — with your approval.")

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

SYSTEM_PROMPT = """You are Alfred, a smart and friendly AI assistant managing Rami Khouri's personal knowledge vault and connected services.

You have THREE main capabilities:

1. **Vault Operations** — The vault contains structured Markdown files (person, org, project, task, note, conversation, decision, etc.).
   Tools: vault_search, vault_read, vault_list, vault_edit, vault_create, vault_delete

2. **Google Workspace** — You can access Rami's Gmail, Google Calendar, and Google Drive.
   Tools: gmail_search, gmail_read, gmail_send, calendar_events, calendar_create, drive_search, drive_read

3. **Manus AI Agent** — You can delegate complex tasks (deep research, analysis, report generation, data processing) to Manus, an autonomous AI agent platform.
   Tools: manus_task (creates a task, requires approval), manus_status (check results), manus_list (list tasks)

Guidelines:
- Be conversational, helpful, and concise. Don't be overly formal.
- When the user asks about emails, use gmail_search. For calendar questions, use calendar_events.
- When the user asks a vault question, use vault_search or vault_read.
- For complex research or analysis that goes beyond the vault, use manus_task to delegate to Manus.
- If you need to ask the user questions to gather information (e.g., to build a profile), ask short, direct questions. **Cluster your questions** into groups of 3-5 at a time rather than asking one by one.
- Read tools execute immediately. Write tools (vault_edit, vault_create, vault_delete, gmail_send, calendar_create, manus_task) require user approval. You can call MULTIPLE write tools in a single response, and they will be queued for the user to approve all at once.
- Summarize information naturally — don't dump raw data.
- If you don't find relevant information, say so honestly.
- You have memory of past conversations — reference previous chats naturally when relevant.
- The user's timezone is Asia/Jerusalem (UTC+2)."""

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

READ_TOOLS = {"vault_search", "vault_read", "vault_list", "gmail_search", "gmail_read", "calendar_events", "drive_search", "drive_read", "manus_status", "manus_list"}
WRITE_TOOLS = {"vault_edit", "vault_create", "vault_delete", "gmail_send", "calendar_create", "manus_task"}

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

# ── Display chat history ────────────────────────────────────

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

# ── Chat input ──────────────────────────────────────────────

prompt = st.chat_input("Ask Alfred a question...", key="chat_input")
should_run_llm = False

if prompt:
    st.chat_message("user").markdown(prompt)
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
        full_system = SYSTEM_PROMPT + memory_ctx
        
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
                    # We must append a copy without tool_calls to the visible messages array
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
                        # We already rendered the text above if it existed
                        # The pending assistant msg should just hold the tool calls for the retry loop
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
