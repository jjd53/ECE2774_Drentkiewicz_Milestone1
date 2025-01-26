class Resistor:
    def __init__(self, name,bus1,bus2,r):
        self.name = name
        self.bus1 = bus1
        self.bus2 = bus2
        self.r = r
        self.g = 0
    def calc_g(self):
        return 1/self.r

    def __repr__(self):
        return f"Resistor(name='{self.name}', bus1='{self.bus1}', bus2='{self.bus2}', resistance={self.r})"

