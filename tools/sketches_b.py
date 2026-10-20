"""Σκίτσα δημοσιεύσεων, δεύτερη σειρά (21.10.2026): ένα νόημα ανά σκίτσο, μία απαλή λούπα, ώχρα μόνο για ό,τι λάμπει.
Γράφει assets/sketches/<slug>.svg και ενημερώνει το content/sketches.json (παλιές εγγραφές μένουν ως έχουν σε _prev)."""
import math, json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pen import Pen, OCHRE

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PI = math.pi
S = {}


def scene(path, slug, cap):
    def deco(fn):
        S[path] = (slug, cap, fn)
        return fn
    return deco


# 1. Η κριτική δεν κατοικεί στο παρόν --------------------------------------
@scene('2026/10/blog-post.html', 'kritiki-b', dict(
    el='Η πόρτα διορθώθηκε. Η κριτική έμεινε.', en='The door was fixed. The review stayed.',
    fr='La porte a été réparée. L’avis est resté.', de='Die Tür wurde repariert. Die Bewertung blieb.'))
def kritiki(p):
    p.floor()
    # τοίχος διαδρόμου ξενοδοχείου, αχνός
    for x in (120, 1080):
        p.line(p.seg(x, 120, x, 600, 10), w=1.4, op=.3)
    p.line(p.seg(120, 120, 1080, 120, 16), w=1.4, op=.3)
    # η πόρτα, κλειστή και ίσια τώρα
    dx, dy, dw, dh = 560, 170, 210, 430
    p.line(p.poly([(dx, 600), (dx, dy), (dx + dw, dy), (dx + dw, 600)]), w=3)
    p.line(p.poly([(dx + 18, 590), (dx + 18, dy + 18), (dx + dw - 18, dy + 18), (dx + dw - 18, 590)]), w=1.6, op=.6)
    p.ring(dx + dw - 40, 400, 9, w=2.2)                       # πόμολο
    p.text(dx + dw / 2, dy - 16, '214', size=22, italic=False, anchor='middle', spacing=3, op=.8)
    # καινούριος μεντεσές που λάμπει
    for y in (230, 520):
        p.line(p.poly([(dx - 6, y), (dx + 8, y), (dx + 8, y + 34), (dx - 6, y + 34), (dx - 6, y)], 2), w=2, col=OCHRE)
    p.group('sk-glow'); p.dot(dx + 1, 247, 3.2, OCHRE); p.dot(dx + 1, 537, 3.2, OCHRE); p.end()
    # κατσαβίδι ακουμπισμένο κάτω
    p.line(p.seg(dx + dw + 40, 596, dx + dw + 120, 586, 4), w=2.2); p.line(p.seg(dx + dw + 120, 586, dx + dw + 160, 581, 3), w=5, op=.5)
    # η κριτική: χαρτάκι καρφιτσωμένο στον τοίχο, που ανεμίζει λίγο
    kx, ky = 250, 230
    p.group('sk-flutter', (kx + 100, ky))
    p.line(p.poly([(kx, ky), (kx + 200, ky), (kx + 196, ky + 230), (kx + 4, ky + 236), (kx, ky)]), w=2.2, fill='none')
    p.text(kx + 18, ky + 40, '★★☆☆☆', size=24, italic=False, op=.85)
    p.text(kx + 18, ky + 82, 'Η πόρτα δεν', size=24)
    p.text(kx + 18, ky + 112, 'έκλεινε καλά.', size=24)
    for k in range(4):
        p.line(p.seg(kx + 18, ky + 146 + k * 20, kx + 180 - (k % 2) * 30, ky + 146 + k * 20, 4), w=1.2, op=.4)
    p.end()
    p.dot(kx + 100, ky - 2, 5, 'currentColor')
    # η μικρή λεπτομέρεια: το κλειδί με τη μεγάλη ετικέτα κρεμασμένο στο πόμολο
    p.group('sk-sway', (dx + dw - 40, 409))
    p.line([(dx + dw - 40, 409), (dx + dw - 42, 440), (dx + dw - 38, 462)], w=1.6)
    p.line(p.poly([(dx + dw - 52, 462), (dx + dw - 24, 462), (dx + dw - 28, 510), (dx + dw - 48, 510), (dx + dw - 52, 462)], 3), w=1.8)
    p.end()
    return 'Μια πόρτα ξενοδοχείου, ίσια και με καινούριους μεντεσέδες που λάμπουν· δίπλα, καρφιτσωμένη στον τοίχο, μια κριτική δύο αστεριών γράφει «Η πόρτα δεν έκλεινε καλά».'


