# Errors and Logging

Prefer consistency with the repo. Use this file when you need defaults.

## Error Handling

- Raise the most specific exception that matches the error.
- Keep exception messages actionable (what failed + key identifier).
- Avoid swallowing exceptions; log and re-raise when the caller cannot proceed.
- Use exception chaining to preserve root cause:

```python
try:
    return parse_payload(raw)
except ValueError as err:
    raise PayloadError("invalid payload") from err
```

Ref: https://docs.python.org/3/tutorial/errors.html#exception-chaining

## Logging

- Prefer module-level loggers:

```python
import logging

logger = logging.getLogger(__name__)
```

- Prefer parameterized logging:

```python
logger.info("loaded user_id=%s", user_id)
```

- Do not log secrets.

Ref: https://docs.python.org/3/library/logging.html
