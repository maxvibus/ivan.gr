"""Σκίτσα δημοσιεύσεων, έβδομη σειρά (21.10.2026): Μάρτιος 2025, β΄ μέρος."""
import math, os, sys, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pen import OCHRE
from sketchbook import registry, person, run, PI

S, scene = registry()


def flame(p, x, y, s=1, cls='sk-flicker'):
    p.group(cls, (x, y))
    p.out.append(f'<path d="M{x} {y - 34 * s:.0f} Q{x + 12 * s:.0f} {y - 14 * s:.0f} {x} {y} Q{x - 12 * s:.0f} {y - 14 * s:.0f} {x} {y - 34 * s:.0f}Z" fill="{OCHRE}" stroke="{OCHRE}" stroke-width="1.5"/>')
    p.end()


@scene('2025/03/2000.html', 'diktyo-2000', dict(
    el='Από το 2000 η νοημοσύνη απλώνεται σε δίκτυο.', en='Since 2000, intelligence spreads as a network.',
    fr='Depuis 2000, l’intelligence s’étend en réseau.', de='Seit 2000 breitet sich Intelligenz als Netz aus.'))
def diktyo(p):
    p.floor()
    nodes = [(220, 300), (420, 180), (600, 330), (820, 200), (980, 360), (380, 470), (760, 480)]
    for i, (x, y) in enumerate(nodes):
        for j in range(i + 1, len(nodes)):
            if (i + j) % 3 != 0: p.line(p.seg(x, y, nodes[j][0], nodes[j][1], 6), w=1.2, op=.4)
    p.line(p.arc(220, 300, 46, 38, 0, 2 * PI, 22), w=2.2); p.line([(190, 300), (220, 280), (250, 300)], w=1.6, op=.7)         # εγκέφαλος
    p.line(p.poly([(780, 170), (860, 170), (860, 230), (780, 230), (780, 170)], 3), w=2.2)                                        # οθόνη
    p.line(p.seg(980, 410, 980, 340, 3), w=2.2); p.line(p.arc(980, 320, 34, 30, 0, 2 * PI, 18), w=2)                              # δέντρο
    p.line(p.poly([(405, 150), (435, 150), (435, 205), (405, 205), (405, 150)], 2), w=2)                                          # κινητό
    for (x, y) in nodes[2:3] + nodes[5:]: p.dot(x, y, 5)
    p.group('sk-glow'); p.dot(600, 330, 8, OCHRE); p.ring(600, 330, 24, w=1.2, col=OCHRE, op=.6); p.end()
    return 'Ένας εγκέφαλος, ένα κινητό, μια οθόνη και ένα δέντρο, ενωμένα με λεπτές γραμμές σε ένα δίκτυο που φωτίζεται στο κέντρο.'


@scene('2025/03/5-20-1900-2000.html', 'tainia', dict(
    el='Η σκέψη σε ταινία με μηδενικά και ένα.', en='Thought on a tape of zeros and ones.',
    fr='La pensée sur un ruban de zéros et de uns.', de='Denken auf einem Band aus Nullen und Einsen.'))
def tainia(p):
    y = 360
    p.line(p.seg(40, y - 40, 1160, y - 40, 20), w=2.4); p.line(p.seg(40, y + 40, 1160, y + 40, 20), w=2.4)
    bits = '0110100111010010110'
    for k, b in enumerate(bits):
        x = 70 + k * 60
        p.line(p.seg(x - 30, y - 40, x - 30, y + 40, 2), w=1.2, op=.5)
        p.text(x, y + 14, b, size=36, italic=False, anchor='middle', col=OCHRE if k == 9 else 'currentColor', op=.9)
    p.group('sk-bob', (630, 250))
    p.line(p.poly([(590, 200), (670, 200), (670, 290), (650, 310), (610, 310), (590, 290), (590, 200)], 4), w=2.6)
    p.text(630, 260, '▼', size=26, italic=False, anchor='middle', op=.7)
    p.end()
    return 'Μια μακριά ταινία χωρισμένη σε τετράγωνα με μηδενικά και άσσους, και από πάνω μια κεφαλή ανάγνωσης στέκεται πάνω από ένα φωτεινό ψηφίο.'


