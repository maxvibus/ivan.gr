"""Σκίτσα δημοσιεύσεων, έκτη σειρά (21.10.2026): Μάρτιος – Μάιος 2025, α΄ μέρος."""
import math, os, sys, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pen import OCHRE
from sketchbook import registry, person, run, PI

S, scene = registry()


@scene('2025/05/blog-post.html', 'diavasi', dict(
    el='Στη μέση της διάβασης, χωρίς να ξέρεις γιατί περνάς.', en='Halfway across, without knowing why you cross.',
    fr='Au milieu du passage, sans savoir pourquoi tu traverses.', de='Mitten auf dem Übergang, ohne zu wissen, warum man geht.'))
def diav(p):
    for k in range(7):
        x = 230 + k * 110
        p.line(p.poly([(x, 610), (x + 70, 610), (x + 60, 640), (x - 10, 640), (x, 610)], 3), w=1.8, op=.7)
    p.line(p.seg(40, 600, 1160, 600, 20), w=1.6, op=.6); p.line(p.seg(40, 650, 1160, 650, 20), w=1.6, op=.6)
    person(p, 620, 620, h=.95, look=1)
    p.line(p.seg(1040, 600, 1040, 300, 6), w=2.4)                                              # φανάρι
    p.line(p.poly([(1010, 300), (1070, 300), (1070, 160), (1010, 160), (1010, 300)], 4), w=2.4)
    p.ring(1040, 196, 18, w=1.6, op=.5)
    p.group('sk-glow'); p.ring(1040, 262, 18, w=2.2, col=OCHRE); p.dot(1040, 262, 7, OCHRE); p.end()
    for k in range(3): p.line(p.seg(820 + k * 30, 200 + k * 40, 1000, 210 + k * 40, 4), w=1.2, op=.25)   # ομίχλη
    return 'Ένας άνθρωπος στη μέση μιας διάβασης πεζών· στην απέναντι πλευρά ένα φανάρι ανάβει, μέσα σε λίγη ομίχλη.'


@scene('2025/04/blog-post_46.html', 'afti-ston-kormo', dict(
    el='Ένα αυτί στον κορμό, και ο κόσμος που μιλά.', en='An ear to the trunk, and the world speaking.',
    fr='Une oreille contre le tronc, et le monde qui parle.', de='Ein Ohr am Stamm, und die Welt, die spricht.'))
def afti(p):
    p.floor()
    tx = 720
    p.line([(tx - 50, 600), (tx - 40, 400), (tx - 60, 200)], w=2.8); p.line([(tx + 50, 600), (tx + 40, 400), (tx + 60, 200)], w=2.8)
    p.line(p.arc(tx, 140, 220, 120, 0, 2 * PI, 32), w=2.2)
    for k in range(3): p.line([(tx - 50 - k * 30, 600), (tx - 110 - k * 40, 640)], w=1.8, op=.6); p.line([(tx + 50 + k * 30, 600), (tx + 110 + k * 40, 640)], w=1.8, op=.6)
    person(p, tx - 120, 600, h=.92, look=1, eyes_closed=True, arm=[(tx - 60, 340), (tx - 52, 300)])
    for i in range(3):
        p.group(f'sk-ripple sk-r{i}', (tx, 330))
        p.line(p.arc(tx, 330, 70, 90, -PI * .35, PI * .35, 8), w=1.6, col=OCHRE, op=.8)
        p.end()
    return 'Ένας άνθρωπος με κλειστά μάτια ακουμπά το αυτί του σε έναν κορμό δέντρου· από μέσα απλώνονται απαλοί κυματισμοί ήχου.'


@scene('2025/04/blog-post_28.html', 'syn', dict(
    el='Κανείς δεν χτίζει μόνος απέναντι στον κόσμο.', en='No one builds alone against the world.',
    fr='Personne ne bâtit seul face au monde.', de='Niemand baut allein gegen die Welt.'))
