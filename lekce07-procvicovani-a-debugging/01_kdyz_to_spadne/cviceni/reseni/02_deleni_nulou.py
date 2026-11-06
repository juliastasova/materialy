# Řešení cvičení 2 – Když to spadne
# Opravený program. Pod ním je, jak se ta chyba našla.

znamky = "13245"

soucet = 0
pocet = 0

for znak in znamky:
    soucet = soucet + int(znak)
    pocet = pocet + 1

print(f"Průměr známek: {soucet / pocet:.1f}")


# ZeroDivisionError: division by zero
#
# Nulou dělit nejde. Hláška tedy říká, že pocet byl v tu chvíli nula.
#
# Proměnná pocet se založila na začátku a pak už se o ni nikdo
# nestaral. V cyklu chybělo zvyšování – soucet se zvětšoval,
# pocet zůstal na nule.
