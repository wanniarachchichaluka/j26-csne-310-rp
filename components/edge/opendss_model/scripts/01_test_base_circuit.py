import py_dss_interface
from pathlib import Path


# ---------------------------------------------------------
# Project paths
# ---------------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parents[1]
MODEL_FILE = PROJECT_ROOT / "models" / "base_circuit.dss"


# ---------------------------------------------------------
# Start OpenDSS
# ---------------------------------------------------------

dss = py_dss_interface.DSS()

print("OpenDSS engine initialized.")


# ---------------------------------------------------------
# Load the circuit
# ---------------------------------------------------------

dss.text(f'Compile "{MODEL_FILE}"')

print(f"Circuit loaded from: {MODEL_FILE}")


# ---------------------------------------------------------
# Solve
# ---------------------------------------------------------

dss.text("Solve")


# ---------------------------------------------------------
# Check convergence
# ---------------------------------------------------------

converged = dss.solution.converged

print(f"Solution converged: {converged}")


# ---------------------------------------------------------
# Basic circuit information
# ---------------------------------------------------------

print(f"Number of buses: {dss.circuit.num_buses}")
print(f"Number of elements: {dss.circuit.num_ckt_elements}")

print("Base circuit test completed.")