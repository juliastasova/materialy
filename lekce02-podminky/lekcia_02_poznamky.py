vek = 15

if vek >= 18:
    print("Jsi plnoletá.")
    print("Můžeš volit.")
    
#podmienky s if
# použiť tab (osadenie), pre veci, ktoré patria do if


# podmienky s if-else
teplota = 5

if teplota > 15:
    print("Je hezky, jde se ven.")
else:
    print("Radši si vezmi bundu.") # pozor na chybu - zabudnutie osadenia
    
# ak riadok nie je osadený, s pomocou print sa vypíše vždy:
if teplota > 15:
    print("Tohle jen když je teplo.")
print("Tohle se vypíše vždycky.")
# riadky musia byť vždy osadené rovnako, najlepšie tabulátorom. ak nebudú, vypíše indentation error
if vek >= 18:
    print("Jsi plnoletá.")
    print("Můžeš volit.")     # IndentationError!
        
     
# elif - ak mám viac, ako 2 podmienky   
    
znamka = 2

if znamka == 1:

    print("Výborně!")
elif znamka == 2:
    print("Chvalitebně.")
elif znamka == 3:
    print("Dobře.")
else:
    print("Příště to půjde líp.")
    
#Python zkouší podmínky odshora dolů a zastaví se u PRVNÍ, která platí. Její větev spustí a zbytek přeskočí. Proto se vždycky spustí nejvýš jedna větev.

#else je nepovinné. Když ho vynecháš a žádná podmínka neplatí, neudělá se prostě nic:
teplota = 10

if teplota < 0:
    print("Mrzne.")
elif teplota < 15:
    print("Chladno.")
elif teplota < 25:
    print("Příjemně.")

# if vnútri if - môžu sa dať aj jedno do druhého
# if můžeš dát dovnitř jiného if. Hodí se, když chceš něco ověřit TEPRVE potom, co platí něco jiného. Vnitřní blok jen odsadíš ještě o kus dál.

venku_prsi = True
mam_destnik = False

if venku_prsi:
    print("Venku prší.")
    # Tenhle if řešíme jen tehdy, když prší:
    if mam_destnik:
        print("Naštěstí mám deštník.")
    else:
        print("A nemám deštník – zmoknu.")
else:
    print("Je sucho, pohoda.")
    
#Kdy vnořený if a kdy elif?

#elif se hodí, když se rozhoduješ mezi možnostmi JEDNÉ otázky (jaká je známka? jaká je teplota?) – platí právě jedna větev.

#Vnořený if se hodí, když se ptáš na DVĚ různé věci za sebou a druhá má smysl jen podle výsledku první (prší? a když prší, mám deštník?).

# Podmienka na vstup od užívateľa
strana = float(input("Zadej stranu čtverce v centimetrech: "))

if strana > 0:
    print("Obvod je", 4 * strana, "cm")
    print("Obsah je", strana * strana, "cm²")
else:
    print("Strana musí být kladné číslo.")
    
# spojovanie podmienok - and, if or, not
vek = 25
print(vek >= 18 and vek < 65)   # True – je zároveň dospělý i mladší 65

den = "sobota"
print(den == "sobota" or den == "neděle")   # True – je to víkend

a = 5
b = -2

if a <= 0 or b <= 0:
    print("Strany musí být kladné.")
else:
    print("Obvod je", 2 * (a + b))
    
#Pozor: and/or spojují CELÉ podmínky, ne holá čísla. Všimni si, že nahoře máme porovnání dvakrát – zvlášť pro a a zvlášť pro b:
x = 12
y = 25
z = 8

if x >= y and x >= z:
    print("Největší je", x)
elif y >= x and y >= z:
    print("Největší je", y)
else:
    print("Největší je", z)

# otočenie podmienky - not   
#not znamená „ne". Otočí hodnotu naruby: z True udělá False a naopak. Hodí se, když chceš reagovat na to, že něco NEPLATÍ.
print(not True)     # False
print(not False)    # True

prsi = False
print(not prsi)    # True – „neprší"

# typické použitie - reagivať na opak
prihlaseny = False

if not prihlaseny:
    print("Nejprve se přihlas.")

heslo_ok = True
jmeno_ok = False
print(heslo_ok and jmeno_ok)        # False
print(not (heslo_ok and jmeno_ok))  # True

if not (heslo_ok and jmeno_ok):
    print("Přihlášení selhalo.")
# Čti to jako „není pravda, že platí heslo i jméno zároveň". Závorka je důležitá – řekne Pythonu, co přesně má not otočit.

#### najviac striktná podmienka musí byť na začiatku, pozor na toto!!
#