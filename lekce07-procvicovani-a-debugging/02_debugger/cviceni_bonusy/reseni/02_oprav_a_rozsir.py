# Řešení bonusu 2 – Debugger
# Tvoje řešení může vypadat jinak, a to je v pořádku.

veta = "Python je jazyk pro lidi a stroje"
samohlasky = "aeiouy"

pocet_samohlasek = 0
pocet_souhlasek = 0

for znak in veta.lower():
    if znak == " ":
        continue
    if znak in samohlasky:
        pocet_samohlasek = pocet_samohlasek + 1
    else:
        pocet_souhlasek = pocet_souhlasek + 1

pocet_pismen = pocet_samohlasek + pocet_souhlasek
podil = pocet_samohlasek / pocet_pismen * 100

print(f"Samohlásek: {pocet_samohlasek}")
print(f"Souhlásek: {pocet_souhlasek}")
print(f"Samohlásky tvoří {podil:.1f} % písmen.")


# Souhlásek vycházelo 27, což je počet všech písmen ve větě.
# To samo napovídá, že se počítadlo souhlásek zvyšuje pokaždé,
# i u samohlásky.
#
# Chybělo else. Bez něj jsou ty dva ify nezávislé: první se ptá
# na samohlásku, druhý se nezeptá na nic a přičte vždycky.
