# ---------------------------------------------
#  Metody za sebou
# ---------------------------------------------
# Spusť soubor a zkus různé odpovědi: ano, ANO, nebo ano s mezerou.
#
# V lekci 2 jsi odpověď porovnávala přímo:
#   if odpoved == "ano":
# Taková podmínka projde jen u přesně napsaného "ano". "ANO" ani " ano "
# už neprojdou, i když uživatelka myslela to samé.

odpoved = input("Chceš pokračovat? (ano/ne) ")


# Nejdřív po krocích, tak jak bys to napsala dneska:
bez_mezer = odpoved.strip()         # zmizí mezery na krajích
upravena = bez_mezer.lower()        # vzniknou malá písmena

print(f"[{upravena}]")

if upravena == "ano":
    print("Pokračujeme.")
else:
    print("Končíme.")


# Protože strip() vrací řetězec, dá se lower() zavolat rovnou na jeho
# výsledku a obě metody napsat na jeden řádek. Vyhodnocuje se to zleva
# doprava, takže vyjde to samé:
zkracene = odpoved.strip().lower()

print(f"[{zkracene}]")

# Takhle zkráceně se to píše nejčastěji.
