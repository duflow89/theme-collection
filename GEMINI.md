# Antigravity adapter

The canonical repository contract is `AGENTS.md`. Antigravity IDE imports it through `.agents/rules/repository.md`, while Antigravity CLI discovers the root `AGENTS.md` directly. This file intentionally does not import it again, avoiding duplicate context when both entry points are active.

Use the project resources under `.agents/`: the `theme-workflow` skill for implementation, the `validate-theme` workflow for repeatable validation, and the `theme-reviewer` custom agent for review-only release checks.
