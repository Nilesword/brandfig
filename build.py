# Builds the v2 site pages from shared parts, so the nav, buttons and footer stay identical everywhere.
#   python build.py  -> index.html and logo/, concepts/, guidelines/, bento/, export/ (each index.html: clean URLs on GitHub Pages)
# Copy comes from the Figma design (lab file, page "Website · v2"); see README.md.

MONTHLY = 'https://checkout.dodopayments.com/buy/pdt_0Nobm5F51QuNxu7qwlBDT?quantity=1&amp;redirect_url=https://getbrandfig.com'
YEARLY = 'https://checkout.dodopayments.com/buy/pdt_0NobmzpvQTNbngnL3Y2Li?quantity=1&amp;redirect_url=https://getbrandfig.com'
FIGMA = 'https://www.figma.com/community/plugin/1686542100112642893'
# stylesheet version: changes whenever site.css does, so browsers never use a stale copy
import hashlib
CSS_V = hashlib.md5(open('site.css', 'rb').read()).hexdigest()[:8]

# Lucide icons, the same ones as the plugin's tool tabs
ICON = {
  'pen-tool': '<path d="M15.707 21.293a1 1 0 0 1-1.414 0l-1.586-1.586a1 1 0 0 1 0-1.414l5.586-5.586a1 1 0 0 1 1.414 0l1.586 1.586a1 1 0 0 1 0 1.414z"/><path d="m18 13-1.375-6.874a1 1 0 0 0-.746-.776L3.235 2.028a1 1 0 0 0-1.207 1.207L5.35 15.879a1 1 0 0 0 .776.746L13 18"/><path d="m2.3 2.3 7.286 7.286"/><circle cx="11" cy="11" r="2"/>',
  'presentation': '<path d="M2 3h20"/><path d="M21 3v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V3"/><path d="m7 21 5-5 5 5"/>',
  'book-open-text': '<path d="M12 7v14"/><path d="M16 12h2"/><path d="M16 8h2"/><path d="M3 18a1 1 0 0 1-1-1V4a1 1 0 0 1 1-1h5a4 4 0 0 1 4 4 4 4 0 0 1 4-4h5a1 1 0 0 1 1 1v13a1 1 0 0 1-1 1h-6a3 3 0 0 0-3 3 3 3 0 0 0-3-3z"/><path d="M6 12h2"/><path d="M6 8h2"/>',
  'layout-grid': '<rect width="7" height="7" x="3" y="3" rx="1"/><rect width="7" height="7" x="14" y="3" rx="1"/><rect width="7" height="7" x="14" y="14" rx="1"/><rect width="7" height="7" x="3" y="14" rx="1"/>',
  'package': '<path d="M11 21.73a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73z"/><path d="M12 22V12"/><polyline points="3.29 7 12 12 20.71 7"/><path d="m7.5 4.27 9 5.15"/>',
}
def icon(k, color='currentColor'):
    return f'<svg viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICON[k]}</svg>'

FIGLOGO = '<svg class="figlogo" viewBox="0 0 38 57" aria-hidden="true"><path d="M19 28.5a9.5 9.5 0 1 1 19 0 9.5 9.5 0 0 1-19 0z" fill="#1ABCFE"/><path d="M0 47.5A9.5 9.5 0 0 1 9.5 38H19v9.5a9.5 9.5 0 1 1-19 0z" fill="#0ACF83"/><path d="M19 0v19h9.5a9.5 9.5 0 1 0 0-19H19z" fill="#FF7262"/><path d="M0 9.5A9.5 9.5 0 0 0 9.5 19H19V0H9.5A9.5 9.5 0 0 0 0 9.5z" fill="#F24E1E"/><path d="M0 28.5A9.5 9.5 0 0 0 9.5 38H19V19H9.5A9.5 9.5 0 0 0 0 28.5z" fill="#A259FF"/></svg>'
PINWHEEL = '<svg width="120" height="120" viewBox="0 0 40 40" aria-hidden="true"><path d="M13.0964 20.3536L17.6262 22.4473L17.046 27.6527L8.94876 36.8282C4.2486 33.8023 0.898178 28.8615 0 23.108L13.0964 20.3536Z" fill="#15E3FF"/><path d="M25.183 25.94L31.2414 36.3789C27.992 38.6605 24.0331 40 19.7612 40C18.3744 40 17.0206 39.8587 15.7133 39.59L17.046 27.6527L20.4765 23.7656L25.183 25.94Z" fill="#348DFC"/><path d="M39.1022 14.881C39.5332 16.5143 39.763 18.2294 39.763 19.9982C39.763 24.1145 38.5192 27.9403 36.3874 31.1207L25.184 25.9405L22.5551 21.4123L25.8574 17.6692L39.1022 14.881Z" fill="#FD4873"/><path d="M20.132 0C26.1505 0.109415 31.5194 2.877 35.1148 7.17842L25.8561 17.6694L20.9792 18.6959L18.519 14.4574L20.132 0Z" fill="#FFC700"/><path d="M18.519 14.4574L17.9745 19.3269L13.0991 20.353L0.514709 14.5347C2.09964 8.94044 6.05794 4.3436 11.2327 1.9007L18.519 14.4574Z" fill="#00E7B9"/></svg>'

