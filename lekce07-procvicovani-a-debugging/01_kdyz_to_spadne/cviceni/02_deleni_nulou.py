# Cvičení 2 – Když to spadne
# Spusť soubor (Run), přečti hlášku a chybu oprav.

# Program má spočítat průměr známek.

znamky = "13245"

soucet = 0
pocet = 0

for znak in znamky:
    soucet = soucet + int(znak)

print(f"Průměr známek: {soucet / pocet:.1f}")
