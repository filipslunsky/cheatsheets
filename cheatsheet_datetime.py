# Modul datetime
from datetime import datetime, timedelta

# Aktuální datum a čas
ted = datetime.now()
print("Aktuální čas:", ted)

# Vytvoření konkrétního data
datum = datetime(2024, 12, 24)
print("Štědrý den:", datum)

# Rozdíl mezi dvěma daty
rozdil = datum - ted
print("Dní do Štědrého dne:", rozdil.days)

# Přidání 7 dní
za_tyden = ted + timedelta(days=7)
print("Za týden:", za_tyden.strftime("%d.%m.%Y"))

# Formátování data
print("Formátovaný čas:", ted.strftime("%H:%M:%S"))

