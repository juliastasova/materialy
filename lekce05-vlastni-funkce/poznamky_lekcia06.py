# Reťazce
# reťazce sa začínajú a končia úvodzovkami
vek = int(input("zadaj svoj vek: "))
# imput iba vracia reťazce a nie čísla
print(vek + vek)
print("za 10 rokov budeš mať", int(vek) + 10)

print(len(vek))

if "Petr" in vek:
    print("mas v mene slovo Petr")
else:
    print("nemas v mene slovo Petr")

#  nemusím pozerať len na jeden znak, ale aj viac písmen/slov?

# prechádzanie reťazcom - vytlačí písmeno jedno po druhom
for pismeno in meno:
    print(pismeno)

vek = 30 

print("Je mi", vek, "let")

# koncept F string - nemusím prevádzať z textu na čísla a naopak - zase skončí ako reťazec
print(f"Jsem (meno) a je mi (vek)")

kniha = "Maly princ"
stran_celkem = 320
precteno = 183
print(f"V (kniha) zbyva (stran_celkem - precteno) do konce")

def procenta(cast, celek):
    return cast/celek * 100
print(f"mas procteno (procenta(precteno - stran_celkem):.2f) stran knihy")

#  :.2f - zaokrúhli na 2 des miesta

# špeciálne znaky v texte 
#\n nový riadok:
print("Ahoj\nTomasi")

#\t - tabulátor(odsadenie):

#\"Tomasi"\ úvodzovky v reťazci
# alebo ôžem použiť aj dvojo rôznych úvodzoviek
# tiež môže byť tripple úvodzoky: keď vo funkcii urobím enter, formátuje sa to podľa toho
print("""Ahoj Tomasi""")

#####################################################
############ metódy na volanie reťazcov #############
#####################################################
# napríklad len:
print(len("sjdfhjhdsfbfbhd"))
# toto je volanie funkcie na reťazec

# volanie je v opačnom poradí - reťazec má v sebe zabalené metódy, ktoré si volá
print("pyladies".upper())
print("PYLADIES".lower())

print("PYLADIES".count())

print("ahoj adame".lower().count("a"))
#pozor - veľké A je niečo než malé a, najprv previesť na malé písmená a až potom spočítať

veta = "Ahoj Adame"
zmensena = veta.lower()
pocet_a = zmensena.count("a")

# find and replace v texte 
veta = "AHoj Adame"
lepsi_veta = veta.replace("Ahoj", "Dobrý den")

print(lepsi_veta)

# funkcia, čo sa pýta na email a chcem ho zmenšiť a vrátiť zmenšené
def zeptat_se_na_email():
    return input("napis email").lower()

# vytvorí sa nový reťazec, takže adam sa vypíše všetko s malým
jmeno = "adam"
velke_jmeno = jmeno.upper()
print(jmeno)

# potrebujeme zistiť, či reťazec je číslo ešte predtým, než ho prevádzame na číslo
vek = input("zadej vek")
if vek.isdigit():
    print("za 10 let ti bude", int(vek) + 10)
else:
    print("pises blbosti")

# vytlačiť napr len prvé 2 písmená zo slova
slovo = "PyLadies"
print(slovo[7])
# vytiskne siedme písmeno, začína sa od nuly
# ale dĺžka by bola 8, lebo 0 je 1 znak
print(slovo[len(slovo)-1])

# v mínuskách začíname na 1, python vie aj záporné čísla, ide od -1 do -8
print(slovo[-1])

# range - od nuly do indexu 2 aleb bez indexu ako takého - tak isté intervaly ako u range, neobsahuje poslednú časť/definíciu intervalu
print(slovo[0:2])

# posledné 3 písmená
print(slovo[-3:])
# posledné 3 písmená - znamená to isté, ako to nad tým
print(slovo[-3:-1])

# prehodiť slovo a potom ísť do konca: o krok, o ktorý sa preskakuje (o 1 extra písmeno)
print(slovo[::-1])

# error, lebo reťazec sa neupravuje, jednotlivé pozície nemôžem upravovať ale môžem ich rozseknúť
slovo = "ahoj"
slovo[0] = "B" + slovo[1:]
print(slovo[0])