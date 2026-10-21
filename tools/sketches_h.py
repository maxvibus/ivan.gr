"""Σκίτσα δημοσιεύσεων, όγδοη σειρά (21.10.2026): Μάρτιος 2025, γ΄ μέρος."""
import math, os, sys, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pen import OCHRE
from sketchbook import registry, person, run, PI

S, scene = registry()


@scene('2025/03/blog-post_59.html', 'alma', dict(
    el='Ένα πέρασμα σε κάτι που δεν υπήρχε πριν.', en='A crossing into something that did not exist before.',
    fr='Un passage vers quelque chose qui n’existait pas avant.', de='Ein Übergang in etwas, das es vorher nicht gab.'))
def alma(p):
    p.line([(40, 460), (420, 460), (430, 700)], w=2.6); p.line([(780, 700), (790, 420), (1160, 420)], w=2.6)
    for k in range(3): p.line(p.seg(460 + k * 100, 700, 480 + k * 100, 620, 3), w=1, op=.3)
    p.group('sk-bob', (600, 280))
    x, y = 600, 300
    p.line(p.arc(x, y - 60, 22, 24, 0, 2 * PI, 16), w=2.4)
    p.line([(x - 4, y - 36), (x - 10, y + 10), (x - 40, y + 40)], w=2.4); p.line([(x - 10, y + 10), (x + 30, y + 30), (x + 60, y + 20)], w=2.4)
    p.line([(x - 2, y - 26), (x - 40, y - 50)], w=2.2); p.line([(x - 2, y - 26), (x + 40, y - 60)], w=2.2)
    p.end()
    p.out.append(f'<path d="M400 450 Q 600 160 800 410" stroke="{OCHRE}" stroke-width="1.8" fill="none" stroke-dasharray="5 8"/>')
    return 'Ένας άνθρωπος στον αέρα πηδά από τον έναν γκρεμό στον άλλον, ψηλότερο· μια διακεκομμένη γραμμή σε ώχρα δείχνει την τροχιά του.'


@scene('2025/03/blog-post_89.html', 'tomi-synexeia', dict(
    el='Η τομή δείχνει τη συνέχεια.', en='The cut reveals the continuity.',
    fr='La coupure révèle la continuité.', de='Der Schnitt zeigt die Kontinuität.'))
def tomi(p):
    p.line([(60, 400), (300, 380), (520, 390)], w=3); p.line([(680, 390), (900, 400), (1140, 380)], w=3)
    for x in (520, 680):
        p.line(p.seg(x, 370, x, 410, 2), w=1.6)
    p.group('sk-glow'); p.out.append(f'<path d="M520 390 Q 600 330 680 390" stroke="{OCHRE}" stroke-width="2" fill="none" stroke-dasharray="3 6"/>'); p.dot(600, 360, 5, OCHRE); p.end()
    p.line(p.seg(60, 500, 1140, 500, 20), w=1.2, op=.3)
    return 'Μια γραμμή που κόβεται στη μέση· στο κενό ανάμεσα στα δύο κομμάτια ένα φωτεινό τόξο τα ενώνει.'


@scene('2025/03/blog-post_12.html', 'kormos-tomi', dict(
    el='Στην τομή του κορμού φαίνονται όλα τα χρόνια.', en='In the cut of the trunk all the years appear.',
    fr='Dans la coupe du tronc apparaissent toutes les années.', de='Im Schnitt des Stammes zeigen sich alle Jahre.'))
def kormos(p):
    p.floor()
    cx, cy = 600, 420
    p.line([(cx - 170, 600), (cx - 160, cy)], w=2.6); p.line([(cx + 170, 600), (cx + 160, cy)], w=2.6)
    for k in range(9):
        r = 160 - k * 17
        p.line(p.arc(cx, cy, r, r * .3, 0, 2 * PI, 30), w=1.6 if k else 2.6, op=1 if k in (0,) else .55,
               col=OCHRE if k == 1 else 'currentColor')
    p.line(p.seg(cx, cy, cx + 120, cy - 20, 4), w=1.2, op=.5)
    p.group('sk-sway', (cx + 230, 600)); p.line([(cx + 230, 600), (cx + 226, 520), (cx + 240, 480)], w=2); p.line([(cx + 226, 530), (cx + 200, 510), (cx + 196, 524), (cx + 226, 530)], w=1.8); p.end()
    return 'Ένα κομμένο κούτσουρο από ψηλά, με τους δακτυλίους των χρόνων του· ένας δακτύλιος λάμπει, και δίπλα φυτρώνει ένα νέο βλαστάρι.'


