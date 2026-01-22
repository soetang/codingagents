---
name: python-programming
description: Python coding standards and workflow guidance with Google-style docstrings. Use when writing, refactoring, or reviewing Python code and you need consistent style decisions (PEP 8 defaults, typing guidance, and tool-aware formatting/linting).
---

# Python Programming

Use this skill as a lightweight, tool-aware style guide for Python changes.

## Workflow

1. Read repo configuration first
   - Look for `pyproject.toml`, `ruff.toml`, `setup.cfg`, `tox.ini`, and existing code style in nearby files.
   - Treat repo tools/config as the source of truth (formatter, linter, type checker).

2. Apply style decisions in this order
   - Match conventions in the touched files.
   - Follow configured tooling.
   - If neither is explicit, default to PEP 8.

3. Write Google-style docstrings
   - Use Google format for public modules/classes/functions.
   - Read `references/docstrings-google.md` for the exact format and examples.

4. Use typing consistently
   - Match the repo's typing posture.
   - If type hints are already present, keep them accurate and reasonably complete.
   - Read `references/typing.md` for practical defaults and tradeoffs.

5. Cite sources for non-obvious style rules
   - Prefer stable citations by section anchor (PEP HTML line numbers are not stable).
   - Example: `https://peps.python.org/pep-0008/#indentation`.

## Reference Map

- PEP 8 quick rules: `references/pep-0008.md`
- Best practices (practical): `references/best-practices.md`
- Google docstrings: `references/docstrings-google.md`
- PEP 257 notes: `references/pep-0257.md`
- Typing guidance: `references/typing.md`
- Tool-aware workflow: `references/tooling.md`
- Testing (pytest patterns): `references/testing-pytest.md`
- Errors and logging: `references/errors-logging.md`
- Project structure: `references/project-structure.md`
