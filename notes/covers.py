# Guide covers: one idea per guide, drawn for it, on one ground. Run from the repo root, then look at every cover.
#   PYTHONUTF8=1 python notes/covers.py
# Writes img/covers/<slug>.webp (1200x1200, 1:1) and .jpg (1200x630 share image). Rules: notes/GUIDE-COVERS.md. Needs Chrome and Pillow.
import os, re, subprocess, tempfile, math
from PIL import Image
W = H = 1200
GROUND, BLUE, WHITE, INK, PINK, LIME = '#1c1c20', '#133fff', '#ffffff', '#0d0d0d', '#ff2d78', '#b8fa4e'
FIT = .8                                               # breathing space around every cover
S1, S2, S3 = '#26262b', '#32323a', '#4a4a54'          # shapes that stay in the background
CHROME = 'C:/Program Files/Google/Chrome/Application/chrome.exe'
logo = open('img/articles/et-logo.svg', encoding='utf-8').read()
paths = re.findall(r'<path (?:[^>]*? )?d="([^"]+)"', logo)
MARK = paths[0]                                        # 0..134 x 0..122

def mark(cx, cy, h, fill, extra=''):
    k = h / 122
    return f'<path transform="translate({cx-67.2*k:.1f} {cy-61*k:.1f}) scale({k:.4f})" d="{MARK}" fill="{fill}" {extra}/>'
def full(cx, cy, w, fill):
    k = w / 745
    return f'<g transform="translate({cx-w/2:.1f} {cy-61*k:.1f}) scale({k:.4f})" fill="{fill}">' + ''.join(f'<path d="{p}"/>' for p in paths) + '</g>'
def rect(x, y, w, h, fill, r=0, extra=''):
    return f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{r}" fill="{fill}" {extra}/>'
def text(x, y, s, size, fill=WHITE, weight=600, anchor='start'):
    return f'<text x="{x:.1f}" y="{y:.1f}" font-size="{size}" font-weight="{weight}" fill="{fill}" text-anchor="{anchor}">{s}</text>'
def cursor(x, y, k=3.2):                               # Lucide mouse-pointer-2
    return f'<path transform="translate({x-4*k} {y-4*k}) scale({k})" d="M4.037 4.688a.495.495 0 0 1 .651-.651l16 6.5a.5.5 0 0 1-.063.947l-6.124 1.58a2 2 0 0 0-1.438 1.435l-1.579 6.126a.5.5 0 0 1-.947.063z" fill="{WHITE}" stroke="{INK}" stroke-width="1.2" stroke-linejoin="round"/>'
def check(cx, cy, r):                                  # Lucide check
    k = r / 15
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{BLUE}"/><path transform="translate({cx-12*k} {cy-11.5*k}) scale({k})" d="M20 6 9 17l-5-5" stroke="{WHITE}" stroke-width="2.6" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'
def selection(x, y, w, h):
    o = rect(x, y, w, h, 'none', 0, f'stroke="{BLUE}" stroke-width="4"')
    for X in (x, x+w):
        for Y in (y, y+h):
            o += rect(X-9, Y-9, 18, 18, WHITE, 0, f'stroke="{BLUE}" stroke-width="4"')
    return o

