import cirq

# Anzahl der Qubits für n = 1024
num_qubits = 10  # 2^10 = 1024

# Qubits erstellen
qubits = [cirq.LineQubit(i) for i in range(num_qubits)]

# Schaltkreis erstellen
circuit = cirq.Circuit()

# Schritt 1: Alle Qubits in Superposition bringen (repräsentieren n = 0 bis 63)
for qubit in qubits:
    circuit.append(cirq.H(qubit))

# Schritt 2: Phasenkodierung für 2^n
for i, qubit in enumerate(qubits):
    # Jede Potenz 2^i wird durch eine Phasendrehung kodiert
    circuit.append(cirq.ZPowGate(exponent=2**i)(qubit))

# Schritt 3: Messung
circuit.append(cirq.measure(*qubits, key="result"))

# Simulator initialisieren
simulator = cirq.Simulator()

# Schaltkreis simulieren
result = simulator.run(circuit, repetitions=1000)

# Ergebnisse sammeln
counts = result.histogram(key="result")

# Speichern der Ergebnisse in einem Dictionary
data = {}
for value, count in counts.items():
    data[value] = {
        "2^n": 2**value,
        "count": count
    }

# Sortiere nach n-Werten
sorted_data = dict(sorted(data.items()))

# Ausgabe der sortierten Ergebnisse
print("Messresultate (2^n Werte) nach n sortiert:")
for n, info in sorted_data.items():
    print(f"n={n}, 2^{n} = {info['2^n']}, count={info['count']}")
