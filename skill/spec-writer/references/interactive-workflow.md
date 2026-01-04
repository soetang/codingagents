# Interactive Specification Workflow

## Quick Reference for LLM-Guided Specification Creation

### Workflow Overview

```
START → Gather Requirements → Define Acceptance Criteria → Technical Specification → 
Interface Design → Test Scenarios → Implementation Considerations → Validate → END
```

### Step-by-Step Guide with Prompts

#### 1. Gather Requirements

**Objective:** Understand the problem and user needs

**LLM Prompts:**
```
"What problem are we trying to solve?"
"Who are the main users of this feature?"
"What are the key benefits this feature will provide?"
"Can you provide the primary user story?"
"Are there any secondary user stories?"
```

**User Input Examples:**
- Problem statement
- User roles and personas
- Feature benefits
- User stories in "As a... I want... So that..." format

#### 2. Define Acceptance Criteria

**Objective:** Establish clear completion criteria

**LLM Prompts:**
```
"What must be true for this feature to be considered complete?"
"What are the minimum viable requirements?"
"Are there any specific performance targets?"
"What constraints should we consider?"
"What would make this feature fail acceptance?"
```

**User Input Examples:**
- Functional completion criteria
- Performance metrics (response times, throughput)
- Quality standards
- Constraints and limitations

#### 3. Technical Specification

**Objective:** Define detailed requirements

**LLM Prompts:**
```
"What are the core functional requirements?"
"What non-functional requirements should we consider?"
  - "Performance targets?"
  - "Security requirements?"
  - "Scalability needs?"
"What data structures are needed?"
"What API endpoints are required?"
"What error conditions should we handle?"
"What edge cases might occur?"
```

**User Input Examples:**
- Functional requirements list
- Performance metrics (e.g., "<500ms response time")
- Security requirements (e.g., "Role-based access control")
- Data model definitions
- API specifications
- Error handling strategies

#### 4. Interface Design

**Objective:** Create clean, maintainable interfaces

**LLM Prompts:**
```
"What design pattern would be most appropriate?"
  - "Strategy for multiple algorithms?"
  - "Factory for object creation?"
  - "Observer for event handling?"
"What are the key interfaces needed?"
"What methods should each interface include?"
"What parameters and return types are needed?"
"What exceptions might be raised?"
"Can you provide a code example of the interface?"
```

**User Input Examples:**
- Design pattern choice with rationale
- Interface definitions with methods
- Method signatures with types
- Exception handling strategies
- Code examples

#### 5. Test Scenarios

**Objective:** Ensure comprehensive test coverage

**LLM Prompts:**
```
"What are the happy path scenarios?"
"What error conditions should we test?"
"What performance metrics are important?"
"What integration points need testing?"
"What are the expected results for each scenario?"
"Are there any edge cases we should specifically test?"
```

**User Input Examples:**
- Happy path test cases
- Error condition scenarios
- Performance test targets
- Integration test scenarios
- Expected outcomes for each test

#### 6. Implementation Considerations

**Objective:** Plan for successful implementation

**LLM Prompts:**
```
"What dependencies are required?"
"What configuration options should be available?"
"Are there any special deployment requirements?"
"What monitoring metrics should we track?"
"What logging should be implemented?"
"What alert thresholds should we set?"
```

**User Input Examples:**
- Dependency list with versions
- Configuration options
- Deployment requirements
- Monitoring metrics
- Logging strategies
- Alert thresholds

### Validation and Iteration

**Validation Command:**
```bash
python3 scripts/validate_spec.py comprehensive your_specification.md
```

**Iteration Prompts:**
```
"The validation found missing sections. Let's fill those in."
"Some requirements are vague. Can you provide more specifics?"
"The test scenarios could be more comprehensive. What other cases should we consider?"
"The interface definition needs more detail. What methods are essential?"
```

### Tips for Effective Interactive Specification

1. **Ask Specific Questions:** Focus on one aspect at a time
2. **Provide Examples:** Show templates and patterns
3. **Validate Early:** Check completeness at each step
4. **Iterate:** Allow going back to refine previous answers
5. **Progressive Detail:** Start broad, then get specific
6. **User-Friendly:** Explain technical concepts when needed
7. **Complete Coverage:** Ensure all sections are addressed

### Common Pitfalls to Avoid

- **Vague Requirements:** "Should be fast" → "Response time <500ms"
- **Missing Edge Cases:** Consider error conditions and boundaries
- **Incomplete Interfaces:** Define all necessary methods and parameters
- **Poor Test Coverage:** Include happy path, errors, performance, integration
- **Unclear Acceptance Criteria:** Make criteria measurable and testable

### Example Interactive Session Flow

```
LLM: "Let's create a comprehensive specification. What problem are we solving?"

User: "We need a payment processing system for our e-commerce platform."

LLM: "Great! Who are the main users of this payment system?"

User: "Customers making purchases, finance team monitoring transactions, and support staff handling refunds."

LLM: "Perfect. Let's start with the primary user story for customers:"

User: "As a customer, I want to complete my purchase securely so that I can receive my order."

LLM: "Excellent! Now let's define acceptance criteria. What must be true for the payment system to be complete?"

User: "Must support credit cards and PayPal, process payments in <2s, have <1% failure rate, and be PCI compliant."

LLM: "Great metrics! Now let's dive into functional requirements..."

...and so on through each section.
```