# Vizuální styl ilustrací v materiálech

Popis stylu odvozený z existujících obrázků (`definice_funkce.png`,
`index_a_vyrez.png`, `cyklus_while.png`, `promenne_vizualizace.png`).
Část mezi značkami níže posílá skript `generuj.py` modelu před každým zadáním.
Když se styl změní, uprav ji tady.

<!-- STYL-START -->
STYLE GUIDE – educational illustration for a Czech beginner Python course (PyLadies Prague).

Overall look:
- Clean flat educational infographic, slightly hand-drawn feel but crisp and legible.
- Warm off-white background (#FAF8F5). No gradients, no shadows, no 3D, no photos.
- No people, mascots or decorative clipart unless the brief explicitly asks for it.
- Portrait layout, generous whitespace, content arranged top to bottom.

Typography:
- Section titles: large, heavy, rounded sans-serif, bright red (#E02B2B),
  left-aligned, often numbered ("1. …", "2. …").
- Code and short labels: monospace font.
- Callout labels: smaller rounded sans-serif or monospace.

Code blocks:
- Code sits in a rounded rectangle with light warm grey/beige fill (#F2F0EC)
  and a thin grey border.
- Syntax colors: keywords (def, if, else, while, for, return) red;
  variable and parameter names purple (#5B2A86); strings and numbers blue (#1F4FA0);
  built-in calls like print/input and comments (# …) green (#2E7D32);
  everything else near-black.
- Indentation shown faithfully; a thin dashed pink vertical guide line may mark indented blocks.

Annotations and shapes:
- Callouts: small rounded rectangles with a thin colored outline (red, purple, green or black)
  matching what they point at, containing short Czech text. Connected to the target
  by a thin straight line ending in a small filled dot on the target.
- Flow arrows: thick, solid red arrows with rounded bends. Arrows to program output are green.
- Highlighted items: light pink fill (#FDE3E3) with red outline.
- Program output / result: rounded box with light green fill and green outline, green text.
- Sections separated by a red dashed horizontal line across the full width.
- Grids of characters/values: row of equal rounded square cells with red outline.

Text rules:
- ALL visible text is Czech with correct diacritics (č, ř, š, ž, ě, ů, á, í, é, ý), except Python code.
- Render every quoted text string from the brief EXACTLY, letter by letter. Do not add any
  other text, captions, watermarks or signatures.
- Python code must be rendered exactly as given, character by character.
<!-- STYL-END -->