@scene('2025/03/blog-post_84.html', 'zygaria', dict(
    el='Τα αποσιωπητικά βαραίνουν περισσότερο από την απάντηση.', en='The ellipsis weighs more than the answer.',
    fr='Les points de suspension pèsent plus que la réponse.', de='Die Auslassungspunkte wiegen mehr als die Antwort.'))
def zyg(p):
    p.floor()
    p.line(p.seg(600, 600, 600, 180, 8), w=2.6); p.line(p.seg(540, 600, 660, 600, 3), w=2.6)
    p.group('sk-sway', (600, 180))
    p.line(p.seg(360, 130, 840, 230, 10), w=2.6)
    for x, y, txt, big in ((360, 130, 'απάντηση', True), (840, 230, '…', False)):
        p.line([(x - 70, y + 120), (x, y), (x + 70, y + 120)], w=1.4, op=.7)
        p.line(p.arc(x, y + 120, 90, 18, 0, PI, 12), w=2.4)
        if big:
            p.line(p.arc(x, y + 80, 76, 34, 0, 2 * PI, 20), w=1.8, op=.7); p.text(x, y + 88, txt, size=20, anchor='middle', op=.7)
        else:
            p.text(x, y + 112, txt, size=60, italic=False, anchor='middle', col=OCHRE)
    p.end()
    return 'Μια ζυγαριά: στη μία πλάστιγγα ένα μεγάλο συννεφάκι που γράφει «απάντηση», στην άλλη μόνο τρεις τελείες, και γέρνει προς τις τελείες.'


@scene('2025/03/blog-post_58.html', 'speira', dict(
    el='Γυρνώντας στα ίδια βήματα, σε άλλο σημείο.', en='Returning on the same steps, to a different place.',
    fr='Revenir sur les mêmes pas, à un autre endroit.', de='Auf denselben Schritten zurück, an einen anderen Ort.'))
def speira(p):
    cx, cy = 600, 380
    for t in range(0, 70):
        a = t * .32; r = 30 + t * 3.2
        x, y = cx + r * math.cos(a), cy + r * .55 * math.sin(a)
        if t % 2 == 0: p.out.append(f'<ellipse cx="{x:.0f}" cy="{y:.0f}" rx="7" ry="3.5" fill="currentColor" opacity="{.15 + t / 120:.2f}" transform="rotate({math.degrees(a) + 90:.0f} {x:.0f} {y:.0f})"/>')
    p.group('sk-glow'); p.dot(cx, cy, 6, OCHRE); p.end()
    person(p, 960, 560, h=.6, look=-1)
    return 'Ίχνη βημάτων σε σπείρα που ξεκινά από ένα φωτεινό κέντρο και ανοίγει προς τα έξω, ως έναν άνθρωπο που στέκεται στην άκρη της.'


@scene('2025/03/blog-post_76.html', 'arnaki', dict(
    el='Ένας τίτλος θυμωμένος, κι ένα αρνάκι που χαμογελά.', en='An angry headline, and a lamb that smiles.',
    fr='Un titre en colère, et un agneau qui sourit.', de='Eine wütende Schlagzeile, und ein Lamm, das lächelt.'))
