# Bonus 1 – Debugger
# Tenhle program se zacyklí. Než ho spustíš, přečti si, jak ho
# zastavíš: červeným čtverečkem Stop nahoře, nebo kliknutím do
# terminálu a Ctrl+C.

# Program má odpočítat od sta k nule po pěti a vypsat, kolik kroků
# to trvalo. Místo toho běží pořád dokola.
#
# Spusť ho přes Python Debugger a nech ho chvíli běžet. Pak zmáčkni
# v pruhu nahoře Pause – dvě svislé čárky na místě, kde byl Continue.
# Program se zastaví tam, kde zrovna je, a v panelu Variables uvidíš,
# proč se nehne z místa.
#
# Pak chybu oprav.

cislo = 100
kroku = 0

while cislo != 0:
    kroku = kroku + 1

print(f"Hotovo za {kroku} kroků.")
