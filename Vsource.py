#Creation of the Vsource class
#Class takes name, bus1, and v attributes
#The attributes represent a name, bus1 is the node connection, and v is the
# voltage of the source in volts
class Vsource:
    def __init__(self, name,bus1,v):
        self.name = name
        self.bus1 = bus1
        self.v = v

    # This code helped with testing and troubleshooting
    # Does not affect output
    def __repr__(self):
        return f"Vsource(name='{self.name}', bus1='{self.bus1}', voltage={self.v})"


