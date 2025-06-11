# První řádek kódu:
# 1. Napište script, který bude mít output do konzole:
# 1
# Hello World

# 2
# Hello
# World

# 3
# H
# e
# l
# l
# o

# W
# o
# r
# l
# d


# 2 Proměnné
# Vytvořte proměnné:
# křestní jméno
# příjmení
# celé jméno
# e-mail
# uživatel je registrován

# 3 Primitivní datové typy
# přiřaďte do proměnných správné datové typy
# string
# integer
# float
# boolean
# výstup do konzole

# Spojte dva stringy pomocí +
# Spojte string a proměnnou pomocí šablonového literálu

# Změňte integer na float
# Změňte string na integer
# Změňte integer na string

# Python jako kalkulačka - aritmetické operátory
# a) trojúhelník má stranu 7.5cm a výšku 8.2 cm, spočítejte plochu
# b) pravoúhlý trojúhelník má odvěsny 5cm a 7cm, spočítejte délku přepony
# c) kruh má poloměr 8cm, spočítejte
#                                     obvod
#                                     plochu
#                                     objem koule o stejném poloměru
# d) spočítejte kořeny rovnice x^2 + 5x + 6 = 0

# 4 Logické operátory - True/False

# a) Vyhodnoťte následující výrazy a zjistěte, zda jsou True nebo False
#    Zapište výsledek do proměnné a vypište ji do konzole

# Je 5 rovno 5?
# Je 10 různé od 3?
# Je 7 větší než 2?
# Je 4 menší nebo rovno 4?
# Je 3 větší než nebo rovno 10?

# b) Práce s proměnnými
# Do proměnných uložte věk dvou osob (např. Alice a Bob)
# Pomocí logických operátorů zjistěte:
#   - Je Alice starší než Bob?
#   - Je Bob mladší nebo stejně starý jako Alice?

# c) Použití "and" a "or"
# Máme následující údaje o uživateli:
#   věk = 20
#   je_student = True
# Zjistěte:
#   - Má nárok na studentskou slevu (věk < 26 a je student)?
#   - Má nárok na důchod (věk >= 65 nebo není student)?

# d) Použití not
# Máme proměnnou:
#   verified = False
# Ověřte, zda uživatel není ověřený (použijte `not`)

# e) Porovnejte dvě hesla
# Do dvou proměnných uložte textové řetězce jako hesla (password_1 a password_2)
# Zkontrolujte, jestli se hesla shodují

# f) BONUS: Složený výraz
# Zjistěte, jestli má uživatel právo vstoupit:
# Podmínky:
#   - věk alespoň 18 let
#   - a zároveň není na blacklistu (proměnná is_blacklisted = False)

# 5 Rozhodování v Pythonu – podmínky (if, elif, else)

# a) Základní podmínky
# Vytvořte proměnnou číslo = 10
# Pomocí if-elif-else:
#   - Pokud je číslo větší než 10, vypište "Číslo je větší než 10"
#   - Pokud je číslo rovno 10, vypište "Číslo je přesně 10"
#   - Jinak vypište "Číslo je menší než 10"

# b) Určete, zda je číslo sudé nebo liché
# Použijte zbytek po dělení (%) a podmínku if

# c) Ověření věku pro vstup
# Do proměnné `vek` zadejte věk uživatele
# Pokud je uživatel mladší než 15 → "Nemáte přístup"
# Pokud je 15–17 let → "Přístup s omezením"
# Pokud je 18 a více → "Vítejte!"

# d) Převod známky na slovní hodnocení
# Do proměnné `znamka` zadejte číslo 1–5
# Pokud je:
#   1 → "Výborný"
#   2 → "Chvalitebný"
#   3 → "Dobrý"
#   4 → "Dostatečný"
#   5 → "Nedostatečný"
# Pro jiné číslo vypište "Neplatná známka"

# e) BONUS: Automatická odpověď robota
# Uživatel zadá svůj dotaz jako string do proměnné `dotaz`
# Pokud obsahuje "ahoj" → vypište "Ahoj! Jak vám mohu pomoci?"
# Pokud obsahuje "cena" → vypište "Naše produkty začínají na 199 Kč."
# Jinak vypište "Omlouvám se, nerozumím otázce."
# (Můžete použít `in` a metodu `.lower()` pro zjednodušení)

# 6 Cykly a smyčky v Pythonu (Loops)

# a) while smyčka – počítání do 5
# Pomocí while cyklu vypište čísla od 1 do 5 včetně
# Použijte samopřiřazení (counter += 1)

# b) while + input
# Pomocí while cyklu se ptejte uživatele na jméno, dokud nenapíše "konec"
# Pokud zadá cokoliv jiného, vypište "Ahoj, [jméno]!"

