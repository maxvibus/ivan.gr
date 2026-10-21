"""Σκίτσα δημοσιεύσεων, ένατη σειρά (21.10.2026): Φεβρουάριος – Μάρτιος 2025, τα πρώτα κείμενα."""
import math, os, sys, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pen import OCHRE
from sketchbook import registry, person, run, PI

S, scene = registry()


def C(el, en, fr, de): return dict(el=el, en=en, fr=fr, de=de)


@scene('2025/03/blog-post_22.html', 'dakry', C('Η ωραιότητα που δακρύζει.', 'Beauty that sheds a tear.', 'La beauté qui verse une larme.', 'Schönheit, die eine Träne vergießt.'))
def dakry(p):
    p.floor()
    p.line([(600, 600), (596, 420), (610, 300)], w=2.2)
    p.line([(598, 470), (550, 440), (540, 456), (598, 470)], w=1.8)
    for k in range(6):
        a = k * PI / 3 - PI / 2
        p.line(p.arc(610 + 46 * math.cos(a), 260 + 46 * math.sin(a), 32, 24, 0, 2 * PI, 14), w=2.2)
    p.ring(610, 260, 16, w=2, col=OCHRE)
    p.group('sk-bob', (664, 330)); p.line([(664, 314), (656, 334), (664, 342), (672, 334), (664, 314)], w=1.8, col=OCHRE); p.end()
    return 'Ένα λουλούδι με ανοιχτά πέταλα· από την άκρη ενός πετάλου κρέμεται μια σταγόνα σαν δάκρυ.'


@scene('2025/03/blog-post_14.html', 'pena-granazi', C('Πένα και γρανάζι, από το ίδιο χέρι.', 'Pen and gear, from the same hand.', 'Plume et engrenage, de la même main.', 'Feder und Zahnrad, aus derselben Hand.'))
def pena(p):
    cx, cy = 600, 360
    p.group('sk-sway', (cx, cy))
    p.ring(cx, cy, 120, w=2.6); p.ring(cx, cy, 40, w=2)
    for k in range(12): a = k * PI / 6; p.line(p.poly([(cx + 120 * math.cos(a - .1), cy + 120 * math.sin(a - .1)), (cx + 150 * math.cos(a - .08), cy + 150 * math.sin(a - .08)), (cx + 150 * math.cos(a + .08), cy + 150 * math.sin(a + .08)), (cx + 120 * math.cos(a + .1), cy + 120 * math.sin(a + .1))], 1), w=2.4)
    p.end()
    p.line([(cx, cy - 30), (cx - 24, cy + 40), (cx, cy + 90), (cx + 24, cy + 40), (cx, cy - 30)], w=2.4, col=OCHRE)
    p.line(p.seg(cx, cy + 10, cx, cy + 80, 2), w=1.6, col=OCHRE); p.dot(cx, cy + 10, 4, OCHRE)
    return 'Ένα γρανάζι, και στο κέντρο του, στη θέση του άξονα, η μύτη μιας πένας.'


@scene('2025/03/blog-post_69.html', 'ti-diavazo', C('Ο αναγνώστης που απορεί.', 'The reader who wonders.', 'Le lecteur qui s’étonne.', 'Der Leser, der sich wundert.'))
def tidiav(p):
    p.floor()
    person(p, 560, 600, h=1, sit=True, glasses=True, look=1, arm=[(620, 380), (680, 400)])
    p.line(p.poly([(530, 600), (530, 520), (640, 520), (640, 600)], 4), w=2.2)
    p.line([(660, 420), (670, 360), (760, 350), (770, 360)], w=2.4); p.line([(880, 420), (870, 360), (780, 350), (770, 360)], w=2.4); p.line(p.seg(660, 420, 880, 420, 6), w=2.2)
    p.line([(530, 290), (560, 280), (580, 286)], w=2); p.line([(600, 286), (620, 278), (650, 288)], w=2)   # σηκωμένα φρύδια
    for k, (x, y, sz) in enumerate(((720, 230, 50), (800, 180, 40), (660, 160, 34))):
        p.group('sk-bob', (x, y)); p.text(x, y, ';', size=sz, italic=False, col=OCHRE if k == 0 else 'currentColor', op=.8); p.end()
    return 'Ένας άνθρωπος με γυαλιά διαβάζει ένα βιβλίο με σηκωμένα φρύδια· γύρω του αιωρούνται ερωτηματικά.'


@scene('2025/03/blog-post_26.html', 'vivliothiki', C('Μια βιβλιοθήκη όπου όλα είναι γραμμένα.', 'A library where everything is written.', 'Une bibliothèque où tout est écrit.', 'Eine Bibliothek, in der alles geschrieben steht.'))
def vivl(p):
    for side in (-1, 1):
        for k in range(5):
            x0 = 600 + side * (520 - k * 90); x1 = 600 + side * (430 - k * 90)
            top0, bot0 = 80 + k * 50, 640 - k * 50; top1, bot1 = 130 + k * 50, 590 - k * 50
            p.line(p.seg(x0, top0, x0, bot0, 6), w=1.6, op=.6)
            for r in range(6):
                y0 = top0 + (bot0 - top0) * r / 6; y1 = top1 + (bot1 - top1) * r / 6
                p.line(p.seg(x0, y0, x1, y1, 3), w=1.2, op=.5)
                for b in range(3):
                    t = (b + .5) / 3; bx = x0 + (x1 - x0) * t; by = y0 + (y1 - y0) * t
                    p.line(p.seg(bx, by, bx, by - 22 * (1 - k * .12), 2), w=1.4, op=.5)
    p.group('sk-glow'); p.line(p.poly([(588, 360), (612, 360), (612, 320), (588, 320), (588, 360)], 2), w=2.4, col=OCHRE); p.ring(600, 340, 40, w=1.2, col=OCHRE, op=.6); p.end()
    return 'Ένας μακρύς διάδρομος βιβλιοθήκης σε προοπτική, με ράφια γεμάτα βιβλία ως το βάθος· στο κέντρο ένα βιβλίο φωτίζεται.'


