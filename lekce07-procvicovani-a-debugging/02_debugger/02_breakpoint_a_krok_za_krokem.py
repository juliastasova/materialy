# ---------------------------------------------
#  Breakpoint a krok za krokem
# ---------------------------------------------
# Kámen, nůžky, papír možná znáš z bonusu ve čtvrté lekci. Tahle
# verze navíc uklidí, co uživatelka napíše, a o výsledku rozhodují
# vlastní funkce.
#
# Spusť ho a napiš kamen.

from random import randrange


def uklid_vstupu(text):
    return text.strip().title()


def tah_pocitace():
    cislo = randrange(1, 4)
    if cislo == 1:
        return "kamen"
    elif cislo == 2:
        return "nuzky"
    else:
        return "papir"


def je_platny(tah):
    return tah == "kamen" or tah == "nuzky" or tah == "papir"


def kdo_vyhral(tvuj, pocitacuv):
    if tvuj == pocitacuv:
        return "remiza"
    vyhrala_kamenem = tvuj == "kamen" and pocitacuv == "papir"
    vyhrala_nuzkami = tvuj == "nuzky" and pocitacuv == "papir"
    vyhrala_papirem = tvuj == "papir" and pocitacuv == "kamen"
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


# Napsala jsi kamen a program odpověděl "Takový tah neznám."
# Přitom kamen mezi tahy patří.
#
# Rozhoduje o tom funkce je_platny na řádku 27. Ta vypadá v pořádku –
# porovnává vstup se všemi třemi tahy. Zajímavější je, co do ní
# vlastně přišlo.


# ----- Breakpoint -----
#
# 1. Klikni do šedého pruhu vlevo od čísla řádku 28. Objeví se
#    červená tečka – to je breakpoint. Může být i uvnitř funkce:
#    program se na něm zastaví pokaždé, když se funkce zavolá.
#    (Ukazuje to obrázek debugger_breakpoint.png.)
#
# 2. Nespouštěj soubor tlačítkem Run. Vedle něj je šipka dolů.
#    Klikni na ni a vyber "Python Debugger: Debug Python File".
#    Jde to i klávesou F5.
#    (Ukazuje to obrázek debugger_spusteni.png.)
#
#    Při prvním spuštění se tě VS Code může zeptat, co vlastně má
#    spustit. Nabídne seznam a v něm vyber "Python File". Příště
#    už se neptá.
#
#    Když v nabídce není nic s Pythonem, chybí rozšíření Python
#    z první lekce. Doinstaluj ho a zkus to znovu.
#
# 3. Napiš do terminálu kamen. Program se zastaví na řádku 28,
#    ten zežloutne a vlevo se otevře panel Variables.
#    (Ukazuje to obrázek debugger_zastaveno.png.)
#
# V panelu je:
#
#   tah = 'Kamen'
#
# Velké K. Napsala jsi malé písmeno a do funkce přišlo velké, takže
# se tah nerovná ani jednomu ze tří. Všimni si uvozovek – panel
# ukazuje hodnotu přesně tak, jak ji Python má.
#
# Vstup se uklízí na řádku 14 a je tam title(), která změní první
# písmeno na velké. Patří tam lower(). Oprav to a spusť znovu.


# ----- Tlačítka -----
#
# Nahoře uprostřed, nad kódem, se objevil pruh se šesti tlačítky.
# Zleva:
#
#   1. Continue (modrá šipka s čárkou) – program běží dál až
#      k dalšímu breakpointu. Když už žádný nepřijde, doběhne.
#   2. Step Over (oblouk s tečkou) – provede jeden řádek a zastaví
#      se na dalším. Volání funkce provede celé najednou.
#   3. Step Into (šipka dolů do tečky) – když se na řádku volá
#      funkce, vejde do ní a zastaví se na jejím prvním řádku.
#   4. Step Out (šipka nahoru od tečky) – dokončí funkci, ve které
#      zrovna jsi, a zastaví se tam, odkud se volala.
#   5. Restart (zelená kolečková šipka) – spustí program znovu
#      od začátku.
#   6. Stop (červený čtvereček) – program ukončí.
#
# (Celý pruh zblízka ukazuje obrázek debugger_tlacitka.png.)


# ----- Krok za krokem -----
#
# Teď už hra běží. Zahraj několikrát za sebou kamen a dívej se
# na výsledky. Dřív nebo později uvidíš tohle:
#
#   Ty hraješ: kamen
#   Počítač hrál: nuzky
#   Prohrála jsi.
#
# Jenže kámen tupí nůžky. Tohle kolo jsi vyhrála.
#
# Rozhoduje funkce kdo_vyhral. Dej breakpoint na řádek 34, spusť
# program přes Python Debugger a zahraj kamen.
#
# Když počítač zahraje taky kamen, je to remíza. Funkce skončí už
# na řádku 33, k breakpointu se nedostane a program doběhne. Spusť
# ho znovu. Chyba, která se projeví jen někdy, se hledá opakováním.
#
# Když počítač zahraje nuzky, program se zastaví na řádku 34.
# Mačkej Step Over a po každém zmáčknutí se podívej do panelu,
# co přibylo:
#
#   tvuj = 'kamen'              sedí, to jsi napsala
#   pocitacuv = 'nuzky'         sedí, to padlo počítači
#   vyhrala_kamenem = False     nesedí
#   vyhrala_nuzkami = False
#   vyhrala_papirem = False
#
# Kámen proti nůžkám je výhra, takže vyhrala_kamenem má být True.
# Přečti si řádek 34: ptá se, jestli počítač hrál papir. Kámen ale
# poráží nůžky, ne papír.
#
# Oprav na řádku 34 "papir" na "nuzky" a zahraj si znovu.


# ----- Víc breakpointů najednou -----
#
# Nech si breakpoint na řádku 34 a přidej ještě jeden na řádek 28.
# Po spuštění se program zastaví nejdřív na osmadvacítce, a když
# zmáčkneš Continue, skočí na čtyřiatřicítku.
#
# Když je breakpoint uvnitř cyklu, zabere v každém průchodu znovu.
# Continue tě tam posune vždycky o jedno kolo dál.
#
# Breakpoint zrušíš dalším kliknutím na červenou tečku.
