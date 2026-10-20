"""Γελοιογραφία «Δίαυλος»: σχέδιο με πένα σε SVG (μπλε μελάνι, ώχρα για τα φώτα και τα φτερά)."""
import math, random, os
random.seed(7)
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
W, H = 1200, 720
out = []

def wob(pts, a=1.2):
    return [(x + random.uniform(-a, a), y + random.uniform(-a, a)) for x, y in pts]

def smooth(pts, closed=False):
    if closed: pts = pts + pts[:2]
    d = f'M{pts[0][0]:.1f} {pts[0][1]:.1f}'
    for i in range(1, len(pts) - 1):
        x1, y1 = pts[i]; x2, y2 = pts[i + 1]
        d += f' Q{x1:.1f} {y1:.1f} {(x1 + x2) / 2:.1f} {(y1 + y2) / 2:.1f}'
    if not closed: d += f' L{pts[-1][0]:.1f} {pts[-1][1]:.1f}'
    return d

def line(pts, w=2.6, op=1, col='currentColor', fill='none', closed=False, a=1.0):
    p = wob(pts, a)
    out.append(f'<path d="{smooth(p, closed)}" stroke="{col}" stroke-width="{w}" fill="{fill}" opacity="{op}"/>')

def seg(x1, y1, x2, y2, n=8):
    return [(x1 + (x2 - x1) * t / n, y1 + (y2 - y1) * t / n) for t in range(n + 1)]

def arc(cx, cy, rx, ry, a0, a1, n=24):
    return [(cx + rx * math.cos(a0 + (a1 - a0) * t / n), cy + ry * math.sin(a0 + (a1 - a0) * t / n)) for t in range(n + 1)]

OCHRE = '#D9A866'

# --- ο σταθμός: δύο ψηλά τοξωτά παράθυρα, αχνά -------------------------------
for x in (120, 470):
    line(seg(x, 520, x, 170) + arc(x + 70, 170, 70, 70, math.pi, 2 * math.pi)[1:] + seg(x + 140, 170, x + 140, 520)[1:], w=1.6, op=.35)
    line(seg(x + 70, 100, x + 70, 520), w=1.2, op=.25)
    for y in (260, 350, 440):
        line(seg(x, y, x + 140, y, 4), w=1.2, op=.25)
# πάτωμα
line(seg(40, 600, 1160, 600, 20), w=2.2, op=.8)

# --- ο «Δαίδαλος»: ντουλάπι υπολογιστή με δύο μικρά φτερά ------------------
cx0, cy0, cw, ch = 820, 250, 210, 350
line(seg(cx0, cy0 + ch, cx0, cy0 + 8) + arc(cx0 + 8, cy0 + 8, 8, 8, math.pi, 1.5 * math.pi, 6)[1:] + seg(cx0 + 8, cy0, cx0 + cw - 8, cy0)[1:]
     + arc(cx0 + cw - 8, cy0 + 8, 8, 8, 1.5 * math.pi, 2 * math.pi, 6)[1:] + seg(cx0 + cw, cy0 + 8, cx0 + cw, cy0 + ch)[1:], w=3)
line(seg(cx0 + cw / 2, cy0 + 14, cx0 + cw / 2, cy0 + ch - 6), w=1.6, op=.6)
for col in range(2):
    for r in range(9):
        bx = cx0 + 22 + col * (cw / 2) ; by = cy0 + 34 + r * 33
        line(seg(bx, by, bx + cw / 2 - 44, by, 4), w=1.3, op=.45)
        c = OCHRE if (r * 3 + col * 5) % 4 == 0 else 'currentColor'
        out.append(f'<circle cx="{bx + cw / 2 - 38:.1f}" cy="{by - 7:.1f}" r="3.6" fill="{c}"/>')
