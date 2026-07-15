# Validate theme

Validate one theme without changing repository files.

1. Read `AGENTS.md`, the target app README, and the target theme README; for Chrome, also read the target `INSTALL.md`
2. Determine the target `<app>/<theme-id>` from the user's request; ask only if it cannot be inferred safely
3. Inspect `git status --short --branch` and the relevant diff
4. Run the app-specific validator
5. For Chrome, confirm that the README uses the required standalone Markdown background preview and Markdown installation link
6. For Chrome, run `python3 tools/chrome/validate_theme.py chrome/<theme-id>`
7. Run `python3 tools/agents/validate_setup.py` and `git diff --check`
8. If a distribution archive already exists, inspect its file list without rebuilding it
9. Return `PASS` or `FAIL`, the commands run, exact errors, and remaining human release gates

Do not edit, package, commit, push, tag, publish, or upload anything during this workflow.
