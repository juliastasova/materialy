# Řešení bonusu 2 – Metody řetězců
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# Zeptej se na heslo a zkontroluj tři věci:
#    je aspoň osm znaků dlouhé, je v něm aspoň jedna číslice
#    a je v něm aspoň jedno velké písmeno.
#
#    Ke každé podmínce vypiš, jestli prošla. Na konec vypiš, jestli
#    je heslo přijaté – to je, jen když prošly všechny tři.
#
#    Na číslici se zeptáš průchodem přes znaky: cyklus for z lekce 3
#    a isdigit() na každý znak.
#    Na velké písmeno stačí porovnat heslo se sebou samým po lower().
#    Jde to ale i cyklem jako u číslice – každého znaku se tam zeptáš
#    metodou isupper().

heslo = input("Zadej heslo: ")

dost_dlouhe = len(heslo) >= 8

# lower() vrací nový řetězec, původní heslo nemění. Když se ty dva
# od sebe liší, muselo v hesle být velké písmeno – jinak by lower()
# vrátil přesně to samé.
ma_velke = heslo != heslo.lower()

# isdigit() na celém hesle by se ptalo, jestli jsou číslice všechny
# znaky. Tady potřebuješ vědět, jestli je číslice aspoň jedna – proto
# cyklus. Break ho ukončí, jakmile je jasno.
ma_cislici = False
for znak in heslo:
    if znak.isdigit():
        ma_cislici = True
        break

print(f"Aspoň osm znaků:  {dost_dlouhe}")
print(f"Obsahuje číslici: {ma_cislici}")
print(f"Velké písmeno:    {ma_velke}")

if dost_dlouhe and ma_cislici and ma_velke:
    print("Heslo přijato.")
else:
    print("Heslo nevyhovuje.")


# Velké písmeno jde hledat i cyklem, úplně stejně jako číslici – jen
# se každého znaku ptáš metodou isupper(). Je to delší, zato je na
# první pohled vidět, co se hledá:
ma_velke_cyklem = False
for znak in heslo:
    if znak.isupper():
        ma_velke_cyklem = True
        break

print(f"Velké písmeno (cyklem): {ma_velke_cyklem}")

# Obě řešení jsou správně.
