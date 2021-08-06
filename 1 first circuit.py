from qiskit import QuantumCircuit

qc = QuantumCircuit(3, 3) # Create quantum circuit with 3 qubits and 3 classical bits
qc.draw()  # returns a drawing of the circuit

from qiskit import QuantumCircuit
n = 8
n_q = n
n_b = n
qc_output = QuantumCircuit(n_q,n_b)
for j in range(n):
    qc_output.measure(j,j) # measure qubits 0 to n to classical bits 0 to n respectively
qc_output.draw()