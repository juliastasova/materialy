# ---------------------------------------------
#  Když se nespustí vůbec nic
# ---------------------------------------------
# Spusť soubor. Nevypsalo se ani "Začínám" – přestože je to
# první řádek programu.

print("Začínám")

cena = 100
print(f"Cena: {cena} Kč)

print("Hotovo")


# Hláška:
#
#     File "02_nespustilo_se_vubec.py", line 10
#       print(f"Cena: {cena} Kč)
#             ^
#   SyntaxError: unterminated f-string literal (detected at line 10)
#
# Za Kč chybí uzavírací uvozovka. Python text začal číst a nenašel,
# kde končí.
#
# Zajímavější je, co se nevypsalo. "Začínám" je na řádku 7, je
# napsané správně, a přesto se neobjevilo.
#
# Některé chyby totiž Python najde ještě předtím, než program spustí.
# Nejdřív si přečte celý soubor, a když mu jeden řádek nedává smysl,
# nespustí vůbec nic. Takové chyby jsou dvě: SyntaxError (špatně
# napsaný řádek) a IndentationError (špatné odsazení).
#
# Všimni si, že VS Code ten řádek podtrhl červeně, ještě než jsi
# soubor spustila. Pozná to ze stejného důvodu.
#
# Chyby za běhu jsou ten druhý druh – jako TypeError z minulého
# souboru. Tam se "Jméno: Anna" vypsalo a teprve pak to spadlo.
# Program doběhl až k chybnému řádku, takže všechno nad ním
# se opravdu stalo.
#
# Proto se u každého spadlého programu vyplatí mrknout, jestli se
# vypsalo vůbec něco. Když ne, je chyba v zápisu.
#
# Doplň uvozovku za Kč a spusť znovu.