@scene('2025/03/blog-post_51.html', 'pinakida-othoni', dict(
    el='Πήλινη πινακίδα, πάπυρος, βιβλίο, οθόνη.', en='Clay tablet, papyrus, book, screen.',
    fr='Tablette d’argile, papyrus, livre, écran.', de='Tontafel, Papyrus, Buch, Bildschirm.'))
def pinak(p):
    p.floor()
    p.line(p.poly([(120, 420), (250, 410), (260, 560), (126, 570), (120, 420)], 4), w=2.6)
    for k in range(5): p.line(p.seg(140, 440 + k * 24, 236, 436 + k * 24, 4), w=1.2, op=.5)
    p.line([(360, 430), (520, 430)], w=2.4); p.line([(360, 560), (520, 560)], w=2.4)
    p.line(p.arc(360, 495, 14, 65, PI * .5, PI * 1.5, 10), w=2.4); p.line(p.arc(520, 495, 14, 65, -PI * .5, PI * .5, 10), w=2.4)
    for k in range(4): p.line(p.seg(380, 452 + k * 28, 500, 452 + k * 28, 4), w=1.2, op=.5)
    p.line([(620, 470), (630, 420), (720, 410), (730, 420)], w=2.4); p.line([(840, 470), (830, 420), (740, 410), (730, 420)], w=2.4)
    p.line(p.seg(620, 470, 840, 470, 6), w=2.2); p.line(p.seg(730, 420, 730, 470, 2), w=1.6)
    p.line(p.poly([(920, 380), (1080, 380), (1080, 500), (920, 500), (920, 380)], 4), w=2.4)
    p.line(p.seg(1000, 500, 1000, 560, 2), w=2.2); p.line(p.seg(950, 560, 1050, 560, 3), w=2.2)
    p.group('sk-glow'); p.line(p.poly([(930, 390), (1070, 390), (1070, 490), (930, 490), (930, 390)], 4), w=1.4, col=OCHRE, op=.8); p.end()
    p.out.append(f'<path d="M190 380 Q 600 200 1000 360" stroke="{OCHRE}" stroke-width="1.4" fill="none" stroke-dasharray="4 8" opacity=".8"/>')
    return 'Στη σειρά, μια πήλινη πινακίδα, ένας πάπυρος, ένα ανοιχτό βιβλίο και μια οθόνη, με μια διακεκομμένη καμπύλη να περνά από πάνω τους.'


@scene('2025/03/blog-post_82.html', 'balaki', dict(
    el='Η νοημοσύνη ως μπαλάκι που πηγαινοέρχεται.', en='Intelligence as a ball passed back and forth.',
    fr='L’intelligence comme une balle qui va et vient.', de='Intelligenz als Ball, der hin und her geht.'))
def balaki(p):
    p.floor()
    person(p, 300, 600, h=.9, look=1, arm=[(340, 330), (390, 300)])
    person(p, 900, 600, h=.9, look=-1, arm=[(940, 330), (860, 300)])
    p.out.append(f'<path d="M400 290 Q 620 60 850 290" stroke="currentColor" stroke-width="1.4" fill="none" stroke-dasharray="5 8" opacity=".5"/>')
    p.group('sk-bob', (625, 175)); p.ring(625, 175, 16, w=2.4, col=OCHRE); p.end()
    return 'Δύο άνθρωποι πετούν ο ένας στον άλλον ένα μπαλάκι, που διαγράφει τόξο ανάμεσά τους.'


@scene('2025/03/blog-post_50.html', 'triti-floga', dict(
    el='Δύο φλόγες, και μια τρίτη ανάμεσα.', en='Two flames, and a third between them.',
    fr='Deux flammes, et une troisième entre elles.', de='Zwei Flammen, und eine dritte dazwischen.'))
def triti(p):
    p.line(p.seg(200, 540, 1000, 540, 14), w=2.4)
    for x in (420, 780):
        p.line(p.poly([(x - 16, 540), (x - 16, 400), (x + 16, 400), (x + 16, 540)], 4), w=2.4)
        flame(p, x, 394)
    flame(p, 600, 330, 1.2)
    p.group('sk-glow'); p.ring(600, 312, 40, 50, w=1.2, col=OCHRE, op=.6); p.end()
    p.out.append(f'<path d="M432 380 Q 520 330 586 318" stroke="{OCHRE}" stroke-width="1.2" fill="none" opacity=".6"/><path d="M768 380 Q 680 330 614 318" stroke="{OCHRE}" stroke-width="1.2" fill="none" opacity=".6"/>')
    return 'Δύο αναμμένα κεριά, και ανάμεσά τους, χωρίς κερί από κάτω, μια τρίτη φλόγα.'


