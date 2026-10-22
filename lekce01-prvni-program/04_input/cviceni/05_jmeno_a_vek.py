# Cvičení 5 – Vstup od uživatelky
# Doplň kód pod zadání a soubor spusť (Run).

# Napiš program, který se zeptá na jméno a na věk (převeď na číslo)
#    a vypíše větu: Ahoj <jmeno>, za rok ti bude <věk + 1> let.


vek_text = input("Kolik ti je let? ")   # text, třeba "30"
vek = int(vek_text)                      # převedeno na číslo 30
print("Za rok ti bude", vek + 1)

strana = float(input("Zadej stranu čtverce v cm: "))
print("Obvod čtverce je", 4 * strana, "cm")