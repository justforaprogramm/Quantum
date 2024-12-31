import cirq, qsimcirq
from pprint import pprint

# Define qubits and a short circuit.
q0, q1 = cirq.LineQubit.range(2)
circuit = cirq.Circuit(cirq.H(q0), cirq.CX(q0, q1))

# Simulate the circuit with Cirq and return the full state vector.
cirq_simulator = cirq.Simulator()
cirq_results = cirq_simulator.simulate(circuit)

# Simulate the circuit with qsim and return the full state vector.
qsim_simulator = qsimcirq.QSimSimulator()
qsim_results = qsim_simulator.simulate(circuit)

samples = cirq.sample_state_vector(
    qsim_results.state_vector(), indices=[0, 1], repetitions=10)

print(f'Circuit:\n{circuit}', f'Cirq results:{cirq_results}', f'qsim results:{qsim_results}', 'samples:', sep='\n\n')
pprint(samples)
