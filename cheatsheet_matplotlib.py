# import včetně alias
import matplotlib.pyplot as plt

# tohle ignorujte, doplněné proměnné kvůli chybovým varováním
x = []
y = []
x1 = []
y1 = []
x2 = []
y2 = []

# Základní typy grafů
plt.plot([1, 2, 3, 4], [10, 20, 25, 30])  # čárový graf
plt.bar(["A", "B", "C"], [5, 7, 3])  # sloupcový graf
plt.barh(["A", "B", "C"], [5, 7, 3])  # vodorovný sloupcový graf
plt.scatter([1, 2, 3], [4, 5, 6])  # bodový graf
plt.pie([30, 50, 20], labels=["A", "B", "C"])  # koláčový graf
plt.hist([1, 2, 2, 3, 3, 3, 4], bins=4)  # histogram

# Popisky a titulky
plt.title("Nadpis grafu")  # nastaví hlavní nadpis
plt.xlabel("Osa X")  # popisek osy X
plt.ylabel("Osa Y")  # popisek osy Y
plt.legend(["Data A"])  # legenda k datové řadě
plt.grid(True)  # zapne mřížku v grafu

# Zobrazení grafu a uložení
plt.show()  # zobrazí graf v okně
plt.savefig("graf.png")  # uloží graf jako obrázek (PNG, JPG atd.)

# Více grafů v jednom obrázku (subploty)
plt.subplot(1, 2, 1)  # rozdělí plátno na 1 řádek, 2 sloupce – aktivuje 1. graf
plt.plot([1, 2, 3], [4, 5, 6])
plt.subplot(1, 2, 2)  # aktivuje 2. graf vpravo
plt.plot([1, 2, 3], [6, 5, 4])
plt.show()

# Stylizace grafů
plt.plot(x, y, color="red", linestyle="--", marker="o")  # červená čára, přerušovaná, s kolečky
plt.bar(x, y, width=0.5, color="green")  # užší sloupce, zelená barva
plt.xticks(rotation=45)  # otočení popisků na ose X
plt.tight_layout()  # automatické zarovnání prvků grafu

# Práce s více datovými řadami
plt.plot(x1, y1, label="Skupina A")
plt.plot(x2, y2, label="Skupina B")
plt.legend()  # zobrazí legendu
plt.show()