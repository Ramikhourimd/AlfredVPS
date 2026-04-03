"""
ToolRegistry — discovers, validates, and manages tool plugins from the tools/ directory.

Each tool is a standalone .py file in tools/ that exports:
  TOOL_DEF  (dict)  — OpenAI function-calling schema
  TOOL_TYPE (str)   — "read" or "write"
  execute(args, ctx) -> str  — handler
  describe(args) -> str      — (write tools only) human-readable approval text
"""
import ast
import sys
import importlib
import importlib.util
import traceback
from pathlib import Path
from typing import Dict, List, Optional, Callable


# Safety: blocked imports/calls that self-created tools cannot use
BLOCKED_IMPORTS = {
    "os", "shutil", "subprocess", "socket", "http", "urllib",
    "ctypes", "multiprocessing", "signal", "sys",
}
BLOCKED_CALLS = {
    "eval", "exec", "__import__", "compile", "globals", "locals",
    "getattr", "setattr", "delattr", "open",
}
# Imports that are always safe for self-created tools
SAFE_IMPORTS = {
    "json", "re", "datetime", "math", "statistics", "collections",
    "itertools", "functools", "pathlib", "typing", "textwrap",
    "hashlib", "base64", "csv", "io", "copy", "dataclasses",
    "ddgs", "duckduckgo_search", "requests", "yaml",
}


