# ---------------------------------------------
#  input vždycky vrací text
# ---------------------------------------------
# Pozor na důležitou věc: cokoliv uživatel napíše, input vrátí
# jako TEXT – i když to vypadá jako číslo.
# Spusť soubor a uvidíš, proč na tom záleží.


# Zeptáme se na věk. To, co dostaneme, je text (třeba "30").
vek = input("Kolik ti je let? ")

# Kdybychom teď chtěli přičíst 1, program by SPADL s chybou –
# k textu se totiž číslo přičíst nedá.
# Zkus si to: odkomentuj řádek níž a spusť soubor.
# print("Za rok ti bude", vek + 1)


# Řešení: text převedeme na číslo pomocí funkce int().
# Uděláme to ve dvou krocích, ať je vidět, co se děje:
vek_text = input("Kolik ti je let? ")   # text, třeba "30"
vek = int(vek_text)                      # převedeno na číslo 30
print("Za rok ti bude", vek + 1)


# Zkráceně se to samé píše rovnou na jeden řádek (int okolo inputu):
#   vek = int(input("Kolik ti je let? "))


# Pro desetinná čísla se používá float():
strana = float(input("Zadej stranu čtverce v cm: "))
print("Obvod čtverce je", 4 * strana, "cm")

# Pozn.: desetinná čísla se vypisují s tečkou, takže třeba 12.0.

jmeno = input("Jak se jmenuješ? ")
vek = int(input("Kolik ti je let? "))
print("Ahoj,", jmeno, "- za rok ti bude", vek + 1, "let")

# font - prevedie text na číslo
# float - prevedie na desatinné číslo
# pretože funkcia input vždy vracia len text