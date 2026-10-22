# ---------------------------------------------
#  Základní počítání (+ - * /)
# ---------------------------------------------
# Vypisovat už umíme – teď zkusíme, že Python počítá jako kalkulačka.
# Spusť soubor a sleduj výsledky.


# Sčítání a odčítání
print(3 + 8)
print(10 - 2)


# Násobení se píše hvězdičkou *
print(4 * 5)


# Dělení se píše lomítkem /
print(20 / 4)


# Dělení může vyjít desetinné.
# Desetinná čárka se v Pythonu píše jako tečka.
print(10 - 2.2)


# Někdy vyjde hodně dlouhé desetinné číslo – to je v pořádku,
# Python jen ukazuje výsledek co nejpřesněji.
print(10 / 3)


# Ještě důležitá věc: stejné znaménko se chová jinak u čísel a u textu.
# (S + a * na textu jsme se potkali už u printu.)
print(3 + 8)        # 11      čísla se sčítají
print("3" + "8")    # 38      text se spojuje
print("ha" * 3)     # hahaha  text se opakuje

# Číslo a text jsou totiž různé datové typy. Proto později u input()
# budeme text převádět na číslo (int / float), než s ním počítáme.

print(2837 % 10)