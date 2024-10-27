
# Builder Pattern in Python

The Builder Pattern is a creational design pattern that allows you to construct complex objects step-by-step. It provides a way to construct objects with multiple configuration options without having to pass all options at once or write a large constructor.

This pattern is particularly useful for creating objects with many attributes or when object creation requires several steps.

## Example: Builder Pattern in Python

Suppose we want to build a computer with customizable components, such as CPU, RAM, and storage.

```python
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
```

---

## Explanation

- **Product (`Computer`)**: The class we want to create using the builder pattern. It has attributes for CPU, RAM, and storage.
  
- **Builder (`ComputerBuilder`)**: The builder class provides a step-by-step way to set each attribute (CPU, RAM, and storage) of the `Computer` object.

- **Director**: This optional class defines specific configurations, like a gaming computer or an office computer, using the builder methods.

---

## Output

When running the example code, the output will be:

```
Computer(CPU: Intel i9, RAM: 32GB, Storage: 1TB SSD)
Computer(CPU: AMD Ryzen 7, RAM: 16GB, Storage: 256GB SSD)
```

With the Builder Pattern, you can easily customize object creation without needing a large constructor or numerous configuration parameters.