# key, name, stage, headline, short line, sub-line, what's inside
TOOLS = [
  ('logo', 'Logo', 'Create faster', 'Construction, drawn for you.', 'Construction, drawn for you.',
   'Construction, base grids, clear space and lockups, measured from your logo’s real anchor points.', 'pen-tool',
   [('Construction', 'Lines, circles, anchors and handles from the real vector paths. Key lines, Balanced or Every line. Clean up removes extra anchors and stray handles.'),
    ('Grid', 'Base grids laid in a click: Square, Triangle, Isometric, Hexagon, Circular, Radial and Golden ratio.'),
    ('Clear space', 'Measured by cap height, the mark or pixels, with minimum sizes for screen and print.'),
    ('Lockup', 'Guides for the mark and the type together, and Snap type to line them up.')]),
  ('concepts', 'Concepts', 'Present sooner', 'Concept decks, built from your concepts.', 'Concept decks, built from your concepts.',
   'Add your concepts, pick a template and the presentation is laid out, ready to present.', 'presentation',
   [('Up to six concepts', 'Each with its logos, colours and two fonts.'),
    ('Six templates', 'Northwind, Fieldwork, Kestrel, Riot Club, Basalt and Sundae.'),
    ('Only what’s ready', 'About 17 pages. Empty pages are skipped, and building again updates them.')]),
  ('guidelines', 'Guidelines', 'Hand over ready', 'Guidelines, ready to edit.', 'Guidelines, ready to edit.',
   'Brand guidelines from your logos, colours and type, in twelve templates.', 'book-open-text',
   [('Brand assets', 'Logo versions, colours with roles and type roles, shared with every tool.'),
    ('Twelve templates', 'Northlight, Blocklab, Loudhouse, Funhaus, Darkroom, Full Circle, Ribbon, Bluebird, Transit, Livery, Arcadia and Afterglow.'),
    ('Pages and PDF', 'Reorder and lock pages, then save a PDF. Every page updates when an asset changes.')]),
  ('bento', 'Bento', 'Present sooner', 'Bento, filled with your brand.', 'Bento, filled with your brand.',
   'Select a frame and Brandfig fills it with a bento grid of your brand.', 'layout-grid',
   [('Three layouts', 'Even, Feature and Brick.'),
    ('Shuffle', 'Rolls the tiles, gap and corners in your style.'),
    ('Finish bento', 'Fills the tiles with your logo, colours, type and more.')]),
  ('export', 'Export', 'Hand over ready', 'The brand kit, exported in one go.', 'The brand kit, exported in one go.',
   'Every logo version in every format, in one zip, with a guide for the client.', 'package',
   [('Every version', 'Color, Reversed, Black, White and Grey.'),
    ('Every format', 'AI, EPS, PDF, SVG, PNG and JPG, with the PNG sizes you pick.'),
    ('For the client', 'An optional guidelines PDF, a font list and a Which file to use PDF, all in the same zip.')]),
]

def toolmenu(active=None):
    return ''.join(f'<a class="item{" on" if t[0] == active else ""}" href="/{t[0]}/"{" aria-current=\"page\"" if t[0] == active else ""}><span class="ic">{icon(t[6])}</span><span><b>{t[1]}</b><small>{t[4]}</small></span></a>' for t in TOOLS)

