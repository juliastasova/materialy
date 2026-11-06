# Řešení cvičení 7 – Debugger
# Opravený program. Pod ním je, jak se ta chyba našla.

pin = "4821"

soucet = 0

for znak in pin:
    soucet = soucet + int(znak)

print(f"Součet číslic: {soucet}")


# Dej breakpoint na řádek s printem a mačkej Continue. Program se
# na něm zastavil čtyřikrát – jednou za každou číslici PINu.
# Breakpoint uvnitř cyklu zabere v každém průchodu, takže čtyři
# zastavení znamenají, že ten řádek je uvnitř cyklu.
#
# A tam nepatří. Print byl odsazený stejně jako řádek nad ním,
# takže patřil do těla cyklu.
#
# Odsazení rozhoduje o tom, co je uvnitř cyklu a co až za ním.
# Python v tom chybu nevidí – obě varianty dávají smysl, jen každá
# dělá něco jiného.
