"""
ToolContext — shared dependencies injected into every tool's execute() function.
"""
import os
import json
import subprocess
from pathlib import Path
from dataclasses import dataclass, field
from typing import Any, Optional


@dataclass
class ToolContext:
    """Shared context passed to every tool execute() call."""
    vault_path: Path
    alfred_dir: Path
    milvus_client: Any = None  # pymilvus.MilvusClient or None
    google: Any = None         # google_connector module
    manus: Any = None          # manus_connector module

    # ── Utility methods available to all tools ──

    def get_embedding(self, text: str) -> list:
        """Get text embedding from local Ollama."""
        import requests
        resp = requests.post(
            "http://localhost:11434/api/embeddings",
            json={"model": "nomic-embed-text", "prompt": text}
        )
        return resp.json()["embedding"]

    def run_vault_cmd(self, args: list, stdin_text: str = None) -> tuple:
        """Run an alfred vault CLI command. Returns (ok: bool, output: str)."""
        cmd = ["alfred", "vault"] + args
        env = {**os.environ, "ALFRED_VAULT_PATH": str(self.vault_path)}
        try:
            r = subprocess.run(
                cmd, capture_output=True, text=True, timeout=30,
                cwd=str(self.alfred_dir), env=env,
                stdin=subprocess.PIPE if stdin_text else subprocess.DEVNULL,
                input=stdin_text
            )
            return r.returncode == 0, (r.stdout.strip() or r.stderr.strip())
        except Exception as e:
            return False, str(e)

    def get_active_tasks(self) -> list:
        """Get active tasks from the vault, sorted by priority then due date."""
        task_dir = self.vault_path / "task"
        if not task_dir.exists():
            return []

        import yaml
        priority_order = {"critical": 0, "high": 1, "medium": 2, "low": 3, "": 4}
        tasks = []

        for f in task_dir.glob("*.md"):
            try:
                raw = f.read_text("utf-8", errors="replace")
                if not raw.startswith("---"):
                    continue
                end = raw.index("---", 3)
                fm = yaml.safe_load(raw[3:end])
                if not fm:
                    continue
                status = str(fm.get("status", "")).lower()
                if status in ("done", "cancelled", "archived"):
                    continue
                tasks.append({
                    "name": f.stem,
                    "path": f"task/{f.name}",
                    "priority": str(fm.get("priority", "")).lower(),
                    "deadline": str(fm.get("due", fm.get("deadline", ""))),
                    "status": status,
                })
            except Exception:
                continue

        tasks.sort(key=lambda t: (
            priority_order.get(t["priority"], 4),
            t["deadline"] or "9999"
        ))
        return tasks
