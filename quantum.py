import os
from qiskit import QuantumCircuit
from qiskit.visualization import plot_histogram
from qiskit.quantum_info import Statevector
import matplotlib.pyplot as plt
import numpy as np

class QuantumExperiments:
    def bell_state_entanglement(self):
        qc = QuantumCircuit(2)
        
        qc.h(0)
        qc.cx(0, 1)
        
        statevector = Statevector.from_instruction(qc)
        
        probabilities = np.abs(statevector.data)**2
        
        current_dir = os.path.dirname(os.path.abspath(__file__))
        
        os.makedirs(current_dir, exist_ok=True)
        
        image_path = os.path.join(current_dir, 'bell_state_results.png')
        
        plt.figure(figsize=(10,6))
        plt.bar(['|00⟩', '|01⟩', '|10⟩', '|11⟩'], probabilities)
        plt.title('Bell State Probability Distribution')
        plt.xlabel('Quantum States')
        plt.ylabel('Probability')
        
        print(f"Saving Bell State diagram to: {image_path}")
        
        plt.savefig(image_path)
        plt.close()
        
        return probabilities
    
    def quantum_superposition(self):
        qc = QuantumCircuit(1)
        
        qc.h(0)
        
        statevector = Statevector.from_instruction(qc)
        
        probabilities = np.abs(statevector.data)**2
        
        current_dir = os.path.dirname(os.path.abspath(__file__))
        
        os.makedirs(current_dir, exist_ok=True)
        
        image_path = os.path.join(current_dir, 'superposition_results.png')
        
        plt.figure(figsize=(10,6))
        plt.bar(['|0⟩', '|1⟩'], probabilities)
        plt.title('Quantum Superposition Probability')
        plt.xlabel('Quantum States')
        plt.ylabel('Probability')
        
        print(f"Saving Superposition diagram to: {image_path}")
        
        plt.savefig(image_path)
        plt.close()
        
        return probabilities

def main():
    quantum_exp = QuantumExperiments()
    
    print("Bell State Entanglement Results:")
    bell_results = quantum_exp.bell_state_entanglement()
    print("Probabilities:", bell_results)
    
    print("\nQuantum Superposition Results:")
    superposition_results = quantum_exp.quantum_superposition()
    print("Probabilities:", superposition_results)

if __name__ == "__main__":
    main()
