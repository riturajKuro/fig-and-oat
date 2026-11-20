"""Build one-word 'pop' ASS captions from Whisper word timings, spelled from the authored script.

python build_captions.py <key> <ypos>   -> writes <key>.ass and prints a word/timing table
"""
import difflib, json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
from PIL import ImageFont
FONT = ImageFont.truetype(os.path.join(HERE, "fonts", "Poppins-ExtraBold.ttf"), 124)
SCRIPTS = {
 "ugc-1": "My two-step routine for rough, bumpy skin. Most nights, on dry skin, two or three swipes of this glycolic stick. Leave it on, no rinse, no sticky hands. Once or twice a week in the shower, this mitt: wet it, wring it out, long strokes. Acids plus friction.",
 "ugc-2": "Switched razors and your legs still look bumpy? It might not be your razor. Those little dots are often dead skin around the hair follicles. This is a glycolic acid stick, with salicylic acid and shea butter. Swipe it on dry skin, leave it on, no rinse. It smooths the look of rough, bumpy skin.",
 "ugc-4": "Bumpy legs that a new razor didn't fix? This is my no-mess fix. A glycolic acid stick: two or three swipes on dry skin, leave it on. No rinse, no sticky hands. Start every other night. And grab two, the mitt's free.",
}
OVERRIDES = {"ugc-2": [(12.8, 1045, 96)]}   # (from second, y, max font size): move captions off the label close-up
HIGHLIGHT = {"bumpy", "glycolic", "acid", "salicylic", "shea", "rinse", "free", "razor", "razors", "mess", "no-mess",
             "smooths", "smooth", "swipe", "swipes", "stick", "mitt", "mitt's", "friction", "sticky", "two-step", "dry"}
WHITE, HONEY = "&H00FFFFFF", "&H006FC8F7"   # ASS is &HAABBGGRR -> honey-gold #F7C86F

def norm(t):
    return re.sub(r"[^a-z0-9']", "", t.lower().replace("’", "'"))

def script_tokens(s):
    return [t for t in re.findall(r"[A-Za-z0-9'’\-]+", s)]

def align(words, script):
    """Whisper supplies timing; script supplies spelling. Where they disagree, keep what was actually said."""
    st = script_tokens(script)
    a, b = [norm(w["w"]) for w in words], [norm(t) for t in st]
    out, notes = [], []
    for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(a=a, b=b, autojunk=False).get_opcodes():
        if tag == "equal":
            for k in range(i2 - i1):
                out.append({**words[i1 + k], "t": st[j1 + k]})
        elif tag == "replace" and (i2 - i1) == (j2 - j1):
            for k in range(i2 - i1):
                out.append({**words[i1 + k], "t": st[j1 + k]})
                notes.append(f"spelling: heard '{words[i1+k]['w']}' -> script '{st[j1+k]}'")
        else:
            for k in range(i1, i2):
                out.append({**words[k], "t": re.sub(r"[^\w'’\-]", "", words[k]["w"])})
            if j2 > j1 or i2 > i1:
                notes.append(f"{tag}: said {[w['w'] for w in words[i1:i2]]} vs script {st[j1:j2]} (kept what was said)")
    return [w for w in out if w["t"]], notes

def ts(x):
    h, r = divmod(max(x, 0), 3600); m, s = divmod(r, 60)
    return f"{int(h)}:{int(m):02d}:{s:05.2f}"

def build(key, ypos, dur):
    words = json.load(open(os.path.join(HERE, key + "_words.json")))
    al, notes = align(words, SCRIPTS[key])
    # join split hyphenated words ("two" + "-step")
    j = []
    for w in al:
        if j and w["t"].startswith("-"):
            j[-1] = {**j[-1], "t": j[-1]["t"] + w["t"], "e": w["e"]}
        else:
            j.append(dict(w))
    # pair words too short to read (<0.12 s) with the next word
    al, i = [], 0
    while i < len(j):
        w = j[i]
        if i + 1 < len(j) and (j[i + 1]["s"] - w["s"]) < 0.16:
            n = j[i + 1]; al.append({**w, "t": w["t"] + " " + n["t"], "e": n["e"]}); i += 2
        else:
            al.append(w); i += 1
    LEAD = 0.03
    for w in al:
        w["s"] = max(0.0, w["s"] - LEAD)
    ev = []
    for i, w in enumerate(al):
        start = w["s"]
        nxt = al[i + 1]["s"] if i + 1 < len(al) else None
        end = max(w["e"] + 0.05, start + 0.18)            # never flash shorter than ~4 frames
        if nxt is not None:
            end = nxt if (nxt - w["e"]) < 0.35 else min(end + 0.15, nxt)   # hand straight over, hold briefly at pauses
        end = min(end, dur - 0.02)
        word = w["t"].upper().replace("’", "'")
        col = HONEY if any(norm(p) in HIGHLIGHT for p in w["t"].split()) else WHITE
        # big by default; shrink only if the real rendered width (incl. 108% pop + outline) would pass 620 px of 720
        y, cap = ypos, 124
        for t0, oy, ofs in OVERRIDES.get(key, []):
            if start >= t0: y, cap = oy, ofs
        fs = cap
        while fs > 60 and FONT.font_variant(size=fs).getlength(word) * 1.08 + 24 > 620:
            fs -= 2
        pop = r"{\fscx72\fscy72\t(0,80,\fscx108\fscy108)\t(80,150,\fscx100\fscy100)}"
        ev.append((start, end, f"{{\\pos(360,{y})\\c{col}\\fs{fs}}}{pop}{word}"))
    head = f"""[Script Info]
ScriptType: v4.00+
PlayResX: 720
PlayResY: 1280
WrapStyle: 2
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Pop,Poppins ExtraBold,124,&H00FFFFFF,&H00FFFFFF,&H00141414,&H80000000,0,0,0,0,100,100,1,0,1,7,4,5,40,40,0,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
    lines = [f"Dialogue: 0,{ts(s)},{ts(e)},Pop,,0,0,0,,{t}" for s, e, t in ev]
    open(os.path.join(HERE, key + ".ass"), "w", encoding="utf-8").write(head + "\n".join(lines) + "\n")
    gaps = [round(ev[i+1][0] - ev[i][1], 2) for i in range(len(ev) - 1)]
    overl = [i for i in range(len(ev) - 1) if ev[i][1] > ev[i+1][0] + 1e-3]
    print(f"== {key}: {len(ev)} words, first {ev[0][0]:.2f}s, last ends {ev[-1][1]:.2f}s of {dur:.2f}s, "
          f"overlaps {overl}, shortest {min(e - s for s, e, _ in ev):.2f}s, longest gap {max(gaps) if gaps else 0}s")
    for n in notes: print("   ", n)
    print("   ", " | ".join(f"{t.split('}')[-1]}@{s:.2f}" for s, e, t in ev))

if __name__ == "__main__":
    build(sys.argv[1], int(sys.argv[2]), float(sys.argv[3]))
