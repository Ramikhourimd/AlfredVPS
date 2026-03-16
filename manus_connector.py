"""Manus AI Agent connector for Alfred.

Allows Alfred to delegate complex research, analysis, and content generation
tasks to the Manus autonomous AI agent platform.
"""

import os
import time
import json
import requests
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(Path("/Users/ramikhouri/Desktop/Alfred/.env"))

BASE_URL = "https://api.manus.ai"
API_KEY = os.getenv("MANUS_API_KEY", "")

HEADERS = {
    "API_KEY": API_KEY,
    "Content-Type": "application/json",
    "Accept": "application/json",
}


def _request(method: str, path: str, json_data: dict | None = None) -> dict:
    """Make an authenticated request to the Manus API."""
    url = f"{BASE_URL}{path}"
    resp = requests.request(method, url, headers=HEADERS, json=json_data, timeout=30)
    if resp.status_code >= 400:
        raise Exception(f"Manus API {resp.status_code}: {resp.text[:300]}")
    return resp.json()


# ── Tasks ───────────────────────────────────────────────────

def create_task(prompt: str, project_id: str | None = None) -> dict:
    """Create a new Manus task. Returns {task_id, status, prompt}."""
    body: dict = {"prompt": prompt}
    if project_id:
        body["project_id"] = project_id
    return _request("POST", "/v1/tasks", body)


def get_task(task_id: str) -> dict:
    """Get task details/status. Returns {task_id, status, result, ...}."""
    return _request("GET", f"/v1/tasks/{task_id}")


def list_tasks(status: str | None = None, limit: int = 10) -> list[dict]:
    """List tasks, optionally filtered by status."""
    params = f"?limit={limit}"
    if status:
        params += f"&status={status}"
    return _request("GET", f"/v1/tasks{params}")


def wait_for_task(task_id: str, timeout: int = 120, poll_interval: int = 5) -> dict:
    """Poll a task until it completes or times out."""
    start = time.time()
    while time.time() - start < timeout:
        task = get_task(task_id)
        if task.get("status") in ("completed", "failed"):
            return task
        time.sleep(poll_interval)
    return {"task_id": task_id, "status": "timeout", "error": f"Task did not complete within {timeout}s"}


# ── Projects ────────────────────────────────────────────────

def create_project(name: str, instructions: str = "") -> dict:
    """Create a new Manus project."""
    body = {"name": name}
    if instructions:
        body["instructions"] = instructions
    return _request("POST", "/v1/projects", body)


def list_projects() -> list[dict]:
    """List all Manus projects."""
    return _request("GET", "/v1/projects")
