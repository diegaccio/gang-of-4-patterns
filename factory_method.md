
# Factory Method Pattern

The Factory Method Pattern provides a way to delegate the instantiation of objects to subclasses. This pattern is useful when a superclass defines a common interface for objects it creates, but the exact object type is decided by subclasses.

## Factory Method Pattern Example in Python

In this example, let's imagine we have a logistics system that can handle different types of transport, like trucks and ships.
 
```python
from abc import ABC, abstractmethod

# Product interface
class Transport(ABC):
    @abstractmethod
    def deliver(self) -> str:
        pass

# Concrete Products
class Truck(Transport):
    def deliver(self) -> str:
        return "Delivering by land in a box"

class Ship(Transport):
    def deliver(self) -> str:
        return "Delivering by sea in a container"

# Creator interface
class Logistics(ABC):
    @abstractmethod
    def create_transport(self) -> Transport:
        pass

    def plan_delivery(self) -> str:
        transport = self.create_transport()
        return transport.deliver()

# Concrete Creators
class RoadLogistics(Logistics):
    def create_transport(self) -> Transport:
        return Truck()

class SeaLogistics(Logistics):
    def create_transport(self) -> Transport:
        return Ship()

# Usage
if __name__ == "__main__":
    # Create a Road Logistics and plan a delivery
    logistics = RoadLogistics()
    print(logistics.plan_delivery())  # Output: "Delivering by land in a box"

    # Create a Sea Logistics and plan a delivery
    logistics = SeaLogistics()
    print(logistics.plan_delivery())  # Output: "Delivering by sea in a container"
```

---

## Explanation

- **Product (`Transport`)**: This is an abstract base class with the deliver method that all transport types must implement.
  
- **Concrete Products**: 
  - `Truck` and `Ship` implement the `Transport` interface, each providing their own version of `deliver`.

- **Creator (`Logistics`)**: The abstract `creator` class defines a `create_transport` factory method. It also has a `plan_delivery` method, which uses the `transport` returned by the factory method.

- **Concrete Creators**: 
  - `RoadLogistics` and `SeaLogistics` override `create_transport` to instantiate the appropriate `transport` type (`Truck` or `Ship`).

---

## Output

When you run this code, the output will be:

```
Delivering by land in a box
Delivering by sea in a container
```

This structure lets you easily add new transport types (like `Airplane`) without modifying the existing logistics code.

### Try it yourself

Here’s the working implementation of the Factory Method Pattern in [Python](src/factory_method.py)