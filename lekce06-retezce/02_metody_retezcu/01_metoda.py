# ---------------------------------------------
#  Metoda: co umí text sám
# ---------------------------------------------
# Spusť soubor a porovnej výsledky.
#
# Funkce, které znáš, pracují s textem zvenčí – len() si ho vezme
# a změří:

print(len("pyladies"))      # 8


# Řetězec umí věci i sám o sobě. Zapisuje se to tečkou:

jmeno = "pyladies"
print(jmeno.upper())        # PYLADIES

# Čte se to takhle:
#   jmeno     hodnota, na které metodu voláme
#   .         tečka – „na téhle hodnotě"
#   upper()   metoda, tedy funkce, která k řetězci patří
#
# Kulaté závorky znamenají „zavolej to" – stejně jako u len() nebo
# u tvých funkcí z lekce 5. Bez nich se metoda nezavolá a Python jenom
# oznámí, že nějaká taková metoda existuje:
print(jmeno.upper)      # <built-in method upper of str object at ...>

# Takový výpis skoro vždycky znamená, že někde chybí závorky.


# Metodu jde zavolat i rovnou na textu v uvozovkách:
print("pyladies".upper())           # PYLADIES


# A její výsledek se dá dosadit do f-stringu:
print(f"Vítej, {jmeno.upper()}!")   # Vítej, PYLADIES!