# 2. Το ξέρουν από το 2021 ---------------------------------------------------
@scene('2026/09/2021.html', 'to-xeroun-2021-b', dict(
    el='Δεν του λείπει η λέξη. Του λείπει το γύρισμα του κεφαλιού.', en='It does not lack the word. It lacks the turning of the head.',
    fr='Ce n’est pas le mot qui lui manque. C’est le geste de tourner la tête.', de='Ihm fehlt nicht das Wort. Ihm fehlt die Wendung des Kopfes.'))
def xeroun(p):
    p.floor()
    # αριστερά: οθόνη γεμάτη λέξεις, ακίνητη
    sx, sy = 120, 230
    p.line(p.poly([(sx, sy), (sx + 300, sy), (sx + 300, sy + 220), (sx, sy + 220), (sx, sy)]), w=2.6)
    for k in range(8):
        p.line(p.seg(sx + 24, sy + 30 + k * 23, sx + 276 - (k * 37) % 90, sy + 30 + k * 23, 5), w=1.3, op=.5)
    p.line(p.poly([(sx + 120, sy + 220), (sx + 110, 600)], 6), w=2.2); p.line(p.poly([(sx + 180, sy + 220), (sx + 190, 600)], 6), w=2.2)
    # δεξιά: χέρι που μπαίνει από την άκρη και δείχνει ψηλά, προς ένα μικρό πουλί
    p.line([(1200, 300), (1110, 286), (1030, 268)], w=2.8)                                   # πάνω γραμμή χεριού
    p.line([(1200, 340), (1110, 326), (1036, 304)], w=2.8)                                   # κάτω γραμμή
    p.line([(1030, 268), (1000, 250), (952, 214)], w=2.6)                                   # δείκτης, προς τα πάνω αριστερά
    p.line([(952, 214), (962, 230), (1004, 266)], w=2.2)
    p.line([(1036, 304), (1010, 300), (996, 284), (1006, 270)], w=2.2)                       # κλεισμένα δάχτυλα
    p.line([(1012, 300), (1000, 314), (1018, 318), (1034, 306)], w=2)                        # αντίχειρας
    p.group('sk-bob', (840, 130))
    p.line([(806, 132), (826, 118), (842, 128)], w=2.4); p.line([(842, 128), (860, 114), (880, 124)], w=2.4)
    p.end()
    p.group('sk-glow'); p.dot(842, 142, 4, OCHRE); p.end()
    # κουτάβι καθιστό, σε προφίλ, κοιτάζει προς το χέρι και το πουλί
    bx, by = 640, 600
    p.line([(bx - 60, by), (bx - 92, by - 30), (bx - 96, by - 80), (bx - 70, by - 130), (bx - 20, by - 150), (bx + 20, by - 140)], w=2.8)  # πλάτη
    p.line([(bx + 20, by - 140), (bx + 30, by - 90), (bx + 34, by)], w=2.6)                  # στήθος/μπροστινό πόδι
    p.line([(bx + 8, by - 80), (bx + 6, by)], w=2.4)                                          # άλλο πόδι
    p.line([(bx - 60, by), (bx + 44, by)], w=2.2)
    p.line([(bx - 94, by - 20), (bx - 134, by - 30), (bx - 146, by - 58)], w=2.2)          # ουρά
    p.group('sk-tilt', (bx + 10, by - 150))
    p.line(p.arc(bx + 20, by - 196, 44, 40, 0, 2 * PI, 26), w=2.8)                         # κεφάλι
    p.line([(bx + 56, by - 214), (bx + 92, by - 222), (bx + 98, by - 204), (bx + 60, by - 184)], w=2.4)  # μουσούδα
    p.dot(bx + 96, by - 214, 4.4)                                                            # μύτη
    p.dot(bx + 36, by - 210, 4)                                                              # μάτι
    p.line([(bx - 10, by - 232), (bx - 34, by - 196), (bx - 24, by - 160)], w=2.4)          # αυτί που κρέμεται
    p.end()
    # γραμμή βλέμματος, διακεκομμένη, από το κουτάβι στο πουλί
    p.out.append(f'<path class="sk-glow" d="M{bx + 70} {by - 236} Q 760 260 836 150" stroke="{OCHRE}" stroke-width="1.6" fill="none" stroke-dasharray="3 9" opacity=".9"/>')
    return 'Αριστερά μια οθόνη γεμάτη λέξεις. Στη μέση ένα κουτάβι γυρίζει το κεφάλι εκεί που δείχνει ένα ανθρώπινο χέρι, προς ένα μικρό πουλί.'


