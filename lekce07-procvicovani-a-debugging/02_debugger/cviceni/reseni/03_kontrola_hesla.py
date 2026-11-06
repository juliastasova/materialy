# Řešení cvičení 3 – Debugger
# Opravený program. Pod ním jsou obě chyby popořadě.

heslo = input("Zadej heslo: ")

dost_dlouhe = len(heslo) >= 8
ma_velke = heslo != heslo.lower()

ma_cislici = False
for znak in heslo:
    if znak.isdigit():
        ma_cislici = True
        break

print(f"Aspoň osm znaků:  {dost_dlouhe}")
print(f"Obsahuje číslici: {ma_cislici}")
print(f"Velké písmeno:    {ma_velke}")

if dost_dlouhe and ma_cislici and ma_velke:
    print("Heslo přijato.")
else:
    print("Heslo nevyhovuje.")


# Chyba 1 – 2026Pyladies
#
# Program napsal "Obsahuje číslici: False", přestože heslo začíná
# čtyřmi číslicemi.
#
# Breakpoint uvnitř cyklu a Continue po každém znaku: ma_cislici je
# u znaků '2', '0', '2' a '6' True a u 'P' spadne zpátky na False.
# Každý znak přepsal, co zjistil ten před ním, takže rozhodoval jen
# poslední znak. Pyladies2026 končí číslicí, proto prošlo.
#
# Větev else tam nepatří. Jakmile se číslice najde, ma_cislici má
# zůstat True. Break cyklus rovnou ukončí, dál už se hledat nemusí.
#
#
# Chyba 2 – pyladies2026
#
# Heslo bez velkého písmena prošlo. Po řádku s ma_velke je v panelu:
#
#   heslo = 'pyladies2026'
#   ma_velke = True
#
# upper() udělá z hesla 'PYLADIES2026'. To se od hesla liší, kdykoli
# je v něm aspoň jedno malé písmeno – program se tak ptal na malá
# písmena. Na velké se zeptá lower(): heslo se od své malé verze liší,
# jen když v něm nějaké velké písmeno je.
