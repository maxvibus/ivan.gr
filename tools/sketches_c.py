"""Σκίτσα δημοσιεύσεων, τρίτη σειρά (21.10.2026): Μάρτιος–Απρίλιος 2026 και Φεβρουάριος 2026."""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pen import OCHRE
from sketchbook import registry, person, run, PI

S, scene = registry()


@scene('2026/04/blog-post.html', 'theiotita', dict(
    el='Ένα φωτοστέφανο χωρίς πρόσωπο, πάνω από τα κάγκελα.', en='A halo with no face, above the bars.',
    fr='Une auréole sans visage, au-dessus des barreaux.', de='Ein Heiligenschein ohne Gesicht, über den Gitterstäben.'))
def theiotita(p):
    p.floor()
    # κάγκελα στάβλου
    for k in range(9):
        x = 300 + k * 75
        p.line(p.seg(x, 600, x, 300, 8), w=2.2, op=.8)
    p.line(p.seg(280, 300, 920, 300, 14), w=2.4); p.line(p.seg(280, 440, 920, 440, 14), w=1.8, op=.7)
    # αγελάδα πίσω από τα κάγκελα, ήσυχη
    cx, cy = 600, 470
    p.line([(cx - 160, cy - 40), (cx - 150, cy - 100), (cx - 60, cy - 116), (cx + 90, cy - 112), (cx + 150, cy - 90), (cx + 156, cy - 30)], w=2.8)
    p.line([(cx - 160, cy - 40), (cx - 150, cy + 20), (cx + 150, cy + 24), (cx + 156, cy - 30)], w=2.6)
    for lx in (cx - 130, cx - 90, cx + 100, cx + 136):
        p.line(p.seg(lx, cy + 20, lx + 2, 598, 4), w=2.4)
    hx, hy = cx - 200, cy - 90                                   # κεφάλι γερτό προς το έδαφος
    p.line([(cx - 150, cy - 100), (hx + 20, hy - 10), (hx - 20, hy + 30), (hx - 30, hy + 90), (hx + 10, hy + 110), (hx + 40, hy + 70), (cx - 156, cy - 20)], w=2.6)
    p.line([(hx + 10, hy - 6), (hx - 18, hy - 30)], w=2.2); p.line([(hx + 30, hy - 4), (hx + 44, hy - 34)], w=2.2)  # κέρατα
    p.group('sk-blink', (hx + 6, hy + 30)); p.dot(hx + 6, hy + 30, 3.4); p.end()
    for k in range(4):                                           # κηλίδες
        p.ring(cx - 40 + k * 55, cy - 60 + (k % 2) * 30, 14 + k * 3, w=1.4, op=.5)
    # το φωτοστέφανο: ένας δακτύλιος φωτός που δεν ακουμπά κανένα κεφάλι
    p.group('sk-glow')
    p.ring(600, 170, 70, 18, w=3, col=OCHRE)
    p.end()
    p.group('sk-bob', (600, 170)); p.ring(600, 170, 92, 26, w=1.2, col=OCHRE, op=.5); p.end()
    return 'Μια αγελάδα στέκεται ήσυχη πίσω από κάγκελα στάβλου, με το κεφάλι χαμηλά. Ψηλά από πάνω αιωρείται ένα φωτοστέφανο που δεν ανήκει σε κανένα πρόσωπο.'


@scene('2026/03/blog-post_18.html', 'mana-kai-paidi', dict(
    el='Η αγκαλιά, και η σκιά που της έκλεψε το σχήμα.', en='The embrace, and the shadow that stole its shape.',
    fr='L’étreinte, et l’ombre qui lui a volé sa forme.', de='Die Umarmung, und der Schatten, der ihr die Form gestohlen hat.'))
