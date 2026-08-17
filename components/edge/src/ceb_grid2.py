import pandapower as pp

# initializing the network
net = pp.create_empty_network(name="CEB_Power_grid", f_hz=50.0, sn_mva=1, add_stdtypes=True)

# HV External Grid Bus
b1 = pp.create_bus(
    net,
    vn_kv=11.0,
    name="HV External Grid Bus",
    index=0,
    type="b",
    zone="CEB_MV_Region",
    in_service=True,
    max_vm_pu=1.06,
    min_vm_pu=0.94,
    geodata=(6.9271, 79.8612)
)

pp.create_ext_grid(
    net,
    bus=b1,
    vm_pu=1.0,
    va_degree=0.0,
    name="CEB External 11kV Grid connection",
    in_service=True,
    s_sc_max_mva=238.1,
    s_sc_min_mva=190.0,
    rx_max=1.0,
    rx_min=0.4,
    max_p_mw=0.16,
    min_p_mw=-0.16,
    max_q_mvar=0.077,
    min_q_mvar=-0.077,
    index=None,
    r0x0_max=1.0,
    x0x_max=1.0,
    slack_weight=1.0,
    controllable=False
)

# LV Substation Bus bar
b2 = pp.create_bus(
    net,
    vn_kv=0.4,
    name="LV Substation Bus bar",
    index=1,
    type="b",
    zone="CEB_LV_Substation_Region",
    in_service=True,
    max_vm_pu=1.06,
    min_vm_pu=0.94,
    geodata=(6.9272, 79.8613)
)

# Custom Transformer (160 kVA, 11kV/0.4kV) – CEB 098:2023
pp.create_transformer_from_parameters(
    net,
    hv_bus=b1,
    lv_bus=b2,
    sn_mva=0.160,
    vn_hv_kv=11.0,
    vn_lv_kv=0.4,
    vkr_percent=1.65625,
    vk_percent=4.0,
    pfe_kw=0.360,
    i0_percent=0.5,
    shift_degree=0.0,
    in_service=True,
    name="CEB 160kVA 11/0.4kV Transformer",
    vector_group="Dyn11",
    index=None,
    max_loading_percent=100.0,
    parallel=1,
    df=1.0,
)

# Pole 1 - first LV ABC feeder pole after transformer
b3 = pp.create_bus(
    net,
    vn_kv=0.4,
    name="Pole 1 - (LV feeder Node)",
    index=2,
    type="n",
    zone="CEB_LV_feeder_01",
    in_service=True,
    max_vm_pu=1.06,
    min_vm_pu=0.94,
    geodata=(6.9276, 79.8617)
)

# Defining a custom LV line type for CEB 0.4 kV ABC/AAC
std_types_ceb_lv_04kv = {
    "r_ohm_per_km": 0.443,
    "x_ohm_per_km": 0.088,
    "c_nf_per_km": 220,
    "g_us_per_km": 0.0,
    "max_i_ka": 0.175,
    "r_theta_kelvin_per_mw": 0.0,
    "alpha": 0.004,
    "type": "ol",
    "q_mm2": 70.0,
    "conductor_outer_diameter_m": 0.0142,
    "emissivity": 0.9,
    "solar_absorptivity": 0.9
}

pp.create_std_type(
    net,
    name="CEB_LV_ABC_3x70_54",
    data=std_types_ceb_lv_04kv,
    element="line"
)

line_b2_b3 = pp.create_line(
    net,
    from_bus=b2,
    to_bus=b3,
    length_km=0.045,
    std_type="CEB_LV_ABC_3x70_54",
    name="LV_Feeder_SSN_to_House1",
    in_service=True,
    df=1.0,
    parallel=1,
    max_loading_percent=100.0,
    alpha=0.004,
    temperature_degree_celsius=80.0,
    geodata=[
        (6.9272, 79.8613),
        (6.9276, 79.8617)
    ]
)

# Pole 2 - second LV ABC feeder pole (45-50m)
b4 = pp.create_bus(
    net,
    vn_kv=0.4,
    name="Pole 2 (LV Feeder Node)",
    index=3,
    type="n",
    zone="CEB_LV_Feeder_01",
    in_service=True,
    max_vm_pu=1.06,
    min_vm_pu=0.94,
    geodata=(6.9274, 79.8615)
)

