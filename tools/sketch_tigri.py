"""Σκίτσο για «Το χρώμα της τίγρης» (15.11.2026, δεύτερη μορφή).
Ψηλά χόρτα που τα στελέχη τους είναι γραμμένες λέξεις συγγένειας («να είσαι ευγνώμων», «είμαστε όλοι ανίψια»…).
Μέσα τους μια τίγρη ξαπλωμένη· οι ρίγες της είναι οι ίδιες λέξεις, γι' αυτό σχεδόν δεν ξεχωρίζει.
Μπροστά, στο χώμα, ένα γράμμα σε ώχρα με θέμα «Για βοήθεια»: δεν έγραψε το χρώμα, το έδειξε."""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pen import Pen, OCHRE, FONT

ALT = ('Ψηλά χόρτα, που τα στελέχη τους είναι γραμμένες λέξεις συγγένειας: να είσαι ευγνώμων, είμαστε όλοι ανίψια, έχεις υποχρέωση. '
       'Ανάμεσά τους μια τίγρη ξαπλωμένη· οι ρίγες της είναι οι ίδιες λέξεις και σχεδόν δεν ξεχωρίζει. '
       'Μπροστά, στο χώμα, ένα γράμμα με θέμα «Για βοήθεια».')

WORDS = ['να είσαι ευγνώμων', 'είμαστε όλοι ανίψια', 'έχεις υποχρέωση', 'αφού είσαι κληρονόμος',
         'οικογένεια', 'ανίψια του θείου', 'ευγνώμων', 'συγγένεια', 'υποχρέωση', 'είμαστε όλοι']


def vtext(p, x, y, s, size=17, op=.4, ang=-90, col='currentColor'):
    p.out.append(f'<text transform="translate({x:.0f} {y:.0f}) rotate({ang:.1f})" font-family="{FONT}" font-style="italic" '
                 f'font-size="{size}" fill="{col}" opacity="{op}">{s}</text>')


def hide(p, pts):
    p.out.append(f'<path d="{p.smooth(pts, True)}" stroke="none" style="fill:var(--bg,#FBF8F2)"/>')


def draw(p):
    r = p.r
    fy = 612
    p.floor(fy, 40, 1160)
    # τα χόρτα: λέξεις όρθιες, σαν στελέχη, ψηλά
    x = 300
    while x < 1165:
        s = ' '.join(r.sample(WORDS, 2))
        vtext(p, x, fy - 3, s, size=r.choice((17, 18, 19, 20)), op=round(r.uniform(.2, .36), 2), ang=r.uniform(-96, -84))
        x += r.uniform(16, 24)
    # η τίγρη, ξαπλωμένη, με το κεφάλι αριστερά
    body = [(520, 470), (560, 424), (620, 404), (700, 412), (790, 404), (880, 410), (960, 432), (1010, 478),
            (1022, 540), (1000, 590), (950, 606), (820, 608), (680, 608), (560, 606), (520, 580)]
    head = [(380, 486), (384, 444), (408, 410), (446, 392), (492, 394), (528, 414), (546, 452), (548, 500),
            (534, 540), (500, 566), (456, 572), (414, 560), (390, 530)]
    paws = [(300, 606), (302, 588), (330, 578), (420, 576), (500, 580), (540, 606)]
    paws2 = [(250, 606), (252, 594), (280, 586), (340, 586)]
    for sh in (body, head, paws):
        hide(p, sh)
    # οι ρίγες: οι ίδιες λέξεις, μέσα στο σώμα (κομμένες από το περίγραμμα)
    p.out.append('<clipPath id="sk-tigri-body"><path d="' + p.smooth(body, True) + '"/></clipPath><g clip-path="url(#sk-tigri-body)">')
    for xx in range(560, 1020, 30):
        vtext(p, xx + r.uniform(-4, 4), 612, ' '.join(r.sample(WORDS, 2)), size=19, op=.58, ang=r.uniform(-100, -80))
    p.out.append('</g>')
    p.out.append('<clipPath id="sk-tigri-head"><path d="' + p.smooth(head, True) + '"/></clipPath><g clip-path="url(#sk-tigri-head)">')
    for xx, ang in ((412, -70), (440, -84), (500, -96), (526, -110)):
        vtext(p, xx, 440, 'ευγνώμων υποχρέωση', size=14, op=.6, ang=ang)
    p.out.append('</g>')
    p.line(body + body[:1], w=2.9, a=.8)
    p.line(head + head[:1], w=2.9, a=.8)
    p.line([(404, 418), (400, 386), (430, 398)], w=2.4); p.line([(496, 396), (522, 376), (528, 410)], w=2.4)   # αυτιά
    for k in range(5):                                                          # χαίτη στα μάγουλα
        y0 = 470 + k * 16
        p.line([(386 - (k % 2) * 8, y0), (376 - (k % 2) * 6, y0 + 8)], w=1.6, op=.7)
    p.line(paws, w=2.6); p.line(paws2, w=2.2, op=.8)
    for xx in (330, 362, 394): p.line([(xx, 590), (xx, 606)], w=1.3, op=.7)
    p.line([(1016, 520), (1066, 500), (1100, 446), (1112, 380), (1134, 352), (1152, 360)], w=2.7)   # ουρά
    for ex in (434, 494):                                                       # μάτια, μισόκλειστα
        p.line(p.arc(ex, 468, 13, 6, 0, math.pi, 8), w=2)
    p.line([(450, 506), (464, 520), (478, 506)], w=2.2)                         # μύτη
    p.line([(464, 520), (464, 534)], w=1.6)
    p.line([(442, 540), (464, 534), (486, 540)], w=1.6)
    for s in (-1, 1):                                                           # μουστάκια
        for k in range(2):
            p.line([(464 + s * 30, 528 + k * 8), (464 + s * 70, 520 + k * 14)], w=1.1, op=.6)
    # το γράμμα, μπροστά στο χώμα (ώχρα)
    gx, gy = 40, 560
    p.group('sk-glow')
    p.line(p.poly([(gx, gy), (gx + 170, gy - 14), (gx + 182, gy + 40), (gx + 10, gy + 54), (gx, gy)], 4), w=2.4, col=OCHRE)
    p.text(gx + 92, gy + 22, 'Για βοήθεια', size=22, italic=True, anchor='middle', col=OCHRE)
    p.end()
    for i in range(3):
        p.line(p.seg(gx + 26 + i * 40, gy + 36 - i * 3, gx + 60 + i * 40, gy + 35 - i * 3, 3), w=1.2, op=.6, col=OCHRE)
    return ALT


def svg():
    p = Pen(seed=sum(map(ord, 'to-chroma-tis-tigris')))
    draw(p)
    return p.svg(ALT)


if __name__ == '__main__':
    out = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'assets', 'sketches', 'to-chroma-tis-tigris.svg')
    open(out, 'w', encoding='utf-8').write(svg()); print(out)
