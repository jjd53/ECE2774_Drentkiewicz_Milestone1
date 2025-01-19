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

    def add_bus(self,bus):
        self.buses[bus]=Bus(bus)

    def add_resistor_element(self,name,bus1,bus2,r):
        self.resistors[name] = Resistor(name,bus1,bus2,r)

    def add_load_element(self,name,bus1,p,v):
        self.loads[name] = Load(name,bus1,p,v)

    def add_vsource(self,name,bus1,v):
        self.vsource = Vsource(name,bus1,v)


    def set_i(self,i):
        self.i = i

    def print_nodal_voltage(self):
        #for key in self.buses:
            #print (Bus.v)
        pass
    def print_circuit_current(self):
        print(self.i)


circuit = Circuit("circuit")
B1=circuit.add_bus("bus A")
B2=circuit.add_bus("bus B")
R1=circuit.add_resistor_element("R1","bus A","bus B",10)
Z=circuit.add_load_element("Load","bus B",100,5)
V1=circuit.add_vsource("V1","bus A",100)
print(circuit.__dict__)
