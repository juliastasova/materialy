# Cvičení 2 – Debugger
# Spusť soubor (Run) a zahraj si pár her. Chyby jsou dvě a ta druhá
# se ukáže jen někdy. Najdi je debuggerem a oprav.

# Hádání čísla znáš ze čtvrté lekce. Počítač si vylosuje číslo
# od 1 do 20 a ty hádáš. Po každém tipu napíše "Moc velké." nebo
# "Moc malé.". Když se trefíš, napíše "Trefa!". Když se netrefíš
# ani pátým tipem, prozradí číslo.

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


pokusy = 0

while True:
    hledane_cislo = vylosuj_cislo()
    tip = zeptej_se_na_tip()
    pokusy = pokusy + 1

    if pokusy == 5:
        print(f"Došly ti pokusy. Hledané číslo bylo {hledane_cislo}.")
        break
    if je_trefa(tip, hledane_cislo):
        print("Trefa!")
        break

    print(napoveda(tip, hledane_cislo))