# 3. Η προειδοποίηση στα τσιγάρα -------------------------------------------
@scene('2026/09/blog-post_442.html', 'proeidopoiisi-b', dict(
    el='Λείπει από την πρόταση μια μικρή ερώτηση: ποιος.', en='A small question is missing from the sentence: who.',
    fr='Il manque à la phrase une petite question : qui.', de='Dem Satz fehlt eine kleine Frage: wer.'))
def proeid(p):
    p.floor()
    # εφημερίδα ανοιχτή πάνω σε τραπέζι
    p.line(p.poly([(160, 470), (1040, 470)], 14), w=2.4); p.line(p.seg(220, 470, 210, 600, 4), w=2.2); p.line(p.seg(980, 470, 990, 600, 4), w=2.2)
    nx, ny = 300, 150
    p.line(p.poly([(nx, ny), (nx + 560, ny + 6), (nx + 556, ny + 300), (nx - 4, ny + 296), (nx, ny)]), w=2.4)
    p.line(p.seg(nx + 280, ny + 10, nx + 278, ny + 292, 6), w=1.2, op=.4)
    p.text(nx + 30, ny + 64, 'Η ΤΝ', size=30, italic=False, spacing=1)
    p.text(nx + 146, ny + 64, 'επιτέθηκε', size=28, italic=False)
    # το κενό όπου θα έπρεπε να είναι ο «ποιος»
    p.group('sk-glow')
    p.line(p.poly([(nx + 26, ny + 84), (nx + 136, ny + 84)], 5), w=2.4, col=OCHRE)
    p.text(nx + 82, ny + 112, 'ποιος;', size=24, anchor='middle', col=OCHRE)
    p.end()
    for k in range(6):
        p.line(p.seg(nx + 30, ny + 150 + k * 22, nx + 250, ny + 150 + k * 22, 5), w=1.2, op=.45)
        p.line(p.seg(nx + 306, ny + 40 + k * 26, nx + 530, ny + 40 + k * 26, 5), w=1.2, op=.45)
    # πακέτο τσιγάρων στην άκρη του τραπεζιού, με το μαύρο πλαίσιο προειδοποίησης
    cx, cy = 900, 360
    p.line(p.poly([(cx, cy), (cx + 90, cy), (cx + 90, cy + 110), (cx, cy + 110), (cx, cy)], 4), w=2.4)
    p.line(p.poly([(cx + 8, cy + 54), (cx + 82, cy + 54), (cx + 82, cy + 100), (cx + 8, cy + 100), (cx + 8, cy + 54)], 3), w=1.8)
    p.text(cx + 45, cy + 84, 'ΒΛΑΠΤΕΙ', size=13, italic=False, anchor='middle', spacing=1)
    # τσιγάρο στο τασάκι με λίγο καπνό
    p.line(p.arc(820, 466, 34, 8, PI, 2 * PI, 10), w=2)
    p.line(p.seg(800, 460, 860, 446, 4), w=3)
    p.dot(862, 445, 3, OCHRE)
    p.steam(868, 430, 2)
    return 'Μια ανοιχτή εφημερίδα με τίτλο «Η ΤΝ επιτέθηκε»· μπροστά στον τίτλο λείπει μια λέξη και στη θέση της γράφει «ποιος;». Δίπλα ένα πακέτο τσιγάρα με την προειδοποίηση και ένα τσιγάρο που καπνίζει.'


# 4. Η τεχνητή νοημοσύνη δεν ήρθε από έξω ----------------------------------
@scene('2026/09/blog-post_12.html', 'den-irthe-apo-exo-b', dict(
    el='Ένα χέρι πάνω στο γυαλί, και δύο μάτια που κλείνουν.', en='A hand on the glass, and two eyes closing.',
    fr='Une main sur la vitre, et deux yeux qui se ferment.', de='Eine Hand auf dem Glas, und zwei Augen, die sich schließen.'))