def head(title, desc, path='/'):
    active = path.strip('/') or None
    TOOLMENU = toolmenu(active)
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>{title}</title>
<meta name="description" content="{desc}" />
<link rel="icon" href="/img/mark.svg" />
<link rel="apple-touch-icon" href="/img/apple-touch-icon.png" />
<link rel="canonical" href="https://getbrandfig.com{path}" />
<meta name="theme-color" content="#0a0a0c" />
<meta property="og:type" content="website" />
<meta property="og:site_name" content="Brandfig" />
<meta property="og:title" content="{title}" />
<meta property="og:description" content="{desc}" />
<meta property="og:url" content="https://getbrandfig.com{path}" />
<meta property="og:image" content="https://getbrandfig.com/img/og.jpg" />
<meta property="og:image:width" content="1200" />
<meta property="og:image:height" content="630" />
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:image" content="https://getbrandfig.com/img/og.jpg" />
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600&amp;display=swap" rel="stylesheet" />
<link rel="stylesheet" href="/site.css?v={CSS_V}" />
</head>
<body>
<header class="bar"><nav class="nav wrap">
  <a class="mark" href="/"><img src="/img/wordmark.svg" alt="Brandfig"></a>
  <div class="links">
    <details class="menu"><summary{' class="here"' if active else ''}>Tools<svg viewBox="0 0 24 24" aria-hidden="true"><path d="m6 9 6 6 6-6"/></svg></summary>
      <div class="drop">{TOOLMENU}</div></details>
    <a href="/#pricing">Pricing</a><a href="/#faq">FAQ</a>
  </div>
  <div class="right">
    <a class="btn primary" href="{MONTHLY}">Try free for 3 days</a>
    <details class="menu burger"><summary aria-label="Menu"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h16"/></svg></summary>
      <div class="drop">{TOOLMENU}<a class="plain" href="/#pricing">Pricing</a><a class="plain" href="/#faq">FAQ</a></div></details>
  </div>
</nav></header>
'''

BUTTONS = f'''<div class="buttons"><a class="btn primary" href="{MONTHLY}">Start free trial</a><a class="btn ghost" href="{FIGMA}">{FIGLOGO}Get it on Figma</a></div>'''
BUTTONS_SOON = BUTTONS[:-6] + '<span class="btn soon" aria-label="Adobe Illustrator, coming soon"><span class="ai" aria-hidden="true">Ai</span>Adobe Illustrator<small>Coming soon</small></span></div>'

FOOTER = f'''<footer class="footer wrap">
  <div class="cta"><h2>Brand work, automated.</h2><p class="lead">Try every tool free for 3 days. Cancel anytime.</p>{BUTTONS}</div>
  <div class="cols">
    <div class="brand"><img src="/img/wordmark.svg" alt="Brandfig"><p>Automation for brand designers, inside Figma.</p><a href="mailto:contact@getbrandfig.com">contact@getbrandfig.com</a></div>
    <div><h4>Tools</h4>{''.join(f'<a href="/{t[0]}/">{t[1]}</a>' for t in TOOLS)}</div>
    <div><h4>Product</h4><a href="/#pricing">Pricing</a><a href="/#faq">FAQ</a><a href="{FIGMA}">Figma Community</a></div>
    <div><h4>Follow</h4><a href="https://www.instagram.com/getbrandfig/">Instagram</a><a href="https://www.threads.net/@getbrandfig">Threads</a></div>
    <div><h4>Legal</h4><a href="/terms.html">Terms</a><a href="/privacy.html">Privacy</a><a href="/refund.html">Refunds</a></div>
  </div>
  <div class="bottom"><span>© 2026 Brandfig</span><span>Made by Nilesh Shukla (Nilesword)</span></div>
</footer>
'''

def loop(key, label, lazy=True):
    return (f'<div class="loop"><video muted loop playsinline preload="none" poster="/img/loops/{key}.jpg" data-src="/img/loops/{key}.mp4" '
            f'aria-label="{label}"></video></div>')

SCRIPT = '''<script>
// Sticky bar: tightens and lifts a shade once the page scrolls
const bar = document.querySelector('.bar');
const onScroll = () => bar.classList.toggle('scrolled', scrollY > 8);
addEventListener('scroll', onScroll, { passive: true }); onScroll();
// Nav menus: one open at a time; close on outside click or Escape
const menus = [...document.querySelectorAll('details.menu')];
menus.forEach(m => m.addEventListener('toggle', () => { if (m.open) menus.forEach(o => { if (o !== m) o.open = false; }); }));
document.addEventListener('click', e => menus.forEach(m => { if (!m.contains(e.target)) m.open = false; }));
document.addEventListener('keydown', e => { if (e.key === 'Escape') menus.forEach(m => { m.open = false; }); });
// Loops play only when visible (and never with reduced motion: the poster shows the finished state)
const still = matchMedia('(prefers-reduced-motion: reduce)').matches;
const io = new IntersectionObserver(es => es.forEach(e => { const v = e.target;
  if (e.isIntersecting && !still) { if (!v.src) v.src = v.dataset.src; v.play().catch(() => {}); } else v.pause(); }), { threshold: .25 });
