# Decorator Pattern

The **Decorator Pattern** is a structural design pattern that allows for dynamically adding new functionalities to an object without modifying its original structure. This pattern is particularly useful in scenarios where we want to enhance the behavior of objects in a flexible and reusable way.

In this example, we implement a simple notification system that can send a basic notification and then be "decorated" to add extra features, like sending notifications via email and SMS.

### Components of the Example

1. **Base Interface**: Defines the method that each notification type must implement.
2. **Concrete Class**: Implements the base notification.
3. **Base Decorator**: A base class that implements the interface and contains a notifier, allowing new functionalities to be added.
4. **Concrete Decorators**: Specific decorators that extend the base decorator to add features, like email and SMS notifications.

### Example Code

Here’s an example implementation of the Decorator Pattern in [Python](decorator.py)


