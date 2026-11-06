# Řešení cvičení 4 – Debugger
# Opravený program. Pod ním je, jak se ta chyba našla.

vek = 10
plna_cena = 250

if vek < 6:
    cena = 0
elif vek < 18:
    cena = plna_cena / 2
elif vek < 65:
    cena = plna_cena
else:
    cena = plna_cena * 0.70

print(f"Vstupenka pro {vek} let: {cena:.0f} Kč")


# Breakpoint na první if a pak Step Over. Žlutý řádek skočil rovnou
# do větve cena = plna_cena a odtud až na print.
#
# Desetileté dítě je míň než 65, takže projde hned první podmínkou.
# Větve v if/elif se zkouší odshora a jakmile jedna platí, zbytek
# se přeskočí. Do větví pro děti se program nedostal nikdy.
#
# Podmínky proto musí jít od nejužší po nejširší.
