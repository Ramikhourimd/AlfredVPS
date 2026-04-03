"""
Alfred Extensions System — Skills, MCP Servers, and Plugins
Provides a Claude-desktop-like extensibility framework.
"""
import json
import os
import subprocess
import threading
import time
import uuid
from pathlib import Path
from datetime import datetime

import streamlit as st
import yaml

# ── Paths ───────────────────────────────────────────────────
ALFRED_DIR = Path(__file__).parent
DATA_DIR = ALFRED_DIR / "data"
SKILLS_DIR = DATA_DIR / "skills"
PLUGINS_DIR = DATA_DIR / "plugins"
MCP_CONFIG = DATA_DIR / "mcp_config.json"

SKILLS_DIR.mkdir(parents=True, exist_ok=True)
PLUGINS_DIR.mkdir(parents=True, exist_ok=True)


# ═══════════════════════════════════════════════════════════
#  SKILLS MANAGER
# ═══════════════════════════════════════════════════════════

class SkillManager:
    """Manages markdown-based skill files with YAML frontmatter."""

    @staticmethod
    def _parse_skill(path: Path) -> dict:
        """Parse a skill .md file into a dict."""
        try:
            text = path.read_text("utf-8", errors="replace")
            if text.startswith("---"):
                parts = text.split("---", 2)
                if len(parts) >= 3:
                    meta = yaml.safe_load(parts[1]) or {}
                    body = parts[2].strip()
                    return {
                        "file": path.name,
                        "path": str(path),
                        "name": meta.get("name", path.stem),
                        "description": meta.get("description", ""),
                        "icon": meta.get("icon", "🔧"),
                        "enabled": meta.get("enabled", False),
                        "instructions": body,
                    }
            # Fallback: no frontmatter
            return {
                "file": path.name,
                "path": str(path),
                "name": path.stem.replace("_", " ").title(),
                "description": "",
                "icon": "🔧",
                "enabled": False,
                "instructions": text.strip(),
            }
        except Exception as e:
            return {"file": path.name, "path": str(path), "name": path.stem,
                    "description": f"Error: {e}", "icon": "❌", "enabled": False, "instructions": ""}

    @staticmethod
    def list_skills() -> list[dict]:
        """Return all skills from data/skills/."""
        skills = []
        for f in sorted(SKILLS_DIR.glob("*.md")):
            skills.append(SkillManager._parse_skill(f))
        return skills

    @staticmethod
    def get_active_skills_prompt() -> str:
        """Return combined prompt from all enabled skills."""
        parts = []
        for skill in SkillManager.list_skills():
            if skill["enabled"] and skill["instructions"]:
                parts.append(f"\n\n**[Skill: {skill['name']}]**\n{skill['instructions']}")
        if parts:
            return "\n\n--- ACTIVE SKILLS ---" + "".join(parts)
        return ""

    @staticmethod
    def toggle_skill(filename: str, enabled: bool):
        """Toggle a skill's enabled state by rewriting its frontmatter."""
        path = SKILLS_DIR / filename
        if not path.exists():
            return
        text = path.read_text("utf-8", errors="replace")
        if text.startswith("---"):
            parts = text.split("---", 2)
            if len(parts) >= 3:
                meta = yaml.safe_load(parts[1]) or {}
                meta["enabled"] = enabled
                new_front = yaml.dump(meta, default_flow_style=False, allow_unicode=True).strip()
                path.write_text(f"---\n{new_front}\n---\n{parts[2].strip()}\n", encoding="utf-8")

    @staticmethod
    def create_skill(name: str, description: str, icon: str, instructions: str) -> str:
        """Create a new skill file. Returns the filename."""
        slug = name.lower().replace(" ", "_").replace("-", "_")
        slug = "".join(c for c in slug if c.isalnum() or c == "_")
        filename = f"{slug}.md"
        path = SKILLS_DIR / filename
        content = f"""---
name: {name}
description: {description}
icon: {icon}
enabled: false
---
{instructions.strip()}
"""
        path.write_text(content, encoding="utf-8")
        return filename

    @staticmethod
    def delete_skill(filename: str):
        """Delete a skill file."""
        path = SKILLS_DIR / filename
        if path.exists():
            path.unlink()

    @staticmethod
    def update_skill(filename: str, name: str, description: str, icon: str, instructions: str):
        """Update an existing skill."""
        path = SKILLS_DIR / filename
        if not path.exists():
            return
        # Read current state to preserve enabled
        text = path.read_text("utf-8", errors="replace")
        enabled = False
        if text.startswith("---"):
            parts = text.split("---", 2)
            if len(parts) >= 3:
                meta = yaml.safe_load(parts[1]) or {}
                enabled = meta.get("enabled", False)

        content = f"""---
name: {name}
description: {description}
icon: {icon}
enabled: {str(enabled).lower()}
---
{instructions.strip()}
"""
        path.write_text(content, encoding="utf-8")


