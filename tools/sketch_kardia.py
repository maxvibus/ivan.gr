"""Σκίτσο για «Μου απαντούν όσοι έχουν καρδιά, όχι χαρτιά» (18.11.2026).
Αριστερά: μια ψηλή στοίβα από χαρτιά και φακέλους, αχνή, βουβή.
Στη μέση: ένας άνθρωπος με γυαλιά, γυρισμένος προς τα δεξιά, κρατά ένα φύλλο χαρτί.
Δεξιά: μια μισάνοιχτη καγκελόπορτα αυλής· από εκεί ένα μικρό γράμμα (ώχρα) έρχεται προς το μέρος του.
Η απάντηση ήρθε από απέναντι."""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pen import Pen, OCHRE
from sketchbook import person, PI

ALT = ('Αριστερά, μια ψηλή στοίβα από χαρτιά και φακέλους, αχνή και βουβή. '
       'Στη μέση, ένας άνθρωπος με γυαλιά κρατά ένα φύλλο χαρτί και κοιτάζει δεξιά. '
       'Δεξιά, μια μισάνοιχτη καγκελόπορτα αυλής, από όπου ένα μικρό γράμμα έρχεται προς το μέρος του.')


def draw(p):
    fy = 600
    p.floor(fy, 40, 1160)
    r = p.r
    # η στοίβα των χαρτιών: αρχιτεκτονικά, αχνά
    y = fy
    k = 0
    while y > 170:
        h = r.uniform(10, 22)
        x0 = 90 + r.uniform(-10, 10); x1 = 270 + r.uniform(-10, 10)
        p.line(p.poly([(x0, y), (x0, y - h), (x1, y - h), (x1, y)], 4), w=1.4, op=round(r.uniform(.25, .35), 2), a=.6)
        if k % 3 == 1:   # ένας φάκελος με κορδόνι
            p.line(p.seg(x0 + 20, y - h / 2, x1 - 20, y - h / 2, 6), w=1.1, op=.22, a=.5)
        y -= h; k += 1
    # ο άνθρωπος
    x = 520
    sh = person(p, x, fy, h=.95, look=1, glasses=True,
                arm=[(x + 70, fy - 236), (x + 104, fy - 252), (x + 118, fy - 262)])
    # το φύλλο που κρατά (μελάνι, όχι ώχρα: είναι το δικό του ερώτημα)
    px, py = x + 112, fy - 300
    p.line(p.poly([(px, py), (px + 44, py - 4), (px + 48, py + 54), (px + 4, py + 58), (px, py)], 3), w=1.8, op=.85)
    for i in range(3):
        p.line(p.seg(px + 9, py + 14 + i * 12, px + 38, py + 12 + i * 12, 4), w=1.1, op=.55)
    # η καγκελόπορτα, μισάνοιχτη
    g0, g1, gt = 900, 1090, 380
    p.line(p.seg(g0, fy, g0, gt - 20, 6), w=2.6)                      # κολόνες
    p.line(p.seg(g1, fy, g1, gt - 20, 6), w=2.6)
    p.line(p.seg(g0 - 14, gt - 20, g0 + 14, gt - 20, 3), w=2.4)
    p.line(p.seg(g1 - 14, gt - 20, g1 + 14, gt - 20, 3), w=2.4)
    # φύλλο της πόρτας ανοιχτό προς τα μέσα, σε προοπτική
    hx, hy0, hy1 = g1, gt + 10, fy - 10
    ox, oy0, oy1 = g1 - 120, gt + 40, fy - 30
    p.line([(hx, hy0), (ox, oy0)], w=2.2); p.line([(hx, hy1), (ox, oy1)], w=2.2)
    p.line([(ox, oy0), (ox, oy1)], w=2.2)
    for t in (.2, .4, .6, .8):
        bx = hx + (ox - hx) * t; by0 = hy0 + (oy0 - hy0) * t; by1 = hy1 + (oy1 - hy1) * t
        p.line(p.seg(bx, by0, bx, by1, 5), w=1.6, op=.8)
    # χαμηλός φράχτης δεξιά κι αριστερά της πόρτας
    for x0, x1 in ((760, g0), (g1, 1160)):
        p.line(p.seg(x0, fy - 110, x1, fy - 110, 8), w=1.4, op=.35)
        for xx in range(int(x0) + 10, int(x1), 26):
            p.line(p.seg(xx, fy, xx, fy - 118, 3), w=1.2, op=.3)
    # το γράμμα που έρχεται από απέναντι (ώχρα), με δυο γραμμούλες κίνησης
    ex, ey = 760, 300
    p.group('sk-glow')
    p.line(p.poly([(ex, ey), (ex + 58, ey - 6), (ex + 62, ey + 34), (ex + 4, ey + 40), (ex, ey)], 3), w=2.2, col=OCHRE)
    p.line([(ex + 1, ey + 1), (ex + 32, ey + 20), (ex + 59, ey - 5)], w=1.8, col=OCHRE)
    p.end()
    for i in range(2):
        yy = ey + 8 + i * 18
        p.line(p.seg(ex + 78, yy, ex + 112, yy - 2, 4), w=1.4, op=.5)
    return ALT


def svg():
    p = Pen(seed=sum(map(ord, 'kardia-ochi-chartia')))
    draw(p)
    return p.svg(ALT)


if __name__ == '__main__':
    out = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'assets', 'sketches', 'kardia-ochi-chartia.svg')
    open(out, 'w', encoding='utf-8').write(svg()); print(out)
