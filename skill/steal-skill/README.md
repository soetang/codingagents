# Steal Skill

Steal existing skills, commands, and agents from GitHub repositories.

## Overview

This tool copies valid, existing resources from GitHub repos - it does **not** convert arbitrary repos into skills/commands/agents.

## Important

This tool **only steals existing resources**:

- **For skills**: Target path must contain a `SKILL.md` file
- **For commands**: Target path must point to a `.md` file  
- **For agents**: Target path must point to a `.md` file

If you point to a wrong location, the tool will list available resources it found in the repository.

## Requirements

```bash
pip install httpx
```

## Quick Start

### Steal a Skill

```bash
cd ~/.config/opencode/skill/steal-skill

# Steal slack-gif-creator from Anthropics
python3 scripts/steal_to_skill.py anthropics/skills --path skills/slack-gif-creator
```

### Steal a Command

```bash
# Steal a command file
python3 scripts/steal_to_command.py user/repo --path commands/my-command.md
```

### Steal an Agent

```bash
# Steal an agent file
python3 scripts/steal_to_agent.py user/repo --path agents/my-agent.md
```

## Available Scripts

### 1. steal_to_skill.py

Steals an existing skill from a GitHub repository.

**Usage:**
```bash
python3 scripts/steal_to_skill.py <username/repo> --path <path-to-skill> [OPTIONS]
```

**Options:**
- `--path <subpath>` - Path to the skill directory (must contain SKILL.md)
- `--dest <directory>` - Destination directory (default: `./skill/`)
- `--name <custom-name>` - Custom name for the skill

**Examples:**
```bash
# Steal from Anthropics skills repo
python3 scripts/steal_to_skill.py anthropics/skills --path skills/slack-gif-creator

# Steal from OpenCode-style repo
python3 scripts/steal_to_skill.py soetang/codingagents --path skill/hello-world

# Custom destination
python3 scripts/steal_to_skill.py user/repo --path skill/my-skill --dest ~/.config/opencode/skill
```

**What happens:**
- ✅ Downloads the repo
- ✅ Verifies SKILL.md exists at the target path
- ✅ Copies entire skill directory
- ❌ If no SKILL.md found: Lists all available skills in the repo

### 2. steal_to_command.py

Steals an existing command from a GitHub repository.

**Usage:**
```bash
python3 scripts/steal_to_command.py <username/repo> --path <command.md> [OPTIONS]
```

**Options:**
- `--path <file>` - **Required** - Path to the .md command file
- `--dest <directory>` - Destination directory (default: `./command/`)
- `--name <custom-name>` - Custom name for the command

**Examples:**
```bash
# Steal a command
python3 scripts/steal_to_command.py user/repo --path commands/check-code.md

# Custom destination
python3 scripts/steal_to_command.py user/repo --path cmd.md --dest ~/.config/opencode/command
```

**What happens:**
- ✅ Downloads the repo
- ✅ Verifies path points to a .md file
- ✅ Copies the .md file
- ❌ If not a .md file: Lists all available .md files in the repo

### 3. steal_to_agent.py

Steals an existing agent from a GitHub repository.

**Usage:**
```bash
python3 scripts/steal_to_agent.py <username/repo> --path <agent.md> [OPTIONS]
```

**Options:**
- `--path <file>` - **Required** - Path to the .md agent file
- `--dest <directory>` - Destination directory (default: `./agent/`)
- `--name <custom-name>` - Custom name for the agent

**Examples:**
```bash
# Steal an agent
python3 scripts/steal_to_agent.py user/repo --path agents/code-reviewer.md

# Custom destination
python3 scripts/steal_to_agent.py user/repo --path agent.md --dest ~/.config/opencode/agent
```

**What happens:**
- ✅ Downloads the repo
- ✅ Verifies path points to a .md file
- ✅ Copies the .md file
- ❌ If not a .md file: Lists all available .md files in the repo

## Common Patterns

### Discover Available Skills

Point to a repo or wrong path to see what's available:

```bash
python3 scripts/steal_to_skill.py anthropics/skills
```

Output:
```
❌ No SKILL.md found

Found 17 skill(s) in this repository:
  - skills/slack-gif-creator/
  - skills/skill-creator/
  - skills/mcp-builder/
  ...

💡 Try one of these:
  python3 steal_to_skill.py <repo> --path skills/slack-gif-creator
```

### Different Repository Conventions

The tool handles multiple naming conventions:

**Anthropics style:**
```bash
python3 scripts/steal_to_skill.py anthropics/skills --path skills/my-skill
```

**OpenCode style:**
```bash
python3 scripts/steal_to_skill.py user/repo --path skill/my-skill
```

**Standard .claude/ convention:**
```bash
python3 scripts/steal_to_skill.py user/agent-resources --path .claude/skills/my-skill
```

## Examples

### Example 1: Steal Anthropic's slack-gif-creator skill

```bash
cd ~/.config/opencode/skill/steal-skill

python3 scripts/steal_to_skill.py anthropics/skills \
  --path skills/slack-gif-creator \
  --dest ~/.config/opencode/skill
```

This skill is from Anthropic and provides utilities for creating animated GIFs optimized for Slack.

### Example 2: Discover and steal from a new repo

```bash
# First, discover what's available
python3 scripts/steal_to_skill.py someuser/cool-repo

# Output shows available skills, then steal one:
python3 scripts/steal_to_skill.py someuser/cool-repo --path skill/the-one-i-want
```

### Example 3: Steal with custom name

```bash
python3 scripts/steal_to_skill.py user/repo \
  --path skill/original-name \
  --name my-custom-name
```

## Error Handling

### Skill not found

If SKILL.md doesn't exist at the path:
```
❌ No SKILL.md found at path 'wrong-path'

Found 5 skill(s) in this repository:
  - skill/skill-a/
  - skill/skill-b/
  ...
```

### Command/Agent not .md file

If you point to a directory or non-.md file:
```
❌ Path 'some-dir' does not point to a valid .md command file.

Found 3 command(s) in this repository:
  - commands/cmd-a.md
  - commands/cmd-b.md
  ...
```

## Development

The tool is structured as three standalone scripts that share common patterns:

- `scripts/steal_to_skill.py` - Steals skills (directories with SKILL.md)
- `scripts/steal_to_command.py` - Steals commands (.md files)
- `scripts/steal_to_agent.py` - Steals agents (.md files)

Each script includes:
- GitHub repo download/extraction
- Resource discovery (finding all available resources)
- Validation (ensuring target is valid)
- Helpful error messages with suggestions

## License

MIT License - See LICENSE file for details
