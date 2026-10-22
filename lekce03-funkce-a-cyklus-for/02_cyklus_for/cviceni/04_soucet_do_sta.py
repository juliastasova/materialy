# Cvičení 4 – Cyklus for
# Doplň kód pod zadání a soubor spusť (Run).

# Spočítej součet všech čísel od 1 do 100 pomocí cyklu for
#    (ne funkcí sum) a výsledek vypiš.

soucet = 0
for cislo in range (1, 101):
    print(soucet+cislo)
    soucet = soucet + cislo
print(soucet)


