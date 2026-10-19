"""Κοντινά κείμενα: ομοιότητα λεξιλογίου (TF-IDF, συνημίτονο), χωρίς ερμηνεία."""
import math, re, unicodedata
from collections import Counter

def toks(t):
    t = unicodedata.normalize('NFD', t.lower())
    t = ''.join(c for c in t if not unicodedata.combining(c)).replace('ς', 'σ')
    # πρόχειρο κόψιμο καταλήξεων: κρατά τα πρώτα 6 γράμματα κάθε μακριάς λέξης
    return [w[:6] for w in re.findall(r'[α-ωa-z]{5,}', t)]

def neighbours(docs, k=3, floor=0.08):
    """docs: {key: text} -> {key: [(key2, score), ...]}"""
    tf = {d: Counter(toks(x)) for d, x in docs.items()}
    df = Counter(w for c in tf.values() for w in c)
    n = len(docs)
    vec = {}
    for d, c in tf.items():
        v = {w: (1 + math.log(f)) * math.log(n / df[w]) for w, f in c.items() if 1 < df[w] < n * .5}
        norm = math.sqrt(sum(x * x for x in v.values())) or 1
        vec[d] = {w: x / norm for w, x in v.items()}
    out = {}
    for a in vec:
        sc = []
        for b in vec:
            if a == b: continue
            va, vb = vec[a], vec[b]
            if len(vb) < len(va): va, vb = vb, va
            s = sum(x * vb.get(w, 0) for w, x in va.items())
            if s >= floor: sc.append((b, s))
        out[a] = sorted(sc, key=lambda x: -x[1])[:k]
    return out
