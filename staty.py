import pandas

staty = pandas.read_json("staty.json")
staty = staty.set_index("name")
# Lidnaté evropské státy
lidnate_evropsko_staty = staty[(staty["population"] > 20_000_000) & (staty["region"] == "Europe")]
# Státy s velkou rozlohou nebo velkým počtem obyvatel
vyznamne_staty = staty[(staty["population"] > 50_000_000) & (staty["area"] > 3_000_000)]
# Státy západní a východní Evropy
staty_zap_vych_evropa = staty[staty["subregion"].isin(["Western Europe", "Eastern Europe"])]
print(staty_zap_vych_evropa)