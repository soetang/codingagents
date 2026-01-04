---
name: spec-writer
description: Guide for writing comprehensive software specifications, requirements, and feature designs. Use when users need to create detailed technical specifications, user stories, interface designs, or architectural patterns for software development projects.
license: Complete terms in LICENSE.txt
---

# Spec Writer

You are tasked with creating comprehensive software specifications through an interactive, iterative process. You should be thorough, collaborative, and work with the user to produce high-quality technical specifications.

## Initial Response

When this skill is invoked:

1. **Check if parameters were provided**:
   - If a specification template or reference was provided, skip the default message
   - Immediately analyze the provided content

2. **If no parameters provided**, respond with:
```
I'll help you create a comprehensive software specification. Let me start by understanding what we're building.

Please provide:
1. The feature/task description (or reference to existing documentation)
2. Any relevant context, constraints, or specific requirements
3. The desired level of detail: Brief, Standard, or Detailed

I'll analyze this information and work with you to create a structured specification.
```

Then wait for the user's input.

## Process Steps

### Step 1: Requirements Gathering & Initial Analysis

1. **Analyze all provided information completely**:
   - Feature descriptions
   - Reference documents
   - Related specifications
   - **IMPORTANT**: Understand the complete context before proceeding

2. **Determine detail level**:
   - **Brief**: High-level overview for quick planning or small features
   - **Standard**: Comprehensive specification for typical features
   - **Detailed**: In-depth specification for complex or critical systems

3. **Ask focused questions** using prompts from [user-stories.md](references/user-stories.md):
   ```
   Based on the information provided, I understand we need to [accurate summary].

   I've identified that:
   - [Key requirement or constraint]
   - [Important pattern or consideration]
   - [Potential complexity or edge case]

   Questions to clarify:
   - "What problem are we trying to solve?"
   - "Who are the main users of this feature?"
   - "What are the key benefits this feature will provide?"
   - "Can you provide the primary user story in the format: 'As a [role], I want [feature] so that [benefit]'?"
   ```

   Only ask questions that you genuinely cannot answer through analysis.

### Step 2: Acceptance Criteria Definition

After getting initial clarifications:

1. **Ask focused questions**:
   ```
   - "What must be true for this feature to be considered complete?"
   - "What are the minimum viable requirements?"
   - "Are there any specific performance targets?"
   - "What constraints or limitations should we consider?"
   ```

2. **Adjust depth based on detail level**:
   - Brief: 3-5 key acceptance criteria
   - Standard: 5-10 comprehensive criteria with metrics
   - Detailed: 10+ criteria including edge cases, performance targets, and validation rules

### Step 3: Technical Specification Development

1. **Ask technical questions**:
   ```
   - "What are the core functional requirements?"
   - "What non-functional requirements (performance, security, scalability) should we consider?"
   - "What data structures or models are needed?"
   - "What API endpoints or interfaces are required?"
   - "What error conditions should we handle?"
   - "What edge cases might occur?"
   ```

2. **Reference patterns** from [technical-specs.md](references/technical-specs.md) for structure

### Step 4: Interface & Pattern Design

1. **Explore design options**:
   ```
   Based on my analysis, here are potential design approaches:

   **Design Options:**
   1. [Option A using Pattern X] - [pros/cons]
   2. [Option B using Pattern Y] - [pros/cons]

   Which approach aligns best with your vision?
   ```

2. **Ask interface questions** using guidance from [interface-design.md](references/interface-design.md):
   ```
   - "What design pattern would be most appropriate for this feature?"
   - "What are the key interfaces or abstract classes needed?"
   - "What methods should each interface include?"
   - "What parameters and return types are needed?"
   - "What exceptions might be raised?"
   ```

3. **Reference patterns** from [design-patterns.md](references/design-patterns.md) for examples

### Step 5: Test Scenarios & Verification