# Pole 3 - second LV ABC feeder pole (45-50m)
b5 = pp.create_bus(
    net,
    vn_kv=0.4,
    name="Pole 3 (LV Feeder End)",
    index=4,
    type="n",
    zone="CEB_LV_Feeder_01",
    in_service=True,
    max_vm_pu=1.06,
    min_vm_pu=0.94,
    geodata=(6.9280, 79.8621)
)

# Main LV feeder: Pole 1 to Pole 2 (~45m)
line_b3_b4 = pp.create_line(
    net,
    from_bus=b3,
    to_bus=b4,
    length_km=0.045,
    std_type="CEB_LV_ABC_3x70_54",
    name="LV_Feeder_Pole1_to_Pole2",
    in_service=True,
    df=1.0,
    parallel=1,
    max_loading_percent=100.0,
    alpha=0.004,
    temperature_degree_celsius=80.0,
    geodata=[
        (6.9276, 79.8617),
        (6.9274, 79.8615)
    ]
)

# Main LV feeder: Pole 1 to Pole 2 (~45m)
line_b4_b5 = pp.create_line(
    net,
    from_bus=b4,
    to_bus=b5,
    length_km=0.045,
    std_type="CEB_LV_ABC_3x70_54",
    name="LV_Feeder_Pole2_to_Pole3",
    in_service=True,
    df=1.0,
    parallel=1,
    max_loading_percent=100.0,
    alpha=0.004,
    temperature_degree_celsius=80.0,
    geodata=[
        (6.9274, 79.8615),
        (6.9280, 79.8621)
    ]
)

# House 1 (No Solar) - connected to Pole 1
b_house1 = pp.create_bus(
    net,
    vn_kv=0.4,
    name="House 1 (No Solar)",
    index=5,
    type="n",
    zone="CEB_LV_Feeder_01",
    in_service=True,
    max_vm_pu=1.06,
    min_vm_pu=0.94,
    geodata=(6.9277, 79.8618)
)

# House 2 (Solar 10 kW) - connected to Pole 1
b_house2 = pp.create_bus(
    net,
    vn_kv=0.4,
    name="House 2 (Solar 10 kW)",
    index=6,
    type="n",
    zone="CEB_LV_Feeder_01",
    in_service=True,
    max_vm_pu=1.06,
    min_vm_pu=0.94,
    geodata=(6.9275, 79.8616)
)

# House 3 (No Solar) - connected to Pole 2
b_house3 = pp.create_bus(
    net,
    vn_kv=0.4,
    name="House 3 (No Solar)",
    index=7,
    type="n",
    zone="CEB_LV_Feeder_01",
    in_service=True,
    max_vm_pu=1.06,
    min_vm_pu=0.94,
    geodata=(6.9273, 79.8614)
)

# House 4 (Solar 10 kW) - connected to Pole 2
b_house4 = pp.create_bus(
    net,
    vn_kv=0.4,
    name="House 4 (Solar 10 kW)",
    index=8,
    type="n",
    zone="CEB_LV_Feeder_01",
    in_service=True,
    max_vm_pu=1.06,
    min_vm_pu=0.94,
    geodata=(6.9276, 79.8617)
)

# House 5 (Solar 10 kW) - connected to Pole 2
b_house5 = pp.create_bus(
    net,
    vn_kv=0.4,
    name="House 5 (Solar 10 kW)",
    index=9,
    type="n",
    zone="CEB_LV_Feeder_01",
    in_service=True,
    max_vm_pu=1.06,
    min_vm_pu=0.94,
    geodata=(6.9278, 79.8619)
)

# House 6 (No Solar) - connected to Pole 3
b_house6 = pp.create_bus(
    net,
    vn_kv=0.4,
    name="House 6 (No Solar)",
    index=10,
    type="n",
    zone="CEB_LV_Feeder_01",
    in_service=True,
    max_vm_pu=1.06,
    min_vm_pu=0.94,
    geodata=(6.9279, 79.8620)
)

# House 7 (Solar 10 kW) - connected to Pole 3 (feeder end)
b_house7 = pp.create_bus(
    net,
    vn_kv=0.4,
    name="House 7 (Solar 10 kW - Feeder End)",
    index=11,
    type="n",
    zone="CEB_LV_Feeder_01",
    in_service=True,
    max_vm_pu=1.06,
    min_vm_pu=0.94,
    geodata=(6.9281, 79.8622)
)