def gatos(p):
    # παράθυρο κουζίνας, μεγάλο, στο κέντρο
    wx, wy, ww, wh = 300, 90, 600, 470
    p.line(p.poly([(wx, wy), (wx + ww, wy), (wx + ww, wy + wh), (wx, wy + wh), (wx, wy)]), w=3)
    p.line(p.seg(wx + ww / 2, wy, wx + ww / 2, wy + wh, 8), w=1.6, op=.5)
    p.line(p.poly([(wx - 40, wy + wh), (wx + ww + 40, wy + wh)], 8), w=2.6)                     # περβάζι
    p.line(p.poly([(wx - 40, wy + wh + 16), (wx + ww + 40, wy + wh + 16)], 8), w=1.6, op=.6)
    for k in range(2):
        p.line(p.seg(wx + 40 + k * 22, wy + 40, wx + 100 + k * 22, wy + 130, 3), w=1.2, op=.3)
    # γάτος έξω, καθιστός στο περβάζι, μεγάλος
    gx, gy = 700, wy + wh
    p.line([(gx - 90, gy), (gx - 96, gy - 60), (gx - 70, gy - 120), (gx, gy - 132)], w=2.8)
    p.line([(gx, gy - 132), (gx + 60, gy - 110), (gx + 84, gy - 50), (gx + 80, gy)], w=2.8)
    p.line([(gx + 80, gy - 6), (gx + 130, gy - 12), (gx + 150, gy - 50), (gx + 140, gy - 76)], w=2.2)  # ουρά
    p.line([(gx - 30, gy - 40), (gx - 32, gy)], w=2.2); p.line([(gx + 10, gy - 40), (gx + 8, gy)], w=2.2)
    hx, hy = gx - 10, gy - 190
    p.line(p.arc(hx, hy, 62, 54, 0, 2 * PI, 28), w=2.8)
    p.line([(hx - 54, hy - 26), (hx - 46, hy - 92), (hx - 14, hy - 52)], w=2.4)
    p.line([(hx + 14, hy - 52), (hx + 46, hy - 92), (hx + 54, hy - 26)], w=2.4)
    p.group('sk-blink', (hx, hy - 6))
    p.line(p.arc(hx - 22, hy - 6, 9, 8, 0, 2 * PI, 10), w=1.8); p.line(p.arc(hx + 22, hy - 6, 9, 8, 0, 2 * PI, 10), w=1.8)
    p.dot(hx - 22, hy - 6, 3); p.dot(hx + 22, hy - 6, 3)
    p.end()
    p.group('sk-blink-c', (hx, hy - 6))
    p.line(p.arc(hx - 22, hy - 6, 9, 4, 0, PI, 6), w=1.8); p.line(p.arc(hx + 22, hy - 6, 9, 4, 0, PI, 6), w=1.8)
    p.end()
    p.line([(hx - 6, hy + 14), (hx, hy + 20), (hx + 6, hy + 14)], w=1.8)
    for s_ in (-1, 1):
        for k in (0, 10):
            p.line(p.seg(hx + s_ * 26, hy + 20 + k, hx + s_ * 80, hy + 12 + k * 1.6, 3), w=1.2, op=.6)
    # το χέρι από μέσα: ανοιχτή παλάμη πάνω στο γυαλί, στο ύψος του κεφαλιού
    px, py = hx - 96, hy - 6
    p.group('sk-bob', (px, py))
    p.line(p.arc(px, py + 20, 36, 42, -PI * .05, PI * 1.05, 16), w=2.4)                     # βάση παλάμης
    for k, (fx, L) in enumerate(((-28, 50), (-10, 66), (8, 64), (24, 50))):
        p.line([(px + fx - 7, py + 6), (px + fx - 8, py - L + 8), (px + fx, py - L), (px + fx + 8, py - L + 8), (px + fx + 7, py + 6)], w=2)
    p.line([(px + 34, py + 30), (px + 62, py + 8), (px + 70, py + 18), (px + 40, py + 48)], w=2)  # αντίχειρας
    p.line([(px - 30, py + 58), (px - 34, wy + wh)], w=2.4); p.line([(px + 30, py + 60), (px + 34, wy + wh)], w=2.4)  # καρπός
    p.end()
    p.group('sk-glow'); p.ring(px + 4, py - 6, 70, 60, w=1.4, col=OCHRE, op=.8); p.end()
    p.floor(600, 40, 1160)
    return 'Ένας γάτος κάθεται έξω στο περβάζι ενός παραθύρου κουζίνας. Από μέσα ένα χέρι ακουμπά ανοιχτό πάνω στο τζάμι, εκεί που είναι το κεφάλι του, κι εκείνος κλείνει τα μάτια.'