def arnaki(p):
    p.floor()
    p.line(p.poly([(120, 160), (520, 170), (516, 560), (116, 550), (120, 160)], 6), w=2.4)
    p.text(318, 240, 'Η ΟΡΓΗ', size=44, italic=False, anchor='middle', spacing=2)
    p.text(318, 296, 'ΤΩΝ ΑΜΝΩΝ', size=40, italic=False, anchor='middle', spacing=2)
    for k in range(6): p.line(p.seg(150, 340 + k * 30, 480, 340 + k * 30, 6), w=1.2, op=.4)
    ax, ay = 820, 470
    for k in range(10):
        a = k * 2 * PI / 10; p.line(p.arc(ax + 70 * math.cos(a), ay + 40 * math.sin(a), 28, 22, 0, 2 * PI, 12), w=1.8)
    for lx in (ax - 50, ax - 20, ax + 30, ax + 60): p.line(p.seg(lx, ay + 40, lx, 600, 3), w=2.4)
    p.group('sk-tilt', (ax - 80, ay - 20))
    p.line(p.arc(ax - 110, ay - 30, 36, 30, 0, 2 * PI, 18), w=2.4)
    p.line([(ax - 136, ay - 52), (ax - 160, ay - 40), (ax - 140, ay - 30)], w=2)
    p.dot(ax - 120, ay - 36, 3.4); p.line(p.arc(ax - 112, ay - 18, 10, 6, 0, PI, 6), w=1.8)
    p.end()
    p.group('sk-glow'); p.ring(ax, ay, 120, 80, w=1.2, col=OCHRE, op=.6); p.end()
    return 'Αριστερά μια εφημερίδα με τίτλο «Η ΟΡΓΗ ΤΩΝ ΑΜΝΩΝ»· δεξιά ένα αρνάκι από μπουκλίτσες που γέρνει το κεφάλι και χαμογελά.'


@scene('2025/03/blog-post_0.html', 'fos-enochlei', dict(
    el='Το φως ενοχλεί όσους είχαν συνηθίσει το σκοτάδι.', en='Light disturbs those used to the dark.',
    fr='La lumière dérange ceux qui s’étaient habitués à l’obscurité.', de='Licht stört die, die an das Dunkel gewöhnt waren.'))
def fos(p):
    p.floor()
    person(p, 600, 600, h=.95, look=0, arm=[(640, 330), (680, 290)])
    p.line(p.seg(680, 290, 680, 260, 2), w=1.6); p.line(p.poly([(664, 260), (696, 260), (692, 304), (668, 304), (664, 260)], 2), w=2)
    p.group('sk-glow'); p.dot(680, 282, 6, OCHRE); p.ring(680, 282, 70, w=1.2, col=OCHRE, op=.5); p.end()
    for x, side in ((300, 1), (900, -1)):
        person(p, x, 600, h=.85, look=side, arm=[(x + 30 * side, 330), (x + 10 * side, 300)])
        p.line([(x - 6, 300), (x + 34 * side, 296)], w=2.4)
    return 'Ένας άνθρωπος στη μέση κρατά ένα φανάρι· δύο άλλοι δεξιά κι αριστερά σκιάζουν τα μάτια τους με το χέρι.'


@scene('2025/03/blog-post_11.html', 'diaplasi', dict(
    el='Ο χώρος όπου η καρδιά παίρνει σχήμα.', en='The place where the heart takes shape.',
    fr='Le lieu où le cœur prend forme.', de='Der Ort, an dem das Herz Gestalt annimmt.'))
def diapl(p):
    p.floor()
    tx = 820
    p.line([(tx - 30, 600), (tx - 24, 340)], w=2.6); p.line([(tx + 30, 600), (tx + 26, 340)], w=2.6)
    p.group('sk-sway', (tx, 340)); p.line(p.arc(tx, 260, 170, 110, 0, 2 * PI, 30), w=2.2); p.end()
    x = 620
    person(p, x, 600, h=.6, sit=True, look=1, arm=[(x + 40, 470), (x + 70, 470)])
    p.line(p.poly([(x + 50, 480), (x + 110, 470), (x + 114, 500), (x + 54, 510), (x + 50, 480)], 3), w=2)
    p.group('sk-glow'); p.line([(x + 82, 452), (x + 74, 440), (x + 82, 434), (x + 90, 440), (x + 82, 452)], w=2, col=OCHRE); p.end()
    return 'Ένα παιδί κάθεται κάτω από ένα δέντρο και διαβάζει ένα περιοδικό· πάνω από τις σελίδες αιωρείται μια μικρή καρδιά.'


