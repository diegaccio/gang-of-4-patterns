# The Product
class Computer:
    def __init__(self, cpu: str = "", ram: str = "", storage: str = ""):
        self.cpu = cpu
        self.ram = ram
        self.storage = storage

    def __str__(self) -> str:
        return f"Computer(CPU: {self.cpu}, RAM: {self.ram}, Storage: {self.storage})"

# The Builder interface
class ComputerBuilder:
    def __init__(self):
        self.computer = Computer()

    def set_cpu(self, cpu: str):
        self.computer.cpu = cpu
        return self

    def set_ram(self, ram: str):
        self.computer.ram = ram
        return self

    def set_storage(self, storage: str):
        self.computer.storage = storage
        return self

    def build(self) -> Computer:
        return self.computer

# Director class (optional)
class Director:
    @staticmethod
    def build_gaming_computer(builder: ComputerBuilder) -> Computer:
        return builder.set_cpu("Intel i9").set_ram("32GB").set_storage("1TB SSD").build()

    @staticmethod
    def build_office_computer(builder: ComputerBuilder) -> Computer:
        return builder.set_cpu("Intel i5").set_ram("16GB").set_storage("512GB SSD").build()

# Usage
if __name__ == "__main__":
    builder = ComputerBuilder()

    # Using the Director for preset configurations
    gaming_computer = Director.build_gaming_computer(builder)
    print(gaming_computer)

    # Building a custom configuration directly
    custom_computer = builder.set_cpu("AMD Ryzen 7").set_ram("16GB").set_storage("256GB SSD").build()
    print(custom_computer)