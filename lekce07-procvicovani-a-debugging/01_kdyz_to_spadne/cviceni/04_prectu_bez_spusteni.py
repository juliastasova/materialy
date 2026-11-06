# Cvičení 4 – Když to spadne
# Tenhle soubor nespouštěj. Jsou v něm tři hlášky z cizích programů.
# U každé napiš do komentáře, na kterém řádku to spadlo, jaký je to
# druh chyby a co se nejspíš stalo.
#
# Samotný kód těch programů nevidíš. To je schválně – z hlášky se
# dá poznat dost.

# ------- Hláška 1 -------
#     File "dochazka.py", line 5
#         print(pocet)
#   IndentationError: unexpected indent
#
# Tvoje odpověď:


# ------- Hláška 2 -------
#   Traceback (most recent call last):
#     File "uctenka.py", line 9, in <module>
#       print(s_poplatkem("12,50"))
#             ~~~~~~~~~~~^^^^^^^^^
#     File "uctenka.py", line 6, in s_poplatkem
#       return na_cislo(castka) + 100
#              ~~~~~~~~^^^^^^^^
#     File "uctenka.py", line 2, in na_cislo
#       return int(text)
#   ValueError: invalid literal for int() with base 10: '12,50'
#
# Tvoje odpověď:


# ------- Hláška 3 -------
#   200
#   Traceback (most recent call last):
#     File "prumer.py", line 6, in <module>
#       print(vysledek + 50)
#             ~~~~~~~~~^~~~
#   TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'
#
# Tvoje odpověď:
