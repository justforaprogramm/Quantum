import cirq

# Define qubit
q0 = cirq.LineQubit(0)

# Schaltkreis definieren
circuit = cirq.Circuit(
    cirq.H(q0),                # Hadamard-Gatter auf qubit1 => 1/(2^1/2)(|0> + |1>)
    cirq.measure(q0, key='result')  # Messung 
)

# Simulator initialisieren
simulator = cirq.Simulator()

# Schaltkreis simulieren
result = simulator.run(circuit, repetitions=1)

# Ergebnisse anzeigen
print('Messresultate:')
print(result.histogram(key='result'))
