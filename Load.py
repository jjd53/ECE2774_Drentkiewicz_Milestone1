class Load:
    def __init__(self, name,bus1,p,v):
        self.name = name
        self.bus1 = bus1
        self.p = float(p)
        self.v = float(v)

    def calc_g(self):
        return self.p/(self.v)**2

    def __repr__(self):
        return f"Load(name='{self.name}', bus1='{self.bus1}', power={self.p}, voltage={self.v})"



