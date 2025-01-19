class Bus:
    def __init__(self, name):
        self.name = name
        self.v=0
    def set_bus(self,v):
        self.v = v

    def __repr__(self):

        return f"Bus(name='{self.name}', voltage={self.v})"

# B1 = Bus("B1")
#
# B1.set_bus(480)
#
# print(B1.__dict__)