def mana(p):
    p.floor()
    # η σκιά στον τοίχο: μεγάλη, με στέμμα, στην ίδια χειρονομία — μόνο περίγραμμα, αχνό
    sx = 760
    p.line(p.arc(sx, 210, 70, 74, 0, 2 * PI, 30), w=2, op=.35)
    p.line(p.poly([(sx - 50, 150), (sx - 40, 100), (sx - 14, 132), (sx, 92), (sx + 14, 132), (sx + 40, 100), (sx + 50, 150)], 3), w=2, op=.4)
    p.line([(sx - 70, 280), (sx - 130, 420), (sx - 120, 600)], w=2, op=.35); p.line([(sx + 70, 280), (sx + 140, 420), (sx + 130, 600)], w=2, op=.35)
    p.line([(sx - 110, 360), (sx - 20, 420), (sx + 60, 380)], w=2, op=.35)           # το χέρι που «αγκαλιάζει»
    p.ring(sx + 10, 380, 36, w=1.6, op=.3)                                          # το «παιδί» του: κενό
    # η μάνα με το παιδί, μπροστά, μικρή και ζεστή
    mx = 380
    p.head(mx, 300, 34, glasses=False, look=1)
    p.line([(mx - 40, 280), (mx - 50, 330), (mx - 30, 360)], w=2, op=.8)            # μαλλιά πίσω
    p.line([(mx - 6, 336), (mx - 34, 352), (mx - 46, 440), (mx - 70, 600)], w=2.8)            # φόρεμα
    p.line([(mx + 8, 336), (mx + 34, 350), (mx + 50, 450), (mx + 74, 600)], w=2.8)
    p.line(p.seg(mx - 70, 600, mx + 74, 600, 6), w=2.2, op=.6)
    p.group('sk-bob', (mx + 50, 400))
    p.line(p.arc(mx + 50, 392, 26, 24, 0, 2 * PI, 22), w=2.4)                       # το κεφάλι του παιδιού
    p.line(p.arc(mx + 56, 398, 5, 3, 0, PI, 6), w=1.6)
    p.line([(mx + 30, 414), (mx + 50, 470), (mx + 100, 470), (mx + 96, 430)], w=2.4)
    p.end()
    p.line([(mx + 14, 352), (mx + 60, 440), (mx + 110, 450)], w=2.6)                 # χέρι που κρατά
    p.line([(mx - 8, 360), (mx + 20, 400), (mx + 74, 404)], w=2.4)
    p.group('sk-glow'); p.ring(mx + 50, 420, 72, 66, w=1.4, col=OCHRE, op=.8); p.end()
    return 'Μια μάνα κρατά το παιδί της στην αγκαλιά. Πίσω τους στον τοίχο, μια μεγάλη σκιά με στέμμα κάνει την ίδια χειρονομία, αλλά η αγκαλιά της είναι άδεια.'


@scene('2026/03/blog-post_17.html', 'diaxeiristis', dict(
    el='Κάτι γράφεται, και δεν κάθεται κανείς στην καρέκλα.', en='Something is being written, and no one sits in the chair.',
    fr='Quelque chose s’écrit, et personne n’est assis sur la chaise.', de='Etwas wird geschrieben, und niemand sitzt auf dem Stuhl.'))
def diax(p):
    p.floor()
    p.window(860, 200, 600, 150, .3)
    # τραπέζι και γραφομηχανή
    p.line(p.seg(260, 420, 700, 420, 10), w=2.6); p.line(p.seg(290, 420, 290, 600, 6), w=2.4); p.line(p.seg(670, 420, 670, 600, 6), w=2.4)
    tx, ty = 470, 420
    p.line(p.poly([(tx - 90, ty), (tx - 80, ty - 60), (tx + 80, ty - 60), (tx + 90, ty), (tx - 90, ty)], 4), w=2.6)
    for r in range(3):
        for k in range(8):
            p.group(f'sk-glow') if (r == 1 and k == 4) else None
            p.dot(tx - 60 + k * 17 + r * 4, ty - 44 + r * 14, 3)
            p.end() if (r == 1 and k == 4) else None
    p.line(p.seg(tx - 100, ty - 70, tx + 100, ty - 70, 6), w=3)                    # κύλινδρος
    # το χαρτί που βγαίνει, με γραμμές που γράφονται μόνες
    p.line(p.poly([(tx - 60, ty - 70), (tx - 58, ty - 230), (tx + 60, ty - 236), (tx + 62, ty - 70)], 5), w=2)
    for k in range(5):
        p.line(p.seg(tx - 44, ty - 210 + k * 26, tx + 44 - (k * 13) % 30, ty - 210 + k * 26, 4), w=1.3, op=.5)
    p.group('sk-glow'); p.line(p.seg(tx - 44, ty - 80, tx + 8, ty - 80, 3), w=2, col=OCHRE); p.end()
    # η άδεια καρέκλα
    cx = 470
    p.line(p.poly([(cx - 50, 600), (cx - 46, 500), (cx + 50, 500), (cx + 54, 600)], 5), w=2.4)
    p.line(p.poly([(cx + 46, 500), (cx + 60, 380)], 5), w=2.4); p.line(p.poly([(cx - 40, 500), (cx - 30, 470)], 2), w=2.2)
    # φλιτζάνι, ακόμα ζεστό
    p.line(p.poly([(620, 420), (616, 390), (650, 390), (646, 420)], 3), w=2); p.steam(633, 380, 2)
    return 'Μια γραφομηχανή πάνω σε τραπέζι γράφει μόνη της σε ένα χαρτί. Η καρέκλα μπροστά της είναι άδεια· δίπλα, ένα φλιτζάνι ακόμα αχνίζει.'


