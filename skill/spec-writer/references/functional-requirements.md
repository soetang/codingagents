# Functional Requirements Guide

Functional requirements describe WHAT the system must do from a business and user perspective, not HOW it's implemented.

## Structure

```markdown
## Functional Requirements

### Core Requirements
- System must [capability]
- Users must be able to [action]
- Data must be [constraint]

### Non-Functional Requirements

**Performance:**
- [Specific metric with target]
- [Response time requirement]

**Security:**
- [Authentication requirement]
- [Data protection requirement]

**Scalability:**
- [Volume requirement]
- [Growth expectation]
```

## Best Practices

1. **Be Specific**: Use measurable criteria
2. **Use "Must" Language**: Clear about what's required
3. **Stay High-Level**: Avoid implementation details
4. **Focus on Capability**: Not the technical solution
5. **Include Constraints**: What limitations exist?

## Core vs Non-Functional

### Core (Functional) Requirements
What the system does:
- Features and capabilities
- User actions
- Data handling
- Business rules

### Non-Functional Requirements
How well it does it:
- Performance targets
- Security standards
- Scalability needs
- Reliability expectations

## Examples

### Good Example: API Key Management

**Core Requirements:**
- System must generate unique API keys on demand
- Users must be able to create, view, and revoke keys
- Keys must be shown only once at creation
- System must allow users to label keys for identification
- Revoked keys must immediately stop working

**Non-Functional Requirements:**

**Performance:**
- Key generation < 200ms
- Key validation < 50ms
- Support 10,000 key validations per second

**Security:**
- Keys must be cryptographically secure (256-bit)
- Keys must be hashed before storage
- Failed validation attempts must be rate-limited

**Scalability:**
- Support 100,000 active keys per organization
- Handle 1M+ validation requests per minute

### Bad Example (Too Technical)

❌ **Don't write like this:**
- Use JWT tokens with RS256 signing
- Implement Redis cache for key lookups
- Create PostgreSQL table with uuid primary key
- Use bcrypt with cost factor 12

✅ **Write like this instead:**
- System must authenticate API requests securely
- Key validation must be fast (< 50ms)
- Keys must be stored securely (not in plaintext)
- System must handle high validation volume

### Example: Model Training Pipeline

**Core Requirements:**
- System must accept training data in CSV or JSON format
- Users must be able to configure hyperparameters before training
- System must validate data format before starting training
- Users must be able to monitor training progress in real-time
- System must save trained models automatically
- Users must be able to cancel training jobs

**Non-Functional Requirements:**

**Performance:**
- Support datasets up to 10GB
- Training start time < 30 seconds
- Progress updates every 5 seconds

**Security:**
- Training data must be encrypted in transit
- Models must be access-controlled by user/team
- Training logs must not expose sensitive data

**Scalability:**
- Support 50 concurrent training jobs
- Queue additional jobs automatically
- Scale compute resources based on load

### Example: GenAI Chat Interface

**Core Requirements:**
- System must stream responses token-by-token to users
- Users must be able to stop generation mid-stream
- System must maintain conversation context across messages
- Users must be able to edit previous messages and regenerate
- System must handle code blocks with syntax highlighting
- Conversations must be saved automatically

**Non-Functional Requirements:**

**Performance:**
- First token latency < 500ms
- Streaming rate 50+ tokens/second
- Context switching < 200ms

**Security:**
- Conversations must be private per user
- API keys must not be logged
- PII must be filtered from training data

**Scalability:**
- Support 1,000 concurrent conversations
- Handle conversations with 100+ messages
- Store 1M+ conversations per user

## Constraints & Assumptions

Always document:

### Constraints
What limits or restricts the solution:
- Budget limitations
- Technology choices (must use existing stack)
- Regulatory requirements
- Timeline constraints
- Resource availability

### Assumptions
What you're assuming to be true:
- User has internet connection
- Browser supports WebSockets
- Data is in English
- Users are authenticated
- Third-party APIs are available

**Example:**
```markdown
### Constraints & Assumptions

**Constraints:**
- Must integrate with existing authentication system
- Cannot store PII outside EU (GDPR)
- Must complete within 3-month timeline
- Limited to current cloud budget

**Assumptions:**
- Users have modern browsers (last 2 years)
- Average dataset size < 1GB
- Peak usage during business hours
- Users understand basic ML concepts
```

## Writing Tips

### DO:
- ✅ Start with "System must" or "Users must be able to"
- ✅ Use measurable criteria (< 500ms, 99.9% uptime)
- ✅ Focus on business value
- ✅ Include performance targets
- ✅ Document constraints

### DON'T:
- ❌ Specify implementation ("use Redis")
- ❌ Include code or architecture details
- ❌ Use vague terms ("should be fast")
- ❌ Skip non-functional requirements
- ❌ Forget about security and scalability

## Questions to Ask

1. **What must the system do?** (core capabilities)
2. **Who will use it?** (user actions)
3. **What data is involved?** (data requirements)
4. **How fast must it be?** (performance)
5. **How secure?** (security requirements)
6. **How much volume?** (scalability)
7. **What are the constraints?** (limitations)
8. **What are we assuming?** (assumptions)
9. **What error conditions exist?** (error handling)
10. **What shouldn't it do?** (out of scope)

## Integration with User Stories

Requirements should directly support user stories:

**User Story:**
```
As a data scientist
I want to train ML models on my data
So that I can make predictions
```

**Functional Requirements:**
```
- System must accept training data in CSV/JSON format
- Users must be able to configure model hyperparameters
- System must train models and report accuracy metrics
- Users must be able to download trained models
- System must notify users when training completes
```

Each requirement makes the user story achievable.
