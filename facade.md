# Facade Pattern

The **Facade Pattern** is a structural design pattern that provides a simplified interface to a complex subsystem, making it easier to interact with the subsystem by hiding its complexity. This pattern is useful when you want to simplify client interactions with complex libraries or multiple classes.

### Example of the Facade Pattern in Python

In this example, we’ll create a `ComputerFacade` class that simplifies the process of starting up a computer. The computer consists of multiple subsystems: CPU, Memory, and HardDrive.

```python
# Subsystem class - CPU
class CPU:
    def freeze(self):
        return "CPU: Freezing processor."

    def jump(self, position):
        return f"CPU: Jumping to start position {position}."

    def execute(self):
        return "CPU: Executing instructions."

# Subsystem class - Memory
class Memory:
    def load(self, position, data):
        return f"Memory: Loading {data} to position {position}."

# Subsystem class - HardDrive
class HardDrive:
    def read(self, lba, size):
        return f"HardDrive: Reading {size} bytes from LBA {lba}."

# Facade class - ComputerFacade
class ComputerFacade:
    def __init__(self):
        self.cpu = CPU()
        self.memory = Memory()
        self.hard_drive = HardDrive()

    def start_computer(self):
        startup_sequence = [
            self.cpu.freeze(),
            self.memory.load(0, "bootloader"),
            self.cpu.jump(0),
            self.hard_drive.read(0, 1024),
            self.cpu.execute()
        ]
        return "\n".join(startup_sequence)

# Usage
if __name__ == "__main__":
    computer = ComputerFacade()
    print(computer.start_computer())
```

### Explanation

1. **Subsystem Classes (CPU, Memory, HardDrive)**: These classes represent the components of a computer system with complex interactions. Each provides specific functionality.

2. **ComputerFacade (Facade)**: This class provides a simple interface to start the computer. It uses the subsystem classes (`CPU`, `Memory`, and `HardDrive`) to perform a series of operations, abstracting away the complexities of starting a computer.

3. **start_computer() Method**: This method in `ComputerFacade` initiates a sequence of subsystem operations, hiding the details from the client.

### Output

When you run this code, it outputs:

```
CPU: Freezing processor.
Memory: Loading bootloader to position 0.
CPU: Jumping to start position 0.
HardDrive: Reading 1024 bytes from LBA 0.
CPU: Executing instructions.
```

### Benefits of the Facade Pattern

- **Simplified Interface**: Provides a high-level interface that makes the subsystem easier to use.
- **Loose Coupling**: Reduces dependency on specific subsystem classes, promoting flexibility and modularity.
- **Ease of Maintenance**: Modifications to subsystem classes don’t directly affect client code, as long as the facade's interface remains consistent.

### Try it yourself

Here’s the working implementation of the Facade Pattern in [Python](src/facade.py)