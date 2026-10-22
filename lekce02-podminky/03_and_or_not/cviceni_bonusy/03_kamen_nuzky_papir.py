# Bonus 3 – And, or a not
# Doplň kód pod zadání a soubor spusť (Run).

# Kámen, nůžky, papír. Zeptej se obou hráčů na tah – ať zadají
#     "kamen", "nuzky" nebo "papir". Vypiš, kdo vyhrál:
#       - "Remíza.", když mají oba stejně,
#       - jinak urči vítěze podle pravidel:
#           kámen tupí nůžky, nůžky stříhají papír, papír balí kámen.
#     Vypiš "Vyhrál hráč 1." / "Vyhrál hráč 2.".

hrac1 = input("hrac1: kamen/noznice/papier: ")
hrac2 = input("hrac2: kamen/noznice/papier: ")
if(hrac1 == hrac2):
    print("remiza")
elif(hrac1 == "kamen" and hrac2 =="noznice" or hrac1 == "nuzky" and hrac2 == "papier" or hrac1 == "papier" and hrac2 == "kamen"):
    print("vyhral hrac 1")
else:
    print("vyhral hrac 2")