@scene('2025/03/blog-post_2.html', 'pigaino-reo', C('Πηγαίνω, ρέω: το ίδιο ρήμα.', 'I go, I flow: the same verb.', 'Je vais, je coule : le même verbe.', 'Ich gehe, ich fließe: dasselbe Verb.'))
def pigaino(p):
    p.line([(40, 520), (400, 500), (800, 520), (1160, 500)], w=2, op=.7)
    for k in range(3):
        p.group('sk-sway' if k % 2 else 'sk-bob', (600, 560 + k * 26))
        p.line([(40, 560 + k * 26), (300, 550 + k * 26), (600, 566 + k * 26), (900, 552 + k * 26), (1160, 560 + k * 26)], w=1.6, col=OCHRE if k == 1 else 'currentColor', op=.7)
        p.end()
    person(p, 520, 500, h=.85, look=1)
    p.text(780, 300, 'ἰέναι', size=40, op=.7)
    return 'Ένας άνθρωπος περπατά στην όχθη ενός ποταμού προς την ίδια κατεύθυνση με το νερό· πάνω γράφει «ἰέναι».'


@scene('2025/03/blog-post_56.html', 'grafo-xana', C('Δεν σβήνω· γράφω ξανά.', 'I do not erase; I write again.', 'Je n’efface pas ; j’écris de nouveau.', 'Ich lösche nicht; ich schreibe neu.'))
def grafo(p):
    p.line(p.poly([(200, 160), (1000, 150), (1010, 560), (190, 570), (200, 160)], 6), w=2.4)
    p.line([(260, 300), (360, 260), (460, 320), (560, 280)], w=2, op=.3)
    p.line([(260, 420), (360, 380), (460, 440), (560, 400), (660, 430), (760, 380)], w=2.4, col=OCHRE)
    p.group('sk-bob', (600, 280)); p.line(p.poly([(580, 300), (620, 250), (650, 270), (610, 320), (580, 300)], 2), w=2.2); p.end()
    p.line(p.seg(760, 380, 860, 260, 4), w=4, op=.7); p.line(p.seg(756, 386, 762, 378, 1), w=2)
    return 'Σε ένα φύλλο μια παλιά γραμμή σβήνεται με γόμα και ακριβώς από κάτω ένα μολύβι τραβά μια καινούρια, φωτεινή.'


@scene('2025/03/blog-post_25.html', 'elika', C('Η γλώσσα σαν έλικα που κρατά τον κώδικα.', 'Language like a helix holding the code.', 'La langue comme une hélice qui garde le code.', 'Sprache wie eine Helix, die den Code bewahrt.'))
def elika(p):
    letters = 'ΛΟΓΟΣΦΩΣΝΟΥΣΕΚ'
    a_pts, b_pts = [], []
    for i in range(80):
        x = 120 + i * 12; a = i * .18
        a_pts.append((x, 360 + 110 * math.sin(a))); b_pts.append((x, 360 - 110 * math.sin(a)))
    p.line(a_pts, w=2.4); p.line(b_pts, w=2.4, col=OCHRE)
    for k in range(14):
        i = 3 + k * 5; x = 120 + i * 12; y1 = a_pts[i][1]; y2 = b_pts[i][1]
        p.line(p.seg(x, y1, x, y2, 3), w=1.2, op=.4)
        p.text(x, (y1 + y2) / 2 + 8, letters[k], size=22, italic=False, anchor='middle', op=.85)
    return 'Μια διπλή έλικα σαν του DNA· στα σκαλοπάτια της είναι γραμμένα ελληνικά γράμματα.'


@scene('2025/03/blog-post_71.html', 'isyxo-nero', C('Ένα ήσυχο νερό δεν είναι άδειο.', 'Still water is not empty.', 'Une eau calme n’est pas vide.', 'Stilles Wasser ist nicht leer.'))
def isyxo(p):
    p.line(p.seg(40, 400, 1160, 400, 22), w=1.8, op=.7)
    p.line([(600, 400), (600, 220)], w=2.4); p.line(p.arc(600, 170, 110, 70, 0, 2 * PI, 26), w=2.2)
    p.line([(600, 400), (600, 580)], w=1.6, op=.35); p.line(p.arc(600, 630, 110, 70, 0, 2 * PI, 26), w=1.6, op=.35)
    p.group('sk-glow'); p.dot(900, 120, 6, OCHRE); p.dot(900, 680, 5, OCHRE, op=.5); p.end()
    for k in range(3): p.line(p.seg(200 + k * 300, 460, 300 + k * 300, 460, 3), w=1, op=.3)
    return 'Ένα δέντρο στην όχθη μιας ήσυχης λίμνης καθρεφτίζεται ολόκληρο στο νερό, μαζί με ένα αστέρι.'


