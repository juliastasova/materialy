# Řešení cvičení 1 – Když to spadne
# Opravený program. Pod ním je, jak se ta chyba našla.

cena = int(input("Cena za kus: "))
pocet = int(input("Počet kusů: "))

print(f"Celkem: {cena * pocet} Kč")


# TypeError: can't multiply sequence by non-int of type 'str'
#
# input vrací text, i když naťukáš číslici. Dva texty se násobit
# nedají. int() z textu udělá číslo.
#
# "sequence" v hlášce znamená text – pro Python je to posloupnost
# znaků, jak víš z lekce 3.
