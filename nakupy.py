import pandas
nakupy = pandas.read_csv("nakupy.csv")
nakupy_orezane = nakupy[["jmeno", "cena"]]
print(nakupy_orezane.iloc[-5:])
