class Load:
    def __init__(self, name,bus1,p,r):
        self.name = name
        self.bus1 = bus1
        self.p = p
        self.r = r

    def calc_g(self):
        self.g = 1/self.r

L1 = Load("L1","Bus A",100,5)

L1.calc_g()

print(L1.__dict__)

