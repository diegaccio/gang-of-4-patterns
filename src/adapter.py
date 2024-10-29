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
