class Bus:
    def __init__(self, name):
        self.name = name

    def set_bus(self,v):
        self.v = v

B1 = Bus("B1")

B1.set_bus(480)

print(B1.__dict__)