# Bonus 2 – Debugger
# Nejdřív chybu najdi a oprav, pak program rozšiř.

# Program počítá, kolik je ve větě samohlásek a kolik souhlásek.
# Mezery se nepočítají.
#
# Samohlásky a souhlásky dohromady musí dát počet písmen ve větě.
# Zkontroluj, jestli to tak vychází.
#
# 1. Najdi a oprav chybu.
# 2. Pak přidej výpis, kolik procent ze všech písmen jsou
#    samohlásky, zaokrouhleno na jedno desetinné místo.

veta = "Python je jazyk pro lidi a stroje"
samohlasky = "aeiouy"

pocet_samohlasek = 0
pocet_souhlasek = 0

for znak in veta.lower():
    if znak == " ":
        continue
    if znak in samohlasky:
        pocet_samohlasek = pocet_samohlasek + 1
    pocet_souhlasek = pocet_souhlasek + 1

print(f"Samohlásek: {pocet_samohlasek}")
print(f"Souhlásek: {pocet_souhlasek}")
