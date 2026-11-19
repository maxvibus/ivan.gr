"""Σκίτσο για «Πού χωρούν όσοι δεν αντέχουμε;» (19.11.2026, δεύτερη μορφή, κατά την περιγραφή του Ιβάν).
Εθνική οδός με τρεις λωρίδες σε κάθε πλευρά, σε προοπτική προς τον ορίζοντα, όπου υψώνεται ο Όλυμπος.
Ένα αυτοκίνητο από πίσω: μπροστά ο πατέρας και η μητέρα, πίσω η γιαγιά και το παιδί στο παράθυρο.
Από το στόμα του παιδιού βγαίνουν νότες (ώχρα) και ανεβαίνουν γύρω γύρω από το αμάξι ως τον ουρανό.
Πάνω από τον δρόμο μια ηλεκτρονική πινακίδα δείχνει στους οδηγούς τον τίτλο του κειμένου."""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pen import Pen, OCHRE, FONT

ALT = ('Εθνική οδός με τρεις λωρίδες σε κάθε πλευρά, που χάνεται προς τον Όλυμπο στον ορίζοντα. '
       'Ένα αυτοκίνητο ταξιδεύει προς το βουνό· από το πίσω τζάμι φαίνονται μπροστά ο πατέρας και η μητέρα, πίσω η γιαγιά και το παιδί που τραγουδά. '
       'Νότες βγαίνουν από το στόμα του και ανεβαίνουν γύρω γύρω από το αμάξι ως τον ουρανό. '
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
    w = 220 * S
    x0, x1 = cx - w / 2, cx + w / 2
    yb = cy - 18 * S                      # κάτω άκρη αμαξώματος
    yl = yb - 62 * S                      # ύψος πορτ-μπαγκάζ
    yt = cy - 200 * S                     # οροφή
    def L(pts, **k): p.line(pts, **k)
    hide(p, [(x0, cy), (x0 - 4, yb - 40 * S), (x0 + 8, yl), (x0 + 30 * S, yt), (x1 - 30 * S, yt), (x1 - 8, yl), (x1 + 4, yb - 40 * S), (x1, cy)])
    # αμάξωμα και πορτ-μπαγκάζ
    L([(x0, yb), (x0 - 4 * S, yb - 40 * S), (x0 + 8 * S, yl), (x1 - 8 * S, yl), (x1 + 4 * S, yb - 40 * S), (x1, yb), (x0, yb)], w=2.6)
    # καμπίνα
    L([(x0 + 10 * S, yl), (x0 + 30 * S, yt), (x1 - 30 * S, yt), (x1 - 10 * S, yl)], w=2.4)
    # μεγάλο πίσω τζάμι
    wy0, wy1 = yt + 10 * S, yl - 6 * S
    wl0, wr0, wl1, wr1 = x0 + 38 * S, x1 - 38 * S, x0 + 22 * S, x1 - 22 * S
    L(p.poly([(wl1, wy1), (wl0, wy0), (wr0, wy0), (wr1, wy1), (wl1, wy1)], 4), w=1.6, op=.85)
    # φανάρια (ώχρα), πινακίδα, τροχοί, σκιά
    for a0, a1 in ((x0 + 4 * S, x0 + 38 * S), (x1 - 38 * S, x1 - 4 * S)):
        L(p.poly([(a0, yb - 40 * S), (a1, yb - 40 * S), (a1, yb - 27 * S), (a0, yb - 27 * S), (a0, yb - 40 * S)], 2), w=2, col=OCHRE)
    L(p.poly([(cx - 28 * S, yb - 28 * S), (cx + 28 * S, yb - 28 * S), (cx + 28 * S, yb - 12 * S), (cx - 28 * S, yb - 12 * S), (cx - 28 * S, yb - 28 * S)], 2), w=1.3, op=.7)
    for wx in (x0 + 14 * S, x1 - 32 * S):
        L(p.poly([(wx, yb), (wx + 18 * S, yb), (wx + 18 * S, cy), (wx, cy), (wx, yb)], 2), w=2.2)
    L(p.seg(x0 - 10, cy + 2, x1 + 10, cy + 2, 6), w=1.2, op=.4)

    def bust(hx, hy, r, op=1.0, wgt=2.0):
        """Κεφάλι και ώμοι που κόβονται στην κάτω άκρη του τζαμιού."""
        p.line(p.arc(hx, hy, r, r * 1.08, 0, 2 * math.pi, 26), w=wgt, op=op)
        sh = hy + r * 1.1
        L([(hx - r * 1.9, wy1), (hx - r * 1.7, sh + r * .5), (hx - r * .5, sh)], w=wgt * .85, op=op)
        L([(hx + r * .5, sh), (hx + r * 1.7, sh + r * .5), (hx + r * 1.9, wy1)], w=wgt * .85, op=op)

    # μπροστά (πιο μακριά, μικρότεροι): ο πατέρας στο τιμόνι, αριστερά· η μητέρα δεξιά
    bust(cx - 30 * S, wy0 + 30 * S, 13 * S, op=.6, wgt=1.7)
    bust(cx + 30 * S, wy0 + 31 * S, 12.5 * S, op=.6, wgt=1.7)
    L(p.arc(cx + 30 * S, wy0 + 36 * S, 15 * S, 15 * S, math.pi * 1.0, math.pi * 2.0, 10), w=1.3, op=.5)     # μαλλιά μητέρας
    # πίσω (πιο κοντά): η γιαγιά Τσικό δεξιά, με κότσο
    gxh, gyh = cx + 40 * S, wy1 - 40 * S
    bust(gxh, gyh, 17 * S, wgt=2.2)
    p.ring(gxh + 2, gyh - 21 * S, 6 * S, w=1.8)
    # το παιδί αριστερά, γυρισμένο στο πλάι, με το στόμα ανοιχτό στο τραγούδι
    kx, ky = cx - 42 * S, wy1 - 36 * S
    bust(kx, ky, 15 * S, wgt=2.4)
    p.line(p.arc(kx + 2, ky - 9 * S, 12 * S, 6 * S, math.pi * 1.05, math.pi * 1.95, 8), w=1.6, op=.8)   # μαλλιά
    p.dot(kx - 7 * S, ky - 3 * S, 1.7)
    p.ring(kx - 9 * S, ky + 6 * S, 3.4, w=1.8)                                                       # στόμα
    L([(kx + 14 * S, ky + 20 * S), (kx + 26 * S, ky + 2 * S), (kx + 22 * S, ky - 12 * S)], w=2.0)     # χέρι που κρατά τον ρυθμό

    # --- οι νότες: γύρω γύρω από το αμάξι, ως τον ουρανό ------------------------
    NOTES = ['♪', '♫', '♩', '♬']
    sign = (470, 250, 800, 352)
    car = (x0 - 14, yt - 14, x1 + 14, cy + 6)
    pts, last, path = [], None, []
    for j in range(2000):
        t = j / 1999
        th = math.pi * .9 + t * math.pi * 6.0             # τρεις στροφές, από το παιδί ως τον ουρανό
        R = 175 + 150 * t
        x = cx - 10 + R * math.cos(th)
        y = (ky - 10) - (ky - 70) * t + R * .32 * math.sin(th)
        path.append((x, y, car[0] < x < car[2] and car[1] < y < car[3]))
        if last and math.hypot(x - last[0], y - last[1]) < 46 + 26 * t: continue
        last = (x, y)
        if car[0] < x < car[2] and car[1] < y < car[3]: continue
        if sign[0] - 24 < x < sign[2] + 24 and sign[1] - 34 < y < sign[3] + 14: continue
        if not (24 < x < 1176 and 24 < y < 700): continue
        pts.append((x, y, t))
    # η τροχιά τους, μια λεπτή γραμμή σε ώχρα που κόβεται πίσω από το αμάξι
    seg_ = []
    for k, (x, y, inside) in enumerate(path):
        if inside or k == len(path) - 1:
            if len(seg_) > 4: p.line(seg_[::6], w=1.1, op=.35, col=OCHRE, a=.3)
            seg_ = []
        else:
            seg_.append((x, y))
    # από το στόμα του παιδιού ως την αρχή της τροχιάς
    sx0, sy0 = path[0][0], path[0][1]
    p.line([(kx - 14 * S, ky + 6 * S), (kx - 34 * S, ky + 2 * S), ((kx + sx0) / 2, (ky + sy0) / 2 + 4), (sx0, sy0)], w=1.1, op=.45, col=OCHRE, a=.3)
    p.text(round(kx - 34 * S), round(ky - 2 * S), '♪', size=18, italic=False, anchor='middle', op=.95, col=OCHRE)
    for i, (x, y, t) in enumerate(pts):
        size = round(24 + 14 * t)
        op = round(.95 - .45 * t, 2)
        if i % 3 == 0: p.group('sk-glow')
        p.text(round(x), round(y), NOTES[i % 4], size=size, italic=False, anchor='middle', op=op, col=OCHRE)
        if i % 3 == 0: p.end()
    return ALT


def svg():
    p = Pen(seed=sum(map(ord, 'pou-chorane-osoi-den-antechoume')))
    draw(p)
    return p.svg(ALT)


if __name__ == '__main__':
    out = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'assets', 'sketches', 'pou-chorane-osoi-den-antechoume.svg')
    open(out, 'w', encoding='utf-8').write(svg()); print(out)
