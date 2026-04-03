#!/usr/bin/env python3
"""
vault_omi_sync.py — Bidirectional sync between Alfred vault and Omi.

Runs both directions:
  1. Alfred vault → Omi (memories + knowledge graph)
  2. Omi → Alfred vault (transcription sessions → inbox)

This is the script that launchd calls daily.

Usage:
    python3 scripts/vault_omi_sync.py             # full bidirectional sync
    python3 scripts/vault_omi_sync.py --dry-run    # preview only (both directions)
    python3 scripts/vault_omi_sync.py --vault-only # only vault → Omi
    python3 scripts/vault_omi_sync.py --omi-only   # only Omi → vault
"""
from __future__ import annotations

import subprocess
import sys
import os
from datetime import datetime
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
LOG_DIR = SCRIPT_DIR / "logs"
LOG_DIR.mkdir(exist_ok=True)


def run_script(name: str, script_path: Path, extra_args: list[str] | None = None) -> int:
    """Run a sync script and capture output."""
    args = [sys.executable, str(script_path)]
    if extra_args:
        args.extend(extra_args)

    print(f"\n{'='*60}")
    print(f"  Running: {name}")
    print(f"{'='*60}\n")

    result = subprocess.run(
        args,
        cwd=str(SCRIPT_DIR.parent),
        capture_output=False,
        text=True,
    )
    return result.returncode


def main() -> None:
    dry_run = "--dry-run" in sys.argv
    vault_only = "--vault-only" in sys.argv
    omi_only = "--omi-only" in sys.argv

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Vault ↔ Omi Bidirectional Sync — {timestamp}")
    if dry_run:
        print("MODE: Dry run (no changes)")

    extra = ["--dry-run"] if dry_run else []
    exit_code = 0

    # Direction 1: Alfred vault → Omi
    if not omi_only:
        rc = run_script(
            "Alfred → Omi (vault records → memories + KG)",
            SCRIPT_DIR / "alfred_to_omi.py",
            extra,
        )
        if rc != 0:
            print(f"\nWARNING: alfred_to_omi.py exited with code {rc}")
            exit_code = 1

    # Direction 2: Omi → Alfred vault
    if not vault_only:
        rc = run_script(
            "Omi → Alfred (transcription sessions → inbox)",
            SCRIPT_DIR / "omi_to_alfred.py",
            extra if dry_run else [],  # omi_to_alfred doesn't support --dry-run yet
        )
        if rc != 0:
            print(f"\nWARNING: omi_to_alfred.py exited with code {rc}")
            exit_code = 1

    print(f"\n{'='*60}")
    print(f"  Sync complete — {datetime.now().strftime('%H:%M:%S')}")
    print(f"{'='*60}")

    sys.exit(exit_code)


if __name__ == "__main__":
    main()
