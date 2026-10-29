# Bonus 4 – Návratová hodnota
# Doplň kód pod zadání a soubor spusť (Run).

# Napiš funkci cena_jizdenky, která má na vstupu věk cestujícího
#     a základní cenu jízdenky, a vrátí cenu, kterou cestující zaplatí:
#
#       děti do 10 let včetně       zdarma
#       mládež do 18 let včetně     polovina
#       senioři od 65 let včetně    třetina
#       ostatní                     plná cena
#
#     Vyzkoušej ji pro několik věků a ceny vypiš.
def ohodnot_znamku(znamka):
    if znamka == 1:
        return "Výborně"
    elif znamka == 2:
        return "Chvalitebně"
    elif znamka == 3:
        return "Dobře"
    else:
        return "Ještě zabereme"

for znamka in range(1, 6):
    print(znamka, "->", ohodnot_znamku(znamka))