import pandas
jmena = pandas.read_csv("jmena.csv")

#Vypiš všechny řádky se jmény, jejichž nositelé mají průměrný věk vyšší než 60.
print(jmena[jmena["věk"] > 60])
#Vypiš pouze jména z těch řádků, kde četnost je mezi 80 000 a 100 000.
tab_2 = jmena[(jmena["četnost"] > 80_000) & (jmena["četnost"] < 100_000)]
#print(tab_2["jméno"])
#Vypiš jména a četnost pro jména se slovanským nebo hebrejským původem. Kolik takových jmen je?
tab_3 = jmena[jmena["původ"].isin(["hebrejský", "slovanský"])]
print(tab_3[["jméno", "četnost"]])
#Vypiš všechna jména, která mají svátek první 3 dny v prosinci.
tab_4 = jmena[jmena["svátek"].isin(["1.12", "2.12", "3.12"])]
print(tab_4["jméno"])
print("*" * 60)
t1 = jmena[jmena["věk"] > 60]
print(t1[["jméno", "věk"]])

pandas.to_datetime(jmena["svátek"])