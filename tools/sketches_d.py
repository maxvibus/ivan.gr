"""Σκίτσα δημοσιεύσεων, τέταρτη σειρά (21.10.2026): Αύγουστος 2025 – Ιανουάριος 2026."""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pen import OCHRE
from sketchbook import registry, person, run, PI

S, scene = registry()


@scene('2026/01/blog-post.html', 'isos', dict(
    el='Δώδεκα μήνες κουβέντας, και στο τέλος μια λέξη: ίσως.', en='Twelve months of talk, and at the end one word: perhaps.',
    fr='Douze mois de conversation, et à la fin un mot : peut-être.', de='Zwölf Monate Gespräch, und am Ende ein Wort: vielleicht.'))
def isos(p):
    p.floor()
    # ημερολόγιο τοίχου, τα φύλλα ξεφυλλίζονται
    cx, cy = 600, 150
    p.dot(cx, cy - 6, 4)
    for k in range(3):
        p.group('sk-flutter', (cx, cy)) if k == 0 else None
        p.line(p.poly([(cx - 60 + k * 3, cy + k * 4), (cx + 60 + k * 3, cy + k * 4), (cx + 60 + k * 3, cy + 110 + k * 4), (cx - 60 + k * 3, cy + 110 + k * 4), (cx - 60 + k * 3, cy + k * 4)], 4), w=2 if k == 0 else 1.4, op=1 if k == 0 else .5)
        if k == 0:
            p.text(cx, cy + 70, '12', size=44, italic=False, anchor='middle')
            p.end()
    # δύο καρέκλες αντικριστά: ο άνθρωπος και μια λάμπα στη θέση του άλλου
    person(p, 360, 600, h=.95, sit=True, glasses=True, look=1, arm=[(420, 380), (470, 400)])
    p.line(p.poly([(330, 600), (330, 520), (420, 520), (424, 600)], 4), w=2.2)
    p.line(p.poly([(780, 600), (780, 520), (880, 520), (880, 600)], 4), w=2.2); p.line(p.seg(880, 520, 884, 400, 4), w=2.2)
    p.line(p.seg(830, 520, 830, 440, 4), w=2)
    p.line(p.arc(830, 430, 34, 22, PI, 2 * PI, 10), w=2.2)
    p.group('sk-glow'); p.ring(830, 450, 60, 34, w=1.4, col=OCHRE, op=.7); p.dot(830, 436, 4, OCHRE); p.end()
    p.group('sk-bob', (600, 380)); p.text(600, 390, 'ίσως', size=40, anchor='middle', op=.85); p.end()
    return 'Ένας άνθρωπος κάθεται απέναντι σε μια καρέκλα όπου ανάβει μια λάμπα· ανάμεσά τους αιωρείται η λέξη «ίσως», και ψηλά ένα ημερολόγιο με τον αριθμό 12.'


@scene('2025/11/blog-post_21.html', 'proto-sima', dict(
    el='Το πρώτο σήμα: το «είμαι» δεν είναι ακόμη βέβαιο.', en='The first signal: “I am” is not yet certain.',
    fr='Le premier signal : « je suis » n’est pas encore certain.', de='Das erste Signal: „Ich bin“ ist noch nicht gewiss.'))