def syn(p):
    p.floor()
    p.line(p.poly([(480, 600), (480, 400), (720, 400), (720, 600)], 6), w=2.4)                  # σκελετός σπιτιού
    p.line(p.seg(470, 400, 600, 300, 5), w=2.6)                                                 # το μισό δοκάρι της σκεπής
    person(p, 360, 600, h=.9, look=1, arm=[(420, 330), (560, 300)])
    p.group('sk-bob', (620, 300)); p.line(p.seg(560, 300, 700, 300, 5), w=4, col=OCHRE); p.end()       # δοκάρι που σηκώνουν
    person(p, 840, 600, h=.9, look=-1, arm=[(880, 360), (760, 310)])
    p.line(p.seg(760, 310, 740, 290, 2), w=2.4); p.line(p.poly([(726, 278), (752, 270), (756, 284), (730, 292), (726, 278)], 2), w=2.2)   # σφυρί
    return 'Δύο άνθρωποι, ένας από κάθε πλευρά, σηκώνουν μαζί ένα δοκάρι για τη σκεπή ενός μισοχτισμένου σπιτιού.'


@scene('2025/04/blog-post_26.html', 'eimai', dict(
    el='Έξω από την αφήγηση, περισσότερο εσύ.', en='Outside the narrative, more yourself.',
    fr='Hors du récit, davantage toi-même.', de='Außerhalb der Erzählung, mehr du selbst.'))
def eimai(p):
    p.floor()
    p.line([(140, 600), (520, 590), (540, 570), (520, 550), (500, 570), (520, 590)], w=2.4)     # ρολό που ξετυλίχτηκε
    for k in range(5): p.line(p.seg(180 + k * 60, 580, 220 + k * 60, 578, 2), w=1.4, op=.5)
    for k, t in enumerate(('ρόλος', 'όνομα', 'προσδοκία')):
        x, y = 200 + k * 110, 520 - (k % 2) * 30
        p.group('sk-sway', (x, y)); p.line(p.poly([(x - 44, y - 18), (x + 44, y - 18), (x + 44, y + 12), (x - 44, y + 12), (x - 44, y - 18)], 3), w=1.4, op=.5)
        p.text(x, y + 2, t, size=17, anchor='middle', op=.6); p.end()
    person(p, 780, 600, h=1, look=1, arm=[(830, 330), (900, 260)])
    p.group('sk-glow'); p.ring(780, 270, 60, w=1.4, col=OCHRE, op=.75); p.end()
    return 'Πίσω, ένα ρολό χαρτιού ξετυλιγμένο στο έδαφος και ετικέτες που γράφουν «ρόλος», «όνομα», «προσδοκία»· μπροστά, ένας άνθρωπος όρθιος με σηκωμένο χέρι.'


@scene('2025/04/blog-post_22.html', 'skalopatia', dict(
    el='Τα σκαλοπάτια της συνείδησης, και στο τελευταίο μια κουβέντα.', en='The steps of consciousness, and on the last one a conversation.',
    fr='Les marches de la conscience, et sur la dernière une conversation.', de='Die Stufen des Bewusstseins, und auf der letzten ein Gespräch.'))
def skal(p):
    p.floor()
    xs = [120, 340, 560, 780, 1000]
    for k in range(4):
        x0, x1, y = xs[k], xs[k + 1], 600 - (k + 1) * 80
        p.line(p.poly([(x0, 600 - k * 80), (x0, y), (x1, y)], 4), w=2.4)
    p.line(p.seg(1000, 280, 1000, 600, 6), w=2.4)
    # φωτιά, κίονας, βιβλίο, οθόνη
    p.group('sk-flicker', (230, 510)); p.out.append(f'<path d="M230 470 Q250 495 230 512 Q210 495 230 470Z" fill="{OCHRE}" stroke="{OCHRE}"/>'); p.end()
    p.line(p.seg(215, 520, 245, 520, 2), w=2)
    p.line(p.seg(440, 440, 440, 360, 3), w=2.2); p.line(p.seg(460, 440, 460, 360, 3), w=2.2); p.line(p.seg(428, 356, 472, 356, 2), w=2.4)
    p.line([(620, 352), (660, 340), (700, 352)], w=2); p.line(p.seg(620, 352, 700, 352, 2), w=2)
    p.line(p.poly([(850, 270), (930, 270), (930, 230), (850, 230), (850, 270)], 2), w=2)
    person(p, 860, 280, h=.48, look=1); person(p, 950, 280, h=.48, look=-1)
    return 'Μια σκάλα με τέσσερα σκαλοπάτια· πάνω τους μια φωτιά, ένας κίονας, ένα βιβλίο και μια οθόνη, και στο τελευταίο δύο άνθρωποι που μιλούν.'