def export():
    # the same mark six times, each drawn as its format: vectors keep their outline, pixels step
    ORANGE, CREAM = '#ff5c28', '#fff1e6'
    q, R, gx, gy = 75, 150, 120, 70                     # clover of four circles, radius q
    inside = lambda a, b: abs(a) <= q and abs(b) <= q or any((a-u*q)**2+(b-v*q)**2 <= q*q for u in (-1, 1) for v in (-1, 1))
    x0, y0, o = 600-R-gx/2, 600-2*R-gy, ''
    for i, n in enumerate(('AI', 'EPS', 'SVG', 'PDF', 'PNG', 'JPG')):
        x, y = x0+(i % 2)*(2*R+gx), y0+(i//2)*(2*R+gy)
        d = f'M{x} {y-q}A{q} {q} 0 1 1 {x+q} {y}A{q} {q} 0 1 1 {x} {y+q}A{q} {q} 0 1 1 {x-q} {y}A{q} {q} 0 1 1 {x} {y-q}z'
        fg = CREAM
        if n in ('AI', 'SVG'):
            o += f'<path d="{d}" stroke="{ORANGE}" stroke-width="5"/>'
            for u in (-1, 1):
                for v in (-1, 1):
                    for ax, ay, hx, hy in ((u*q, v*R, 1, 0), (u*R, v*q, 0, 1)):
                        if n == 'AI':
                            h = q*.5523
                            o += f'<path d="M{x+ax-hx*h} {y+ay-hy*h}L{x+ax+hx*h} {y+ay+hy*h}" stroke="{CREAM}" stroke-width="3"/>' + ''.join(f'<circle cx="{x+ax+t*hx*h}" cy="{y+ay+t*hy*h}" r="6" fill="{CREAM}"/>' for t in (-1, 1))
                        o += rect(x+ax-9, y+ay-9, 18, 18, CREAM, 0, f'stroke="{ORANGE}" stroke-width="4"')
            fg = ORANGE
        elif n in ('PNG', 'JPG'):
            c = R/9
            if n == 'JPG': o += rect(x-R, y-R, 2*R, 2*R, CREAM)
            o += ''.join(rect(x-R+a*c, y-R+b*c, c+.5, c+.5, ORANGE) for a in range(18) for b in range(18) if inside(-R+(a+.5)*c, -R+(b+.5)*c))
        else:
            o += f'<path d="{d}" fill="{ORANGE if n == "EPS" else CREAM}"/>'
            if n == 'PDF': fg = ORANGE
        o += text(x, y+17, n, 48, fg, 600, 'middle')
    return o

def construction():
    # left half: what it is built from. right half: the mark
    k = 6
    cx, cy = 600, 620
    ox, oy = cx-67.2*k, cy-61*k
    P = lambda x, y: (ox+x*1.4*k, oy+y*1.4*k)
    o = f'<clipPath id="l"><rect width="{cx}" height="{H}"/></clipPath><clipPath id="r"><rect x="{cx}" width="{W}" height="{H}"/></clipPath>'
    o += f'<g clip-path="url(#r)">{mark(cx, cy, 122*k, WHITE)}</g><g clip-path="url(#l)">' + mark(cx, cy, 122*k, S1, f'stroke="{WHITE}" stroke-width="{4/k:.2f}"')
    def line(a, b, e):
        (x1, y1), (x2, y2) = P(*a), P(*b)
        L = math.hypot(x2-x1, y2-y1)
        u, v = (x2-x1)/L, (y2-y1)/L
        return f'<path d="M{x1-u*e:.1f} {y1-v*e:.1f}L{x2+u*e:.1f} {y2+v*e:.1f}" stroke="{PINK}" stroke-width="3"/>'
    for x in (36.353, 39.942):
        o += line((x, 0), (x, 86), 70)
    o += line((0, 0), (48, 0), 100) + line((0, 41.72), (48, 41.72), 100)
    o += line((1.895, 65.842), (26.113, 49.956), 150) + line((14.59, 86.302), (36.353, 72.015), 150) + line((.602, 71.503), (8.703, 84.964), 90)
    for x, y, r in ((28.15, 38.6, 8.2), (47.998, 49.6, 7.9)):
        X, Y = P(x, y)
        o += f'<circle cx="{X:.1f}" cy="{Y:.1f}" r="{r*1.4*k:.1f}" fill="none" stroke="{PINK}" stroke-width="2.5"/>'
    for p in ((36.353, 4.183), (40.538, 0), (36.353, 38.708), (26.113, 49.956), (1.895, 65.842), (.602, 71.503), (8.703, 84.964), (14.59, 86.302), (36.353, 72.015), (39.942, 65.368), (39.942, 49.547)):
        X, Y = P(*p)
        o += rect(X-8, Y-8, 16, 16, GROUND, 0, f'stroke="{PINK}" stroke-width="3.5"')
    return o + '</g>' + f'<path d="M{cx} 130V{H-110}" stroke="{BLUE}" stroke-width="6"/>' + cursor(cx+10, 950, 4.6)

def package():
    # a node graph: one logo, its versions, its files. One path is lit
    MINT, NODE, LINE, o = '#5fe3b3', '#2a2a30', '#45454f', ''
    def pin(cx, cy, r, f):                              # sample mark: a four-blade pinwheel of quarter discs
        return ''.join(f'<path transform="rotate({k*90} {cx} {cy})" d="M{cx} {cy}V{cy-r}A{r} {r} 0 0 1 {cx+r} {cy}z" fill="{f}" stroke="none"/>' if k % 2 == 0 else
                       f'<path transform="rotate({k*90} {cx} {cy})" d="M{cx+r} {cy-r}V{cy}H{cx}A{r} {r} 0 0 1 {cx+r} {cy-r}z" fill="{f}"/>' for k in range(4))
    root = (85, 470, 260, 260)
    vers = [(475, 200+i*290, 260, 220) for i in range(3)]
    files = [(885, 96+i*174, 230, 138, n) for i, n in enumerate(('AI', 'EPS', 'SVG', 'PDF', 'PNG', 'JPG'))]
    mid = lambda n: n[1]+n[3]/2
    def wire(x1, y1, x2, y2, lit=False):
        d = (x2-x1)*.5
        return f'<path d="M{x1} {y1}C{x1+d} {y1} {x2-d} {y2} {x2} {y2}" stroke="{MINT if lit else LINE}" stroke-width="{7 if lit else 4}"/>'
    def port(x, y, lit=False): return f'<circle cx="{x}" cy="{y}" r="13" fill="{MINT if lit else "#8b8b96"}" stroke="{GROUND}" stroke-width="6"/>'
    V, F = 1, 2                                         # the lit path: full logo, SVG
    lit = ''
    for i, v in enumerate(vers):
        w = wire(root[0]+root[2], 600, v[0], mid(v), i == V)
        if i == V: lit += w
        else: o += w
        for j, f in enumerate(files if i == V else ()):  # only the chosen version, or the lines tangle
            w = wire(v[0]+v[2], mid(v), f[0], mid(f), i == V and j == F)
            if i == V and j == F: lit += w
            else: o += w
    o += lit + rect(*root, MINT, 30) + pin(215, 600, 84, INK)
    for i, v in enumerate(vers):
        on = i == V
        cx, cy, fg = v[0]+v[2]/2, mid(v), INK if on else WHITE
        o += rect(*v, MINT if on else NODE, 26)
        if i == 0: o += pin(cx, cy, 66, fg)
        if i == 1: o += pin(cx, cy-38, 42, fg) + text(cx, cy+74, 'Kora', 58, fg, 600, 'middle')
        if i == 2: o += text(cx, cy+25, 'Kora', 76, fg, 600, 'middle')
    for j, f in enumerate(files):
        on = j == F
        o += rect(*f[:4], MINT if on else NODE, 24) + text(f[0]+f[2]/2, mid(f)+20, f[4], 56, INK if on else WHITE, 600, 'middle')
    o += port(root[0]+root[2], 600, True)
    for i, v in enumerate(vers): o += port(v[0], mid(v), i == V) + (port(v[0]+v[2], mid(v), True) if i == V else '')
    for j, f in enumerate(files): o += port(f[0], mid(f), j == F)
    return o

def clear():
    # a crowded page that keeps its distance
    o = ''
    c, g = 124, 16
    for j in range(-2, 11):
        for i in range(-2, 11):
            if not (1 <= i <= 7 and 3 <= j <= 5):
                o += rect(-22+i*(c+g), -22+j*(c+g), c, c, S2 if (i*5+j*3) % 7 in (0, 3) else S1, 12)
    lw = 660                                            # the unit is the cap height
    u, lh = lw*67.2/745, lw*122/745
    zx, zy, zw, zh = 600-lw/2-u, 600-lh/2-u, lw+2*u, lh+2*u
    o += rect(zx, zy, zw, zh, 'none', 0, f'stroke="{BLUE}" stroke-width="5" stroke-dasharray="14 10"')
    for X in (zx, zx+zw-u):
        for Y in (zy, zy+zh-u):
            o += rect(X, Y, u, u, BLUE) + text(X+u/2, Y+u/2+9, 'x', 30, WHITE, 500, 'middle')
    return o + full(600, 600, lw, WHITE)

def guidelines():
    # the checklist itself: some done, one being ticked, one to go
    LILAC, NODE, RING, o = '#b9a5ff', '#2a2a30', '#5a5a66', ''
    w, h, g = 1000, 164, 26
    x0, y0 = 600-w/2, 600-(5*h+4*g)/2
    def tick(cx, cy, r, bg, fg):
        k = r/15
        return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{bg}"/><path transform="translate({cx-12*k} {cy-11.5*k}) scale({k})" d="M20 6 9 17l-5-5" stroke="{fg}" stroke-width="2.6" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'
    for i, n in enumerate(('Logo', 'Clear space', 'Colour', 'Type', 'Examples')):
        y, on = y0+i*(h+g), i == 3
        m, e, fg = y+h/2, x0+w-56, INK if on else WHITE
        o += rect(x0, y, w, h, LILAC if on else NODE, 30)
        if i < 4: o += tick(x0+88, m, 34, INK if on else LILAC, LILAC if on else INK)
        else: o += f'<circle cx="{x0+88}" cy="{m}" r="31" stroke="{RING}" stroke-width="6"/>'
        o += text(x0+164, m+23, n, 66, fg if i < 4 else '#9a9aa6')
        if i == 0: o += f'<path d="M{e-92} {m-46}h46a46 46 0 0 1 0 92h-46z" fill="{LILAC}"/><circle cx="{e-23}" cy="{m-23}" r="23" fill="{WHITE}"/>'
        if i == 1: o += rect(e-128, m-46, 128, 92, 'none', 0, f'stroke="{LILAC}" stroke-width="4" stroke-dasharray="11 8"') + rect(e-92, m-16, 56, 32, LILAC, 16)
        if i == 2: o += ''.join(f'<circle cx="{e-38-j*88}" cy="{m}" r="38" fill="{c}"/>' for j, c in enumerate((WHITE, LILAC, '#6d55d6')))
        if i == 3: o += text(e, m+36, 'Aa', 104, INK, 600, 'end')
        if i == 4: o += ''.join(rect(e-74-j*88, m-46, 74, 92, RING, 12) for j in range(3))
    return o + cursor(x0+92, y0+3*(h+g)+h/2+40, 4.2)

COVERS = {'export-logo-files-from-figma': export, 'logo-construction-grid-in-figma': construction, 'client-logo-package': package,
          'logo-clear-space-and-minimum-size': clear, 'what-to-include-in-brand-guidelines': guidelines}

if __name__ == '__main__':
    tmp = tempfile.mkdtemp().replace('\\', '/')
    fonts = os.path.abspath('../brandkit-figma-plugin/src/ui/assets/fonts').replace('\\', '/')
    font = ''.join(f"@font-face{{font-family:G;font-weight:{w};src:url('file:///{fonts}/geist-{w}.woff2')}}" for w in (400, 500, 600))
    for slug, f in COVERS.items():
        open(f'{tmp}/c.html', 'w', encoding='utf-8').write(f'<meta charset="utf-8"><style>{font}body{{margin:0}}svg{{display:block;font-family:G}}</style><svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" fill="none">{rect(0, 0, W, H, GROUND)}<g transform="translate({W*(1-FIT)/2} {H*(1-FIT)/2}) scale({FIT})">{f()}</g></svg>')
        subprocess.run([CHROME, '--headless=new', '--disable-gpu', '--hide-scrollbars', '--allow-file-access-from-files', '--force-device-scale-factor=2', f'--window-size={W},{H+200}', f'--screenshot={tmp}/c.png', f'file:///{tmp}/c.html'], capture_output=True)
        im = Image.open(f'{tmp}/c.png').convert('RGB').crop((0, 0, W*2, H*2)).resize((W, H), Image.LANCZOS)
        im.save(f'img/covers/{slug}.webp', quality=92)
        share = Image.new('RGB', (1200, 630), GROUND)
        share.paste(im.resize((630, 630), Image.LANCZOS), (285, 0))
        share.save(f'img/covers/{slug}.jpg', quality=90)
    print(len(COVERS), 'covers')