@scene('2025/03/blog-post_3.html', 'episkepsi', C('Σε σκέφτομαι: μια επίσκεψη χωρίς δρόμο.', 'I think of you: a visit without a road.', 'Je pense à toi : une visite sans chemin.', 'Ich denke an dich: ein Besuch ohne Weg.'))
def episk(p):
    p.floor()
    for x in (240, 960):
        p.line(p.poly([(x - 100, 600), (x - 100, 400), (x + 100, 400), (x + 100, 600)], 5), w=2.4)
        p.line(p.poly([(x - 120, 400), (x, 310), (x + 120, 400)], 4), w=2.4)
        p.line(p.poly([(x - 30, 440), (x + 30, 440), (x + 30, 500), (x - 30, 500), (x - 30, 440)], 2), w=2)
        p.out.append(f'<rect x="{x - 26}" y="444" width="52" height="52" fill="{OCHRE}" opacity=".25"/>')
    p.out.append(f'<path class="sk-glow" d="M270 440 Q 600 140 930 440" stroke="{OCHRE}" stroke-width="2" fill="none" stroke-dasharray="4 8"/>')
    return 'Δύο σπίτια μακριά το ένα από το άλλο, με φωτισμένα παράθυρα· μια διακεκομμένη καμπύλη φωτός ενώνει τα παράθυρά τους πάνω από το κενό.'


@scene('2025/03/blog-post_28.html', 'to-ek', C('Το εκ: μια αφετηρία που δεν λέει από πού.', 'The ek: an origin that does not say from where.', 'Le ek : une origine qui ne dit pas d’où.', 'Das ek: ein Ursprung, der nicht sagt, woher.'))
def toek(p):
    cx, cy = 600, 360
    p.text(cx, cy + 40, 'εκ', size=130, italic=False, anchor='middle', op=.9)
    for k in range(12):
        a = k * PI / 6
        p.line(p.seg(cx + 150 * math.cos(a), cy + 120 * math.sin(a), cx + 260 * math.cos(a), cy + 200 * math.sin(a), 4), w=1.6, op=.5)
    p.group('sk-glow'); p.dot(cx, cy - 20, 6, OCHRE); p.ring(cx, cy, 130, 110, w=1.2, col=OCHRE, op=.6); p.end()
    return 'Η λέξη «εκ» στο κέντρο, και γύρω της ακτίνες που ξεκινούν προς όλες τις κατευθύνσεις.'


@scene('2025/03/anthropia.html', 'anthropia', C('Ανθρωπιά: ένα χέρι που σηκώνει.', 'Anthropiá: a hand that lifts.', 'Anthropiá : une main qui relève.', 'Anthropiá: eine Hand, die aufhilft.'))
def anthr(p):
    p.floor()
    person(p, 760, 600, h=.95, look=-1, arm=[(720, 360), (620, 420)])
    x, y = 440, 600
    p.line(p.arc(x, y - 110, 30, 32, 0, 2 * PI, 18), w=2.4)
    p.line([(x + 10, y - 80), (x + 40, y - 30), (x + 90, y - 6)], w=2.6); p.line([(x - 10, y - 80), (x - 20, y - 20), (x + 40, y)], w=2.6)
    p.line([(x + 20, y - 70), (x + 90, y - 140), (x + 170, y - 170)], w=2.6)
    p.group('sk-glow'); p.ring(612, 428, 22, w=1.6, col=OCHRE); p.end()
    return 'Ένας άνθρωπος κάθεται πεσμένος στο έδαφος και απλώνει το χέρι· ένας άλλος σκύβει και το πιάνει για να τον σηκώσει.'


@scene('2025/03/blog-post_6.html', 'pigi', C('Η μάθηση γυρίζει στην πηγή.', 'Learning returns to the source.', 'Apprendre revient à la source.', 'Lernen kehrt zur Quelle zurück.'))
def pigi(p):
    p.floor()
    p.line(p.poly([(780, 600), (780, 420), (980, 420), (980, 600)], 5), w=2.6)                  # βρύση
    p.line(p.seg(880, 460, 880, 500, 2), w=3); p.line(p.seg(860, 500, 900, 500, 2), w=2.4)
    p.group('sk-bob', (880, 520)); p.line(p.seg(880, 506, 880, 560, 3), w=1.8, col=OCHRE); p.end()
    p.line(p.arc(880, 580, 60, 12, 0, PI, 10), w=2)
    person(p, 740, 600, h=.55, look=1, arm=[(770, 470), (860, 540)])
    p.out.append('<path d="M100 600 C 100 300, 600 200, 640 560" stroke="currentColor" stroke-width="1.4" fill="none" stroke-dasharray="5 9" opacity=".45"/>')
    return 'Ένα παιδί σκύβει και πίνει νερό από μια πέτρινη βρύση· πίσω του ένα μονοπάτι έκανε κύκλο για να καταλήξει εκεί.'


