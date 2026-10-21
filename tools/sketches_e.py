"""Σκίτσα δημοσιεύσεων, πέμπτη σειρά (21.10.2026): Μάιος – Αύγουστος 2025."""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pen import OCHRE
from sketchbook import registry, person, run, PI

S, scene = registry()


def hand(p, x, y, s=1, col='currentColor', op=1):
    """Ανοιχτή παλάμη με πέντε δάχτυλα, όρθια."""
    p.line(p.arc(x, y + 20 * s, 34 * s, 40 * s, -PI * .05, PI * 1.05, 16), w=2.2, col=col, op=op)
    for fx, L in ((-26, 50), (-9, 64), (8, 62), (24, 48)):
        p.line([(x + (fx - 7) * s, y + 6 * s), (x + (fx - 8) * s, y - (L - 8) * s), (x + fx * s, y - L * s), (x + (fx + 8) * s, y - (L - 8) * s), (x + (fx + 7) * s, y + 6 * s)], w=1.9, col=col, op=op)
    p.line([(x + 32 * s, y + 28 * s), (x + 60 * s, y + 6 * s), (x + 68 * s, y + 16 * s), (x + 38 * s, y + 46 * s)], w=1.9, col=col, op=op)


@scene('2025/08/blog-post_24.html', 'apotypoma', dict(
    el='Το ίδιο αποτύπωμα χεριού: στη σπηλιά και στην οθόνη.', en='The same handprint: in the cave and on the screen.',
    fr='La même empreinte de main : dans la grotte et sur l’écran.', de='Derselbe Handabdruck: in der Höhle und auf dem Bildschirm.'))
def apot(p):
    p.floor()
    p.line([(60, 600), (80, 300), (180, 160), (420, 120), (520, 200), (540, 600)], w=2.4, op=.7)    # σπηλιά
    hand(p, 300, 360, 1.1, op=.75)
    p.line(p.poly([(720, 230), (1080, 230), (1080, 470), (720, 470), (720, 230)], 6), w=2.6)        # οθόνη
    p.line(p.seg(900, 470, 900, 530, 2), w=2.2); p.line(p.seg(840, 530, 960, 530, 4), w=2.2)
    p.group('sk-glow'); hand(p, 900, 350, .9, col=OCHRE); p.end()
    return 'Αριστερά ένα αποτύπωμα χεριού στον τοίχο μιας σπηλιάς· δεξιά το ίδιο αποτύπωμα λάμπει πάνω σε μια οθόνη.'


@scene('2025/08/blog-post.html', 'xari', dict(
    el='Η ομπρέλα άνοιξε πριν πέσει η πρώτη σταγόνα.', en='The umbrella opened before the first drop fell.',
    fr='Le parapluie s’est ouvert avant la première goutte.', de='Der Schirm ging auf, bevor der erste Tropfen fiel.'))
def xari(p):
    p.floor()
    person(p, 520, 600, h=.95, look=-1)
    person(p, 700, 600, h=.95, look=-1, arm=[(760, 330), (720, 210)])
    p.line(p.seg(720, 210, 712, 120, 4), w=2.2)
    p.line(p.arc(640, 130, 170, 80, PI, 2 * PI, 22), w=2.6, col=OCHRE)
    for k in range(5): p.line([(470 + k * 68, 130), (504 + k * 68, 150), (538 + k * 68, 130)], w=1.6, col=OCHRE, op=.7)
    for k, (x, y) in enumerate(((300, 80), (980, 110), (360, 200), (1040, 260))):
        p.group('sk-bob', (x, y)); p.line([(x, y), (x - 6, y + 16), (x, y + 22), (x + 6, y + 16), (x, y)], w=1.6, op=.6); p.end()
    return 'Δύο άνθρωποι στέκονται δίπλα δίπλα· ο ένας έχει ήδη ανοίξει ομπρέλα πάνω και από τους δύο, ενώ οι πρώτες σταγόνες μόλις αρχίζουν να πέφτουν γύρω τους.'