# πινακιδούλα
out.append(f'<text x="{cx0 + cw / 2}" y="{cy0 - 10}" text-anchor="middle" font-family="EB Garamond, Garamond, serif" font-size="17" letter-spacing="3" fill="currentColor" opacity=".8">ΔΑΙΔΑΛΟΣ</text>')

def wing(x, y, side):
    # μικρό φτερό: πέντε φτερά σε βεντάλια, λίγο ανασηκωμένα
    for k in range(5):
        ang = math.radians(-100 + side * (18 + k * 14))
        L = 34 + k * 9
        ex, ey = x + side * math.cos(math.radians(8 + k * 12)) * L, y - math.sin(math.radians(8 + k * 12)) * L
        mx, my = (x + ex) / 2 + side * 4, (y + ey) / 2 - 8
        out.append(f'<path d="M{x:.1f} {y:.1f} Q{mx:.1f} {my:.1f} {ex:.1f} {ey:.1f}" stroke="{OCHRE}" stroke-width="7" stroke-linecap="round" fill="none"/>')
        out.append(f'<path d="M{x:.1f} {y:.1f} Q{mx:.1f} {my:.1f} {ex:.1f} {ey:.1f}" stroke="currentColor" stroke-width="1.4" fill="none" opacity=".8"/>')
# κινούμενα μέρη: ομάδες με όνομα, για την απαλή λούπα του ιστότοπου (το CSS ορίζει την κίνηση)
for k, (wx, sd) in enumerate(((cx0 + 30, -1), (cx0 + cw - 30, 1))):
    out.append(f'<g class="sk-wing sk-w{k}" style="transform-origin:{wx:.0f}px {cy0 - 6:.0f}px">')
    wing(wx, cy0 - 6, sd)
    out.append('</g>')
# κινητικές γραμμούλες: τα φτερά φτερουγίζουν
out.append('<g class="sk-flap">')
for s, x in ((-1, cx0 - 40), (1, cx0 + cw + 40)):
    for k in range(3):
        line(arc(x, cy0 - 70, 14 + k * 9, 14 + k * 9, math.radians(-60 if s > 0 else 120), math.radians(-20 if s > 0 else 160), 6), w=1.4, op=.55)
out.append('</g>')

# --- ο άνθρωπος στο σκαμνί ---------------------------------------------------
sx, sy = 250, 600
line(seg(sx - 40, sy, sx - 30, sy - 120) + seg(sx - 30, sy - 120, sx + 40, sy - 120)[1:] + seg(sx + 40, sy - 120, sx + 50, sy)[1:], w=2.4)  # σκαμνί
line(seg(sx - 34, sy - 60, sx + 44, sy - 60), w=1.6, op=.7)
hx, hy = 262, 330
line(arc(hx, hy, 40, 42, 0, 2 * math.pi, 30), w=2.8, closed=False)        # κεφάλι
line(arc(hx - 2, hy - 30, 30, 14, math.pi * 1.05, math.pi * 1.95, 10), w=2, op=.8)  # μαλλιά
line(arc(hx + 16, hy - 4, 9, 8, 0, 2 * math.pi, 12), w=1.8)               # γυαλιά
line(arc(hx - 10, hy - 4, 9, 8, 0, 2 * math.pi, 12), w=1.8)
line(seg(hx - 1, hy - 5, hx + 7, hy - 5, 2), w=1.6)
line(arc(hx - 40, hy + 2, 6, 10, math.pi * .5, math.pi * 1.5, 8), w=2)    # αυτί αριστερά
line(arc(hx + 30, hy + 16, 5, 4, 0, 2 * math.pi, 10), w=1.8)   # στόμα
# σώμα καθιστό
line([(hx - 6, hy + 42), (hx - 18, 420), (hx - 22, 470), (sx - 10, 480)], w=2.8)          # πλάτη
line([(hx + 14, hy + 40), (hx + 30, 420), (hx + 34, 470), (sx + 30, 480)], w=2.8)         # στήθος
line([(sx - 10, 480), (sx + 70, 484), (sx + 92, 520), (sx + 96, 598)], w=2.6)             # πόδι
line([(sx + 30, 480), (sx + 96, 470), (sx + 120, 520), (sx + 126, 598)], w=2.6)
line([(sx + 92, 598), (sx + 136, 598)], w=3)
line([(sx + 120, 598), (sx + 160, 598)], w=3)
# χέρι που κρατά τον αυλό στο στόμα
line([(hx + 26, 410), (hx + 64, 400), (hx + 62, hy + 18)], w=2.6)

