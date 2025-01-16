class Load:
    def __init__(self, name,bus1,p,v):
        self.name = name
        self.bus1 = bus1
        self.p = float(p)
        self.v = float(v)

    def calc_g(self):
        self.g = self.p/(self.v)**2

L1 = Load("L1","Bus A",100,5)

L1.calc_g()

print(L1.__dict__)

