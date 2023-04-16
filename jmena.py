import pandas
jmena = pandas.read_csv("jmena.csv")
jmena= jmena.set_index("jméno")
# Vypište na konzoli informace o jménu Jiří.
print(jmena.loc["Jiří"])
# Vypište na konzoli informace pro jména Martin, Zuzana a Josef.
print(jmena.loc[["Martin", "Zuzana", "Josef"]])
# Vypište na konzoli informace o všech nejčastějších jménech až po Martina.
print(jmena.loc[:"Martin"])
# Vypište pouze průměrné věky osob mající jména mezi Martinem a Terezou.
print(jmena.loc["Martin":"Tereza", "věk"])
# Vypište průměrný věk a původ pro všechna jména od Libora dolů.
print(jmena.loc["Libor":, ["věk", "původ"]])
# Vypište sloupečky mezi věkem a původem pro všechna jména v tabulce.
print(jmena.loc[:, "věk":"původ"])
