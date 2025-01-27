#Creation of the Load class
#Class takes name, bus1, p and v attributes which represent a name,
#bus1 is the node connection, p is the load's rated power in watts,
#and v is the load's rated voltage in volts
class Load:
    def __init__(self, name,bus1,p,v):
        self.name = name
        self.bus1 = bus1
        self.p = float(p)
        self.v = float(v)

    #This method calculates and returns the load's conductance value
    def calc_g(self):
        return self.p/(self.v)**2

    # This code helped with testing and troubleshooting
    # Does not affect output
    def __repr__(self):
        return f"Load(name='{self.name}', bus1='{self.bus1}', power={self.p}, voltage={self.v})"



