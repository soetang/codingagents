# Project Structure Defaults

Always follow the repo structure first. Use these defaults when starting new Python code in a repo that is not opinionated.

## Common Layout

- Prefer a `src/` layout for packages when creating a new project structure:

```
.
├── pyproject.toml
├── src/
│   └── your_package/
│       ├── __init__.py
│       └── ...
└── tests/
    └── test_...
```

Ref: https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/

## Module Boundaries

- Keep I/O at the edges (files, network, subprocess) and keep core logic testable.
- Avoid giant "utils" modules; name modules by responsibility.