@scene('2025/03/blog-post_24.html', 'porta-sxoleiou', dict(
    el='Το σχολείο έκλεισε την πόρτα· ο δρόμος έμεινε ανοιχτός.', en='The school closed its door; the road stayed open.',
    fr='L’école a fermé sa porte ; la route est restée ouverte.', de='Die Schule schloss ihre Tür; der Weg blieb offen.'))
def porta(p):
    p.floor()
    p.line(p.poly([(160, 600), (160, 200), (460, 200), (460, 600)], 8), w=2.4)
    for k in range(6): p.line(p.seg(180 + k * 50, 600, 180 + k * 50, 230, 8), w=1.8)
    p.line(p.seg(160, 230, 460, 230, 6), w=2)
    p.text(310, 180, 'ΣΧΟΛΕΙΟ', size=24, italic=False, anchor='middle', spacing=3, op=.8)
    p.line([(560, 600), (760, 560), (1160, 520)], w=1.6, op=.5); p.line([(560, 640), (800, 620), (1160, 600)], w=1.6, op=.5)
    person(p, 740, 590, h=.6, look=1)
    p.group('sk-bob', (960, 220)); p.line([(930, 220), (950, 206), (966, 216)], w=2.2); p.line([(966, 216), (984, 202), (1004, 212)], w=2.2); p.end()
    p.group('sk-glow'); p.ring(1060, 140, 30, w=2, col=OCHRE); p.end()
    return 'Μια κλειστή καγκελόπορτα σχολείου· έξω ένα παιδί περπατά σε έναν δρόμο που ανοίγεται, κάτω από ένα πουλί και τον ήλιο.'


@scene('2025/03/blog-post_54.html', 'katharsi', dict(
    el='Το νερό καθαρίζει όταν το αφήσεις να ησυχάσει.', en='Water clears when you let it settle.',
    fr='L’eau s’éclaircit quand on la laisse se reposer.', de='Wasser klärt sich, wenn man es zur Ruhe kommen lässt.'))
def kath(p):
    p.line(p.seg(300, 560, 900, 560, 10), w=2.4)
    p.line([(500, 560), (480, 220)], w=2.6); p.line([(700, 560), (720, 220)], w=2.6); p.line(p.arc(600, 220, 120, 16, 0, 2 * PI, 20), w=2)
    p.line(p.arc(600, 280, 112, 12, 0, PI, 14), w=1.4, op=.6)
    rr = random.Random(6)
    for k in range(14):
        x = rr.uniform(510, 690); y = rr.uniform(300, 520)
        p.group('sk-bob', (x, y)); p.dot(x, y, 2 + rr.random() * 2, op=.3 + (y - 300) / 400); p.end()
    p.line(p.arc(600, 540, 96, 10, 0, PI, 12), w=1.6, op=.6)
    p.group('sk-glow'); p.line(p.seg(520, 300, 680, 300, 6), w=1.6, col=OCHRE, op=.8); p.end()
    return 'Ένα ψηλό ποτήρι με νερό· τα σωματίδια κατακάθονται αργά στον πάτο και πάνω το νερό φωτίζεται καθαρό.'


@scene('2025/03/blog-post_17.html', 'afesi-ptisi', dict(
    el='Την αφήνεις, και πετά.', en='You let it go, and it flies.',
    fr='Tu la laisses, et elle s’envole.', de='Man lässt es los, und es fliegt.'))
def afesi(p):
    p.line([(160, 640), (380, 520), (520, 470)], w=2.6); p.line([(160, 680), (400, 560), (540, 500)], w=2.6)
    for fx, L in ((-30, 50), (-10, 66), (10, 64), (30, 52)):
        p.line([(560 + fx - 8, 480), (560 + fx - 10, 480 - L + 10), (560 + fx + 4, 480 - L), (560 + fx + 12, 480 - L + 10), (560 + fx + 8, 480)], w=2)
    p.group('sk-bob', (760, 260))
    p.line([(700, 280), (740, 240), (770, 262), (810, 220), (840, 250)], w=2.6, col=OCHRE)
    p.line(p.arc(770, 270, 26, 12, 0, 2 * PI, 14), w=2, col=OCHRE)
    p.end()
    for k in range(3): p.line(p.arc(700 - k * 30, 330 + k * 30, 20, 20, -PI * .2, PI * .3, 5), w=1.4, op=.5)
    return 'Ένα ανοιχτό χέρι μόλις άφησε ένα πουλί, που ανοίγει τα φτερά του και ανεβαίνει.'


