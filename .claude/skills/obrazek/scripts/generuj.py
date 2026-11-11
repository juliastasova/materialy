"""Vygeneruje ilustraci do materiálů přes OpenAI Images API.

Použití:
    python generuj.py --prompt-file zadani.txt --out cesta/obrazek.png \
        --ref lekce05-vlastni-funkce/01_definice_funkce/definice_funkce.png

Ke každému zadání se automaticky přidá popis stylu ze souboru styl.md.
S --ref volá images.edit (referenční obrázky drží styl), bez něj images.generate.
Klíč čte z proměnné prostředí OPENAI_API_KEY.
"""

import argparse
import base64
import sys
from contextlib import ExitStack
from pathlib import Path

from openai import OpenAI

SKILL_DIR = Path(__file__).resolve().parent.parent
STYLE_FILE = SKILL_DIR / "styl.md"


def load_style() -> str:
    text = STYLE_FILE.read_text(encoding="utf-8")
    # Pro model jen část mezi značkami, zbytek souboru je pro lidi.
    start, end = "<!-- STYL-START -->", "<!-- STYL-END -->"
    if start in text and end in text:
        text = text.split(start, 1)[1].split(end, 1)[0]
    return text.strip()


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    src = p.add_mutually_exclusive_group(required=True)
    src.add_argument("--prompt", help="zadání obrázku")
    src.add_argument("--prompt-file", type=Path, help="soubor se zadáním (UTF-8)")
    p.add_argument("--out", type=Path, required=True, help="kam uložit PNG")
    p.add_argument("--ref", type=Path, action="append", default=[], help="referenční obrázek (lze opakovat)")
    p.add_argument("--model", default="gpt-image-2.5-sunburst")
    p.add_argument("--size", default="1024x1536", help="WIDTHxHEIGHT, násobky 16 (výchozí na výšku)")
    p.add_argument("--quality", default="high", help="low | medium | high | xhigh | max | auto")
    p.add_argument("--n", type=int, default=1, help="počet variant")
    p.add_argument("--no-style", action="store_true", help="nepřidávat styl.md")
    p.add_argument("--force", action="store_true", help="přepsat existující soubor")
    args = p.parse_args()

    prompt = args.prompt if args.prompt is not None else args.prompt_file.read_text(encoding="utf-8")
    if not args.no_style:
        prompt = f"{load_style()}\n\n--- ZADÁNÍ OBRÁZKU ---\n{prompt.strip()}"
        if args.ref:
            prompt += (
                "\n\nThe attached images are STYLE REFERENCES ONLY: copy their visual style "
                "(colors, fonts, boxes, arrows, callouts, background) exactly, "
                "but do NOT copy their content or text."
            )

    outs = [args.out] if args.n == 1 else [
        args.out.with_name(f"{args.out.stem}_{i + 1}{args.out.suffix}") for i in range(args.n)
    ]
    existing = [o for o in outs if o.exists()]
    if existing and not args.force:
        print(f"Soubor už existuje: {', '.join(map(str, existing))} (použij --force)", file=sys.stderr)
        return 1
    for r in args.ref:
        if not r.exists():
            print(f"Referenční obrázek neexistuje: {r}", file=sys.stderr)
            return 1

    client = OpenAI()
    common = dict(model=args.model, prompt=prompt, size=args.size, quality=args.quality, n=args.n)
    with ExitStack() as stack:
        if args.ref:
            files = [stack.enter_context(open(r, "rb")) for r in args.ref]
            result = client.images.edit(image=files, **common)
        else:
            result = client.images.generate(**common)

    for out, item in zip(outs, result.data):
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_bytes(base64.b64decode(item.b64_json))
        print(f"Uloženo: {out}")
    usage = getattr(result, "usage", None)
    if usage:
        print(f"Tokeny: {usage}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
