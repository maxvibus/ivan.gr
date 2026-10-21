"""Σκίτσο για «Η πρόταση πριν από τις λέξεις της» (21.10.2026).
Αριστερά: πάνω σε γραμμή τετραδίου, θόρυβος που καθαρίζει ολόκληρος μαζί και γίνεται φράση (όχι από αριστερά προς τα δεξιά).
Δεξιά: ένα βρέφος έχει ήδη γυρίσει το κεφάλι προς τη μητέρα του· κατεύθυνση χωρίς πρόταση."""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pen import Pen, OCHRE
from sketchbook import person, PI

ALT = ('Αριστερά, πάνω σε μια γραμμή τετραδίου, σκόρπιες κουκκίδες καθαρίζουν όλες μαζί και γίνονται η φράση «η πρόταση πριν από τις λέξεις της»· '
       'δεξιά, ένα μωρό καθισμένο στο πάτωμα έχει ήδη γυρίσει το κεφάλι προς τη μητέρα του.')


def draw(p):
    p.floor(600, 40, 1160)
    # γραμμές τετραδίου
    for y in (300, 380, 460):
        p.line(p.seg(70, y, 640, y, 12), w=1.2, op=.35)
    # θόρυβος: σε όλο το πλάτος της φράσης, στις ίδιες θέσεις όπου θα σταθούν τα γράμματα
    p.group('sk-noise')
    for k in range(110):
        x = 84 + p.r.uniform(0, 330); y = p.r.choice((300, 380)) - p.r.uniform(6, 34)
        if p.r.random() < .55:
            p.dot(x, y, round(p.r.uniform(1.2, 2.6), 1), op=round(p.r.uniform(.35, .8), 2))
        else:
            a = p.r.uniform(0, PI); l = p.r.uniform(5, 12)
            p.line([(x, y), (x + l * math.cos(a), y + l * math.sin(a))], w=1.4, op=.6, a=.4)
    p.end()
    # η φράση, ολόκληρη μαζί
    p.group('sk-words')
    p.text(84, 292, 'η πρόταση πριν', size=44)
    p.text(84, 372, 'από τις λέξεις της', size=44)
    p.end()
    # βρέφος, καθιστό, κοιτάζει δεξιά
    bx, fy = 800, 600
    p.head(bx, 500, 26, glasses=False, look=1)
    p.line([(bx - 14, 524), (bx - 34, 560), (bx - 30, fy - 4), (bx + 40, fy - 2), (bx + 30, 556), (bx + 12, 524)], w=2.6)
    p.line([(bx + 24, 548), (bx + 56, 572), (bx + 66, 566)], w=2.2)          # χέρι που απλώνει λίγο
    # μητέρα, όρθια, κοιτάζει αριστερά προς το παιδί
    person(p, 1010, fy, h=.92, look=-1)
    # το βλέμμα: μια αχνή ώχρα ανάμεσά τους, χωρίς λέξη
    p.group('sk-glow')
    p.line(p.seg(830, 492, 980, 306, 6), w=1.4, col=OCHRE, op=.6)
    p.end()
    return ALT


def svg():
    p = Pen(seed=sum(map(ord, 'protasi-prin-tis-lexeis')))
    draw(p)
    return p.svg(ALT)


if __name__ == '__main__':
    out = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'assets', 'sketches', 'protasi-prin-tis-lexeis.svg')
    open(out, 'w', encoding='utf-8').write(svg()); print(out)
