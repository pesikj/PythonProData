import pandas
pandas.set_option('display.max_columns', None)
pandas.set_option('display.width', 600)
staty = pandas.read_json("staty.json")
staty["density"] = staty["population"] / staty["area"]
staty = staty.sort_values(["name", "density"], ascending=[False, True])
print(staty.head())