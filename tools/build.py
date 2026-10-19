#!/usr/bin/env python3
"""ivan.gr — στατικός ιστότοπος από τα κείμενα (content/*.json).
Κρατά τις παλιές διευθύνσεις του Blogger (/2026/09/x.html, /p/x.html) ώστε κανένας σύνδεσμος να μη χαθεί.
Όλοι οι εσωτερικοί σύνδεσμοι είναι σχετικοί, ώστε ο ιστότοπος να δουλεύει και σε προεπισκόπηση με πρόθεμα."""
import json, os, re, html, shutil, posixpath, datetime
from urllib.parse import urlparse
from bs4 import BeautifulSoup, NavigableString
import pyphen
import hashlib, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import og, near
HYPH = {'el': pyphen.Pyphen(lang='el_GR'), 'en': pyphen.Pyphen(lang='en_GB'), 'fr': pyphen.Pyphen(lang='fr'), 'de': pyphen.Pyphen(lang='de_DE')}
WORD = re.compile(r'[^\W\d_]{8,}')

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
HOME = {'el': 'keimena/index.html', 'en': 'p/en.html', 'fr': 'p/fr.html', 'de': 'p/de.html'}  # βιβλιοθήκη ανά γλώσσα
FRONT = {'el': 'index.html', 'en': 'p/en.html', 'fr': 'p/fr.html', 'de': 'p/de.html'}  # πρώτη σελίδα ανά γλώσσα
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

def hyphenate(soup, lang):
    d = HYPH.get(lang)
    if not d: return
    for t in soup.find_all(string=True):
        if not isinstance(t, NavigableString) or t.parent is None or t.parent.name in ('h1','h2','h3','h4','a','script','style','code'): continue
        if not any(par.name in ('p','li','blockquote','td') for par in t.parents): continue
        new = WORD.sub(lambda m: d.inserted(m.group(0), hyphen='\u00ad'), str(t))
        if new != str(t): t.replace_with(NavigableString(new))

def clean(h, frm, lang='el'):
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
    hyphenate(soup, lang)
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
newdir = os.path.join(ROOT, 'content', 'new-posts')
for fn in sorted(os.listdir(newdir)) if os.path.isdir(newdir) else []:
    if not fn.endswith('.json'): continue
    n = json.load(open(os.path.join(newdir, fn), encoding='utf-8'))
    pth = f"{n['date'][:4]}/{n['date'][5:7]}/{n['slug']}.html"
    data['posts'].append(dict(id=n['slug'], title=n['title'], url=f'{SITE}/{pth}', published=n['date'], updated=n.get('updated', n['date']), labels=n.get('labels', []), html=n['html']))
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
OG_IDX_P = None; OG_IDX = {}
def og_image(key, title, meta):
    """Φτιάχνει την κάρτα κοινοποίησης μόνο όταν άλλαξε ο τίτλος ή η γραμμή κάτω από αυτόν."""
    global OG_IDX_P, OG_IDX
    if OG_IDX_P is None:
        OG_IDX_P = os.path.join(OUT, 'og', 'index.json')
        try: OG_IDX = json.load(open(OG_IDX_P, encoding='utf-8'))
        except Exception: OG_IDX = {}
    rp = 'og/' + key + '.png'; h = hashlib.sha1((title + '|' + meta).encode()).hexdigest()[:12]
    if OG_IDX.get(rp) != h or not os.path.exists(os.path.join(OUT, rp)):
        og.card(title, meta, os.path.join(OUT, rp)); OG_IDX[rp] = h
    return rp

def og_save():
    if OG_IDX_P:
        json.dump(OG_IDX, open(OG_IDX_P, 'w', encoding='utf-8'), ensure_ascii=False, indent=0, sort_keys=True)