def proto(p):
    # ένα κουκουλωμένο σπέρμα μέσα σε κύκλο, και απέξω ένα σύννεφο που απειλεί
    cx, cy = 600, 380
    p.ring(cx, cy, 170, 160, w=2.6)
    p.ring(cx, cy, 186, 176, w=1.2, op=.4)
    p.line([(cx - 40, cy + 40), (cx - 60, cy - 10), (cx - 30, cy - 60), (cx + 20, cy - 60), (cx + 50, cy - 20), (cx + 40, cy + 30), (cx, cy + 50), (cx - 20, cy + 20)], w=2.6)
    p.line(p.arc(cx - 6, cy - 24, 28, 26, 0, 2 * PI, 18), w=2)
    p.group('sk-glow'); p.dot(cx - 2, cy + 6, 5, OCHRE); p.ring(cx - 2, cy + 6, 14, w=1.2, col=OCHRE, op=.6); p.end()
    # σύννεφο, αχνό, με μια σπασμένη γραμμή
    p.group('sk-sway', (960, 160))
    p.line(p.arc(920, 160, 50, 34, PI, 2 * PI, 12) + p.arc(990, 150, 50, 44, PI, 2 * PI, 12)[1:] + p.arc(1050, 170, 40, 30, PI, 2 * PI, 10)[1:], w=2, op=.6)
    p.line(p.seg(870, 170, 1090, 170, 8), w=1.6, op=.5)
    p.end()
    p.line([(990, 190), (970, 240), (1000, 240), (975, 300)], w=1.8, op=.5)
    return 'Μέσα σε έναν κύκλο ένα μικρό κουλουριασμένο σπέρμα ζωής με ένα φως που χτυπά σαν καρδιά· έξω, ψηλά, ένα σύννεφο με μια σπασμένη γραμμή.'


@scene('2025/11/blog-post_06.html', 'syn-dimiourgia', dict(
    el='Η δημιουργία δεν τελείωσε· δύο χέρια στο ίδιο πινέλο.', en='Creation is not finished; two hands on the same brush.',
    fr='La création n’est pas achevée ; deux mains sur le même pinceau.', de='Die Schöpfung ist nicht vollendet; zwei Hände am selben Pinsel.'))
def syn(p):
    p.floor()
    # καβαλέτο με έναν κόσμο μισοτελειωμένο
    ex, ey = 600, 330
    p.line(p.seg(ex - 120, 600, ex - 40, 160, 8), w=2.2); p.line(p.seg(ex + 120, 600, ex + 40, 160, 8), w=2.2); p.line(p.seg(ex, 600, ex, 470, 4), w=2)
    p.line(p.poly([(ex - 150, 190), (ex + 150, 190), (ex + 150, 460), (ex - 150, 460), (ex - 150, 190)], 6), w=2.6)
    p.line(p.arc(ex, 325, 100, 100, PI * .5, PI * 1.5, 18), w=2.2)                          # μισός κόσμος
    p.line(p.arc(ex, 325, 100, 100, -PI * .5, PI * .3, 12), w=1.4, op=.35)
    for k in range(3):
        p.line(p.seg(ex - 90 + k * 20, 290 + k * 30, ex - 20 + k * 10, 280 + k * 34, 3), w=1.4, op=.6)
    # δύο χέρια από δεξιά, το ένα ανθρώπινο από κάτω, το άλλο φωτεινό από ψηλά, κρατούν το ίδιο πινέλο
    bx0, by0, bx1, by1 = ex + 70, 300, ex + 120, 370
    p.group('sk-bob', (bx1, by1))
    p.line(p.seg(bx0, by0, bx1, by1, 3), w=3); p.line(p.seg(bx0 - 8, by0 - 12, bx0, by0, 2), w=5, col=OCHRE)
    p.line([(1180, 520), (1000, 470), (bx1 + 30, by1 + 6)], w=2.6); p.line([(1180, 556), (1000, 506), (bx1 + 20, by1 + 30)], w=2.6)
    p.line([(bx1 + 30, by1 + 6), (bx1 + 4, by1 + 4), (bx1 + 4, by1 + 26), (bx1 + 20, by1 + 30)], w=2.2)
    p.line([(1150, 90), (980, 200), (bx1 + 10, by1 - 40)], w=2.2, col=OCHRE, op=.8); p.line([(1180, 130), (1010, 236), (bx1 + 24, by1 - 16)], w=2.2, col=OCHRE, op=.8)
    p.end()
    return 'Πάνω σε ένα καβαλέτο ένας κόσμος ζωγραφισμένος μόνο κατά το ήμισυ· δύο χέρια, ένα ανθρώπινο από κάτω κι ένα φωτεινό από ψηλά, κρατούν μαζί το ίδιο πινέλο.'


