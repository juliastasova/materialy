# ---------------------------------------------
#  Když to spadne ve funkci
# ---------------------------------------------
# Spusť soubor. První průměr se spočítá, druhý shodí program.

def prumer(soucet, pocet):
    return soucet / pocet


def vypis_prumer(nazev, soucet, pocet):
    vysledek = prumer(soucet, pocet)
    print(f"{nazev}: {vysledek:.1f}")


vypis_prumer("Leden", 120, 4)
vypis_prumer("Únor", 0, 0)


# Hláška má tentokrát tři patra:
#
#   Leden: 30.0
#   Traceback (most recent call last):
#     File "03_spadlo_to_ve_funkci.py", line 16, in <module>
#       vypis_prumer("Únor", 0, 0)
#       ~~~~~~~~~~~~^^^^^^^^^^^^^^
#     File "03_spadlo_to_ve_funkci.py", line 11, in vypis_prumer
#       vysledek = prumer(soucet, pocet)
#     File "03_spadlo_to_ve_funkci.py", line 7, in prumer
#       return soucet / pocet
#              ~~~~~~~^~~~~~~
#   ZeroDivisionError: division by zero
#
# Odspodu: dělení nulou se stalo na řádku 7, uvnitř funkce prumer.
# O patro výš je vidět, kdo prumer zavolal – funkce vypis_prumer
# z řádku 11. A nahoře řádek 16, odkud to celé začalo.
#
# "most recent call last" znamená, že nejspodnější patro je to
# poslední a nejhlubší.
#
# Spadlo to na řádku 7, ale chyba tam není. Dělení dvou čísel je
# napsané správně a pro leden fungovalo. Problém vznikl na řádku 16:
# tam někdo poslal jako počet nulu. To nejvrchnější patro bývá řádek,
# který jsi psala ty – a tam bývá i chyba.
#
# Změň řádek 16 na vypis_prumer("Únor", 90, 3) a spusť znovu.
