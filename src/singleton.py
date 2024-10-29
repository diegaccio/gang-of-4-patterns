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