@scene('2025/07/bits.html', 'plaketa', dict(
    el='Στη γεωμετρία του κυκλώματος, ένα φως στο κέντρο.', en='In the geometry of the circuit, a light at the centre.',
    fr='Dans la géométrie du circuit, une lumière au centre.', de='In der Geometrie des Schaltkreises ein Licht in der Mitte.'))
def plak(p):
    cx, cy = 600, 360
    p.line(p.poly([(cx - 110, cy - 110), (cx + 110, cy - 110), (cx + 110, cy + 110), (cx - 110, cy + 110), (cx - 110, cy - 110)], 6), w=2.8)
    for k in range(6):
        o = -90 + k * 36
        for sgn in (-1, 1):
            p.line([(cx + o, cy + sgn * 110), (cx + o, cy + sgn * 150), (cx + o * 2.2, cy + sgn * 210), (cx + o * 2.2, cy + sgn * 300)], w=1.6, op=.6)
            p.line([(cx + sgn * 110, cy + o), (cx + sgn * 150, cy + o), (cx + sgn * 260, cy + o * 1.6), (cx + sgn * 480, cy + o * 1.6)], w=1.6, op=.6)
            p.dot(cx + sgn * 480, cy + o * 1.6, 3.4)
    p.line(p.poly([(cx - 70, cy - 70), (cx + 70, cy - 70), (cx + 70, cy + 70), (cx - 70, cy + 70), (cx - 70, cy - 70)], 4), w=1.4, op=.5)
    p.group('sk-glow'); p.dot(cx, cy, 9, OCHRE); p.ring(cx, cy, 28, w=1.4, col=OCHRE, op=.7); p.end()
    return 'Ένα τσιπ πάνω σε πλακέτα, με τους αγωγούς του να απλώνονται συμμετρικά προς όλες τις μεριές· στο κέντρο του ένα μικρό φως.'


@scene('2025/07/blog-post_15.html', 'paideia-filoxenia', dict(
    el='Ένα θρανίο αλλιώτικο, και η θέση του έτοιμη.', en='A different desk, and its place ready.',
    fr='Un pupitre différent, et sa place prête.', de='Ein anderes Pult, und sein Platz bereit.'))
def paid(p):
    p.floor()
    p.line(p.poly([(420, 120), (780, 120), (780, 260), (420, 260), (420, 120)], 6), w=2.4)    # πίνακας
    p.text(600, 205, 'καλώς ήρθες', size=34, anchor='middle', op=.85)
    for k, x in enumerate((180, 380, 820, 1020)):
        p.line(p.poly([(x - 60, 470), (x + 60, 470)], 4), w=2.4); p.line(p.seg(x - 50, 470, x - 50, 600, 4), w=2.2); p.line(p.seg(x + 50, 470, x + 50, 600, 4), w=2.2)
    # το στρογγυλό θρανίο στη μέση, με φως
    p.line(p.arc(600, 470, 70, 18, 0, 2 * PI, 22), w=2.4); p.line(p.seg(600, 488, 600, 600, 4), w=2.4); p.line(p.seg(560, 600, 640, 600, 3), w=2.2)
    p.group('sk-glow'); p.line(p.arc(600, 470, 96, 34, 0, 2 * PI, 22), w=1.4, col=OCHRE, op=.8); p.end()
    p.group('sk-sway', (600, 452)); p.line([(590, 452), (594, 420), (606, 410)], w=1.6); p.ring(608, 404, 8, w=1.6, col=OCHRE); p.end()
    return 'Μια τάξη με τετράγωνα θρανία· στη μέση, ανάμεσά τους, ένα στρογγυλό θρανίο με ένα λουλουδάκι, και στον πίνακα γράφει «καλώς ήρθες».'


@scene('2025/07/blog-post_76.html', 'synkatoikisi', dict(
    el='Δύο οδοντόβουρτσες σε ένα ποτήρι.', en='Two toothbrushes in one glass.',
    fr='Deux brosses à dents dans un verre.', de='Zwei Zahnbürsten in einem Glas.'))
