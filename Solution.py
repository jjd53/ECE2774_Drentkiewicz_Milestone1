from Circuit import Circuit
from Resistor import Resistor

class Solution:

    def __init__(self, circuit):
        self.circuit = circuit

    def do_power_flow(self):

        gr = self.circuit.resistors["Rab"].calc_g()

        gl = self.circuit.loads["Lb"].calc_g()

        i = self.circuit.buses['bus A'].v / ((1/gr)+(1/gl))

        self.circuit.set_i(i)

        Vb = self.circuit.i / gl

        self.circuit.buses["bus B"].v = Vb

