# Modul random
import random

# Náhodné celé číslo v rozsahu 1 až 10
cislo = random.randint(1, 10)
print("Náhodné číslo:", cislo)

# Náhodná hodnota z listu
barva = random.choice(["červená", "zelená", "modrá"])
print("Vybraná barva:", barva)

# Zamíchání pořadí prvků v listu
cisla = [1, 2, 3, 4, 5]
random.shuffle(cisla)
print("Zamíchaný list:", cisla)

# Náhodné desetinné číslo mezi 0 a 1
desetinne = random.random()
print("Desetinné číslo:", desetinne)