@scene('2026/03/blog-post_14.html', 'ego-gramma', dict(
    el='Μια γραμμή στο χώμα: από εδώ εγώ, από εκεί ο κόσμος.', en='A line in the dirt: here I am, there the world.',
    fr='Une ligne dans la terre : ici moi, là le monde.', de='Eine Linie im Staub: hier ich, dort die Welt.'))
def ego(p):
    p.line(p.seg(40, 560, 1160, 560, 20), w=1.4, op=.4)
    # ο άνθρωπος με το ραβδί σέρνει κύκλο γύρω του
    x = 560
    person(p, x, 540, h=.9, arm=[(x + 70, 440), (x + 120, 470)])
    p.line(p.seg(x + 120, 470, x + 200, 560, 4), w=2.6)                            # ραβδί
    p.group('sk-glow'); p.line(p.arc(x, 560, 230, 46, PI * .05, PI * 1.98, 40), w=2.6, col=OCHRE); p.end()
    # έξω από τον κύκλο ο κόσμος: πουλιά, ένα δέντρο, ο ήλιος
    p.group('sk-bob', (200, 170))
    p.line([(170, 170), (190, 156), (206, 166)], w=2.2); p.line([(206, 166), (224, 152), (244, 162)], w=2.2)
    p.end()
    tx = 980
    p.line(p.seg(tx, 560, tx, 380, 5), w=2.6)
    p.group('sk-sway', (tx, 380)); p.line(p.arc(tx, 320, 80, 70, 0, 2 * PI, 26), w=2.2); p.end()
    p.ring(200, 380, 40, w=1.6, op=.6)
    for k in range(8):
        a = k * PI / 4; p.line(p.seg(200 + 52 * math.cos(a), 380 + 52 * math.sin(a), 200 + 66 * math.cos(a), 380 + 66 * math.sin(a), 2), w=1.4, op=.6)
    return 'Ένας άνθρωπος με ένα ραβδί χαράζει κύκλο στο χώμα γύρω από τον εαυτό του. Έξω από τον κύκλο πουλιά, ένα δέντρο, ο ήλιος.'


@scene('2026/03/blog-post_13.html', 'dyo-typoi', dict(
    el='Το ίδιο βιβλίο: μαξιλάρι για τον έναν, πηγάδι για τον άλλον.', en='The same book: a pillow for one, a well for the other.',
    fr='Le même livre : un oreiller pour l’un, un puits pour l’autre.', de='Dasselbe Buch: ein Kissen für den einen, ein Brunnen für den anderen.'))
