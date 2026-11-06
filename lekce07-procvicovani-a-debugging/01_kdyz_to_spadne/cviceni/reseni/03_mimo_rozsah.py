# Řešení cvičení 3 – Když to spadne
# Opravený program. Pod ním je, jak se ta chyba našla.

def cislice_na(pin, pozice):
    return int(pin[pozice])


pin = "4821"
soucet = 0

for i in range(len(pin)):
    cislice = cislice_na(pin, i)
    soucet = soucet + cislice
    print(f"{i + 1}. číslice: {cislice}")

print(f"Součet: {soucet}")


# IndexError: string index out of range
#
# Čtyři řádky se vypsaly a teprve pátý průchod spadl. Na prvních
# čtyřech číslicích tedy program fungoval.
#
# Hláška má dvě patra. Spodní ukazuje na řádek v cislice_na, kde
# se do PINu sahá. Vrchní ukazuje na řádek v cyklu, odkud se funkce
# zavolala – a tam je i chyba.
#
# "4821" má čtyři znaky s indexy 0, 1, 2, 3. range(len(pin) + 1)
# ale dojde až k pětce, takže poslední průchod sahá na index 4.
# Správně je range(len(pin)).