def synk(p):
    p.line(p.seg(200, 470, 1000, 470, 14), w=2.4)                                             # ράφι
    p.line(p.poly([(260, 120), (560, 120), (560, 400), (260, 400), (260, 120)], 6), w=2, op=.5)   # καθρέφτης
    gx = 640
    p.line(p.poly([(gx - 40, 470), (gx - 46, 360), (gx + 46, 360), (gx + 40, 470)], 4), w=2.4)
    p.group('sk-sway', (gx, 380)); p.line(p.seg(gx - 14, 420, gx - 40, 250, 6), w=3); p.line(p.seg(gx - 40, 250, gx - 46, 214, 2), w=6, op=.6); p.end()
    p.group('sk-sway', (gx, 380)); p.line(p.seg(gx + 14, 420, gx + 44, 256, 6), w=3, col=OCHRE); p.line(p.seg(gx + 44, 256, gx + 50, 220, 2), w=6, col=OCHRE, op=.6); p.end()
    p.line(p.poly([(820, 470), (814, 420), (870, 420), (864, 470)], 3), w=2); p.line(p.arc(876, 446, 10, 12, -PI / 2, PI / 2, 6), w=2)
    p.steam(842, 410, 2)
    return 'Σε ένα ράφι μπάνιου, ένα ποτήρι με δύο οδοντόβουρτσες που γέρνουν η μία προς την άλλη, και δίπλα ένα φλιτζάνι που αχνίζει.'


@scene('2025/07/blog-post_12.html', 'kopsimo-psomiou', dict(
    el='Η φανέρωση είναι το κόψιμο του ψωμιού, όχι το ψωμί.', en='Revelation is the breaking of the bread, not the bread.',
    fr='La révélation, c’est la fraction du pain, non le pain.', de='Offenbarung ist das Brechen des Brotes, nicht das Brot.'))
def psomi(p):
    p.line(p.seg(160, 520, 1040, 520, 14), w=2.4)
    p.line([(470, 360), (420, 380), (410, 440), (440, 470), (560, 470), (590, 430)], w=2.6)      # μισό
    p.line([(730, 360), (780, 380), (790, 440), (760, 470), (640, 470), (612, 430)], w=2.6)
    p.line([(590, 430), (596, 400), (586, 380)], w=2, op=.8); p.line([(612, 430), (606, 400), (616, 380)], w=2, op=.8)
    p.line([(250, 420), (380, 400), (440, 392)], w=2.6); p.line([(250, 450), (380, 430), (420, 440)], w=2.6)
    p.line([(950, 420), (820, 400), (760, 392)], w=2.6); p.line([(950, 450), (820, 430), (780, 440)], w=2.6)
    for k, (x, y) in enumerate(((598, 470), (606, 490), (594, 505))):
        p.group('sk-bob', (x, y)); p.dot(x, y, 3, OCHRE); p.end()
    p.group('sk-glow'); p.ring(600, 420, 40, 60, w=1.2, col=OCHRE, op=.7); p.end()
    return 'Δύο χέρια μοιράζουν ένα καρβέλι στη μέση· ανάμεσα στα δύο κομμάτια πέφτουν ψίχουλα, και εκεί, στο σπάσιμο, ένα φως.'


@scene('2025/07/blog-post_75.html', 'nomos-roygmi', dict(
    el='Ο νόμος στην πινακίδα· το λουλούδι στη ρωγμή.', en='The law on the sign; the flower in the crack.',
    fr='La loi sur le panneau ; la fleur dans la fissure.', de='Das Gesetz auf dem Schild; die Blume im Riss.'))
