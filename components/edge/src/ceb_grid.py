import pandapower as pp

net = pp.create_empty_network()

b1 = pp.create_bus(net, vn_kv=11.0, name="CEB 11kv Bus")
b2 = pp.create_bus(net, vn_kv=0.4, name="Substation 0.4kV Bus")
b3 = pp.create_bus(net, vn_kv=0.4, name="Household Bus")

# External grid (Slack Bus)
pp.create_ext_grid(net, bus=b1, vm_pu=1.0)

# Custom Transformer (160 kVA, 11kV/0.4kV)
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
    name="CEB 11kV/0.4kV 160kVATransformer"
)

# Custom CEB Line Type
pp.create_std_type(
    net,
    data={
        "r_ohm_per_km": 0.550,
        "x_ohm_per_km": 0.091,
        "c_nf_per_km": 0.0,
        "max_i_ka": 0.213,
        "type": "ol",
    },
    name="CEB LV ABC 70mm2",
    element="line"
)

# Line from b2 to b3 (50m = 0.05 km)
pp.create_line(
    net,
    from_bus=b2,
    to_bus=b3,
    length_km=0.05,
    std_type="CEB LV ABC 70mm2",
    name="CEB Consumer Line 50m"
)

pp.create_load(net, bus=b3, p_mw=0.002, q_mvar=0.00065)

pp.create_sgen(
    net,
    bus=b3,
    p_mw=0.010,
    q_mvar=0.000,
    sn_mva=0.010,
    name="Rooftop Solar PV 10kW"
)

pp.runpp(net)
















































print("\n=== BUS VOLTAGES ===")
print(net.res_bus[["vm_pu", "va_degree"]])

print("\n=== EXTERNAL GRID POWER FLOW ===")
# Negative active power (p_mw) indicates reverse power flow into the 11kV grid
print(net.res_ext_grid[["p_mw", "q_mvar"]])

print("\n=== TRANSFORMER LOADING & POWER FLOW ===")
print(net.res_trafo[["loading_percent", "p_hv_mw", "q_hv_mvar", "pl_mw"]])

print("\n=== LV LINE LOADING & POWER FLOW ===")
# Negative p_from_mw means power flows backwards from b3 towards b2
print(net.res_line[["loading_percent", "i_ka", "p_from_mw", "p_to_mw", "pl_mw"]])

print(net.res_bus[["vm_pu", "va_degree"]])

# Transformer Loading Percentage
print("\n--- Transformer Loading ---")
print(net.res_trafo[["loading_percent", "p_hv_mw", "q_hv_mvar", "pl_mw"]])

# LV ABC Line Loading Percentage & Losses
print("\n--- LV Line Loading & Losses ---")
print(net.res_line[["loading_percent", "i_ka", "pl_mw", "ql_mvar"]])