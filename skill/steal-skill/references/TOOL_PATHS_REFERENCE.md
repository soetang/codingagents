# Tool Paths Reference

This document provides a reference for the different directory structures and output paths used by various AI coding tools.

## OpenCode

**Configuration Paths:**
- Global config: `~/.config/opencode/`
- Repository config: `.opencode/` (in project root)

**Resource Directories:**
- Skills: `skill/` (singular)
- Commands: `command/` (singular)
- Agents: `agent/` (singular)

**Precedence Order:**
Repository-specific configurations take precedence over global configurations. See [OpenCode Config Documentation](https://opencode.ai/docs/config/#precedence-order) for details.

**Example Paths:**
```
~/.config/opencode/skill/my-skill/
~/.config/opencode/command/my-command.md
~/.config/opencode/agent/my-agent.md

.opencode/skill/project-specific-skill/
.opencode/command/project-specific-command.md
.opencode/agent/project-specific-agent.md
```

---

## Codex (OpenAI)

**Configuration Paths:**
- Global config: `~/.codex/`
- Repository config: `.codex/` (in project root)

**Resource Directories:**
- Skills: `skills/` (plural)
- Commands: `commands/` (plural)
- Agents: `agents/` (plural)

**Documentation:**
- [Basic Configuration](https://developers.openai.com/codex/config-basic/)

**Example Paths:**
```
~/.codex/skills/my-skill/
~/.codex/commands/my-command.md
~/.codex/agents/my-agent.md

.codex/skills/project-specific-skill/
.codex/commands/project-specific-command.md
.codex/agents/project-specific-agent.md
```

---

## Claude Code (Anthropic)

**Configuration Paths:**
- Global config: `~/.claude/`
- Repository config: `.claude/` (in project root)

**Resource Directories:**
- Skills: `skills/` (plural)
- Commands: `commands/` (plural)
- Agents: `agents/` (plural)

**Documentation:**
- [Settings Documentation](https://code.claude.com/docs/en/settings)

**Example Paths:**
```
~/.claude/skills/my-skill/
~/.claude/commands/my-command.md
~/.claude/agents/my-agent.md

.claude/skills/project-specific-skill/
.claude/commands/project-specific-command.md
.claude/agents/project-specific-agent.md
```

---

## Quick Comparison Table

| Tool | Config Dir | Skills Dir | Commands Dir | Agents Dir | Resource Format |
|------|-----------|-----------|--------------|-----------|----------------|
| **OpenCode** | `.opencode/` | `skill/` | `command/` | `agent/` | Singular |
| **Codex** | `.codex/` | `skills/` | `commands/` | `agents/` | Plural |
| **Claude Code** | `.claude/` | `skills/` | `commands/` | `agents/` | Plural |

---

## Notes for Steal-Skill Tool

When stealing resources from different tool ecosystems:

1. **OpenCode** uses singular directory names (`skill/`, `command/`, `agent/`)
2. **Codex and Claude Code** use plural directory names (`skills/`, `commands/`, `agents/`)
3. All tools support both global and repository-specific configurations
4. Skills require a marker file:
   - OpenCode: `SKILL.md`
   - Claude Code: `SKILL.md`
   - Codex: `SKILL.md` or `skill.yaml`
5. Commands and Agents are typically single `.md` files

### Search Patterns

The steal-skill scripts already handle these variations through glob patterns:

```python
# For skills
"skills/*/SKILL.md",       # Claude Code / Codex style
"skill/*/SKILL.md",        # OpenCode style
".claude/skills/*/SKILL.md",  # Claude Code repo-specific
".codex/skills/*/SKILL.md",   # Codex repo-specific
".opencode/skill/*/SKILL.md", # OpenCode repo-specific

# For commands
"commands/*.md",          # Claude Code / Codex
"command/*.md",           # OpenCode
".claude/commands/*.md",  # Claude Code repo-specific
".codex/commands/*.md",   # Codex repo-specific
".opencode/command/*.md", # OpenCode repo-specific

# For agents
"agents/*.md",          # Claude Code / Codex
"agent/*.md",           # OpenCode
".claude/agents/*.md",  # Claude Code repo-specific
".codex/agents/*.md",   # Codex repo-specific
".opencode/agent/*.md", # OpenCode repo-specific
```
