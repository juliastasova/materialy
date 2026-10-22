# Cvičení 3 – And, or a not
# Doplň kód pod zadání a soubor spusť (Run).

# Přihlášení. Správné jméno je "anna" a správné heslo je "tajne".
#    Zeptej se na jméno i heslo a vypiš "Vítej!", jen když sedí obojí.
#    Jinak vypiš "Špatné údaje.".


meno(input("Meno: "))
heslo(input("Heslo: "))
if meno == "anna" and heslo == "tajne":
    print("Vitaj")
else:
    print("Zlé meno alebo heslo")
