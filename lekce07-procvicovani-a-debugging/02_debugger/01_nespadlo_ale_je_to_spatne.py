# ---------------------------------------------
#  Nespadlo to, a přesto je to špatně
# ---------------------------------------------
# Spusť soubor a zadej 2 a 3. Nespadne. Je výsledek správně?

prvni = input("První číslo: ")
druhe = input("Druhé číslo: ")

print(f"Součet: {prvni + druhe}")


# Žádná chybová hláška se neobjevila. Program udělal přesně to, co
# jsme napsali – jen jsme napsali něco jiného, než jsme mysleli.
#
# Celá minulá složka stála na tom, že hláška je nápověda. Tady žádná
# není. Zbývá podívat se dovnitř: co je v proměnných doopravdy?

print(prvni)            # 2
print(type(prvni))      # <class 'str'>


# type() je vestavěná funkce jako len(). Řekne, jakého typu hodnota
# je. Tady str, tedy text.
#
# input vrací text pokaždé, i když naťukáš číslici. A plus mezi
# dvěma texty je spojí, jak víš z lekce 6.

prvni = int(prvni)
druhe = int(druhe)

print(f"Součet: {prvni + druhe}")       # Součet: 5


# Printem se dá nakouknout do každého programu. Má to ale dvě
# nevýhody. Musíš dopředu uhodnout, kterou proměnnou chceš vidět –
# a když uhodneš špatně, přidáváš další print a spouštíš znovu.
# A po opravě ty printy zase mažeš.
#
# U čtyř řádků to nevadí. U programu, kde se chyba schovává mezi
# několika funkcemi, je to zdlouhavé.
#
# VS Code umí program zastavit uprostřed běhu a ukázat všechny
# proměnné naráz, bez psaní a bez mazání. O tom je zbytek téhle
# složky.
