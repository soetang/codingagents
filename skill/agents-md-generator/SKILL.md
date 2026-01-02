---
name: agents-md-generator
description: Creates agents.md files for repositories containing AI agent workflows, development instructions, and best practices. Use when the user asks to create an agents.md file, set up agent documentation for a repository, or needs repository-specific instructions for AI agents. Supports Python repos (with uv, ruff, mypy, pytest) and can be extended for other tech stacks.
---

# Agents.md Generator

## Overview

This skill generates `agents.md` files that provide AI agents with comprehensive, repository-specific instructions for development workflows, code quality standards, testing procedures, and best practices.

## Workflow

### 1. Analyze Repository Structure

First, examine the repository to determine the tech stack and tooling:

- Look for configuration files (e.g., `pyproject.toml`, `package.json`, `Cargo.toml`)
- Check for dependency management tools (e.g., `uv`, `npm`, `cargo`)
- Identify linting/formatting tools (e.g., `ruff`, `eslint`, `prettier`)
- Find test frameworks (e.g., `pytest`, `jest`, `cargo test`)
- Note type checking tools (e.g., `mypy`, `typescript`)

### 2. Select Template

Based on the repository type, select the appropriate template:

**Python repositories**: Use `references/python_template.md` as the base template. This covers:
- Dependency management with `uv`
- Code quality with `ruff` (linting and formatting)
- Type checking with `mypy`
- Testing with `pytest`
- Python-specific style guidelines

**Other repository types**: Adapt the Python template structure to the specific tech stack, maintaining the same organizational pattern:
- Dependency management section
- Code quality and formatting section
- Testing section
- Style guidelines section
- Development workflow section

### 3. Customize Content

Adapt the template to the specific repository:

**Replace tool-specific commands**: Update commands to match the repository's actual tools and configuration.

**Preserve repository conventions**: Examine existing code to identify:
- Import organization patterns
- Docstring styles already in use
- Naming conventions
- Code organization patterns

**Add repository-specific sections** as needed:
- Build commands if the project requires compilation
- Deployment procedures for services
- Database migration commands
- Environment setup steps
- CI/CD integration notes

**Remove irrelevant sections**: Delete sections that don't apply to the repository (e.g., type checking if not used).

### 4. Validate Against Repository

Before finalizing:

- Verify all commands work in the repository's environment
- Check that configuration file references are accurate (e.g., `pyproject.toml` paths)
- Ensure examples align with actual project structure
- Confirm test commands match the test directory structure

### 5. Place the File

Create `agents.md` in the repository root, ensuring it's:
- At the same level as primary config files (e.g., `pyproject.toml`, `package.json`)
- Named exactly `agents.md` (lowercase)
- Committed to version control for team-wide use

## Content Structure

An `agents.md` file should follow this general structure:

1. **Repository type/language identifier** - Brief header indicating the tech stack
2. **Dependency Management** - Adding, removing, and updating dependencies
3. **Code Quality & Formatting** - Linting, formatting, and code style tools
4. **Type Checking** (if applicable) - Type system usage and validation
5. **Testing** - Running tests, test organization, coverage requirements
6. **Code Style Guidelines** - Language-specific conventions and patterns
7. **Development Workflow** - Pre-commit checks, PR requirements, common tasks
8. **Additional Sections** - Build, deploy, environment setup as needed

## Templates and Examples

### Python Template

For Python repositories, use `references/python_template.md` which includes:
- `uv` for dependency management
- `ruff` for linting and formatting
- `mypy` for type checking
- `pytest` for testing
- Google-style docstrings
- Modern Python type hints

To use: Read `references/python_template.md` and customize based on the repository's actual setup.

### OpenCode Configuration Repository Example

For repositories that are primarily configuration/documentation (like OpenCode config repos), see `references/agents.md` which demonstrates:
- Working with agent definition files
- Minimal dependency management (Node.js only)
- Git workflow and commit conventions
- Repository organization approach
- Pointing to existing documentation rather than duplicating it
- Common tasks without duplicating skill workflows

This example shows how to document a configuration-focused repository while avoiding duplication of information that agents can read directly from other sources (like skill files).

## Best Practices

**Avoid duplication**: Don't document information that agents can read directly from other sources. For example:
- Don't list all current files - agents can use file tools to explore
- Don't duplicate skill workflows - agents can read SKILL.md files
- Don't list current dependencies - point to `package.json` or `pyproject.toml`

**Keep commands current**: Use the actual commands that work in the repository, not hypothetical ones.

**Be concise**: Include only information that's non-obvious or repository-specific. Avoid general programming advice.

**Use examples**: Show concrete examples of commands, import patterns, and docstrings from the actual codebase.

**Organize logically**: Group related commands together (e.g., all testing commands in one section).

**Include common workflows**: Add sections for frequent tasks like "Before Creating a Pull Request" or "Running All Checks".

**Reference, don't duplicate**: Point to where information is defined rather than copying it (e.g., "Ruff settings are in `pyproject.toml` under `[tool.ruff]`").