# c) for smyčka – výpis čísel
# Pomocí for cyklu vypište čísla od 10 do 20

# d) for smyčka – práce se seznamem
# Udělejte skript, který vypíše na jednotlivé řádky pomocí for smyčky 5, 4, 3, 2, 1, start

# e) Použití break
# Použij while smyčku, která se opakuje navždy (while True)
# Pomocí input() se ptej: „Zadej tajné heslo: “
# Pokud uživatel zadá "1234", vypiš "Správné heslo" a použij break

# f) Výpočet součtu čísel
# Pomocí for smyčky sečti všechna čísla od 1 do 100 a výsledek ulož do proměnné `soucet`

# BONUS: Tabulka násobků
# Pomocí for smyčky vypiš násobilku pro číslo 7 (od 1 do 10)
# Výstup např.: "7 x 3 = 21"

# 7 Funkce v Pythonu

# a) Vytvoř funkci bez argumentu
# Napiš funkci `pozdrav`, která vypíše: "Ahoj, vítám tě v kurzu Pythonu!"
# Funkci zavolej.

# b) Funkce s jedním argumentem
# Napiš funkci `pozdrav_jmeno`, která přijme jedno jméno jako argument
# a vypíše: "Ahoj, [jméno]!"
# Vyzkoušej ji s různými jmény.

# c) Funkce se dvěma argumenty
# Napiš funkci `secti`, která sečte dvě čísla a vrátí výsledek pomocí `return`
# Vypiš výsledek volání funkce `secti(5, 8)`

# d) Funkce s návratovou hodnotou
# Napiš funkci `je_plnolety`, která přijme věk (číslo) a vrátí True, pokud je větší nebo roven 18, jinak False
# Vypiš výsledek pro věk 20 a 15

# e) Funkce s výpočtem
# Napiš funkci `obvod_ctverce`, která přijme délku jedné strany čtverce a vrátí obvod
# Ověř, že `obvod_ctverce(4)` vrátí 16

# f) Funkce s řetězci
# Napiš funkci `vytvor_email`, která přijme jméno a příjmení a vrátí string ve formátu: `jmeno.prijmeni@example.com`
# Příklad: `vytvor_email("filip", "slunsky")` → `"filip.slunsky@example.com"`

# g) Funkce s podmínkou uvnitř
# Napiš funkci `pozdrav_podle_casu`, která přijme číslo (hodinu)
# Pokud je hodina menší než 12, vrátí "Dobré ráno"
# Jinak vrátí "Dobrý den"

# BONUS: Funkce s klíčovým slovem pass
# Napiš funkci `bude_dodelano`, která zatím nic nedělá – použij klíčové slovo `pass`

# 8 Rozsah proměnných (variable scope)

# a) Globální proměnná
# Vytvoř proměnnou jmeno = "Filip" mimo jakoukoliv funkci
# Potom vytvoř funkci pozdrav(), která použije tuto proměnnou a vytiskne: "Ahoj, Filip"
# Zavolej funkci

# b) Lokální proměnná ve funkci
# Vytvoř funkci nastav_jmeno(), která vytvoří proměnnou jmeno = "Petra"
# Uvnitř funkce ji vypiš pomocí print()
# Zkus proměnnou jmeno vytisknout i mimo funkci – co se stane?

# c) Přístup ke globální proměnné z funkce (pouze pro čtení)
# Vytvoř globální proměnnou vek = 30
# Vytvoř funkci ukaz_vek(), která pouze vytiskne věk
# Zavolej funkci

# d) Změna globální proměnné z funkce
# Uprav předešlou funkci ukaz_vek(), aby měnila globální proměnnou vek na 35
# Nezapomeň uvnitř funkce použít klíčové slovo `global`
# Zavolej funkci a potom vypiš vek mimo funkci – co se změnilo?

# e) Lokální proměnná uvnitř smyčky
# Použij for cyklus k vypsání čísel 0 až 4
# Uvnitř cyklu vytvoř proměnnou text = "běžím"
# Vypiš ji v každém kroku
# Po skončení smyčky zkus vytisknout text – co se stane?

# BONUS: Scope a stejný název proměnné
# Vytvoř globální proměnnou jmeno = "Eva"
# Potom vytvoř funkci zmen_jmeno(), která má uvnitř proměnnou jmeno = "Tomáš"
# Vypiš jmeno uvnitř funkce a mimo ni – porovnej rozdíly

# 9 Komplexní datové typy – Listy

# a) Vytvoř seznam
# Vytvoř seznam se třemi oblíbenými jídly a ulož ho do proměnné oblibena_jidla
# Vypiš celý seznam do konzole

# b) Zjisti délku seznamu
# Pomocí len() zjisti, kolik prvků seznam obsahuje