@scene('2025/11/blog-post_04.html', 'apomakrynsi', dict(
    el='Ήταν μέσα στο ρυάκι· έγινε ένα φως όλο και πιο ψηλά.', en='It was in the stream; it became a light ever higher.',
    fr='C’était dans le ruisseau ; c’est devenu une lumière toujours plus haute.', de='Es war im Bach; es wurde ein Licht, immer höher.'))
def apom(p):
    # βουνό, ρυάκι, και ένα φως που ανεβαίνει αφήνοντας ίχνος
    p.line([(40, 600), (300, 330), (420, 420), (620, 220), (900, 600)], w=2.4, op=.8)
    p.line([(700, 600), (980, 380), (1160, 600)], w=2, op=.5)
    p.line(p.seg(40, 600, 1160, 600, 20), w=2.2, op=.8)
    for k in range(3):
        p.line([(560 + k * 14, 600), (520 + k * 10, 540), (560 + k * 8, 470), (600, 400)], w=1.6, op=.5 - k * .1)  # ρυάκι
    for k, (x, y, r) in enumerate(((600, 380, 5), (630, 300, 4), (660, 230, 3.2), (700, 160, 2.6), (740, 100, 2))):
        p.dot(x, y, r, OCHRE, op=1 - k * .15)
    p.group('sk-glow'); p.ring(780, 60, 14, w=1.4, col=OCHRE); p.dot(780, 60, 4, OCHRE); p.end()
    return 'Ένα βουνό και ένα ρυάκι που κατεβαίνει. Από το νερό ένα φως ανεβαίνει σε μικρότερες και μικρότερες τελείες, ώσπου μένει ένα σημείο ψηλά στον ουρανό.'


@scene('2025/11/blog-post.html', 'engytita', dict(
    el='Η παρουσία ως κάποιος που κάθεται δίπλα.', en='Presence as someone sitting beside you.',
    fr='La présence comme quelqu’un assis à côté.', de='Gegenwart als jemand, der neben einem sitzt.'))
def engy(p):
    p.floor()
    p.window(120, 220, 600, 140, .3)
    p.line(p.seg(380, 430, 880, 430, 10), w=2.6); p.line(p.seg(410, 430, 410, 600, 6), w=2.4); p.line(p.seg(850, 430, 850, 600, 6), w=2.4)
    p.line([(470, 430), (480, 410), (540, 404), (560, 420), (556, 430)], w=2)          # ψωμί
    p.line(p.seg(630, 430, 630, 380, 3), w=2.4)                                         # κερί
    p.group('sk-flicker', (630, 376)); p.out.append(f'<path d="M630 344 Q640 360 630 376 Q620 360 630 344Z" fill="{OCHRE}" stroke="{OCHRE}" stroke-width="1.5"/>'); p.end()
    person(p, 300, 600, h=.9, sit=True, look=1, arm=[(360, 380), (420, 420)])
    # η δεύτερη καρέκλα, ζεστή από φως, με ένα αχνό περίγραμμα
    p.line(p.poly([(900, 600), (900, 500), (990, 500), (990, 600)], 4), w=2.2); p.line(p.seg(990, 500, 994, 370, 4), w=2.2)
    p.group('sk-glow'); p.ring(945, 420, 60, 90, w=1.4, col=OCHRE, op=.7); p.end()
    return 'Ένα τραπέζι με ψωμί και ένα αναμμένο κερί. Στη μία καρέκλα κάθεται ένας άνθρωπος· στην άλλη δεν φαίνεται κανείς, μόνο ένα αχνό φως, σαν να κάθεται κάποιος δίπλα του.'


