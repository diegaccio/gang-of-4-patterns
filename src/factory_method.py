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
