# Modul csv
import csv

# Zápis dat do CSV souboru
data = [
    ["jméno", "věk"],
    ["Anna", 25],
    ["Petr", 30]
]

with open("uzivatele.csv", "w", newline="", encoding="utf-8") as soubor:
    zapisovac = csv.writer(soubor)
    zapisovac.writerows(data)

# Čtení dat ze souboru
with open("uzivatele.csv", "r", encoding="utf-8") as soubor:
    ctecka = csv.reader(soubor)
    for radek in ctecka:
        print("Řádek:", radek)