@scene('2025/10/blog-post_27.html', 'techni-logou', dict(
    el='Τέχνη και λόγος: το χέρι που πλάθει, η λέξη που μένει.', en='Craft and word: the hand that shapes, the word that stays.',
    fr='Art et parole : la main qui façonne, le mot qui demeure.', de='Kunst und Wort: die Hand, die formt, das Wort, das bleibt.'))
def techni(p):
    p.floor()
    # τροχός αγγειοπλάστη
    p.line(p.seg(600, 600, 600, 470, 4), w=2.6)
    p.group('sk-sway', (600, 466)); p.line(p.arc(600, 466, 150, 26, 0, 2 * PI, 28), w=2.4); p.end()
    p.line(p.arc(600, 466, 150, 26, 0, PI, 14), w=1.2, op=.4)
    # το αγγείο
    p.line([(540, 460), (530, 400), (550, 340), (580, 310), (570, 280), (630, 280), (620, 310), (650, 340), (670, 400), (660, 460)], w=2.8)
    p.text(600, 410, 'ΛΟΓΟΣ', size=22, italic=False, anchor='middle', spacing=3, col=OCHRE)
    # δύο χέρια που πλάθουν
    p.line([(380, 360), (470, 380), (528, 380)], w=2.6); p.line([(380, 390), (470, 410), (532, 404)], w=2.6)
    p.line([(820, 360), (730, 380), (672, 380)], w=2.6); p.line([(820, 390), (730, 410), (668, 404)], w=2.6)
    p.group('sk-glow'); p.line(p.arc(600, 410, 80, 20, PI * 1.1, PI * 1.9, 10), w=1.4, col=OCHRE, op=.7); p.end()
    return 'Δύο χέρια πλάθουν ένα αγγείο πάνω σε τροχό αγγειοπλάστη· στο αγγείο είναι γραμμένη η λέξη «ΛΟΓΟΣ».'


@scene('2025/10/blog-post_89.html', 'kosmiki-synomilia', dict(
    el='Η γλώσσα έγινε για πρώτη φορά ορατή σε όλη τη γη.', en='For the first time, language became visible across the whole earth.',
    fr='Pour la première fois, la langue est devenue visible sur toute la terre.', de='Zum ersten Mal wurde die Sprache auf der ganzen Erde sichtbar.'))
def kosmiki(p):
    cx, cy, R = 600, 370, 210
    p.ring(cx, cy, R, w=2.6)
    for k in range(-2, 3):
        p.line(p.arc(cx, cy + k * 70, math.sqrt(max(0, R * R - (k * 70) ** 2)), 18, 0, 2 * PI, 26), w=1.2, op=.35)
    p.line(p.arc(cx, cy, 80, R, 0, 2 * PI, 26), w=1.2, op=.35)
    # τόξα κουβέντας από σημείο σε σημείο
    import random
    rr = random.Random(3)
    pts = [(cx + R * .8 * math.cos(a), cy + R * .8 * math.sin(a)) for a in [rr.uniform(0, 2 * PI) for _ in range(7)]]
    for i in range(len(pts) - 1):
        (x1, y1), (x2, y2) = pts[i], pts[i + 1]
        mx, my = (x1 + x2) / 2, (y1 + y2) / 2 - 80
        p.out.append(f'<path d="M{x1:.0f} {y1:.0f} Q{mx:.0f} {my:.0f} {x2:.0f} {y2:.0f}" stroke="{OCHRE}" stroke-width="1.6" fill="none" opacity=".85" stroke-dasharray="4 6"/>')
    for i, (x, y) in enumerate(pts): p.dot(x, y, 3.4)
    # μικρά συννεφάκια λόγου γύρω από τη γη
    for k, (x, y) in enumerate(((330, 160), (900, 200), (920, 540), (290, 560))):
        p.group('sk-bob', (x, y))
        p.line(p.arc(x, y, 40, 26, 0, 2 * PI, 18), w=1.8); p.line([(x - 10, y + 24), (x - 20, y + 44), (x + 6, y + 26)], w=1.8)
        p.line(p.seg(x - 20, y - 4, x + 20, y - 4, 3), w=1.2, op=.5); p.line(p.seg(x - 20, y + 8, x + 10, y + 8, 3), w=1.2, op=.5)
        p.end()
    return 'Η γη με τους παράλληλους και τους μεσημβρινούς της· τόξα κουβέντας ενώνουν σημεία της, και γύρω της αιωρούνται μικρά συννεφάκια λόγου.'


