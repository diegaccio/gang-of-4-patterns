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
