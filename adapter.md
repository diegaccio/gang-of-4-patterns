# Adapter Pattern in Python

The **Adapter Pattern** is a structural design pattern that allows incompatible interfaces to work together. It acts as a bridge between two interfaces, enabling classes with different interfaces to collaborate without modifying their code.

## Example of the Adapter Pattern in Python

In this example, let's imagine we have a `EuropeanSocket` that supplies power in 220V, but we have an `AmericanDevice` that only operates on 110V. To allow these two to work together, we’ll create an `Adapter`.

```python

# Existing interface (European socket)
class EuropeanSocket:
    def provide_power(self) -> str:
        return "Power supply at 220V"

# Target interface (American device)
class AmericanDevice:
    def operate_on_110v(self) -> str:
        return "Operating on 110V power"

# Adapter class
class Adapter:
    def __init__(self, socket: EuropeanSocket):
        self.socket = socket

    def convert_and_supply_power(self) -> str:
        # Adapting the voltage to match the American device requirements
        power = self.socket.provide_power()
        return f"{power} converted to 110V for American device."

# Usage
if __name__ == "__main__":
    # European socket (adaptee)
    european_socket = EuropeanSocket()
    
    # Adapter to allow American device to work with European socket
    adapter = Adapter(european_socket)
    
    # Simulate American device using adapted power
    american_device = AmericanDevice()
    print(adapter.convert_and_supply_power())  # Output: "Power supply at 220V converted to 110V for American device."

```

## Output

When you run this code, the output will be:

```
Power supply at 220V converted to 110V for American device.
```

This pattern is useful for integrating incompatible components without changing their underlying code, making systems more modular and flexible.

### Try it yourself

Here’s the working implementation of the Adapter Pattern in [Python](src/adapter.py)