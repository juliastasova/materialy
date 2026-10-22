# Cvičení 7 – Vestavěné funkce
# Doplň kód pod zadání a soubor spusť (Run).

# Uživatel zadá počet sekund (třeba 3661). Přepočítej ho na hodiny,
#    minuty a sekundy a vypiš je jako 1:1:1 jediným printem.

sekundy = int(input("zadaj číslo sekúnd: "))
hodiny = sekundy // 3600
minuty = sekundy % 3600 // 60  
zvysok = sekundy % 60  
print(hodiny, minuty, zvysok, sep=":")

