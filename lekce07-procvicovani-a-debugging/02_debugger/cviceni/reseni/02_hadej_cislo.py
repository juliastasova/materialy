# Řešení cvičení 2 – Debugger
# Opravený program. Pod ním jsou obě chyby popořadě.

from random import randrange


def vylosuj_cislo():
    return randrange(1, 21)


def zeptej_se_na_tip():
    return int(input("Hádej číslo od 1 do 20: "))


def je_trefa(tip, hledane):
    return tip == hledane


def napoveda(tip, hledane):
    if tip > hledane:
        return "Moc velké."
    else:
        return "Moc malé."


hledane_cislo = vylosuj_cislo()
pokusy = 0

while True:
    tip = zeptej_se_na_tip()
    pokusy = pokusy + 1

    if je_trefa(tip, hledane_cislo):
        print("Trefa!")
        break
    if pokusy == 5:
        print(f"Došly ti pokusy. Hledané číslo bylo {hledane_cislo}.")
        break

    print(napoveda(tip, hledane_cislo))


# Chyba 1 – číslo se pořád mění
#
# Nápovědy si odporovaly – třeba na 10 program napsal "Moc velké."
# a o kolo později na 9 "Moc malé.".
#
# S breakpointem na řádku s print(napoveda(...)) a Continue po každém
# tipu je v panelu Variables vidět, že hledane_cislo je v každém kole
# jiné.
#
# Losování bylo uvnitř cyklu, takže proběhlo v každém kole znovu.
# Patří před cyklus – číslo se vylosuje jednou na celou hru.
#
#
# Chyba 2 – trefa pátým tipem
#
# Ukáže se, jen když se trefíš právě pátým tipem. Program pak napíše
# "Došly ti pokusy." a jako hledané prozradí přesně to číslo, které
# jsi zadala.
#
# Breakpoint na řádku if pokusy == 5 zabere v každém kole. Mačkej
# Continue, dokud se netrefíš pátým tipem. V panelu je pak třeba:
#
#   tip = 13
#   hledane_cislo = 13
#   pokusy = 5
#
# Step Over skočí do větve, kde došly pokusy, a program skončí dřív,
# než se dostane ke kontrole trefy. Podmínky se zkouší odshora, takže
# kontrola trefy musí být první.
