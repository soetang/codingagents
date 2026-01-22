# Personal Project using OpenCode CLI

This is a personal project with commands, skills and agents for the OpenCode CLI. 

### Core components

**Agents** are specialized AI workflows stored as markdown files in the `agent/` directory. They define specific behaviors based on the task at hand. Whether agents operate autonomously depends on the tools and permissions available to them.

**Sub-Agents** are agents designed to be invoked by other agents (or by you) to handle focused subtasks. They provide specialized capabilities that primary agents can leverage.

**Skills** are packaged bundles of instructions, scripts, references, and assets stored in the `skill/` directory. Skills extend OpenCode's capabilities by providing domain-specific knowledge, workflows, and tools. Think of them as "onboarding guides" that transform OpenCode into a specialist for particular tasks.

## Core agents

OpenCode ships with built-in `plan` and `build` agents. They are defaults in the CLI and are not derived from HumanLayer.

## HumanLayer-based commands and sub-agents

Commands and sub-agents adapted from: https://github.com/humanlayer/humanlayer/tree/main/.claude

### Commands
- **create-plan**: Guides interactive implementation planning and produces structured plan documents
- **research**: Documents the codebase as-is by orchestrating parallel research agents
- **implement_plan**: Implements approved plans with phased verification and checklist updates

### Sub-Agents
- **codebase-locator**: Locates files and components relevant to tasks
- **codebase-analyzer**: Analyzes implementation details and traces data flow
- **codebase-pattern-finder**: Finds similar implementations and usage examples
- **thoughts-locator**: Discovers relevant documents in the thoughts directory
- **thoughts-analyzer**: Extracts key insights from thought documents

## Additional sub-agents

- **code-simplifier**: Simplifies and refines code for clarity and maintainability (sourced from `.claude` resources)

## Skills

Skills are modular packages that provide specialized knowledge and workflows:

- **skill-creator** (from Anthropic): Complete workflow for creating, validating, and packaging new skills
- **slack-gif-creator** (from Anthropic): Knowledge and utilities for creating animated GIFs optimized for Slack
- **steal-skill**: Steal existing skills, commands, and agents from GitHub repositories
- **agents-md-generator**: Generates `agents.md` files for repositories with development instructions and best practices
- **spec-writer**: Helps write software specifications, requirements, and feature designs

Skills include their own documentation in `SKILL.md` files and may bundle scripts, references, and assets.

## Commands

Custom commands for improved workflows:

- **create-plan**: Create implementation plans via the plan agent
- **research**: Document codebase as-is via the plan agent
- **implement_plan**: Implement plans via the build agent
- **note-improvement**: Capture agent/skill/command improvement suggestions and create GitHub issues

## Getting Started

1. Install OpenCode CLI
2. Copy the agents, skills, and commands to your relevant opencode directories
3. Use OpenCode CLI to run agents and commands

For detailed instructions, see: [https://opencode.ai/](https://opencode.ai/)

## License

This project is dual-licensed:

- **Overall Project**: MIT License - see the [LICENSE](LICENSE) file for details
- **HumanLayer-inspired Agent System**: Apache License 2.0 - see the [LICENSE-APACHE](LICENSE-APACHE) file
- **Skills**: Licensed under MIT unless a specific LICENSE file exists in the skill's folder
