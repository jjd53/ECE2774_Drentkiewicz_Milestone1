from Bus import Bus
class Vsource:
    def __init__(self, name,bus1,v):
        self.name = name
        self.bus1 = bus1
        self.v = v




    def __repr__(self):
        return f"Vsource(name='{self.name}', bus1='{self.bus1}', voltage={self.v})"