def dyo(p):
    p.floor()
    p.line(p.seg(600, 140, 600, 600, 12), w=1.2, op=.3)
    # αριστερά: ξαπλωμένος, το βιβλίο κάτω από το κεφάλι
    p.line(p.poly([(140, 560), (300, 556), (304, 580), (138, 584), (140, 560)], 4), w=2.2)   # βιβλίο-μαξιλάρι
    p.line(p.arc(220, 528, 32, 30, 0, 2 * PI, 22), w=2.6)
    for k in (-10, 10): p.line(p.arc(220 + k, 526, 6, 3, 0, PI, 6), w=1.6)
    p.line([(250, 540), (360, 560), (500, 566)], w=2.6); p.line([(250, 556), (360, 590), (500, 596)], w=2.6)
    p.group('sk-bob', (300, 450)); p.text(280, 470, 'z', size=26, op=.6); p.text(304, 444, 'z', size=34, op=.5); p.end()
    # δεξιά: καθιστός, σκυμμένος στο ίδιο βιβλίο, με λάμπα — και από το βιβλίο κατεβαίνει πηγάδι
    x = 820
    p.head(x, 360, 34, glasses=True, look=1)
    p.line([(x - 8, 396), (x - 30, 470), (x - 30, 560)], w=2.8); p.line([(x + 14, 394), (x + 40, 450)], w=2.6)
    p.line(p.seg(x - 30, 560, x + 70, 560, 4), w=2.6); p.line(p.seg(x + 70, 560, x + 76, 600, 3), w=2.6)
    p.line(p.poly([(x + 30, 470), (x + 150, 466), (x + 156, 486), (x + 26, 490), (x + 30, 470)], 4), w=2.2)  # ανοιχτό βιβλίο
    p.line(p.seg(x + 92, 470, x + 92, 488, 2), w=1.4)
    for k in range(4):                                              # το πηγάδι κάτω από το βιβλίο
        p.line(p.arc(x + 92, 520 + k * 22, 40 - k * 6, 8 - k, 0, 2 * PI, 18), w=1.4, op=.5 - k * .1)
    p.line(p.seg(x + 160, 330, x + 160, 486, 5), w=2)                 # λάμπα
    p.line(p.arc(x + 160, 330, 34, 26, PI, 2 * PI, 10), w=2.2)
    p.group('sk-glow'); p.ring(x + 150, 360, 50, 30, w=1.4, col=OCHRE, op=.7); p.dot(x + 160, 336, 4, OCHRE); p.end()
    return 'Δύο άνθρωποι με το ίδιο βιβλίο. Ο ένας κοιμάται με το βιβλίο κάτω από το κεφάλι. Ο άλλος διαβάζει σκυμμένος στο φως μιας λάμπας, και κάτω από τις σελίδες ανοίγει ένα πηγάδι.'


@scene('2026/03/ai.html', 'oria-glossas', dict(
    el='Πριν κλειδώσει η λέξη, όλες αιωρούνται.', en='Before the word locks in, they all hover.',
    fr='Avant que le mot ne se fige, tous flottent.', de='Bevor das Wort einrastet, schweben sie alle.'))
def oria(p):
    p.floor()
    p.line(p.poly([(340, 520), (860, 520), (880, 560), (320, 560), (340, 520)], 8), w=2.4)    # ανοιχτό τετράδιο
    p.line(p.seg(600, 520, 600, 560, 2), w=1.6)
    for k in range(3):
        p.line(p.seg(370, 534 + k * 8, 580, 534 + k * 8, 6), w=1, op=.35)
    # μολύβι που περιμένει
    p.line(p.seg(700, 500, 790, 420, 4), w=5, op=.6); p.line(p.seg(690, 510, 700, 500, 2), w=2)
    letters = 'λόγοςφωςοδόςκόσμοςνους'
    import random
    rr = random.Random(5)
    for i, ch in enumerate(letters):
        x = 380 + rr.uniform(0, 440); y = 180 + rr.uniform(0, 240)
        cls = 'sk-bob' if i % 2 else 'sk-sway'
        p.group(cls, (x, y))
        p.text(f'{x:.0f}', f'{y:.0f}', ch, size=rr.choice((34, 40, 48)), op=.45 + rr.random() * .45, col=OCHRE if i == 7 else 'currentColor')
        p.end()
    return 'Πάνω από ένα ανοιχτό τετράδιο και ένα μολύβι που περιμένει, γράμματα αιωρούνται ακόμα χωρίς σειρά· ένα από αυτά λάμπει.'


@scene('2026/03/blog-post_21.html', 'ekprosopisi', dict(
    el='Του έδωσε το κλειδί. Η πόρτα ήταν η δική του.', en='He gave him the key. The door was his own.',
    fr='Il lui a donné la clé. La porte était la sienne.', de='Er gab ihm den Schlüssel. Die Tür war seine eigene.'))
