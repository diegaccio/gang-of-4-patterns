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