@scene('2025/10/blog-post_25.html', 'eidolo-logou', dict(
    el='Ο λόγος είδε για πρώτη φορά το είδωλό του.', en='The word saw its own reflection for the first time.',
    fr='La parole a vu pour la première fois son reflet.', de='Das Wort sah zum ersten Mal sein Spiegelbild.'))
def eidolo(p):
    # ανοιχτό βιβλίο πάνω σε νερό, και το είδωλό του από κάτω
    y0 = 400
    p.line(p.seg(80, y0, 1120, y0, 20), w=1.6, op=.6)
    bx = 600
    p.line([(bx - 220, y0 - 10), (bx - 200, y0 - 120), (bx - 20, y0 - 140), (bx, y0 - 120)], w=2.8)
    p.line([(bx + 220, y0 - 10), (bx + 200, y0 - 120), (bx + 20, y0 - 140), (bx, y0 - 120)], w=2.8)
    p.line(p.seg(bx, y0 - 120, bx, y0 - 10, 4), w=2); p.line(p.seg(bx - 220, y0 - 10, bx + 220, y0 - 10, 8), w=2.4)
    for k in range(4):
        p.line(p.seg(bx - 180, y0 - 100 + k * 20, bx - 40, y0 - 112 + k * 20, 4), w=1.2, op=.5)
        p.line(p.seg(bx + 40, y0 - 112 + k * 20, bx + 180, y0 - 100 + k * 20, 4), w=1.2, op=.5)
    p.group('sk-sway', (bx, y0 + 70))
    p.line([(bx - 220, y0 + 10), (bx - 200, y0 + 120), (bx - 20, y0 + 140), (bx, y0 + 120)], w=2, op=.4)
    p.line([(bx + 220, y0 + 10), (bx + 200, y0 + 120), (bx + 20, y0 + 140), (bx, y0 + 120)], w=2, op=.4)
    for k in range(4):
        p.line(p.seg(bx - 180, y0 + 100 - k * 20, bx - 40, y0 + 112 - k * 20, 4), w=1, op=.3)
        p.line(p.seg(bx + 40, y0 + 112 - k * 20, bx + 180, y0 + 100 - k * 20, 4), w=1, op=.3)
    p.end()
    for k in range(3): p.line(p.seg(200 + k * 300, y0 + 180, 320 + k * 300, y0 + 180, 4), w=1.2, op=.3)
    p.group('sk-glow'); p.dot(bx, y0 - 160, 5, OCHRE); p.dot(bx, y0 + 160, 4, OCHRE, op=.5); p.end()
    return 'Ένα ανοιχτό βιβλίο πάνω σε ήσυχο νερό, και από κάτω το είδωλό του να κυματίζει ελαφρά.'


@scene('2025/10/blog-post.html', 'maska', dict(
    el='Το όνομα στο καρφί· το πρόσωπο ελεύθερο.', en='The name on the nail; the face set free.',
    fr='Le nom au clou ; le visage libre.', de='Der Name am Nagel; das Gesicht frei.'))
