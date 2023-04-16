import pandas
# Načti data do DataFrame, který si pojmenuj jobs.
jobs = pandas.read_csv("DataAnalyst.csv")
# Nech si zobrazit názvy sloupců, které jsou v souboru uloženy.
print(jobs.columns)
# Je možné použít i info

# Podívej se, kolik má soubor řádek.
print(jobs.shape)
# Je možné použít i info

# Zjisti všechny informace o pracovní pozici na desátém řádku.
print(jobs.iloc[9])


# Podívej se, kde budou pracovat zájemci vybraní na dvanáctou až dvacátou pozici.
jobs_location = jobs[["Company Name", "Location"]]
print(jobs_location.iloc[11:20])

#jobs = jobs.rename(columns={"Headquarters": "HQ", "Type of ownership": "Ownership"})
#print(jobs.columns)
#jobs.to_csv("DataAnalystUpdated.csv")
