# Interface Design Guide

## Principles

### SOLID Principles

1. **Single Responsibility**: Each interface should have one purpose
2. **Open/Closed**: Interfaces should be open for extension, closed for modification
3. **Liskov Substitution**: Subtypes should be substitutable for base types
4. **Interface Segregation**: Clients shouldn't depend on interfaces they don't use
5. **Dependency Inversion**: Depend on abstractions, not concretions

## Best Practices

### Clear Naming

```python
# Good
class DataProcessor:
    def process(self, data: list) -> dict:
        pass

# Bad
class Processor:
    def do_stuff(self, input) -> dict:
        pass
```

### Minimal Interfaces

```python
# Good - focused interface
class Logger:
    def log(self, message: str, level: str = "info") -> None:
        pass

# Bad - too broad
class Utilities:
    def log(self, message):
        pass
    def validate(self, data):
        pass
    def format(self, text):
        pass
```

### Type Hints

```python
# Good - clear types
class UserRepository:
    def get_user(self, user_id: str) -> Optional[User]:
        pass
    def save_user(self, user: User) -> bool:
        pass

# Bad - no type information
class UserRepo:
    def get(user_id):
        pass
    def save(user):
        pass
```

## Example: Payment Processing Interface

```python
from abc import ABC, abstractmethod
from typing import Optional

class PaymentProcessor(ABC):
    """Abstract base class for payment processing"""
    
    @abstractmethod
    def process_payment(self, amount: float, currency: str = "USD") -> bool:
        """
        Process a payment transaction
        
        Args:
            amount: Payment amount
            currency: 3-letter currency code
            
        Returns:
            bool: True if payment succeeded, False otherwise
        """
        pass
    
    @abstractmethod
    def refund_payment(self, transaction_id: str) -> bool:
        """
        Refund a previous payment
        
        Args:
            transaction_id: ID of original transaction
            
        Returns:
            bool: True if refund succeeded, False otherwise
        """
        pass
    
    def get_supported_currencies(self) -> list[str]:
        """Get list of supported currencies"""
        return ["USD", "EUR", "GBP"]

class StripeProcessor(PaymentProcessor):
    def process_payment(self, amount: float, currency: str = "USD") -> bool:
        # Stripe-specific implementation
        return True
    
    def refund_payment(self, transaction_id: str) -> bool:
        # Stripe refund logic
        return True
```

## Documentation

Always include:

1. **Purpose**: What the interface does
2. **Methods**: What each method does
3. **Parameters**: Input types and meanings
4. **Returns**: Output types and meanings
5. **Examples**: Usage examples