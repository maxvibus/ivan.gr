"""Σκίτσο για «Το χρώμα της τίγρης» (15.11.2026).
Δεξιά: ψηλά χόρτα, και μέσα τους μια τίγρη που οι ρίγες της είναι ίδιες με τα στελέχη· σχεδόν δεν φαίνεται.
Αριστερά: ένας ηλικιωμένος άνθρωπος κρατά ένα φύλλο χαρτί (ώχρα) και δείχνει με το απλωμένο χέρι προς τα χόρτα.
Δεν έγραψε το χρώμα· το έδειξε."""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pen import Pen, OCHRE
from sketchbook import person, PI

ALT = ('Δεξιά, ψηλά χόρτα· ανάμεσά τους μια τίγρη ξαπλωμένη, που οι ρίγες της μοιάζουν με τα στελέχη και σχεδόν δεν ξεχωρίζει. '
       'Αριστερά, ένας ηλικιωμένος άνθρωπος με ένα φύλλο χαρτί στο ένα χέρι δείχνει με το άλλο προς το σημείο όπου κρύβεται.')


def draw(p):
    fy = 600
    p.floor(fy, 40, 1160)
    r = p.r
    # χόρτα: όρθια στελέχη με ελαφριά κλίση
    for k in range(70):
        x = 600 + k * 8 + r.uniform(-3, 3)
        top = fy - r.uniform(150, 250)
        lean = r.uniform(-14, 14)
        p.line([(x, fy), (x + lean * .4, (fy + top) / 2), (x + lean, top)], w=round(r.uniform(1.3, 1.8), 1), op=round(r.uniform(.35, .55), 2), a=.6)
    # τίγρη ξαπλωμένη μέσα στα χόρτα
    hx, hy = 760, 520
    p.ring(hx, hy, 36, 32, w=2.0, op=.5)                                   # κεφάλι
    p.line([(hx - 26, hy - 22), (hx - 20, hy - 44), (hx - 6, hy - 30)], w=1.8, op=.5)   # αυτιά
    p.line([(hx + 6, hy - 31), (hx + 20, hy - 46), (hx + 26, hy - 22)], w=1.8, op=.5)
    p.line([(hx + 30, hy - 16), (hx + 90, hy - 42), (hx + 200, hy - 50), (hx + 300, hy - 40), (hx + 350, hy - 14), (hx + 360, hy + 30)], w=2.0, op=.5)   # ράχη
    p.line([(hx + 24, hy + 26), (hx + 120, hy + 58), (hx + 260, hy + 60), (hx + 360, hy + 34)], w=2.0, op=.5)   # κοιλιά
    p.line([(hx + 360, hy + 30), (hx + 400, hy + 10), (hx + 420, hy - 30), (hx + 440, hy - 40)], w=1.8, op=.45)      # ουρά
    p.line([(hx - 30, fy - 2), (hx + 40, fy - 6), (hx + 60, hy + 50)], w=1.8, op=.45)                                 # μπροστινό πόδι
    # οι ρίγες: ίδιες με τα στελέχη
    for k in range(9):
        x = hx + 70 + k * 32 + r.uniform(-4, 4)
        p.line([(x, hy - 44 + r.uniform(0, 8)), (x + r.uniform(-6, 6), hy - 6), (x + r.uniform(-8, 8), hy + 30)], w=1.8, op=.55, a=.6)
    for k in range(25):
        x = 700 + k * 17 + r.uniform(-4, 4); top = fy - r.uniform(90, 160)
        p.line([(x, fy), (x + r.uniform(-8, 8), top)], w=1.5, op=.45, a=.6)
    # τα μάτια: δύο μικρά σημάδια, χωρίς λάμψη
    p.dot(hx - 12, hy - 4, 2.4, op=.8); p.dot(hx + 10, hy - 4, 2.4, op=.8)
    # ο άνθρωπος που δείχνει
    x = 270
    sh = person(p, x, fy, h=.95, look=1, glasses=True,
                arm=[(x + 80, fy - 228), (x + 150, fy - 238), (x + 200, fy - 232)])
    # το φύλλο χαρτί στο άλλο χέρι (ώχρα)
    px, py = x - 70, sh + 120
    p.group('sk-glow')
    for a, b in (((px, py), (px + 48, py - 6)), ((px + 48, py - 6), (px + 54, py + 58)), ((px + 54, py + 58), (px + 6, py + 64)), ((px + 6, py + 64), (px, py))):
        p.line(p.seg(*a, *b, 3), w=2, col=OCHRE)
    for i in range(3):
        p.line(p.seg(px + 10, py + 16 + i * 13, px + 42, py + 13 + i * 13, 4), w=1.2, col=OCHRE, op=.8)
    p.end()
    return ALT


def svg():
    p = Pen(seed=sum(map(ord, 'to-chroma-tis-tigris')))
    draw(p)
    return p.svg(ALT)


if __name__ == '__main__':
    out = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'assets', 'sketches', 'to-chroma-tis-tigris.svg')
    open(out, 'w', encoding='utf-8').write(svg()); print(out)
