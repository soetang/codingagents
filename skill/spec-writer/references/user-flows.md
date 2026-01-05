# User Flows Guide

User flows describe how users interact with your feature from their perspective. Focus on the user's journey, not technical implementation.

## Structure

```
[User Action] → [System Response] → [User Sees/Experiences]
```

## Best Practices

1. **Start with the user's goal** - What are they trying to accomplish?
2. **Use simple language** - Avoid technical jargon
3. **Include decision points** - Where do users make choices?
4. **Show system feedback** - What does the user see at each step?
5. **Document error scenarios** - What happens when things go wrong?

## Template

### Happy Path
```
1. User [action] → System [response] → User sees [outcome]
2. User [next action] → System [response] → User achieves [goal]
```

### Error Scenarios
```
1. User [invalid action] → System shows [error message] → User can [recovery option]
2. System encounters [issue] → User sees [helpful message] → User can [alternative action]
```

### Edge Cases (User Perspective)
```
- What if user has no data yet?
- What if user lacks permissions?
- What if user tries to do X before Y?
```

## Examples

### Example 1: Authentication Flow

**Happy Path:**
1. User opens app → System shows login screen → User sees email/password fields
2. User enters credentials and clicks "Login" → System validates → User sees dashboard
3. User clicks "Remember me" → System stores session → User stays logged in

**Error Scenarios:**
1. User enters wrong password → System shows "Invalid credentials" message → User can retry or click "Forgot password"
2. User's session expires → System redirects to login → User sees "Your session has expired, please log in again"

**Edge Cases:**
- What if user has never logged in? → Show welcome/onboarding flow
- What if user forgot password? → Self-service reset link via email
- What if user is already logged in? → Skip login, go to dashboard

### Example 2: API Key Management (GenAI Infrastructure)

**Happy Path:**
1. Developer navigates to API settings → System shows current keys → Developer sees list of active keys
2. Developer clicks "Create New Key" → System generates key → Developer sees key with copy button
3. Developer names the key "Production API" → System saves label → Key appears in list with name

**Error Scenarios:**
1. Developer reaches key limit → System shows "Maximum keys reached" → Developer must delete old key first
2. Developer tries to regenerate revoked key → System shows "Cannot regenerate revoked keys" → Developer creates new key instead

**Edge Cases:**
- What if developer hasn't created any keys yet? → Show empty state with "Create Your First Key" CTA
- What if key is compromised? → Show "Revoke" button with confirmation dialog
- What if developer loses the key after creation? → Show warning: "Copy now, cannot be viewed again"

### Example 3: Model Training Pipeline

**Happy Path:**
1. Data scientist uploads training data → System validates format → Scientist sees "Data validated successfully"
2. Scientist configures hyperparameters → System shows preview of config → Scientist clicks "Start Training"
3. System begins training → Scientist sees progress bar and metrics → Training completes with accuracy score

**Error Scenarios:**
1. Scientist uploads invalid data format → System shows "CSV format required, received JSON" → Scientist can download format template
2. Training fails due to OOM → System shows "Memory limit exceeded, reduce batch size" → Scientist adjusts config and retries

**Edge Cases:**
- What if training takes hours? → Email notification when complete
- What if scientist wants to stop mid-training? → Show "Cancel" button with progress preservation option
- What if previous training is still running? → Queue new job or show warning

## Writing Tips

### DO:
- ✅ Focus on what the user experiences
- ✅ Use concrete, specific actions
- ✅ Include system feedback at each step
- ✅ Think about error recovery
- ✅ Consider the user's mental model

### DON'T:
- ❌ Include implementation details ("database query runs")
- ❌ Use technical terminology ("OAuth handshake completes")
- ❌ Skip error scenarios
- ❌ Assume users know your system
- ❌ Forget about edge cases

## Questions to Ask

When documenting user flows, consider:

1. **Goal**: What is the user trying to accomplish?
2. **Entry Point**: Where does this flow start?
3. **Steps**: What actions does the user take?
4. **Feedback**: What does the user see/hear/experience at each step?
5. **Decisions**: Where do users make choices?
6. **Success**: How does the user know they succeeded?
7. **Failure**: What happens when something goes wrong?
8. **Recovery**: How can users fix errors or try again?
9. **Edge Cases**: What unusual situations might occur?
10. **Exit**: Where does this flow end?

## Integration with Requirements

User flows should directly support your user stories:

**User Story:**
```
As a developer
I want to create API keys
So that I can authenticate my applications
```

**User Flow:**
```
1. Developer navigates to API Keys page
2. Developer clicks "Create New Key"
3. System generates unique key and shows it once
4. Developer copies key and names it
5. Developer uses key in their application
```

The flow shows HOW the user story gets accomplished from the user's perspective.
