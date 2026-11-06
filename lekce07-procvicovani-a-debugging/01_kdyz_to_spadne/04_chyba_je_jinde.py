# ---------------------------------------------
#  Hláška ukazuje, kde to Python poznal
# ---------------------------------------------
# Spusť soubor. Spadne – a tentokrát na řádku, kde je všechno
# napsané správně.

jablka = 5
hruksy = 3
cena_jablka = 12
cena_hrusky = 15

print("Počítám nákup...")

za_jablka = jablka * cena_jablka
za_hrusky = hrusky * cena_hrusky

print(f"Celkem: {za_jablka + za_hrusky} Kč")


# Hláška:
#
#   Počítám nákup...
#   Traceback (most recent call last):
#     File "04_chyba_je_jinde.py", line 15, in <module>
#       za_hrusky = hrusky * cena_hrusky
#                   ^^^^^^
#   NameError: name 'hrusky' is not defined. Did you mean: 'hruksy'?
#
# Řádek 15 je napsaný správně. Chyba je na řádku 8: proměnná se tam
# omylem jmenuje hruksy. Python o ní ví, ale pod tímhle jménem,
# takže na řádku 15 žádné hrusky nenajde.
#
# V minulém souboru ti hláška ukázala celou cestu – tři patra, odkud
# kam. Tady ukáže jediný bod: místo, kde to Python poznal. Odtud
# musíš hledat sama.
#
# Pomůže konec hlášky: "Did you mean: 'hruksy'?" Python našel podobné
# jméno a nabízí ho. U překlepů trefí skoro vždycky, takže tahle část
# stojí za přečtení.
#
# NameError znamená skoro vždycky jedno ze dvou:
#   - překlep ve jméně proměnné (jako tady),
#   - nebo proměnná ještě neexistuje, protože řádek, kde vzniká,
#     je až pod tím, kde ji používáš.
#
# Oprav řádek 8 na hrusky = 3 a spusť znovu.