# c) Přístup přes index
# Vypiš první a poslední prvek seznamu
# (přes index 0 a přes index -1)

# d) Změna hodnoty v seznamu
# Změň druhé jídlo v seznamu na "pizza"
# Znovu vypiš celý seznam

# e) Přidání nového prvku
# Přidej na konec seznamu nové jídlo pomocí append()
# Přidej na druhé místo další jídlo pomocí insert()

# f) Odebrání prvku
# Odstraň konkrétní jídlo pomocí remove()
# Odstraň prvek na konkrétním indexu pomocí pop()

# g) Minimum a maximum
# Vytvoř nový seznam cisel = [3, 7, 2, 9, 4]
# Vypiš nejmenší a největší číslo pomocí min() a max()

# h) Iterování (looping)
# Vytvoř seznam zvířat = ["kočka", "pes", "králík"]
# Pomocí for smyčky vypiš každé zvíře na nový řádek

# BONUS: Kombinování typů
# Vytvoř seznam mix = [23, "text", True]
# Vypiš každý prvek pomocí for smyčky a zároveň vypiš i jeho datový typ (type())

# 10 Komplexní datové typy – Sety (množiny)

# a) Vytvoření množiny
# Vytvoř množinu oblibene_barvy s hodnotami: "červená", "zelená", "modrá"
# Vypiš celou množinu do konzole

# b) Žádné duplicity
# Vytvoř množinu cisla = {1, 2, 2, 3, 4, 4, 5}
# Vypiš množinu – co se stane s duplicitami?

# c) Přidávání prvků
# Přidej do množiny oblibene_barvy novou barvu pomocí add()
# Vytvoř druhou množinu vice_barev = {"žlutá", "fialová"}
# Slouč je pomocí update()

# d) Odebrání prvků
# Odeber "zelená" pomocí remove()
# Odeber "černá" pomocí discard() – co se stane?
# Zkus odstranit "černá" pomocí remove() – co se stane?

# e) Testování prvků
# Ověř, jestli "modrá" je v oblibene_barvy pomocí 'in'
# Ověř, jestli "černá" není v oblibene_barvy pomocí 'not in'

# f) Iterování přes množinu
# Pomocí for smyčky vypiš všechny barvy v množině oblibene_barvy

# g) Operace s množinami
# Vytvoř dvě množiny:
#  set_a = {1, 2, 3, 4}
#  set_b = {3, 4, 5, 6}
# Vypiš:
# - průnik (intersection)
# - sjednocení (union)
# - je set_a podmnožinou set_b? (issubset)
# - je set_a nadmnožinou set_b? (issuperset)

# BONUS:
# Převod seznamu na množinu
# Vytvoř seznam se_studenty = ["Anna", "Petr", "Petr", "Lucie", "Anna"]
# Převáděním na množinu zjisti, kolik unikátních jmen se v seznamu nachází

# 11 Komplexní datové typy – Tuples (n-tice)

# a) Vytvoření tuple
# Vytvoř tuple student = ("Anna", 22, True)
# Vypiš tuple do konzole

# b) Tuple s jedním prvkem
# Vytvoř tuple s jedním prvkem "Python"
# (Pozor na čárku – bez ní to není tuple)
# Vypiš typ pomocí funkce type()

# c) Přístup k prvkům pomocí indexu
# Vytvoř tuple barvy = ("červená", "zelená", "modrá")
# Vypiš první prvek (index 0)
# Vypiš poslední prvek pomocí záporného indexu

# d) Iterování přes tuple
# Pomocí for smyčky vypiš všechny prvky tuple barvy

# e) Délka, minimum, maximum
# Vytvoř tuple cisla = (3, 1, 5, 2)
# Vypiš:
# - počet prvků (len)
# - nejmenší prvek (min)
# - největší prvek (max)

# f) Neměnnost
# Zkus změnit hodnotu jednoho prvku v tuple barvy
# -> co se stane?

# g) Konverze na list
# Převeď tuple barvy na list pomocí list(barvy)
# Změň druhý prvek na "žlutá"
# Převeď zpět na tuple

# BONUS:
# Použití tuple k vrácení více hodnot z funkce
# Napiš funkci, která vrátí součet a rozdíl dvou čísel jako tuple
# def soucet_rozdil(a, b):
#     return (a + b, a - b)
# Výsledek ulož do proměnné a vypiš jednotlivé prvky

# 12 Komplexní datové typy – Dictionary (slovníky)

# a) Vytvoření slovníku
# Vytvoř slovník student = {"jméno": "Petr", "věk": 21, "aktivní": True}
# Vypiš celý slovník