# 5. «Μπορεί να κάνει λάθη» -------------------------------------------------
@scene('2026/09/blog-post_08.html', 'mporei-na-kanei-lathi', dict(
    el='Η μικρή φράση στο κάτω μέρος. Το μεγάλο κτίριο δεν έχει καμία.', en='The small line at the bottom. The big building has none.',
    fr='La petite phrase en bas. Le grand bâtiment n’en a aucune.', de='Der kleine Satz unten. Das große Gebäude hat keinen.'))
def lathi(p):
    p.floor()
    # κρατικό κτίριο με κίονες, μεγάλο, δεξιά
    bx, by = 640, 230
    p.line(p.poly([(bx - 20, by), (bx + 240, by - 110), (bx + 500, by), (bx - 20, by)], 8), w=2.8)  # αέτωμα
    p.line(p.seg(bx - 30, by + 18, bx + 510, by + 18, 12), w=2.4)
    for k in range(6):
        x = bx + 10 + k * 92
        p.line(p.seg(x, by + 30, x, 560, 8), w=2.2); p.line(p.seg(x + 30, by + 30, x + 30, 560, 8), w=2.2)
    p.line(p.seg(bx - 40, 566, bx + 520, 566, 12), w=2.4); p.line(p.seg(bx - 60, 586, bx + 540, 586, 12), w=2.2)
    # σημαία που κυματίζει
    p.line(p.seg(bx + 240, by - 110, bx + 240, by - 210, 4), w=2)
    p.group('sk-sway', (bx + 240, by - 200))
    p.line([(bx + 240, by - 206), (bx + 280, by - 214), (bx + 318, by - 198), (bx + 316, by - 160), (bx + 278, by - 174), (bx + 240, by - 166)], w=2)
    p.end()
    # αριστερά: η απάντηση του μοντέλου, σε πλαίσιο, με τη μικρή φράση κάτω
    ax, ay = 110, 200
    p.line(p.poly([(ax, ay), (ax + 380, ay), (ax + 380, ay + 290), (ax, ay + 290), (ax, ay)]), w=2.4)
    for k in range(7):
        p.line(p.seg(ax + 26, ay + 34 + k * 26, ax + 354 - (k * 41) % 110, ay + 34 + k * 26, 6), w=1.3, op=.5)
    p.text(ax + 190, ay + 270, 'μπορεί να κάνει λάθη', size=15, anchor='middle', op=.8)
    # μεγεθυντικός φακός πάνω στη μικρή φράση
    p.group('sk-bob', (ax + 190, ay + 264))
    p.ring(ax + 190, ay + 264, 44, w=2.6, col=OCHRE)
    p.line(p.seg(ax + 222, ay + 296, ax + 270, ay + 344, 3), w=4)
    p.end()
    return 'Αριστερά μια απάντηση μοντέλου σε πλαίσιο, με τη μικρή φράση «μπορεί να κάνει λάθη» στο κάτω μέρος και έναν φακό πάνω της. Δεξιά ένα μεγάλο κρατικό κτίριο με κίονες και σημαία, χωρίς καμία τέτοια φράση.'


# 6. Πού είναι ο κόσμος; -----------------------------------------------------
@scene('2026/09/blog-post_07.html', 'pou-einai-o-kosmos', dict(
    el='Είμαι εγώ. Δεν είμαι εγώ έτσι.', en='It is me. I am not like that.',
    fr='C’est moi. Je ne suis pas comme ça.', de='Das bin ich. So bin ich nicht.'))