def head(frm, lang, title, desc, canon_path, alts=None, extra='', img=None):
    img = img or og_image('site', 'Κείμενα φιλοσοφίας, θεολογίας και γλώσσας', '')
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
<meta name="theme-color" content="#FBF8F2">
<script>try{{var t=localStorage.getItem('ivan-theme');if(t)document.documentElement.dataset.theme=t;}}catch(e){{}}</script>
<meta name="referrer" content="no-referrer">
<link rel="canonical" href="{SITE}/{canon_path.replace('index.html','')}">
{alt}<meta property="og:title" content="{E(title)}">
<meta property="og:description" content="{E(desc)}">
<meta property="og:url" content="{SITE}/{canon_path.replace('index.html','')}">
<meta property="og:site_name" content="ivan.gr">
<meta property="og:image" content="{SITE}/{img}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{ico}" sizes="32x32" type="image/png">
<link rel="apple-touch-icon" href="{ico180}">
<link rel="preload" href="{fr}" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{css}">
<link rel="alternate" type="application/atom+xml" title="ivan.gr" href="{rel(frm,'feed.xml')}">
<script src="{rel(frm,'assets/site.js')}" defer></script>
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

NIGHT_BTN = '<button type="button" class="night" aria-label="Νυχτερινή ανάγνωση" aria-pressed="false"><svg width="18" height="18" viewBox="0 0 24 24" aria-hidden="true"><path d="M20 14.5A8 8 0 1 1 9.5 4a6.5 6.5 0 0 0 10.5 10.5z" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/></svg></button>'

def footer(frm):
    return f'<footer class="foot"><a href="{rel(frm,"index.html")}">ivan.gr</a> · © 2025–2026 Ιβάν Δ. Αθανασόπουλος</footer>\n'

def write(p, s):
    fp = os.path.join(OUT, p); os.makedirs(os.path.dirname(fp) or OUT, exist_ok=True)
    open(fp, 'w', encoding='utf-8').write(s)

# --- βιβλιοθήκες (ανά γλώσσα) ---------------------------------------------
LIBNAME = {'el': 'Βιβλιοθήκη', 'en': 'Library', 'fr': 'Bibliothèque', 'de': 'Bibliothek'}

def masthead(frm, lang, cur, alts):
    n = []
    if lang == 'el':
        links = [('front', 'Σήμερα', 'index.html'), ('lib', 'Βιβλιοθήκη', 'keimena/index.html'), ('arch', 'Αρχείο φύλλων', 'fylla/index.html'), ('map', 'Χάρτης', 'xartis/index.html')]
        for key, lab, to in links:
            if key in ('front', 'arch') and not ISSUES: continue
            a = ' aria-current="page"' if key == cur else ''
            n.append(f'<a href="{rel(frm, to)}"{a}>{lab}</a>')
        n.append(f'<a class="ek" href="{rel(frm, "ek/index.html")}">εκ</a>')
    return (f'<header class="mast"><a class="wm" href="{rel(frm, FRONT[lang])}">ivan.gr</a>'
            f'<nav class="mnav" aria-label="Πλοήγηση">{"".join(n)}</nav>'
            f'<div class="mtools">{langnav(frm, lang, alts)}{NIGHT_BTN}</div></header>\n')