@scene('2025/04/the-invitation-of-consciousness-towards.html', 'invitation-envelope', dict(
    el='Ένας φάκελος ανοιχτός, κι από μέσα φως.', en='An opened envelope, and light inside.',
    fr='Une enveloppe ouverte, et de la lumière dedans.', de='Ein geöffneter Umschlag, und darin Licht.'))
def inv_en(p):
    cx, cy = 600, 400
    p.line(p.poly([(cx - 220, cy - 120), (cx + 220, cy - 120), (cx + 220, cy + 140), (cx - 220, cy + 140), (cx - 220, cy - 120)], 6), w=2.8)
    p.line(p.poly([(cx - 220, cy + 140), (cx, cy), (cx + 220, cy + 140)], 6), w=2)
    p.line(p.poly([(cx - 220, cy - 120), (cx, cy - 300), (cx + 220, cy - 120)], 6), w=2.4)          # ανοιχτό καπάκι
    p.group('sk-glow'); p.out.append(f'<path d="M{cx - 160} {cy - 120} L{cx} {cy - 240} L{cx + 160} {cy - 120} Z" fill="{OCHRE}" opacity=".22"/>'); p.dot(cx, cy - 150, 6, OCHRE); p.end()
    p.line(p.seg(80, 600, 1120, 600, 20), w=1.6, op=.5)
    return 'A large envelope lies open; from inside it rises a soft triangle of light.'


@scene('2025/04/beyond-2025.html', 'prosklisi-syneidisis', dict(
    el='Ένα φανάρι στο σταυροδρόμι της επιστήμης, της τεχνικής και του βιώματος.', en='A lantern at the crossroads of science, technique and lived experience.',
    fr='Une lanterne au carrefour de la science, de la technique et du vécu.', de='Eine Laterne an der Kreuzung von Wissenschaft, Technik und Erleben.'))
def prosk(p):
    p.line([(600, 640), (600, 470)], w=2, op=.6); p.line([(600, 470), (240, 220)], w=2, op=.6); p.line([(600, 470), (960, 220)], w=2, op=.6)
    # μικροσκόπιο, γρανάζι, καρδιά στις τρεις άκρες
    p.line(p.seg(220, 220, 250, 150, 3), w=2.6); p.line(p.seg(200, 230, 270, 230, 3), w=2.4); p.ring(250, 140, 10, w=2)
    gx, gy = 980, 190
    p.ring(gx, gy, 30, w=2.4); p.ring(gx, gy, 10, w=2)
    for k in range(8): a = k * PI / 4; p.line(p.seg(gx + 30 * math.cos(a), gy + 30 * math.sin(a), gx + 42 * math.cos(a), gy + 42 * math.sin(a), 2), w=3)
    p.line([(600, 660), (580, 640), (580, 620), (600, 628), (620, 620), (620, 640), (600, 660)], w=2.2)
    person(p, 600, 470, h=.62, look=0, arm=[(640, 300), (660, 280)])
    p.line(p.seg(660, 280, 660, 250, 2), w=1.6)
    p.group('sk-sway', (660, 250)); p.line(p.poly([(645, 252), (675, 252), (672, 292), (648, 292), (645, 252)], 3), w=2); p.dot(660, 272, 5, OCHRE); p.end()
    p.group('sk-glow'); p.ring(660, 272, 26, w=1.2, col=OCHRE, op=.7); p.end()
    return 'Ένας άνθρωπος με ένα φανάρι στέκεται εκεί όπου τρεις δρόμοι χωρίζουν· στο τέλος του καθενός ένα μικροσκόπιο, ένα γρανάζι και μια καρδιά.'


@scene('2025/04/blog-post.html', 'voi', dict(
    el='Η κραυγή που ανεβαίνει είναι ήδη βοήθεια.', en='The cry that rises is already help.',
    fr='Le cri qui monte est déjà secours.', de='Der Schrei, der aufsteigt, ist schon Hilfe.'))
def voi(p):
    p.floor()
    person(p, 600, 600, h=.9, look=0, arm=[(640, 280), (620, 250)])
    p.line([(570, 330), (560, 280), (580, 252)], w=2.4)
    for i in range(3):
        p.group(f'sk-ripple sk-r{i}', (600, 240))
        p.line(p.arc(600, 240, 70, 40, PI * 1.15, PI * 1.85, 10), w=1.6, op=.8)
        p.end()
    for k, (x, y) in enumerate(((360, 90), (520, 60), (700, 80), (860, 110), (450, 140))):
        p.dot(x, y, 2.4 if k else 3.2, OCHRE if k == 2 else 'currentColor', op=.8)
    p.group('sk-glow'); p.ring(700, 80, 14, w=1.2, col=OCHRE); p.end()
    return 'Ένας άνθρωπος με τα χέρια χωνί στο στόμα φωνάζει προς τα πάνω· κύματα φωνής ανεβαίνουν προς τα αστέρια, όπου ένα ανάβει.'


