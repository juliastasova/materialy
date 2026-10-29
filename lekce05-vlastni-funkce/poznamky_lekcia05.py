# Funkcie 
# premenná je škatulka, kde si uložím hodnotu - a potom ju môžem použiť znovu. premenná by mala byť deskriptívna

# keď sú niekde zátvorky, tak viem, že je to funkcia
# do funkcie môžeme poslať premennú a ona s ňou potom niečo urobí
# funkcia nemusí vždy mať nejaký vstup 

# vek_uzivatele = 1
# print(vek_uzivatele)

#  neustále opakovanie môžeme zmeniť cez cyklus

# definovanie max hodnoty - naša vlastná funkcia
#  odsadenie zátvorky a čo robí

# definícia funkcie
# True v def funkcii znamená, že je voliteľný parameter - iba ak zadáme false tak sa nepustí
# musí to byť vždycky posledná položka - iba tak môže veriť poradiu
# nemôže byť parameter s východziou hodnotou
def vypis_cisla_do_max_hodnoty(max_hodnota, jmeno_volani, ukaz_caru=True):
    for aktualni_cislo in range(1, max_hodnota):
        print(jmeno_volani, ":", str(aktualni_cislo))
    if ukaz_caru:
        print("-" * 30)
# toto je len definícia funkcie, keď toto spustíme v termináli nebude nič
# pretože je to len definovanie funkcie a nie jej zavolanie
# v zátvorke funkcie v def musíme dať hodnoty

# volanie funkcie
vypis_cisla_do_max_hodnoty(10, "volani A", True)
vypis_cisla_do_max_hodnoty(100, "volani B", True)
vypis_cisla_do_max_hodnoty(1000, "volani C", False)

# rozumieť rozdiel definícia vs. volanie
# nedajú sa sčitovať reťazce s 


# max_hodnota = 10

# for cislo in range(1, 11):
#     print("Aktualni cislo je:", cislo)

# for cislo in range(1, 100):
#     print("Aktualni cislo je:", cislo)

# for cislo in range(1, 1000):
#     print("Aktualni cislo je:", cislo)

#  návratové hodnoty

cislo_od_uzivatele = input("zadej cislo") # z inputu nám niečo vypadne, môžeme si doň uložiť číslo

def cena_mhd(vek):
    print("pocitam cenu listku pro vek", vek)
    
    if vek < 6:
        return 0
    elif vek < 18:
        return 39
    elif vek < 65:
        return 50
    else:
        return 0

zustatek_uctu = 1000

cena_jizdenky = cena_mhd(7) # priraďujem to, čo volanie funkcie vráti - spočítaj cenu jízdenky pro 7 a ulož do premennej cena jízdenky

print("cena jizdenky je: ")

cena_jizdenky = cena_jizdenky * 1.5

zustatek_uctu = zustatek_uctu - cena_jizdenky
