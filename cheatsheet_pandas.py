# import včetně alias
import pandas as pd

# Načítání a ukládání dat
df = pd.read_csv("sales.csv")  # načte data ze souboru CSV
df = pd.read_excel("data.xlsx")  # načte data z Excel souboru
df.to_csv("vystup.csv", index=False)  # uloží DataFrame do CSV souboru
df.to_excel("vystup.xlsx", index=False)  # uloží DataFrame do Excel souboru

# Základní přehled o datech
df.head()  # zobrazí prvních 5 řádků
df.tail()  # zobrazí posledních 5 řádků
df.info()  # zobrazí informace o sloupcích a typy dat
df.describe()  # základní statistický přehled (průměr, min, max atd.)
df.shape  # vrátí počet řádků a sloupců (např. (100, 5))
df.columns  # vrátí názvy sloupců
df.dtypes  # vrátí datové typy sloupců


# Výběr dat
df["jmeno_sloupce"]  # výběr jednoho sloupce
df[["sloupec1", "sloupec2"]]  # výběr více sloupců
df.iloc[0]  # první řádek podle indexu
df.loc[0]  # první řádek podle názvu indexu (pokud je nastavený)
df.iloc[0:5]  # prvních 5 řádků (řezání)

# Filtrování a podmínky
df[df["vek"] > 30]  # řádky, kde je věk větší než 30
df[df["overeno"] == "ano"]  # řádky, kde je ověřeno "ano"

# Přidání a úprava sloupců
df["cele_jmeno"] = df["jmeno"] + " " + df["prijmeni"]  # nový sloupec spojením dvou
df["status"] = df["overeno"].apply(lambda x: "zaměstnanec" if x == "ano" else "host")  # nový sloupec podle podmínky

# Mazání
df.drop("sloupec", axis=1, inplace=True)  # odstraní sloupec
df.drop([0, 1], axis=0)  # odstraní řádky s indexem 0 a 1

# Úpravy dat
df.rename(columns={"jmeno": "jméno"})  # přejmenuje sloupec
df["jmeno"] = df["jmeno"].str.upper()  # převede text na velká písmena
df["vek"] = df["vek"].fillna(0)  # nahradí chybějící hodnoty (NaN) nulou
df = df.dropna()  # odstraní řádky s chybějícími hodnotami

# Seskupování a agregace 
df.groupby("oddeleni")["plat"].mean()  # průměrný plat podle oddělení
df["plat"].sum()  # součet všech hodnot ve sloupci
df["vek"].value_counts()  # počet výskytů jednotlivých hodnot ve věku

# Řazení a třídění
df.sort_values("vek")  # seřadí podle věku vzestupně
df.sort_values("plat", ascending=False)  # seřadí podle platu sestupně

# Vytváření DataFrame z dat
data = {"jmeno": ["Petr", "Jana"], "vek": [28, 34]}
df = pd.DataFrame(data)  # vytvoří nový DataFrame ze slovníku
