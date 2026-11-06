# Řešení cvičení 1 – Debugger
# Opravený program. Pod ním jsou obě chyby popořadě.

def prumer(test1, test2, test3):
    return (test1 + test2 + test3) / 3


def slovni_znamka(body):
    if body >= 90:
        return "výborně"
    elif body >= 75:
        return "chvalitebně"
    elif body >= 60:
        return "dobře"
    elif body >= 45:
        return "dostatečně"
    else:
        return "nedostatečně"


def prospel(znamka):
    if znamka == "nedostatečně":
        return "neprospěl"
    else:
        return "prospěl"


def vysvedceni(jmeno, test1, test2, test3):
    body = prumer(test1, test2, test3)
    znamka = slovni_znamka(body)
    return f"{jmeno}: {body:.1f} bodů, {znamka}, {prospel(znamka)}"


print(vysvedceni("Jana", 40, 35, 45))
print(vysvedceni("Petr", 95, 88, 91))
print(vysvedceni("Klára", 88, 91, 91))


# Chyba 1 – Jana
#
# "nedostatečně, prospěl" si odporuje. Body a známka spolu přitom
# sedí: 40 bodů je míň než 45, takže prumer i slovni_znamka
# počítají správně. Zbývá prospel.
#
# Dej breakpoint na první řádek funkce prospel a spusť program přes
# Python Debugger. V panelu Variables je:
#
#   znamka = 40.0
#
# Parametr se jmenuje znamka, ale je v něm číslo. Porovnání
# 40.0 == "nedostatečně" nikdy neplatí, takže funkce pokaždé vrátí
# "prospěl".
#
# Sama funkce je v pořádku. Chyba je na řádku, odkud se volá:
# ve vysvedceni dostane body místo znamka.
#
#
# Chyba 2 – Klára
#
# Klára má přesně 90 bodů a podle stupnice to je výborně. Program
# ale vypsal chvalitebně.
#
# Dej breakpoint dovnitř slovni_znamka a pak zmáčkni Step Over přes
# první if: v panelu je body = 90.0 a žlutý řádek přeskočí rovnou
# na elif.
# Podmínka body > 90 pro devadesátku neplatí.
#
# Ve stupnici stojí "90 a víc", takže tam patří >=. Zbylé tři
# podmínky ho mají správně, vypadlo jen z té první.
#
#
# U Petra přitom vycházelo všechno správně. Program, který dá dobrý
# výsledek pro jeden vstup, tím ještě není ověřený.