@scene('2025/03/blog-post_92.html', 'kampana', dict(
    el='Ο ήχος δεν φτάνει στο αυτί· γεμίζει τον τόπο.', en='Sound does not reach the ear; it fills the place.',
    fr='Le son n’atteint pas l’oreille ; il remplit le lieu.', de='Der Klang erreicht nicht das Ohr; er füllt den Ort.'))
def kampana(p):
    p.line([(40, 600), (300, 420), (520, 520), (760, 380), (1160, 600)], w=2.2, op=.6)
    p.line(p.seg(40, 600, 1160, 600, 20), w=2, op=.7)
    cx = 600
    p.line(p.poly([(cx - 70, 380), (cx - 70, 220), (cx + 70, 220), (cx + 70, 380)], 5), w=2.4)
    p.line(p.arc(cx, 220, 70, 50, PI, 2 * PI, 12), w=2.4)
    p.group('sk-sway', (cx, 240))
    p.line([(cx - 30, 320), (cx - 26, 270), (cx, 252), (cx + 26, 270), (cx + 30, 320), (cx - 30, 320)], w=2.6)
    p.dot(cx, 328, 5, OCHRE)
    p.end()
    for i in range(3):
        p.group(f'sk-ripple sk-r{i}', (cx, 290))
        p.line(p.arc(cx, 290, 260, 150, -PI * .1, PI * 1.1, 30), w=1.4, col=OCHRE, op=.6)
        p.end()
    return 'Ένα μικρό καμπαναριό σε μια κοιλάδα· η καμπάνα κουνιέται και ο ήχος της απλώνεται σε μεγάλους κύκλους πάνω από τους λόφους.'


@scene('2025/03/blog-post_66.html', 'agalma', dict(
    el='Ένα άγαλμα ανάμεσα σε κίονες, κι ένα πουλί στον ώμο του.', en='A statue among columns, and a bird on its shoulder.',
    fr='Une statue parmi les colonnes, et un oiseau sur son épaule.', de='Eine Statue zwischen Säulen, und ein Vogel auf ihrer Schulter.'))
def agalma(p):
    p.floor()
    for x in (160, 320, 880, 1040):
        p.line(p.seg(x - 30, 600, x - 30, 160, 10), w=2, op=.5); p.line(p.seg(x + 30, 600, x + 30, 160, 10), w=2, op=.5)
        for k in range(3): p.line(p.seg(x - 15 + k * 15, 590, x - 15 + k * 15, 170, 10), w=1, op=.3)
        p.line(p.seg(x - 44, 160, x + 44, 160, 4), w=2, op=.5)
    p.line(p.seg(100, 140, 1100, 140, 20), w=2, op=.5)
    cx = 600
    p.line(p.poly([(cx - 80, 600), (cx - 80, 540), (cx + 80, 540), (cx + 80, 600)], 4), w=2.4)
    p.line(p.arc(cx, 260, 36, 40, 0, 2 * PI, 22), w=2.6)
    p.line([(cx - 10, 300), (cx - 50, 330), (cx - 60, 420), (cx - 50, 540)], w=2.6); p.line([(cx + 12, 300), (cx + 52, 330), (cx + 60, 420), (cx + 54, 540)], w=2.6)
    for k in range(5): p.line([(cx - 40 + k * 20, 360), (cx - 44 + k * 22, 540)], w=1.2, op=.5)   # πτυχώσεις
    p.group('sk-bob', (cx + 56, 318))
    p.line([(cx + 40, 318), (cx + 60, 300), (cx + 84, 304), (cx + 96, 296), (cx + 90, 312), (cx + 70, 322), (cx + 40, 318)], w=2, col=OCHRE)
    p.end()
    return 'Ένα μαρμάρινο άγαλμα με πτυχωτό ένδυμα στέκει ήσυχο ανάμεσα σε κίονες· ένα μικρό πουλί έχει καθίσει στον ώμο του.'


@scene('2025/03/blog-post_15.html', 'sfragida', dict(
    el='Η σφραγίδα αφήνει έκτυπο· το χέρι αφήνει πράξη.', en='The seal leaves an imprint; the hand leaves an act.',
    fr='Le sceau laisse une empreinte ; la main laisse un acte.', de='Das Siegel hinterlässt einen Abdruck; die Hand hinterlässt eine Tat.'))