def library(lang, frm=None):
    frm = frm or HOME[lang]; T = L[lang]
    if lang == 'el':
        items = [dict(t=p['title'].strip(), path=p['path'], date=p['published'], txt=text_of(p['html'])) for p in posts]
    else:
        lst = [g for d in trans.values() for l, g in d.items() if l == lang] + [g for g in orphans if g['lang'] == lang]
        lst.sort(key=lambda g: g['published'], reverse=True)
        items = [dict(t=g['title'].strip(), path=g['path'], date=g['published'],
                      txt=re.sub(r'^.*?(Greek original|Original grec|Griechisches Original)\s*', '', text_of(g['html']))) for g in lst]
    lead, recent = items[0], items[1:7]
    years = {}
    for it in items: years.setdefault(it['date'][:4], []).append(it)
    alts = dict(HOME)
    s = head(frm, lang, LIBNAME[lang] + ' · ivan.gr', T['intro'], HOME[lang], alts)
    s += '<body class="lib">\n' + masthead(frm, lang, 'lib', alts)
    s += '<main id="texts" class="wrap">\n'
    s += f'<h1 class="libh">{E(LIBNAME[lang])}</h1>\n<p class="intro">{E(T["intro"])}</p>\n'
    s += '<article class="lead">\n'
    s += f'<p class="kicker">{E(T["latest"])} · <time datetime="{lead["date"][:10]}">{E(dlong(lead["date"], lang))}</time></p>\n'
    s += f'<h2><a href="{rel(frm, lead["path"])}">{E(lead["t"])}</a></h2>\n'
    s += f'<p class="ex">{E(excerpt(lead["txt"]))}</p>\n'
    s += f'<p class="go"><a href="{rel(frm, lead["path"])}">{E(T["read"])}</a></p>\n</article>\n'
    s += f'<section class="recent"><h2 class="h">{E(T["recent"])}</h2><ol>\n'
    for it in recent:
        s += f'<li><a href="{rel(frm, it["path"])}"><time datetime="{it["date"][:10]}">{E(dshort(it["date"], lang))}</time><span>{E(it["t"])}</span></a></li>\n'
    s += '</ol></section>\n'
    s += f'<section class="index" id="index"><div class="ihead"><h2 class="h">{E(T["all"])} <span class="n">{len(items)}</span></h2>\n'
    s += f'<label class="search"><span class="vh">{E(T["search"])}</span><input type="search" placeholder="{E(T["search"])}" autocomplete="off" spellcheck="false" data-src="{rel(frm, "search/" + lang + ".json")}"></label></div>\n'
    for y in sorted(years, reverse=True):
        s += f'<div class="year"><h3>{y}</h3><ul>\n'
        for it in years[y]:
            s += f'<li data-p="{E(it["path"])}" data-k="{E(norm(it["t"] + " " + it["txt"][:400]))}"><a href="{rel(frm, it["path"])}"><span>{E(it["t"])}</span><time datetime="{it["date"][:10]}">{E(dshort(it["date"], lang))}</time></a></li>\n'
        s += '</ul></div>\n'
    s += f'<p class="none" hidden>{E(T["none"])}</p></section>\n'
    write('search/' + lang + '.json', json.dumps([{'p': it['path'], 'x': it['txt']} for it in items], ensure_ascii=False, separators=(',', ':')))
    if lang == 'el':
        s += f'<p class="book">Μέσα από αυτόν τον διάλογο αναδύθηκε το <a href="{rel(frm, "ek/index.html")}">«εκ»</a> — βιβλίο, 2027.</p>\n'
    s += '</main>\n' + footer(frm) + '</body>\n</html>\n'
    write(frm, s)

# --- φύλλα (το φύλλο της ημέρας) -------------------------------------------
WEEKDAYS = ['Δευτέρα', 'Τρίτη', 'Τετάρτη', 'Πέμπτη', 'Παρασκευή', 'Σάββατο', 'Κυριακή']
ISSUES = []
_fd = os.path.join(ROOT, 'content', 'fylla')
for fn in sorted(os.listdir(_fd)) if os.path.isdir(_fd) else []:
    if fn.endswith('.json'):
        ISSUES.append(json.load(open(os.path.join(_fd, fn), encoding='utf-8')))
ISSUES.sort(key=lambda x: x['date'], reverse=True)

def issue_date(d):
    y, m, dd = dparts(d)
    wd = WEEKDAYS[datetime.date(y, m, dd).weekday()]
    return f'{wd} {dd} {L["el"]["months"][m-1]} {y}'

