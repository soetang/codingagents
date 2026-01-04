---
description: Capture agent/skill/command improvement and create GitHub issue
agent: general
subtask: false
---

You are helping the user create an improvement suggestion for an OpenCode component (agent/skill/command) and submit it as a GitHub issue.

Follow these steps carefully:

## Step 1: Gather Information

Ask the user for the following information (ask one question at a time for clarity):

1. **Component Type**: What type of component needs improvement? (agent/skill/command)
2. **Component Name**: Which specific component? (e.g., "codebase-analyzer", "spec-writer", "test")
3. **Model Used**: What model were you using when you noticed the issue? (e.g., "claude-3-5-sonnet-20241022")
4. **Your Goal**: What were you trying to accomplish?
5. **What Went Wrong**: Where did the component fail or perform poorly?
6. **Improvement Suggestion**: What specific improvement would you suggest?

## Step 2: Generate Issue Template

Once you have all the information, generate an issue description following this format:

```
## Improvement Suggestion for [Component Type]: [Component Name]

**Model**: [model-name]

**User Goal**:
- [What the user was trying to accomplish]

**Issue Observed**:
- [What went wrong]
- [Where the component failed]

**Suggested Improvement**:
- [Specific improvement suggestion]

**Context**:
- Session: [current date and time]
- Component path: [component-type]/[component-name].md
```

## Step 3: Show Preview and Allow Editing

Present the generated issue description to the user and say:

```
Here's the issue description I've generated. You can:
1. Approve it as-is (type 'approve' or 'yes')
2. Edit it (type 'edit' and provide your modifications)
3. Cancel (type 'cancel' or 'no')

What would you like to do?
```

If the user wants to edit:
- Ask them to provide their edited version
- Show the new version and ask for approval again

## Step 4: Create GitHub Issue

Once approved, create the issue using the gh CLI:

1. Generate issue title: `Improve [component-type]: [component-name] - [brief issue summary]`
2. Use this bash command to create the issue:

```bash
gh issue create \
  --repo soetang/codingagents \
  --title "[issue title]" \
  --body "[issue description]"
```

## Step 5: Confirm Success

After creating the issue:
- Show the issue URL to the user
- Confirm that it was created successfully
- Remind them they can edit or add comments on GitHub

---

**Important Notes**:
- Keep all responses concise and use bullet points
- Be conversational but efficient
- If gh CLI fails, show the error and suggest checking authentication with `gh auth status`