def kosmos(p):
    p.floor()
    p.window(860, 220, 600, 160, .3)
    # άνθρωπος όρθιος, κοιτάζει μια φωτογραφία που κρατά
    hx, hy = 420, 230
    p.head(hx, hy, 40, look=1)
    p.line(p.arc(hx + 16, hy + 22, 6, 4, 0, PI, 6), w=1.8)                                    # στόμα σφιγμένο
    p.line([(hx - 8, hy + 42), (hx - 30, 380), (hx - 26, 470), (hx - 40, 600)], w=2.8)
    p.line([(hx + 14, hy + 42), (hx + 30, 380), (hx + 26, 470), (hx + 36, 600)], w=2.8)
    p.line([(hx - 52, 600), (hx - 30, 600)], w=3); p.line([(hx + 30, 600), (hx + 58, 600)], w=3)
    p.line([(hx + 20, 320), (hx + 80, 360), (hx + 140, 340)], w=2.6)                          # χέρι
    # η φωτογραφία: το ίδιο πρόσωπο, χαμογελαστό
    fx, fy = hx + 130, 250
    p.group('sk-sway', (fx + 4, fy + 100))
    p.line(p.poly([(fx, fy), (fx + 120, fy - 6), (fx + 126, fy + 140), (fx + 6, fy + 146), (fx, fy)], 4), w=2.4)
    p.line(p.arc(fx + 62, fy + 58, 22, 23, 0, 2 * PI, 18), w=2)
    p.line(p.arc(fx + 54, fy + 54, 5, 4, 0, 2 * PI, 8), w=1.4); p.line(p.arc(fx + 70, fy + 54, 5, 4, 0, 2 * PI, 8), w=1.4)
    p.line(p.arc(fx + 62, fy + 64, 9, 6, 0, PI, 8), w=1.6)                                       # χαμόγελο
    p.line([(fx + 44, fy + 82), (fx + 34, fy + 136)], w=1.8); p.line([(fx + 80, fy + 82), (fx + 92, fy + 136)], w=1.8)
    p.end()
    # γωνίτσα φωτός στη φωτογραφία
    p.group('sk-glow'); p.line([(fx + 98, fy + 4), (fx + 118, fy - 4), (fx + 122, fy + 18)], w=2.4, col=OCHRE); p.end()
    # ερωτηματικό που πάει και έρχεται, σαν σκέψη
    p.group('sk-bob', (hx - 70, hy - 70))
    p.text(hx - 80, hy - 60, ';', size=54, italic=False, op=.75)
    p.end()
    return 'Ένας άνθρωπος με γυαλιά κοιτάζει σφιγμένος μια φωτογραφία που κρατά, όπου το ίδιο πρόσωπο χαμογελά.'


# 7. Όταν είπα στο θεό ---------------------------------------------------------
@scene('2026/09/blog-post.html', 'katofli', dict(
    el='Τα παπούτσια έμειναν στο κατώφλι.', en='The shoes stayed at the threshold.',
    fr='Les chaussures sont restées sur le seuil.', de='Die Schuhe blieben auf der Schwelle.'))
def katofli(p):
    p.floor()
    # η είσοδος ενός ναού: τόξο και δίφυλλη πόρτα ανοιχτή στο σκοτάδι
    cx = 640
    p.line(p.seg(cx - 170, 600, cx - 170, 260) + p.arc(cx, 260, 170, 170, PI, 2 * PI)[1:] + p.seg(cx + 170, 260, cx + 170, 600)[1:], w=3)
    p.line(p.seg(cx - 130, 600, cx - 130, 280) + p.arc(cx, 280, 130, 130, PI, 2 * PI)[1:] + p.seg(cx + 130, 280, cx + 130, 600)[1:], w=1.6, op=.6)
    p.line(p.seg(cx - 220, 610, cx + 220, 610, 10), w=2.4); p.line(p.seg(cx - 250, 630, cx + 250, 630, 10), w=2)  # σκαλοπάτια
    # μέσα, στο βάθος: ένα κερί που τρεμοπαίζει
    p.line(p.seg(cx, 520, cx, 440, 4), w=2.6)
    p.line(p.seg(cx - 26, 520, cx + 26, 520, 4), w=2)
    p.group('sk-flicker', (cx, 436))
    p.out.append(f'<path d="M{cx} 400 Q{cx + 12} 420 {cx} 436 Q{cx - 12} 420 {cx} 400Z" fill="{OCHRE}" stroke="{OCHRE}" stroke-width="1.5"/>')
    p.end()
    p.group('sk-glow'); p.ring(cx, 420, 46, w=1.2, col=OCHRE, op=.5); p.end()
    # τα παπούτσια, στη σειρά στο κατώφλι
    def shoe(x, y=604, f=1, rot=0):
        pts = [(0, 0), (0, -14), (20, -18), (32, -28), (48, -24), (60, -10), (62, 0), (0, 0)]
        c, s_ = math.cos(rot), math.sin(rot)
        p.line([(x + f * (u * c - v * s_), y + u * s_ + v * c) for u, v in pts], w=2.2)
    for x in (cx - 150, cx - 20):
        shoe(x); shoe(x + 66)
    shoe(cx + 190, 604, 1, -.12); shoe(cx + 290, 600, -1, .25)                               # το δικό του, στραβά
    # ίχνη από γυμνά πόδια που φεύγουν δεξιά
    for k in range(4):
        x = cx + 300 + k * 70; y = 600 + (k % 2) * 10
        p.out.append(f'<ellipse cx="{x}" cy="{y - 8}" rx="11" ry="5" fill="currentColor" opacity="{.5 - k * .1:.2f}"/>')
    return 'Η τοξωτή είσοδος ενός ναού, με ένα κερί που τρεμοπαίζει στο βάθος. Στο κατώφλι παπούτσια στη σειρά, ένα ζευγάρι αφημένο στραβά, και ίχνη από γυμνά πόδια που φεύγουν.'