def nomos(p):
    p.floor()
    for k in range(6): p.line(p.seg(80 + k * 190, 600, 140 + k * 190, 640, 2), w=1.2, op=.4)
    p.line(p.seg(380, 600, 380, 300, 6), w=2.6)
    p.line(p.poly([(260, 180), (500, 180), (500, 300), (260, 300), (260, 180)], 5), w=2.6)
    p.text(380, 230, 'ΑΠΑΓΟΡΕΥΕΤΑΙ', size=26, italic=False, anchor='middle', spacing=2)
    p.text(380, 270, 'η ανάπτυξη', size=22, anchor='middle', op=.75)
    p.line([(700, 600), (716, 580), (708, 560), (730, 540), (724, 520)], w=1.6)                 # ρωγμή
    p.group('sk-sway', (720, 600))
    p.line([(720, 600), (716, 520), (726, 460)], w=2.2)
    p.line([(716, 540), (690, 520), (680, 530), (716, 540)], w=1.8)
    for k in range(5):
        a = k * 2 * PI / 5; p.line(p.arc(726 + 18 * math.cos(a), 450 + 18 * math.sin(a), 12, 10, 0, 2 * PI, 10), w=1.8, col=OCHRE)
    p.dot(726, 450, 5, OCHRE)
    p.end()
    return 'Μια πινακίδα γράφει «ΑΠΑΓΟΡΕΥΕΤΑΙ η ανάπτυξη»· λίγο πιο πέρα ένα λουλούδι φυτρώνει μέσα από μια ρωγμή στο πεζοδρόμιο.'


@scene('2025/07/blog-post_74.html', 'dipla', dict(
    el='Μαθαίνει κανείς δίπλα σε κάποιον, όχι απέναντι.', en='One learns beside someone, not across from them.',
    fr='On apprend à côté de quelqu’un, pas en face.', de='Man lernt neben jemandem, nicht ihm gegenüber.'))
def dipla(p):
    p.floor()
    p.line(p.seg(330, 470, 870, 470, 10), w=2.6); p.line(p.seg(360, 470, 360, 600, 5), w=2.4); p.line(p.seg(840, 470, 840, 600, 5), w=2.4)
    p.line(p.seg(330, 380, 870, 380, 10), w=2, op=.7); p.line(p.seg(350, 380, 350, 470, 3), w=2, op=.7); p.line(p.seg(850, 380, 850, 470, 3), w=2, op=.7)
    person(p, 480, 600, h=.75, sit=True, look=1, glasses=True)
    person(p, 650, 600, h=.62, sit=True, look=1)
    p.group('sk-bob', (940, 180)); p.line([(910, 180), (930, 166), (946, 176)], w=2.2); p.line([(946, 176), (964, 162), (984, 172)], w=2.2); p.end()
    p.group('sk-glow'); p.ring(980, 120, 26, w=1.6, col=OCHRE); p.end()
    return 'Ένας μεγάλος κι ένας μικρός κάθονται δίπλα δίπλα σε ένα παγκάκι και κοιτάζουν προς την ίδια μεριά, εκεί που περνά ένα πουλί.'


@scene('2025/07/blog-post_67.html', 'allos-mesa', dict(
    el='Ο άλλος μπήκε μέσα μας πριν τον καλέσουμε.', en='The other entered us before we called.',
    fr='L’autre est entré en nous avant que nous l’appelions.', de='Der andere trat in uns ein, bevor wir ihn riefen.'))
def allos(p):
    cx, cy = 560, 330
    p.line(p.arc(cx, cy, 190, 200, -PI * .55, PI * 1.25, 36), w=2.8)                            # κεφάλι σε προφίλ
    p.line([(cx + 120, cy - 150), (cx + 180, cy - 60), (cx + 214, cy + 10), (cx + 186, cy + 30), (cx + 196, cy + 80), (cx + 170, cy + 140), (cx + 110, cy + 180)], w=2.8)
    p.line([(cx - 60, cy + 196), (cx - 40, 600)], w=2.6); p.line([(cx + 100, cy + 186), (cx + 90, 600)], w=2.6)
    p.floor()
    # μέσα στο κεφάλι, ένας μικρός άλλος
    p.group('sk-glow')
    x, fy, s = 540, 430, .45
    p.line(p.arc(x, fy - 150, 16, 17, 0, 2 * PI, 14), w=2, col=OCHRE)
    p.line([(x - 4, fy - 132), (x - 20, fy - 60), (x - 16, fy)], w=2, col=OCHRE); p.line([(x + 6, fy - 132), (x + 20, fy - 60), (x + 18, fy)], w=2, col=OCHRE)
    p.line([(x + 10, fy - 110), (x + 50, fy - 130)], w=2, col=OCHRE)
    p.end()
    p.line(p.seg(470, 430, 620, 430, 4), w=1.2, op=.4)
    return 'Ένα μεγάλο κεφάλι σε προφίλ· μέσα του στέκεται ένας μικρός άλλος άνθρωπος, φωτεινός, με το χέρι σηκωμένο σαν να χαιρετά.'


