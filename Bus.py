#Creation of the Bus class
#Classs takes a name attribute and initializes a voltage attribute called 'v'
class Bus:
    def __init__(self, name):
        self.name = name
        self.v=0

    #Set bus method assigns a voltage value to the bus attribute 'v'
    def set_bus(self,v):
        self.v = v

    #This code helped with testing and troubleshooting
    #Does not affect output
    def __repr__(self):

        return f"Bus(name='{self.name}', voltage={self.v})"


