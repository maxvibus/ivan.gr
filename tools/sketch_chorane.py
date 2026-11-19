"""Σκίτσο για «Πού χωρούν όσοι δεν αντέχουμε;» (19.11.2026, δεύτερη μορφή, κατά την περιγραφή του Ιβάν).
Εθνική οδός με τρεις λωρίδες σε κάθε πλευρά, σε προοπτική προς τον ορίζοντα, όπου υψώνεται ο Όλυμπος.
Ένα αυτοκίνητο από πίσω: μπροστά ο πατέρας και η μητέρα, πίσω η γιαγιά και το παιδί στο παράθυρο.
Από το παράθυρο βγαίνουν λόγια και τραγούδια (ώχρα) και μένουν πίσω, σβήνοντας.
Πάνω από τον δρόμο μια ηλεκτρονική πινακίδα δείχνει στους οδηγούς τον τίτλο του κειμένου."""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pen import Pen, OCHRE, FONT

ALT = ('Εθνική οδός με τρεις λωρίδες σε κάθε πλευρά, που χάνεται προς τον Όλυμπο στον ορίζοντα. '
       'Ένα αυτοκίνητο με μια οικογένεια ταξιδεύει προς το βουνό· από το πίσω παράθυρο ένα παιδί τραγουδά, '
       'και τα λόγια και οι νότες του μένουν πίσω στον αέρα και σβήνουν. '
       'Πάνω από τον δρόμο, μια ηλεκτρονική πινακίδα γράφει: Πού χωρούν όσοι δεν αντέχουμε;')

VX, HY = 470, 330          # σημείο φυγής, ορίζοντας
BOT = 720


def X(f, y):
    """Θέση στον δρόμο: f από -1 (αριστερή άκρη) έως 1 (δεξιά άκρη), σε βάθος y."""
    return VX + f * 820 * (y - HY) / (BOT - HY)


MED = .045                 # μισό πλάτος διαχωριστικού


def lane_f(side, k):
    """Όριο λωρίδας k (0..3) στην πλευρά side (+1 δεξιά, -1 αριστερά)."""
    return side * (MED + (1 - MED) * k / 3)


def hide(p, pts):
    """Καλύπτει ό,τι βρίσκεται πίσω (χρώμα του φόντου της σελίδας, χωρίς περίγραμμα)."""
    p.out.append(f'<path d="{p.smooth(pts, True)}" stroke="none" style="fill:var(--bg,#FBF8F2)"/>')


