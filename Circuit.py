from Bus import Bus
from Resistor import Resistor
from Load import Load
from Vsource import Vsource


class Circuit:
    def __init__(self, name):
        self.name = str(name)
        self.buses = {}
        self.resistors = {}
        self.loads = {}
        self.vsource = {}
        self.i = 0


    def add_bus(self,bus):
        self.buses[bus]=Bus(bus)

    def add_resistor_element(self,name,bus1,bus2,r):
        self.resistors[name] = Resistor(name,bus1,bus2,r)


    def add_load_element(self,name,bus1,p,v):
        self.loads[name] = Load(name,bus1,p,v)

    def add_vsource(self,name,bus1,v):
        self.vsource = Vsource(name,bus1,v)
        self.buses[bus1].v=v



    def set_i(self,i):
        self.i = i

    def print_nodal_voltage(self):
        for key in self.buses:
            print ("{} voltage = {} V".format(key,self.buses[key].v))
        pass
    def print_circuit_current(self):
        print("Circuit current = {} A".format(self.i))




