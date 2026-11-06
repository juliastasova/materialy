# Řešení bonusu 3 – Debugger
# Opravený program. Pod ním jsou všechny tři chyby popořadě.

def zaloha_z(castka):
    return round(castka / 3)


osoby = 4
clenky = 2
cena_osoby = 2400

celkem = osoby * cena_osoby

if osoby >= 3:
    celkem = celkem * 0.9

celkem = celkem - clenky * 200

zaloha = zaloha_z(celkem)

print(f"Osob: {osoby}, z toho členek: {clenky}")
print(f"Celkem: {celkem:.0f} Kč")
print(f"Záloha: {zaloha} Kč")


# 1. NameError: name 'cena_osoba' is not defined.
#    Proměnná se jmenuje cena_osoby. Python správné jméno sám
#    nabídl na konci hlášky.
#
#    Po opravě program doběhne a vypíše celkem 8 440 Kč
#    a zálohu 3 200 Kč. Obojí je špatně.
#
# 2. Celkem mělo vyjít 8 240, vyšlo 8 440 – rozdíl 200 Kč.
#    Členky jsou dvě, takže sleva má být 2 × 200. V programu
#    se odečítalo jen plochých 200 Kč bez ohledu na jejich počet.
#
#    Po opravě sedí celkem 8 240 Kč. Záloha je pořád 3 200.
#
# 3. Třetí chyba je ta nepříjemná. Funkce zaloha_z je v pořádku –
#    breakpoint uvnitř ní to ukáže hned: dostane castku a vydělí ji
#    třemi.
#    Jenže dostane 9 600, ne 8 240.
#
#    Breakpoint na řádek s voláním a pohled do panelu Variables:
#    celkem je v tu chvíli 9 600, protože slevy se počítají
#    až pod tím řádkem. Záloha se tedy počítala z ceny před
#    slevami.
#
#    Funkce byla celou dobu správně. Špatně bylo místo, odkud
#    se volala.
