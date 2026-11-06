# Cvičení 1 – Debugger
# Spusť soubor (Run). Dvě ze tří vysvědčení jsou špatně. Najdi
# debuggerem obě chyby a oprav je.

# Program vypíše vysvědčení: spočítá průměr ze tří testů, přeloží
# ho na slovní známku a připíše, jestli student prospěl.
#
# Stupnice:
#   90 bodů a víc    výborně
#   75 a víc         chvalitebně
#   60 a víc         dobře
#   45 a víc         dostatečně
#   míň než 45       nedostatečně
#
# Neprospěl ten, kdo má nedostatečně.

def prumer(test1, test2, test3):
    return (test1 + test2 + test3) / 3


def slovni_znamka(body):
    if body > 90:
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
    return f"{jmeno}: {body:.1f} bodů, {znamka}, {prospel(body)}"


print(vysvedceni("Jana", 40, 35, 45))
print(vysvedceni("Petr", 95, 88, 91))
print(vysvedceni("Klára", 88, 91, 91))