@scene('2025/03/blog-post_95.html', 'titlos-doro', C('Ο τίτλος σαν καρτελάκι σε δώρο.', 'The title like a tag on a gift.', 'Le titre comme une étiquette sur un cadeau.', 'Der Titel wie ein Anhänger an einem Geschenk.'))
def titlos(p):
    p.floor()
    p.line(p.poly([(460, 600), (460, 380), (740, 380), (740, 600)], 5), w=2.6)
    p.line(p.poly([(440, 380), (760, 380), (760, 330), (440, 330), (440, 380)], 4), w=2.6)
    p.line(p.seg(600, 330, 600, 600, 6), w=3, col=OCHRE)
    p.line([(600, 330), (540, 270), (520, 300), (600, 330), (660, 270), (680, 300), (600, 330)], w=2.4, col=OCHRE)
    p.line([(680, 300), (800, 260)], w=1.4)
    p.group('sk-sway', (800, 260))
    p.line(p.poly([(800, 250), (920, 230), (930, 290), (810, 310), (800, 250)], 3), w=2); p.text(864, 280, 'τίτλος', size=22, anchor='middle')
    p.end()
    return 'Ένα κουτί δώρου με κορδέλα· από τον φιόγκο κρέμεται ένα καρτελάκι που γράφει «τίτλος».'


@scene('2025/03/blog-post_90.html', 'anorthosi', C('Η ανάσταση ως ανόρθωση.', 'Resurrection as rising upright.', 'La résurrection comme redressement.', 'Auferstehung als Aufrichtung.'))
def anorth(p):
    p.floor()
    x = 600
    p.line(p.arc(x + 10, 300, 32, 34, 0, 2 * PI, 18), w=2.6)
    p.line([(x, 334), (x - 20, 420), (x - 60, 480), (x - 40, 600)], w=2.6); p.line([(x + 20, 334), (x + 30, 430), (x + 60, 520), (x + 50, 600)], w=2.6)
    p.line([(x + 20, 350), (x + 80, 280), (x + 110, 200)], w=2.6); p.line([(x - 4, 350), (x - 60, 380), (x - 90, 440)], w=2.4)
    for k in range(3): p.line(p.arc(x, 600, 120 + k * 40, 30 + k * 10, PI * 1.05, PI * 1.95, 10), w=1.2, op=.4 - k * .1)
    p.group('sk-glow'); p.dot(x + 120, 180, 7, OCHRE); p.ring(x + 120, 180, 30, w=1.2, col=OCHRE, op=.6); p.end()
    return 'Ένας άνθρωπος ανασηκώνεται από το έδαφος, με το ένα χέρι υψωμένο προς ένα φως από πάνω.'


@scene('2025/03/blog-post_61.html', 'neos-vlastos', C('Από τον πεσμένο κορμό, ένας νέος βλαστός.', 'From the fallen trunk, a new shoot.', 'Du tronc tombé, une nouvelle pousse.', 'Aus dem gefallenen Stamm ein neuer Trieb.'))
def neos(p):
    p.floor()
    p.line([(200, 600), (220, 540), (900, 520), (960, 560), (940, 600)], w=2.8)
    p.line(p.arc(220, 570, 20, 30, 0, 2 * PI, 14), w=2)
    for k in range(4): p.line(p.seg(300 + k * 150, 540, 360 + k * 150, 536, 2), w=1.2, op=.5)
    p.group('sk-sway', (640, 520))
    p.line([(640, 524), (636, 440), (650, 360)], w=2.2, col=OCHRE)
    p.line([(638, 460), (600, 430), (594, 446), (638, 460)], w=1.8, col=OCHRE); p.line([(644, 400), (690, 376), (694, 392), (644, 400)], w=1.8, col=OCHRE)
    p.end()
    return 'Ένας κορμός δέντρου πεσμένος στο έδαφος, και από τη μέση του φυτρώνει ένας νέος βλαστός.'


@scene('2025/03/blog-post_99.html', 'kardia-mati', C('Η καρδιά ως κέντρο αντίληψης, όχι μόνο συναίσθημα.', 'The heart as a centre of perception, not only feeling.', 'Le cœur comme centre de perception, pas seulement d’émotion.', 'Das Herz als Zentrum der Wahrnehmung, nicht nur des Gefühls.'))
def kardia(p):
    cx, cy = 600, 360
    pts = [(cx + 16 * (16 * math.sin(t) ** 3), cy - 16 * (13 * math.cos(t) - 5 * math.cos(2 * t) - 2 * math.cos(3 * t) - math.cos(4 * t))) for t in [i * 2 * PI / 60 for i in range(61)]]
    p.line(pts, w=2.8)
    p.line(p.arc(cx, cy - 10, 70, 34, PI * 1.05, PI * 1.95, 10) + p.arc(cx, cy - 10, 70, 34, PI * .05, PI * .95, 10), w=2.2)
    p.group('sk-blink', (cx, cy - 10)); p.ring(cx, cy - 10, 20, w=2, col=OCHRE); p.dot(cx, cy - 10, 8, OCHRE); p.end()
    return 'Μια μεγάλη καρδιά, και μέσα της ένα ανοιχτό μάτι που βλέπει.'


@scene('2025/03/blog-post_44.html', 'apo-to-ena', C('Από το ένα στο εμείς.', 'From the one to the we.', 'De l’un au nous.', 'Vom Einen zum Wir.'))
def ena(p):
    cx, cy = 600, 360
    p.group('sk-glow'); p.dot(cx, cy, 10, OCHRE); p.end()
    for r, n in ((90, 6), (170, 12), (250, 18)):
        pts = [(cx + r * math.cos(k * 2 * PI / n), cy + r * .7 * math.sin(k * 2 * PI / n)) for k in range(n)]
        for x, y in pts: p.dot(x, y, 5 - r / 100)
        p.line(pts + pts[:1], w=1.2, op=.35)
    return 'Ένα φωτεινό σημείο στο κέντρο, και γύρω του τρεις όλο και μεγαλύτεροι κύκλοι από σημεία ενωμένα μεταξύ τους.'