# ═══════════════════════════════════════════════════════════
#  MCP CLIENT
# ═══════════════════════════════════════════════════════════

class MCPClient:
    """Manages MCP server connections via JSON-RPC over stdio."""

    def __init__(self):
        self._servers: dict[str, dict] = {}  # name -> { process, tools, config }
        self._lock = threading.Lock()

    def load_config(self) -> list[dict]:
        """Load MCP server configurations."""
        if MCP_CONFIG.exists():
            try:
                data = json.loads(MCP_CONFIG.read_text("utf-8"))
                return data.get("servers", [])
            except Exception:
                return []
        return []

    def save_config(self, servers: list[dict]):
        """Save MCP server configurations."""
        MCP_CONFIG.write_text(json.dumps({"servers": servers}, indent=2), encoding="utf-8")

    def add_server(self, name: str, command: str, args: list[str], env: dict = None):
        """Add a server to config."""
        configs = self.load_config()
        configs.append({
            "name": name,
            "command": command,
            "args": args,
            "env": env or {},
            "enabled": True,
        })
        self.save_config(configs)

    def remove_server(self, name: str):
        """Remove a server from config and stop it."""
        self.stop_server(name)
        configs = self.load_config()
        configs = [c for c in configs if c["name"] != name]
        self.save_config(configs)

    def toggle_server(self, name: str, enabled: bool):
        """Toggle a server's enabled state."""
        configs = self.load_config()
        for c in configs:
            if c["name"] == name:
                c["enabled"] = enabled
                break
        self.save_config(configs)
        if not enabled:
            self.stop_server(name)

    def start_server(self, config: dict) -> bool:
        """Start an MCP server process and discover its tools."""
        name = config["name"]
        with self._lock:
            if name in self._servers and self._servers[name].get("process"):
                proc = self._servers[name]["process"]
                if proc.poll() is None:
                    return True  # Already running

        try:
            env = {**os.environ, **(config.get("env") or {})}
            proc = subprocess.Popen(
                [config["command"]] + config.get("args", []),
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                env=env,
                text=True,
                bufsize=1,
            )

            # Send initialize request
            init_req = {
                "jsonrpc": "2.0",
                "id": 1,
                "method": "initialize",
                "params": {
                    "protocolVersion": "2024-11-05",
                    "capabilities": {},
                    "clientInfo": {"name": "Alfred", "version": "1.0"}
                }
            }
            proc.stdin.write(json.dumps(init_req) + "\n")
            proc.stdin.flush()

            # Read response with timeout
            proc.stdout.readline()  # Read init response

            # Send initialized notification
            init_notif = {"jsonrpc": "2.0", "method": "notifications/initialized"}
            proc.stdin.write(json.dumps(init_notif) + "\n")
            proc.stdin.flush()

            # Request tool list
            tools_req = {
                "jsonrpc": "2.0",
                "id": 2,
                "method": "tools/list",
                "params": {}
            }
            proc.stdin.write(json.dumps(tools_req) + "\n")
            proc.stdin.flush()

            tools_resp_line = proc.stdout.readline()
            tools = []
            try:
                tools_resp = json.loads(tools_resp_line)
                tools = tools_resp.get("result", {}).get("tools", [])
            except Exception:
                pass

            with self._lock:
                self._servers[name] = {
                    "process": proc,
                    "tools": tools,
                    "config": config,
                    "connected": True,
                    "started_at": datetime.now().isoformat(),
                }
            return True

        except Exception as e:
            with self._lock:
                self._servers[name] = {
                    "process": None,
                    "tools": [],
                    "config": config,
                    "connected": False,
                    "error": str(e),
                }
            return False

    def stop_server(self, name: str):
        """Stop an MCP server process."""
        with self._lock:
            if name in self._servers:
                proc = self._servers[name].get("process")
                if proc and proc.poll() is None:
                    try:
                        proc.terminate()
                        proc.wait(timeout=5)
                    except Exception:
                        try:
                            proc.kill()
                        except Exception:
                            pass
                del self._servers[name]

    def get_server_status(self, name: str) -> dict:
        """Get status of a server."""
        with self._lock:
            if name in self._servers:
                srv = self._servers[name]
                proc = srv.get("process")
                is_running = proc and proc.poll() is None
                return {
                    "connected": is_running,
                    "tool_count": len(srv.get("tools", [])),
                    "tools": srv.get("tools", []),
                    "error": srv.get("error", ""),
                    "started_at": srv.get("started_at", ""),
                }
        return {"connected": False, "tool_count": 0, "tools": [], "error": "Not started"}

    def get_mcp_tools(self) -> list[dict]:
        """Return all tools from connected MCP servers in OpenAI format."""
        all_tools = []
        with self._lock:
            for name, srv in self._servers.items():
                if not srv.get("connected"):
                    continue
                proc = srv.get("process")
                if not proc or proc.poll() is not None:
                    srv["connected"] = False
                    continue
                prefix = name.lower().replace(" ", "_").replace("-", "_")
                for tool in srv.get("tools", []):
                    tool_name = f"mcp_{prefix}__{tool['name']}"
                    all_tools.append({
                        "type": "function",
                        "function": {
                            "name": tool_name,
                            "description": f"[MCP: {name}] {tool.get('description', '')}",
                            "parameters": tool.get("inputSchema", {"type": "object", "properties": {}})
                        }
                    })
        return all_tools

    def exec_tool(self, tool_name: str, args: dict) -> str:
        """Execute a tool call on an MCP server."""
        # tool_name format: mcp_servername__toolname
        parts = tool_name.replace("mcp_", "", 1).split("__", 1)
        if len(parts) != 2:
            return f"Invalid MCP tool name format: {tool_name}"

        server_prefix, real_tool = parts

        with self._lock:
            target = None
            for name, srv in self._servers.items():
                prefix = name.lower().replace(" ", "_").replace("-", "_")
                if prefix == server_prefix:
                    target = srv
                    break

        if not target:
            return f"MCP server not found for tool: {tool_name}"

        proc = target.get("process")
        if not proc or proc.poll() is not None:
            return f"MCP server is not running"

        try:
            req_id = int(time.time() * 1000) % 1000000
            req = {
                "jsonrpc": "2.0",
                "id": req_id,
                "method": "tools/call",
                "params": {
                    "name": real_tool,
                    "arguments": args,
                }
            }
            proc.stdin.write(json.dumps(req) + "\n")
            proc.stdin.flush()

            resp_line = proc.stdout.readline()
            if resp_line:
                resp = json.loads(resp_line)
                result = resp.get("result", {})
                content = result.get("content", [])
                # Flatten content array
                texts = []
                for item in content:
                    if isinstance(item, dict) and item.get("type") == "text":
                        texts.append(item.get("text", ""))
                    elif isinstance(item, str):
                        texts.append(item)
                return "\n".join(texts) if texts else json.dumps(result)
            return "No response from MCP server"
        except Exception as e:
            return f"MCP tool execution error: {e}"

    def start_enabled_servers(self):
        """Start all enabled MCP servers from config."""
        configs = self.load_config()
        for config in configs:
            if config.get("enabled", False):
                self.start_server(config)


