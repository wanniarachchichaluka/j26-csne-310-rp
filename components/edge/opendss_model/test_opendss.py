import py_dss_interface

# Initialize the OpenDSS engine
dss = py_dss_interface.DSS()

print("OpenDSS initialized successfully.")

# Clear any existing circuit
dss.text("Clear")

# Create a new circuit
dss.text("New Circuit.MyTestCircuit BasekV=0.4 PU=1.0")

# Add buses
dss.text("New Bus.Bus1")
dss.text("New Bus.Bus2")

# Create a line between the buses
dss.text("New Line.Line1 Bus1=Bus1 Bus2=Bus2 R1=0.1 X1=0.05")

# Define a load at Bus1 (single-phase, 1 kW, pf 0.90)
dss.text("New Load.Load1 Bus1=Bus1 Phases=1 Conn=Wye kV=0.23 kW=1.0 pf=0.90")

# Run the power flow
dss.text("Solve")

print("\nPower flow solved successfully!")

# Get number of buses
num_buses = dss.circuit.num_buses
print(f"Number of buses: {num_buses}")

# Get bus names
bus_names = dss.circuit.bus_names
print(f"Bus names: {bus_names}")

# Get voltages using the ActiveBus method
print("\n=== Bus Voltages (pu) ===")
for i in range(num_buses):
    dss.circuit.set_active_bus(i)
    voltage = dss.active_bus.pu_vmag
    angle = dss.active_bus.pu_vangle
    print(f"Bus {i}: Voltage = {voltage[0]:.4f} pu, Angle = {angle[0]:.4f}°")

print("\nOpenDSS test successful!")