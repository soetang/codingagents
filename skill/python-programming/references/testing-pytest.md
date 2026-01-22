# Testing (pytest)

Follow the repo's test framework first. Use this when the repo uses pytest or when you need a default.

## Basics

- Put tests in `tests/`.
- Name files `test_*.py`.
- Name tests `test_*`.

Ref: https://docs.pytest.org/en/stable/

## Arrange / Act / Assert

Keep tests readable by splitting setup, execution, and assertions.

## Prefer Fixtures Over Setup Helpers

- Use fixtures for reusable setup/teardown.
- Prefer small fixtures with clear scope (`function` by default).

Ref: https://docs.pytest.org/en/stable/explanation/fixtures.html

## Parametrization

Use `@pytest.mark.parametrize` for behavior matrices.

Ref: https://docs.pytest.org/en/stable/how-to/parametrize.html

## Exception Testing

Use `pytest.raises` and assert on messages only when messages are part of the contract.

Ref: https://docs.pytest.org/en/stable/how-to/assert.html#assertions-about-expected-exceptions

## Mocking

- Prefer injecting dependencies over heavy mocking.
- When mocking, prefer `unittest.mock` and patch at the import location used by the code under test.

Ref: https://docs.python.org/3/library/unittest.mock.html
