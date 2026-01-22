# Tool-Aware Workflow

Always prefer repo tooling/config over generic defaults.

## Detect Configuration

- `pyproject.toml`: common home for ruff/black/isort/mypy/pytest config
- `ruff.toml`: ruff config
- `setup.cfg` / `tox.ini`: older but still common

## Format / Lint / Type Check

Use whatever the repo uses. Common patterns:

- Ruff:
  - Format: `ruff format .`
  - Lint: `ruff check .`
- Black:
  - Format: `black .`
- isort:
  - Imports: `isort .`
- mypy:
  - Types: `mypy src/`

If a repo uses `uv`, commands often run as:

- `uv run ruff format .`
- `uv run ruff check .`
- `uv run mypy src/`

## Import Organization

- Prefer the repo's configured import sorter (ruff or isort).
- If no tool is present, follow PEP 8 import grouping.
