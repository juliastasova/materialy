# Funkcie dohromady - opakovanie:
def je_heslo_dlhe(heslo):
    return len(heslo) > 8

def spytaj_sa_na_meno():
    meno = input("zadaj meno: ")
    return meno 

def spytaj_sa_na_heslo():
    return input("zadaj heslo: ")

def prihlasenie():
    jmeno = spytaj_sa_na_meno()
    heslo = spytaj_sa_na_heslo()
    if je_heslo_dlhe(heslo):
         print("vitej", meno)
    else:
        print("heslo má zlú dĺžku")
 
 def spytaj_sa_na_email():
    return input("zadaj email: ")

def prihlasenie_s_mailom():
    jmeno = spytaj_sa_na_email()
    heslo = spytaj_sa_na_heslo()
    if je_heslo_dlhe(heslo):
         print("vitej", meno)
    else:
        print("heslo má zlú dĺžku")
    
prihlasenie()   
    
