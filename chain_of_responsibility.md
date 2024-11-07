# Chain of Responsibility Pattern

The **Chain of Responsibility Pattern** is a behavioral design pattern that allows a request to be passed along a chain of handlers, where each handler decides whether to process the request or pass it to the next handler. This pattern is useful for handling various requests without hardcoding the handler's responsibilities.

Here’s an example of the Chain of Responsibility Pattern in Python. In this example, we simulate a logging system that handles messages of different levels (info, warning, error). Each handler in the chain only processes messages of its designated level and passes others along.

### Example of the Chain of Responsibility Pattern in Python

```python
from abc import ABC, abstractmethod

# Abstract Handler
class Logger(ABC):
    def __init__(self, next_handler=None):
        self._next_handler = next_handler

    @abstractmethod
    def handle(self, level, message):
        if self._next_handler:
            return self._next_handler.handle(level, message)

# Concrete Handlers
class InfoLogger(Logger):
    def handle(self, level, message):
        if level == "info":
            print(f"[INFO]: {message}")
        else:
            super().handle(level, message)

class WarningLogger(Logger):
    def handle(self, level, message):
        if level == "warning":
            print(f"[WARNING]: {message}")
        else:
            super().handle(level, message)

class ErrorLogger(Logger):
    def handle(self, level, message):
        if level == "error":
            print(f"[ERROR]: {message}")
        else:
            super().handle(level, message)

# Usage
if __name__ == "__main__":
    # Setting up the chain of responsibility
    error_logger = ErrorLogger()
    warning_logger = WarningLogger(error_logger)
    info_logger = InfoLogger(warning_logger)

    # Testing the chain with different log levels
    info_logger.handle("info", "This is an informational message.")
    info_logger.handle("warning", "This is a warning message.")
    info_logger.handle("error", "This is an error message.")
```

### Explanation

1. **Logger (Abstract Handler)**: Defines an interface for handling requests and optionally passes the request to the next handler in the chain.
  
2. **InfoLogger, WarningLogger, ErrorLogger (Concrete Handlers)**: Each of these classes processes specific types of messages. If they cannot handle a particular message, they pass it along to the next handler.

3. **Client Usage**: The client sets up a chain, starting with `InfoLogger`, followed by `WarningLogger`, and ending with `ErrorLogger`. Depending on the log level of each message, it’s processed by the appropriate handler in the chain.

### Output

Running this code produces:

```
[INFO]: This is an informational message.
[WARNING]: This is a warning message.
[ERROR]: This is an error message.
```

### Benefits of the Chain of Responsibility Pattern

- **Decouples Senders and Receivers**: Separates the request sender and the request handlers, allowing handlers to be dynamically assigned or removed.
- **Flexible Processing Structure**: Handlers can be easily reordered, added, or removed without affecting client code.
- **Simplifies Responsibility Assignment**: Each handler only processes the requests it’s concerned with, reducing complex if-else chains.

### Try it yourself

Here’s the working implementation of the Chain of Responsibility  Pattern in [Python](src/chain_of_responsibility.py)
