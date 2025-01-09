# Quantencomputer
# Leitfrage: Was ist ein Quantencomputer

## einfach bleiben
+ qubit
    + was ist ein qubit
        + bloch sphere
    + unterschied zu bit
    + physikalischer hintergrund
        + superposition
        + verschrenkung
        + Inteferenz
+ unterschiede zu klassischen computer
    + computer herkömmlich CPU und GPU
    + neuerdigs auch TPU (Tensor Prozessing Unit) für KI
    + bei Quantencomputern QPU (Quantum Prozessing Unit)
+ nutztungsweisen
    + kann nicht mehr als herkömmlicher computer, aber so manches schneller
    + ist exponentiel schneller
## ohne einfach
+ zwei arten von benutztungen
    + annealing
    + gatter
+ unterschiede zu klassischen computer
    + functiuniert durch die qubits und anderen gatter grundsätztlich anderss
+ qubit
    + superconducting qubits
    + trapped ion qubits
    + quatum dots
    + photons
    + neutral atoms
+ nutztungsweisen
    + vermutung vorab große wahrscheinlichkeit nutzung als co prozessor
    + heute bis ~5 jahre
        + zufallszahlen
        + maschinelles lernen /K
    + ~5 bis ~20 jahre
        + kryptographie
        + gesundheitswesen
        + wetter und klima
        + verkehr und autonomes fahren
    + 20+
        + matrialien erforschen  durch teilchensimulation
        + energiequellen neu und weiterentwickeln
        + forschung quantenphysik
        + Superinteligenz
        + cybersecurity -> überleitung zu shor algorhythmus

## programmieren
+ probleme beim googlen
    + viel wird einfach erklärt tief in die materie kommt man nur schwer
+ probleme beim coden
    + linux ist besser weil auf windows hats nicht getan
    + wie habe ichs dann gemacht
        + googles python integration cirq genutzt
        + mit der simulation simcirq oder direkt die simulationsklasse angesteuert der einfach halt
    + entscheidung language
+ qubit beim coden
    + ```cirq.LineQubit(x:int)```
+ gates
    + Pauli-X
    + Pauli-Y
    + Pauli-Z
    + Hadamard
    + (Messung) -> direkter bezug zu quantenphysik göttingen
+ algorhythmen
    + shor
    + grover
    + qft
    + vqe
    + qaoa
    + amplitude amplification
    + hhl
    + qpe
    + deutsch jozsa
    + boson sampling
+ easy code
    + random zahlen (theorie)
    + algorhythmen in der anwendung (auch spontan möglich aber eher nicht gewollt)
## Fazit
+ ein quantencomputer ist eine rechenmaschine wie ein klassischer computer, er nutzt allerdings physikalische eigenschafften der quantenmechanik um sehr schnell rechnen zu können.
## Quellen
+ www.<b>ibm</b>.com/think/topics/quantum-computing
+ www.<b>all-electronics</b>.de/elektronik-entwicklung/quantencomputer/diese-arten-von-quantencomputern-gibt-es-760.html
+ www.<b>datacenter-insider</b>.de/was-ist-quanten-annealing-a-782266/
+ <b>qmunity</b>.thequantuminsider.com/2024/06/11/introduction-to-cirq/
+ en.<b>wikipedia</b>.org/wiki/Tensor_Processing_Unit
+ de.<b>wikipedia</b>.org/wiki/Polynomialzeit
+ www.<b>weltderphysik</b>.de/gebiet/technik/quantenmechanik-quantentechnik/einfuehrung-quantencomputer/
+ www.<b>btechnologyreview</b>.com/2019/01/29/66141/what-is-quantum-computing/
+ <b>github</b>.com/quantumlib/qsim/tree/v0.21.0
+ <b>github</b>.com/quantumlib/qsim/blob/v0.21.0/qsimcirq/qsim_simulator.py#L123-L838

+ https://www.youtube.com/watch?v=90za6mazNps
+ https://www.youtube.com/watch?v=-UlxHPIEVqA ****
+ https://www.youtube.com/watch?v=8K0VAdo2wdg
