"""Κάρτες κοινοποίησης (1200×630): τίτλος σε EB Garamond, χαρτί και μπλε του ιστότοπου."""
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
FONTS = os.path.join(HERE, '..', 'assets', 'fonts')
W, H, M = 1200, 630, 96
BG, INK, BLUE, MUTED, OCHRE = '#FBF8F2', '#1F3550', '#005EAB', '#4A5A70', '#EDC89B'
_f = {}
def font(name, size):
    k = (name, size)
    if k not in _f: _f[k] = ImageFont.truetype(os.path.join(FONTS, f'ebgaramond-{name}.woff2'), size)
    return _f[k]

def wrap(text, f, width):
    lines, cur = [], ''
    for w in text.split():
        t = (cur + ' ' + w).strip()
        if f.getlength(t) <= width or not cur: cur = t
        else: lines.append(cur); cur = w
    if cur: lines.append(cur)
    return lines

def card(title, meta, out):
    img = Image.new('RGB', (W, H), BG); d = ImageDraw.Draw(img)
    d.rectangle([0, H - 14, W, H], fill=OCHRE)
    d.text((M, 72), 'ivan.gr', font=font('extrabold', 46), fill=BLUE)
    top, bottom = 168, H - 136
    for size in (78, 70, 62, 56, 50, 45, 40):
        f = font('semibold', size); lines = wrap(title, f, W - 2 * M); lh = int(size * 1.18)
        if len(lines) * lh <= bottom - top: break
    lines = lines[:max(1, (bottom - top) // lh)]
    y = top + (bottom - top - len(lines) * lh) // 2
    for ln in lines:
        d.text((M, y), ln, font=f, fill=INK); y += lh
    if meta: d.text((M, H - 104), meta, font=font('italic', 32), fill=MUTED)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    img.quantize(colors=48, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE).save(out, optimize=True)
