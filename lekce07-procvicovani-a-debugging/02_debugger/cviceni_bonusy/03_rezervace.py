# Bonus 3 – Debugger
# Jsou tu tři chyby a každá je jiného druhu. Jednu ti ukáže chybová
# hláška, druhou poznáš z výsledku a na tu třetí se hodí debugger.
# Oprav je po jedné a po každé opravě program spusť.

# Program spočítá rezervaci kurzu.
#   - kurz stojí 2 400 Kč za osobu
#   - od tří osob je sleva 10 % z celkové ceny
#   - každá členka klubu má navíc slevu 200 Kč
#   - záloha je třetina výsledné ceny zaokrouhlená na celé koruny
#
# Počítá se pro čtyři osoby, z toho dvě členky. Obě vypsaná čísla
# si zkontroluj podle pravidel výš – u zálohy stačí podělit
# celkovou cenu třemi.

def zaloha_z(castka):
    return round(castka / 3)


osoby = 4
clenky = 2
cena_osoby = 2400

celkem = osoby * cena_osoba

zaloha = zaloha_z(celkem)

if osoby >= 3:
    celkem = celkem * 0.9

celkem = celkem - 200

print(f"Osob: {osoby}, z toho členek: {clenky}")
print(f"Celkem: {celkem:.0f} Kč")
print(f"Záloha: {zaloha} Kč")