# --- ο δίαυλος: διπλός σωλήνας από το στόμα στο ντουλάπι και πίσω στο αυτί ----
def tube(pts, gap=7):
    for off in (-gap / 2, gap / 2):
        q = []
        for i, (x, y) in enumerate(pts):
            x2, y2 = pts[min(i + 1, len(pts) - 1)]; x1, y1 = pts[max(i - 1, 0)]
            dx, dy = x2 - x1, y2 - y1; L = math.hypot(dx, dy) or 1
            q.append((x - dy / L * off, y + dx / L * off))
        line(q, w=2.2, a=.5)
go = [(hx + 36, hy + 18), (hx + 90, hy + 34), (hx + 140, 400), (hx + 175, 500), (hx + 230, 560), (480, 572), (640, 574), (760, 572), (cx0, 560)]
back = [(cx0, 330), (780, 300), (720, 200), (600, 150), (440, 130), (300, 140), (190, 170), (150, 230), (160, 290), (hx - 70, hy - 2)]
tube(go)
tube(back)
# χωνί στο αυτί
line([(hx - 44, hy - 6), (hx - 66, hy - 18), (hx - 70, hy + 16), (hx - 44, hy + 8)], w=2.2)
# νότες/λέξεις που ταξιδεύουν
out.append(f'<text x="{hx + 70}" y="{hy - 26}" font-family="EB Garamond, Garamond, serif" font-style="italic" font-size="30" fill="currentColor">Καλημέρα!</text>')
out.append(f'<text x="{hx - 230}" y="{hy + 50}" font-family="EB Garamond, Garamond, serif" font-style="italic" font-size="24" fill="currentColor" opacity=".85">…καλημέρα</text>')
for i, (x, y) in enumerate(((560, 573), (690, 574), (600, 152), (420, 133))):
    out.append(f'<circle class="sk-sig sk-s{i}" cx="{x}" cy="{y}" r="3" fill="{OCHRE}"/>')

# --- το φλιτζάνι του καφέ ------------------------------------------------------
fx, fy = 150, 600
line([(fx - 22, fy - 34), (fx - 18, fy), (fx + 18, fy), (fx + 22, fy - 34), (fx - 22, fy - 34)], w=2.2)
line(arc(fx + 28, fy - 18, 9, 10, -math.pi / 2, math.pi / 2, 8), w=2)
for i, k in enumerate((-8, 6)):
    out.append(f'<g class="sk-steam sk-st{i}">')
    line([(fx + k, fy - 44), (fx + k + 6, fy - 58), (fx + k, fy - 72), (fx + k + 6, fy - 86)], w=1.4, op=.6)
    out.append('</g>')

svg = (f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" '
       f'aria-label="Ένας άνθρωπος σε σκαμνί λέει «Καλημέρα!» σε έναν διπλό σωλήνα που φτάνει ως ένα ψηλό ντουλάπι υπολογιστή με δύο μικρά φτερά· ο σωλήνας γυρίζει πίσω στο αυτί του, όπου ακούγεται «…καλημέρα».">'
       f'<g stroke-linecap="round" stroke-linejoin="round">' + ''.join(out) + '</g></svg>')
open(os.path.join(ROOT, 'assets', 'sketches', '2026-10-20-diavlos.svg'), 'w', encoding='utf-8').write(svg)
print(len(svg))
