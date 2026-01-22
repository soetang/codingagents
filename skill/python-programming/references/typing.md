# Typing Guidance

Follow the repo's typing posture first (mypy/pyright/ruff rules, existing patterns). When you need defaults:

## Defaults

- Use modern syntax when available: `X | None`, `list[str]`, `dict[str, int]`.
- Avoid `Any` unless it is truly unavoidable.
- Prefer explicit return types for public functions.
- Prefer `collections.abc` types for public interfaces when it improves flexibility (`Sequence`, `Mapping`, `Iterable`).
- Prefer `TypedDict` for dict-like records with known keys.
- Prefer `Protocol` for structural interfaces when it reduces coupling.

## Practical Notes

- Keep types aligned with runtime behavior; do not "type" code into lying.
- Do not add types to every internal helper if the repo is untyped; add types where they materially improve clarity/safety.

## References

- Typing specification: https://typing.readthedocs.io/
- PEP 484 (type hints): https://peps.python.org/pep-0484/
- PEP 604 (union types): https://peps.python.org/pep-0604/
- collections.abc: https://docs.python.org/3/library/collections.abc.html