# Custom service-drop line type for CEB 0.4 kV household connections
std_type_ceb_service_drop = {
    "r_ohm_per_km": 1.9,
    "x_ohm_per_km": 0.09,
    "c_nf_per_km": 150.0,
    "g_us_per_km": 0.0,
    "max_i_ka": 0.08,
    "r_theta_kelvin_per_mw": 0.0,
    "alpha": 0.004,
    "type": "ol",
    "q_mm2": 16.0,
    "conductor_outer_diameter_m": 0.010,
    "emissivity": 0.9,
    "solar_absorptivity": 0.9
}

pp.create_std_type(
    net,
    name="CEB_LV_Service_Drop_16mm2",
    data=std_type_ceb_service_drop,
    element="line"
)

# Pole 1 to House 1 (No Solar)
line_pole1_house1 = pp.create_line(
    net,
    from_bus=b3,
    to_bus=b_house1,
    length_km=0.02,
    std_type="CEB_LV_Service_Drop_16mm2",
    name="ServiceDrop_Pole1_House1",
    in_service=True,
    df=1.0,
    parallel=1,
    max_loading_percent=100.0,
    alpha=0.004,
    temperature_degree_celsius=40.0,
    geodata=[
        (6.9276, 79.8617),
        (6.9277, 79.8618)
    ]
)

# Pole 1 to House 2 (Solar 10 kW)
line_pole1_house2 = pp.create_line(
    net,
    from_bus=b3,
    to_bus=b_house2,
    length_km=0.02,
    std_type="CEB_LV_Service_Drop_16mm2",
    name="ServiceDrop_Pole1_House2",
    in_service=True,
    df=1.0,
    parallel=1,
    max_loading_percent=100.0,
    alpha=0.004,
    temperature_degree_celsius=40.0,
    geodata=[
        (6.9276, 79.8617),
        (6.9275, 79.8616)
    ]
)

# Pole 2 to House 3 (No Solar)
line_pole2_house3 = pp.create_line(
    net,
    from_bus=b4,
    to_bus=b_house3,
    length_km=0.02,
    std_type="CEB_LV_Service_Drop_16mm2",
    name="ServiceDrop_Pole2_House3",
    in_service=True,
    df=1.0,
    parallel=1,
    max_loading_percent=100.0,
    alpha=0.004,
    temperature_degree_celsius=40.0,
    geodata=[
        (6.9274, 79.8615),
        (6.9273, 79.8614)
    ]
)

# Pole 2 to House 4 (Solar 10 kW)
line_pole2_house4 = pp.create_line(
    net,
    from_bus=b4,
    to_bus=b_house4,
    length_km=0.02,
    std_type="CEB_LV_Service_Drop_16mm2",
    name="ServiceDrop_Pole2_House4",
    in_service=True,
    df=1.0,
    parallel=1,
    max_loading_percent=100.0,
    alpha=0.004,
    temperature_degree_celsius=40.0,
    geodata=[
        (6.9274, 79.8615),
        (6.9276, 79.8617)
    ]
)

# Pole 2 to House 5 (Solar 10 kW)
line_pole2_house5 = pp.create_line(
    net,
    from_bus=b4,
    to_bus=b_house5,
    length_km=0.02,
    std_type="CEB_LV_Service_Drop_16mm2",
    name="ServiceDrop_Pole2_House5",
    in_service=True,
    df=1.0,
    parallel=1,
    max_loading_percent=100.0,
    alpha=0.004,
    temperature_degree_celsius=40.0,
    geodata=[
        (6.9274, 79.8615),
        (6.9278, 79.8619)
    ]
)

# Pole 3 to House 6 (No Solar)
line_pole3_house6 = pp.create_line(
    net,
    from_bus=b5,
    to_bus=b_house6,
    length_km=0.02,
    std_type="CEB_LV_Service_Drop_16mm2",
    name="ServiceDrop_Pole3_House6",
    in_service=True,
    df=1.0,
    parallel=1,
    max_loading_percent=100.0,
    alpha=0.004,
    temperature_degree_celsius=40.0,
    geodata=[
        (6.9280, 79.8621),
        (6.9279, 79.8620)
    ]
)

# Pole 3 to House 7 (Solar 10 kW - Feeder End)
line_pole3_house7 = pp.create_line(
    net,
    from_bus=b5,
    to_bus=b_house7,
    length_km=0.02,
    std_type="CEB_LV_Service_Drop_16mm2",
    name="ServiceDrop_Pole3_House7",
    in_service=True,
    df=1.0,
    parallel=1,
    max_loading_percent=100.0,
    alpha=0.004,
    temperature_degree_celsius=40.0,
    geodata=[
        (6.9280, 79.8621),
        (6.9281, 79.8622)
    ]
)

