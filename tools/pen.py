"""Πένα του ivan.gr: κοινά εργαλεία για τα σκίτσα στο ύφος του «Δίαυλου» (βλ. ΥΦΟΣ_ΣΚΙΤΣΩΝ.md)."""
import math, random

OCHRE = '#D9A866'
FONT = 'EB Garamond, Garamond, serif'


class Pen:
    def __init__(self, seed=7, W=1200, H=720):
        self.r = random.Random(seed); self.W, self.H = W, H; self.out = []

    # --- βασικά ---------------------------------------------------------------
    def wob(self, pts, a=1.0):
        return [(x + self.r.uniform(-a, a), y + self.r.uniform(-a, a)) for x, y in pts]

    @staticmethod
    def smooth(pts, closed=False):
        if closed: pts = pts + pts[:2]
        d = f'M{pts[0][0]:.1f} {pts[0][1]:.1f}'
        for i in range(1, len(pts) - 1):
            x1, y1 = pts[i]; x2, y2 = pts[i + 1]
            d += f' Q{x1:.1f} {y1:.1f} {(x1 + x2) / 2:.1f} {(y1 + y2) / 2:.1f}'
        if not closed: d += f' L{pts[-1][0]:.1f} {pts[-1][1]:.1f}'
        return d

    def line(self, pts, w=2.6, op=1, col='currentColor', fill='none', closed=False, a=1.0, cls=None):
        p = self.wob(pts, a)
        c = f' class="{cls}"' if cls else ''
        self.out.append(f'<path{c} d="{self.smooth(p, closed)}" stroke="{col}" stroke-width="{w}" fill="{fill}" opacity="{op}"/>')

    @staticmethod
    def seg(x1, y1, x2, y2, n=8):
        return [(x1 + (x2 - x1) * t / n, y1 + (y2 - y1) * t / n) for t in range(n + 1)]

    @staticmethod
    def arc(cx, cy, rx, ry, a0, a1, n=24):
        return [(cx + rx * math.cos(a0 + (a1 - a0) * t / n), cy + ry * math.sin(a0 + (a1 - a0) * t / n)) for t in range(n + 1)]

    def poly(self, pts, n=6):
        """Πολύγωνο από ευθείες με ενδιάμεσα σημεία, για να τρέμει φυσικά."""
        q = [pts[0]]
        for (x1, y1), (x2, y2) in zip(pts, pts[1:]):
            q += self.seg(x1, y1, x2, y2, n)[1:]
        return q

    def ring(self, cx, cy, r, ry=None, w=2.2, op=1, col='currentColor', fill='none', n=28, cls=None):
        self.line(self.arc(cx, cy, r, ry or r, 0, 2 * math.pi, n), w=w, op=op, col=col, fill=fill, cls=cls)

    def dot(self, x, y, r=3.4, col='currentColor', cls=None, op=1):
        c = f' class="{cls}"' if cls else ''
        self.out.append(f'<circle{c} cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{col}" opacity="{op}"/>')

    def text(self, x, y, s, size=26, italic=True, anchor='start', op=1, spacing=0, cls=None, col='currentColor'):
        c = f' class="{cls}"' if cls else ''
        st = ' font-style="italic"' if italic else ''
        ls = f' letter-spacing="{spacing}"' if spacing else ''
        self.out.append(f'<text{c} x="{x}" y="{y}" text-anchor="{anchor}" font-family="{FONT}"{st} font-size="{size}"{ls} fill="{col}" opacity="{op}">{s}</text>')

    def group(self, cls, origin=None):
        """Ομάδα που κινείται. Το σημείο περιστροφής δίνεται με εμφωλευμένες μετατοπίσεις SVG
        (όχι με transform-origin σε px, που το Safari δεν το τηρεί και τα κομμάτια «πετούν»)."""
        st = getattr(self, '_st', None)
        if st is None: st = self._st = []
        if origin:
            ox, oy = origin
            self.out.append(f'<g transform="translate({ox:.0f} {oy:.0f})"><g class="{cls}"><g transform="translate({-ox:.0f} {-oy:.0f})">')
            st.append(3)
        else:
            self.out.append(f'<g class="{cls}">'); st.append(1)

    def end(self):
        self.out.append('</g>' * self._st.pop())

    # --- μοτίβα ---------------------------------------------------------------
    def floor(self, y=600, x0=40, x1=1160):
        self.line(self.seg(x0, y, x1, y, 20), w=2.2, op=.8)

    def window(self, x, y0, y1, w=140, op=.35):
        """Τοξωτό παράθυρο, αχνό, σαν αρχιτέκτονας."""
        self.line(self.seg(x, y1, x, y0) + self.arc(x + w / 2, y0, w / 2, w / 2, math.pi, 2 * math.pi)[1:] + self.seg(x + w, y0, x + w, y1)[1:], w=1.6, op=op)
        self.line(self.seg(x + w / 2, y0 - w / 2, x + w / 2, y1), w=1.2, op=op * .7)
        for k in range(1, 4):
            yy = y0 + (y1 - y0) * k / 4
            self.line(self.seg(x, yy, x + w, yy, 4), w=1.2, op=op * .7)

    def head(self, hx, hy, r=40, glasses=True, look=0, eyes_closed=False):
        """Κεφάλι με λίγες γραμμές· look: -1 αριστερά, 1 δεξιά."""
        self.line(self.arc(hx, hy, r, r * 1.05, 0, 2 * math.pi, 30), w=2.8)
        self.line(self.arc(hx - 2, hy - r * .75, r * .75, r * .35, math.pi * 1.05, math.pi * 1.95, 10), w=2, op=.8)
        ex = hx + look * r * .3
        if glasses:
            self.line(self.arc(ex + 13, hy - 4, 9, 8, 0, 2 * math.pi, 12), w=1.8)
            self.line(self.arc(ex - 13, hy - 4, 9, 8, 0, 2 * math.pi, 12), w=1.8)
            self.line(self.seg(ex - 4, hy - 5, ex + 4, hy - 5, 2), w=1.6)
        if eyes_closed:
            for k in (-13, 13):
                self.line(self.arc(ex + k, hy - 2, 5, 3, 0, math.pi, 6), w=1.6)

    def steam(self, x, y, k=2, cls='sk-steam'):
        for i in range(k):
            self.group(f'{cls} sk-st{i}')
            dx = -8 + i * 14
            self.line([(x + dx, y), (x + dx + 6, y - 14), (x + dx, y - 28), (x + dx + 6, y - 42)], w=1.4, op=.6)
            self.end()

    def svg(self, label):
        return (f'<svg viewBox="0 0 {self.W} {self.H}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{label}">'
                f'<g stroke-linecap="round" stroke-linejoin="round">' + ''.join(self.out) + '</g></svg>')
