---
description: Handles build, test, and development workflow tasks for repositories. Use when the user needs to run builds, execute tests, install dependencies, or perform other development commands.
mode: "primary"
permission:
  edit: allow
  write: allow  
  bash:
    "git status": allow
    "git diff*": allow
    "git log*": allow
    "*": ask
---