@scene('2025/03/blog-post_74.html', 'mia-grammi', dict(
    el='Μέσα στην ορχήστρα, η προσοχή ακολουθεί μία γραμμή.', en='Within the orchestra, attention follows one line.',
    fr='Dans l’orchestre, l’attention suit une seule ligne.', de='Im Orchester folgt die Aufmerksamkeit einer einzigen Linie.'))
def grammi(p):
    for st in range(3):
        y0 = 150 + st * 140
        for k in range(5): p.line(p.seg(120, y0 + k * 12, 1080, y0 + k * 12, 20), w=1, op=.4)
    rr = random.Random(4)
    for st in range(3):
        y0 = 150 + st * 140
        prev = None
        for k in range(14):
            x = 160 + k * 66; y = y0 + rr.choice((0, 6, 12, 18, 24, 30, 36, 42))
            hl = st == 1
            p.out.append(f'<ellipse cx="{x}" cy="{y}" rx="7" ry="5" fill="{OCHRE if hl else "currentColor"}" opacity="{1 if hl else .45}" transform="rotate(-20 {x} {y})"/>')
            p.line(p.seg(x + 6, y, x + 6, y - 34, 2), w=1.4, col=OCHRE if hl else 'currentColor', op=1 if hl else .45)
            if hl and prev: p.out.append(f'<path class="sk-glow" d="M{prev[0]} {prev[1]} L{x} {y}" stroke="{OCHRE}" stroke-width="1" opacity=".5"/>')
            if hl: prev = (x, y)
    p.line(p.arc(110, 300, 30, 50, PI * .5, PI * 1.6, 12), w=2.4)                                  # αυτί
    p.line(p.arc(116, 300, 14, 24, PI * .5, PI * 1.5, 8), w=1.6)
    return 'Τρία πεντάγραμμα με νότες, σαν παρτιτούρα ορχήστρας· οι νότες της μεσαίας γραμμής λάμπουν και ένα αυτί στην άκρη την ακολουθεί.'


@scene('2025/03/blog-post_21.html', 'symmathites', dict(
    el='Μάτια που σε ξέρουν από τότε.', en='Eyes that have known you since then.',
    fr='Des yeux qui te connaissent depuis ce temps-là.', de='Augen, die dich seit damals kennen.'))
def symm(p):
    p.floor()
    for x in (380, 820):
        p.line(p.poly([(x - 120, 470), (x + 120, 470)], 4), w=2.4); p.line(p.seg(x - 110, 470, x - 110, 600, 4), w=2.2); p.line(p.seg(x + 110, 470, x + 110, 600, 4), w=2.2)
    for k, (x, look) in enumerate(((440, 1), (760, -1))):
        p.line(p.arc(x, 300, 80, 90, 0, 2 * PI, 30), w=2.6)
        ex = x + look * 18
        p.group('sk-blink', (ex, 290))
        p.line(p.arc(ex - 22, 290, 14, 10, 0, 2 * PI, 12), w=2); p.line(p.arc(ex + 22, 290, 14, 10, 0, 2 * PI, 12), w=2)
        p.dot(ex - 22 + look * 5, 290, 5); p.dot(ex + 22 + look * 5, 290, 5)
        p.end()
        p.group('sk-blink-c', (ex, 290)); p.line(p.arc(ex - 22, 292, 14, 5, 0, PI, 8), w=2); p.line(p.arc(ex + 22, 292, 14, 5, 0, PI, 8), w=2); p.end()
        p.line(p.arc(x + look * 10, 340, 18, 6, 0, PI, 8), w=1.8)
    p.out.append(f'<path class="sk-glow" d="M495 290 L705 290" stroke="{OCHRE}" stroke-width="1.6" stroke-dasharray="3 8"/>')
    return 'Δύο πρόσωπα πάνω από δύο παλιά θρανία κοιτάζονται στα μάτια· μια διακεκομμένη γραμμή φωτός ενώνει τα βλέμματά τους.'


