# Personal Project using OpenCode CLI

A simple project using the OpenCode CLI for personal use.

## Overview

This is a personal project that uses the OpenCode CLI to work with codebases. The agents is heavily inspired by the HumanLayer framework but adapted for personal use. However i migth add other approaches in the future.

## Humanlayer agents:

Agents/commands from: https://github.com/humanlayer/humanlayer/tree/main/.claude

The system includes two types of agents:

### Primary Agents
- **research**: Conducts comprehensive research across codebases
- **create-plan**: Creates implementation plans based on existing patterns
- **implement_plan**: Implements plans by writing code and updating files

### Sub-Agents
- **codebase-locator**: Locates files and components relevant to tasks
- **codebase-analyzer**: Analyzes implementation details and traces data flow
- **codebase-pattern-finder**: Finds similar implementations and usage examples
- **thoughts-locator**: Discovers relevant documents in the thoughts directory
- **thoughts-analyzer**: Extracts key insights from thought documents

## Getting Started

1. Install OpenCode CLI
2. Set up your project
3. Use the CLI commands

For detailed instructions, see: [https://opencode.ai/](https://opencode.ai/)

## License

This project is dual-licensed:

- **Overall Project**: MIT License - see the [LICENSE](LICENSE) file for details
- **HumanLayer-inspired Agent System**: Apache License 2.0 - see the [LICENSE-APACHE](LICENSE-APACHE) file
- **Skills**: Licensed under MIT unless a specific LICENSE file exists in the skill's folder

## Note

This is a personal project inspired by HumanLayer agent architecture and not affiliated with OpenCode. The agent system design is heavily influenced by the HumanLayer framework but adapted for personal use with OpenCode CLI.

## Future Ideas & TODO

### Agent Enhancements
- **Refactoring Agent**: A specialized agent for code refactoring with safety checks
- **Task Description Agent**: Creates structured task descriptions for better organization
- **Workflow Agent**: Handles git commits, CHANGELOG.md updates, and version management
- **Release Agent**: Automates release processes including version bumping and tagging

### Command Ideas
- `/refactor "code pattern" "new pattern"` - Safe code refactoring
- `/create-task "task description"` - Structured task creation
- `/handle-workflow "commit message"` - Automated commit and version management
- `/update-changelog "version" "changes"` - CHANGELOG.md updates

### Workflow Improvements
- **Automated Versioning**: Auto-detect version bumps based on commit types
- **Change Tracking**: Automatic CHANGELOG.md generation from commits
- **Release Automation**: Streamlined release process with safety checks
- **Task Organization**: Better task management and prioritization