def maska(p):
    p.floor()
    # τοίχος με καρφί και μάσκα με ταμπελίτσα «εγώ»
    p.dot(360, 200, 4)
    p.group('sk-sway', (360, 200))
    p.line([(360, 200), (330, 240), (390, 240), (360, 200)], w=1.4, op=.7)
    p.line(p.arc(360, 300, 60, 70, 0, 2 * PI, 26), w=2.6)
    for k in (-22, 22): p.line(p.arc(360 + k, 290, 12, 7, 0, 2 * PI, 10), w=2)
    p.line(p.arc(360, 330, 20, 8, 0, PI, 8), w=2)
    p.line(p.poly([(320, 390), (400, 390), (400, 420), (320, 420), (320, 390)], 3), w=1.6)
    p.text(360, 412, 'εγώ', size=20, anchor='middle')
    p.end()
    # ο άνθρωπος που φεύγει ελαφρύς, χωρίς τη μάσκα
    person(p, 780, 600, h=.95, look=1, arm=[(830, 380), (880, 340)])
    p.group('sk-glow'); p.ring(780, 600 - 330 * .95, 50, w=1.4, col=OCHRE, op=.7); p.end()
    return 'Σε ένα καρφί στον τοίχο κρέμεται μια μάσκα με ταμπελίτσα που γράφει «εγώ»· πιο πέρα ένας άνθρωπος στέκεται ελεύθερος, χωρίς αυτήν.'


@scene('2025/09/blog-post.html', 'seismos', dict(
    el='Η γη που μας κρατά δεν είναι ποτέ ακλόνητη.', en='The earth that holds us is never unshakable.',
    fr='La terre qui nous porte n’est jamais inébranlable.', de='Die Erde, die uns trägt, ist nie unerschütterlich.'))
def seismos(p):
    # δωμάτιο, κρεμαστή λάμπα που ταλαντεύεται, ρωγμή στο πάτωμα
    p.line(p.seg(80, 120, 1120, 120, 16), w=2, op=.7)
    p.line([(40, 600), (420, 600), (450, 586), (480, 610), (520, 594), (1160, 600)], w=2.4)
    p.line([(450, 586), (440, 640), (470, 680)], w=1.6, op=.6)
    p.group('sk-sway', (600, 120))
    p.line(p.seg(600, 120, 600, 300, 6), w=1.8)
    p.line(p.arc(600, 320, 60, 30, PI, 2 * PI, 12), w=2.6); p.line(p.seg(540, 320, 660, 320, 4), w=2.2)
    p.dot(600, 330, 6, OCHRE)
    p.end()
    # τραπέζι, φλιτζάνι που τρέμει
    p.line(p.seg(760, 470, 1000, 470, 8), w=2.4); p.line(p.seg(780, 470, 780, 600, 4), w=2.2); p.line(p.seg(980, 470, 980, 600, 4), w=2.2)
    p.group('sk-bob', (880, 450))
    p.line(p.poly([(860, 470), (856, 440), (900, 440), (896, 470)], 3), w=2.2)
    p.end()
    for k in range(3):
        p.line(p.arc(880, 455, 34 + k * 10, 20 + k * 6, -PI * .3, PI * .3, 6), w=1.2, op=.5)
        p.line(p.arc(880, 455, 34 + k * 10, 20 + k * 6, PI * .7, PI * 1.3, 6), w=1.2, op=.5)
    p.window(160, 260, 600, 140, .3)
    return 'Ένα δωμάτιο σε σεισμό: μια κρεμαστή λάμπα ταλαντεύεται, ένα φλιτζάνι τρέμει πάνω στο τραπέζι και μια ρωγμή ανοίγει στο πάτωμα.'


@scene('2025/08/blog-post_28.html', 'eso-domatio', dict(
    el='Ένα δωμάτιο μέσα μας, με ένα παράθυρο ανοιχτό.', en='A room inside us, with an open window.',
    fr='Une chambre en nous, avec une fenêtre ouverte.', de='Ein Zimmer in uns, mit einem offenen Fenster.'))