# ═══════════════════════════════════════════════════════════
#  PLUGIN MANAGER
# ═══════════════════════════════════════════════════════════

class PluginManager:
    """Manages plugin bundles (skills + MCP configs)."""

    @staticmethod
    def list_plugins() -> list[dict]:
        """List all installed plugins."""
        plugins = []
        for d in sorted(PLUGINS_DIR.iterdir()):
            if d.is_dir():
                manifest = d / "plugin.json"
                if manifest.exists():
                    try:
                        data = json.loads(manifest.read_text("utf-8"))
                        data["path"] = str(d)
                        data["dir_name"] = d.name
                        plugins.append(data)
                    except Exception:
                        plugins.append({
                            "name": d.name,
                            "description": "Invalid plugin manifest",
                            "icon": "❌",
                            "path": str(d),
                            "dir_name": d.name,
                            "enabled": False,
                        })
        return plugins

    @staticmethod
    def get_plugin_skills(plugin: dict) -> list[dict]:
        """Get skills from a plugin."""
        plugin_dir = Path(plugin["path"])
        skills = []
        for skill_rel in plugin.get("skills", []):
            skill_path = plugin_dir / skill_rel
            if skill_path.exists():
                skills.append(SkillManager._parse_skill(skill_path))
        return skills

    @staticmethod
    def toggle_plugin(dir_name: str, enabled: bool):
        """Toggle a plugin's enabled state."""
        manifest = PLUGINS_DIR / dir_name / "plugin.json"
        if manifest.exists():
            data = json.loads(manifest.read_text("utf-8"))
            data["enabled"] = enabled
            manifest.write_text(json.dumps(data, indent=2), encoding="utf-8")


