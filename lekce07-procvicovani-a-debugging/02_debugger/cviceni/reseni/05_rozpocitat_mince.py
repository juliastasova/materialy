# Řešení cvičení 5 – Debugger
# Opravený program. Pod ním je, jak se ta chyba našla.

zbyva = 87
dvacetikoruny = 0
petikoruny = 0

while zbyva >= 20:
    dvacetikoruny = dvacetikoruny + 1
    zbyva = zbyva - 20

while zbyva >= 5:
    petikoruny = petikoruny + 1
    zbyva = zbyva - 5

print(f"Dvacetikoruny: {dvacetikoruny}")
print(f"Pětikoruny: {petikoruny}")
print(f"Koruny: {zbyva}")


# Výpis končil na "Koruny: -13". Zbývat nemůže míň než nic, takže
# bylo jasné, že se někde odečítá moc.
#
# Breakpoint na první řádek druhého cyklu a pohled do panelu:
#
#   zbyva = 7, dvacetikoruny = 4      po prvním cyklu, sedí
#
# První cyklus je tedy v pořádku. Pak Step Over přes dva řádky
# druhého cyklu: petikoruny vyskočí na 1, což sedí, a zbyva spadne
# ze sedmi na -13.
#
# Ze zbytku se odečetlo dvacet místo pěti. Druhý cyklus vznikl
# zkopírováním prvního a v kopii zůstalo staré číslo.
