from Circuit import Circuit
from Solution import Solution

circuit = Circuit("circuit")
bus_a=circuit.add_bus("bus A")
bus_b=circuit.add_bus("bus B")
Rab=circuit.add_resistor_element("Rab","bus A","bus B",5)
Lb=circuit.add_load_element("Lb","bus B",2000,100)
Va=circuit.add_vsource("Va","bus A",100)
print(circuit.__dict__)