# 8. Η σιωπή που γνωρίζει ότι είναι -----------------------------------------
@scene('2026/05/blog-post.html', 'siopi', dict(
    el='Ο θόρυβος περνά. Κάτι μένει και ξέρει ότι μένει.', en='The noise passes. Something stays, and knows it stays.',
    fr='Le bruit passe. Quelque chose demeure, et sait qu’il demeure.', de='Der Lärm vergeht. Etwas bleibt und weiß, dass es bleibt.'))
def siopi(p):
    # ορίζοντας θάλασσας, χαμηλά
    p.line(p.seg(40, 520, 1160, 520, 22), w=1.6, op=.5)
    for k in range(3):
        p.line(p.seg(120 + k * 300, 556 + k * 14, 300 + k * 300, 556 + k * 14, 5), w=1.2, op=.3)
    # άνθρωπος καθιστός σταυροπόδι, από πίσω, στο κέντρο
    cx, cy = 600, 470
    p.line(p.arc(cx, cy - 170, 34, 36, 0, 2 * PI, 26), w=2.8)
    p.line([(cx - 14, cy - 136), (cx - 46, cy - 90), (cx - 58, cy - 20), (cx - 90, cy + 20)], w=2.8)
    p.line([(cx + 14, cy - 136), (cx + 46, cy - 90), (cx + 58, cy - 20), (cx + 90, cy + 20)], w=2.8)
    p.line([(cx - 110, cy + 24), (cx - 20, cy + 40), (cx + 20, cy + 40), (cx + 110, cy + 24)], w=2.6)
    # κύματα θορύβου γύρω, που απλώνουν και σβήνουν
    for i in range(3):
        p.group(f'sk-ripple sk-r{i}', (cx, cy - 120))
        p.line(p.arc(cx, cy - 120, 150, 120, -PI * .15, PI * .15, 8), w=1.6, op=.6)
        p.line(p.arc(cx, cy - 120, 150, 120, PI * .85, PI * 1.15, 8), w=1.6, op=.6)
        p.end()
    # η σιωπή: ένα σταθερό σημείο φωτός πάνω από τον ορίζοντα, που ανασαίνει αργά
    p.group('sk-glow'); p.dot(cx, 160, 7, OCHRE); p.ring(cx, 160, 20, w=1.2, col=OCHRE, op=.6); p.end()
    return 'Ένας άνθρωπος κάθεται σταυροπόδι μπροστά σε έναν ήσυχο ορίζοντα θάλασσας. Γύρω του κύματα θορύβου απλώνουν και σβήνουν· ψηλά ένα μικρό σταθερό φως.'


def main():
    sj = os.path.join(ROOT, 'content', 'sketches.json')
    data = json.load(open(sj, encoding='utf-8'))
    for path, (slug, cap, fn) in S.items():
        p = Pen(seed=sum(map(ord, slug)))
        label = fn(p)
        open(os.path.join(ROOT, 'assets', 'sketches', slug + '.svg'), 'w', encoding='utf-8').write(p.svg(label))
        old = data.get(path)
        if old and old.get('slug') != slug:
            data.setdefault('_prev', {})[path] = old          # η προηγούμενη εκδοχή κρατιέται
        data[path] = dict(slug=slug, caption=cap, approved=True, alt=label)
        print(slug)
    json.dump(data, open(sj, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)


if __name__ == '__main__':
    main()
