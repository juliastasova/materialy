# poznámky - 3.lekcia 08/10
# funkcia je napríklad aj print()
# berú vstup, s ktorým pracujú, niektoré funkcie nepotrebujú vstup (napr print vytiskne prázdny riadok)
# funkcie zvládajú niekoĺko vstupov/argumentov
# argumenty sa oddeľujú čiarkou
print(1, 2, 3, sep=",", end="!!!") # separátor, vytlačí čiarky medzi číslami, end dá na koniec niečo

vek= int(input("kolik ti je let?"))
print(int(vek + 1))
# funkcie môžu mať vstup i výstup. print má argument, input chce argument a tiež výstup

# formáty hodnôt - čísla/písmená, musíme previesť na správne hodnoty 

# metoda lem
jmeno = input("jmeno?")
print("tve jmeno je", len(jmeno), "dlouhe")
# len je skratka pre length, môžeme ju volať na reťazce aka písmená. započítava medzeru ako znak tiež
# dĺžka reťazca začína od 1
# pozícia reťazca začína od 0
# length vracia číslo, netreba vôbec transformovať formáty

# absolútna hodnota ignoruje mínusové čísla
print(abs(-7))

# round - zaokrúhľovanie 
print(round(3.14159, 2)) 
# Python najprv zaokrúhli na celé číslo
# ak chceme presný počet des. miest tak treba špecifikovať ďalším argumentom

# min - minimum value
print(min(2, 3, 5)
# max - maximum value
print(max(2, 3, 5)
      
# range - vracia čísla od 0 do 4 ak zadáme 5, berie číslo predtým čiže 4
print(range(5))
# ak je tam aj len, tak to vráti čísla od 0 do 5 lebo 
# range vracia skupinu čísel, ktoré môžeme prechádzať, je to funkcia iba na čísla
print(len(range(5)))
      
#  for loop - cyklus 
#  pre každú premennú v intervale 0 až 3 vytlač. range znamená, koľkokrát chceme niečo robiť
#  i nám pomáha vedieť, v koľkom sme cykle
for i in range(4): 
    print("Ahoj" i)

#  str je opak int
#  str znamená, že sa to znova premení na text/string
#  str - string
# float - pri práci s desatinnými číslami

# 
soucet = 0
for i in range(0, 5):
    print("soucet na zacatku cyklu:", soucet)
    soucet = soucet + i
    print("soucet na konci cyklu:", soucet) 
print("po cyklu:", soucet)
#  súčet sa redefinuje v cykle, čiže musíme dať 0

# vnorený cyklus:
for i in range(5):
    print(i)
    for j in range(4):
        print("kolo:", i, "pokus:", j)

jmeno = input("Jmeno?")

#  cez for loop vieme prechádzať aj texty
for pismeno in jmeno:
    print(pismeno)
    