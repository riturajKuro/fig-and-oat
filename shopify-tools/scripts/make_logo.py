import os, sys
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.boundsPen import BoundsPen
from PIL import Image, ImageFont, ImageDraw

FONT, OUT = sys.argv[1], sys.argv[2]
os.makedirs(OUT, exist_ok=True)

FIG, OAT, HONEY, LEAF = "#4A1F3D", "#F3EADB", "#B08A5B", "#7A8450"
HONEY_D, LEAF_D = "#D9B98C", "#A9B37A"

f = TTFont(FONT)
gs, cmap, hmtx = f.getGlyphSet(), f.getBestCmap(), f["hmtx"]
upm = f["head"].unitsPerEm


def layout(segs, track=0):
    """segs: [(text, color)] -> list of (path_d, color), bounds"""
    x, out = 0, []
    bp = BoundsPen(gs)
    for text, color in segs:
        for ch in text:
            g = cmap[ord(ch)]
            sp = SVGPathPen(gs)
            # flip y (font units are y-up)
            gs[g].draw(TransformPen(sp, (1, 0, 0, -1, x, 0)))
            gs[g].draw(TransformPen(bp, (1, 0, 0, 1, x, 0)))
            out.append((sp.getCommands(), color))
            x += hmtx[g][0] + track
    xmin, ymin, xmax, ymax = bp.bounds
    return out, (xmin, -ymax, xmax - xmin, ymax - ymin)


def svg(segs, name, pad=0.12, bg=None, square=False, track=0):
    paths, (x, y, w, h) = layout(segs, track)
    p = pad * max(w, h)
    if square:
        s = max(w, h) + 2 * p
        vx, vy, vw, vh = x - (s - w) / 2, y - (s - h) / 2, s, s
    else:
        vx, vy, vw, vh = x - p, y - p, w + 2 * p, h + 2 * p
    body = "".join(f'<path d="{d}" fill="{c}"/>' for d, c in paths)
    rect = f'<rect x="{vx}" y="{vy}" width="{vw}" height="{vh}" fill="{bg}"/>' if bg else ""
    with open(os.path.join(OUT, name), "w") as fh:
        fh.write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vx:.0f} {vy:.0f} {vw:.0f} {vh:.0f}">'
                 f'<title>fig&amp;oat.</title>{rect}{body}</svg>')


def png(segs, name, width, pad=0.12, bg=None, square=False):
    # render big then downsample for clean edges
    size = 1000
    font = ImageFont.truetype(FONT, size)
    text = "".join(t for t, _ in segs)
    l, t, r, b = font.getbbox(text)
    w, h = r - l, b - t
    p = int(pad * max(w, h))
    W, H = (max(w, h) + 2 * p,) * 2 if square else (w + 2 * p, h + 2 * p)
    img = Image.new("RGBA", (W, H), bg or (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    x0, y0 = (W - w) // 2 - l, (H - h) // 2 - t
    x = x0
    for seg, color in segs:
        d.text((x, y0), seg, font=font, fill=color)
        x += font.getlength(seg)
    scale = width / W
    img.resize((width, round(H * scale)), Image.LANCZOS).save(os.path.join(OUT, name))


color_light = [("fig", FIG), ("&", HONEY), ("oat", FIG), (".", LEAF)]
color_dark = [("fig", OAT), ("&", HONEY_D), ("oat", OAT), (".", LEAF_D)]
mono_fig = [("fig&oat.", FIG)]
mono_oat = [("fig&oat.", OAT)]
icon = [("f", OAT), ("&", HONEY_D), ("o", OAT), (".", LEAF_D)]

for segs, base in [(color_light, "logo-fig"), (color_dark, "logo-cream"),
                   (mono_fig, "logo-mono-fig"), (mono_oat, "logo-mono-cream")]:
    svg(segs, base + ".svg")
    png(segs, base + ".png", 2000)
png(color_light, "shopify-header-logo.png", 600, pad=0.04)

svg(icon, "icon.svg", pad=0.28, bg=FIG, square=True)
png(icon, "icon-instagram-1080.png", 1080, pad=0.28, bg=FIG, square=True)
png(icon, "favicon-512.png", 512, pad=0.18, bg=FIG, square=True)
print("done", sorted(os.listdir(OUT)))
