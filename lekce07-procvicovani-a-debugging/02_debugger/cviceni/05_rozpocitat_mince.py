# Cvičení 5 – Debugger
# Spusť soubor (Run). Výsledek je špatný. Najdi chybu debuggerem.

# Program rozpočítá částku na mince: nejdřív bere dvacetikoruny,
# ze zbytku pětikoruny a co zůstane, jsou koruny.
#
# Na výpisu je jedno číslo, které takhle vyjít nemůže.

zbyva = 87
dvacetikoruny = 0
petikoruny = 0

while zbyva >= 20:
    dvacetikoruny = dvacetikoruny + 1
    zbyva = zbyva - 20

while zbyva >= 5:
    petikoruny = petikoruny + 1
    zbyva = zbyva - 20

print(f"Dvacetikoruny: {dvacetikoruny}")
print(f"Pětikoruny: {petikoruny}")
print(f"Koruny: {zbyva}")
