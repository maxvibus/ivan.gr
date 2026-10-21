"""Κοινά για κάθε σειρά σκίτσων: μητρώο σκηνών, ανθρώπινη φιγούρα, εγγραφή στο content/sketches.json."""
import math, json, os
from pen import Pen, OCHRE

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PI = math.pi


def registry():
    S = {}
    def scene(path, slug, cap):
        def deco(fn):
            S[path] = (slug, cap, fn)
            return fn
        return deco
    return S, scene


def person(p, x, fy=600, h=1.0, look=0, glasses=False, arm=None, sit=False, eyes_closed=False):
    """Όρθια (ή καθιστή) φιγούρα με λίγες γραμμές. x: κέντρο, fy: πάτωμα, h: κλίμακα.
    arm: λίστα σημείων για το ένα χέρι από τον ώμο, αλλιώς κρέμεται."""
    s = h
    hy = fy - (330 if not sit else 250) * s
    p.head(x, hy, 34 * s, glasses=glasses, look=look, eyes_closed=eyes_closed)
    sh = hy + 36 * s
    if not sit:
        hip = fy - 150 * s
        p.line([(x - 6 * s, sh), (x - 30 * s, sh + 14 * s), (x - 34 * s, sh + 70 * s), (x - 26 * s, hip)], w=2.8)   # ώμος, πλευρά
        p.line([(x + 8 * s, sh), (x + 32 * s, sh + 14 * s), (x + 34 * s, sh + 70 * s), (x + 26 * s, hip)], w=2.8)
        p.line([(x - 26 * s, hip), (x - 30 * s, hip + 80 * s), (x - 32 * s, fy)], w=2.6)                            # πόδια
        p.line([(x - 4 * s, hip + 10 * s), (x - 8 * s, hip + 80 * s), (x - 10 * s, fy)], w=2.4)
        p.line([(x + 26 * s, hip), (x + 28 * s, hip + 80 * s), (x + 32 * s, fy)], w=2.6)
        p.line([(x + 4 * s, hip + 10 * s), (x + 8 * s, hip + 80 * s), (x + 10 * s, fy)], w=2.4)
        p.line([(x - 4 * s, hip + 10 * s), (x + 4 * s, hip + 10 * s)], w=2)
        p.line([(x - 40 * s, fy), (x - 8 * s, fy)], w=3); p.line([(x + 10 * s, fy), (x + 42 * s, fy)], w=3)
    else:
        p.line([(x - 8 * s, sh), (x - 22 * s, sh + 100 * s), (x - 20 * s, sh + 150 * s)], w=2.8)
        p.line([(x + 10 * s, sh), (x + 24 * s, sh + 100 * s), (x + 30 * s, sh + 150 * s)], w=2.8)
        p.line([(x - 20 * s, sh + 150 * s), (x + 70 * s, sh + 152 * s), (x + 76 * s, fy)], w=2.6)
        p.line([(x + 30 * s, sh + 150 * s), (x + 96 * s, sh + 146 * s), (x + 100 * s, fy)], w=2.6)
    if arm:
        p.line([(x + 32 * s, sh + 16 * s)] + arm, w=2.6)
    else:
        p.line([(x + 32 * s, sh + 16 * s), (x + 42 * s, sh + 80 * s), (x + 40 * s, sh + 140 * s)], w=2.4)
    p.line([(x - 30 * s, sh + 16 * s), (x - 42 * s, sh + 80 * s), (x - 40 * s, sh + 140 * s)], w=2.4)
    return sh


def run(S):
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