def sfrag(p):
    p.line(p.seg(160, 520, 1040, 520, 14), w=2.4)
    p.line(p.arc(480, 500, 90, 26, 0, 2 * PI, 24), w=2.4)                                             # κερί
    p.line(p.arc(480, 498, 56, 15, 0, 2 * PI, 20), w=1.6); p.text(480, 506, 'Π', size=24, italic=False, anchor='middle', op=.8)
    p.group('sk-bob', (760, 300))
    p.line(p.poly([(730, 400), (790, 400), (784, 330), (736, 330), (730, 400)], 3), w=2.4)
    p.line(p.arc(760, 316, 16, 14, 0, 2 * PI, 14), w=2.4); p.line(p.poly([(722, 404), (798, 404)], 3), w=3)
    p.line([(800, 300), (900, 260), (1000, 250)], w=2.6); p.line([(800, 330), (900, 300), (1000, 290)], w=2.6)
    p.end()
    p.group('sk-glow'); p.ring(480, 498, 70, 20, w=1.2, col=OCHRE, op=.8); p.end()
    return 'Ένα χέρι κρατά μια σφραγίδα που μόλις σηκώθηκε από ένα κομμάτι κερί, όπου έμεινε τυπωμένο το γράμμα Π.'


@scene('2025/03/blog-post_38.html', 'rigma', dict(
    el='Ένα ρήγμα στον χρόνο, κι από εκεί φως.', en='A rift in time, and light coming through.',
    fr='Une faille dans le temps, et de là de la lumière.', de='Ein Riss in der Zeit, und von dort Licht.'))
def rigma(p):
    p.floor()
    cx, cy = 600, 320
    p.ring(cx, cy, 170, w=3); p.ring(cx, cy, 154, w=1.2, op=.5)
    for k in range(12):
        a = k * PI / 6; p.line(p.seg(cx + 140 * math.cos(a), cy + 140 * math.sin(a), cx + 126 * math.cos(a), cy + 126 * math.sin(a), 2), w=2)
    p.line(p.seg(cx, cy, cx, cy - 100, 3), w=3); p.line(p.seg(cx, cy, cx + 70, cy + 30, 3), w=3)
    p.out.append(f'<path class="sk-glow" d="M{cx - 120} {cy - 110} L{cx - 40} {cy - 40} L{cx - 60} {cy + 10} L{cx + 30} {cy + 70} L{cx + 10} {cy + 110} L{cx + 110} {cy + 130} L{cx + 30} {cy + 90} L{cx + 50} {cy + 60} L{cx - 40} {cy - 10} L{cx - 20} {cy - 50} Z" fill="{OCHRE}" opacity=".35" stroke="{OCHRE}" stroke-width="1.5"/>')
    p.line(p.seg(cx, 490, cx, 600, 4), w=2.2)
    return 'Ένα μεγάλο ρολόι με ένα ρήγμα που το διασχίζει διαγώνια· από τη ρωγμή περνά φως.'


@scene('2025/03/blog-post_23.html', 'daxtylo-sta-xeili', dict(
    el='Ένα δάχτυλο στα χείλη που μένει για χρόνια.', en='A finger on the lips that stays for years.',
    fr='Un doigt sur les lèvres qui reste des années.', de='Ein Finger auf den Lippen, der jahrelang bleibt.'))
def daxt(p):
    p.floor()
    person(p, 470, 600, h=.62, look=1)
    p.line([(900, 220), (760, 300), (560, 390)], w=2.8); p.line([(900, 260), (770, 330), (580, 404)], w=2.8)   # το χέρι του ενήλικα
    p.line([(560, 390), (500, 404), (494, 414), (560, 404)], w=2.4)
    p.group('sk-glow'); p.line(p.arc(410, 380, 70, 40, -PI * .5, PI * .5, 10), w=1.4, col=OCHRE, op=.7); p.end()
    p.group('sk-bob', (320, 300)); p.line(p.arc(320, 300, 50, 32, 0, 2 * PI, 18), w=1.6, op=.5); p.line(p.seg(286, 276, 354, 324, 3), w=2, op=.6); p.end()
    return 'Ένα παιδί, και ένα μεγάλο χέρι ενήλικα που του ακουμπά ένα δάχτυλο στα χείλη· δίπλα του ένα συννεφάκι λόγου διαγραμμένο.'


