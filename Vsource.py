class Vsource:
    def __init__(self, name,bus1,v):
        self.name = name
        self.bus1 = bus1
        self.v = v


V1 = Vsource("V1","Bus A",480 )

print(V1.__dict__)

