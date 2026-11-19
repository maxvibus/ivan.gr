"""Σκίτσο για «Πού χωρούν όσοι δεν αντέχουμε;» (19.11.2026).
Αριστερά: τρία όμοια πλαίσια, σαν οθόνες ή κουτιά, το καθένα με μια ίδια άκαμπτη φιγούρα (οι ρόλοι, το «τι»).
Δεξιά: ένα ανοιχτό πλαίσιο πόρτας· στο κατώφλι ένας άνθρωπος με γυαλιά, γυρισμένος προς τα πλαίσια.
Δεν φεύγει. Στο στήθος του ένα μικρό σημάδι σε ώχρα, αγκάθι ή παρηγοριά."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pen import Pen, OCHRE
from sketchbook import person

ALT = ('Αριστερά, τρία όμοια πλαίσια, το καθένα με μια ίδια άκαμπτη φιγούρα. '
       'Δεξιά, ένας άνθρωπος με γυαλιά στέκεται στο κατώφλι μιας ανοιχτής πόρτας και κοιτάζει προς τα πλαίσια. '
       'Στο στήθος του, ένα μικρό σημάδι.')


def draw(p):
    fy = 600
    p.floor(fy, 40, 1160)
    r = p.r
    # τα τρία πλαίσια των ρόλων: ίδια, αχνά
    for i in range(3):
        x0 = 70 + i * 205; x1 = x0 + 170; y0 = 250; y1 = 560
        p.line(p.poly([(x0, y1), (x0, y0), (x1, y0), (x1, y1), (x0, y1)], 4), w=1.6, op=.4, a=.5)
        cx = (x0 + x1) / 2
        # η ίδια φιγούρα: κεφάλι, κορμός, χέρια κολλημένα
        p.ring(cx, y0 + 62, 22, w=1.5, op=.38)
        p.line(p.seg(cx, y0 + 86, cx, y0 + 210, 5), w=1.6, op=.38)
        p.line([(cx - 30, y0 + 100), (cx - 30, y0 + 190)], w=1.4, op=.32)
        p.line([(cx + 30, y0 + 100), (cx + 30, y0 + 190)], w=1.4, op=.32)
        p.line([(cx - 30, y0 + 100), (cx + 30, y0 + 100)], w=1.4, op=.32)
        p.line(p.seg(cx - 12, y0 + 210, cx - 14, y1 - 6, 4), w=1.4, op=.32)
        p.line(p.seg(cx + 12, y0 + 210, cx + 14, y1 - 6, 4), w=1.4, op=.32)
    # το πλαίσιο της πόρτας, ανοιχτό
    d0, d1, dt = 860, 1080, 150
    p.line(p.seg(d0, fy, d0, dt, 8), w=2.6)
    p.line(p.seg(d1, fy, d1, dt, 8), w=2.6)
    p.line(p.seg(d0 - 10, dt, d1 + 10, dt, 6), w=2.6)
    # το φύλλο της πόρτας, ανοιχτό προς τα έξω (δεξιά), σε προοπτική
    p.line([(d1, dt + 8), (d1 + 70, dt + 40)], w=1.8, op=.6)
    p.line([(d1, fy - 4), (d1 + 70, fy - 30)], w=1.8, op=.6)
    p.line([(d1 + 70, dt + 40), (d1 + 70, fy - 30)], w=1.8, op=.6)
    # το κατώφλι
    p.line(p.seg(d0 - 16, fy + 8, d1 + 16, fy + 8, 6), w=2.2, op=.8)
    # ο άνθρωπος στο κατώφλι, γυρισμένος προς τα αριστερά
    x = 970
    person(p, x, fy, h=.95, look=-1, glasses=True)
    # το σημάδι στο στήθος (ώχρα)
    hx, hy = x - 4, fy - 238
    p.group('sk-glow')
    p.line(([(hx, hy + 14), (hx - 12, hy + 2), (hx - 9, hy - 8), (hx, hy - 3),
                     (hx + 9, hy - 8), (hx + 12, hy + 2), (hx, hy + 14)]), w=2.2, col=OCHRE)
    p.end()
    return ALT


def svg():
    p = Pen(seed=sum(map(ord, 'pou-chorane-osoi-den-antechoume')))
    draw(p)
    return p.svg(ALT)


if __name__ == '__main__':
    out = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'assets', 'sketches', 'pou-chorane-osoi-den-antechoume.svg')
    open(out, 'w', encoding='utf-8').write(svg()); print(out)
