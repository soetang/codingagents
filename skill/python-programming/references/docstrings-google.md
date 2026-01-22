# Google-Style Docstrings

Use Google-style docstrings for public modules, classes, and functions.

Keep the summary line short, imperative, and on the first line.

## Function Example

```python
def parse_user_id(value: str) -> int:
    """Parse a user id from a string.

    Args:
        value: Raw user id input.

    Returns:
        Parsed user id.

    Raises:
        ValueError: If the value is not a valid integer user id.
    """

    user_id = int(value)
    if user_id <= 0:
        raise ValueError("user id must be positive")
    return user_id
```

## Class Example

```python
class UserCache:
    """Cache user records in memory.

    Attributes:
        max_size: Maximum number of cached users.
    """

    def __init__(self, max_size: int) -> None:
        """Initialize the cache.

        Args:
            max_size: Maximum number of cached users.
        """

        self.max_size = max_size
        self._data: dict[int, dict[str, object]] = {}
```

## Module Docstring Example

```python
"""User identity utilities.

This module contains helpers for parsing and validating user identifiers.
"""
```

## Practical Rules

- Add `Args:` if the function takes parameters.
- Add `Returns:` if the function returns a value other than `None`.
- Add `Raises:` for user-visible or test-relevant exceptions.
- Prefer documenting behavior/constraints over restating types.
- Do not add docstrings for private helpers unless the behavior is non-obvious.