@scene('2025/03/blog-post_27.html', 'veli', dict(
    el='Λέξεις σαν βέλη, κι ένας που δεν απαντά με βέλη.', en='Words like arrows, and one who does not answer with arrows.',
    fr='Des mots comme des flèches, et quelqu’un qui ne répond pas par des flèches.', de='Worte wie Pfeile, und einer, der nicht mit Pfeilen antwortet.'))
def veli(p):
    p.floor()
    p.line(p.poly([(160, 600), (170, 440), (330, 440), (340, 600)], 4), w=2.4)
    person(p, 250, 440, h=.7, look=1, arm=[(290, 300), (340, 280)])
    for k, (y, dy) in enumerate(((280, 0), (320, 10), (250, -6))):
        p.line(p.seg(380, y, 600, y + dy, 6), w=2); p.line([(590, y + dy - 10), (606, y + dy), (590, y + dy + 10)], w=2)
    person(p, 880, 600, h=.95, look=-1, arm=[(830, 330), (790, 300)])
    p.group('sk-sway', (790, 300)); p.line([(790, 300), (784, 260), (794, 240)], w=1.8); p.ring(796, 232, 10, w=1.8, col=OCHRE); p.end()
    return 'Από ένα βήμα ρήτορα ξεκινούν λέξεις σαν βέλη· απέναντι, ένας άνθρωπος δεν απαντά με βέλη, κρατά ένα λουλούδι.'


@scene('2025/03/blog-post_87.html', 'idios-sporos', dict(
    el='Σιωπή και λόγος φυτρώνουν από τον ίδιο σπόρο.', en='Silence and speech sprout from the same seed.',
    fr='Le silence et la parole germent de la même graine.', de='Schweigen und Wort keimen aus demselben Samen.'))
def sporos(p):
    p.line(p.seg(40, 520, 1160, 520, 20), w=2.2, op=.8)
    for k in range(6): p.line(p.seg(100 + k * 180, 560, 160 + k * 180, 560, 2), w=1.2, op=.3)
    p.out.append(f'<ellipse cx="600" cy="560" rx="16" ry="10" fill="{OCHRE}" opacity=".9"/>')
    p.line([(600, 550), (596, 520), (560, 440), (520, 380)], w=2.2)
    p.line([(600, 550), (606, 520), (650, 440), (690, 380)], w=2.2)
    p.group('sk-sway', (520, 380)); p.line(p.arc(500, 360, 40, 26, 0, 2 * PI, 18), w=2); p.text(500, 368, 'λόγος', size=22, anchor='middle'); p.end()
    p.group('sk-bob', (690, 380)); p.line(p.arc(712, 360, 40, 26, 0, 2 * PI, 18), w=2, op=.6); p.end()
    return 'Από έναν σπόρο κάτω από το χώμα βγαίνουν δύο βλαστοί· στον έναν ένα φύλλο γράφει «λόγος», ο άλλος έχει ένα φύλλο άγραφο.'


@scene('2025/03/blog-post_20.html', 'grothia-palami', dict(
    el='Μια γροθιά και μια ανοιχτή παλάμη· η αλλαγή διαλέγει.', en='A fist and an open palm; change chooses.',
    fr='Un poing et une paume ouverte ; le changement choisit.', de='Eine Faust und eine offene Hand; der Wandel wählt.'))
def groth(p):
    p.floor()
    p.line([(380, 600), (370, 420), (360, 340)], w=2.6, op=.5); p.line([(450, 600), (446, 420), (444, 340)], w=2.6, op=.5)
    p.line(p.poly([(340, 340), (350, 270), (460, 266), (466, 340), (340, 340)], 5), w=2.4, op=.5)
    for k in range(3): p.line(p.seg(356, 290 + k * 16, 456, 288 + k * 16, 3), w=1.4, op=.4)
    p.line([(760, 600), (756, 420), (740, 360)], w=2.6); p.line([(830, 600), (834, 420), (850, 360)], w=2.6)
    for fx, L in ((-40, 60), (-14, 84), (14, 82), (40, 62)):
        p.line([(795 + fx - 9, 360), (795 + fx - 10, 360 - L + 10), (795 + fx, 360 - L), (795 + fx + 10, 360 - L + 10), (795 + fx + 9, 360)], w=2.2)
    p.group('sk-sway', (796, 290)); p.line([(796, 300), (792, 250)], w=1.8); p.ring(794, 238, 12, w=2, col=OCHRE); p.end()
    return 'Αριστερά μια σφιγμένη γροθιά σηκωμένη, αχνή· δεξιά μια ανοιχτή παλάμη που κρατά ένα μικρό λουλούδι.'