@scene('2025/03/blog-post_46.html', 'gefyra-dia', C('Το «δια»: γέφυρα, όχι διαχωρισμός.', '“Dia”: a bridge, not a division.', '« Dia » : un pont, non une séparation.', '„Dia“: eine Brücke, keine Trennung.'))
def gefyra(p):
    p.line([(40, 460), (360, 460), (400, 640)], w=2.4); p.line([(800, 640), (840, 460), (1160, 460)], w=2.4)
    p.line(p.arc(600, 560, 260, 160, PI * 1.08, PI * 1.92, 24), w=2.8)
    p.line(p.seg(340, 460, 860, 460, 14), w=2.6)
    for k in range(9): x = 380 + k * 55; p.line(p.seg(x, 460, x, 560 - 160 * math.sin(math.acos(max(-1, min(1, (x - 600) / 260)))) + 160 * 0, 2), w=1.2, op=.5)
    p.text(200, 420, 'προ', size=34, anchor='middle', op=.75); p.text(1000, 420, 'μετά', size=34, anchor='middle', op=.75)
    p.group('sk-glow'); p.text(600, 430, 'διά', size=36, anchor='middle', col=OCHRE); p.end()
    return 'Μια τοξωτή γέφυρα ενώνει δύο όχθες που γράφουν «προ» και «μετά»· στη μέση της γράφει «διά».'


@scene('2025/03/blog-post_79.html', 'enikos', C('Ένα γράμμα στον ενικό, για όποιον το διαβάζει.', 'A letter in the singular, for whoever reads it.', 'Une lettre au singulier, pour qui la lit.', 'Ein Brief in der Einzahl, für jeden, der ihn liest.'))
def enikos(p):
    p.floor()
    person(p, 420, 600, h=.95, sit=True, glasses=True, look=1, arm=[(480, 380), (560, 360)])
    p.line(p.poly([(390, 600), (390, 520), (500, 520), (500, 600)], 4), w=2.2)
    p.line(p.poly([(560, 260), (760, 250), (770, 430), (566, 440), (560, 260)], 4), w=2.2)
    p.text(590, 300, 'Εσύ,', size=30, col=OCHRE)
    for k in range(4): p.line(p.seg(590, 330 + k * 24, 740 - k * 20, 328 + k * 24, 4), w=1.2, op=.5)
    return 'Ένας άνθρωπος με γυαλιά κρατά ένα γράμμα που αρχίζει με τη λέξη «Εσύ,».'


@scene('2025/03/blog-post_42.html', 'kefali-kardia', C('Από το κεφάλι στην καρδιά, ένα σκαλί.', 'From head to heart, one step.', 'De la tête au cœur, une marche.', 'Vom Kopf zum Herzen, eine Stufe.'))
def kefkar(p):
    p.floor()
    person(p, 600, 600, h=1.05, look=0)
    p.out.append(f'<path class="sk-glow" d="M600 286 C 640 330, 560 360, 600 400" stroke="{OCHRE}" stroke-width="2" fill="none" stroke-dasharray="3 6"/>')
    p.line([(590, 404), (584, 396), (590, 390), (600, 398), (610, 390), (616, 396), (610, 404), (600, 414), (590, 404)], w=2, col=OCHRE)
    return 'Ένας άνθρωπος όρθιος· μια φωτεινή διακεκομμένη γραμμή κατεβαίνει από το κεφάλι του ως μια μικρή καρδιά στο στήθος.'


@scene('2025/03/blog-post_30.html', 'ergo-pou-vrike', C('Δεν το σχεδιάσαμε· μας βρήκε.', 'We did not plan it; it found us.', 'Nous ne l’avons pas prévu ; il nous a trouvés.', 'Wir haben es nicht geplant; es hat uns gefunden.'))
def ergo(p):
    p.floor()
    p.line(p.seg(380, 480, 820, 480, 10), w=2.6); p.line(p.seg(400, 480, 400, 600, 4), w=2.2); p.line(p.seg(800, 480, 800, 600, 4), w=2.2)
    p.line(p.seg(380, 400, 820, 400, 10), w=2, op=.6); p.line(p.seg(390, 400, 390, 480, 3), w=2, op=.6); p.line(p.seg(810, 400, 810, 480, 3), w=2, op=.6)
    p.line(p.poly([(560, 480), (570, 452), (680, 450), (690, 478)], 3), w=2.4)
    for k in range(3): p.line(p.seg(580, 462 + k * 5, 670, 460 + k * 5, 3), w=1, op=.5)
    p.group('sk-glow'); p.ring(625, 460, 80, 30, w=1.4, col=OCHRE, op=.7); p.end()
    for k, (x, y) in enumerate(((560, 300), (700, 260), (630, 340))):
        p.group('sk-bob', (x, y)); p.line([(x, y), (x + 14, y - 8), (x + 18, y + 4), (x, y)], w=1.4, op=.6); p.end()
    return 'Πάνω σε ένα παγκάκι στο πάρκο, ένα δεμένο χειρόγραφο που κάποιος βρήκε, φωτισμένο· γύρω του πέφτουν φύλλα.'


