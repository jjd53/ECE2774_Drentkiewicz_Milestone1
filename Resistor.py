#Creation of the Resistor class
#Class takes name, bus1, bus2 and r attributes and initializes a conductance attribute called 'g'
#The attributes represent a name, bus1 is the first node connection, bus2 is the second node connection,
#and r is the resistance in ohms
class Resistor:
    def __init__(self, name,bus1,bus2,r):
        self.name = name
        self.bus1 = bus1
        self.bus2 = bus2
        self.r = r
        self.g = 0

    #This method calculates and returns the conductance value of a resistor object
    def calc_g(self):
        return 1/self.r

    # This code helped with testing and troubleshooting
    # Does not affect output
    def __repr__(self):
        return f"Resistor(name='{self.name}', bus1='{self.bus1}', bus2='{self.bus2}', resistance={self.r})"

