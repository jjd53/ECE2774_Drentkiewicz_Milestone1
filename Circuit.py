#Imports all object classes and methods to be used in the Circuit class
from Bus import Bus
from Resistor import Resistor
from Load import Load
from Vsource import Vsource

#Creation of the Circuit class
#Class takes in a name, inherits all data from circuit element object classes
#and initializes a circuit current variable, 'i', in amps
class Circuit:
    def __init__(self, name):
        self.name = str(name)
        self.buses = {}
        self.resistors = {}
        self.loads = {}
        self.vsource = {}
        self.i = 0

    #This method creates a circuit object using the Bus class as a sub-class
    def add_bus(self,bus):
        self.buses[bus]=Bus(bus)

    #This method creates a circuit object using the Resistor class as a sub-class
    def add_resistor_element(self,name,bus1,bus2,r):
        self.resistors[name] = Resistor(name,bus1,bus2,r)

    #This method creates a circuit object using the Load class as a sub-class
    def add_load_element(self,name,bus1,p,v):
        self.loads[name] = Load(name,bus1,p,v)

    #This method creates a circuit object using the Vsource class as a sub-class
    #It also sets whatever bus it is conneccted to have the same voltage value
    def add_vsource(self,name,bus1,v):
        self.vsource = Vsource(name,bus1,v)
        self.buses[bus1].v=v

    #This method sets a value for the circuit object's current variable
    def set_i(self,i):
        self.i = i

    #This method simply prints the values of all bus voltages in the circuit
    def print_nodal_voltage(self):
        for key in self.buses:
            print ("{} voltage = {} V".format(key,self.buses[key].v))
        pass

    # This method simply prints the value of the current in the circuit
    def print_circuit_current(self):
        print("Circuit current = {} A".format(self.i))




