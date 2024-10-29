# Singleton Pattern in Python

The **Singleton Pattern** is a creational design pattern that ensures a class has only one instance and provides a global point of access to that instance. This pattern is useful when exactly one instance of a class is needed to coordinate actions across a system.

## Example of the Singleton Pattern in Python

Here's an example implementation of the Singleton Pattern using the `__new__` method.

```python
class Singleton:
    _instance = None  # Class-level attribute to store the singleton instance

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
            # Initialize any other attributes here if needed
        return cls._instance

    def __init__(self):
        # This initialization runs only once due to the way the Singleton is structured.
        self.value = 0

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

# Usage
if __name__ == "__main__":
    # Create the first instance
    singleton1 = Singleton()
    singleton1.set_value(42)
    print("Singleton1 Value:", singleton1.get_value())  # Output: 42

    # Attempt to create a second instance
    singleton2 = Singleton()
    print("Singleton2 Value:", singleton2.get_value())  # Output: 42

    # Check if both variables point to the same instance
    print("Are both instances the same?", singleton1 is singleton2)  # Output: True
```

## Explanation

- **Singleton Class**:
  - `_instance` is a class attribute that stores the single instance of `Singleton`.
  - `__new__` is overridden to control the instantiation of the class. It checks if `_instance` is `None` (i.e., the class hasn’t been instantiated yet) and creates the instance if needed. If `_instance` is already set, it simply returns the existing instance.
  - `__init__` initializes instance attributes. Due to the `__new__` method's control, this only sets values the first time.

- **Usage**:
  - `singleton1` and `singleton2` both refer to the same instance. Any change to `singleton1` (like setting the value) will reflect in `singleton2` because they are the same object.

## Output

The output will be:

```
Singleton1 Value: 42
Singleton2 Value: 42
Are both instances the same? True
```

In this example, the Singleton Pattern ensures that `Singleton` has only one instance, accessible globally across the system.

### Try it yourself

Here’s the working implementation of the Singleton Pattern in [Python](src/singleton.py)
