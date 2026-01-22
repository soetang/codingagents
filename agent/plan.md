---
description: Creates and manages implementation plans. Can write plan documents, request edits, and run safe git commands like git status and git diff.
mode: "primary"
permission:
  edit: ask
  write: allow  
  bash:
    "git status": allow
    "git diff*": allow
    "git log*": allow
    "git branch --show-current": allow
    "*": ask
---