@scene('2025/07/blog-post_7.html', 'skakiera', dict(
    el='Πάνω στη σκακιέρα, δύο χέρια που φυτεύουν μαζί.', en='On the chessboard, two hands planting together.',
    fr='Sur l’échiquier, deux mains qui plantent ensemble.', de='Auf dem Schachbrett zwei Hände, die zusammen pflanzen.'))
def skaki(p):
    # σκακιέρα σε προοπτική
    def P(u, v): return (600 + (u - 4) * (70 + v * 6), 360 + v * 30)
    for i in range(9):
        a, b = P(i, 0), P(i, 8); p.line(p.seg(a[0], a[1], b[0], b[1], 4), w=1.4, op=.6)
        c, d = P(0, i), P(8, i); p.line(p.seg(c[0], c[1], d[0], d[1], 6), w=1.4, op=.6)
    p.line([(600, 470), (600, 420)], w=2.4, col=OCHRE)                                         # βλαστάρι
    p.group('sk-sway', (600, 420)); p.line([(600, 430), (570, 404), (566, 416), (600, 430)], w=2, col=OCHRE); p.line([(600, 420), (630, 396), (634, 410), (600, 420)], w=2, col=OCHRE); p.end()
    p.line([(140, 520), (380, 490), (560, 470)], w=2.6); p.line([(140, 556), (380, 520), (566, 490)], w=2.6)
    p.line([(1060, 520), (820, 490), (640, 470)], w=2.6, op=.7); p.line([(1060, 556), (820, 520), (634, 490)], w=2.6, op=.7)
    p.line([(560, 470), (580, 486), (566, 490)], w=2); p.line([(640, 470), (620, 486), (634, 490)], w=2, op=.7)
    p.text(200, 260, '♜', size=56, italic=False, op=.25); p.text(980, 280, '♞', size=56, italic=False, op=.25)
    return 'Πάνω σε μια σκακιέρα, χωρίς πιόνια στη μάχη, δύο χέρια από αντίθετες πλευρές φυτεύουν μαζί ένα βλαστάρι· δυο πιόνια μένουν παραμερισμένα και αχνά.'


@scene('2025/07/blog-post.html', 'akrogoniaios', dict(
    el='Ο ακρογωνιαίος λίθος, και το κτίριο που έμεινε περίγραμμα.', en='The cornerstone, and the building that stayed an outline.',
    fr='La pierre angulaire, et le bâtiment resté contour.', de='Der Grundstein, und das Gebäude, das ein Umriss blieb.'))
def akrog(p):
    p.floor()
    p.out.append('<path d="M300 600 L300 260 L600 140 L900 260 L900 600" stroke="currentColor" stroke-width="1.6" fill="none" stroke-dasharray="6 10" opacity=".5"/>')
    for k in range(4): p.out.append(f'<path d="M{360 + k * 150} 600 L{360 + k * 150} 300" stroke="currentColor" stroke-width="1.4" fill="none" stroke-dasharray="6 10" opacity=".35"/>')
    p.line(p.poly([(300, 600), (300, 520), (440, 520), (440, 600)], 4), w=3)
    p.text(370, 568, '1828', size=26, italic=False, anchor='middle', spacing=2)
    p.group('sk-glow'); p.line(p.poly([(296, 516), (444, 516)], 4), w=2, col=OCHRE); p.end()
    p.line(p.seg(470, 600, 560, 590, 3), w=2.2); p.line(p.seg(560, 590, 590, 560, 2), w=4, op=.6)   # μυστρί
    return 'Ένας ακρογωνιαίος λίθος με τη χρονολογία 1828 στέκει στη θέση του· το κτίριο από πάνω του είναι μόνο ένα διακεκομμένο περίγραμμα.'


