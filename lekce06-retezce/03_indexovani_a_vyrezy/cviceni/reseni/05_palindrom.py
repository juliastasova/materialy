# Řešení cvičení 5 – Indexování a výřezy
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# Zeptej se na slovo a vypiš, jestli se čte stejně zepředu i pozpátku.
#    Na velikosti písmen ať nezáleží, takže "Oko" projde taky.

slovo = input("Napiš slovo: ").strip().lower()

if slovo == slovo[::-1]:
    print(f"{slovo} je palindrom.")
else:
    print(f"{slovo} palindrom není.")

# Výřez s krokem -1 vrátí otočený text. Když se otočený rovná
# původnímu, je to palindrom.


# Když si na slovo[::-1] nevzpomeneš, poskládáš otočené slovo cyklem
# z lekce 3 – každý další znak dáváš před ty předchozí:
otocene = ""
for znak in slovo:
    otocene = znak + otocene

print(f"Pozpátku: {otocene}")

if slovo == otocene:
    print(f"{slovo} je palindrom.")
else:
    print(f"{slovo} palindrom není.")

# Obě řešení jsou správně.
