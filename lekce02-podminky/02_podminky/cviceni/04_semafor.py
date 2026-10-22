# Cvičení 4 – Podmínky
# Doplň kód pod zadání a soubor spusť (Run).

# Máš proměnnou barva se stavem semaforu ("červená", "oranžová"
#    nebo "zelená"). Vypiš, co má řidič udělat:
#    "červená" → "Stůj", "oranžová" → "Připrav se", "zelená" → "Jeď",
#    cokoli jiného → "Neznámý signál".
barva = "zelená"


barva = "zelená"
if barva == "červená":
    print("Stůj")
elif barva == "oranžová":
    print("Připrav se")
elif barva == "zelená":
    print("Jeď")
else:
    print("Neznámý signál")