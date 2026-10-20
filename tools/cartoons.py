"""Γελοιογραφίες για τα κείμενα: πένα σε SVG, μπλε μελάνι (currentColor), ώχρα για τα φώτα.
Κάθε σχέδιο είναι συνάρτηση που επιστρέφει SVG· γράφονται στο assets/sketches/<slug>.svg."""
import math, random, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OCHRE = '#D9A866'
FONT = 'EB Garamond, Garamond, serif'


class Pen:
    def __init__(self, seed, w=1200, h=720):
        random.seed(seed); self.out = []; self.w = w; self.h = h

    def _wob(self, pts, a):
        return [(x + random.uniform(-a, a), y + random.uniform(-a, a)) for x, y in pts]

    @staticmethod
    def _smooth(pts):
        d = f'M{pts[0][0]:.1f} {pts[0][1]:.1f}'
        for i in range(1, len(pts) - 1):
            x1, y1 = pts[i]; x2, y2 = pts[i + 1]
            d += f' Q{x1:.1f} {y1:.1f} {(x1 + x2) / 2:.1f} {(y1 + y2) / 2:.1f}'
        return d + f' L{pts[-1][0]:.1f} {pts[-1][1]:.1f}'

    def line(self, pts, w=2.6, op=1, col='currentColor', fill='none', a=1.0):
        self.out.append(f'<path d="{self._smooth(self._wob(pts, a))}" stroke="{col}" stroke-width="{w}" fill="{fill}" opacity="{op}"/>')

    @staticmethod
    def seg(x1, y1, x2, y2, n=8):
        return [(x1 + (x2 - x1) * t / n, y1 + (y2 - y1) * t / n) for t in range(n + 1)]

    @staticmethod
    def arc(cx, cy, rx, ry, a0, a1, n=24):
        return [(cx + rx * math.cos(a0 + (a1 - a0) * t / n), cy + ry * math.sin(a0 + (a1 - a0) * t / n)) for t in range(n + 1)]

    def rect(self, x, y, rw, rh, **k):
        self.line(self.seg(x, y, x + rw, y) + self.seg(x + rw, y, x + rw, y + rh)[1:] + self.seg(x + rw, y + rh, x, y + rh)[1:] + self.seg(x, y + rh, x, y)[1:], **k)

    def circle(self, cx, cy, r, **k):
        self.line(self.arc(cx, cy, r, r, 0, 2 * math.pi, 30), **k)

    def dot(self, x, y, r=3.5, col='currentColor'):
        self.out.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{col}"/>')

    def text(self, x, y, s, size=28, italic=True, anchor='start', op=1, col='currentColor', weight=400, spacing=0):
        st = ' font-style="italic"' if italic else ''
        self.out.append(f'<text x="{x}" y="{y}" font-family="{FONT}" font-size="{size}"{st} font-weight="{weight}" letter-spacing="{spacing}" text-anchor="{anchor}" fill="{col}" opacity="{op}">{s}</text>')

    def floor(self, y=600):
        self.line(self.seg(40, y, self.w - 40, y, 20), w=2.2, op=.8)

    # ο άνθρωπος του ιστότοπου: στρογγυλό κεφάλι, γυαλιά, λίγα μαλλιά
    def head(self, hx, hy, r=40, facing=1):
        self.circle(hx, hy, r, w=2.8)
        self.line(self.arc(hx - 2 * facing, hy - r * .74, r * .75, r * .35, math.pi * 1.05, math.pi * 1.95, 10), w=2, op=.8)
        self.circle(hx + 16 * facing, hy - 4, 9, w=1.8); self.circle(hx - 10 * facing, hy - 4, 9, w=1.8)
        self.line(self.seg(hx + 1 * facing, hy - 5, hx + 7 * facing, hy - 5, 2), w=1.6)
        self.line(self.arc(hx + 6 * facing, hy + 17, 9, 4, .15 * math.pi, .85 * math.pi, 8), w=1.8)  # χαμόγελο

    def svg(self, label, vb=None):
        vb = vb or f'0 0 {self.w} {self.h}'
        return (f'<svg viewBox="{vb}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{label}">'
                f'<g stroke-linecap="round" stroke-linejoin="round">' + ''.join(self.out) + '</g></svg>')


