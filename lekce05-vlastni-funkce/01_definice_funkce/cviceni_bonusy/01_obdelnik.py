# Bonus 1 – Definice funkce
# Doplň kód pod zadání a soubor spusť (Run).

# Napiš funkci obdelnik(sirka, vyska), která z hvězdiček vypíše
#     obdélník zadané velikosti. obdelnik(5, 3) vypíše tři řádky
#     po pěti hvězdičkách.

def zkontroluj_heslo(heslo, min_delka=8):
    """Vypíše, jestli je heslo dost dlouhé.

    heslo      text, který se kontroluje
    min_delka  nejmenší povolená délka, celé číslo větší než nula
    """
    if len(heslo) < min_delka:
        print(heslo, "– moc krátké")
    else:
        print(heslo, "– dost dlouhé")

zkontroluj_heslo("kolo")
zkontroluj_heslo("pyladies2026")

zkontroluj_heslo("kolo", 0)

help(zkontroluj_heslo)