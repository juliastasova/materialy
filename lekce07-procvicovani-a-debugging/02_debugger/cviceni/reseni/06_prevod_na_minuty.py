# Řešení cvičení 6 – Debugger
# Opravený program. Pod ním je, jak se ta chyba našla.

def na_minuty(cas):
    hodiny = int(cas[0])
    minuty = int(cas[2:])
    return hodiny * 60 + minuty


pondeli = na_minuty("2:45")
streda = na_minuty("1:30")
patek = na_minuty("2:20")

celkem = pondeli + streda + patek

print(f"Pondělí: {pondeli} min")
print(f"Středa:  {streda} min")
print(f"Pátek:   {patek} min")
print(f"Celkem:  {celkem} min")


# Breakpoint na první řádek na_minuty a pak Step Over po řádcích.
# V panelu Variables:
#
#   cas = '2:45'
#   hodiny = 2        sedí
#   minuty = 4        nesedí, má to být 45
#
# Výřez cas[2:3] bere od indexu 2 do indexu 3 a konec se nepočítá –
# vyjde z něj jediný znak "4". Správně je cas[2:], tedy od indexu 2
# až do konce textu.
