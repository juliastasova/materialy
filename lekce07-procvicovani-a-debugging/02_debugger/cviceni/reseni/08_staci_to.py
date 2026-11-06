# Řešení cvičení 8 – Debugger
# Opravený program. Pod ním je, jak se ta chyba našla.

castka = int(input("Kolik korun máš? "))
cena = int(input("Kolik stojí vstupenka? "))

if castka > cena:
    print("Stačí.")
else:
    print("Nestačí.")


# Dej breakpoint na řádek s podmínkou. V panelu Variables je:
#
#   castka = '1000'
#   cena = '250'
#
# Obě čísla sedí, ale jsou v uvozovkách – a to znamená text. Ve
# výpisu by tohle vidět nebylo, print uvozovky neukazuje.
#
# input vrací text. Texty se porovnávají znak po znaku od začátku:
# "1000" začíná jedničkou, "250" dvojkou, a jednička je dřív.
# Proto "1000" > "250" neplatí.
#
# S int() se porovnávají čísla a program odpoví správně.