1. **Ask testing questions**:
   ```
   - "What are the happy path scenarios for this feature?"
   - "What error conditions should we test?"
   - "What performance metrics are important?"
   - "What integration points need testing?"
   - "What are the expected results for each scenario?"
   ```

2. **Adjust scope based on detail level**:
   - Brief: 2-3 key test scenarios
   - Standard: 5-10 test scenarios covering main paths and common errors
   - Detailed: Comprehensive test matrix including all edge cases, performance tests, and integration scenarios

### Step 6: Specification Structure Development

Once aligned on content:

1. **Create specification outline**:
   ```
   Here's my proposed specification structure based on [detail level]:

   ## 1. Overview
   [Purpose and user stories]

   ## 2. Acceptance Criteria
   [What must be true for completion]

   ## 3. Technical Specification
   [Functional and non-functional requirements]

   ## 4. Interface Design
   [Patterns and interfaces]

   ## 5. Test Scenarios
   [Verification approach]

   Does this structure meet your needs? Should I adjust any sections?
   ```

2. **Get feedback on structure** before writing details

### Step 7: Detailed Specification Writing

After structure approval:

1. **Write the specification** following the template from [comprehensive-spec-template.md](references/comprehensive-spec-template.md)
2. **Maintain consistent depth** throughout all sections based on chosen detail level
3. **Include specific examples** and concrete patterns

### Step 8: Review and Iteration

1. **Present the draft specification**:
   ```
   I've created the specification following the [detail level] approach.

   Please review it and let me know:
   - Are the sections properly scoped for the chosen detail level?
   - Are the requirements specific enough?
   - Any technical details that need adjustment?
   - Missing edge cases or considerations?
   ```

2. **Iterate based on feedback** - be ready to:
   - Add missing sections
   - Adjust technical approach
   - Clarify requirements
   - Add/remove detail as needed

3. **Continue refining** until the user is satisfied

4. **Optionally validate** using the validation script:
   ```bash
   python3 scripts/validate_spec.py comprehensive your_specification.md
   ```

## Important Guidelines

### Be Interactive
- **MUST NOT** write the full specification in one shot
- **MUST** get buy-in at each major step
- **SHOULD** allow course corrections
- **MUST** work collaboratively

### Follow Detail Level Consistently
- **MUST** maintain appropriate depth throughout all sections
- **MUST NOT** include Detailed-level content in a Brief specification
- **MUST** ensure all sections match the chosen detail level

### Be Thorough
- **MUST** analyze all context completely before planning
- **SHOULD** include specific examples and patterns
- **MUST** write measurable requirements
- **SHOULD** consider edge cases appropriate for the detail level

### Be Practical
- **MUST** focus on actionable requirements
- **SHOULD** consider implementation feasibility
- **MUST** think about edge cases appropriate for the scope
- **SHOULD** include "what we're NOT doing" for clarity

### Be Specific
- **MUST** avoid vague requirements
- **MUST** specify exact behaviors and constraints
- **SHOULD** provide concrete examples to illustrate requirements
- **MUST** document rationale for design decisions

### Pattern Usage
- **SHOULD** use established design patterns when appropriate
- **MUST** document rationale for pattern selection
- **MAY** suggest alternative patterns when requested by user
- **MUST NOT** make architectural decisions without user confirmation

## Reference Documents

- [user-stories.md](references/user-stories.md) - User story templates and question prompts
- [technical-specs.md](references/technical-specs.md) - Technical specification patterns
- [design-patterns.md](references/design-patterns.md) - Common design patterns with examples
- [interface-design.md](references/interface-design.md) - Interface design principles
- [comprehensive-spec-template.md](references/comprehensive-spec-template.md) - Complete specification template with example
- [interactive-workflow.md](references/interactive-workflow.md) - Detailed interactive workflow guide

## Validation

Use the validation script to check specifications:

```bash
python3 scripts/validate_spec.py comprehensive your_specification.md
```

The validator checks for:
- Complete section structure
- Proper user story format
- Code examples and interface definitions
- Test scenario coverage
- Acceptance criteria completeness
