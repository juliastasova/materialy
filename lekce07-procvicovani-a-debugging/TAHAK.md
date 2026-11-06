# Tahák – Lekce 7: Procvičování a debugging

Rychlý přehled toho, co jsme se naučili. Klidně si ho vytiskni na A4.

## Jak číst chybovou hlášku

```text
Traceback (most recent call last):
  File "nakup.py", line 15, in <module>        ← soubor a číslo řádku
    za_hrusky = hrusky * cena_hrusky           ← kód na tom řádku
                ^^^^^^                         ← kde to Python poznal
NameError: name 'hrusky' is not defined. Did you mean: 'hruksy'?
```

Čte se odspodu. Poslední řádek říká druh chyby a co se stalo.

Řádek v hlášce je místo, kde to Python poznal. Chyba může být výš –
tady se proměnná při vytvoření jmenovala `hruksy`. U překlepů poradí
`Did you mean`.

## Hláška bez řádku Traceback

```text
  File "cena.py", line 10
    print(f"Cena: {cena} Kč)
          ^
SyntaxError: unterminated f-string literal (detected at line 10)
```

Chyba v zápisu (`SyntaxError`, `IndentationError`). Python ji najde ještě
před spuštěním, takže se neprovede nic – ani řádky nad ní.

U ostatních chyb se všechno nad chybným řádkem opravdu provedlo.

## Hláška s víc patry

```text
Traceback (most recent call last):
  File "prumer.py", line 16, in <module>       ← odtud to začalo
    vypis_prumer("Únor", 0, 0)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^
  File "prumer.py", line 11, in vypis_prumer
    vysledek = prumer(soucet, pocet)
  File "prumer.py", line 7, in prumer          ← tady to spadlo
    return soucet / pocet
           ~~~~~~~^~~~~~~
ZeroDivisionError: division by zero
```

Spodní patro je místo, kde to spadlo. Horní patro je řádek, který jsi
psala ty, a tam bývá i chyba – tady se do funkce poslala nula.

## Časté chyby

| Hláška | Co se většinou stalo |
|---|---|
| `SyntaxError` | chybí dvojtečka, závorka nebo uvozovka |
| `IndentationError` | řádek je odsazený jinak, než má |
| `NameError` | překlep ve jméně, nebo proměnná ještě neexistuje |
| `TypeError` | text místo čísla (`input` vrací text), nebo `None` z funkce bez `return` |
| `ValueError` | `int()` dostal text, který není celé číslo, třeba `"12,50"` |
| `ZeroDivisionError` | dělení nulou – nějaký počet zůstal na nule |
| `IndexError` | index za koncem textu – poslední je `len(text) - 1` |

## Když to nespadne, a přesto je to špatně

```python
print(prvni)            # 2
print(type(prvni))      # <class 'str'>   type() řekne typ hodnoty
```

## Debugger ve VS Code

1. Klikni vlevo od čísla řádku – objeví se červená tečka, **breakpoint**.
2. Šipka vedle tlačítka Run → **Python Debugger: Debug Python File**
   (nebo F5).
3. Program se na breakpointu zastaví, řádek zežloutne a panel
   **Variables** ukáže všechny proměnné.

```text
tah = 'Kamen'       v uvozovkách = text, přesně tak, jak ho Python má
cena = 250          bez uvozovek = číslo
```

Breakpoint zrušíš dalším kliknutím na tečku.

## Tlačítka debuggeru

| Tlačítko | Co dělá |
|---|---|
| Continue | program běží dál až k dalšímu breakpointu |
| Step Over | provede jeden řádek a zastaví se na dalším |
| Step Into | vejde do funkce, která se na řádku volá |
| Step Out | dokončí funkci a zastaví se tam, odkud se volala |
| Restart | spustí program znovu od začátku |
| Stop | program ukončí |
| Pause | je na místě Continue, když program běží; zastaví ho tam, kde zrovna je |

- Breakpoint v cyklu zabere v každém průchodu. Continue tě posune o kolo dál.
- Když se program na breakpointu nezastaví, k tomu řádku se nedostal.
- Chyba, která se projeví jen někdy, se hledá opakováním: spouštěj znovu,
  dokud nenastane.

## Konstanty

```python
KAMEN = "kamen"         # velká písmena: hodnota se v programu nemění

tah == KAMNE            # překlep ve jméně → NameError, Python ho najde
tah == "kamne"          # překlep v textu → žádná hláška, jen špatný výsledek
```