document.querySelectorAll('video[data-src]').forEach(v => io.observe(v));
'''

TAIL = '</script>\n</body>\n</html>\n'

# ---------- home ----------
TOP = ['decks/northwind', 'guides/transit-pattern', 'decks/kestrel', 'decks/fieldwork', 'decks/sundae', 'decks/riot-club', 'decks/basalt']
BOTTOM = ['decks/northwind-colour', 'guides/funhaus-typefaces', 'decks/kestrel-brief', 'guides/full-circle-pattern', 'decks/fieldwork-concept',
  'guides/arcadia-palette', 'decks/basalt-type', 'decks/riot-club-next-steps', 'guides/transit-contents', 'decks/sundae-three-words', 'decks/basalt-thanks']

FAQ = [
  ('Is it AI?', 'No. Construction is geometry: Brandfig reads your logo’s anchor points and curves and draws from them. Decks and guides are templates filled with your own logos, colours and fonts.'),
  ('How does the free trial work?', 'Every tool is unlocked for 3 days. You add a card at checkout but nothing is charged until day 3; cancel before then and you won’t be charged at all.'),
  ('How does the subscription work?', 'Pro is billed monthly ($7) or yearly ($56, saving 33%) and renews automatically. Cancel anytime from the link in your receipt email; Pro keeps working until the end of the period you’ve paid for.'),
  ('How do I activate it?', 'Your license key arrives by email. Open Brandfig in Figma, paste the key and press Activate.'),
  ('How many computers can I use?', 'One key works on two computers. Teams need one license per designer.'),
  ('Does my work leave Figma?', 'No. Everything runs inside Figma on your computer. The only thing it checks online is your license. See the <a href="/privacy.html">privacy policy</a>.'),
  ('Can I get a refund?', 'Payments aren’t refunded, except duplicate charges or where the law requires it. Try it free for 3 days first. See the <a href="/refund.html">refund policy</a>.'),
  ('Is it coming to Illustrator?', 'Yes, the Illustrator version is in the works.'),
]

def home():
    tabs = ''.join(
        f'<button class="tab" role="tab" aria-selected="{"true" if t[0] == "concepts" else "false"}" data-key="{t[0]}" data-label="{t[1]} tool at work">'
        f'<span class="name">{icon(t[6])}{t[1]}</span><span class="more">{t[4]}<a href="/{t[0]}/">See the {t[1]} tool</a></span></button>'
        for t in TOOLS)
    picks = ''.join(f'<span class="{"on" if t[0] == "concepts" else ""}"><i>{icon(t[6], "#0A0A0C" if t[0] == "concepts" else "#EDEDEA")}</i>{t[1]}</span>' for t in TOOLS)
    faq = ''.join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q, a in FAQ)
    return head('Brandfig · Brand work, automated.', 'Brandfig automates your brand design workflow in Figma, from construction to the final files. Create faster, ship sooner.') + f'''
<section class="stage" aria-label="Pages Brandfig builds from its deck and guideline templates">
  <div class="rows"></div>
  <div class="panel"><img src="/img/panels/logo-construction@2x.webp" width="360" height="720" alt="The Brandfig panel, Logo tool, Construction tab, ready to draw"></div>
</section>
<section class="hero-copy wrap">
  <h1>Brand work, automated.</h1>
  <p class="lead">Brandfig automates your brand design workflow, from construction to the final files. Create faster, ship sooner.</p>
  {BUTTONS_SOON}
  <p class="note">3 days free, then $7/month. Cancel anytime.</p>
</section>

<section class="block wrap" id="how">
  <div class="head"><p class="eyebrow">How it works</p><h2>Select, choose, done.</h2><p class="lead">Brandfig works on what you already have in the file: your logos, colours and fonts.</p></div>
  <div class="steps">
    <div class="step"><div class="art"><div class="sel"><i></i><i></i><i></i><i></i>{PINWHEEL}<b>Mark</b></div></div><h3>Select your logo</h3><p>Pick the mark, the logotype or a frame on the canvas.</p></div>
    <div class="step"><div class="art"><div class="picks">{picks}</div></div><h3>Choose what to make</h3><p>Construction, a grid, a concept deck, guidelines or the export.</p></div>
    <div class="step"><div class="art paper"><img src="/img/steps/construction.jpg" alt="Construction drawn on the ET Robotics mark" loading="lazy"></div><h3>Get editable layers</h3><p>Brandfig draws it in Figma. Change anything, it stays yours.</p></div>
  </div>
