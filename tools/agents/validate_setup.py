#!/usr/bin/env python3
"""Validate cross-agent repository instructions and skills."""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
CANONICAL_SKILL = Path(".agents/skills/theme-workflow/SKILL.md")
CLAUDE_SKILL = Path(".claude/skills/theme-workflow/SKILL.md")

REQUIRED_FILES = (
    Path("AGENTS.md"),
    Path("CLAUDE.md"),
    Path("GEMINI.md"),
    Path(".agents/rules/repository.md"),
    CANONICAL_SKILL,
    CLAUDE_SKILL,
    Path(".agents/workflows/validate-theme.md"),
    Path(".agents/agents/theme-reviewer/agent.md"),
    Path(".claude/agents/theme-reviewer.md"),
    Path(".claude/settings.json"),
    Path("docs/agents/README.md"),
    Path("templates/chrome-theme/README.md"),
    Path("templates/chrome-theme/INSTALL.md"),
)

ADAPTER_IMPORTS = {
    Path("CLAUDE.md"): "@AGENTS.md",
    Path(".agents/rules/repository.md"): "@../../AGENTS.md",
}

FRONTMATTER_FILES = {
    CANONICAL_SKILL: {"name", "description"},
    CLAUDE_SKILL: {"name", "description"},
    Path(".agents/agents/theme-reviewer/agent.md"): {"name", "description"},
    Path(".claude/agents/theme-reviewer.md"): {"name", "description"},
}


def read(relative_path: Path) -> str:
    return (ROOT / relative_path).read_text(encoding="utf-8")


def frontmatter(content: str) -> dict[str, str]:
    if not content.startswith("---\n"):
        return {}

    closing = content.find("\n---\n", 4)
    if closing == -1:
        return {}

    values: dict[str, str] = {}
    for line in content[4:closing].splitlines():
        match = re.match(r"^([A-Za-z][A-Za-z0-9_-]*):\s*(.*?)\s*$", line)
        if match:
            values[match.group(1)] = match.group(2)
    return values


def markdown_body(content: str) -> str:
    if not content.startswith("---\n"):
        return content.strip()
    closing = content.find("\n---\n", 4)
    if closing == -1:
        return ""
    return content[closing + 5 :].strip()


def command_output(command: list[str]) -> tuple[int, str]:
    result = subprocess.run(
        command,
        cwd=ROOT,
        check=False,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        timeout=30,
    )
    return result.returncode, result.stdout.strip()


