# ---------------------------------------------
#  Chybová hláška je nápověda
# ---------------------------------------------
# V lekci 1 jsme u první chybové hlášky slíbili, že se jim budeme
# věnovat později. Teď je to později.
#
# Spusť soubor. Spadne – to je schválně.

jmeno = "Anna"
vek = "30"

print(f"Jméno: {jmeno}")

rok_narozeni = 2026 - vek
print(f"Rok narození: {rok_narozeni}")


# V terminálu se objeví tohle:
#
#   Jméno: Anna
#   Traceback (most recent call last):
#     File "01_hlaska_je_napoveda.py", line 14, in <module>
#       rok_narozeni = 2026 - vek
#                      ~~~~~^~~~~
#   TypeError: unsupported operand type(s) for -: 'int' and 'str'
#
# (U tebe bude před názvem souboru ještě celá cesta k němu.)
#
# Čte se to odspodu.
#
# Poslední řádek je ten důležitý – druh chyby a co se stalo:
#   TypeError       Python dostal jiný typ hodnoty, než čekal.
#   unsupported     mínus mezi int a str nefunguje.
#
# Nad ním je vypsaný řádek s kódem a vlnovky ukazují na místo,
# kde to prasklo. Úplně nahoře je soubor a číslo řádku.
#
# V lekci 1 stačilo vědět, že hláška říká soubor, řádek a druh chyby.
# Teď ten poslední řádek přečteme celý. Číslo řádku tě pošle na
# správné místo, poslední řádek řekne, co tam hledat.
#
# Tady je vek text "30", ne číslo 30. Oprav řádek 10 na vek = 30
# a spusť znovu.