@scene('2025/03/blog-post_9.html', 'xaos-xari', dict(
    el='Το χάος ως άνοιγμα, πριν γίνει χάρη.', en='Chaos as an opening, before it becomes grace.',
    fr='Le chaos comme ouverture, avant de devenir grâce.', de='Das Chaos als Öffnung, bevor es zur Gnade wird.'))
def xaos(p):
    rr = random.Random(2)
    pts = [(160 + rr.uniform(-60, 60) + k * 12, 360 + rr.uniform(-120, 120)) for k in range(30)]
    p.line(pts, w=1.6, op=.6)
    curve = [(520 + k * 20, 360 - 90 * math.sin(k / 6) * math.exp(-k / 28)) for k in range(32)]
    p.line([pts[-1]] + curve, w=2.4, col=OCHRE)
    p.group('sk-glow'); p.dot(curve[-1][0], curve[-1][1], 6, OCHRE); p.end()
    return 'Αριστερά μια μουτζούρα από μπερδεμένες γραμμές· από μέσα της ξεκινά μια καμπύλη σε ώχρα που ξετυλίγεται ήρεμη προς τα δεξιά.'


@scene('2025/03/blog-post_41.html', 'matia-xoros', dict(
    el='Η ματιά απλώνει τον χώρο.', en='The gaze unfolds space.',
    fr='Le regard déploie l’espace.', de='Der Blick entfaltet den Raum.'))
def matia(p):
    ex, ey = 200, 360
    p.line(p.arc(ex, ey, 60, 30, PI * 1.05, PI * 1.95, 10) + p.arc(ex, ey, 60, 30, PI * .05, PI * .95, 10), w=2.4)
    p.group('sk-blink', (ex, ey)); p.ring(ex, ey, 14, w=2); p.dot(ex, ey, 6); p.end()
    for (x, y) in ((1100, 120), (1100, 600), (700, 240), (700, 480)):
        p.line(p.seg(ex + 50, ey, x, y, 10), w=1.2, op=.4)
    p.line(p.poly([(700, 240), (1100, 120), (1100, 600), (700, 480), (700, 240)], 6), w=2.2)
    p.line(p.poly([(800, 300), (900, 270), (900, 380), (800, 400), (800, 300)], 3), w=1.6, op=.7)
    p.group('sk-glow'); p.line(p.poly([(806, 306), (894, 280), (894, 374), (806, 394), (806, 306)], 3), w=1.6, col=OCHRE); p.end()
    return 'Ένα μάτι αριστερά, και από αυτό ακτίνες που ανοίγουν σε προοπτική ένα δωμάτιο με ένα φωτεινό παράθυρο στο βάθος.'


@scene('2025/03/blog-post_83.html', 'orizontas', dict(
    el='Στη γραμμή όπου θάλασσα και ουρανός είναι ένα.', en='At the line where sea and sky are one.',
    fr='Sur la ligne où mer et ciel ne font qu’un.', de='An der Linie, wo Meer und Himmel eins sind.'))
def oriz(p):
    p.line(p.seg(40, 380, 1160, 380, 22), w=1.4, op=.6)
    for k in range(4): p.line(p.seg(160 + k * 260, 430 + k * 20, 300 + k * 260, 430 + k * 20, 4), w=1.2, op=.35)
    p.line([(40, 600), (500, 560), (1160, 590)], w=2, op=.7)
    person(p, 600, 560, h=.75, look=0)
    p.group('sk-glow'); p.dot(600, 380, 6, OCHRE); p.ring(600, 380, 30, 10, w=1.2, col=OCHRE, op=.7); p.end()
    return 'Ένας άνθρωπος στην ακτή κοιτάζει τον ορίζοντα, εκεί που η θάλασσα και ο ουρανός ενώνονται σε μία γραμμή με ένα φως.'


