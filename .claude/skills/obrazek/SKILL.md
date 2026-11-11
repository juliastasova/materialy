---
name: obrazek
description: Vygeneruje ilustraci (schéma, vizualizaci konceptu) do materiálů kurzu přes OpenAI Images API ve stejném vizuálním stylu jako stávající obrázky v lekcích. Použij, když uživatel chce nový obrázek k výkladu, upravit existující obrázek nebo „nakreslit“ koncept do lekce.
---

# Obrázek do materiálů

Generuje PNG ilustrace přes OpenAI Images API (model `gpt-image-2.5-sunburst`)
tak, aby ladily se stávajícími obrázky v lekcích. Styl je popsaný v
`styl.md` a skript ho přidává ke každému zadání automaticky. Referenční
obrázky ho drží ještě víc.

## Předpoklady

- Proměnná prostředí `OPENAI_API_KEY`. Když chybí, řekni uživateli, ať ji
  nastaví (`setx OPENAI_API_KEY "sk-..."` a restart terminálu). Klíč nikdy
  nevypisuj a neukládej do repa.
- `pip install -U openai`.

## Postup

1. **Ujasni si obsah.** Přečti výklad (`NN_nazev.py`), ke kterému obrázek patří.
   Kód na obrázku musí přesně odpovídat kódu ve výkladu – stejná jména
   proměnných, stejné řetězce. Obrázek má jednu myšlenku, nejvýš 2–3 sekce.
2. **Vyber referenční obrázky.** Vždy 1–2 nejpodobnější z repa
   (`git ls-files "*.png"`). Výchozí volba:
   - kód s popisky: `lekce05-vlastni-funkce/01_definice_funkce/definice_funkce.png`
   - mřížka hodnot / znaků: `lekce06-retezce/03_indexovani_a_vyrezy/index_a_vyrez.png`
   - vývojový diagram, tok programu: `lekce04-cyklus-while/01_cyklus_while/cyklus_while.png`

   Screenshoty (`debugger_*.png`) jako referenci nepoužívej.
3. **Napiš zadání** do souboru ve scratchpadu (UTF-8), ne do repa. Anglicky
   popiš rozvržení, česky v uvozovkách uveď **každý text**, který má na obrázku
   být, a kód vlož doslova. Například:

   ```
   Two sections separated by a red dashed line.
   Section 1 title: "1. Co vrací return"
   Code block:
   def dvojnasobek(cislo):
       return cislo * 2
   Callout pointing at `return` (red outline): "vrátí výsledek"
   Section 2 title: "2. ..."
   ```
4. **Spusť skript** z kořene repa:

   ```
   python .claude/skills/obrazek/scripts/generuj.py --prompt-file <zadani.txt> --out <slozka_konceptu>/<nazev>.png --ref <reference1> --ref <reference2>
   ```

   Volby: `--size` (výchozí `1024x1536` na výšku, `1536x1024` na šířku),
   `--quality` (výchozí `high`; na rychlé návrhy `medium`), `--n 2` pro dvě
   varianty, `--force` pro přepsání. Existující soubor bez `--force` nepřepíše.
5. **Zkontroluj výsledek** – otevři PNG nástrojem Read a projdi:
   - je každý text a kód přesně správně, včetně diakritiky?
   - sedí barvy, nadpisy, boxy a šipky se stylem ostatních obrázků?
   - nepřibyl text navíc?

   Chyby oprav úpravou zadání a vygeneruj znovu. Malou opravu jedné oblasti
   jde udělat i tak, že vygenerovaný obrázek dáš jako první `--ref` a v zadání
   popíšeš jen změnu. Po 3 neúspěšných pokusech ukaž uživateli, co máš, a zeptej se.
6. **Zapoj obrázek do výkladu** podle README (sekce Pro autory): soubor leží ve
   složce konceptu, název malými písmeny bez diakritiky s podtržítky a výklad ho
   zmíní řádkem celým v závorce, např. `# (Ukazuje to obrázek nazev.png.)`.

## Pravidla

- Každé volání stojí peníze (víc u vyšší kvality a velikosti). Negeneruj
  desítky variant naslepo; ověř zadání, než ho pošleš.
- Nic necommituj bez výslovného souhlasu uživatele.
- Když uživatel změní styl (nová barva, jiný font), uprav část mezi značkami
  v `styl.md`, ať to platí i pro další obrázky.