</section>

<section class="block wrap" id="tools">
  <div class="head"><p class="eyebrow">Tools</p><h2>Five tools, one panel.</h2><p class="lead">From the first sketch to the handover. Pick a tool to see it at work.</p></div>
  <div class="show">
    <div class="tabs" role="tablist" aria-label="Tools">{tabs}</div>
    {loop('concepts', 'Concepts tool at work')}
  </div>
</section>

<section class="block wrap" id="pricing">
  <div class="head"><p class="eyebrow">Pricing</p><h2>Try everything free for 3 days.</h2><p class="lead">Every tool, one key for two computers. Pick a plan; both start with 3 free days.</p></div>
  <div class="plans">
    <div class="plan"><h3>Monthly</h3><div class="price"><b>$7</b><span>/month</span></div><p>Billed monthly after the 3 free days. Cancel before day 3 and you won’t be charged.</p><a class="btn ghost" href="{MONTHLY}">Start free trial</a></div>
    <div class="plan blue"><h3>Yearly</h3><div class="price"><b>$56</b><span>/year, save 33%</span></div><p>$4.67 a month, billed yearly after the 3 free days. Cancel before day 3 and you won’t be charged.</p><a class="btn white" href="{YEARLY}">Start free trial</a></div>
  </div>
</section>

<section class="block wrap" id="faq">
  <div class="head"><p class="eyebrow">FAQ</p><h2>Questions, answered.</h2></div>
  <div class="faq">{faq}</div>
</section>
''' + FOOTER + SCRIPT + f'''
// Hero: two rows of real template pages flow out from behind the panel (two copies each: a seamless loop at -50%)
const TOP = {TOP!r}, BOTTOM = {BOTTOM!r};
const rows = document.querySelector('.rows');
for (const [set, dur] of [[TOP, 80], [BOTTOM, 110]]) {{
  const r = document.createElement('div'); r.className = 'row'; r.style.setProperty('--dur', dur + 's');
  r.innerHTML = [...set, ...set].map((n, i) => `<img src="/img/${{n}}.webp" width="480" height="270" alt="" ${{i < 4 ? '' : 'loading="lazy"'}}>`).join('');
  rows.appendChild(r);
}}
// Tools: each tab swaps in its own loop
const video = document.querySelector('#tools video');
document.querySelectorAll('.tab').forEach(tab => tab.addEventListener('click', () => {{
  document.querySelectorAll('.tab').forEach(t => t.setAttribute('aria-selected', String(t === tab)));
  const k = tab.dataset.key; video.poster = `/img/loops/${{k}}.jpg`; video.dataset.src = `/img/loops/${{k}}.mp4`; video.setAttribute('aria-label', tab.dataset.label);
  if (still) {{ video.removeAttribute('src'); video.load(); }} else {{ video.src = video.dataset.src; video.play().catch(() => {{}}); }}
}}));
''' + TAIL

def tool(t):
    key, name, stage, h1, _, sub, ic, cards = t
    cards_html = ''.join(f'<div class="card"><h3>{a}</h3><p>{b}</p></div>' for a, b in cards)
    return head(f'{name} · Brandfig', sub, f'/{key}/') + f'''
<section class="tool-hero wrap">
  <p class="eyebrow">{stage} · {name}</p>
  <h1>{h1}</h1>
  <p class="lead">{sub}</p>
  {BUTTONS}
  {loop(key, f'{name} tool at work')}
</section>
<section class="block wrap">
  <div class="head"><p class="eyebrow">What’s inside</p></div>
  <div class="cards">{cards_html}</div>
</section>
''' + FOOTER + SCRIPT + TAIL

if __name__ == '__main__':
    import os
    open('index.html', 'w', encoding='utf-8').write(home())
    for t in TOOLS:
        os.makedirs(t[0], exist_ok=True)
        open(f'{t[0]}/index.html', 'w', encoding='utf-8').write(tool(t))
    print('built: index.html, ' + ', '.join(f'{t[0]}/' for t in TOOLS))
