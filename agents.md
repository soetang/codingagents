# OpenCode Configuration Repository

This repository contains personal OpenCode CLI configuration including custom agents, skills, and workflows.

## Repository Organization

This repository uses a structured approach to organize OpenCode resources:

- **`agent/`** - Agent definition files (markdown)
- **`skill/`** - Skill packages and definitions
- **`thoughts/`** - Personal notes and planning documents
- **`opencode.jsonc`** - OpenCode configuration

To explore current contents, use standard file navigation tools (ls, glob, read, etc.).

## Working with Agents

### Agent Types

Agents are markdown files with YAML frontmatter that define their mode:

**Primary agents** (`mode: "primary"`):
- Top-level agents invoked directly by users or the main OpenCode instance
- Handle complete workflows and complex tasks
- Examples: research, create-plan, implement_plan, build

**Sub-agents** (`mode: "subagent"`):
- Specialized agents invoked by other agents to handle focused subtasks
- Provide specific capabilities that primary agents leverage
- Examples: codebase-locator, codebase-analyzer, thoughts-locator

### Creating or Updating Agents

When creating or updating agent files:

1. Place markdown files in `agent/` directory
2. Add YAML frontmatter with required fields:
   - `description`: When and how to use the agent
   - `mode`: Either `"primary"` or `"subagent"`
   - `permission`: Optional permissions (e.g., `bash: ask`, `edit: deny`)
3. Follow the established structure from existing agents
4. Include clear instructions for the agent's purpose and workflow
5. Reference any required tools or dependencies
6. Document expected inputs and outputs

### Agent Permissions

Agents can specify granular permissions in their frontmatter:

**Edit permissions:**
- `edit: allow` - Can edit files directly
- `edit: ask` - Must ask before editing
- `edit: deny` - Cannot edit files

**Write permissions:**
- `write: allow` - Can write files directly
- `write: ask` - Must ask before writing
- `write: deny` - Cannot write files

**Bash permissions:**

Bash permissions support pattern-based rules with specific command allowances:

```yaml
bash:
  "exact command": allow      # Exact command allowed
  "command*": allow           # Command with any arguments allowed
  "another command*": deny    # Command explicitly denied
  "*": ask                    # All other commands require permission
```

The pattern matching works as follows:
- Exact strings match specific commands: `"git status": allow`
- Wildcards (`*`) match arguments: `"git diff*": allow` matches `git diff`, `git diff --staged`, etc.
- The catch-all `"*"` specifies the default behavior for unmatched commands
- Rules are evaluated in order, first match wins
- Each rule can have `allow`, `ask`, or `deny` as the permission level

**WebFetch permissions:**
- `webfetch: allow` - Can fetch web content
- `webfetch: ask` - Must ask before fetching
- `webfetch: deny` - Cannot fetch web content

## Working with Skills

Skills are stored in the `skill/` directory. Each skill contains its own documentation and workflow instructions.

To work with skills, read the skill's `SKILL.md` file or explore the `skill_creator` skill for creation workflows.

## Dependencies

### Node.js Dependencies

This repo uses minimal npm dependencies for OpenCode plugins.

**Install dependencies:**
```bash
npm install
```

Check `package.json` for current dependencies.

### Python Dependencies

Python scripts in skill directories require Python 3.x. Most scripts have no external dependencies - check individual script files for requirements.

## Git Workflow

### Committing Changes

When creating commits:

1. Use clear, descriptive commit messages
2. Start with a verb in present tense (e.g., "Add", "Update", "Fix")
3. Keep first line under 72 characters
4. Follow the repository's existing commit style

**Check status before committing:**
```bash
git status
git diff
```

**Standard commit workflow:**
```bash
git add <files>
git commit -m "Brief description of changes"
```

### Branch Strategy

This is a personal repository - work directly on main or create feature branches as needed.

## OpenCode Configuration

### Configuration File

The `opencode.jsonc` file configures OpenCode behavior:

```jsonc
{
    "$schema": "https://opencode.ai/config.json",
    "enabled_providers": ["anthropic", "mistral"],
    "provider": {
        "mistral": {
            "npm": "@ai-sdk/mistral",
            "name": "mistral"
        }
    }
}
```

### Modifying Configuration

When updating `opencode.jsonc`:
- Maintain valid JSON format (with comments)
- Follow the OpenCode schema
- Test changes by running OpenCode CLI

## Development Best Practices

**Organization:**
- Agent files in `agent/`
- Skills in `skill/`
- Thoughts in `thoughts/`
- Configuration in root

**Documentation:**
- Document agent workflows clearly
- Include examples in skill files
- Keep README.md updated

**Testing:**
- Test agent definitions with OpenCode CLI
- Validate skills before packaging
- Verify Python scripts run without errors

**Version Control:**
- Commit logical units of work
- Check `.gitignore` for exclusion patterns

## Common Tasks

### Create a New Agent

1. Create a new `.md` file in `agent/`
2. Follow the structure of existing agents
3. Test with OpenCode CLI
4. Commit the changes

### Create a New Skill

Use the `skill_creator` skill - it contains the full workflow for creating, validating, and packaging skills.

### Add a New AI Provider

1. Install the provider SDK: `npm install @ai-sdk/<provider>`
2. Update `opencode.jsonc` with provider configuration
3. Add to `enabled_providers` array
4. Test the provider with OpenCode CLI

## Troubleshooting

**OpenCode doesn't recognize agents/skills:**
- Verify files are in correct directories
- Check file naming conventions
- Restart OpenCode CLI if needed