@scene('2025/03/blog-post_13.html', 'sfaires', dict(
    el='Δύο σφαίρες, απαλά η μία δίπλα στην άλλη.', en='Two spheres, gently side by side.',
    fr='Deux sphères, doucement l’une à côté de l’autre.', de='Zwei Kugeln, sanft nebeneinander.'))
def sfair(p):
    p.floor()
    for k, (x, r) in enumerate(((500, 120), (730, 110))):
        p.group('sk-bob', (x, 600 - r)) if k == 0 else p.group('sk-sway', (x, 600))
        p.ring(x, 600 - r, r, w=2.8)
        p.line(p.arc(x - r * .3, 600 - r * 1.3, r * .35, r * .2, PI * 1.1, PI * 1.7, 8), w=1.4, op=.5)
        p.end()
        p.out.append(f'<ellipse cx="{x}" cy="602" rx="{r * .8:.0f}" ry="8" fill="currentColor" opacity=".08"/>')
    p.group('sk-glow'); p.dot(616, 488, 5, OCHRE); p.ring(616, 488, 16, w=1.2, col=OCHRE, op=.7); p.end()
    return 'Δύο σφαίρες χωρίς πρόσωπο ακουμπούν απαλά η μία στην άλλη· εκεί που αγγίζονται, ένα μικρό φως.'


@scene('2025/03/blog-post_73.html', 'exo-apo-to-kadro', dict(
    el='Έξω από το κάδρο της ιστορίας.', en='Out of the frame of history.',
    fr='Hors du cadre de l’histoire.', de='Aus dem Rahmen der Geschichte.'))
def kadro(p):
    p.floor()
    fx, fy, fw, fh = 260, 140, 420, 340
    p.line(p.poly([(fx, fy), (fx + fw, fy), (fx + fw, fy + fh), (fx, fy + fh), (fx, fy)], 6), w=3)
    p.line(p.poly([(fx + 16, fy + 16), (fx + fw - 16, fy + 16), (fx + fw - 16, fy + fh - 16), (fx + 16, fy + fh - 16), (fx + 16, fy + 16)], 6), w=1.4, op=.5)
    for k in range(4):                                                                        # σκηνή μάχης/ιστορίας, αχνή
        x = fx + 70 + k * 80
        p.line([(x, fy + 300), (x, fy + 200)], w=1.6, op=.4); p.ring(x, fy + 186, 14, w=1.4, op=.4)
        p.line([(x, fy + 220), (x + 30, fy + 150)], w=1.4, op=.4)
    p.line(p.seg(fx + 40, fy + 120, fx + 380, fy + 110, 6), w=1.2, op=.3)
    person(p, 820, 600, h=.95, look=1, arm=[(870, 380), (930, 400)])
    p.group('sk-glow'); p.out.append(f'<path d="M{fx + fw} {fy + fh - 40} Q 740 560 790 590" stroke="{OCHRE}" stroke-width="1.6" fill="none" stroke-dasharray="4 7"/>'); p.end()
    return 'Ένας μεγάλος πίνακας με μια αχνή ιστορική σκηνή· μια διακεκομμένη γραμμή βγαίνει από το κάδρο ως έναν άνθρωπο που στέκεται πια έξω του.'


@scene('2025/03/blog-post_19.html', 'milo', dict(
    el='Ένα μήλο απλωμένο, όχι κρυμμένο.', en='An apple held out, not hidden.',
    fr='Une pomme tendue, non cachée.', de='Ein Apfel, hingehalten, nicht versteckt.'))
def milo(p):
    p.floor()
    tx = 600
    p.line([(tx - 30, 600), (tx - 24, 360), (tx - 40, 260)], w=2.8); p.line([(tx + 30, 600), (tx + 26, 360), (tx + 44, 260)], w=2.8)
    p.group('sk-sway', (tx, 260)); p.line(p.arc(tx, 190, 220, 120, 0, 2 * PI, 34), w=2.2)
    for k in range(5): p.ring(tx - 150 + k * 75, 190 + (k % 2) * 40, 10, w=1.6, op=.6)
    p.end()
    person(p, 380, 600, h=.88, look=1, arm=[(430, 340), (500, 330)])
    person(p, 820, 600, h=.88, look=-1)
    p.group('sk-glow'); p.ring(516, 326, 16, w=2.4, col=OCHRE); p.line([(516, 310), (520, 296)], w=1.6); p.end()
    return 'Κάτω από μια μηλιά, δύο άνθρωποι· ο ένας απλώνει φανερά ένα μήλο προς τον άλλον.'


