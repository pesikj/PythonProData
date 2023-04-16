import pandas

# Načti dva datové sety studentů do oddělených pandas DataFrame a pomocí funkce concat je spoj do jednoho setu.
studenti1 = pandas.read_csv("studenti1.csv")
studenti2 = pandas.read_csv("studenti2.csv")
studenti = pandas.concat([studenti1, studenti2], ignore_index=True)

# Pokud studentovi chybí ročník, znamená to, že již nestuduje. 
# Pokud mu chybí číslo skupiny, znamená to, že jde o dálkového studenta. 
# Kolik studentů v datovém setu již nestuduje a kolik jsou dálkoví studenti?
dalkari = studenti[studenti["kruh"].isnull()]
print(dalkari.shape)
nestudujici = studenti[studenti["ročník"].isnull()]
print(nestudujici.shape)

# Vyčisti data od studentů, kteří nestudují nebo studují jen dálkově. Nadále budeme pracovat pouze 
# s prezenčními studenty.
studenti = studenti.dropna()
print(studenti.head())

# Zjisti, kolik prezenčních studentů je v každém z oborů.
print(studenti.groupby("obor")["příjmení"].count())
print(studenti.groupby("obor").size())

# Zjisti průměrný prospěch studentů v každém oboru.
print(studenti.groupby("obor")["prospěch"].mean())

# Načti datový set s křestními jmény. Proveď join s tabulkou studentů tak, 
# abychom věděli pohlaví jednotlivých studentů.
jmena = pandas.read_csv("jmena.csv")
studenti = pandas.merge(studenti, jmena, on=["jméno"])
print(studenti.head())

# Zjisti, zda na naší fakultě studují IT spíše ženy nebo spíše muži.
print(studenti.groupby("pohlaví").count())
print(studenti.groupby("pohlaví")["jméno"].count())
print(studenti.groupby("pohlaví").size())