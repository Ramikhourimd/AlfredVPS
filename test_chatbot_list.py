import subprocess
import os
from pathlib import Path

VAULT_PATH = Path("/Users/ramikhouri/Desktop/Taliaz")
ALFRED_DIR = Path("/Users/ramikhouri/Desktop/Alfred")

def run_vault_cmd(args, stdin_text=None):
    cmd = ["alfred", "vault"] + args
    env = {**os.environ, "ALFRED_VAULT_PATH": str(VAULT_PATH)}
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=30, cwd=str(ALFRED_DIR),
                           env=env,
                           stdin=subprocess.PIPE if stdin_text else None, input=stdin_text)
        return r.returncode == 0, (r.stdout.strip() or r.stderr.strip())
    except Exception as e:
        return False, str(e)

ok, out = run_vault_cmd(["list", "person"])
if ok:
    print(f"Output length: {len(out)}")
else:
    print(f"Error output: {out}")