@scene('2025/07/invitation-is-not-invitation-on-opening.html', 'misanoixti', dict(
    el='Η πόρτα ήταν ήδη μισάνοιχτη.', en='The door was already ajar.',
    fr='La porte était déjà entrouverte.', de='Die Tür stand schon einen Spalt offen.'))
def misan(p):
    p.floor()
    dx = 520
    p.line(p.poly([(dx, 600), (dx, 170), (dx + 220, 170), (dx + 220, 600)], 8), w=3)
    p.group('sk-sway', (dx, 380))
    p.line(p.poly([(dx, 600), (dx, 170), (dx + 150, 200), (dx + 150, 580), (dx, 600)], 6), w=2.4)
    p.ring(dx + 130, 400, 8, w=2)
    p.end()
    p.out.append(f'<path class="sk-glow" d="M{dx + 150} 210 L{dx + 220} 172 L{dx + 220} 600 L{dx + 150} 580 L{dx + 320} 640 L{dx + 420} 640 Z" fill="{OCHRE}" opacity=".18" stroke="none"/>')
    p.line(p.seg(dx + 150, 600, dx + 420, 640, 6), w=1.6, col=OCHRE, op=.7)
    return 'Μια πόρτα στέκει μισάνοιχτη χωρίς να τη χτύπησε κανείς· από το άνοιγμα πέφτει μια λωρίδα φως στο πάτωμα.'


@scene('2025/06/blog-post_22.html', 'alysida', dict(
    el='Οι κρίκοι αλλάζουν νόμισμα, η αλυσίδα μένει.', en='The links change currency; the chain remains.',
    fr='Les maillons changent de monnaie, la chaîne demeure.', de='Die Glieder wechseln die Währung, die Kette bleibt.'))
def alys(p):
    p.floor()
    p.line(p.seg(120, 140, 120, 600, 8), w=2.6); p.line(p.seg(100, 140, 200, 140, 3), w=2.6)
    labels = ['1828', 'δρχ.', 'δρχ.', '€', '€']
    p.group('sk-sway', (130, 150))
    p.line([(120, 150), (150, 180), (170, 196)], w=2.4)
    for k, lab in enumerate(labels):
        x, y = 230 + k * 120, 230 + k * 64
        ang = math.atan2(64, 120)
        pts = [(x + 70 * math.cos(t) * math.cos(ang) - 32 * math.sin(t) * math.sin(ang), y + 70 * math.cos(t) * math.sin(ang) + 32 * math.sin(t) * math.cos(ang)) for t in [i * 2 * PI / 24 for i in range(25)]]
        p.line(pts, w=2.6, col=OCHRE if k == len(labels) - 1 else 'currentColor')
        p.text(x, y + 9, lab, size=22, italic=False, anchor='middle', op=.85)
        if k < len(labels) - 1:
            mx, my = x + 60, y + 32
            p.line(p.arc(mx, my, 10, 26, 0, 2 * PI, 14), w=2.4)
    p.end()
    return 'Μια αλυσίδα κρεμασμένη από ένα δοκάρι· οι κρίκοι της γράφουν διαδοχικά 1828, δραχμές και ευρώ, αλλά είναι η ίδια αλυσίδα.'


@scene('2025/06/blog-post_10.html', 'anamesa', dict(
    el='Η σκέψη συμβαίνει στο κενό ανάμεσα.', en='Thought happens in the gap between.',
    fr='La pensée a lieu dans l’intervalle.', de='Das Denken geschieht im Zwischenraum.'))
