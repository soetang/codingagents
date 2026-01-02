# Python Repo Instructions

### Adding Dependencies

- Add a runtime dependency: `uv add <package-name>`
- Add a development dependency: `uv add --dev <package-name>`
- Lock dependencies: `uv lock`
- Sync after manual edits to pyproject.toml: `uv sync`

## Code Quality & Formatting

### Ruff - Linting and Formatting

This project uses **ruff** for both linting and code formatting.

- Format code: `uv run ruff format .`
- Check formatting without changes: `uv run ruff format --check .`
- Run linter: `uv run ruff check .`
- Run linter with auto-fix: `uv run ruff check --fix .`
- Run all checks: `uv run ruff check . && uv run ruff format --check .`

### Type Checking

- Run mypy for type checking: `uv run mypy src/`
- Run mypy on specific file: `uv run mypy path/to/file.py`

### Running All Checks

Before committing, run all quality checks:
```bash
uv run ruff format . && \
uv run ruff check --fix . && \
uv run mypy src/
```

## Testing

### Running Tests

- Run all tests: `uv run pytest`
- Run specific test file: `uv run pytest tests/test_module.py`
- Run tests matching pattern: `uv run pytest -k "test_pattern"`
- Run with coverage: `uv run pytest --cov=src --cov-report=term-missing`
- Run with verbose output: `uv run pytest -v`
- Run with print output: `uv run pytest -s`

### Test Organization

- All tests go in the `tests/` directory
- Test files must start with `test_` and end with `.py`
- Test functions must start with `test_`
- Use descriptive test names that explain what is being tested
- Add tests for new functionality and bug fixes

## Code Style Guidelines

### General Python Style

- Follow PEP 8 conventions (enforced by ruff)
- Use type hints for function signatures and class attributes
- Prefer explicit over implicit

### Import Organization

Ruff automatically organizes imports. The expected order is:
1. Standard library imports
2. Third-party imports
3. Local application imports

Blank lines separate each group.

### Docstrings

Use **Google-style docstrings** for all public modules, classes, methods, and functions.

Example function docstring:
```python
def process_data(items: list[str], timeout: int = 30) -> dict[str, Any]:
    """Process a list of items and return results.

    Args:
        items: List of items to process.
        timeout: Maximum time in seconds. Defaults to 30.

    Returns:
        Dictionary containing processed results.

    Raises:
        ValueError: If items list is empty.
    """
```

Example class docstring:
```python
class DataProcessor:
    """Process and transform data from various sources.

    Attributes:
        config: Configuration dictionary for the processor.
        cache_enabled: Whether caching is enabled.
    """
    
    def __init__(self, config: dict[str, Any]) -> None:
        """Initialize the DataProcessor.

        Args:
            config: Configuration dictionary with processing options.
        """
```

### Type Hints

- All public functions and methods should have type hints
- Use modern Python type syntax (e.g., `list[int]` instead of `List[int]`)
- Use `typing` module for complex types (e.g., `TypeVar`, `Protocol`, `Generic`)
- Use `Optional[T]` or `T | None` for nullable types

### Naming Conventions

- Classes: `PascalCase`
- Functions/methods: `snake_case`
- Constants: `UPPER_SNAKE_CASE`
- Private methods/attributes: prefix with single underscore `_private_method`

## Development Workflow

### Before Creating a Pull Request

1. Ensure all tests pass: `uv run pytest`
2. Format code: `uv run ruff format .`
3. Fix linting issues: `uv run ruff check --fix .`
4. Verify type hints: `uv run mypy src/`
5. Ensure test coverage is adequate: `uv run pytest --cov=src --cov-report=term-missing`
6. Update documentation if needed

### Commit Message Guidelines

- Use clear, descriptive commit messages
- Start with a verb in present tense (e.g., "Add feature", "Fix bug", "Update docs")
- Keep first line under 72 characters
- Add detailed description after blank line if needed

### Creating New Modules

When adding new modules:
1. Create module in appropriate location under `src/`
2. Add comprehensive docstrings
3. Add type hints to all functions
4. Create corresponding test file in `tests/`
5. Update `__init__.py` if the module should be part of public API
6. Add module to documentation if needed

### Import Errors

If you encounter import errors:
1. Ensure virtual environment is activated
2. Run `uv sync` to ensure all dependencies are installed
3. Verify package is installed in editable mode: `uv pip install -e .`

### Configuration
Ruff settings are in `pyproject.toml` under `[tool.ruff]`. 
Mypy settings are in `pyproject.toml` under `[tool.mypy]`. 

