#!/usr/bin/env python3
"""ivan.gr — στατικός ιστότοπος από τα κείμενα (content/*.json).
Κρατά τις παλιές διευθύνσεις του Blogger (/2026/09/x.html, /p/x.html) ώστε κανένας σύνδεσμος να μη χαθεί.
Όλοι οι εσωτερικοί σύνδεσμοι είναι σχετικοί, ώστε ο ιστότοπος να δουλεύει και σε προεπισκόπηση με πρόθεμα."""
import json, os, re, html, shutil, posixpath, datetime
from urllib.parse import urlparse
from bs4 import BeautifulSoup

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = ROOT  # ο ιστότοπος ζει στη ρίζα του αποθετηρίου
SITE = 'https://www.ivan.gr'
data = json.load(open(os.path.join(ROOT, 'content', 'texts.json'), encoding='utf-8'))
fixes = json.load(open(os.path.join(ROOT, 'content', 'fixes.json'), encoding='utf-8'))
manual = json.load(open(os.path.join(ROOT, 'content', 'manual-translations.json'), encoding='utf-8'))

L = {
 'el': dict(name='ΕΛ', sub='Φιλοσοφία · Θεολογία · Γλώσσα',
   intro='Κείμενα φιλοσοφίας, θεολογίας και γλώσσας, που διαμορφώνονται μέσα από γραπτό διάλογο με γλωσσικά μοντέλα.',
   latest='Νεότερο', recent='Πρόσφατα', all='Όλα τα κείμενα', search='Αναζήτηση', none='Τίποτα δεν βρέθηκε.', read='Ανάγνωση',
   prev='Προηγούμενο', next='Επόμενο', index='Όλα τα κείμενα', down='Στα κείμενα', author='Ιβάν Δ. Αθανασόπουλος',
   months=['Ιανουαρίου','Φεβρουαρίου','Μαρτίου','Απριλίου','Μαΐου','Ιουνίου','Ιουλίου','Αυγούστου','Σεπτεμβρίου','Οκτωβρίου','Νοεμβρίου','Δεκεμβρίου'],
   short=['Ιαν','Φεβ','Μαρ','Απρ','Μαΐ','Ιουν','Ιουλ','Αυγ','Σεπ','Οκτ','Νοε','Δεκ']),
 'en': dict(name='EN', sub='Philosophy · Theology · Language',
   intro='Texts on philosophy, theology and language, shaped through written dialogue with language models.',
   latest='Latest', recent='Recent', all='All texts', search='Search', none='Nothing found.', read='Read',
   prev='Previous', next='Next', index='All texts', down='To the texts', author='Ivan D. Athanasopoulos',
   months=['January','February','March','April','May','June','July','August','September','October','November','December'],
   short=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']),
 'fr': dict(name='FR', sub='Philosophie · Théologie · Langage',
   intro='Des textes de philosophie, de théologie et de langage, façonnés au fil d’un dialogue écrit avec des modèles de langage.',
   latest='Le plus récent', recent='Récents', all='Tous les textes', search='Rechercher', none='Aucun résultat.', read='Lire',
   prev='Précédent', next='Suivant', index='Tous les textes', down='Vers les textes', author='Ivan D. Athanasopoulos',
   months=['janvier','février','mars','avril','mai','juin','juillet','août','septembre','octobre','novembre','décembre'],
   short=['janv.','févr.','mars','avr.','mai','juin','juil.','août','sept.','oct.','nov.','déc.']),
 'de': dict(name='DE', sub='Philosophie · Theologie · Sprache',
   intro='Texte zu Philosophie, Theologie und Sprache, entstanden im schriftlichen Dialog mit Sprachmodellen.',
   latest='Neuester Text', recent='Neu', all='Alle Texte', search='Suchen', none='Nichts gefunden.', read='Lesen',
   prev='Vorheriger', next='Nächster', index='Alle Texte', down='Zu den Texten', author='Ivan D. Athanasopoulos',
   months=['Januar','Februar','März','April','Mai','Juni','Juli','August','September','Oktober','November','Dezember'],
   short=['Jan.','Feb.','März','Apr.','Mai','Juni','Juli','Aug.','Sept.','Okt.','Nov.','Dez.']),
}
LANGS = ['el', 'en', 'fr', 'de']
HOME = {'el': 'index.html', 'en': 'p/en.html', 'fr': 'p/fr.html', 'de': 'p/de.html'}
E = html.escape

def path_of(url):
    return urlparse(url).path.lstrip('/')

def rel(frm, to):
    """σχετικός σύνδεσμος από το αρχείο frm στο αρχείο to (και τα δύο από τη ρίζα)."""
    if to.endswith('index.html'):
        d = posixpath.dirname(to)
        r = posixpath.relpath(d or '.', posixpath.dirname(frm) or '.')
        return './' if r == '.' else r + '/'
    return posixpath.relpath(to, posixpath.dirname(frm) or '.')

def dparts(s):
    y, m, d = int(s[:4]), int(s[5:7]), int(s[8:10])
    return y, m, d

def dlong(s, lang):
    y, m, d = dparts(s); M = L[lang]['months'][m-1]
    if lang == 'en': return f'{M} {d}, {y}'
    if lang == 'de': return f'{d}. {M} {y}'
    return f'{d} {M} {y}'

def dshort(s, lang):
    y, m, d = dparts(s); M = L[lang]['short'][m-1]
    return f'{M} {d}' if lang == 'en' else (f'{d}. {M}' if lang == 'de' else f'{d} {M}')

def norm(s):
    import unicodedata
    s = unicodedata.normalize('NFD', s)
    s = ''.join(c for c in s if not unicodedata.combining(c))
    return s.lower().replace('ς', 'σ')

def clean(h, frm):
    soup = BeautifulSoup(h, 'html.parser')
    for t in soup.find_all(True):
        for a in ('style', 'class', 'id', 'dir', 'align', 'face', 'size', 'color'):
            if a in t.attrs and not (a == 'class' and t.name == 'div' and 'ivan-translation' in ' '.join(t.get('class', []))):
                if a == 'class' and 'ivan-translation-note' in ' '.join(t.get('class', [])): continue
                del t.attrs[a]
        if t.name in ('span', 'font'): t.unwrap()
    for a in soup.find_all('a', href=True):
        u = urlparse(a['href'])
        if u.netloc in ('www.ivan.gr', 'ivan.gr', 'ivanathanasopoulos.blogspot.com') and u.path.endswith('.html'):
            a['href'] = rel(frm, u.path.lstrip('/')) + (('#' + u.fragment) if u.fragment else '')
        elif u.netloc:
            a['rel'] = 'noopener'
    out = str(soup)
    out = re.sub(r'<p>(\s|&nbsp;| |<br/?>)*</p>', '', out)
    return out

def text_of(h):
    return re.sub(r'\s+', ' ', BeautifulSoup(h, 'html.parser').get_text(' ')).strip()

def excerpt(t, n=320):
    if len(t) <= n: return t
    c = t[:n]; i = max(c.rfind('. '), c.rfind('; '), c.rfind('· '))
    return c[:i+1] if i > n*0.5 else re.sub(r'\s+\S*$', '', c) + '…'

def apply_fixes(item):
    for f in fixes:
        if f['url'] == item['url']:
            for old, new in f['replace']:
                if old not in item['html']: raise SystemExit('fix not found: ' + item['url'] + ' :: ' + old)
                item['html'] = item['html'].replace(old, new)

# --- συλλογή κειμένων -------------------------------------------------------
posts = sorted(data['posts'], key=lambda p: p['published'], reverse=True)
for p in posts: p['lang'] = 'el'; p['path'] = path_of(p['url']); apply_fixes(p)
by_url = {p['url']: p for p in posts}
trans = {}   # ελληνικό url -> {lang: σελίδα}
orphans = []
for g in data['pages']:
    if 'ivan-language-index' in g['html'][:300]: continue
    if g['url'] in manual:
        orig, lg = manual[g['url']]
    else:
        m = re.search(r'lang="(en|fr|de)"', g['html'][:400])
        if not m: raise SystemExit('unknown page: ' + g['url'])
        lg = m.group(1)
        o = re.search(r'ivan-translation-note.*?href="([^"]+)"', g['html'], re.S)
        orig = o.group(1).replace('http://', 'https://') if o else None
    g['lang'] = lg; g['path'] = path_of(g['url']); apply_fixes(g)
    if orig and orig not in by_url and orig.replace('https://www.', 'https://') in by_url: orig = orig.replace('https://www.', 'https://')
    if orig in by_url:
        g['orig'] = orig; g['published'] = by_url[orig]['published']
        trans.setdefault(orig, {})[g['lang']] = g
    else:
        g['orig'] = None; orphans.append(g)

# --- κοινά κομμάτια ---------------------------------------------------------
def head(frm, lang, title, desc, canon_path, alts=None, extra=''):
    css = rel(frm, 'assets/site.css'); ico = rel(frm, 'assets/icon-32.png'); ico180 = rel(frm, 'assets/icon-180.png')
    fr = rel(frm, 'assets/fonts/ebgaramond-regular.woff2')
    alt = ''
    for l, pth in (alts or {}).items():
        alt += f'<link rel="alternate" hreflang="{l}" href="{SITE}/{pth.replace("index.html","")}">\n'
    return f'''<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{E(title)}</title>
<meta name="description" content="{E(desc)}">
<meta name="author" content="Ιβάν Δ. Αθανασόπουλος">
<meta name="theme-color" content="#EDC89B">
<meta name="referrer" content="no-referrer">
<link rel="canonical" href="{SITE}/{canon_path.replace('index.html','')}">
{alt}<meta property="og:title" content="{E(title)}">
<meta property="og:description" content="{E(desc)}">
<meta property="og:url" content="{SITE}/{canon_path.replace('index.html','')}">
<meta property="og:site_name" content="ivan.gr">
<link rel="icon" href="{ico}" sizes="32x32" type="image/png">
<link rel="apple-touch-icon" href="{ico180}">
<link rel="preload" href="{fr}" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{css}">
<link rel="alternate" type="application/atom+xml" title="ivan.gr" href="{rel(frm,'feed.xml')}">
{extra}</head>
'''

def langnav(frm, cur, targets):
    out = []
    for l in LANGS:
        if l not in targets: continue
        lab = L[l]['name']
        if l == cur: out.append(f'<span aria-current="true" lang="{l}">{lab}</span>')
        else: out.append(f'<a href="{rel(frm, targets[l])}" lang="{l}" hreflang="{l}">{lab}</a>')
    return '<nav class="langs" aria-label="Γλώσσα · Language">' + '<i>·</i>'.join(out) + '</nav>'

def footer(frm):
    return f'<footer class="foot"><a href="{rel(frm,"index.html")}">ivan.gr</a> · © 2025–2026 Ιβάν Δ. Αθανασόπουλος</footer>\n'

def write(p, s):
    fp = os.path.join(OUT, p); os.makedirs(os.path.dirname(fp) or OUT, exist_ok=True)
    open(fp, 'w', encoding='utf-8').write(s)

# --- αρχικές (ανά γλώσσα) ---------------------------------------------------
def home(lang):
    frm = HOME[lang]; T = L[lang]
    if lang == 'el':
        items = [dict(t=p['title'].strip(), path=p['path'], date=p['published'], txt=text_of(p['html'])) for p in posts]
    else:
        lst = [g for d in trans.values() for l, g in d.items() if l == lang] + [g for g in orphans if g['lang'] == lang]
        lst.sort(key=lambda g: g['published'], reverse=True)
        items = [dict(t=g['title'].strip(), path=g['path'], date=g['published'], txt=re.sub(r'^.*?(Greek original|Original grec|Griechisches Original)\s*', '', text_of(g['html']))) for g in lst]
    lead, recent = items[0], items[1:7]
    years = {}
    for it in items: years.setdefault(it['date'][:4], []).append(it)
    s = head(frm, lang, 'ivan.gr', T['intro'], frm, {l: HOME[l] for l in LANGS})
    s += '<body class="home">\n'
    s += f'''<header class="cover">
{langnav(frm, lang, HOME)}
<div class="cover-inner">
<h1 class="wordmark">ivan.gr</h1>
<p class="intro">{E(T['intro'])}</p>
</div>
<a class="down" href="#texts" aria-label="{E(T['down'])}"><svg viewBox="0 0 24 24" width="22" height="22" aria-hidden="true"><path d="M12 5v14M6 13l6 6 6-6" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg></a>
</header>
<main id="texts" class="wrap">
<article class="lead">
<p class="kicker">{E(T['latest'])} · <time datetime="{lead['date'][:10]}">{E(dlong(lead['date'], lang))}</time></p>
<h2><a href="{rel(frm, lead['path'])}">{E(lead['t'])}</a></h2>
<p class="ex">{E(excerpt(lead['txt']))}</p>
<p class="go"><a href="{rel(frm, lead['path'])}">{E(T['read'])}</a></p>
</article>
<section class="recent"><h2 class="h">{E(T['recent'])}</h2><ol>
'''
    for it in recent:
        s += f'<li><a href="{rel(frm, it["path"])}"><time datetime="{it["date"][:10]}">{E(dshort(it["date"], lang))}</time><span>{E(it["t"])}</span></a></li>\n'
    s += f'''</ol></section>
<section class="index" id="index"><div class="ihead"><h2 class="h">{E(T['all'])} <span class="n">{len(items)}</span></h2>
<label class="search"><span class="vh">{E(T['search'])}</span><input type="search" placeholder="{E(T['search'])}" autocomplete="off" spellcheck="false"></label></div>
'''
    for y in sorted(years, reverse=True):
        s += f'<div class="year"><h3>{y}</h3><ul>\n'
        for it in years[y]:
            s += f'<li data-k="{E(norm(it["t"] + " " + it["txt"][:400]))}"><a href="{rel(frm, it["path"])}"><span>{E(it["t"])}</span><time datetime="{it["date"][:10]}">{E(dshort(it["date"], lang))}</time></a></li>\n'
        s += '</ul></div>\n'
    s += f'<p class="none" hidden>{E(T["none"])}</p></section>\n'
    if lang == 'el':
        s += f'<p class="book">Μέσα από αυτόν τον διάλογο αναδύθηκε το <a href="{rel(frm, "ek/index.html")}">«εκ»</a> — βιβλίο, 2027.</p>\n'
    s += '</main>\n' + footer(frm)
    s += f'<script src="{rel(frm, "assets/site.js")}" defer></script>\n</body>\n</html>\n'
    write(frm, s)
    return items

# --- σελίδες κειμένων ------------------------------------------------------
def page(item, lang, alts, prev=None, nxt=None):
    frm = item['path']; T = L[lang]
    body = clean(item['html'], frm)
    desc = excerpt(text_of(item['html']), 180)
    s = head(frm, lang, item['title'].strip() + ' · ivan.gr', desc, frm, alts)
    s += '<body class="text">\n'
    s += f'<header class="bar"><a class="home-link" href="{rel(frm, HOME[lang])}">ivan.gr</a>{langnav(frm, lang, alts) if len(alts) > 1 else ""}</header>\n'
    s += f'<main class="wrap"><article class="post"><h1>{E(item["title"].strip())}</h1>\n'
    s += f'<p class="date"><time datetime="{item["published"][:10]}">{E(dlong(item["published"], lang))}</time></p>\n'
    s += f'<div class="body">{body}</div></article>\n<nav class="pn">'
    if nxt: s += f'<a class="nx" href="{rel(frm, nxt["path"])}"><small>{E(T["next"])}</small>{E(nxt["title"].strip())}</a>'
    if prev: s += f'<a class="pv" href="{rel(frm, prev["path"])}"><small>{E(T["prev"])}</small>{E(prev["title"].strip())}</a>'
    s += f'</nav><p class="back"><a href="{rel(frm, HOME[lang])}#index">{E(T["index"])}</a></p></main>\n' + footer(frm)
    s += '</body>\n</html>\n'
    write(frm, s)

def run():
    for l in LANGS: home(l)
    for i, p in enumerate(posts):
        alts = {'el': p['path']}
        for l, g in trans.get(p['url'], {}).items(): alts[l] = g['path']
        page(p, 'el', alts, posts[i+1] if i+1 < len(posts) else None, posts[i-1] if i > 0 else None)
        for l, g in trans.get(p['url'], {}).items():
            page(g, l, alts)
    for g in orphans: page(g, g['lang'], {g['lang']: g['path']})
    # βιβλίο
    src = os.path.join(ROOT, 'tools', 'ek')
    dst = os.path.join(OUT, 'ek')
    if os.path.isdir(dst): shutil.rmtree(dst)
    shutil.copytree(src, dst)
    # τροφοδοσία, χάρτης
    now = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    feed = f'<?xml version="1.0" encoding="utf-8"?>\n<feed xmlns="http://www.w3.org/2005/Atom" xml:lang="el"><title>ivan.gr</title><link href="{SITE}/"/><link rel="self" href="{SITE}/feed.xml"/><id>{SITE}/</id><updated>{now}</updated><author><name>Ιβάν Δ. Αθανασόπουλος</name></author>\n'
    for p in posts[:30]:
        feed += f'<entry><title>{E(p["title"].strip())}</title><link href="{SITE}/{p["path"]}"/><id>{SITE}/{p["path"]}</id><published>{p["published"]}</published><updated>{p["updated"]}</updated><summary>{E(excerpt(text_of(p["html"]), 400))}</summary></entry>\n'
    write('feed.xml', feed + '</feed>\n')
    urls = [''] + [HOME[l] for l in LANGS[1:]] + ['ek/'] + [p['path'] for p in posts] + [g['path'] for d in trans.values() for g in d.values()] + [g['path'] for g in orphans]
    write('sitemap.xml', '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + ''.join(f'<url><loc>{SITE}/{u}</loc></url>\n' for u in urls) + '</urlset>\n')
    write('robots.txt', f'User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n')
    print('posts', len(posts), 'translations', sum(len(d) for d in trans.values()), 'orphans', len(orphans))

if __name__ == '__main__':
    run()