@scene('2025/03/blog-post_94.html', 'roi-fragi', dict(
    el='Η γλώσσα ως ποτάμι, όχι ως φράγμα.', en='Language as a river, not a dam.',
    fr='La langue comme une rivière, non comme un barrage.', de='Sprache als Fluss, nicht als Damm.'))
def roi(p):
    p.line(p.poly([(520, 620), (530, 240), (680, 240), (690, 620)], 6), w=2.8)
    for k in range(5): p.line(p.seg(540, 280 + k * 66, 670, 280 + k * 66, 4), w=1.2, op=.5)
    p.text(605, 220, 'ΦΡΑΓΗ', size=22, italic=False, anchor='middle', spacing=3, op=.7)
    for k in range(4):
        y = 300 + k * 60
        p.group('sk-sway' if k % 2 else 'sk-bob', (600, y))
        p.line([(40, y), (300, y + 10), (480, y - 40), (600, y - 160 + k * 10), (720, y - 40), (900, y + 10), (1160, y)], w=1.8, col=OCHRE if k == 1 else 'currentColor', op=.8)
        p.end()
    return 'Ένα τείχος με την επιγραφή «ΦΡΑΓΗ» στέκεται στη μέση· το νερό δεν σταματά, περνά από πάνω και γύρω του και συνεχίζει να κυλά.'


@scene('2025/03/blog-post_5.html', 'onoma', dict(
    el='Όταν σε φωνάζουν με το όνομά σου, έρχεσαι.', en='When you are called by name, you come.',
    fr='Quand on t’appelle par ton nom, tu viens.', de='Wenn man dich beim Namen ruft, kommst du.'))
def onoma(p):
    p.floor()
    person(p, 320, 600, h=.95, look=1, arm=[(360, 330), (400, 300)])
    p.line(p.arc(560, 220, 90, 46, 0, 2 * PI, 22), w=2); p.line([(480, 246), (430, 280), (500, 260)], w=2)
    p.text(560, 232, '«…»', size=32, anchor='middle', col=OCHRE)
    p.group('sk-tilt', (900, 400)); person(p, 900, 600, h=.62, look=-1); p.end()
    p.group('sk-glow'); p.ring(900, 600 - 330 * .62, 40, w=1.4, col=OCHRE, op=.7); p.end()
    return 'Ένας άνθρωπος φωνάζει κάποιον με το όνομά του, και πιο πέρα ένα παιδί γυρίζει προς αυτόν.'


@scene('2025/03/blog-post_88.html', 'tritos-dromos', dict(
    el='Δύο δρόμοι φαίνονται· ο τρίτος ήταν κρυμμένος στη μέση.', en='Two roads are visible; the third was hidden in the middle.',
    fr='Deux chemins sont visibles ; le troisième était caché au milieu.', de='Zwei Wege sind sichtbar; der dritte war in der Mitte verborgen.'))
def tritos(p):
    p.line([(560, 700), (560, 520), (300, 160)], w=2.4); p.line([(640, 700), (640, 520), (900, 160)], w=2.4)
    p.line([(520, 700), (520, 520), (220, 180)], w=1.6, op=.5); p.line([(680, 700), (680, 520), (980, 180)], w=1.6, op=.5)
    p.out.append(f'<path class="sk-glow" d="M590 700 L596 520 L600 160" stroke="{OCHRE}" stroke-width="2" fill="none" stroke-dasharray="4 8"/>')
    p.group('sk-glow'); p.dot(600, 150, 6, OCHRE); p.end()
    for x in (300, 900):
        p.line(p.seg(x, 160, x, 100, 3), w=2); p.line(p.poly([(x - 40, 100), (x + 40, 100), (x + 40, 70), (x - 40, 70), (x - 40, 100)], 3), w=2)
    return 'Ένα σταυροδρόμι με δύο φανερούς δρόμους προς τα αριστερά και τα δεξιά· στη μέση ξεκινά ένα τρίτο, αχνό, φωτεινό μονοπάτι.'


