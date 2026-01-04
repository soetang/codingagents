# Design Patterns Guide

## Common Patterns

### Strategy Pattern

**Use when**: You need different algorithms for the same task

```python
from abc import ABC, abstractmethod

class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount: float) -> bool:
        pass

class CreditCardStrategy(PaymentStrategy):
    def pay(self, amount: float) -> bool:
        # Credit card payment logic
        return True

class PayPalStrategy(PaymentStrategy):
    def pay(self, amount: float) -> bool:
        # PayPal payment logic
        return True
```

### Factory Pattern

**Use when**: Object creation logic should be centralized

```python
class ReportFactory:
    @staticmethod
    def create_report(report_type: str):
        if report_type == "PDF":
            return PDFReport()
        elif report_type == "Excel":
            return ExcelReport()
        else:
            raise ValueError("Unknown report type")
```

### Observer Pattern

**Use when**: Objects need to notify others about state changes

```python
class Subject:
    def __init__(self):
        self._observers = []
    
    def attach(self, observer):
        self._observers.append(observer)
    
    def notify(self, message):
        for observer in self._observers:
            observer.update(message)

class Logger:
    def update(self, message):
        print(f"LOG: {message}")
```

## When to Use Patterns

1. **Strategy**: Multiple algorithms for same interface
2. **Factory**: Complex object creation
3. **Observer**: Event-driven systems
4. **Decorator**: Adding responsibilities dynamically
5. **Singleton**: Single instance control

## Best Practices

1. **Don't over-engineer**: Use patterns only when they solve real problems
2. **Keep interfaces simple**: Focus on clear, minimal interfaces
3. **Document patterns**: Explain why a pattern was chosen
4. **Consider alternatives**: Sometimes simple solutions are better