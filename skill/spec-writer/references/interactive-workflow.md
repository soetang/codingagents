# Interactive Requirements Workflow

## Quick Reference for Streamlined Requirements Creation

### Workflow Overview

```
START → Problem & User Stories → Requirements → User Flows → Testing & Scope → Write Requirements → END
```

**Total Time: ~20 minutes**

### Step-by-Step Guide with Prompts

#### Step 1: Problem & User Stories (5 min)

**Objective:** Understand what we're building and why

**LLM Prompts:**
```
"What problem are we trying to solve?"
"Who will use this feature?"
"What value does this provide?"
"Can you give me the primary user story in: 'As a [role], I want [capability], so that [benefit]'?"
"Are there secondary user stories we should consider?"
```

**User Input Examples:**
- Problem: "Developers can't self-service API keys, have to contact support"
- Users: "Backend developers integrating with our API"
- Value: "Reduces support burden, faster developer onboarding"
- Primary story: "As a developer, I want to create API keys, so that I can authenticate my apps"

**Output:** Clear problem statement and 1-3 user stories

---

#### Step 2: Requirements (5 min)

**Objective:** Define what the system must do

**LLM Prompts:**
```
"What are the core capabilities the system must have?"
"What actions must users be able to perform?"
"Are there any performance requirements?" (e.g., "< 500ms response")
"What about security requirements?"
"Any scalability needs?" (e.g., "Support 1000 concurrent users")
"What constraints or limitations should we consider?"
```

**User Input Examples:**
- Core: "Generate keys, view keys, revoke keys, label keys"
- Performance: "Key validation under 50ms"
- Security: "Keys hashed in database, rate limit failed attempts"
- Scalability: "10,000 validations per second"
- Constraints: "Must work with existing auth system"

**Output:** 5-10 functional requirements, 3-5 non-functional requirements

---

#### Step 3: User Flows (5 min)

**Objective:** Map the user journey

**LLM Prompts:**
```
"Walk me through the happy path: what does the user do step by step?"
"What does the user see at each step?"
"What are the most common error scenarios?"
"What error messages should users see?"
"What edge cases might occur from the user's perspective?"
```

**User Input Examples:**
- Happy path: "User clicks 'Create Key' → sees key with copy button → copies key → names it"
- Error: "User uses revoked key → gets 401 error → creates new key"
- Edge case: "User closes window before copying → key lost forever"

**Output:** Happy path flow (3-5 steps), 2-3 error scenarios, 2-4 edge cases

---

#### Step 4: Testing & Scope (3 min)

**Objective:** Define how we'll verify success and what's excluded

**LLM Prompts:**
```
"How will we test the happy path from a user perspective?"
"What error conditions should we test?"
"What edge cases need testing?"
"Are there any features or enhancements we're explicitly NOT including?"
"What should we defer to a future version?"
```

**User Input Examples:**
- Happy path test: "Create key, use it in API call, verify it works"
- Error test: "Try using revoked key, verify it fails gracefully"
- Out of scope: "Key rotation, fine-grained permissions, IP allowlisting"

**Output:** 3-5 test scenarios, 3-5 out-of-scope items

---

#### Step 5: Write Requirements (2 min)

**Objective:** Generate the requirements document

**LLM Actions:**
```
1. Compile all gathered information
2. Structure using the template from comprehensive-spec-template.md
3. Write to: thoughts/shared/specs/YYYY-MM-DD-description.md
4. Present summary to user
```

**Document Structure:**
```markdown
# [Feature Name] Requirements

## 1. Overview
- Problem statement
- User stories
- Success criteria

## 2. Functional Requirements
- Core requirements
- Non-functional requirements
- Constraints & assumptions

## 3. User Flows
- Happy path
- Error scenarios
- Edge cases

## 4. Test Scenarios
- Happy path testing
- Error condition testing
- Edge case testing

## 5. Out of Scope

## 6. Open Questions

## 7. References
```

**Output:** Complete requirements document at `thoughts/shared/specs/YYYY-MM-DD-description.md`

---

### Validation and Iteration

**After Writing:**
```
"I've created the requirements document at thoughts/shared/specs/[filename].md

Please review:
- Does the problem statement capture the core issue?
- Are the user stories complete?
- Are requirements specific enough?
- Do the user flows make sense?
- Is the scope clear?"
```

**Iteration Prompts:**
```
"Let's refine the [section] - what needs adjustment?"
"Are there any requirements we missed?"
"Should we add more detail to the user flows?"
"Are there edge cases we haven't considered?"
```

---

### Tips for Effective Requirements Gathering

1. **Ask Specific Questions** - Focus on one aspect at a time
2. **Use Examples** - Concrete scenarios clarify abstract requirements
3. **Stay Business-Focused** - Defer implementation details to planning phase
4. **Think About Users** - Every requirement should connect to user value
5. **Be Concrete** - "< 500ms response" not "fast"
6. **Include Errors** - Error scenarios are just as important as happy path
7. **Set Boundaries** - Out of scope prevents scope creep
8. **Iterate Quickly** - Get something written, then refine

### Common Pitfalls to Avoid

- ❌ **Vague Requirements:** "Should be fast" → ✅ "Response time < 500ms"
- ❌ **Technical Implementation:** "Use Redis cache" → ✅ "Key validation < 50ms"
- ❌ **Missing Edge Cases:** Only happy path → ✅ Include errors and edge cases
- ❌ **Scope Creep:** Everything in scope → ✅ Explicitly list what's out of scope
- ❌ **No User Perspective:** System-focused → ✅ User-focused flows and language

### Example: Quick Session Flow

```
LLM: "What problem are we solving?"
User: "Need API key management for developers."

LLM: "Who will use this?"
User: "Backend developers integrating with our API."

LLM: "Primary user story?"
User: "As a developer, I want to create API keys, so that I can authenticate my apps."

LLM: "Core requirements?"
User: "Generate keys, view list, revoke keys, add labels."

LLM: "Performance needs?"
User: "Key validation under 50ms, support 10k validations/sec."

LLM: "Walk me through the happy path."
User: "User clicks create, sees key, copies it, names it, uses in API."

LLM: "Error scenarios?"
User: "Revoked key returns 401, rate limiting for failed attempts."

LLM: "What's out of scope?"
User: "Key rotation, IP allowlisting, usage analytics."

LLM: "Great! I've captured everything. Writing requirements to thoughts/shared/specs/2025-01-05-api-key-management.md..."
```

**Total: ~15-20 minutes** for a complete, actionable requirements document.

---

### Integration with Planning Phase

Requirements document becomes input to implementation planning:

**Requirements Phase (spec-writer):**
- WHAT needs to be built
- WHY we're building it
- WHO will use it
- WHAT success looks like

**Planning Phase (create-plan):**
- HOW to implement it
- WHAT code changes are needed
- WHAT testing is required
- WHAT the phases are

Clear requirements make planning faster and more accurate.
