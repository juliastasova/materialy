# Cvičení 3 – Definice funkce
# Doplň kód pod zadání a soubor spusť (Run).

# Napiš funkci ohodnot_znamku, která má na vstupu celé číslo a vypíše:
#    1 → "Výborně", 2 → "Chvalitebně", 3 → "Dobře",
#    cokoliv jiného → "Ještě zabereme".
#    Zavolej ji v cyklu for pro známky 1 až 5.


def ohodnot_znamku(znamka):
    if znamka == 1:
        print("Výborně")
    elif znamka == 2:
        print("Chvalitebně")
    elif znamka == 3:
        print("Dobře")
    else:
        print("Ještě zabereme")

for znamka in range(1, 6):
    ohodnot_znamku(znamka)