def issue_page(iss, frm, is_front):
    cards, wins = [], []
    def window(wid, kind, title, meta, body, perm=None):
        p = f'<p class="wperm"><a href="{rel(frm, perm)}">Μόνιμη σελίδα</a></p>' if perm else ''
        wins.append(f'<dialog class="win" id="w-{wid}" aria-labelledby="wt-{wid}"><button type="button" class="wclose" aria-label="Κλείσιμο">'
                    f'<svg width="16" height="16" viewBox="0 0 24 24" aria-hidden="true"><path d="M6 6l12 12M18 6L6 18" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg></button>'
                    f'<p class="wkind">{E(kind)}</p><h2 id="wt-{wid}">{E(title)}</h2>' + (f'<p class="wmeta">{meta}</p>' if meta else '') +
                    f'<div class="body">{body}</div>{p}</dialog>')
    t = iss.get('text')
    if t:
        post = by_url.get(t['ref']) if 'ref' in t else None
        if post:
            title = post['title'].strip(); body = clean(post['html'], frm)
            cards.append(f'<button type="button" class="card c-text" data-w="text"><span class="ck">Το κείμενο της ημέρας</span>'
                         f'<span class="ct">{E(title)}</span><span class="ce">{E(excerpt(text_of(post["html"]), 300))}</span>'
                         f'<span class="cm">{E(dlong(post["published"], "el"))}</span></button>')
            window('text', 'Το κείμενο της ημέρας', title, E(dlong(post['published'], 'el')), body, post['path'])
    sk = iss.get('sketch')
    if sk:
        img = f'<img src="{rel(frm, sk["image"])}" alt="{E(sk.get("alt", sk.get("title", "")))}" loading="lazy">'
        cards.append(f'<button type="button" class="card c-sketch" data-w="sketch"><span class="ck">Σκίτσο</span>{img}'
                     f'<span class="cm">{E(sk.get("caption", ""))}</span></button>')
        window('sketch', 'Σκίτσο', sk.get('title', ''), '', f'<figure>{img}<figcaption>{sk.get("about", "")}</figcaption></figure>')
    news = iss.get('news', [])
    for i, n in enumerate(news):
        wid = f'n{i}'
        cards.append(f'<button type="button" class="card c-news" data-w="{wid}"><span class="ck">{E(n["kind"])}</span>'
                     f'<span class="ct">{E(n["title"])}</span><span class="cl">{E(n.get("line", ""))}</span></button>')
        src = f'<a href="{E(n["url"])}" rel="noopener" target="_blank">{E(n.get("source", n["url"]))}</a>' if n.get('url') else E(n.get('source', ''))
        meta = src + (f' · {E(n["date"])}' if n.get('date') else '')
        body = (f'<p>{E(n["summary"])}</p>' if n.get('summary') else '') + (f'<p class="myline">{E(n["line"])}</p>' if n.get('line') else '')
        window(wid, n['kind'], n['title'], meta, body)
    s = head(frm, 'el', 'ivan.gr' if is_front else f'Φύλλο {iss["number"]} · ivan.gr',
             f'Φύλλο {iss["number"]} · {issue_date(iss["date"])}', 'index.html' if is_front else frm, {'el': 'index.html'})
    s += '<body class="issue">\n' + masthead(frm, 'el', 'front' if is_front else 'arch', FRONT)
    s += f'<main class="sheet"><p class="dateline">Φύλλο {iss["number"]} · {issue_date(iss["date"])}</p>\n'
    top = [c for c in cards if 'c-text' in c or 'c-sketch' in c]
    if top: s += '<div class="top">' + ''.join(top) + '</div>\n'
    if news:
        s += '<section class="news" aria-label="Νέα που διάλεξα"><h2 class="h">Νέα που διάλεξα</h2><div class="ngrid">' + ''.join(c for c in cards if 'c-news' in c) + '</div></section>\n'
    low = ''
    if iss.get('note'):
        low += f'<section class="note"><h2 class="h">Σημείωση</h2><div class="body">{iss["note"]}</div></section>'
    th = [by_url[u] for u in iss.get('thread', []) if u in by_url]
    if th:
        low += '<section class="thread"><h2 class="h">Το νήμα</h2><ul>' + ''.join(
            f'<li><a href="{rel(frm, p["path"])}">{E(p["title"].strip())}</a> <time>{E(dshort(p["published"], "el"))} {p["published"][:4]}</time></li>' for p in th) + '</ul></section>'
    if low: s += f'<div class="low">{low}</div>\n'
    s += f'<p class="intro sheet-intro">{E(L["el"]["intro"])}</p>\n</main>\n' + ''.join(wins) + '\n' + footer(frm) + '</body>\n</html>\n'
    write(frm, s)

