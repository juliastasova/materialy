# Bonus 1 – Cyklus for
# Doplň kód pod zadání a soubor spusť (Run).

# Uživatel zadá číslo N. Spočítej cyklem jeho faktoriál –
#     tedy 1 * 2 * 3 * ... * N – a výsledek vypiš.
#     (Faktoriál z 5 je 120.)



x = int(input("num: "))
start = 1
for x in range(1, x + 1):
    start = start * x
print(start)