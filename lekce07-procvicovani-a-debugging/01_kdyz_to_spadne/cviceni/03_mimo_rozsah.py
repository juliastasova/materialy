# Cvičení 3 – Když to spadne
# Spusť soubor (Run), přečti hlášku a chybu oprav.

# Program má vypsat každou číslici PINu na vlastní řádek a pod tím
# jejich součet.
#
# Všimni si, kolik řádků se vypsalo, než to spadlo.

def cislice_na(pin, pozice):
    return int(pin[pozice])


pin = "4821"
soucet = 0

for i in range(len(pin) + 1):
    cislice = cislice_na(pin, i)
    soucet = soucet + cislice
    print(f"{i + 1}. číslice: {cislice}")

print(f"Součet: {soucet}")