def issues_build():
    if not ISSUES:
        library('el', 'index.html')
        return
    issue_page(ISSUES[0], 'index.html', True)
    for iss in ISSUES:
        issue_page(iss, f'fylla/{iss["date"]}/index.html', False)
    frm = 'fylla/index.html'
    s = head(frm, 'el', 'Αρχείο φύλλων · ivan.gr', 'Όλα τα φύλλα του ivan.gr', frm, {'el': frm})
    s += '<body class="lib">\n' + masthead(frm, 'el', 'arch', FRONT) + '<main class="wrap"><h1 class="libh">Αρχείο φύλλων</h1><ol class="arch">'
    for iss in ISSUES:
        head_t = ''
        t = iss.get('text')
        if t and t.get('ref') in by_url: head_t = by_url[t['ref']]['title'].strip()
        s += f'<li><a href="{rel(frm, "fylla/" + iss["date"] + "/index.html")}"><span>Φύλλο {iss["number"]}</span><time>{E(issue_date(iss["date"]))}</time><em>{E(head_t)}</em></a></li>'
    s += '</ol></main>\n' + footer(frm) + '</body>\n</html>\n'
    write(frm, s)

# --- σελίδες κειμένων ------------------------------------------------------
READ_MIN = {
    'el': lambda m: f'{m} λεπτό ανάγνωσης' if m == 1 else f'{m} λεπτά ανάγνωσης',
    'en': lambda m: f'{m} min read',
    'fr': lambda m: f'{m} min de lecture',
    'de': lambda m: f'{m} Min. Lesezeit',
}

def page(item, lang, alts, prev=None, nxt=None):
    frm = item['path']; T = L[lang]
    body = clean(item['html'], frm, lang)
    desc = excerpt(text_of(item['html']), 180)
    mins = max(1, round(len(text_of(item['html']).split()) / 200))
    img = og_image(frm[:-5] if frm.endswith('.html') else frm, item['title'].strip(), dlong(item['published'], lang) + ' · ' + READ_MIN[lang](mins))
    s = head(frm, lang, item['title'].strip() + ' · ivan.gr', desc, frm, alts, img=img)
    s += '<body class="text">\n<div class="prog" aria-hidden="true"></div>\n'
    s += f'<header class="bar"><a class="home-link" href="{rel(frm, FRONT[lang])}">ivan.gr</a>{langnav(frm, lang, alts) if len(alts) > 1 else ""}{NIGHT_BTN}</header>\n'
    s += f'<main class="wrap"><article class="post"><h1>{E(item["title"].strip())}</h1>\n'
    s += f'<p class="date"><time datetime="{item["published"][:10]}">{E(dlong(item["published"], lang))}</time><span class="rt"> · {E(READ_MIN[lang](mins))}</span></p>\n'
    s += f'<div class="body">{body}</div></article>\n'
    skip = {x['path'] for x in (prev, nxt) if x}
    nb = [q for q in NEAR.get(frm, []) if q[0] not in skip][:3] if lang == 'el' else None
    if nb:
        s += '<section class="near"><h2 class="h">Κοντινά κείμενα</h2><ul>' + ''.join(
            f'<li><a href="{rel(frm, q)}"><span>{E(BYPATH[q]["title"].strip())}</span></a></li>' for q, _ in nb) + '</ul></section>\n'
    s += '<nav class="pn">'
    if nxt: s += f'<a class="nx" href="{rel(frm, nxt["path"])}"><small>{E(T["next"])}</small>{E(nxt["title"].strip())}</a>'
    if prev: s += f'<a class="pv" href="{rel(frm, prev["path"])}"><small>{E(T["prev"])}</small>{E(prev["title"].strip())}</a>'
    s += f'</nav><p class="back"><a href="{rel(frm, HOME[lang])}#index">{E(T["index"])}</a></p></main>\n' + footer(frm)
    s += '</body>\n</html>\n'
    write(frm, s)

NEAR, BYPATH = {}, {}

