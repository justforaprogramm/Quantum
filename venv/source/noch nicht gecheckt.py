import cirq

# Qubits erstellen
qubit1 = cirq.LineQubit(0)
qubit2 = cirq.LineQubit(1)

# Schaltkreis definieren
circuit = cirq.Circuit(
    cirq.H(qubit1),                # Hadamard-Gatter auf qubit1
    cirq.CNOT(qubit1, qubit2),     # CNOT, verschränkt die beiden Qubits
    cirq.measure(qubit1, qubit2, key='result')  # Messung mit dem Schlüssel "result"
)

# Simulator initialisieren
simulator = cirq.Simulator()

# Schaltkreis simulieren
result = simulator.run(circuit, repetitions=1000)

# Ergebnisse anzeigen
print('Messresultate:')
print(result.histogram(key='result'))
