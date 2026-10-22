# Cvičení 6 – And, or a not
# Doplň kód pod zadání a soubor spusť (Run).

# Zabezpečení domu. Dům je zabezpečený, jen když jsou zavřené dveře,
#    zavřená okna a zároveň zapnutý alarm.
#    Zeptej se na všechny tři věci (ano/ne). Pomocí not (…) vypiš
#    "Pozor, dům není zabezpečený!", když zabezpečený NENÍ,
#    jinak vypiš "Zabezpečeno.".


dvere = input("zavreté dveer: ano/ne")
okná = input("zavrené okná: ano/ne")
alarm = input("zapnutý alarm: ano/ne")
if not(dvere == "ano" or okrná == "ano" or alarm == "ano"):
    print("dom nie je zabezpečený")
else:
    print("zabezpečené")