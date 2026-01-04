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

### Good Example
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