# ═══════════════════════════════════════════════════════════
#  SINGLETON INSTANCES
# ═══════════════════════════════════════════════════════════

# Initialize MCP client as singleton in session state
def get_mcp_client() -> MCPClient:
    """Get or create the MCP client singleton."""
    if "mcp_client" not in st.session_state:
        client = MCPClient()
        client.start_enabled_servers()
        st.session_state.mcp_client = client
    return st.session_state.mcp_client


# ═══════════════════════════════════════════════════════════
#  EXTENSIONS TAB UI
# ═══════════════════════════════════════════════════════════

def render_extensions_tab():
    """Render the full Extensions management tab."""

    # Sub-tabs for Skills / MCPs / Plugins
    sub_skills, sub_mcps, sub_plugins = st.tabs(["🎯 Skills", "🔌 MCP Servers", "📦 Plugins"])

    # ── Skills Sub-Tab ──────────────────────────────────────
    with sub_skills:
        st.markdown("### 🎯 Skills")
        st.caption(
            "Skills are instruction sets that modify Alfred's behavior. "
            "Enable a skill to inject its instructions into every conversation."
        )

        skills = SkillManager.list_skills()
        active_count = sum(1 for s in skills if s["enabled"])
        st.markdown(f"**{len(skills)}** skills installed · **{active_count}** active")

        # Create new skill
        with st.expander("➕ Create New Skill", expanded=False):
            with st.form("create_skill_form", clear_on_submit=True):
                col_name, col_icon = st.columns([4, 1])
                with col_name:
                    new_name = st.text_input("Skill Name", placeholder="e.g., Legal Advisor")
                with col_icon:
                    new_icon = st.text_input("Icon", value="🔧", max_chars=2)
                new_desc = st.text_input("Description", placeholder="Brief description of what this skill does")
                new_instructions = st.text_area(
                    "Instructions",
                    height=200,
                    placeholder="Write the instructions that will be injected into Alfred's system prompt when this skill is active..."
                )
                if st.form_submit_button("✅ Create Skill", type="primary"):
                    if new_name and new_instructions:
                        SkillManager.create_skill(new_name, new_desc, new_icon, new_instructions)
                        st.success(f"Skill '{new_name}' created!")
                        st.rerun()
                    else:
                        st.error("Name and instructions are required.")

        st.markdown("---")

        # Skill cards
        if not skills:
            st.info("No skills installed. Create one above or add `.md` files to `data/skills/`.")
        else:
            for skill in skills:
                with st.container():
                    col_toggle, col_info, col_actions = st.columns([1, 6, 2])

                    with col_toggle:
                        enabled = st.toggle(
                            "on",
                            value=skill["enabled"],
                            key=f"skill_toggle_{skill['file']}",
                            label_visibility="collapsed"
                        )
                        if enabled != skill["enabled"]:
                            SkillManager.toggle_skill(skill["file"], enabled)
                            st.rerun()

                    with col_info:
                        status = "🟢" if skill["enabled"] else "⚪"
                        st.markdown(f"**{skill['icon']} {skill['name']}** {status}")
                        st.caption(skill["description"])

                    with col_actions:
                        c1, c2 = st.columns(2)
                        with c1:
                            if st.button("✏️", key=f"edit_{skill['file']}", help="Edit skill"):
                                st.session_state[f"editing_{skill['file']}"] = True
                                st.rerun()
                        with c2:
                            if st.button("🗑️", key=f"del_{skill['file']}", help="Delete skill"):
                                SkillManager.delete_skill(skill["file"])
                                st.rerun()

                    # Edit expander
                    if st.session_state.get(f"editing_{skill['file']}"):
                        with st.expander(f"✏️ Editing: {skill['name']}", expanded=True):
                            with st.form(f"edit_form_{skill['file']}"):
                                e_col1, e_col2 = st.columns([4, 1])
                                with e_col1:
                                    e_name = st.text_input("Name", value=skill["name"])
                                with e_col2:
                                    e_icon = st.text_input("Icon", value=skill["icon"], max_chars=2)
                                e_desc = st.text_input("Description", value=skill["description"])
                                e_instr = st.text_area("Instructions", value=skill["instructions"], height=200)
                                fc1, fc2 = st.columns(2)
                                with fc1:
                                    if st.form_submit_button("💾 Save", type="primary"):
                                        SkillManager.update_skill(skill["file"], e_name, e_desc, e_icon, e_instr)
                                        del st.session_state[f"editing_{skill['file']}"]
                                        st.success("Skill updated!")
                                        st.rerun()
                                with fc2:
                                    if st.form_submit_button("Cancel"):
                                        del st.session_state[f"editing_{skill['file']}"]
                                        st.rerun()

                    st.markdown("---")

    # ── MCP Servers Sub-Tab ─────────────────────────────────
    with sub_mcps:
        st.markdown("### 🔌 MCP Servers")
        st.caption(
            "MCP (Model Context Protocol) servers provide additional tools to Alfred. "
            "Connect external tool servers to extend Alfred's capabilities."
        )

        mcp_client = get_mcp_client()
        configs = mcp_client.load_config()

        # Add new server
        with st.expander("➕ Add MCP Server", expanded=False):
            with st.form("add_mcp_form", clear_on_submit=True):
                mcp_name = st.text_input("Server Name", placeholder="e.g., Web Search")
                mcp_cmd = st.text_input("Command", placeholder="e.g., npx")
                mcp_args = st.text_input("Arguments (comma-separated)", placeholder="-y, @anthropic/mcp-server-brave-search")
                mcp_env = st.text_area(
                    "Environment Variables (JSON)",
                    placeholder='{"API_KEY": "your-key-here"}',
                    height=80,
                )
                if st.form_submit_button("➕ Add Server", type="primary"):
                    if mcp_name and mcp_cmd:
                        args_list = [a.strip() for a in mcp_args.split(",") if a.strip()] if mcp_args else []
                        env_dict = {}
                        if mcp_env:
                            try:
                                env_dict = json.loads(mcp_env)
                            except json.JSONDecodeError:
                                st.error("Invalid JSON in environment variables.")
                                env_dict = None
                        if env_dict is not None:
                            mcp_client.add_server(mcp_name, mcp_cmd, args_list, env_dict)
                            st.success(f"MCP Server '{mcp_name}' added!")
                            st.rerun()
                    else:
                        st.error("Server name and command are required.")

        st.markdown("---")

        if not configs:
            st.info(
                "No MCP servers configured. Add one above to extend Alfred's capabilities.\n\n"
                "**Popular MCP servers:**\n"
                "- `npx -y @anthropic/mcp-server-brave-search` — Web search\n"
                "- `npx -y @anthropic/mcp-server-filesystem` — File system access\n"
                "- `npx -y @anthropic/mcp-server-memory` — Persistent memory\n"
                "- `npx -y @anthropic/mcp-server-github` — GitHub integration"
            )
        else:
            for config in configs:
                name = config["name"]
                status = mcp_client.get_server_status(name)
                is_connected = status["connected"]
                tool_count = status["tool_count"]

                with st.container():
                    col_status, col_info, col_actions = st.columns([1, 5, 3])

                    with col_status:
                        if is_connected:
                            st.markdown("### 🟢")
                        else:
                            st.markdown("### 🔴")

                    with col_info:
                        st.markdown(f"**{name}**")
                        st.caption(f"`{config['command']} {' '.join(config.get('args', []))}`")
                        if is_connected:
                            st.caption(f"🔧 {tool_count} tools available")
                        elif status.get("error"):
                            st.caption(f"❌ {status['error']}")

                    with col_actions:
                        c1, c2, c3 = st.columns(3)
                        with c1:
                            enabled = config.get("enabled", True)
                            new_enabled = st.toggle(
                                "Enable",
                                value=enabled,
                                key=f"mcp_toggle_{name}",
                                label_visibility="collapsed"
                            )
                            if new_enabled != enabled:
                                mcp_client.toggle_server(name, new_enabled)
                                if new_enabled:
                                    mcp_client.start_server(config)
                                st.rerun()
                        with c2:
                            if st.button("🔄", key=f"mcp_restart_{name}", help="Restart"):
                                mcp_client.stop_server(name)
                                mcp_client.start_server(config)
                                st.rerun()
                        with c3:
                            if st.button("🗑️", key=f"mcp_del_{name}", help="Remove"):
                                mcp_client.remove_server(name)
                                st.rerun()

                    # Show tools if connected
                    if is_connected and status["tools"]:
                        with st.expander(f"🔧 Tools ({tool_count})", expanded=False):
                            for tool in status["tools"]:
                                st.markdown(f"- **{tool['name']}** — {tool.get('description', 'No description')}")

                    st.markdown("---")

    # ── Plugins Sub-Tab ─────────────────────────────────────
    with sub_plugins:
        st.markdown("### 📦 Plugins")
        st.caption(
            "Plugins bundle skills and MCP servers together into installable packages. "
            "Drop plugin folders into `data/plugins/` with a `plugin.json` manifest."
        )

        plugins = PluginManager.list_plugins()

        if not plugins:
            st.info(
                "No plugins installed.\n\n"
                "**To create a plugin**, create a folder in `data/plugins/` with this structure:\n"
                "```\n"
                "data/plugins/my-plugin/\n"
                "├── plugin.json\n"
                "├── skills/\n"
                "│   └── my_skill.md\n"
                "└── README.md\n"
                "```\n\n"
                "**plugin.json example:**\n"
                "```json\n"
                '{\n'
                '  "name": "My Plugin",\n'
                '  "description": "What this plugin does",\n'
                '  "icon": "🌟",\n'
                '  "version": "1.0",\n'
                '  "enabled": true,\n'
                '  "skills": ["skills/my_skill.md"],\n'
                '  "mcps": []\n'
                '}\n'
                "```"
            )
        else:
            for plugin in plugins:
                with st.container():
                    col_toggle, col_info = st.columns([1, 8])
                    with col_toggle:
                        enabled = plugin.get("enabled", True)
                        new_enabled = st.toggle(
                            "on",
                            value=enabled,
                            key=f"plugin_toggle_{plugin['dir_name']}",
                            label_visibility="collapsed"
                        )
                        if new_enabled != enabled:
                            PluginManager.toggle_plugin(plugin["dir_name"], new_enabled)
                            st.rerun()

                    with col_info:
                        icon = plugin.get("icon", "📦")
                        st.markdown(f"**{icon} {plugin['name']}** v{plugin.get('version', '?')}")
                        st.caption(plugin.get("description", ""))

                        skills = plugin.get("skills", [])
                        mcps = plugin.get("mcps", [])
                        badges = []
                        if skills:
                            badges.append(f"🎯 {len(skills)} skills")
                        if mcps:
                            badges.append(f"🔌 {len(mcps)} MCPs")
                        if badges:
                            st.caption(" · ".join(badges))

                    st.markdown("---")