def ekpros(p):
    p.floor()
    # ο πολίτης μέσα σε ένα πλαίσιο πόρτας με κάγκελα πίσω του
    x = 360
    for k in range(5):
        p.line(p.seg(240 + k * 60, 600, 240 + k * 60, 220, 8), w=1.8, op=.5)
    p.line(p.seg(220, 220, 500, 220, 8), w=2.2, op=.6)
    person(p, x, 600, h=.95, arm=[(x + 80, 330), (x + 150, 300)])
    # το κλειδί στην παλάμη, ανεβαίνει προς τον άλλον
    p.group('sk-sway', (x + 160, 296))
    p.ring(x + 168, 292, 12, w=2.4, col=OCHRE); p.line(p.seg(x + 180, 292, x + 230, 292, 3), w=2.4, col=OCHRE)
    p.line(p.seg(x + 218, 292, x + 218, 304, 1), w=2.2, col=OCHRE); p.line(p.seg(x + 228, 292, x + 228, 302, 1), w=2.2, col=OCHRE)
    p.end()
    # ο εκπρόσωπος σε βάθρο, ψηλά, με το χέρι απλωμένο
    bx = 820
    p.line(p.poly([(bx - 110, 600), (bx - 100, 420), (bx + 100, 420), (bx + 110, 600)], 6), w=2.6)
    person(p, bx, 420, h=.8, look=-1, arm=[(bx - 40, 280), (bx - 110, 270)])
    return 'Ένας πολίτης, με κάγκελα πίσω του, απλώνει ένα κλειδί προς έναν άνθρωπο ψηλά σε βάθρο, που τεντώνει το χέρι να το πάρει.'


@scene('2026/03/blog-post_7.html', 'leyka', dict(
    el='Τα λευκά πέφτουν έξω από την κάλπη.', en='The blank ballots fall outside the box.',
    fr='Les bulletins blancs tombent hors de l’urne.', de='Die leeren Stimmzettel fallen neben die Urne.'))
def leyka(p):
    p.floor()
    bx, by = 600, 400
    p.line(p.poly([(bx - 120, 600), (bx - 120, by), (bx + 120, by), (bx + 120, 600)], 8), w=2.8)  # κάλπη
    p.line(p.seg(bx - 50, by, bx + 50, by, 4), w=4)
    p.text(bx, by + 110, 'ΚΑΛΠΗ', size=24, italic=False, anchor='middle', spacing=4, op=.75)
    # γεμάτα ψηφοδέλτια μπαίνουν
    for k, (x, y, r) in enumerate(((560, 300, -.2), (620, 250, .15))):
        p.line(p.poly([(x - 30, y), (x + 30, y + r * 30), (x + 30, y + 40 + r * 30), (x - 30, y + 40), (x - 30, y)], 3), w=2)
        p.line(p.seg(x - 20, y + 14, x + 18, y + 14 + r * 20, 3), w=1.4, op=.6)
    # λευκά ψηφοδέλτια που πέφτουν έξω, αργά
    for k, (x, y) in enumerate(((330, 230), (880, 280), (800, 520), (400, 500))):
        p.group('sk-flutter' if k % 2 else 'sk-sway', (x, y))
        p.line(p.poly([(x - 30, y), (x + 30, y - 8), (x + 34, y + 32), (x - 26, y + 40), (x - 30, y)], 3), w=1.8, op=.7)
        p.end()
    p.group('sk-glow'); p.line(p.poly([(370, 580), (430, 572), (434, 598), (372, 600), (370, 580)], 3), w=2, col=OCHRE); p.end()
    return 'Μια κάλπη· δύο γραμμένα ψηφοδέλτια μπαίνουν μέσα, ενώ λευκά ψηφοδέλτια πέφτουν αργά γύρω της, έξω από αυτήν.'


@scene('2026/03/blog-post.html', 'aporia', dict(
    el='Η απορία γύρισε και κοίταξε τον εαυτό της.', en='Wonder turned and looked at itself.',
    fr='L’étonnement s’est retourné et s’est regardé lui-même.', de='Das Staunen drehte sich um und sah sich selbst an.'))
