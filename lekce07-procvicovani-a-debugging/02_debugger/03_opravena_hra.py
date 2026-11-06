# ---------------------------------------------
#  Opravená hra a pojmenované tahy
# ---------------------------------------------
# Tohle je hra z minulého souboru s opravenými chybami. Porovnej si
# ji se svojí verzí – a všimni si tří řádků nahoře, které tam dřív
# nebyly.

from random import randrange

KAMEN = "kamen"
NUZKY = "nuzky"
PAPIR = "papir"


def uklid_vstupu(text):
    return text.strip().lower()


def tah_pocitace():
    cislo = randrange(1, 4)
    if cislo == 1:
        return KAMEN
    elif cislo == 2:
        return NUZKY
    else:
        return PAPIR


def je_platny(tah):
    return tah == KAMEN or tah == NUZKY or tah == PAPIR


def kdo_vyhral(tvuj, pocitacuv):
    if tvuj == pocitacuv:
        return "remiza"
    vyhrala_kamenem = tvuj == KAMEN and pocitacuv == NUZKY
    vyhrala_nuzkami = tvuj == NUZKY and pocitacuv == PAPIR
    vyhrala_papirem = tvuj == PAPIR and pocitacuv == KAMEN
    if vyhrala_kamenem or vyhrala_nuzkami or vyhrala_papirem:
        return "vyhra"
    else:
        return "prohra"


tvuj_tah = uklid_vstupu(input("Tvůj tah (kamen/nuzky/papir): "))

if not je_platny(tvuj_tah):
    print("Takový tah neznám.")
else:
    pocitacuv_tah = tah_pocitace()
    print(f"Ty hraješ: {tvuj_tah}")
    print(f"Počítač hrál: {pocitacuv_tah}")

    vysledek = kdo_vyhral(tvuj_tah, pocitacuv_tah)
    if vysledek == "vyhra":
        print("Vyhrála jsi!")
    elif vysledek == "remiza":
        print("Remíza.")
    else:
        print("Prohrála jsi.")


# Opravené jsou dvě věci: na řádku 16 je lower() místo title()
# a na řádku 36 nůžky místo papíru.
#
# Třetí změna je nahoře, na řádcích 10 až 12. Tahy se dřív psaly
# jako text v uvozovkách pokaždé znovu – dohromady dvanáctkrát.
# Teď jsou uložené v proměnných a všude jinde se používá jméno.
#
# Velká písmena jsou zvyk. Říkají, že tahle hodnota se v programu
# už nemění. Takové proměnné se říká konstanta.


# ----- Proč to stojí za to -----
#
# Zkus si do nějakého porovnání schválně napsat NUZKI a spustit to:
#
#   NameError: name 'NUZKI' is not defined. Did you mean: 'NUZKY'?
#
# Python překlep našel sám a rovnou poradil. Ve jméně proměnné
# si ho všimne, protože žádná taková proměnná neexistuje.
#
# A teď totéž s uvozovkami. Napiš do porovnání "nuzki" a spusť to.
# Žádná hláška. Program poběží dál a jen bude mlčky odpovídat
# špatně – a to je přesně ten druh chyby, který jsi v minulém
# souboru hledala debuggerem.
#
# Stejný překlep, úplně jiné hledání. S konstantou ho najde Python
# za tebe.


# ----- Co to neumí -----
#
# Naše původní chyba by prošla dál i s konstantami. Na řádku 36
# bylo PAPIR tam, kde patří NUZKY – a obě ty proměnné existují,
# takže by si Python nestěžoval.
#
# Konstanty hlídají překlepy, ne špatně vybrané hodnoty.
#
# Stejným způsobem by se daly pojmenovat i výsledky "vyhra",
# "remiza" a "prohra", které se v programu opakují taky.