@scene('2025/03/blog-post_47.html', 'milia-milia', dict(
    el='Μιλιά και μηλιά: λέξεις που θυμούνται η μία την άλλη.', en='Speech and apple tree: words that remember each other.',
    fr='Parole et pommier : des mots qui se souviennent l’un de l’autre.', de='Rede und Apfelbaum: Wörter, die einander erinnern.'))
def milia(p):
    p.floor()
    tx = 520
    p.line([(tx - 30, 600), (tx - 24, 360), (tx - 40, 270)], w=2.8); p.line([(tx + 30, 600), (tx + 26, 360), (tx + 44, 270)], w=2.8)
    p.group('sk-sway', (tx, 270)); p.line(p.arc(tx, 200, 200, 120, 0, 2 * PI, 32), w=2.2)
    for k in range(5): p.ring(tx - 140 + k * 70, 200 + (k % 2) * 40, 11, w=1.8, col=OCHRE if k == 2 else 'currentColor', op=.7)
    p.end()
    p.line(p.arc(900, 220, 150, 70, 0, 2 * PI, 26), w=2.2); p.line([(790, 262), (730, 300), (800, 280)], w=2.2)
    p.text(900, 210, 'μιλιά · μηλιά', size=28, anchor='middle'); p.text(900, 250, 'μήλα · μιλά', size=24, anchor='middle', op=.7)
    return 'Μια μηλιά, και δίπλα της ένα συννεφάκι λόγου που γράφει «μιλιά · μηλιά» και «μήλα · μιλά».'


@scene('2025/03/blog-post_85.html', 'koino-trapezi', dict(
    el='Δύο σπίτια διαφορετικά, ένα τραπέζι ανάμεσα.', en='Two different houses, one table between them.',
    fr='Deux maisons différentes, une table entre elles.', de='Zwei verschiedene Häuser, ein Tisch dazwischen.'))
def koino(p):
    p.floor()
    p.line(p.poly([(100, 600), (100, 360), (320, 360), (320, 600)], 6), w=2.4)                   # κυκλαδίτικο
    p.line(p.arc(210, 360, 60, 50, PI, 2 * PI, 12), w=2.2); p.line(p.poly([(180, 600), (180, 480), (240, 480), (240, 600)], 3), w=2)
    p.line(p.poly([(880, 600), (880, 400), (1100, 400), (1100, 600)], 6), w=2.4)                 # με κεραμιδένια στέγη που ανασηκώνεται
    p.line([(850, 400), (900, 330), (990, 300), (1080, 330), (1130, 400)], w=2.4); p.line([(870, 330), (990, 250), (1110, 330)], w=2.2)
    p.line(p.seg(470, 480, 730, 480, 8), w=2.6); p.line(p.seg(500, 480, 500, 600, 4), w=2.2); p.line(p.seg(700, 480, 700, 600, 4), w=2.2)
    p.line(p.poly([(560, 480), (556, 450), (590, 450), (586, 480)], 3), w=2); p.line(p.poly([(620, 480), (616, 450), (650, 450), (646, 480)], 3), w=2)
    p.steam(573, 440, 1); p.steam(633, 440, 1)
    p.group('sk-glow'); p.ring(600, 470, 150, 40, w=1.2, col=OCHRE, op=.6); p.end()
    return 'Αριστερά ένα κυκλαδίτικο σπίτι με τρούλο, δεξιά ένα σπίτι με ανασηκωμένη ανατολίτικη στέγη· ανάμεσά τους ένα τραπέζι με δύο φλιτζάνια που αχνίζουν.'


@scene('2025/03/blog-post_7.html', 'meteoros', dict(
    el='Μετέωρος, και γελάει.', en='Suspended, and laughing.',
    fr='Suspendu, et il rit.', de='In der Schwebe, und er lacht.'))