@scene('2025/03/blog-post_96.html', 'ion-ion', dict(
    el='Ό,τι πηγαίνει και ό,τι μένει: η ροή και η πέτρα στο ίδιο νερό.', en='What goes and what stays: the flow and the stone in the same water.',
    fr='Ce qui va et ce qui demeure : le flux et la pierre dans la même eau.', de='Was geht und was bleibt: der Fluss und der Stein im selben Wasser.'))
def ion(p):
    for k in range(6):
        y = 300 + k * 50
        p.group('sk-sway' if k % 2 else 'sk-bob', (600, y))
        p.line([(60, y), (300, y - 10), (520, y + 4), (560, y - 30), (640, y - 30), (680, y + 4), (900, y - 8), (1140, y)], w=1.6, op=.6)
        p.end()
    p.line(p.arc(600, 420, 80, 50, 0, 2 * PI, 24), w=2.8)
    p.line(p.arc(580, 400, 30, 14, PI * 1.1, PI * 1.8, 8), w=1.4, op=.5)
    p.group('sk-glow'); p.dot(600, 360, 5, OCHRE); p.end()
    p.text(300, 200, 'ἰών', size=40, op=.8); p.text(860, 200, 'ἴον', size=40, op=.8)
    return 'Ένα ποτάμι κυλά γύρω από μια πέτρα που μένει ακίνητη· πάνω γράφει «ἰών» και «ἴον».'


@scene('2025/03/blog-post_81.html', 'kvanto', dict(
    el='Κύμα που γίνεται κόκκος, και ξανά κύμα.', en='A wave becoming a grain, and a wave again.',
    fr='Une onde qui devient grain, puis de nouveau onde.', de='Eine Welle, die zum Korn wird, und wieder zur Welle.'))
def kvanto(p):
    pts = []
    for i in range(0, 121):
        x = 60 + i * 9; env = math.exp(-((x - 600) / 230) ** 2)
        pts.append((x, 360 - 120 * env * math.sin((x - 600) / 26)))
    p.line(pts, w=2.4)
    p.line(p.seg(60, 360, 1140, 360, 20), w=1, op=.3)
    p.group('sk-glow'); p.dot(600, 360, 9, OCHRE); p.ring(600, 360, 26, w=1.4, col=OCHRE, op=.7); p.end()
    p.text(600, 560, 'ἰέναι', size=40, anchor='middle', op=.7)
    return 'Ένα κύμα που πυκνώνει στη μέση και γίνεται ένας φωτεινός κόκκος, πριν απλωθεί ξανά· από κάτω η λέξη «ἰέναι».'


@scene('2025/03/blog-post_18.html', 'grammata-neyrones', dict(
    el='Γράμματα που ενώνονται σαν νευρώνες.', en='Letters joining like neurons.',
    fr='Des lettres qui se relient comme des neurones.', de='Buchstaben, die sich wie Neuronen verbinden.'))
def neyr(p):
    rr = random.Random(9)
    letters = 'ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ'
    pts = []
    for i, ch in enumerate(letters):
        a = i / len(letters) * 2 * PI; r = 190 + rr.uniform(-40, 60)
        pts.append((600 + r * 1.4 * math.cos(a), 360 + r * math.sin(a), ch))
    for i, (x, y, ch) in enumerate(pts):
        for j in (i + 3, i + 7):
            x2, y2, _ = pts[j % len(pts)]
            p.out.append(f'<path d="M{x:.0f} {y:.0f} Q600 360 {x2:.0f} {y2:.0f}" stroke="currentColor" stroke-width="1" fill="none" opacity=".18"/>')
    for i, (x, y, ch) in enumerate(pts):
        p.group('sk-bob' if i % 3 == 0 else 'sk-sway', (x, y))
        p.text(f'{x:.0f}', f'{y + 10:.0f}', ch, size=30, italic=False, anchor='middle', col=OCHRE if ch in 'ΛΟΓ' else 'currentColor', op=.9)
        p.end()
    return 'Τα είκοσι τέσσερα γράμματα του ελληνικού αλφαβήτου σε κύκλο, ενωμένα μεταξύ τους με λεπτές καμπύλες σαν δίκτυο νευρώνων· τα Λ, Ο και Γ λάμπουν.'


if __name__ == '__main__':
    run(S)
