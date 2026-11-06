# Řešení cvičení 4 – Když to spadne
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# Hláška 1
#   Řádek 5 v souboru dochazka.py, IndentationError.
#   Řádek print(pocet) je odsazený víc, než má být.
#
#   Hlášce chybí "Traceback (most recent call last)". To je známka
#   chyby, kterou Python najde ještě před spuštěním – nevypsalo se
#   tedy vůbec nic.

# Hláška 2
#   Spadlo to na řádku 2 v souboru uctenka.py, ValueError.
#   int() dostal text "12,50" a z toho číslo udělat neumí: desetinná
#   čísla se v Pythonu píšou s tečkou, ne s čárkou.
#
#   Chyba ale vznikla výš. Patra vedou od řádku 9, kde někdo poslal
#   "12,50" do funkce s_poplatkem, přes řádek 6 až do na_cislo.
#   Opravit se to má na řádku 9.

# Hláška 3
#   Řádek 6 v souboru prumer.py, TypeError.
#   V proměnné vysledek je None, tedy "nic", a k ničemu se padesátka
#   přičíst nedá.
#
#   Nad hláškou se vypsalo 200, takže funkce svoje číslo spočítala –
#   jen ho vypsala printem místo toho, aby ho vrátila returnem.
#   Bez returnu vrací funkce None, jak víš z lekce 5.