def xartis():
    """Χάρτης των κειμένων: στατικό SVG, θέσεις από απλή διάταξη δυνάμεων, ακμές από τα κοντινά κείμενα."""
    import numpy as np
    keys = [p['path'] for p in posts]; idx = {k: i for i, k in enumerate(keys)}
    edges = set()
    for a in keys:
        for b, sc in NEAR.get(a, [])[:3]:
            edges.add(tuple(sorted((idx[a], idx[b]))))
    n = len(keys); rng = np.random.default_rng(7); P = rng.uniform(-1, 1, (n, 2))
    E_ = np.array(sorted(edges)); kk = 1.6 / np.sqrt(n); t = .12
    for it in range(400):
        d = P[:, None, :] - P[None, :, :]; dist = np.linalg.norm(d, axis=2) + 1e-6
        F = (d / dist[..., None] * (kk * kk / dist)[..., None]).sum(1)
        dv = P[E_[:, 0]] - P[E_[:, 1]]; dl = np.linalg.norm(dv, axis=1)[:, None] + 1e-6
        att = dv / dl * (dl * dl / kk)
        np.add.at(F, E_[:, 0], -att); np.add.at(F, E_[:, 1], att)
        F -= P * .05
        L_ = np.linalg.norm(F, axis=1)[:, None] + 1e-9
        P += F / L_ * np.minimum(L_, t); t *= .992
    W, H, pad = 1000, 720, 40
    mn, mx = P.min(0), P.max(0); S = (P - mn) / (mx - mn)
    X = pad + S[:, 0] * (W - 2 * pad); Y = pad + S[:, 1] * (H - 2 * pad)
    frm = 'xartis/index.html'; alts = {'el': frm}
    s = head(frm, 'el', 'Χάρτης των κειμένων · ivan.gr', 'Κάθε σημείο είναι ένα κείμενο· οι γραμμές ενώνουν κείμενα με κοινό λεξιλόγιο.', frm, alts)
    s += '<body class="mapp">\n' + masthead(frm, 'el', 'map', alts) + '<main class="wrap wide">\n'
    s += '<h1 class="libh">Χάρτης των κειμένων</h1>\n'
    s += '<p class="intro">Κάθε σημείο είναι ένα κείμενο και οι γραμμές ενώνουν κείμενα με κοινό λεξιλόγιο. Τη γειτονιά τη βρίσκει μέτρηση λέξεων, όχι ανάγνωση.</p>\n'
    s += '<p class="cap" aria-live="polite">Περάστε πάνω από ένα σημείο.</p>\n'
    s += f'<div class="mapbox"><svg class="map" viewBox="0 0 {W} {H}" role="group" aria-label="Χάρτης των κειμένων"><g class="edges">'
    for a, b in sorted(edges):
        s += f'<line x1="{X[a]:.1f}" y1="{Y[a]:.1f}" x2="{X[b]:.1f}" y2="{Y[b]:.1f}" data-a="{a}" data-b="{b}"/>'
    s += '</g><g class="nodes">'
    for i, k in enumerate(keys):
        p = posts[i]; t = p['title'].strip(); words = len(text_of(p['html']).split())
        r = min(11, 3.2 + (words ** .5) / 9); yr = p['published'][:4]
        s += (f'<a href="{rel(frm, k)}" data-i="{i}" data-t="{E(t)}" data-d="{E(dlong(p["published"], "el"))}" aria-label="{E(t)}">'
              f'<circle class="y{yr}" cx="{X[i]:.1f}" cy="{Y[i]:.1f}" r="{r:.1f}"/></a>')
    s += '</g></svg></div>\n'
    s += '<p class="legend"><span class="k y2026"></span>2026 <span class="k y2025"></span>2025 · μέγεθος σημείου: μήκος κειμένου</p>\n'
    s += '</main>\n' + footer(frm) + '</body>\n</html>\n'
    write(frm, s)
def run():
    global NEAR, BYPATH
    BYPATH = {p['path']: p for p in posts}
    NEAR = near.neighbours({p['path']: text_of(p['html']) for p in posts}, k=5)
    xartis()
    for l in LANGS: library(l)
    issues_build()
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
    urls = ['', 'keimena/', 'xartis/'] + [HOME[l] for l in LANGS[1:]] + ['ek/'] + ([f'fylla/{i["date"]}/' for i in ISSUES] + ['fylla/'] if ISSUES else []) + [p['path'] for p in posts] + [g['path'] for d in trans.values() for g in d.values()] + [g['path'] for g in orphans]
    write('sitemap.xml', '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + ''.join(f'<url><loc>{SITE}/{u}</loc></url>\n' for u in urls) + '</urlset>\n')
    write('robots.txt', f'User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n')
    og_save()
    print('posts', len(posts), 'translations', sum(len(d) for d in trans.values()), 'orphans', len(orphans))

if __name__ == '__main__':
    run()
