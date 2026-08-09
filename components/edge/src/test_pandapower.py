import pandapower as pp

net = pp.create_empty_network()
b1=pp.create_bus(net, vn_kv=11.0, name="Bus 1")
b2=pp.create_bus(net, vn_kv=0.4, name="Bus 2")
pp.create_ext_grid(net, bus=b1, vm_pu=1.0)
pp.create_transformer(net, hv_bus=b1, lv_bus=b2, std_type="0.25 MVA 20/0.4 kV", name="Trnsfmr1")
pp.create_load(net, bus=b2, p_mw=0.05, q_mvar=0.01, name="Load 1")

pp.runpp(net)

print("Power flow succeeded")
print(net.res_bus)