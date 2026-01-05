# User Stories Guide

## Template

```
As a [role]
I want [feature]
So that [benefit]
```

## Best Practices

1. **Role**: Be specific about who will use this feature
2. **Feature**: Describe the capability, not the implementation
3. **Benefit**: Explain why this is valuable

## Examples

### Good Example: Data Analysis
```
As a data analyst
I want to export query results to CSV
So that I can analyze the data in Excel
```

### Bad Example (too vague)
```
As a user
I want better reporting
So that I can see data
```

### GenAI Infrastructure Examples

#### Example 1: API Key Management
```
As a backend developer
I want to generate API keys for my applications
So that I can securely authenticate requests to the GenAI API
```

#### Example 2: Model Fine-tuning
```
As a data scientist
I want to upload training data and fine-tune models
So that I can create domain-specific AI models for my use case
```

#### Example 3: Prompt Template Management
```
As a product manager
I want to version and test different prompt templates
So that I can optimize AI responses without code changes
```

#### Example 4: Token Usage Tracking
```
As a team admin
I want to monitor token usage across team members
So that I can manage costs and set appropriate limits
```

#### Example 5: Model Deployment Pipeline
```
As an ML engineer
I want to deploy trained models to production with rollback capability
So that I can safely release new model versions
```

## Advanced Patterns

### Epic → Features → User Stories

```
Epic: Improve Reporting System
  Feature: Export Capabilities
    User Story: Export to CSV
    User Story: Export to PDF
    User Story: Scheduled exports
```

### Acceptance Criteria

Add acceptance criteria to make user stories testable:

```
As a marketing manager
I want to see campaign performance dashboards
So that I can track ROI

Acceptance Criteria:
- Dashboard shows impressions, clicks, conversions
- Data can be filtered by date range
- Real-time updates (within 5 minutes)
```