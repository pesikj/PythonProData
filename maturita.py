import pandas

u202 = pandas.read_csv("u202.csv").dropna()
u203 = pandas.read_csv("u203.csv").dropna()
u302 = pandas.read_csv("u302.csv").dropna()
u202["mistnost"] = "u202"
u203["mistnost"] = "u202"
u302["mistnost"] = "u302"
maturita = pandas.concat([u202, u203, u302], ignore_index=True)
studenti = pandas.read_csv("studenti.csv")
maturita = pandas.merge(maturita, studenti, how="left")
predsedajici = pandas.read_csv("predsedajici.csv")
predsedajici["den"] = predsedajici["den"].str.strip()
maturita = pandas.merge(maturita, predsedajici, how="left", on=["den"])
maturita = maturita.rename(columns={"jmeno_x": "jmenoStudenta", "jmeno_y": "jmenoPredsedajiciho"})
print(maturita.groupby("predmet")["znamka"].min())