@scene('2025/03/blog-post_8.html', 'apokrisi', dict(
    el='Κάποιος φάνηκε· κάποιος άνοιξε το παράθυρο.', en='Someone appeared; someone opened the window.',
    fr='Quelqu’un est apparu ; quelqu’un a ouvert la fenêtre.', de='Jemand erschien; jemand öffnete das Fenster.'))
def apok(p):
    p.floor()
    p.line(p.poly([(620, 600), (620, 200), (1000, 200), (1000, 600)], 8), w=2.4)                   # σπίτι
    p.line(p.poly([(600, 200), (810, 80), (1020, 200)], 6), w=2.4)
    p.line(p.poly([(740, 300), (880, 300), (880, 420), (740, 420), (740, 300)], 4), w=2.2)
    p.group('sk-sway', (740, 360)); p.line(p.poly([(740, 300), (690, 314), (690, 410), (740, 420)], 3), w=2); p.end()
    p.group('sk-glow'); p.out.append(f'<rect x="746" y="306" width="128" height="108" fill="{OCHRE}" opacity=".22"/>'); p.end()
    person(p, 330, 600, h=.9, look=1, arm=[(370, 330), (420, 300)])
    p.line(p.seg(420, 300, 420, 270, 2), w=1.6); p.line(p.poly([(406, 270), (434, 270), (430, 304), (410, 304), (406, 270)], 2), w=2); p.dot(420, 288, 4, OCHRE)
    return 'Ένας άνθρωπος με ένα φανάρι στέκεται έξω από ένα σπίτι· ένα παράθυρο ανοίγει και φωτίζεται σαν απάντηση.'


@scene('2025/03/blog-post_75.html', 'xoris-kena', dict(
    el='Πριν τα κενά ανάμεσα στις λέξεις.', en='Before the spaces between words.',
    fr='Avant les espaces entre les mots.', de='Vor den Abständen zwischen den Wörtern.'))
def kena(p):
    p.line(p.poly([(200, 140), (1000, 130), (1010, 520), (190, 530), (200, 140)], 6), w=2.8)
    rows = ['ΕΝΑΡΧΗΗΝΟΛΟΓΟΣ', 'ΚΑΙΟΛΟΓΟΣΗΝΠΡΟΣ', 'ΤΟΝΘΕΟΝΚΑΙΘΕΟΣ', 'ΗΝΟΛΟΓΟΣ']
    for k, r in enumerate(rows):
        p.text(600, 230 + k * 80, r, size=44, italic=False, anchor='middle', spacing=3, op=.85)
    p.line(p.seg(1060, 560, 1120, 470, 3), w=3); p.group('sk-glow'); p.line(p.seg(1040, 590, 1060, 560, 2), w=6, col=OCHRE); p.end()
    return 'Μια πέτρινη πλάκα με επιγραφή σε κεφαλαία γράμματα, όπου οι λέξεις γράφονται συνεχόμενες χωρίς κενά· δίπλα μια σμίλη.'


@scene('2025/03/blog-post_10.html', 'melani-ryaki', dict(
    el='Η γραμμή του μελανιού γίνεται ρυάκι.', en='The line of ink becomes a stream.',
    fr='La ligne d’encre devient ruisseau.', de='Die Tintenlinie wird zum Bach.'))
def melani(p):
    p.line(p.poly([(140, 160), (520, 150), (530, 420), (130, 430), (140, 160)], 5), w=2.4)
    for k in range(4): p.line(p.seg(170, 200 + k * 34, 480 - k * 40, 196 + k * 34, 4), w=1.3, op=.5)
    p.line([(560, 140), (430, 330)], w=2.6); p.line([(560, 140), (600, 90), (590, 150), (560, 140)], w=1.8)   # πένα
    curve = [(430, 336), (480, 380), (560, 420), (680, 470), (820, 520), (980, 560), (1160, 580)]
    p.line(curve, w=2.4, col=OCHRE)
    for k in range(2): p.line([(x, y + 16 + k * 14) for x, y in curve[2:]], w=1.4, op=.4)
    p.group('sk-bob', (900, 520)); p.line([(880, 510), (900, 500), (914, 512)], w=1.8); p.end()
    return 'Μια πένα γράφει πάνω σε ένα φύλλο· η γραμμή του μελανιού βγαίνει από το χαρτί και συνεχίζει σαν ρυάκι προς τα δεξιά.'


if __name__ == '__main__':
    run(S)
