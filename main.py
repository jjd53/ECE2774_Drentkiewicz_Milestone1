#Imports classes to have access to methods in those classes
from Circuit import Circuit
from Solution import Solution

#Creates a circuit object and adds all circuit elements
circuit = Circuit("circuit")
circuit.add_bus("bus A")
circuit.add_bus("bus B")
circuit.add_resistor_element("Rab","bus A","bus B",15)
circuit.add_load_element("Lb","bus B",2000,250)
circuit.add_vsource("Va","bus A",250)

#Creates the Solution object
answer = Solution(circuit)

#Calls method to compute circuit values
#and prints circuit current and voltages
answer.do_power_flow()
print("Example Circuit:")
circuit.print_nodal_voltage()
circuit.print_circuit_current()

