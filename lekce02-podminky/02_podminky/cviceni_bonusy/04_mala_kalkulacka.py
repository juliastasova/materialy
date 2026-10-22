# Bonus 4 – Podmínky
# Doplň kód pod zadání a soubor spusť (Run).

# Malá kalkulačka.
#     Zeptej se na dvě čísla a na znaménko (+, -, *, /).
#     Podle znaménka vypiš výsledek správné operace.
#     Bonus v bonusu: ošetři dělení nulou vlastní hláškou.


prvé_číslo = int(input("Povedz jedno číslo: "))
druhé_číslo = int(input("Povedz druhé číslo: "))
znamienko = input("napíš znamienko +, -, *, /: ")
if(znamienko == "+"):
    print(prvé_číslo + druhé_číslo)
elif(znamienko == "-"):
    print(prvé_číslo - druhé_číslo)
elif(znamienko == "*"):
    print(prvé_číslo * druhé_číslo)
elif(znamienko == "/"):
    print(prvé_číslo / druhé_číslo)
elif(znamienko == "/" and prvé_číslo or druhé_číslo == 0):
    print("Pri delení 0 vždy dostaneš 0.")