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