#  funkcie, ktoré iba niečo urobia
print("Ahoj", "Anno", 2025)     # Ahoj Anno 2025
print("Ahoj", end=" ")
print("světe")                  # Ahoj světe
print(2, 3, 4, sep=", ")        # 2, 3, 4

# funkcie, ktoré nám aj niečo vrátia
#odpoved = input("Kolik ti je let? ")   # input vrátí text, třeba "30"
#vek = int(odpoved)                     # int z textu udělá číslo 30
#print("Za rok ti bude", vek + 1)

# funkcia length - počet znakov
print(len("PyLadies"))    # 8

#  s len môžeme ďalej aj počítať:
delka = len("kolo")
print(delka + 1)      # 5

# abs - vypíše absolútnu hodnotu
print(abs(-7))        # 7
print(abs(7))         # 7
print(abs(3 - 10))    # 7   z -7 udělá 7

# round - zaokrúhli, ďalší argument je na koľko desatinných miest
print(round(3.14159, 2))  # 3.14   dvě desetinná místa

#  min a max - minimum a maximum z nejakého intervalu

#  range - posledné číslo už nepočíta
print(sum(range(1, 5)))   # 10   sečte 1 + 2 + 3 + 4

# cyklus for
# prechádzanie textu
for cislo in range(3):
    print("Ahoj")
#  for je klíčové slovo pro opakování.
#  cislo je proměnná, do které cyklus postupně ukládá čísla z range.
#  range(3) určuje, která čísla projdeme, a tím i počet opakování.
#  : je dvojtečka na konci řádku, stejně jako u if.
#  Odsazené řádky patří dovnitř cyklu a opakují se.
for cislo in range(5):
    print(cislo)          # vypíše 0, 1, 2, 3, 4 – každé na svůj řádek

# range s krokem: range(od, do, krok) – o kolik se skáče. Tímhle vypíšeme sudá čísla:
for cislo in range(0, 10, 2):
    print(cislo)              # 0, 2, 4, 6, 8
# Důležité: co je odsazené, patří dovnitř cyklu a opakuje se. Co je pod cyklem BEZ odsazení, se provede až potom – jednou.
for cislo in range(3):
    print("uvnitř cyklu:", cislo)
print("hotovo")              # vypíše se jednou, až cyklus doběhne

# zbieranie výsledkov v cykle:
soucet = 0
for cislo in range(1, 6):
    soucet = soucet + cislo   # k dosavadnímu součtu přičti aktuální číslo
print(soucet)                 # 15   protože 1 + 2 + 3 + 4 + 5

# počítadlo:
pocet = 0
for cislo in range(10):
    pocet = pocet + 1
print("cyklus proběhl", pocet, "krát")    # 10


# násobenie - musíme ostať vždy na 1, inak by nám vždy dalo 0
soucin = 1
for cislo in range(1, 5):
    soucin = soucin * cislo
print(soucin)                 # 24

#  vnorené cykly
for kolo in range(1, 4):
    print("Kolo", kolo)
    for pokus in range(1, 3):
        print("  pokus", pokus)

#  zalomenie na riadok:
for tyden in range(1, 4):
    for den in range(1, 8):
        print(den, end=" ")       # dny 1 až 7 vedle sebe
    print()                       # po celém týdnu skoč na nový řádek

#  prechádzanie textu:
slovo = "Ahoj"
for pismeno in slovo:
    print(pismeno)        # A, h, o, j – každé na svůj řádek
    
# podmienka vrámci cyklu for:
pocet = 0
for cislo in range(1, 21):
    if cislo % 2 == 0:
        pocet = pocet + 1
print("sudých čísel:", pocet)     # 10

slovo = "ananas"
samohlasky = 0
for pismeno in slovo:
    if pismeno in "aeiou":
        samohlasky = samohlasky + 1
print("samohlásek:", samohlasky)  # 3