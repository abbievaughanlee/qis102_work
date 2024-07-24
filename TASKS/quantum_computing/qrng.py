# quantum random number generator
import qiskit
from qiskit import QuantumCircuit, QuantumRegister
from qiskit_ibm_runtime import QiskitRuntimeService, Sampler


# create a quantum bit in superposition and a classical bit
# measure the quantum bit -> random number generator
def set_qubits(n: int):
    global QuantumCircuit
    qr = QuantumRegister(n)  # quantum register of size n
    cr = qiskit.ClassicalRegister(n)  # creates classical register of same size n
    circuit = QuantumCircuit(qr, cr) # creates a quantum circuit out of the quantum and the classical registers
    circuit.h(qr) # apply a hadamard gate on the quantum register
    circuit.measure(qr, cr) # measure the circuit -> qubits collapse

# Set the backend provider with the given account token
service = QiskitRuntimeService(
    channel="ibm_quantum",
    token="3b08a8b84bec6881856e5a0efd5efa67054ce394159425dd6b405ee0689caaa2b3259562b01b01feaa458be0f01ec4357d0337c6c10e5d89ad2caef180581d55",
)
backend = service.backend("ibmq_osaka")  # note: backend doesn't have to be ibm_osaka
set_qubits(1) # call function and set number of qubits
job = Sampler(backend).run(circuit)
result = job.result()
print(result)