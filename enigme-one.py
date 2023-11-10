import numpy as np
from qiskit import *
import matplotlib.pyplot as plt
from qiskit.visualization import *

# Gardien G = Gardien de gauche
# Gardien D = Gardien de droite

GUARDIEN_LEFT = 0
GUARDIEN_RIGHT = 1
LIE = 2

# Affichage du circuit quantique
def display():
    circ.draw()
    circ.draw('mpl')
    plt.draw()
    plt.show()

# Inversion des réponses des Gardiens par rapport a la ligne du mensonge
def invert_watchers_answer(circ):
    # Ajout d'une porte CNOT sur le Mensonge par rapport au Gardien D
    circ.cx(LIE, GUARDIEN_RIGHT)
    # Ajout d'une porte NOT sur le Mensonge
    circ.x(LIE)
    # Ajout d'une porte CNOT sur le Mensonge par rapport au Gardien G
    circ.cx(LIE, GUARDIEN_LEFT)
    # Ajout d'une porte NOT sur le Mensonge
    circ.x(LIE)


if __name__ == "__main__":
    # Création du circuit quantique avec 3 qubits (les 2 gardiens et le mensonge)
    circ = QuantumCircuit(3)

    # Ajout d'une porte d'Hadamard sur le Gardien G
    circ.h(GUARDIEN_LEFT)
    # Ajout d'une porte CNOT sur la Gardien G par rapport au Gardien D
    circ.cx(GUARDIEN_LEFT, GUARDIEN_RIGHT)
    # Ajout d'une porte d'Hadamard sur la ligne du mensonge
    circ.h(LIE)

    # Ajout d'une barrière
    circ.barrier()
    # Inversion des réponses des Gardiens par rapport a la ligne du mensonge
    invert_watchers_answer(circ)

    # Ajout d'une barrière
    circ.barrier()
    # Ajout d'une porte de Swap entre les deux Gardiens
    circ.swap(GUARDIEN_LEFT, GUARDIEN_RIGHT)
    # Ajout d'une porte NOT sur les deux Gardiens
    circ.x(GUARDIEN_LEFT)
    circ.x(GUARDIEN_RIGHT)
    # Inversion des réponses des Gardiens par rapport a la ligne du mensonge
    invert_watchers_answer(circ)

    # Mesure des 3 qubits
    circ.measure_all()
    # Affichage du circuit
    display()