# ═══════════════════════════════════════════════════════════
#  GIT TOOLS
# ═══════════════════════════════════════════════════════════

class GitTools:
    """Manages Git-based self-evolution for Alfred."""

    @staticmethod
    def get_tools() -> list[dict]:
        return [
            {
                "type": "function",
                "function": {
                    "name": "workspace_git_commit",
                    "description": "Commit all changes in the workspace to the local Git repository. Use this after making self-edits. REQUIRES USER APPROVAL.",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "message": {"type": "string", "description": "The commit message describing exactly what was changed"}
                        },
                        "required": ["message"]
                    }
                }
            },
            {
                "type": "function",
                "function": {
                    "name": "workspace_git_push",
                    "description": "Push committed changes from the workspace to the remote GitHub repository. REQUIRES USER APPROVAL.",
                    "parameters": {
                        "type": "object",
                        "properties": {}
                    }
                }
            }
        ]

    @staticmethod
    def exec_tool(name: str, args: dict) -> str:
        if name == "workspace_git_commit":
            message = args.get("message", "Auto-commit from Alfred")
            try:
                # Ensure safe directory inside Docker
                subprocess.run(["git", "config", "--global", "--add", "safe.directory", "/app"], capture_output=True)
                subprocess.run(["git", "config", "user.name", "Alfred AI"], capture_output=True)
                subprocess.run(["git", "config", "user.email", "alfred@agent.local"], capture_output=True)
                
                # Add all
                add_res = subprocess.run(["git", "add", "."], capture_output=True, text=True, cwd=str(ALFRED_DIR))
                if add_res.returncode != 0:
                    return f"Git add error: {add_res.stderr}"
                
                # Commit
                commit_res = subprocess.run(["git", "commit", "-m", message], capture_output=True, text=True, cwd=str(ALFRED_DIR))
                if commit_res.returncode != 0:
                    if "nothing to commit" in commit_res.stdout:
                        return "Nothing to commit; working tree clean."
                    return f"Git commit error: {commit_res.stderr}\n{commit_res.stdout}"
                return f"✅ Successfully committed changes: '{message}'"
            except Exception as e:
                return f"Error executing git commit: {e}"

        elif name == "workspace_git_push":
            try:
                subprocess.run(["git", "config", "--global", "--add", "safe.directory", "/app"], capture_output=True)
                
                env = os.environ.copy()
                env["GIT_SSH_COMMAND"] = "ssh -i /app/data/alfred_deploy_key -o IdentitiesOnly=yes -o StrictHostKeyChecking=accept-new"
                
                push_res = subprocess.run(["git", "push", "origin", "main"], capture_output=True, text=True, cwd=str(ALFRED_DIR), env=env)
                if push_res.returncode != 0:
                    return f"Git push error: {push_res.stderr}\n{push_res.stdout}"
                return "✅ Successfully pushed changes to remote repository."
            except Exception as e:
                return f"Error executing git push: {e}"
        
        return f"Unknown git tool: {name}"
