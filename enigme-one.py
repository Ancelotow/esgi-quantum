import numpy as np
from qiskit import *
import matplotlib.pyplot as plt
from qiskit.visualization import *


# Affichage du circuit quantique
def display():
    circ.draw()
    circ.draw('mpl')
    plt.draw()
    plt.show()


if __name__ == "__main__":
    # Création du circuit quantique avec 2 qubits
    circ = QuantumCircuit(3)

    # Ajout d'une porte d'Hadamard
    circ.h(0)

    # Ajout d'une porte de contrôle
    circ.cx(0, 1)

    # Ajout d'une porte d'Hadamard sur la ligne du mensonge
    circ.h(2)

    circ.barrier()
    circ.cx(2, 1)
    circ.x(2)
    circ.cx(2, 0)
    circ.x(2)

    circ.barrier()
    circ.swap(0, 1)
    circ.x(0)
    circ.x(1)
    circ.cx(2, 1)
    circ.x(2)
    circ.cx(2, 0)
    circ.x(2)

    circ.measure_all()
    display()