def aporia(p):
    p.floor()
    # άνθρωπος μπροστά σε καθρέφτη· το είδωλο κοιτάζει τον ίδιο
    x = 420
    person(p, x, 600, h=1, glasses=True, look=1)
    mx = 760
    p.line(p.poly([(mx - 120, 600), (mx - 120, 160), (mx + 120, 160), (mx + 120, 600)], 8), w=2.8)
    p.line(p.poly([(mx - 100, 580), (mx - 100, 180), (mx + 100, 180), (mx + 100, 580)], 8), w=1.4, op=.5)
    p.head(mx, 270, 34 * .9, glasses=True, look=-1)
    p.line([(mx - 8, 304), (mx - 24, 400), (mx - 22, 470)], w=2.2, op=.6); p.line([(mx + 10, 304), (mx + 24, 400), (mx + 22, 470)], w=2.2, op=.6)
    # ερωτηματικό που γυρίζει σε σπείρα ανάμεσά τους
    sx, sy = 590, 170
    pts = [(sx + (4 + t * 3.2) * math.cos(t * .9), sy + (4 + t * 3.2) * math.sin(t * .9)) for t in range(0, 18)]
    p.group('sk-sway', (sx, sy)); p.line(pts, w=2.2, col=OCHRE); p.dot(sx + 2, sy + 70, 4, OCHRE); p.end()
    return 'Ένας άνθρωπος με γυαλιά στέκεται μπροστά σε καθρέφτη και το είδωλό του τον κοιτάζει· ανάμεσά τους ένα ερωτηματικό τυλίγεται σε σπείρα.'


@scene('2026/02/blog-post.html', 'skiniko', dict(
    el='Ένα δέντρο ζωγραφισμένο σε σκηνικό, ανάμεσα σε αληθινά.', en='A tree painted on a stage flat, among real ones.',
    fr='Un arbre peint sur un décor, parmi de vrais arbres.', de='Ein auf eine Kulisse gemalter Baum, zwischen echten.'))
def skiniko(p):
    p.floor()
    def tree(x, s=1, cls='sk-sway'):
        p.line(p.seg(x, 600, x, 600 - 170 * s, 5), w=2.6)
        if cls: p.group(cls, (x, 600 - 170 * s))
        p.line(p.arc(x, 600 - 240 * s, 80 * s, 76 * s, 0, 2 * PI, 26), w=2.2)
        p.line(p.arc(x - 20 * s, 600 - 250 * s, 40 * s, 36 * s, 0, 2 * PI, 18), w=1.4, op=.5)
        if cls: p.end()
    tree(200, 1); tree(1000, .9)
    # σκηνικό: επίπεδη τάβλα με στήριγμα από πίσω, ζωγραφισμένο δέντρο, ακίνητο
    fx = 600
    p.line(p.poly([(fx - 130, 600), (fx - 130, 240), (fx + 130, 240), (fx + 130, 600)], 8), w=2.4)
    p.line(p.seg(fx + 130, 300, fx + 200, 600, 6), w=2, op=.7)                      # αντηρίδα
    p.line(p.seg(fx + 150, 400, fx + 176, 400, 2), w=1.6, op=.6)
    p.line(p.seg(fx, 590, fx, 440, 5), w=2.6)
    p.line(p.arc(fx, 370, 90, 84, 0, 2 * PI, 30), w=2.2)
    p.line(p.arc(fx - 20, 360, 44, 40, 0, 2 * PI, 18), w=1.4, op=.5)
    for k in range(4):
        p.line(p.seg(fx - 120, 270 + k * 90, fx - 100, 250 + k * 90, 2), w=1, op=.3)  # νερά του ξύλου
    p.group('sk-glow'); p.ring(1080, 150, 30, w=2, col=OCHRE); p.end()
    return 'Δύο αληθινά δέντρα κουνιούνται στον αέρα· ανάμεσά τους ένα δέντρο ζωγραφισμένο πάνω σε σκηνικό με αντηρίδα από πίσω μένει ακίνητο.'


if __name__ == '__main__':
    run(S)