@scene('2025/03/blog-post_31.html', 'e-ton-delfon', C('Το Ε των Δελφών: είσαι.', 'The E at Delphi: you are.', 'Le E de Delphes : tu es.', 'Das E von Delphi: du bist.'))
def edelf(p):
    p.floor()
    for x in (250, 950):
        p.line(p.seg(x - 30, 600, x - 30, 200, 10), w=2, op=.5); p.line(p.seg(x + 30, 600, x + 30, 200, 10), w=2, op=.5)
        p.line(p.seg(x - 44, 200, x + 44, 200, 4), w=2, op=.5)
    p.line(p.poly([(440, 600), (440, 220), (760, 220), (760, 600)], 6), w=2.6)
    p.group('sk-glow'); p.text(600, 500, 'Ε', size=280, italic=False, anchor='middle', col=OCHRE, op=.95); p.end()
    p.text(600, 580, 'ΕΙ · ΝΑΙ', size=24, italic=False, anchor='middle', spacing=4, op=.6)
    return 'Ανάμεσα σε δύο κίονες, μια πέτρινη πλάκα με ένα μεγάλο χαραγμένο Ε, και από κάτω «ΕΙ · ΝΑΙ».'


@scene('2025/03/blog-post_55.html', 'laouto', C('Ερωτοαποκρίσεις, όχι απαντήσεις.', 'Questions and replies, not answers.', 'Des questions-réponses, non des réponses.', 'Frage und Erwiderung, keine Antworten.'))
def laouto(p):
    cx, cy = 520, 440
    p.line(p.arc(cx, cy, 150, 110, 0, 2 * PI, 32), w=2.8)
    p.ring(cx + 20, cy - 10, 30, w=2)
    p.line(p.seg(cx + 140, cy - 40, cx + 420, cy - 230, 10), w=2.6); p.line(p.seg(cx + 150, cy - 20, cx + 430, cy - 210, 10), w=2.6)
    p.line([(cx + 425, cy - 220), (cx + 470, cy - 280), (cx + 520, cy - 270), (cx + 520, cy - 230), (cx + 490, cy - 220)], w=2.6, col=OCHRE)
    p.dot(cx + 480, cy - 190, 5, OCHRE)
    for k in range(4): p.line(p.seg(cx - 100, cy - 6 + k * 6, cx + 430, cy - 220 + k * 6, 14), w=.9, op=.6)
    for k in range(3):
        p.group('sk-bob', (cx - 220 + k * 60, cy - 200)); p.text(cx - 220 + k * 60, cy - 200 + (k % 2) * 30, '♪', size=34, italic=False, op=.6); p.end()
    return 'Ένα λαούτο, με το κεφάλι του μπράτσου του να γυρίζει σαν ερωτηματικό· γύρω του αιωρούνται νότες.'


@scene('2025/03/blog-post_64.html', 'pyli', C('Να περνάς από την πύλη χωρίς να φεύγεις.', 'To pass through the gate without leaving.', 'Passer la porte sans partir.', 'Durch das Tor gehen, ohne fortzugehen.'))
def pyli(p):
    p.floor()
    p.line(p.poly([(320, 600), (320, 150), (880, 150), (880, 600)], 8), w=2.8)
    p.line(p.seg(300, 150, 900, 150, 10), w=2.4); p.line(p.seg(300, 120, 900, 120, 10), w=2)
    p.line(p.seg(480, 600, 480, 340, 6) + p.arc(600, 340, 120, 140, PI, 2 * PI, 18)[1:] + p.seg(720, 340, 720, 600, 6)[1:], w=2.6)
    p.out.append(f'<path class="sk-glow" d="M480 600 L480 340 A120 140 0 0 1 720 340 L720 600 Z" fill="{OCHRE}" opacity=".16"/>')
    person(p, 600, 600, h=.62, look=0)
    return 'Μια μεγάλη θριαμβική αψίδα· στο φωτισμένο της άνοιγμα στέκεται ένας μικρός άνθρωπος.'


@scene('2025/03/blog-post_16.html', 'plision', C('Ο πιο κοντινός πλησίον.', 'The nearest neighbour.', 'Le prochain le plus proche.', 'Der nächste Nächste.'))
def plision(p):
    p.floor()
    person(p, 590, 600, h=1, look=0, arm=[(630, 370), (600, 400)])
    p.group('sk-sway', (620, 600))
    p.line(p.arc(640, 270, 34, 36, 0, 2 * PI, 18), w=1.8, col=OCHRE, op=.7)
    p.line([(620, 306), (600, 420), (608, 600)], w=1.8, col=OCHRE, op=.6); p.line([(660, 306), (680, 420), (672, 600)], w=1.8, col=OCHRE, op=.6)
    p.end()
    return 'Ένας άνθρωπος με το χέρι στο στήθος· δίπλα του, σχεδόν πάνω του, ένα φωτεινό περίγραμμα του ίδιου.'


