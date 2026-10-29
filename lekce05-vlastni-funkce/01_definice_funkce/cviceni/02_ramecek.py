# Cvičení 2 – Definice funkce
# Doplň kód pod zadání a soubor spusť (Run).

# Napiš funkci ramecek, která má na vstupu řetězec. Vypíše řádek
# hvězdiček, pod něj ten text a pod něj další řádek hvězdiček.
# Zavolej ji pro dva různé texty.
# Můžeš v ní použít oddelovac() z prvního úkolu – zkopíruj si jeho
# definici sem nahoru, soubory se navzájem nevidí.

def oddelovac():
    print("*" * 30)

def ramecek(text):
    oddelovac()
    print(text)
    oddelovac() 

ramecek("skouska 1")
ramecek("skouska 2")

