# # vo for loopoch definujeme, koľkokrát chceme niečo robiť
# # aka máme preddefinovaný koniec


# # while loops
# # povoľuje, aby bežal cyklus, dokým neplatí podmienka

# heslo = input("zadaj heslo: ")
# while heslo != "pyladies":
#     print("neprihlasena")
#     heslo = input("zadaj heslo")
# print("vitej") # pýta sa na heslo, až dokým užívateľ nezadá správne heslo
# # premenná heslo 

# # importovanie funkcie - hádžeme kockou, dokým nepadne 6ka
# # keď hodíme 1, vypíš hra končí a prehrali sme
# from random import randrange

# hod = randrange(1, 7)
# while hod != 6:
#     if hod == 1:
#         print("koncime")
#         break
#     print("Padlo:", hod, "hazime znovu")
#     hod = randrange(1, 7)
# if hod == 1:
#     print("prehrala si")
# else:
#     print("Padla", hod, "Vyhrala si!")

# # while True: - pravda je vždycky, toto platí a nemusíme definova

# while True:
#     odpoved = input("jask se mas?"
#     print("Ahoj!")

# soucet = 0
# while soucet < 1000: #ak chceme definovať podmienku
#     # alebo for i in range(0, 5):
#     print("beh", i)
#     odpoved = input("zadej cislo (nebo konec)")
#     if odpoved == "konec":
#         break
    
#     cislo = float(odpoved)
#     if odpoved < 0:
#         print("zaporna cisla ignorujeme")
#         i = i - 1 # je mu to jedno, i sa prepisuje z range, ktorý sme preddefinovali
#         continue # vráti nás na začiatok cyklu
    
#     soucet = soucet + cislo
#     if cislo >= 100:
#         break
#     print("zatim mame: ", soucet)
# print("soucet", soucet)   

# # continue a break sa chovajú rovnako vo for aj vo while
 
#  while False:
#      print("ahoj")
     
delka = 100
strihnuti = 0
while delka > 1:
    delka = delka / 2       # měníme proměnnou z podmínky
    strihnuti = strihnuti + 1
    print("Střihnutí", strihnuti, "– délka:", delka, "cm")
print("Počet střihnutí:", strihnuti)