# 1. Η κριτική δεν κατοικεί στο παρόν --------------------------------------------
def kritiki():
    p = Pen(31)
    p.floor()
    # τοίχος και πόρτα, φρεσκοδιορθωμένη
    p.rect(470, 170, 250, 430, w=3)
    p.rect(490, 190, 210, 410, w=2.2, op=.9)
    p.circle(675, 400, 9, w=2.4)
    for y in (230, 540):  # καινούριοι μεντεσέδες, γυαλιστεροί
        p.rect(486, y, 14, 34, w=2, col=OCHRE); p.line(p.seg(493, y + 4, 493, y + 30, 3), w=1.2, col=OCHRE)
    for k in range(3):  # λάμψη του καινούριου
        a = math.radians(200 + k * 40)
        p.line(p.seg(493 + math.cos(a) * 22, 247 + math.sin(a) * 22, 493 + math.cos(a) * 36, 247 + math.sin(a) * 36, 2), w=1.6, col=OCHRE)
    # το χαρτάκι της κριτικής, ακόμη καρφωμένο
    p.line([(560, 280), (676, 286), (672, 372), (556, 366), (560, 280)], w=2, fill='#FBF8F2')
    p.dot(616, 286, 4, OCHRE)
    p.text(616, 316, 'Η πόρτα δεν', 17, anchor='middle'); p.text(616, 338, 'κλείνει καλά', 17, anchor='middle')
    p.text(616, 360, '★ ★', 16, italic=False, anchor='middle', op=.8)
    # ο μάστορας φεύγει με την εργαλειοθήκη, ικανοποιημένος
    p.head(900, 330, facing=1)
    p.line([(894, 372), (880, 470), (884, 520)], w=2.8); p.line([(916, 370), (934, 470), (930, 520)], w=2.8)
    p.line([(884, 520), (870, 598)], w=2.6); p.line([(930, 520), (960, 598)], w=2.6)
    p.line([(886, 410), (840, 470), (836, 500)], w=2.6)
    p.rect(800, 500, 70, 40, w=2.4); p.line(p.arc(835, 500, 18, 14, math.pi, 2 * math.pi, 8), w=2)
    p.line([(926, 410), (960, 450), (990, 430)], w=2.6)
    # ένα μικρό ρομπότ-αναγνώστης κοιτάζει το χαρτάκι και όχι την πόρτα
    p.rect(250, 430, 90, 90, w=2.6); p.dot(278, 465, 5); p.dot(312, 465, 5)
    p.line(p.seg(270, 495, 320, 495, 4), w=2)
    p.line(p.seg(295, 430, 295, 400, 3), w=2); p.dot(295, 396, 6, OCHRE)
    p.line([(270, 520), (264, 598)], w=2.4); p.line([(320, 520), (326, 598)], w=2.4)
    p.text(360, 420, '«…δεν κλείνει καλά»', 24, op=.9)
    p.line([(345, 450), (420, 360), (520, 330)], w=1.4, op=.5)
    return p.svg('Μια πόρτα μόλις επισκευασμένη, με καινούριους μεντεσέδες· πάνω της είναι ακόμη καρφωμένο ένα χαρτάκι που γράφει «Η πόρτα δεν κλείνει καλά». Ένα μικρό ρομπότ διαβάζει το χαρτάκι, ενώ ο μάστορας φεύγει.'), \
        {'el': 'Η πόρτα διορθώθηκε. Η κριτική έμεινε.', 'en': 'The door was fixed. The review stayed.',
         'fr': 'La porte a été réparée. L’avis est resté.', 'de': 'Die Tür wurde repariert. Die Bewertung blieb.'}