class ToolRegistry:
    """Discovers, validates, and manages tool plugin files."""

    def __init__(self, tools_dir: Path):
        self.tools_dir = tools_dir
        self.tools: Dict[str, dict] = {}   # name → {def, type, execute, describe, module, file}
        self.errors: Dict[str, str] = {}   # name → error message
        self._loaded = False

    def discover(self):
        """Scan tools_dir for .py tool files, validate, and import each."""
        self.tools.clear()
        self.errors.clear()

        if not self.tools_dir.exists():
            self.tools_dir.mkdir(parents=True, exist_ok=True)
            return

        for py_file in sorted(self.tools_dir.glob("*.py")):
            if py_file.name.startswith("_"):
                continue  # Skip __init__.py, __pycache__, etc.
            self._load_tool(py_file)

        self._loaded = True

    def _load_tool(self, py_file: Path):
        """Load a single tool file with AST validation."""
        tool_name = py_file.stem
        try:
            # Stage 1: AST validation — check syntax without executing
            source = py_file.read_text("utf-8")
            try:
                ast.parse(source)
            except SyntaxError as e:
                self.errors[tool_name] = f"Syntax error: {e}"
                return

            # Stage 2: Import the module
            spec = importlib.util.spec_from_file_location(
                f"tools.{tool_name}", str(py_file)
            )
            module = importlib.util.module_from_spec(spec)

            # Temporarily add tools dir to sys.path for relative imports
            tools_parent = str(self.tools_dir.parent)
            if tools_parent not in sys.path:
                sys.path.insert(0, tools_parent)

            try:
                spec.loader.exec_module(module)
            except Exception as e:
                self.errors[tool_name] = f"Import error: {e}"
                return

            # Stage 3: Validate required exports
            if not hasattr(module, "TOOL_DEF"):
                self.errors[tool_name] = "Missing TOOL_DEF"
                return
            if not hasattr(module, "TOOL_TYPE"):
                self.errors[tool_name] = "Missing TOOL_TYPE"
                return
            if not hasattr(module, "execute"):
                self.errors[tool_name] = "Missing execute() function"
                return

            tool_def = module.TOOL_DEF
            tool_type = module.TOOL_TYPE
            execute_fn = module.execute
            describe_fn = getattr(module, "describe", None)

            # Validate TOOL_TYPE
            if tool_type not in ("read", "write"):
                self.errors[tool_name] = f"Invalid TOOL_TYPE: {tool_type}"
                return

            # Extract the canonical name from TOOL_DEF
            canonical_name = tool_def.get("function", {}).get("name", tool_name)

            self.tools[canonical_name] = {
                "def": tool_def,
                "type": tool_type,
                "execute": execute_fn,
                "describe": describe_fn,
                "module": module,
                "file": py_file,
            }

        except Exception as e:
            self.errors[tool_name] = f"Load error: {traceback.format_exc()}"

    def get_definitions(self) -> List[dict]:
        """Return OpenAI function-calling schema list for all loaded tools."""
        return [t["def"] for t in self.tools.values()]

    def get_read_tool_names(self) -> set:
        """Return set of read tool names."""
        return {name for name, t in self.tools.items() if t["type"] == "read"}

    def get_write_tool_names(self) -> set:
        """Return set of write tool names."""
        return {name for name, t in self.tools.items() if t["type"] == "write"}

    def execute(self, name: str, args: dict, ctx) -> str:
        """Execute a tool by name. Returns result string."""
        if name not in self.tools:
            return f"Unknown tool: {name}"
        try:
            result = self.tools[name]["execute"](args, ctx)
            if not isinstance(result, str):
                result = str(result)
            # Truncate oversized results to prevent context overflow
            if len(result) > 8000:
                result = result[:8000] + "\n\n...[truncated — result too large]"
            return result
        except Exception as e:
            return f"⚠️ Tool '{name}' error: {e}"

    def describe(self, name: str, args: dict) -> str:
        """Get human-readable description for write tool approval UI."""
        if name not in self.tools:
            return f"Unknown action: {name}"
        describe_fn = self.tools[name].get("describe")
        if describe_fn:
            try:
                return describe_fn(args)
            except Exception:
                pass
        # Fallback: auto-generate from tool name and args
        return f"**{name}** with args: {str(args)[:200]}"

    def is_write_tool(self, name: str) -> bool:
        """Check if a tool requires user approval."""
        return self.tools.get(name, {}).get("type") == "write"

    def is_read_tool(self, name: str) -> bool:
        """Check if a tool executes immediately."""
        return self.tools.get(name, {}).get("type") == "read"

    def reload(self):
        """Re-scan and reload all tools (hot-reload)."""
        # Remember which tools were loaded before
        old_tools = set(self.tools.keys())

        # Clear module cache for tool modules
        for name, t in self.tools.items():
            mod_name = f"tools.{t['file'].stem}"
            if mod_name in sys.modules:
                del sys.modules[mod_name]

        # Re-discover
        self.discover()

        new_tools = set(self.tools.keys())
        added = new_tools - old_tools
        removed = old_tools - new_tools

        report = f"Reloaded {len(self.tools)} tools."
        if added:
            report += f"\n✅ New: {', '.join(sorted(added))}"
        if removed:
            report += f"\n❌ Removed: {', '.join(sorted(removed))}"
        if self.errors:
            report += f"\n⚠️ Errors: {', '.join(f'{k}: {v}' for k, v in self.errors.items())}"
        return report

    def validate_self_created_tool(self, source_code: str) -> tuple:
        """
        Validate source code for a self-created tool.
        Returns (is_valid: bool, error_message: str or None)

        Security checks:
        1. AST syntax validation
        2. Blocked import detection
        3. Blocked function call detection
        4. Required exports check
        """
        # 1. Syntax check
        try:
            tree = ast.parse(source_code)
        except SyntaxError as e:
            return False, f"Syntax error on line {e.lineno}: {e.msg}"

        # 2. Check imports
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    base_module = alias.name.split(".")[0]
                    if base_module in BLOCKED_IMPORTS and base_module not in SAFE_IMPORTS:
                        return False, f"Blocked import: '{alias.name}' — security restriction"
            elif isinstance(node, ast.ImportFrom):
                if node.module:
                    base_module = node.module.split(".")[0]
                    if base_module in BLOCKED_IMPORTS and base_module not in SAFE_IMPORTS:
                        return False, f"Blocked import: 'from {node.module}' — security restriction"

        # 3. Check for blocked function calls
        for node in ast.walk(tree):
            if isinstance(node, ast.Call):
                if isinstance(node.func, ast.Name):
                    if node.func.id in BLOCKED_CALLS:
                        return False, f"Blocked call: '{node.func.id}()' — security restriction"
                elif isinstance(node.func, ast.Attribute):
                    full = f"{_get_call_name(node.func)}"
                    if full in BLOCKED_CALLS:
                        return False, f"Blocked call: '{full}()' — security restriction"

        # 4. Check required exports exist
        has_tool_def = False
        has_tool_type = False
        has_execute = False

        for node in ast.iter_child_nodes(tree):
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name):
                        if target.id == "TOOL_DEF":
                            has_tool_def = True
                        elif target.id == "TOOL_TYPE":
                            has_tool_type = True
            elif isinstance(node, ast.FunctionDef):
                if node.name == "execute":
                    has_execute = True

        errors = []
        if not has_tool_def:
            errors.append("Missing TOOL_DEF assignment")
        if not has_tool_type:
            errors.append("Missing TOOL_TYPE assignment")
        if not has_execute:
            errors.append("Missing execute() function")

        if errors:
            return False, "; ".join(errors)

        return True, None


def _get_call_name(node) -> str:
    """Recursively get the dotted name of an AST call node."""
    if isinstance(node, ast.Attribute):
        parent = _get_call_name(node.value)
        return f"{parent}.{node.attr}" if parent else node.attr
    elif isinstance(node, ast.Name):
        return node.id
    return ""
