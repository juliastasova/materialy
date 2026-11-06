# Cvičení 7 – Debugger
# Spusť soubor (Run). Výsledek je špatný. Najdi chybu debuggerem.

# Program má sečíst číslice v PINu a vypsat jedno číslo –
# konečný součet. Teď vypisuje čtyři řádky.

pin = "4821"

soucet = 0

for znak in pin:
    soucet = soucet + int(znak)
    print(f"Součet číslic: {soucet}")