@scene('2025/03/blog-post_77.html', 'kleps-ydra', C('Μια στιγμή που απλώνεται αντί να περάσει.', 'A moment that spreads instead of passing.', 'Un instant qui s’étend au lieu de passer.', 'Ein Augenblick, der sich ausdehnt, statt zu vergehen.'))
def klep(p):
    cx = 600
    p.line(p.seg(cx - 140, 120, cx + 140, 120, 6), w=3); p.line(p.seg(cx - 140, 600, cx + 140, 600, 6), w=3)
    p.line([(cx - 110, 130), (cx - 100, 280), (cx - 10, 360), (cx - 100, 440), (cx - 110, 590)], w=2.6)
    p.line([(cx + 110, 130), (cx + 100, 280), (cx + 10, 360), (cx + 100, 440), (cx + 110, 590)], w=2.6)
    p.line([(cx - 80, 220), (cx, 300), (cx + 80, 220)], w=1.6, op=.6)
    p.line([(cx - 90, 590), (cx, 520), (cx + 90, 590)], w=1.6, op=.6)
    for k in range(5):
        p.group('sk-bob', (cx, 380 + k * 24)); p.dot(cx + (k % 2) * 6 - 3, 380 + k * 24, 3, OCHRE); p.end()
    p.group('sk-glow'); p.ring(cx, 360, 50, w=1.2, col=OCHRE, op=.6); p.end()
    return 'Μια κλεψύδρα όπου οι κόκκοι της άμμου αιωρούνται σταματημένοι στη μέση, αντί να πέφτουν.'


@scene('2025/03/blog-post_1.html', 'periballon', C('Είμαι περιβάλλον, και με περιβάλλει.', 'I am an environment, and it surrounds me.', 'Je suis environnement, et il m’environne.', 'Ich bin Umwelt, und sie umgibt mich.'))
def periv(p):
    p.floor()
    for k in range(10):
        a = PI + k * PI / 9; x = 600 + 440 * math.cos(a); y = 560 + 160 * math.sin(a) * .3
        if k in (4, 5): continue
        p.line(p.seg(x, 600, x, 420, 4), w=2); p.group('sk-sway', (x, 420)); p.line(p.arc(x, 380, 40, 46, 0, 2 * PI, 16), w=1.8); p.end()
    p.line(p.poly([(540, 600), (540, 420), (660, 420), (660, 600)], 4), w=2.2, col=OCHRE)
    person(p, 466, 600, h=.6, look=1)
    return 'Ένας άνθρωπος μέσα σε έναν κύκλο από δέντρα· στο σημείο όπου λείπουν δύο δέντρα στέκεται μια φωτεινή πόρτα.'


@scene('2025/03/blog-post.html', 'ion-pedio', C('Ό,τι κινείται σχηματίζεται από ό,τι το περιβάλλει.', 'What moves is shaped by what surrounds it.', 'Ce qui bouge est formé par ce qui l’entoure.', 'Was sich bewegt, wird von dem geformt, was es umgibt.'))
def ionp(p):
    cx, cy = 600, 360
    for k in range(7):
        y = 120 + k * 80
        p.line([(40, y), (300, y), (480, y + (cy - y) * .4), (720, y + (cy - y) * .4), (900, y), (1160, y)], w=1.2, op=.4)
    p.group('sk-sway', (cx, cy)); p.line(p.arc(cx, cy, 120, 50, 0, 2 * PI, 26), w=1.8); p.line(p.arc(cx, cy, 50, 120, 0, 2 * PI, 26), w=1.8); p.end()
    p.group('sk-glow'); p.dot(cx, cy, 12, OCHRE); p.end()
    p.text(cx + 20, cy - 14, '+', size=24, italic=False)
    return 'Ένα φορτισμένο σωματίδιο με τροχιές γύρω του, μέσα σε γραμμές πεδίου που λυγίζουν προς το μέρος του.'


@scene('2025/02/blog-post_62.html', 'vroxi-vlastari', C('Το λυπηρό ποτίζει ό,τι θα φυτρώσει.', 'Sorrow waters what will grow.', 'Le chagrin arrose ce qui va pousser.', 'Das Traurige gießt, was wachsen wird.'))
def vroxi(p):
    p.floor()
    p.line(p.arc(560, 150, 70, 46, PI, 2 * PI, 12) + p.arc(650, 140, 70, 60, PI, 2 * PI, 12)[1:] + p.arc(740, 160, 60, 40, PI, 2 * PI, 10)[1:], w=2.2)
    p.line(p.seg(490, 160, 800, 160, 8), w=1.8)
    for k in range(7):
        x = 520 + k * 40
        p.group('sk-bob', (x, 240 + (k % 3) * 40)); p.line([(x, 220 + (k % 3) * 40), (x - 4, 236 + (k % 3) * 40)], w=1.6, op=.6); p.end()
    p.group('sk-sway', (640, 600))
    p.line([(640, 600), (636, 520), (650, 470)], w=2.2, col=OCHRE)
    p.line([(638, 530), (600, 506), (596, 520), (638, 530)], w=1.8, col=OCHRE); p.line([(646, 490), (690, 470), (692, 484), (646, 490)], w=1.8, col=OCHRE)
    p.end()
    return 'Ένα σύννεφο βρέχει πάνω σε ένα μικρό βλαστάρι που μόλις βγήκε από το χώμα.'


