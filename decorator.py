from abc import ABC, abstractmethod

# Base interface
class Notifier(ABC):
    @abstractmethod
    def send_notification(self, message: str):
        pass

# Concrete class
class BasicNotifier(Notifier):
    def send_notification(self, message: str):
        print(f"Basic Notification: {message}")

# Base decorator
class NotifierDecorator(Notifier):
    def __init__(self, notifier: Notifier):
        self._notifier = notifier

    def send_notification(self, message: str):
        self._notifier.send_notification(message)

# Concrete decorator for email
class EmailNotifier(NotifierDecorator):
    def send_notification(self, message: str):
        super().send_notification(message)
        print(f"Email Notification: {message}")

# Concrete decorator for SMS
class SMSNotifier(NotifierDecorator):
    def send_notification(self, message: str):
        super().send_notification(message)
        print(f"SMS Notification: {message}")

# Usage example
if __name__ == "__main__":
    # Create a basic notification and decorate it with email and SMS notifications
    notifier = EmailNotifier(SMSNotifier(BasicNotifier()))
    notifier.send_notification("This is an important notification!")
