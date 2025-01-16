class Resistor:
    def __init__(self, name,bus1,bus2,r):
        self.name = name
        self.bus1 = bus1
        self.bus2 = bus2
        self.r = r

    def calc_g(self):
        self.g = 1/self.r


R1 = Resistor("R1","Bus A","Bus B", 10)

R1.calc_g()

print(R1.__dict__)