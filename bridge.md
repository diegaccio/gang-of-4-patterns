# Bridge Pattern

The **Bridge Pattern** is a structural design pattern that separates an abstraction from its implementation, allowing the two to vary independently. This is useful for creating systems where you want to change the implementation without modifying the code that depends on the abstraction.

## Example of the Bridge Pattern in Python

In this example, we’ll create a simple scenario where we have a `RemoteControl` as an abstraction and various types of `TV` implementations.

```python
# Implementor interface
class TV:
    def turn_on(self):
        pass
    
    def turn_off(self):
        pass

# Concrete Implementor A
class SamsungTV(TV):
    def turn_on(self):
        return "Samsung TV is now ON."

    def turn_off(self):
        return "Samsung TV is now OFF."

# Concrete Implementor B
class LGTV(TV):
    def turn_on(self):
        return "LG TV is now ON."

    def turn_off(self):
        return "LG TV is now OFF."

# Abstraction
class RemoteControl:
    def __init__(self, tv: TV):
        self.tv = tv

    def power_on(self):
        return self.tv.turn_on()

    def power_off(self):
        return self.tv.turn_off()

# Usage
if __name__ == "__main__":
    # Using Samsung TV
    samsung_tv = SamsungTV()
    remote_samsung = RemoteControl(samsung_tv)
    print(remote_samsung.power_on())   # Output: "Samsung TV is now ON."
    print(remote_samsung.power_off())  # Output: "Samsung TV is now OFF."

    # Using LG TV
    lg_tv = LGTV()
    remote_lg = RemoteControl(lg_tv)
    print(remote_lg.power_on())         # Output: "LG TV is now ON."
    print(remote_lg.power_off())        # Output: "LG TV is now OFF."
```

## Output

When you run this code, the output will be:

```
Power supply at 220V converted to 110V for American device.
```

This pattern is useful for integrating incompatible components without changing their underlying code, making systems more modular and flexible.

### Try it yourself

Here’s the working implementation of the Adapter Pattern in [Python](src/adapter.py)