@scene('2025/02/blog-post_40.html', 'rythmos', C('Η συγχώρεση έρχεται σαν ρυθμός, όχι σαν απόφαση.', 'Forgiveness comes as rhythm, not as decision.', 'Le pardon vient comme un rythme, non comme une décision.', 'Vergebung kommt als Rhythmus, nicht als Entschluss.'))
def rythmos(p):
    p.line([(40, 640), (600, 600), (1160, 620)], w=2, op=.7)
    for k in range(4):
        p.group('sk-sway' if k % 2 else 'sk-bob', (600, 400 + k * 50))
        pts = [(40 + i * 20, 400 + k * 50 + 14 * math.sin(i / 3 + k)) for i in range(57)]
        p.line(pts, w=1.6, col=OCHRE if k == 2 else 'currentColor', op=.7)
        p.end()
    person(p, 600, 600, h=.62, sit=True, look=0)
    return 'Ένας άνθρωπος κάθεται στην ακτή μπροστά σε κύματα που έρχονται το ένα πίσω από το άλλο με σταθερό ρυθμό.'


@scene('2025/02/blog-post_97.html', 'motiva-ammou', C('Τα μοτίβα είναι το αποτύπωμα της ροής.', 'Patterns are the imprint of the flow.', 'Les motifs sont l’empreinte du flux.', 'Muster sind der Abdruck des Fließens.'))
def motiva(p):
    p.line([(40, 380), (300, 260), (600, 320), (900, 220), (1160, 300)], w=2.2)
    for k in range(9):
        y = 400 + k * 28
        p.line([(40, y), (200, y - 10), (400, y + 6), (600, y - 8), (800, y + 6), (1000, y - 6), (1160, y)], w=1.4, op=.55)
    p.group('sk-flutter', (760, 200))
    p.line([(720, 220), (800, 180)], w=1.6, col=OCHRE)
    for k in range(6): p.line([(728 + k * 12, 216 - k * 6), (736 + k * 12, 200 - k * 6)], w=1.2, col=OCHRE)
    p.end()
    return 'Αμμόλοφοι με κυματιστά μοτίβα που χάραξε ο άνεμος, και ένα φτερό που αιωρείται από πάνω.'


@scene('2025/02/blog-post_49.html', 'kremasti-gefyra', C('Ούτε πια εκεί, ούτε ακόμα εδώ.', 'No longer there, not yet here.', 'Plus là-bas, pas encore ici.', 'Nicht mehr dort, noch nicht hier.'))
def kremast(p):
    p.line([(40, 420), (220, 420), (240, 700)], w=2.4); p.line([(960, 700), (980, 420), (1160, 420)], w=2.4)
    deck = [(220 + i * 38, 420 + 70 * math.sin(i / 20 * PI)) for i in range(21)]
    p.group('sk-sway', (600, 420))
    p.line(deck, w=2.6); p.line([(x, y - 70) for x, y in deck], w=1.6, op=.7)
    for x, y in deck[::2]: p.line(p.seg(x, y, x, y - 70, 2), w=1, op=.6)
    person(p, 600, 490, h=.5, look=1)
    p.end()
    return 'Ένας άνθρωπος στη μέση μιας κρεμαστής γέφυρας που κουνιέται ελαφρά, ανάμεσα σε δύο γκρεμούς.'


@scene('2025/02/blog-post_28.html', 'anamesa-xeria', C('Λίγο πριν αγγιχτούν.', 'Just before they touch.', 'Juste avant qu’elles se touchent.', 'Kurz bevor sie sich berühren.'))
def xeria(p):
    p.line([(40, 380), (300, 370), (520, 360)], w=2.6); p.line([(40, 420), (300, 410), (520, 390)], w=2.6)
    p.line([(520, 360), (560, 350), (566, 362), (530, 372)], w=2); p.line([(520, 390), (550, 380)], w=2)
    p.line([(1160, 330), (900, 340), (680, 350)], w=2.6); p.line([(1160, 370), (900, 380), (680, 380)], w=2.6)
    p.line([(680, 350), (640, 346), (636, 358), (672, 364)], w=2); p.line([(680, 380), (650, 372)], w=2)
    p.group('sk-glow'); p.dot(600, 356, 5, OCHRE); p.ring(600, 356, 18, w=1.2, col=OCHRE, op=.7); p.end()
    return 'Δύο χέρια από αντίθετες πλευρές απλώνονται το ένα προς το άλλο· ανάμεσα στα δάχτυλά τους, που δεν αγγίζονται ακόμα, ένα φως.'


@scene('2025/02/blog-post.html', 'rogmi-revma', C('Από τη ρωγμή, το ρεύμα.', 'From the crack, the current.', 'De la fissure, le courant.', 'Aus dem Riss die Strömung.'))
def rogmi(p):
    p.line([(200, 600), (240, 300), (400, 180), (800, 170), (960, 300), (1000, 600)], w=2.8)
    p.line([(600, 175), (580, 260), (620, 330), (590, 420), (610, 480)], w=2.2)
    for k in range(3):
        p.group('sk-sway' if k % 2 else 'sk-bob', (620, 560))
        p.line([(605 + k * 6, 480), (620 + k * 10, 540), (700 + k * 20, 600), (900 + k * 30, 640), (1160, 650 + k * 10)], w=1.8, col=OCHRE if k == 1 else 'currentColor', op=.75)
        p.end()
    p.line(p.seg(40, 600, 1160, 600, 20), w=1.4, op=.4)
    return 'Ένας μεγάλος βράχος με μια ρωγμή από πάνω ως κάτω· από τη βάση της βγαίνει νερό και κυλά προς τα δεξιά.'


if __name__ == '__main__':
    run(S)
