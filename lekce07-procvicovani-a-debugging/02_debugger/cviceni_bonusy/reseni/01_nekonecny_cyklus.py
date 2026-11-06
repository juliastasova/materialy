# Řešení bonusu 1 – Debugger
# Opravený program. Pod ním je, jak se ta chyba našla.

cislo = 100
kroku = 0

while cislo != 0:
    cislo = cislo - 5
    kroku = kroku + 1

print(f"Hotovo za {kroku} kroků.")


# Po zmáčknutí Pause se program zastavil uvnitř cyklu a v panelu
# Variables bylo:
#
#   cislo = 100           pořád stejné
#   kroku = 2847193       obrovské číslo (u tebe vyjde jiné,
#                         záleží, jak dlouho jsi nechala program běžet)
#
# Tohle je typický obrázek zacykleného programu. Něco se počítá
# donekonečna a podmínka cyklu se nemá o co opřít.
#
# V cyklu chyběl řádek, který cislo zmenšuje. Dokud zůstává na
# stovce, podmínka cislo != 0 platí pořád.
#
# U každého while stojí za to se zeptat: mění se v cyklu to,
# na co se podmínka ptá?