def smoke_check(errors: list[str]) -> None:
    for executable in ("codex", "claude", "gemini"):
        path = shutil.which(executable)
        if path is None:
            print(f"SKIP: {executable} CLI is not installed")
            continue
        returncode, output = command_output([executable, "--version"])
        if returncode != 0:
            errors.append(f"{executable} --version failed: {output}")
        else:
            print(f"OK CLI: {executable} {output}")

    if shutil.which("gemini") is not None:
        returncode, output = command_output(["gemini", "skills", "list"])
        expected_location = str((ROOT / CANONICAL_SKILL).resolve())
        if returncode != 0:
            errors.append(f"gemini skills list failed: {output}")
        elif "theme-workflow [Enabled]" not in output or expected_location not in output:
            errors.append(
                "Gemini CLI did not discover the repository theme-workflow skill"
            )
        else:
            print("OK discovery: Gemini CLI found theme-workflow")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--smoke",
        action="store_true",
        help="also inspect installed CLIs and Gemini skill discovery",
    )
    args = parser.parse_args()
    errors: list[str] = []

    for relative_path in REQUIRED_FILES:
        if not (ROOT / relative_path).is_file():
            errors.append(f"missing required file: {relative_path}")

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    for relative_path, expected_import in ADAPTER_IMPORTS.items():
        first_content_line = next(
            (line.strip() for line in read(relative_path).splitlines() if line.strip()),
            "",
        )
        if first_content_line != expected_import:
            errors.append(
                f"{relative_path}: first content line must be {expected_import!r}"
            )
            continue
        import_target = (ROOT / relative_path).parent / expected_import[1:]
        if import_target.resolve() != (ROOT / "AGENTS.md").resolve():
            errors.append(
                f"{relative_path}: import does not resolve to the root AGENTS.md"
            )

    gemini_adapter = read(Path("GEMINI.md"))
    routes_to_contract = "AGENTS.md" in gemini_adapter
    routes_to_workspace_rule = ".agents/rules/repository.md" in gemini_adapter
    if not routes_to_contract or not routes_to_workspace_rule:
        errors.append(
            "GEMINI.md must route to AGENTS.md and .agents/rules/repository.md"
        )
    if "@AGENTS.md" in gemini_adapter:
        errors.append("GEMINI.md must not re-import AGENTS.md")

    canonical_skill = (ROOT / CANONICAL_SKILL).read_bytes()
    claude_skill = (ROOT / CLAUDE_SKILL).read_bytes()
    if canonical_skill != claude_skill:
        errors.append(
            f"{CLAUDE_SKILL} must be byte-identical to {CANONICAL_SKILL}"
        )

    for relative_path, required_keys in FRONTMATTER_FILES.items():
        values = frontmatter(read(relative_path))
        missing_keys = sorted(key for key in required_keys if not values.get(key))
        if missing_keys:
            errors.append(
                f"{relative_path}: missing frontmatter keys: {', '.join(missing_keys)}"
            )

    claude_reviewer = Path(".claude/agents/theme-reviewer.md")
    antigravity_reviewer = Path(".agents/agents/theme-reviewer/agent.md")
    if markdown_body(read(claude_reviewer)) != markdown_body(
        read(antigravity_reviewer)
    ):
        errors.append("Claude and Antigravity reviewer bodies must stay synchronized")
    if frontmatter(read(claude_reviewer)).get("permissionMode") != "plan":
        errors.append(
            ".claude/agents/theme-reviewer.md: permissionMode must be 'plan'"
        )

    try:
        claude_settings = json.loads(read(Path(".claude/settings.json")))
    except json.JSONDecodeError as error:
        errors.append(f".claude/settings.json: invalid JSON: {error}")
    else:
        permissions = claude_settings.get("permissions", {})
        ask_rules = permissions.get("ask", [])
        deny_rules = permissions.get("deny", [])
        for rule in ("Bash(git commit *)", "Bash(git push *)", "Bash(git tag *)"):
            if rule not in ask_rules:
                errors.append(f".claude/settings.json: missing ask rule {rule!r}")
        for rule in ("Read(./.env)", "Read(./.env.*)", "Read(./**/*.pem)"):
            if rule not in deny_rules:
                errors.append(f".claude/settings.json: missing deny rule {rule!r}")
        if permissions.get("disableBypassPermissionsMode") != "disable":
            errors.append(
                ".claude/settings.json: permissions.disableBypassPermissionsMode "
                "must be 'disable'"
            )

    gitignore_lines = {
        line.strip()
        for line in read(Path(".gitignore")).splitlines()
        if line.strip() and not line.lstrip().startswith("#")
    }
    required_ignores = {
        ".env",
        ".env.*",
        ".codex/*",
        ".gemini/",
        "CLAUDE.local.md",
        ".claude/settings.local.json",
        ".claude/agent-memory-local/",
        "dist/",
        "*.pem",
    }
    for pattern in sorted(required_ignores - gitignore_lines):
        errors.append(f".gitignore: missing protected pattern {pattern!r}")

    if args.smoke:
        try:
            smoke_check(errors)
        except (OSError, subprocess.SubprocessError) as error:
            errors.append(f"CLI smoke check failed: {error}")

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    print("OK: cross-agent setup")
    print("  canonical instructions: AGENTS.md")
    print(f"  synchronized skill: {CANONICAL_SKILL} == {CLAUDE_SKILL}")
    print("  adapters: Codex, Claude Code, Google Antigravity")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