# 2. Το ξέρουν από το 2021 ---------------------------------------------------------
def to_xeroun():
    p = Pen(2021)
    p.floor()
    # ένα πουλί στο κλαδί, εκεί που δείχνει η μητέρα
    p.line([(900, 160), (1010, 170), (1100, 150)], w=2.4)
    p.line(p.arc(980, 150, 22, 14, math.pi, 2.2 * math.pi, 12), w=2.4); p.dot(992, 146, 3)
    p.line([(1000, 150), (1014, 154), (1000, 158)], w=2, col=OCHRE)
    # μητέρα με το μωρό, δείχνει
    p.head(420, 300, r=38, facing=1)
    p.line([(414, 340), (400, 470), (396, 598)], w=2.8); p.line([(436, 338), (470, 470), (480, 598)], w=2.8)
    p.line([(438, 352), (560, 300), (700, 225), (760, 205)], w=2.6)  # χέρι που δείχνει
    p.line([(410, 360), (440, 440), (500, 440)], w=2.4)  # χέρι που κρατά το μωρό
    p.line([(760, 205), (790, 192)], w=2, op=.6)
    # μωρό στην αγκαλιά, κεφάλι γυρισμένο προς τα εκεί
    p.circle(470, 410, 22, w=2.4); p.dot(480, 405, 2.4); p.line(p.arc(470, 410, 26, 26, -1.2, -0.4, 6), w=1.4, op=.6)
    p.line([(452, 430), (500, 452), (470, 470)], w=2.2)
    # κουτάβι στο πάτωμα, κεφάλι γυρισμένο προς το πουλί
    p.line([(600, 560), (680, 560), (690, 598)], w=2.4); p.line([(610, 560), (600, 598)], w=2.4)
    p.circle(700, 530, 22, w=2.4); p.dot(708, 524, 2.6)
    p.line([(690, 512), (684, 494), (700, 508)], w=2.2)
    p.line([(600, 560), (580, 540)], w=2.2)
    # ουρά που κουνιέται
    for k in range(2): p.line(p.arc(578, 538, 10 + k * 7, 10 + k * 7, math.pi * 1.1, math.pi * 1.5, 5), w=1.2, op=.5)
    # στο τραπέζι, ο υπολογιστής: σύννεφο λέξεων, κοιτάζει ευθεία μπροστά
    p.line(p.seg(80, 470, 330, 470, 6), w=2.6); p.line([(100, 470), (96, 598)], w=2.4); p.line([(310, 470), (314, 598)], w=2.4)
    p.rect(140, 360, 140, 96, w=2.6); p.line([(130, 470), (290, 470)], w=2.2)
    words = ['λέξη', 'γλώσσα', 'κόσμος', 'όνομα', 'πουλί', 'βλέμμα', 'εκεί']
    for i, wd in enumerate(words):
        p.text(120 + (i % 3) * 66, 250 + (i // 3) * 34, wd, 18, op=.75)
    p.line(p.arc(210, 290, 140, 80, 0, 2 * math.pi, 30), w=1.4, op=.35)
    p.line([(196, 360), (200, 372)], w=1.2, op=.4)
    return p.svg('Μια μητέρα δείχνει ένα πουλί σε ένα κλαδί· το μωρό στην αγκαλιά της και το κουτάβι στο πάτωμα γυρίζουν το κεφάλι εκεί. Στο τραπέζι, ένας υπολογιστής γεμάτος λέξεις κοιτάζει ευθεία μπροστά.'), \
        {'el': 'Δεν του λείπει η λέξη. Του λείπει το γύρισμα του κεφαλιού.', 'en': 'It does not lack the word. It lacks the turning of the head.',
         'fr': 'Ce n’est pas le mot qui lui manque. C’est le geste de tourner la tête.', 'de': 'Ihm fehlt nicht das Wort. Ihm fehlt die Wendung des Kopfes.'}


# 3. Η προειδοποίηση στα τσιγάρα ----------------------------------------------------
def proeidopoiisi():
    p = Pen(1209)
    p.floor()
    # αναγνώστης σε πολυθρόνα με εφημερίδα
    p.line(p.seg(300, 598, 300, 450, 6) + p.seg(300, 450, 520, 450, 8)[1:] + p.seg(520, 450, 520, 598, 6)[1:], w=2.6)
    p.line(p.seg(300, 450, 300, 300, 6) + p.seg(300, 300, 340, 300, 2)[1:] + p.seg(340, 300, 340, 450, 6)[1:], w=2.4)
    p.line(p.seg(300, 520, 520, 520, 8), w=1.6, op=.6)
    p.head(420, 300, facing=1)
    p.line([(414, 340), (410, 440)], w=2.8); p.line([(432, 340), (450, 440)], w=2.8)
    # η εφημερίδα, ανοιχτή
    p.line([(470, 250), (800, 230), (812, 470), (482, 488), (470, 250)], w=2.6, fill='#FBF8F2')
    p.line(p.seg(641, 240, 647, 479, 6), w=1.4, op=.6)
    p.text(556, 300, 'Η ΤΕΧΝΗΤΗ', 22, italic=False, anchor='middle', weight=600, spacing=1)
    p.text(556, 330, 'ΝΟΗΜΟΣΥΝΗ', 22, italic=False, anchor='middle', weight=600, spacing=1)
    p.text(556, 360, 'ΕΠΙΤΕΘΗΚΕ', 22, italic=False, anchor='middle', weight=600, spacing=1)
    for y in range(392, 470, 16):
        p.line(p.seg(500, y, 625, y - 1, 4), w=1.2, op=.4); p.line(p.seg(665, y - 2, 790, y - 3, 4), w=1.2, op=.4)
    p.text(726, 300, 'ΤΟ ΚΑΠΝΙΣΜΑ', 18, italic=False, anchor='middle', weight=600)
    p.text(726, 326, 'ΣΚΟΤΩΝΕΙ', 18, italic=False, anchor='middle', weight=600)
    # το μολύβι του αναγνώστη προσθέτει μια λέξη στο περιθώριο
    p.line(p.seg(840, 360, 812, 300, 3), w=3)
    p.line(p.seg(812, 300, 806, 288, 2), w=3, col=OCHRE)
    p.line([(455, 440), (500, 420), (840, 380)], w=2.4, op=.0)
    p.text(860, 300, 'ποιος;', 46, col='currentColor')
    p.line([(850, 312), (812, 330)], w=1.6, op=.6)
    p.line(p.arc(904, 288, 70, 34, 0, 2 * math.pi, 28), w=1.6, col=OCHRE, op=.9)
    return p.svg('Ένας αναγνώστης σε πολυθρόνα διαβάζει εφημερίδα με τίτλους «Η τεχνητή νοημοσύνη επιτέθηκε» και «Το κάπνισμα σκοτώνει»· στο περιθώριο έχει γράψει με μολύβι και κυκλώσει τη λέξη «ποιος;».'), \
        {'el': 'Λείπει από την πρόταση μια μικρή ερώτηση: ποιος.', 'en': 'A small question is missing from the sentence: who.',
         'fr': 'Il manque à la phrase une petite question : qui.', 'de': 'Dem Satz fehlt eine kleine Frage: wer.'}


# 4. Η τεχνητή νοημοσύνη δεν ήρθε από έξω --------------------------------------------
def den_irthe():
    p = Pen(912)
    # το παράθυρο της κουζίνας
    p.rect(330, 120, 540, 420, w=3)
    p.line(p.seg(600, 120, 600, 540, 8), w=2.2, op=.8)
    p.line(p.seg(300, 540, 900, 540, 10), w=3)  # περβάζι
    # ο γάτος έξω, με κλειστά μάτια
    p.line(p.arc(730, 460, 90, 70, math.pi, 2 * math.pi, 20) + p.seg(820, 460, 640, 460, 6)[1:], w=2.6)
    p.circle(700, 360, 46, w=2.6)
    p.line([(668, 330), (662, 296), (690, 318)], w=2.4); p.line([(712, 318), (738, 296), (734, 332)], w=2.4)
    p.line(p.arc(684, 362, 9, 5, .1 * math.pi, .9 * math.pi, 6), w=2); p.line(p.arc(718, 362, 9, 5, .1 * math.pi, .9 * math.pi, 6), w=2)
    p.dot(701, 376, 3, OCHRE)
    for s in (-1, 1):
        for k in (0, 10): p.line(p.seg(701 + s * 16, 380 + k, 701 + s * 52, 374 + k * 1.6, 3), w=1.2, op=.7)
    p.line([(820, 450), (860, 420), (850, 380)], w=2.4)  # ουρά
    # το χέρι από μέσα, ακουμπά το γυαλί
    p.line([(470, 600), (520, 470), (560, 410)], w=2.6, op=.9)   # βραχίονας από κάτω
    p.line([(548, 420), (556, 380), (578, 360), (596, 372), (594, 420), (570, 440), (548, 420)], w=2.6)  # παλάμη
    for k, (fx, top) in enumerate(((560, 300), (572, 292), (584, 296), (594, 310))):
        p.line(p.seg(fx, 372, fx + 2, top, 4), w=2.4)   # δάχτυλα πάνω στο τζάμι
    p.line([(548, 420), (530, 392), (528, 370)], w=2.4)  # αντίχειρας
    # γραμμούλες ζεστασιάς στο τζάμι
    for k in range(3): p.line(p.arc(640, 350, 16 + k * 10, 16 + k * 10, -0.4 * math.pi, 0.4 * math.pi, 6), w=1.4, col=OCHRE, op=.8)
    # στο περβάζι, μέσα: μια ραπτομηχανή και ένα κλαδάκι βαμβάκι
    # ραπτομηχανή: βάση, βραχίονας σε σχήμα C, βελόνα, ρόδα
    p.line(p.seg(350, 540, 470, 540, 4), w=2.4); p.line(p.seg(352, 540, 352, 526, 2) + p.seg(352, 526, 468, 526, 4)[1:] + p.seg(468, 526, 468, 540, 2)[1:], w=2.2)
    p.line(p.seg(372, 526, 372, 470, 4) + p.seg(372, 470, 450, 470, 4)[1:] + p.seg(450, 470, 450, 496, 2)[1:], w=2.4)
    p.line(p.seg(446, 496, 446, 512, 2), w=1.8); p.circle(386, 486, 11, w=2)
    # κλαδάκι βαμβάκι
    p.line(p.seg(500, 540, 500, 492, 3), w=1.8)
    for dx, dy in ((0, 0), (-12, 8), (12, 8)): p.circle(500 + dx, 484 + dy, 9, w=1.6, col=OCHRE)
    return p.svg('Ένας γάτος έξω από το παράθυρο της κουζίνας κλείνει τα μάτια, ενώ από μέσα ένα χέρι ακουμπά το τζάμι στο ύψος του. Στο περβάζι, μέσα, μια ραπτομηχανή και ένα κλαδάκι βαμβάκι.', vb='260 80 680 520'), \
        {'el': 'Ένα χέρι πάνω στο γυαλί, και δύο μάτια που κλείνουν.', 'en': 'A hand on the glass, and two eyes closing.',
         'fr': 'Une main sur la vitre, et deux yeux qui se ferment.', 'de': 'Eine Hand auf dem Glas, und zwei Augen, die sich schließen.'}


DRAWINGS = {
    '2026/10/blog-post.html': ('kritiki', kritiki),
    '2026/09/2021.html': ('to-xeroun-2021', to_xeroun),
    '2026/09/blog-post_442.html': ('proeidopoiisi', proeidopoiisi),
    '2026/09/blog-post_12.html': ('den-irthe-apo-exo', den_irthe),
}

if __name__ == '__main__':
    import json
    d = os.path.join(ROOT, 'assets', 'sketches'); os.makedirs(d, exist_ok=True)
    caps = {}
    for path, (slug, fn) in DRAWINGS.items():
        svg, cap = fn()
        open(os.path.join(d, slug + '.svg'), 'w', encoding='utf-8').write(svg)
        caps[path] = {'slug': slug, 'caption': cap}
    json.dump(caps, open(os.path.join(ROOT, 'content', 'sketches.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(len(caps), 'σχέδια')