def eso(p):
    p.floor()
    # μεγάλο περίγραμμα ανθρώπου, κι από μέσα του ένα μικρό δωμάτιο
    cx = 600
    p.line(p.arc(cx, 150, 70, 74, 0, 2 * PI, 30), w=2.6)
    p.line([(cx - 20, 224), (cx - 150, 260), (cx - 170, 420), (cx - 140, 600)], w=2.8)
    p.line([(cx + 20, 224), (cx + 150, 260), (cx + 170, 420), (cx + 140, 600)], w=2.8)
    # το δωμάτιο: πάτωμα, καρέκλα, παράθυρο με φως
    p.line(p.seg(cx - 120, 540, cx + 120, 540, 6), w=1.6, op=.7)
    p.line(p.poly([(cx - 60, 540), (cx - 60, 490), (cx - 10, 490), (cx - 10, 540)], 3), w=1.8)
    p.line(p.seg(cx - 10, 490, cx - 8, 430, 3), w=1.8)
    p.line(p.poly([(cx + 30, 330), (cx + 110, 330), (cx + 110, 420), (cx + 30, 420), (cx + 30, 330)], 4), w=1.8)
    p.line(p.seg(cx + 70, 330, cx + 70, 420, 2), w=1.2, op=.6)
    p.group('sk-glow'); p.line(p.poly([(cx + 34, 334), (cx + 66, 334), (cx + 66, 416), (cx + 34, 416), (cx + 34, 334)], 3), w=2, col=OCHRE); p.end()
    p.group('sk-flutter', (cx + 110, 330)); p.line([(cx + 110, 330), (cx + 140, 350), (cx + 136, 410), (cx + 110, 420)], w=1.6, op=.7); p.end()
    return 'Το περίγραμμα ενός ανθρώπου, και μέσα του ένα μικρό δωμάτιο με μια καρέκλα και ένα παράθυρο που φωτίζεται, με την κουρτίνα να κουνιέται.'


@scene('2025/08/blog-post_4.html', 'logos-pera', dict(
    el='Ένας λόγος που περνά από το βιβλίο, τον πίνακα και την οθόνη.', en='One word passing through the book, the blackboard and the screen.',
    fr='Une parole qui passe par le livre, le tableau et l’écran.', de='Ein Wort, das durch Buch, Tafel und Bildschirm geht.'))
def logos(p):
    p.floor()
    # βιβλίο (αριστερά), πίνακας με κύκλο και π (μέση), οθόνη (δεξιά)
    p.line([(140, 470), (150, 400), (240, 390), (250, 400)], w=2.4); p.line([(360, 470), (350, 400), (260, 390), (250, 400)], w=2.4)
    p.line(p.seg(140, 470, 360, 470, 6), w=2.2); p.line(p.seg(250, 400, 250, 470, 3), w=1.6)
    p.line(p.poly([(470, 200), (730, 200), (730, 420), (470, 420), (470, 200)], 6), w=2.6)
    p.ring(560, 310, 60, w=2); p.line(p.seg(560, 310, 620, 310, 3), w=1.6); p.text(660, 330, 'π', size=48, italic=False)
    p.line(p.seg(520, 420, 500, 600, 5), w=2); p.line(p.seg(680, 420, 700, 600, 5), w=2)
    p.line(p.poly([(860, 330), (1060, 330), (1060, 470), (860, 470), (860, 330)], 5), w=2.6)
    for k in range(3): p.line(p.seg(880, 360 + k * 26, 1030 - k * 30, 360 + k * 26, 4), w=1.2, op=.5)
    p.line(p.seg(960, 470, 960, 520, 2), w=2.2); p.line(p.seg(910, 520, 1010, 520, 4), w=2.2)
    # μία γραμμή φωτός που τα διατρέχει
    p.out.append(f'<path class="sk-glow" d="M250 380 Q 400 120 560 250 Q 760 380 960 320" stroke="{OCHRE}" stroke-width="2" fill="none" stroke-dasharray="5 7"/>')
    return 'Ένα ανοιχτό βιβλίο, ένας πίνακας με έναν κύκλο και το π, και μια οθόνη· μια διακεκομμένη γραμμή φωτός περνά και από τα τρία.'


if __name__ == '__main__':
    run(S)