def meteor(p):
    p.line(p.seg(300, 80, 900, 80, 12), w=2.4)
    p.group('sk-sway', (600, 80))
    p.line(p.seg(520, 80, 540, 440, 8), w=1.8); p.line(p.seg(680, 80, 660, 440, 8), w=1.8)
    p.line(p.seg(520, 440, 680, 440, 4), w=3)
    x = 600
    p.line(p.arc(x, 330, 30, 32, 0, 2 * PI, 18), w=2.6)
    p.line(p.arc(x, 340, 16, 10, 0, PI, 8), w=2); p.line(p.arc(x - 10, 324, 6, 3, PI, 2 * PI, 4), w=1.6); p.line(p.arc(x + 10, 324, 6, 3, PI, 2 * PI, 4), w=1.6)
    p.line([(x - 10, 362), (x - 16, 438)], w=2.4); p.line([(x + 10, 362), (x + 16, 438)], w=2.4)
    p.line([(x - 16, 440), (x - 40, 500), (x - 30, 540)], w=2.4); p.line([(x + 16, 440), (x + 50, 500), (x + 60, 530)], w=2.4)
    p.line([(x - 14, 380), (540, 300)], w=2.2); p.line([(x + 14, 380), (660, 300)], w=2.2)
    p.end()
    p.group('sk-bob', (760, 300)); p.text(760, 300, 'χα', size=30, col=OCHRE); p.text(800, 260, 'χα', size=24, col=OCHRE, op=.7); p.end()
    p.line(p.seg(40, 660, 1160, 660, 20), w=1.4, op=.4)
    return 'Ένας άνθρωπος σε κούνια ψηλά από το έδαφος γελάει δυνατά, με τα πόδια στον αέρα.'


@scene('2025/03/blog-post_63.html', 'roi-plasi', dict(
    el='Η ροή που πλάθει την κοιλάδα.', en='The flow that shapes the valley.',
    fr='Le flux qui façonne la vallée.', de='Der Fluss, der das Tal formt.'))
def plasi(p):
    p.line([(40, 200), (300, 260), (480, 420), (560, 600)], w=2.4); p.line([(1160, 180), (900, 250), (720, 420), (640, 600)], w=2.4)
    p.line([(40, 320), (260, 360), (420, 470)], w=1.4, op=.4); p.line([(1160, 300), (940, 350), (780, 470)], w=1.4, op=.4)
    for k in range(3):
        p.group('sk-sway' if k % 2 else 'sk-bob', (600, 500))
        p.line([(560 + k * 12, 600), (590 + k * 8, 520), (580 + k * 10, 440), (610, 340), (600, 240)], w=1.8, col=OCHRE if k == 1 else 'currentColor', op=.75)
        p.end()
    return 'Μια κοιλάδα σε σχήμα V ανάμεσα σε δύο πλαγιές, και στον πάτο της ένα ποτάμι που την έχει σκάψει και συνεχίζει να κυλά.'


@scene('2025/03/blog-post_80.html', 'distagmos', dict(
    el='Ένα βήμα πίσω μπροστά σε κάτι ανείπωτα ωραίο.', en='A step back before something unspeakably beautiful.',
    fr='Un pas en arrière devant quelque chose d’indiciblement beau.', de='Ein Schritt zurück vor etwas unsagbar Schönem.'))
def dist(p):
    p.line(p.seg(40, 520, 1160, 520, 22), w=1.4, op=.6)
    p.group('sk-glow'); p.line(p.arc(840, 520, 150, 150, PI, 2 * PI, 24), w=2.6, col=OCHRE)
    for k in range(9): a = PI + k * PI / 8; p.line(p.seg(840 + 180 * math.cos(a), 520 + 180 * math.sin(a), 840 + 230 * math.cos(a), 520 + 230 * math.sin(a), 2), w=1.8, col=OCHRE, op=.7)
    p.end()
    person(p, 380, 600, h=.95, look=1, arm=[(420, 330), (440, 300)])
    p.line([(312, 600), (290, 610)], w=2.4)
    p.line(p.seg(40, 600, 1160, 600, 20), w=2.2, op=.8)
    return 'Ένας ήλιος ανατέλλει πάνω από τη θάλασσα· ένας άνθρωπος μπροστά του κάνει ένα μικρό βήμα πίσω, με το χέρι μισοσηκωμένο.'


if __name__ == '__main__':
    run(S)