def draw(p):
    r = p.r
    # --- ο Όλυμπος στον ορίζοντα: πλατύς όγκος, κοφτές κορυφές στη μέση ----------
    ridge = [(140, HY), (220, 314), (300, 296), (360, 270), (410, 246), (452, 226), (478, 200), (496, 206),
             (512, 178), (528, 186), (544, 150), (556, 160), (570, 128), (582, 142), (594, 120), (606, 134),
             (622, 126), (640, 156), (662, 168), (690, 162), (720, 190), (770, 214), (840, 244), (920, 272), (1000, 298), (1080, HY)]
    DX = VX - 600
    ridge = [(x + DX, y) for x, y in ridge]
    p.line(ridge, w=1.8, op=.55, a=.6)
    for (x0, y0), (x1, y1) in (((570, 128), (552, 196)), ((594, 120), (598, 184)), ((622, 126), (648, 196)),
                               ((544, 150), (520, 214)), ((512, 178), (488, 236)), ((690, 162), (712, 222))):
        p.line(p.seg(x0 + DX, y0, x1 + DX, y1, 5), w=1.1, op=.32, a=.8)
    p.line([(x + DX, y) for x, y in [(468, 222), (500, 208), (530, 200), (560, 176), (590, 160), (620, 166), (660, 188), (700, 196)]], w=1.0, op=.28, a=.6)
    p.line([(60, HY), (150, 316), (240, HY)], w=1.2, op=.3)
    p.line([(1010, HY), (1100, 318), (1190, HY)], w=1.2, op=.3)
    p.line(p.seg(20, HY, 1180, HY, 24), w=1.2, op=.35)

    # --- ο δρόμος --------------------------------------------------------------
    for s in (-1, 1):
        p.line(p.seg(X(s, HY), HY, X(s, BOT), BOT, 10), w=2.2, op=.85)            # άκρες
        p.line(p.seg(X(s * MED, HY), HY, X(s * MED, BOT), BOT, 10), w=1.6, op=.6)  # στηθαίο
        for k in (1, 2):                                                       # διακεκομμένες λωρίδες
            f = lane_f(s, k)
            t = 0.0
            while True:
                y0 = HY + (BOT - HY) * t; y1 = HY + (BOT - HY) * min(1, t + .06 * (0.25 + t))
                if y0 >= BOT: break
                p.line([(X(f, y0), y0), (X(f, y1), y1)], w=1.4, op=.55, a=.3)
                t += .13 * (0.25 + t)
    # το διαχωριστικό στη μέση
    p.line(p.seg(VX, HY, VX, BOT, 10), w=1.2, op=.35)

    # --- η πινακίδα πάνω από το ρεύμα μας, μπροστά τους -------------------------
    gy = 468
    gl, gr = X(MED, gy) + 4, X(1, gy) + 10
    beam = 262
    p.line(p.seg(gl, gy, gl, beam - 6, 6), w=2.2)
    p.line(p.seg(gr, gy, gr, beam - 6, 6), w=2.2)
    p.line(p.seg(gl - 8, beam, gr + 8, beam, 10), w=2.2)
    p.line(p.seg(gl - 8, beam - 10, gr + 8, beam - 10, 10), w=1.4, op=.7)
    for k in range(1, 8):                                     # δικτύωμα της γέφυρας
        xa = gl + (gr - gl) * (k - 1) / 7; xb = gl + (gr - gl) * k / 7
        p.line([(xa, beam - 10), (xb, beam)], w=1.0, op=.5)
    sx0, sx1, sy0, sy1 = (gl + gr) / 2 - 165, (gl + gr) / 2 + 165, beam + 4, beam + 84
    for xx in (sx0 + 40, sx1 - 40):
        p.line(p.seg(xx, beam, xx, sy0, 2), w=1.4)
    hide(p, [(sx0, sy0), (sx1, sy0), (sx1, sy1), (sx0, sy1)])
    p.line(p.poly([(sx0, sy0), (sx1, sy0), (sx1, sy1), (sx0, sy1), (sx0, sy0)], 6), w=2.4)
    p.line(p.poly([(sx0 + 8, sy0 + 8), (sx1 - 8, sy0 + 8), (sx1 - 8, sy1 - 8), (sx0 + 8, sy1 - 8), (sx0 + 8, sy0 + 8)], 6), w=1.1, op=.45)
    p.group('sk-glow')
    p.text(round((sx0 + sx1) / 2), round(sy0 + 36), 'ΠΟΥ ΧΩΡΟΥΝ ΟΣΟΙ', size=22, italic=False, anchor='middle', spacing=3, col=OCHRE)
    p.text(round((sx0 + sx1) / 2), round(sy0 + 64), 'ΔΕΝ ΑΝΤΕΧΟΥΜΕ;', size=22, italic=False, anchor='middle', spacing=3, col=OCHRE)
    p.end()

    # --- το αυτοκίνητο, από πίσω, στη μεσαία λωρίδα, πριν από τη γέφυρα --------
    cy = 640
    cx = (X(lane_f(1, 1), cy) + X(lane_f(1, 2), cy)) / 2
    S = 1.0
    w, h = 210 * S, 132 * S
    x0, x1 = cx - w / 2, cx + w / 2
    yb, yt = cy - 18 * S, cy - h
    def L(pts, **k): p.line(pts, **k)
    hide(p, [(x0, cy), (x0, yb - 46 * S), (x0 + 10 * S, yb - 70 * S), (x0 + 30 * S, yt), (x1 - 30 * S, yt), (x1 - 10 * S, yb - 70 * S), (x1, yb - 46 * S), (x1, cy)])
    L([(x0, yb), (x0 - 4 * S, yb - 46 * S), (x0 + 6 * S, yb - 70 * S), (x1 - 6 * S, yb - 70 * S), (x1 + 4 * S, yb - 46 * S), (x1, yb), (x0, yb)], w=2.6)
    L([(x0 + 10 * S, yb - 70 * S), (x0 + 30 * S, yt), (x1 - 30 * S, yt), (x1 - 10 * S, yb - 70 * S)], w=2.4)
    wy0, wy1 = yt + 7 * S, yb - 75 * S
    L(p.poly([(x0 + 24 * S, wy1), (x0 + 38 * S, wy0), (x1 - 38 * S, wy0), (x1 - 24 * S, wy1), (x0 + 24 * S, wy1)], 4), w=1.5, op=.8)
    for a0, a1 in ((x0 + 4 * S, x0 + 36 * S), (x1 - 36 * S, x1 - 4 * S)):
        L(p.poly([(a0, yb - 44 * S), (a1, yb - 44 * S), (a1, yb - 31 * S), (a0, yb - 31 * S), (a0, yb - 44 * S)], 2), w=2, col=OCHRE)
    L(p.poly([(cx - 26 * S, yb - 30 * S), (cx + 26 * S, yb - 30 * S), (cx + 26 * S, yb - 15 * S), (cx - 26 * S, yb - 15 * S), (cx - 26 * S, yb - 30 * S)], 2), w=1.3, op=.7)
    for wx in (x0 + 14 * S, x1 - 32 * S):
        L(p.poly([(wx, yb), (wx + 18 * S, yb), (wx + 18 * S, cy), (wx, cy), (wx, yb)], 2), w=2.2)
    L(p.seg(x0 - 10, cy + 2, x1 + 10, cy + 2, 6), w=1.2, op=.4)
    # μέσα: μπροστά ο πατέρας (οδηγός) και η μητέρα, πίσω δεξιά η γιαγιά με κότσο
    hf = wy0 + 20 * S
    p.ring(cx - 26 * S, hf, 11 * S, 12 * S, w=1.8, op=.7)
    p.ring(cx + 22 * S, hf + 1, 10.5 * S, 11.5 * S, w=1.8, op=.7)
    p.ring(cx + 40 * S, hf + 17 * S, 13 * S, 14 * S, w=2.0)
    p.ring(cx + 40 * S, hf + 1 * S, 5 * S, w=1.6)
    # το παιδί στο αριστερό πίσω παράθυρο, γυρισμένο προς τα πίσω, με ανοιχτό στόμα
    kx, ky = x0 + 16 * S, yt + 30 * S
    p.ring(kx, ky, 14 * S, 15 * S, w=2.4)
    p.line(p.arc(kx + 2, ky - 10 * S, 11 * S, 5 * S, math.pi * 1.05, math.pi * 1.95, 8), w=1.6, op=.8)
    p.ring(kx - 4 * S, ky + 6 * S, 3, w=1.7)
    p.dot(kx - 7 * S, ky - 3 * S, 1.6); p.dot(kx + 4 * S, ky - 3 * S, 1.6)

    # --- τα λόγια και τα τραγούδια μένουν πίσω, προς εμάς, και σβήνουν ---------
    # γύρω από το αμάξι και πίσω του, προς εμάς: όσο μένουν πίσω μεγαλώνουν και σβήνουν
    trail = [('λα λα λα', 26, .95, kx - 60, ky - 30), ('♪', 30, .9, kx - 30, ky - 64), ('κι άλλο!', 28, .78, x1 + 60, yt + 8),
             ('♫', 34, .7, x1 + 40, yt - 40), ('λα λα', 34, .55, kx - 120, ky + 40), ('♪', 40, .45, x1 + 92, yb - 10),
             ('τραλαλά', 44, .32, kx - 170, ky + 110), ('♫', 50, .24, x1 + 120, cy + 34), ('λα', 56, .14, kx - 230, cy + 46)]
    for i, (s, size, op, x, y) in enumerate(trail):
        if i < 4: p.group('sk-glow')
        p.text(round(x), round(y), s, size=size, italic=True, anchor='middle', op=op, col=OCHRE)
        if i < 4: p.end()
    for i in range(2):
        p.line(p.seg(kx - 18, ky - 8 + i * 10, kx - 36, ky - 6 + i * 10, 3), w=1.3, op=.5)
    return ALT


def svg():
    p = Pen(seed=sum(map(ord, 'pou-chorane-osoi-den-antechoume')))
    draw(p)
    return p.svg(ALT)


if __name__ == '__main__':
    out = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'assets', 'sketches', 'pou-chorane-osoi-den-antechoume.svg')
    open(out, 'w', encoding='utf-8').write(svg()); print(out)