# Based on CEB consumption data: 32% <30kWh, 48% 31-90kWh, 11% 91-120kWh, 8% 121-180kWh, 4% >180kWh
# House 1 (No Solar) – Low consumption (~60 kWh/month, 1 kW peak)
pp.create_load(
    net,
    bus=b_house1,
    p_mw=0.001,
    q_mvar=0.00048,
    name="Load_House1_Low_1kW",
    in_service=True
)

# House 2 (Solar 10 kW) – Low-Medium consumption (~75 kWh/month, 1.5 kW peak)
pp.create_load(
    net,
    bus=b_house2,
    p_mw=0.0015,
    q_mvar=0.00073,
    name="Load_House2_LowMed_1.5kW",
    in_service=True
)

# House 3 (No Solar) – Medium consumption (~105 kWh/month, 2 kW peak)
pp.create_load(
    net,
    bus=b_house3,
    p_mw=0.002,
    q_mvar=0.00097,
    name="Load_House3_Med_2kW",
    in_service=True
)

# House 4 (Solar 10 kW) – Medium-High consumption (~135 kWh/month, 2.5 kW peak)
pp.create_load(
    net,
    bus=b_house4,
    p_mw=0.0025,
    q_mvar=0.00121,
    name="Load_House4_MedHigh_2.5kW",
    in_service=True
)

# House 5 (Solar 10 kW) – Medium-High consumption (~135 kWh/month, 2.5 kW peak)
pp.create_load(
    net,
    bus=b_house5,
    p_mw=0.0025,
    q_mvar=0.00121,
    name="Load_House5_MedHigh_2.5kW",
    in_service=True
)

# House 6 (No Solar) – High consumption (~200 kWh/month, 3.5 kW peak)
pp.create_load(
    net,
    bus=b_house6,
    p_mw=0.0035,
    q_mvar=0.00170,
    name="Load_House6_High_3.5kW",
    in_service=True
)

# House 7 (Solar 10 kW - Feeder End) – High consumption (~200 kWh/month, 3.5 kW peak)
pp.create_load(
    net,
    bus=b_house7,
    p_mw=0.0035,
    q_mvar=0.00170,
    name="Load_House7_High_3.5kW",
    in_service=True
)

# Realistic household solar PV systems (diverse sizes)
# Based on SLSEA net metering guidelines and CEB data
# Inverters set to unity PF (q_mvar=0) for maximum active power export
# House 2 (Solar 2 kWp) – Small system for average household
pp.create_sgen(
    net,
    bus=b_house2,
    p_mw=0.002,
    q_mvar=0.0,
    sn_mva=0.0025,
    name="SolarPV_House2_2kWp",
    in_service=True,
    type="wye",
    scaling=1.0
)

# House 4 (Solar 3 kWp) – Medium system for medium-high consumption house
pp.create_sgen(
    net,
    bus=b_house4,
    p_mw=0.003,
    q_mvar=0.0,
    sn_mva=0.0035,
    name="SolarPV_House4_3kWp",
    in_service=True,
    type="wye",
    scaling=1.0
)

# House 5 (Solar 3 kWp) – Medium system for medium-high consumption house
pp.create_sgen(
    net,
    bus=b_house5,
    p_mw=0.003,
    q_mvar=0.0,
    sn_mva=0.0035,
    name="SolarPV_House5_3kWp",
    in_service=True,
    type="wye",
    scaling=1.0
)

# House 7 (Solar 4 kWp) – Large system for high consumption feeder end house
pp.create_sgen(
    net,
    bus=b_house7,
    p_mw=0.004,
    q_mvar=0.0,
    sn_mva=0.0045,
    name="SolarPV_House7_4kWp",
    in_service=True,
    type="wye",
    scaling=1.0
)

# Run AC power flow
pp.runpp(net, algorithm="nr", calculate_voltage_angles=True)

# Inspect bus voltages
print("=== Bus Voltages ===")
print(net.res_bus[["vm_pu", "va_degree"]])

# Inspect transformer loading
print("\n=== Transformer Results ===")
print(net.res_trafo[["loading_percent", "i_hv_ka", "i_lv_ka", "p_hv_mw", "q_hv_mvar"]])

# Inspect line loadings (main feeder + service drops)
print("\n=== Line Results ===")
print(net.res_line[["loading_percent", "i_ka", "p_from_mw", "q_from_mvar"]])

# External grid power
print("\n=== External Grid ===")
print(net.res_ext_grid[["p_mw", "q_mvar"]])