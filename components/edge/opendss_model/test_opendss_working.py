import py_dss_interface

# Initialize OpenDSS
dss = py_dss_interface.DSS()

print("OpenDSS initialized successfully!")

# Clear and create circuit
dss.text("Clear")
dss.text("New Circuit.MyTestCircuit BasekV=0.4 PU=1.0 MVAsc3=100 MVAsc1=100")

# Define buses (no BasekV parameter)
dss.text("New Bus.Bus1")
dss.text("New Bus.Bus2")

# Define line
dss.text("New Line.Line1 Bus1=Bus1 Bus2=Bus2 R1=0.1 X1=0.05")

# Define load (single-phase)
dss.text("New Load.Load1 Bus1=Bus1 Phases=1 Conn=Wye kV=0.23 kW=1.0 pf=0.90")

# Solve
dss.text("Solve")

print("\nPower flow solved successfully!")

# Get number of buses
num_buses = dss.circuit.num_buses
print(f"Number of buses: {num_buses}")

# Get bus names
bus_names = dss.circuit.bus_names
print(f"Bus names: {bus_names}")

# Get voltages using the active bus method
print("\n=== Bus Voltages (pu) ===")
dss.circuit.set_active_bus(0)
v1 = dss.active_bus.pu_vmag
a1 = dss.active_bus.pu_vangle
print(f"Bus1: Voltage = {v1[0]:.4f} pu, Angle = {a1[0]:.4f}°")

dss.circuit.set_active_bus(1)
v2 = dss.active_bus.pu_vmag
a2 = dss.active_bus.pu_vangle
print(f"Bus2: Voltage = {v2[0]:.4f} pu, Angle = {a2[0]:.4f}°")

print("\nOpenDSS test successful!")