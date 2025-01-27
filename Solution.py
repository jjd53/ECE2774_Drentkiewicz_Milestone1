#Creation of the Solution class
#This class takes in a circuit as a sub-class in order to use values of all
#circuit element values to be used in calculations
class Solution:

    def __init__(self, circuit):
        self.circuit = circuit

    #This method obtains conductance values for the resistor and the load,
    #calculates and sets the current in the circuit nad calculates and sets the voltage
    #at bus B
    def do_power_flow(self):

        gr = self.circuit.resistors["Rab"].calc_g()

        gl = self.circuit.loads["Lb"].calc_g()

        i = self.circuit.buses['bus A'].v / ((1/gr)+(1/gl))

        self.circuit.set_i(i)

        Vb = self.circuit.i / gl

        self.circuit.buses["bus B"].v = Vb