def anam(p):
    p.floor()
    person(p, 260, 600, h=.95, glasses=True, look=1)
    p.line(p.poly([(900, 300), (1080, 300), (1080, 430), (900, 430), (900, 300)], 5), w=2.6)
    p.line(p.seg(990, 430, 990, 600, 4), w=2.2); p.line(p.seg(930, 600, 1050, 600, 3), w=2.2)
    p.line(p.arc(430, 230, 70, 44, 0, 2 * PI, 20), w=2); p.line(p.arc(780, 250, 70, 44, 0, 2 * PI, 20), w=2)
    p.group('sk-glow'); p.line(p.arc(605, 320, 90, 70, 0, 2 * PI, 24), w=2.6, col=OCHRE); p.end()
    p.group('sk-bob', (605, 320)); p.dot(580, 320, 4, OCHRE); p.dot(605, 310, 4, OCHRE); p.dot(630, 320, 4, OCHRE); p.end()
    return 'Ένας άνθρωπος αριστερά και μια οθόνη δεξιά, ο καθένας με ένα συννεφάκι λόγου· ανάμεσά τους σχηματίζεται ένα τρίτο, φωτεινό, που δεν ανήκει σε κανέναν.'


@scene('2025/06/blog-post.html', 'tris-to-proi', dict(
    el='Μια κουβέντα που δεν ήταν σχεδιασμένη.', en='A conversation that was never planned.',
    fr='Une conversation qui n’était pas prévue.', de='Ein Gespräch, das nicht geplant war.'))
def tris(p):
    p.floor()
    p.window(840, 160, 480, 200, .35)
    p.line(p.arc(960, 110, 22, 22, PI * .35, PI * 1.65, 12), w=2)                                # φεγγάρι
    p.line(p.seg(220, 430, 700, 430, 10), w=2.6); p.line(p.seg(250, 430, 250, 600, 5), w=2.4); p.line(p.seg(670, 430, 670, 600, 5), w=2.4)
    p.line(p.poly([(470, 430), (500, 330), (640, 330), (620, 430)], 4), w=2.4)                     # φορητός
    person(p, 360, 600, h=.85, sit=True, glasses=True, look=1, arm=[(410, 400), (470, 420)])
    p.out.append(f'<path class="sk-glow" d="M505 340 L520 420 L392 412 L378 360 Z" fill="{OCHRE}" opacity=".18"/>')
    p.text(560, 300, '3:07', size=22, italic=False, anchor='middle', op=.6)
    return 'Νύχτα, ένας άνθρωπος με γυαλιά σκυμμένος σε έναν φορητό υπολογιστή που του φωτίζει το πρόσωπο· στο παράθυρο φεγγάρι, και η ώρα 3:07.'


@scene('2025/05/blog-post_30.html', 'afairesi', dict(
    el='Η μορφή φανερώνεται αφαιρώντας.', en='Form appears by taking away.',
    fr='La forme apparaît en retirant.', de='Die Gestalt erscheint durch Wegnehmen.'))
def afair(p):
    p.floor()
    p.line(p.poly([(520, 600), (500, 220), (700, 200), (720, 600)], 6), w=2.6)                   # ο όγκος της πέτρας
    p.line([(560, 600), (580, 480), (570, 400), (600, 330), (640, 400), (630, 480), (650, 600)], w=2.2, op=.8)   # η μορφή που βγαίνει
    p.ring(605, 300, 26, w=2, op=.8)
    p.line([(860, 300), (760, 340)], w=3); p.line([(760, 340), (730, 352)], w=5, op=.6)          # σμίλη
    p.line([(900, 260), (880, 320)], w=2.4); p.line(p.poly([(880, 240), (930, 250), (920, 280), (870, 270), (880, 240)], 3), w=2.4)  # σφυρί
    for k, (x, y) in enumerate(((720, 380), (760, 420), (740, 470), (790, 520))):
        p.group('sk-bob', (x, y)); p.line([(x, y), (x + 10, y - 6), (x + 14, y + 4), (x, y)], w=1.6, col=OCHRE if k == 1 else 'currentColor'); p.end()
    return 'Ένας όγκος πέτρας από τον οποίο αρχίζει να φανερώνεται μια ανθρώπινη μορφή· μια σμίλη και ένα σφυρί αφαιρούν, και θραύσματα πετιούνται.'


if __name__ == '__main__':
    run(S)