# b) Přístup ke konkrétní hodnotě přes klíč
# Vypiš jméno studenta (pomocí klíče "jméno")
# Vypiš věk studenta (pomocí klíče "věk")

# c) Přidání nebo změna položky
# Změň věk na 22
# Přidej nový klíč "město" s hodnotou "Praha"

# d) Použití metody update()
# Přidej nebo změň hodnoty pomocí student.update({"aktivní": False, "škola": "ČVUT"})

# e) Odebrání položky
# Odeber klíč "město" pomocí metody pop()

# f) Získání všech klíčů a hodnot
# Vypiš seznam všech klíčů pomocí student.keys()
# Vypiš seznam všech hodnot pomocí student.values()

# g) Iterování přes slovník
# Pomocí for smyčky vypiš všechny klíče a jejich hodnoty ve formátu:
# jméno: Petr
# věk: 22
# ...

# BONUS:
# Vytvoř slovník známky = {"matematika": 1, "čeština": 2, "angličtina": 1}
# Spočítej průměr známek (pomocí values())
# Vypiš předměty, kde má student jedničku

# 13 Kombinace komplexních datových typů

# a) List of lists (seznamy v seznamu)
# Vytvoř seznam známek tří studentů:
# známky = [[1, 2, 1], [2, 3, 2], [1, 1, 1]]
# Vypiš známky druhého studenta
# Vypiš první známku třetího studenta

# b) List of sets (seznamy množin)
# Vytvoř seznam koníčků pro každého uživatele:
# konicky = [{"běh", "plavání"}, {"čtení", "vaření"}, {"běh", "vaření"}]
# Vypiš koníčky druhého uživatele

# BONUS:
# Které koníčky mají první a třetí uživatel společné?
# Vypiš jejich průnik pomocí .intersection()

# c) List of dictionaries (seznamy slovníků)
# Vytvoř seznam studentů:
# studenti = [
#     {"jméno": "Petr", "věk": 20},
#     {"jméno": "Lucie", "věk": 21},
#     {"jméno": "Jan", "věk": 19}
# ]
# Vypiš jméno druhého studenta
# Změň věk třetího studenta na 20

# d) Slovník ve slovníku (nested dictionary)
# Vytvoř slovník student = {
#     "jméno": "Petr",
#     "kontakt": {
#         "email": "petr@example.com",
#         "telefon": "123456789"
#     }
# }
# Vypiš e-mail studenta

# e) List ve slovníku
# Vytvoř slovník: student = {"jméno": "Lucie", "známky": [1, 2, 1, 1]}
# Vypiš poslední známku
# Přidej novou známku do seznamu

# f) N-tice ve slovníku
# Vytvoř slovník: bod = {"x": 10, "y": 20, "souřadnice": (10, 20)}
# Vypiš souřadnice
# Vypiš souřadnici y (druhý prvek n-tice)

# BONUS - kombinace více struktur:
# Vytvoř seznam slovníků, kde každý obsahuje jméno a souřadnice (jako n-tici):
# body = [
#     {"jméno": "A", "souřadnice": (0, 0)},
#     {"jméno": "B", "souřadnice": (3, 4)}
# ]
# Vypiš vzdálenost bodu B od počátku pomocí Pythagorovy věty

# 14 Řešení chyb a výjimek v Pythonu

# a) SyntaxError - chyba syntaxe
# Zkus tento kód, oprav chybu a spusť:
# print("Ahoj"

# b) TypeError - chybný datový typ
# Co se stane, když zkombinujeme string a int?
# Oprav kód tak, aby fungoval (použij konverzi na string):
# print("Můj věk je " + 20)

# c) KeyError - chybějící klíč ve slovníku
# slovnik = {"jmeno": "Petr"}
# Vypiš slovnik["prijmeni"]
# Ošetři kód, aby při chybě klíče nevznikla chyba, ale vypsala se přátelská zpráva

# d) ValueError - špatná hodnota
# Převod nečíselného stringu na int:
# cislo = int("abc")
# Použij try-except, aby program nekončil chybou, ale vypsal "Neplatný vstup"

# e) KeyboardInterrupt - přerušení programu uživatelem
# Vytvoř program, který čeká na vstup uživatele pomocí input()
# Ošetři možnost přerušení klávesou Ctrl+C pomocí try-except a vypiš "Program přerušen uživatelem"

# f) Ošetření chyb pomocí try-except
# Napiš funkci safe_int(), která přečte vstup od uživatele a pokusí se jej převést na int
# Pokud to nelze, vyzve uživatele znovu

# g) Ochrana datových typů a vstupů
# Zkontroluj, zda je proměnná x typu int, pokud ne, vypiš upozornění
# x = "test"

# BONUS: Použij finally blok, který vždy vypíše "Konec programu"

