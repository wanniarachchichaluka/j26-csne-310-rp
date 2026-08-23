from pathlib import Path
import py_dss_interface


# ============================================================
# Paths
# ============================================================

PROJECT_ROOT = Path(__file__).resolve().parents[1]
MODEL_FILE = PROJECT_ROOT / "models" / "base_circuit.dss"


# ============================================================
# Start OpenDSS
# ============================================================

dss = py_dss_interface.DSS()

print("=" * 60)
print("OpenDSS Base Circuit Verification")
print("=" * 60)

print(f"Model file: {MODEL_FILE}")

if not MODEL_FILE.exists():
    raise FileNotFoundError(f"Model file not found: {MODEL_FILE}")


# ============================================================
# Compile circuit
# ============================================================

dss.text(f'Compile "{MODEL_FILE}"')


# ============================================================
# Solve
# ============================================================

dss.text("Solve")


# ============================================================
# Verification
# ============================================================

print()
print("Circuit name:", dss.circuit.name)
print("Buses:", dss.circuit.buses_names)
print("Number of buses:", dss.circuit.num_buses)
print("Number of elements:", dss.circuit.num_ckt_elements)
print("Converged:", dss.solution.converged)

print()
print("=" * 60)
print("Verification completed")
print("=" * 60)