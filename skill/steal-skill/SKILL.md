---
name: steal-skill
description: Steal existing skills, commands, and agents from GitHub repositories. Use when the user wants to copy/import valid OpenCode resources from external GitHub repos. Only works with existing resources (does not convert arbitrary repos).
---

# Steal Skill

## Overview

Steal existing skills, commands, and agents from GitHub repositories. This tool copies valid, existing resources - it does **not** convert arbitrary repos into skills/commands/agents.

## Important Notes

This tool **only steals existing resources** - it does not convert arbitrary repos:

- **For skills**: Target path must contain a `SKILL.md` file
- **For commands**: Target path must point to a `.md` file  
- **For agents**: Target path must point to a `.md` file

If you point to a wrong location, the tool will list available resources it found in the repository.

## When to Use

Use this skill when:
- User wants to steal/copy existing skills from a GitHub repo
- User wants to import commands or agents from a GitHub repo
- The repo uses different naming conventions (e.g., `skills/`, `skill/`, `.claude/skills/`)
- You need to extract a specific resource from a larger repo
- You want to quickly import external resources into OpenCode

## Available Scripts

### 1. steal_to_skill.py

Steals an existing skill from a GitHub repository.

**Usage:**
```bash
python3 scripts/steal_to_skill.py <username/repo> [OPTIONS]
```

**Options:**
- `--path <subpath>` - Path to the skill directory in the repo (must contain SKILL.md)
- `--dest <directory>` - Destination directory (default: `./skill/`)
- `--name <custom-name>` - Custom name for the skill

**Examples:**
```bash
# Steal a skill from Anthropics repo
python3 scripts/steal_to_skill.py anthropics/skills --path skills/analyze-paper

# Steal from OpenCode-style repo
python3 scripts/steal_to_skill.py soetang/codingagents --path skill/hello-world

# Use custom destination
python3 scripts/steal_to_skill.py user/repo --path skills/my-skill --dest ~/.config/opencode/skill

# GitHub URL format
python3 scripts/steal_to_skill.py https://github.com/user/repo --path skill/my-skill

# Custom skill name
python3 scripts/steal_to_skill.py user/repo --path skill/original-name --name my-custom-name
```

**Behavior:**
- **Requires**: Source directory must contain `SKILL.md`
- **If no SKILL.md found**: Shows error and lists all available skills in the repo
- Copies entire skill directory as-is
- Sanitizes skill names to lowercase with hyphens

### 2. steal_to_command.py

Steals an existing command from a GitHub repository.

**Usage:**
```bash
python3 scripts/steal_to_command.py <username/repo> --path <command.md> [OPTIONS]
```

**Options:**
- `--path <file>` - **Required** - Path to the .md command file in repo
- `--dest <directory>` - Destination directory (default: `./command/`)
- `--name <custom-name>` - Custom name for the command

**Examples:**
```bash
# Steal a command file
python3 scripts/steal_to_command.py user/repo --path command/check-code.md

# Steal from commands directory
python3 scripts/steal_to_command.py user/repo --path commands/my-command.md

# Use custom destination
python3 scripts/steal_to_command.py user/repo --path script.md --dest ~/.config/opencode/command
```

**Behavior:**
- **Requires**: Path must point to a `.md` file
- **If not a .md file**: Shows error and lists all available commands in the repo
- Copies the .md file to the destination

### 3. steal_to_agent.py

Steals an existing agent from a GitHub repository.

**Usage:**
```bash
python3 scripts/steal_to_agent.py <username/repo> --path <agent.md> [OPTIONS]
```

**Options:**
- `--path <file>` - **Required** - Path to the .md agent file in repo
- `--dest <directory>` - Destination directory (default: `./agent/`)
- `--name <custom-name>` - Custom name for the agent

**Examples:**
```bash
# Steal an agent file
python3 scripts/steal_to_agent.py user/repo --path agent/code-reviewer.md

# Steal from agents directory
python3 scripts/steal_to_agent.py user/repo --path agents/my-agent.md

# Use custom destination
python3 scripts/steal_to_agent.py user/repo --path agent.md --dest ~/.config/opencode/agent
```

**Behavior:**
- **Requires**: Path must point to a `.md` file
- **If not a .md file**: Shows error and lists all available agents in the repo
- Copies the .md file to the destination

## Workflow

When a user asks to steal/import a resource from a GitHub repository:

1. **Identify the resource type** they want (skill/command/agent)

2. **Determine the repository details**:
   - GitHub username/repo or full URL
   - Specific path within the repo pointing to the resource
   - Desired destination directory

3. **Run the appropriate script**:
   ```bash
   cd ~/.config/opencode/skill/steal-skill
   python3 scripts/steal_to_skill.py <username/repo> --path <path-to-skill> [options]
   ```

4. **If the path is wrong**: The script will list all available resources in the repo

5. **Verify and test** the stolen resource in OpenCode

## Common Patterns

### Pattern 1: Steal from Anthropics-style Repo
```bash
# Anthropics uses skills/ directory (not .claude/skills/)
python3 scripts/steal_to_skill.py anthropics/skills --path skills/some-skill-name
```

### Pattern 2: Steal from OpenCode-style Repo
```bash
# OpenCode uses singular directories: skill/, command/, agent/
python3 scripts/steal_to_skill.py soetang/codingagents --path skill/my-skill
```

### Pattern 3: Steal from Standard .claude/ Repo
```bash
# Standard agent-resources convention
python3 scripts/steal_to_skill.py username/agent-resources --path .claude/skills/my-skill
```

### Pattern 4: List Available Resources
```bash
# Point to repo root or wrong path to see available resources
python3 scripts/steal_to_skill.py username/repo
# Script will error and list all skills it found
```

## Requirements

All scripts require the `httpx` library:
```bash
pip install httpx
```

## Troubleshooting

**"Repository not found"** - Verify the repo exists and is public; script tries both main/master branches

**"Path not found in repository"** - Double-check the --path value; paths are case-sensitive

**"httpx is required"** - Install httpx: `pip install httpx`
