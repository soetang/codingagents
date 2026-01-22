# Python Best Practices (Practical)

Follow repo conventions and tooling first. Use this file when the repo is silent and you need a reasonable default.

## Core Principles

- Prefer readability over cleverness.
  - Ref: https://peps.python.org/pep-0020/

## Data Modeling

- Prefer `@dataclass` for simple, immutable-ish records.
  - Keep fields explicit; avoid dynamic attribute injection.
  - Ref: https://docs.python.org/3/library/dataclasses.html

## Files and Paths

- Prefer `pathlib.Path` over raw strings for filesystem paths (especially when joining, iterating, or checking existence).
  - Ref: https://docs.python.org/3/library/pathlib.html

## Resource Management

- Prefer context managers (`with`) for resources (files, locks, network connections) so cleanup happens reliably.
  - Ref: https://docs.python.org/3/reference/compound_stmts.html#the-with-statement

## Exceptions

- Raise specific exceptions; avoid broad `except Exception` unless you re-raise or add context.
- When catching and re-raising, use `raise ... from err` to preserve cause.
  - Ref: https://docs.python.org/3/tutorial/errors.html#exception-chaining

## Logging

- Prefer `logging` over `print` for non-trivial programs and libraries.
- Use structured, parameterized logging (`logger.info("x=%s", x)`) to avoid unnecessary string formatting.
  - Ref: https://docs.python.org/3/library/logging.html

## Functions and APIs

- Keep functions small and single-purpose.
- Prefer explicit keyword arguments for boolean flags if call sites are unclear.
- Avoid mutable default arguments; use `None` and initialize inside.
  - Ref: https://docs.python.org/3/tutorial/controlflow.html#default-argument-values

## Imports

- Avoid import cycles by extracting shared types/utilities or using local imports only when necessary.

## Testing

- Prefer unit tests for logic-heavy code; add integration tests for I/O boundaries.
- Keep test names descriptive (intent-based).
