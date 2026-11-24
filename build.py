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

# ---------- search: titles and descriptions carry the words people search for; the visible copy stays in the brand voice
SITE = 'https://getbrandfig.com'
SEO = {
  '/': ('Brandfig: Logo construction and brand guidelines plugin for Figma',
        'Brandfig is a Figma plugin for brand designers. Draw logo construction grids, build concept decks and brand guidelines, and export every logo file in one go.'),
  'logo': ('Logo construction grid generator for Figma · Brandfig',
           'Draw logo construction lines, circles and anchors from your real vector paths in Figma. Plus base grids, clear space and lockup guides.'),
  'concepts': ('Logo concept presentation templates for Figma · Brandfig',
               'Turn your logo concepts into a client-ready presentation in Figma. Six templates, up to six concepts, every page editable.'),
  'guidelines': ('Brand guidelines generator for Figma · Brandfig',
                 'Build brand guidelines from your logos, colours and type in Figma. Twelve templates, pages you can reorder and lock, and a PDF export.'),
  'bento': ('Brand bento grid generator for Figma · Brandfig',
            'Fill any Figma frame with a bento grid of your brand: logo, colours, type, construction and patterns. Even, Feature and Brick layouts.'),
  'export': ('Export logo files in every format from Figma · Brandfig',
             'Export every logo version as AI, EPS, PDF, SVG, PNG and JPG in one zip from Figma, with a guidelines PDF and a Which file to use guide.'),
}

# ---------- tool pages: the line above the headline, steps, example pages and questions
PAGES = {
  'logo': {
    'kicker': 'Logo construction for Figma',
    'steps': [('Select your logo', 'Any vector logo on the canvas. Brandfig works from the paths you drew.'),
              ('Draw construction', 'Choose Key lines, Balanced or Every line, then press Draw construction.'),
              ('Keep designing', 'The construction lands as editable layers, and can redraw itself when the logo changes.')],
    'faq': [('How do I make a logo construction grid in Figma?', 'Select the vector logo, open the Logo tool in Brandfig and press Draw construction. It draws lines, circles, anchors and handles from the logo’s paths, and you choose which parts to show.'),
            ('What’s the difference between a base grid and a construction grid?', 'A base grid comes first: it’s what you sketch the logo on. Construction comes after: it shows the lines and circles behind the finished shape. The Logo tool makes both. Read the <a href="/guides/logo-construction-grid-in-figma/">logo construction guide</a>.'),
            ('How is clear space measured?', 'By the cap height of the type, the width of the mark or a pixel value you set. Minimum sizes for screen and print sit beside it. Read the <a href="/guides/logo-clear-space-and-minimum-size/">clear space guide</a>.'),
            ('Does it work on any logo?', 'It works on vector logos. A PNG or JPG has no paths to measure, so use the vector version.'),
            ('Where does the construction go next?', 'Use it in your <a href="/concepts/">concept deck</a>, your <a href="/guidelines/">brand guidelines</a> or a <a href="/bento/">bento grid</a>.')]},
  'concepts': {
    'kicker': 'Logo concept presentations for Figma',
    'steps': [('Add your concepts', 'Up to six, each with its logos, colours and two fonts.'),
              ('Pick a template', 'Six directions, from calm to loud. Your own frame can be the template too.'),
              ('Build presentation', 'The pages are laid out in Figma. Edit anything, then present.')],
    'faq': [('What goes into a logo presentation?', 'A cover, the brief, three words and references. Then, for each concept: an opener, the logo, versions, construction, colour, type, stationery, digital and in use. It closes with the concepts side by side and next steps.'),
            ('How many concepts can I present?', 'You can add up to six. The templates are designed for one to four in a deck.'),
            ('Can I edit the pages?', 'Yes. Every page is made of normal Figma layers, so you can change the words, images and layout.'),
            ('What if a concept isn’t finished?', 'Pages that would be empty are skipped. Build again when you have more and the deck updates.'),
            ('What happens after the client picks one?', 'Take the chosen direction into <a href="/guidelines/">brand guidelines</a>, then <a href="/export/">export the logo files</a>.')]},
  'guidelines': {
    'kicker': 'Brand guidelines for Figma',
    'steps': [('Add brand assets', 'Your logo versions, colours with roles and type roles.'),
              ('Pick a template', 'Twelve designs. Choose the pages you need and put them in order.'),
              ('Build guidelines', 'The guide is laid out in Figma, ready to edit and save as a PDF.')],
    'faq': [('What should brand guidelines include?', 'The logo and its versions, clear space, minimum sizes, the colour palette, typefaces and how it all comes together. You choose which pages go in and add your own words. Read the <a href="/guides/what-to-include-in-brand-guidelines/">brand guidelines checklist</a>.'),
            ('How do I update the guidelines when the brand changes?', 'Change the asset and build again. Pages you lock stay as you left them.'),
            ('Can I send them as a PDF?', 'Yes. Brandfig saves the guide as one PDF, and can add it to the zip when you <a href="/export/">export the logo files</a>.'),
            ('Are colour values included?', 'Yes: HEX, RGB and CMYK. CMYK is a conversion, so check it with the printer before production.'),
            ('Can I edit the templates?', 'Yes. The pages are normal Figma layers, so change anything you like.')]},
  'bento': {
    'kicker': 'Brand bento grids for Figma',
    'steps': [('Select a frame', 'Any size or shape. The bento is built to fit it.'),
              ('Choose a layout', 'Even, Feature or Brick, with 2 to 16 tiles. Set the gap and corners, or Shuffle.'),
              ('Finish bento', 'Your logos, colours, type and construction go into the tiles.')],
    'faq': [('What is a brand bento grid?', 'One frame split into tiles, each showing a part of the identity: the logo, colours, type, construction and more. It shows the whole brand at a glance.'),
            ('What size can the bento be?', 'Any frame size: a slide, a square post, a portfolio cover. Select the frame and the grid fills it.'),
            ('Where does the content come from?', 'From your brand assets or from one of your <a href="/concepts/">concepts</a>.'),
            ('Can I change the tiles afterwards?', 'Yes. The tiles are normal Figma layers, so you can swap, resize or restyle them.')]},
  'export': {
    'kicker': 'Logo file export for Figma',
    'steps': [('Add your logo versions', 'Mark, logotype, full logo or any version you’ve drawn.'),
              ('Pick the files', 'Choose colour versions, formats and PNG sizes. The panel counts the files for you.'),
              ('Export files', 'Everything is sorted into folders and saved as one zip.')],
    'faq': [('Can I export AI and EPS files from Figma with Brandfig?', 'Yes. AI files are PDF-compatible and open as vectors in Illustrator. EPS files are made from the vector logo. Pictures and angular gradients can’t go in an EPS. Read the <a href="/guides/export-logo-files-from-figma/">logo export guide</a> for every format.'),
            ('Which logo files should I give a client?', 'Vector files for print and design work (AI, EPS, PDF, SVG) and PNG or JPG for everyday screen use, in colour, reversed, black and white. Read the <a href="/guides/client-logo-package/">logo package guide</a>.'),
            ('How will the client know which file to use?', 'Add the Which file to use PDF. It explains each format, size and colour version, the logo rules and where to find every file.'),
            ('Which PNG sizes can I export?', 'Presets from 256 to 4096 px wide, and any custom width.'),
            ('Can the brand guidelines go in the same zip?', 'Yes, as a PDF, along with a font list. Build them first with the <a href="/guidelines/">Guidelines tool</a>.')]},
}

def toolmenu(active=None):
    return ''.join(f'<a class="item{" on" if t[0] == active else ""}" href="/{t[0]}/"{" aria-current=\"page\"" if t[0] == active else ""}><span class="ic">{icon(t[6])}</span><span><b>{t[1]}</b><small>{t[4]}</small></span></a>' for t in TOOLS)

def head(title, desc, path='/', ld=''):
    active = path.strip('/') if path.strip('/') in SEO else None
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
{ld}</head>
<body>
<header class="bar"><nav class="nav wrap">
  <a class="mark" href="/"><img src="/img/wordmark.svg" alt="Brandfig"></a>
  <div class="links">
    <details class="menu"><summary{' class="here"' if active else ''}>Tools<svg viewBox="0 0 24 24" aria-hidden="true"><path d="m6 9 6 6 6-6"/></svg></summary>
      <div class="drop">{TOOLMENU}</div></details>
    <a href="/#pricing">Pricing</a><a href="/guides/"{' class="here"' if path.startswith("/guides/") else ""}>Guides</a><a href="/#faq">FAQ</a>
  </div>
  <div class="right">
    <a class="btn primary" href="{MONTHLY}">Try free for 3 days</a>
    <details class="menu burger"><summary aria-label="Menu"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h16"/></svg></summary>
      <div class="drop">{TOOLMENU}<a class="plain" href="/#pricing">Pricing</a><a class="plain" href="/guides/">Guides</a><a class="plain" href="/#faq">FAQ</a></div></details>
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
    <div><h4>Product</h4><a href="/#pricing">Pricing</a><a href="/#faq">FAQ</a><a href="{FIGMA}">Figma Community</a><a href="/guides/">Guides</a></div>
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
  ('Is it AI?', 'No. You bring the logo, colours and fonts, and you make every choice.'),
  ('How does the free trial work?', 'Every tool is unlocked for 3 days. You add a card at checkout but nothing is charged until day 3; cancel before then and you won’t be charged at all.'),
  ('How does the subscription work?', 'Pro is billed monthly ($7) or yearly ($56, saving 33%) and renews automatically. Cancel anytime from the link in your receipt email; Pro keeps working until the end of the period you’ve paid for.'),
  ('How do I activate it?', 'Your license key arrives by email. Open Brandfig in Figma, paste the key and press Activate.'),
  ('How many computers can I use?', 'One key works on two computers. Teams need one license per designer.'),
  ('Does my work leave Figma?', 'No. Everything runs inside Figma on your computer. The only thing it checks online is your license. See the <a href="/privacy.html">privacy policy</a>.'),
  ('Can I get a refund?', 'Payments aren’t refunded, except duplicate charges or where the law requires it. Try it free for 3 days first. See the <a href="/refund.html">refund policy</a>.'),
  ('Is it coming to Illustrator?', 'Yes, the Illustrator version is in the works.'),
]

import json, re
def ldjson(obj):
    return '<script type="application/ld+json">' + json.dumps(obj, ensure_ascii=False) + '</script>' + chr(10)
APP = {
  '@type': 'SoftwareApplication', 'name': 'Brandfig', 'url': SITE + '/',
  'applicationCategory': 'DesignApplication', 'operatingSystem': 'Figma (web, macOS, Windows)',
  'description': SEO['/'][1], 'image': SITE + '/img/og.jpg', 'downloadUrl': FIGMA, 'installUrl': FIGMA,
  'featureList': ['Logo construction lines, circles and anchors', 'Base grids', 'Clear space and minimum sizes', 'Lockup guides',
                  'Logo concept presentations', 'Brand guidelines with PDF export', 'Bento grids', 'Logo export in AI, EPS, PDF, SVG, PNG and JPG'],
  'offers': [
    {'@type': 'Offer', 'name': 'Monthly', 'price': '7', 'priceCurrency': 'USD', 'url': MONTHLY.replace('&amp;', '&'), 'description': '3-day free trial, then billed monthly'},
    {'@type': 'Offer', 'name': 'Yearly', 'price': '56', 'priceCurrency': 'USD', 'url': YEARLY.replace('&amp;', '&'), 'description': '3-day free trial, then billed yearly'}],
  'publisher': {'@type': 'Organization', 'name': 'Brandfig', 'url': SITE + '/', 'logo': SITE + '/img/apple-touch-icon.png', 'email': 'contact@getbrandfig.com',
                'sameAs': [FIGMA, 'https://www.instagram.com/getbrandfig/', 'https://www.threads.net/@getbrandfig']},
}
def faq_ld(items):
    return {'@type': 'FAQPage', 'mainEntity': [{'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': re.sub('<[^>]+>', '', a)}} for q, a in items]}
def faq_html(items):
    return '<div class="faq">' + ''.join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q, a in items) + '</div>'
def home_ld():
    faq = faq_ld(FAQ)
    site = {'@type': 'WebSite', 'name': 'Brandfig', 'url': SITE + '/'}
    return ldjson({'@context': 'https://schema.org', '@graph': [site, APP, faq]})
def tool_ld(key, name):
    crumbs = {'@type': 'BreadcrumbList', 'itemListElement': [
        {'@type': 'ListItem', 'position': 1, 'name': 'Brandfig', 'item': SITE + '/'},
        {'@type': 'ListItem', 'position': 2, 'name': name, 'item': f'{SITE}/{key}/'}]}
    return ldjson({'@context': 'https://schema.org', '@graph': [crumbs, faq_ld(PAGES[key]['faq'])]})

def home():
    tabs = ''.join(
        f'<button class="tab" role="tab" aria-selected="{"true" if t[0] == "concepts" else "false"}" data-key="{t[0]}" data-label="{t[1]} tool at work">'
        f'<span class="name">{icon(t[6])}{t[1]}</span><span class="more">{t[4]}<a href="/{t[0]}/">See the {t[1]} tool</a></span></button>'
        for t in TOOLS)
    picks = ''.join(f'<span class="{"on" if t[0] == "concepts" else ""}"><i>{icon(t[6], "#0A0A0C" if t[0] == "concepts" else "#EDEDEA")}</i>{t[1]}</span>' for t in TOOLS)
    faq = faq_html(FAQ)
    return head(*SEO['/'], '/', home_ld()) + f'''
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
  {faq}
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
    p = PAGES[key]
    steps = ''.join(f'<div class="card"><h3>{a}</h3><p>{b}</p></div>' for a, b in p['steps'])
    cards_html = ''.join(f'<div class="card"><h3>{a}</h3><p>{b}</p></div>' for a, b in cards)
    return head(*SEO[key], f'/{key}/', tool_ld(key, name)) + f'''
<section class="tool-hero wrap">
  <h1><span class="eyebrow">{p['kicker']}</span> {h1}</h1>
  <p class="lead">{sub}</p>
  {BUTTONS}
  {loop(key, f'{name} tool at work')}
</section>
<section class="block wrap">
  <div class="head"><h2>What’s inside</h2></div>
  <div class="cards">{cards_html}</div>
</section>
<section class="block wrap">
  <div class="head"><h2>How it works</h2></div>
  <div class="cards">{steps}</div>
</section>
<section class="block wrap">
  <div class="head"><h2>Questions, answered.</h2></div>
  {faq_html(p['faq'])}
</section>
''' + FOOTER + SCRIPT + TAIL

# ---------- guides: plain answers to what designers search for
GUIDES = [{
  'tool': 'export',
  'cat': 'Logo files',
  'slug': 'export-logo-files-from-figma',
  'short': 'Export logo files from Figma',
  'title': 'How to export logo files from Figma, with AI and EPS · Brandfig',
  'desc': 'Export a logo from Figma as PNG, JPG, SVG and PDF, make AI and EPS files for print, and pick the right logo file for every job.',
  'h1': 'How to export logo files from Figma, including AI and EPS',
  'lead': 'Figma exports PNG, JPG, SVG and PDF. For AI and EPS, take the vector into Illustrator, or use a plugin that makes both inside Figma.',
  'published': '2026-11-25', 'modified': '2026-11-25',
  'body': '''
<h2>Get the logo ready</h2>
<p>A few minutes here saves a second export later.</p>
<ul>
  <li><b>Keep it vector.</b> If any part of the logo is an image, it stays pixels in every file.</li>
  <li><b>Outline the type and strokes.</b> Work on a copy, so the editable logo stays in your file. Outlined type looks the same on every computer.</li>
  <li><b>Clean the shape.</b> Remove hidden layers and stray points, and leave no background behind the logo.</li>
  <li><b>Name each version.</b> Mark, Logotype, Full logo. Figma uses the layer name as the file name.</li>
</ul>

<h2>Export PNG, JPG, SVG and PDF in Figma</h2>
<ol>
  <li>Select the logo version, not the page it sits on.</li>
  <li>In the right panel, find Export and press the plus.</li>
  <li>Choose the format. Add a row for each one you need.</li>
  <li>For PNG and JPG, type a width such as <b>1024w</b>. SVG and PDF export at 1x, because vectors scale to any size.</li>
  <li>For SVG, open the export settings and keep Outline text on.</li>
  <li>Press Export.</li>
</ol>
<p>PNG and SVG keep a transparent background. JPG doesn’t, so place the logo on the background colour you want first.</p>

<h2>Make an AI file</h2>
<p>Figma has no AI export. In Illustrator:</p>
<ol>
  <li>Export the logo from Figma as SVG or PDF.</li>
  <li>Open that file in Illustrator and release any clipping masks you don’t need.</li>
  <li>Check the colours and the shape against the original.</li>
  <li>Choose File, Save As, Adobe Illustrator (AI), with Create PDF Compatible File on.</li>
</ol>

<h2>Make an EPS file</h2>
<p>Printers, sign makers and embroidery shops often ask for EPS. With the logo open in Illustrator, choose File, Save As, Illustrator EPS. EPS doesn’t keep see-through effects, so use solid colours and shapes.</p>

<h2>Export AI and EPS inside Figma</h2>
<p>The <a href="/export/">Export tool in Brandfig</a> makes all six formats from the logo versions in your file. Pick the colour versions, the formats and the PNG sizes, and it saves one zip, sorted into folders.</p>
{loop}
<p>The AI files are PDF-compatible and open as vectors in Illustrator. The EPS files are made from the vector logo. Pictures and angular gradients can’t go in an EPS.</p>

<h2>Which logo file for which job</h2>
<table>
  <thead><tr><th>Job</th><th>Best file</th><th>Also works</th></tr></thead>
  <tbody>
    <tr><td>Website and apps</td><td>SVG</td><td>PNG</td></tr>
    <tr><td>Social posts and profile pictures</td><td>PNG, 1024 px or wider</td><td>JPG</td></tr>
    <tr><td>Slides and documents</td><td>PNG, 1024 px or wider</td><td>JPG</td></tr>
    <tr><td>Email signature</td><td>PNG</td><td>JPG</td></tr>
    <tr><td>Print: cards, flyers, posters</td><td>PDF</td><td>AI, EPS</td></tr>
    <tr><td>Signs, merch, embroidery, vinyl</td><td>EPS</td><td>AI, PDF</td></tr>
    <tr><td>Another designer</td><td>AI</td><td>SVG, PDF</td></tr>
  </tbody>
</table>

<h2>Send them to the client</h2>
<p>Every version, in every colour it needs, as vector and pixel files with clear names. The <a href="/guides/client-logo-package/">client logo package guide</a> has the full list and a folder structure to copy.</p>
<p>Colour on screen is RGB and print is CMYK, so agree the CMYK values with the printer and ask for a proof before a big run.</p>
''',
  'faq': [
    ('Can Figma export AI files?', 'No. Figma exports PNG, JPG, SVG and PDF. Open the SVG or PDF in Illustrator and save it as AI, or use a plugin such as <a href="/export/">Brandfig</a> that saves AI files from Figma.'),
    ('Can Figma export EPS files?', 'No. Save the EPS from Illustrator, or make it in Figma with a plugin such as <a href="/export/">Brandfig</a>.'),
    ('Is SVG or PNG better for a logo?', 'SVG for websites and apps, because it stays sharp at any size. PNG wherever SVG isn’t accepted, such as documents and social media.'),
    ('What size should a PNG logo be?', 'At least as wide as it will show, and twice that for sharp phone and laptop screens. 512, 1024 and 2048 px cover most uses.'),
    ('Why does the font change when a client opens the logo?', 'The type is still live text and the client doesn’t have the font. Outline the type before you export.'),
  ],
}, {
  'tool': 'logo',
  'cat': 'Logo design',
  'slug': 'logo-construction-grid-in-figma',
  'short': 'Logo construction grid in Figma',
  'title': 'How to make a logo construction grid in Figma · Brandfig',
  'desc': 'Draw a logo construction grid in Figma: pick a base grid, add the lines and circles behind the shape, and present it clearly.',
  'h1': 'How to make a logo construction grid in Figma',
  'lead': 'Outline the logo, draw a line along each key edge, and fit a circle to each true curve. Keep only the lines that explain the shape.',
  'published': '2026-11-25', 'modified': '2026-11-25',
  'body': '''
<h2>Base grid or construction grid</h2>
<p>They get mixed up, but they do different jobs.</p>
<ul>
  <li><b>Base grid.</b> Comes first. You sketch the logo on it, so sizes and angles stay consistent.</li>
  <li><b>Construction grid.</b> Comes after. It shows the lines, circles and alignments in the finished logo.</li>
</ul>
<p>You can use one without the other. A logo drawn freely can still have a clear construction.</p>

<h2>Pick a base grid</h2>
<table>
  <thead><tr><th>Grid</th><th>Good for</th></tr></thead>
  <tbody>
    <tr><td>Square</td><td>Letters, blocky marks and icons</td></tr>
    <tr><td>Triangle</td><td>Faceted marks and 60° angles</td></tr>
    <tr><td>Isometric</td><td>Cubes and marks with depth</td></tr>
    <tr><td>Hexagon</td><td>Cells, badges and six-sided marks</td></tr>
    <tr><td>Circular</td><td>Rings, arcs and round marks</td></tr>
    <tr><td>Radial</td><td>Blades, petals and anything that turns around a centre</td></tr>
    <tr><td>Golden ratio</td><td>Testing proportion, when it suits the idea</td></tr>
  </tbody>
</table>

<h2>Draw the construction in Figma</h2>
<ol>
  <li>Duplicate the logo and flatten the copy, so you have one clean vector. Keep the original safe.</li>
  <li>Lower the copy’s opacity, or give it a thin stroke and no fill, then lock it.</li>
  <li>Draw a line along each important edge: top, bottom, left, right and the main joins. Run it past the logo on both sides.</li>
  <li>Add lines for the diagonals that repeat. Check that matching angles really match.</li>
  <li>Press O and hold Shift to draw a circle over each curve that is part of a circle. Match the radius and the centre.</li>
  <li>Give every line and circle the same thin stroke, in one colour.</li>
  <li>Group the lines and the circles, and name the groups.</li>
</ol>
<p>If a circle almost fits, look closely. Either the curve is meant to be different, which is fine, or it needs a small correction.</p>

<h2>Keep only what explains the logo</h2>
<p>A construction grid is there to show decisions. If a line doesn’t touch an edge, a centre or a curve, take it out.</p>
<ul>
  <li><b>Show repeats.</b> Equal stroke widths, shared angles and circles of the same size.</li>
  <li><b>Show alignment.</b> Where the mark meets the type, and where edges share a line.</li>
  <li><b>Stay honest.</b> Don’t add golden ratio circles to a logo that wasn’t drawn with them.</li>
  <li><b>Trust your eye.</b> Optical corrections break the grid on purpose. Leave them in.</li>
</ul>

<h2>Draw it with Brandfig</h2>
<p>Select a vector logo, open the <a href="/logo/">Logo tool in Brandfig</a> and press Draw construction. It draws the lines, circles, anchors and handles from the logo’s paths. Choose Key lines, Balanced or Every line, and turn parts on or off.</p>
{loop}
<p>Everything lands as editable layers, and can redraw itself when the logo changes. The same tool lays all seven base grids, so you can sketch on one and draw the construction over the final mark.</p>

<h2>Present the construction</h2>
<ul>
  <li><b>One page, one logo.</b> Give it room and keep the caption short.</li>
  <li><b>Logo first.</b> Show the finished logo before the lines, so people know what they’re looking at.</li>
  <li><b>Say what it proves.</b> “Five equal blades around one centre” says more than “construction”.</li>
</ul>
<p>It fits in a <a href="/concepts/">concept deck</a> to explain the idea, and in the <a href="/guidelines/">brand guidelines</a> as a reference.</p>
''',
  'faq': [
    ('Does every logo need a construction grid?', 'No. It helps when the shape has clear repeats, angles or curves. For an expressive or drawn logo, clear space and minimum size are more useful.'),
    ('Should I draw the grid before or after the logo?', 'A base grid before, if it helps you sketch. The construction grid after, once the shape is final.'),
    ('Do logos need to follow the golden ratio?', 'No. It’s one way to test proportion. Use it when it fits the idea, and leave it out when it doesn’t.'),
    ('Can I make a construction grid from a PNG?', 'Not an accurate one. Draw the logo as a vector first, then build the construction from that.'),
    ('What colour should construction lines be?', 'One colour that stands apart from the logo, with a thin stroke. Blue, grey or one of the brand’s colours all work.'),
  ],
}, {
  'tool': 'export',
  'cat': 'Logo files',
  'slug': 'client-logo-package',
  'short': 'Client logo package',
  'title': 'What to include in a client’s logo package · Brandfig',
  'desc': 'A client logo package checklist: logo versions, colours, file formats, sizes, folder names and the note that tells clients which file to use.',
  'h1': 'What to include in a client’s logo package',
  'lead': 'Every logo version, in every colour it needs, as vector and pixel files. Sort them into clear folders and add one page that says which file goes where.',
  'published': '2026-11-25', 'modified': '2026-11-25',
  'body': '''
<p>Two months after handover, the sign maker wants an EPS, the web team wants an SVG, and the client has only kept a JPG from an email. A good package has the answer already in it.</p>

<h2>What a logo package is</h2>
<p>It’s the folder of finished logo files a client keeps and uses: every version of the logo, in every colour and format it needs. It isn’t the working file, and it isn’t a price tier.</p>

<h2>Logo versions</h2>
<p>Send the versions the brand will use, and nothing it won’t. Rejected concepts and working files stay with you.</p>
<table>
  <thead><tr><th>Version</th><th>Where it’s used</th></tr></thead>
  <tbody>
    <tr><td>Full logo, wide</td><td>Website headers, signs, letterheads</td></tr>
    <tr><td>Full logo, stacked</td><td>Square and tall spaces, packaging</td></tr>
    <tr><td>Mark</td><td>Profile pictures, app icons, favicons</td></tr>
    <tr><td>Logotype</td><td>Small heights, and next to a mark that’s already there</td></tr>
  </tbody>
</table>
<figure><img src="/img/articles/logo-versions.webp" width="1520" height="394" alt="ET Robotics full logo, mark and logotype" loading="lazy"><figcaption>Full logo, mark and logotype: ET Robotics</figcaption></figure>
<p>A logotype with no mark may only need one version, plus a short form for the profile picture.</p>

<h2>Colour versions</h2>
<ul>
  <li><b>Colour.</b> The main logo, for white and light backgrounds.</li>
  <li><b>Reversed.</b> The logo on the brand’s own colour.</li>
  <li><b>Black.</b> Stamps, engraving, receipts and one-ink print.</li>
  <li><b>White.</b> Dark backgrounds and dark photos. Warn the client that it looks empty on a white screen.</li>
  <li><b>Grey.</b> Optional. Partner and sponsor lists often ask for it.</li>
</ul>
<figure><img src="/img/articles/logo-colours.webp" width="1520" height="704" alt="ET Robotics logo in colour, two reversed versions, black, white and grey" loading="lazy"><figcaption>Colour, reversed on two brand colours, black, white and grey</figcaption></figure>

<h2>File formats</h2>
<table>
  <thead><tr><th>Format</th><th>What it’s for</th></tr></thead>
  <tbody>
    <tr><td>SVG</td><td>Websites and apps</td></tr>
    <tr><td>PNG</td><td>Slides, documents, social media and email, on a transparent background</td></tr>
    <tr><td>JPG</td><td>Forms and older apps that don’t take transparency</td></tr>
    <tr><td>PDF</td><td>Print shops, and sharing with anyone</td></tr>
    <tr><td>EPS</td><td>Signs, embroidery, vinyl and older software</td></tr>
    <tr><td>AI</td><td>The client’s next designer</td></tr>
  </tbody>
</table>
<p>PNG widths of 512, 1024 and 2048 px cover most jobs. For a favicon, add the mark at 16, 32 and 48 px, and simplify it if it fills in. Social networks often crop profile pictures to a circle, so centre the mark and leave room around it.</p>
<p>If the client prints often, agree CMYK values and spot colours with the printer, and keep those print files in a folder of their own. Figma doesn’t export AI or EPS, so see <a href="/guides/export-logo-files-from-figma/">how to export logo files from Figma</a>.</p>

<h2>Folders and file names</h2>
<p>Sort by version, then by format. A client looks for the mark first and the file type second.</p>
<pre>Northwind
      Which file to use.pdf
      Northwind Brand guidelines.pdf
      Fonts.txt
      Mark
            SVG
            PNG
            JPG
            PDF
            EPS
            AI
      Full logo
            …</pre>
<p>Name every file in the same order: brand, version, colour, size. <b>Northwind-Mark-Black-1024px.png</b> still makes sense after someone emails it on its own. Avoid “final”, dates and initials.</p>

<h2>The page that says which file to use</h2>
<p>Clients rarely know the difference between EPS and SVG, and they shouldn’t have to. One page answers it:</p>
<ul>
  <li><b>Jobs, not formats.</b> “Print shop: PDF” is easier to use than “PDF: print”.</li>
  <li><b>A few rules.</b> Scale evenly, keep the colours, leave clear space.</li>
  <li><b>Smallest sizes.</b> For screen and for print. Here’s <a href="/guides/logo-clear-space-and-minimum-size/">how to set them</a>.</li>
  <li><b>Brand colours.</b> HEX, RGB and CMYK values they can copy.</li>
</ul>

<h2>Guidelines and fonts</h2>
<p>Add the <a href="/guides/what-to-include-in-brand-guidelines/">brand guidelines</a> as a PDF. List the fonts with a link to each one. Don’t pass on font files unless the licence allows it.</p>

<h2>Make the package in Figma</h2>
<p>Add the logo versions to the <a href="/export/">Export tool in Brandfig</a>, then pick colours, formats and PNG sizes. It saves one zip, with a folder for each version. The guidelines, font list and Which file to use PDF can go in the same zip.</p>
{loop}

<h2>Before you send it</h2>
<ol>
  <li>Open one file of each format.</li>
  <li>Place a PNG on a dark slide to check its background is transparent.</li>
  <li>Open an SVG in a browser and zoom in on the edges.</li>
  <li>Check that the type is outlined, so nothing asks for a font.</li>
  <li>Download the zip from your own link and open it the way the client will.</li>
</ol>
''',
  'faq': [
    ('How many files should a logo package have?', 'As many as the brand needs. Three versions in four colours and six formats is already 72 files, before extra PNG sizes, so clear folders matter more than the count.'),
    ('Should I send the client an AI file?', 'If your agreement includes it, yes. It gives their next designer a clean vector to work from.'),
    ('Should I send the working Figma file?', 'Only if it’s part of the agreement. The logo package works without it.'),
    ('Do clients need both RGB and CMYK files?', 'RGB for anything on screen. CMYK when they print often. Confirm the values with the printer and ask for a proof.'),
    ('Can I include the fonts?', 'Only when the licence allows sharing. Otherwise, send the font names and where to get them.'),
  ],
}, {
  'tool': 'logo',
  'cat': 'Logo design',
  'slug': 'logo-clear-space-and-minimum-size',
  'short': 'Logo clear space and minimum size',
  'title': 'Logo clear space and minimum size, in Figma · Brandfig',
  'desc': 'Set logo clear space with a unit from the logo, find its minimum size for screen and print, and mark both in Figma.',
  'h1': 'How to set logo clear space and minimum size in Figma',
  'lead': 'Take a unit from the logo, such as its cap height, and keep that much space on every side. For minimum size, make the logo smaller until a detail fails, then go back up.',
  'published': '2026-11-25', 'modified': '2026-11-25',
  'body': '''
<p>You hand over a logo, and the next time you see it there’s a web address pushed against its edge. Or it’s on a pen, with the type filled in. Two small rules prevent most of that.</p>

<h2>What clear space is</h2>
<p>Clear space is the empty area around a logo. Text, other logos, busy photo details and the page edge stay out of it. It’s a minimum, so more room is always fine. You’ll also see it called an exclusion zone or a safe area.</p>

<h2>Pick a unit from the logo</h2>
<p>Use a part of the logo as the unit, not a fixed number. It then scales with the logo, on a business card or on a billboard.</p>
<table>
  <thead><tr><th>Unit</th><th>Good for</th></tr></thead>
  <tbody>
    <tr><td>Cap height</td><td>Logotypes, and logos with a mark and type</td></tr>
    <tr><td>Width of the mark</td><td>Compact marks. Often a half or a quarter of it</td></tr>
    <tr><td>Part of the logo’s height</td><td>Logos with nothing obvious to measure. Try a half or a quarter</td></tr>
    <tr><td>One part of the mark</td><td>A dot, a blade or a stroke people can spot</td></tr>
    <tr><td>Pixels</td><td>One fixed size only, such as an app header</td></tr>
  </tbody>
</table>
<p>One cap height on every side is a good place to start. Compare it with half and with two. Too little and the logo feels crowded. Too much and nobody follows the rule.</p>

<h2>Mark clear space in Figma</h2>
<ol>
  <li>Duplicate the logo and work on the copy.</li>
  <li>Draw a square as tall as a flat capital in the logotype, such as H or E. This is your unit. Round letters overshoot, so don’t measure those.</li>
  <li>Place a copy of the square on each side, touching the outermost edge of the logo.</li>
  <li>Draw a rectangle around the outside of the squares. That’s the clear space.</li>
  <li>Give the area a light, flat fill and send it behind the logo.</li>
  <li>Label the unit, such as “x = cap height”.</li>
  <li>Group the marks and name the group Clear space.</li>
</ol>
<figure><img src="/img/articles/clear-space.svg" width="1079" height="476" alt="Clear space of one cap height around the ET Robotics logo" loading="lazy"><figcaption>Clear space of one cap height. The squares show the unit.</figcaption></figure>
<p>Measure from the shape you can see. If the frame around the logo has padding, the space will come out too big.</p>

<h2>Find the minimum size</h2>
<p>Minimum size is the smallest the logo can go before it stops being clear. Test it instead of guessing.</p>
<ol>
  <li>Place the logo at 200, 120, 80, 60 and 40 px wide.</li>
  <li>View them at 100% zoom on a normal screen and on a phone.</li>
  <li>Find the first one where a gap closes, a thin stroke fades or a word is hard to read.</li>
  <li>Set the minimum one step above it.</li>
  <li>Print the same row at real size in millimetres, and repeat.</li>
</ol>
<figure><div class="sizes"><span><img src="/img/articles/et-logo.svg" width="200" height="33" alt="ET Robotics logo, 200 px wide">200</span><span><img src="/img/articles/et-logo.svg" width="120" height="20" alt="ET Robotics logo, 120 px wide">120</span><span><img src="/img/articles/et-logo.svg" width="80" height="13" alt="ET Robotics logo, 80 px wide">80</span><span><img src="/img/articles/et-logo.svg" width="60" height="10" alt="ET Robotics logo, 60 px wide">60</span><span><img src="/img/articles/et-logo.svg" width="40" height="7" alt="ET Robotics logo, 40 px wide">40</span></div><figcaption>The ET Robotics logo at each width, in px. The type goes before the mark does.</figcaption></figure>
<ul>
  <li><b>Screen and print are separate.</b> Give pixels for screen and millimetres for print.</li>
  <li><b>Each version has its own limit.</b> The mark can usually go smaller than the full logo.</li>
  <li><b>Say what to measure.</b> Write “24 px wide” or “24 px high”, not just 24 px.</li>
  <li><b>Plan what comes next.</b> Below the minimum, switch to the mark or a simpler version.</li>
  <li><b>Ask about the material.</b> Embroidery, engraving and vinyl have their own limits, so check with whoever makes it.</li>
</ul>

<h2>Mark it with Brandfig</h2>
<p>Open Clear space in the <a href="/logo/">Logo tool in Brandfig</a>. Choose cap height, mark width or your own pixel value, set how much goes around the logo, and press Mark clear space. You can show the unit marker, the measurements and a shaded zone. Apply it to the selected layers or to all the brand’s logos.</p>
<p>Enter the screen and print minimums you tested in the same place. Clear space can become a page in the <a href="/guidelines/">brand guidelines</a>, and the sizes appear on the Minimum size page.</p>

<h2>Write the rule</h2>
<p>Keep it to two lines a client can follow:</p>
<ul>
  <li>Keep one cap height clear on every side of the logo.</li>
  <li>Don’t use the full logo below 80 px wide on screen or 20 mm wide in print.</li>
</ul>
<p>Use your own tested numbers. These only show the wording.</p>
''',
  'faq': [
    ('How much clear space should a logo have?', 'One cap height, or a quarter to a half of the mark’s width, is a common starting point. Test it on real pages and adjust.'),
    ('What is the minimum size for a logo?', 'There’s no standard number. It depends on the thinnest stroke, the smallest gap and the type, so test each version on screen and on paper.'),
    ('Is clear space the same on every side?', 'Usually, because it’s easier to follow. A logo with an uneven shape can have different space per side if the rule stays clear.'),
    ('What is x in a clear space diagram?', 'The unit, taken from part of the logo. 2x means twice that part.'),
    ('Does clear space apply to favicons and app icons?', 'Not in the same way. They have very little room, so set their padding separately.'),
  ],
}, {
  'tool': 'guidelines',
  'cat': 'Brand guidelines',
  'slug': 'what-to-include-in-brand-guidelines',
  'short': 'What to include in brand guidelines',
  'title': 'What to include in brand guidelines: a checklist · Brandfig',
  'desc': 'A brand guidelines checklist: logo, colour, type, imagery and examples. What each page should say, and what a small brand can skip.',
  'h1': 'What to include in brand guidelines: a checklist',
  'lead': 'Cover the logo, colour and type, then show them working together. Add voice, photography and layouts when the brand has them.',
  'published': '2026-11-25', 'modified': '2026-11-25',
  'body': '''
<p>A new marketing hire opens the file on their first day. They want to know which logo to use, which blue is right and which font goes in a headline. Good guidelines answer those in a minute, without a call to you.</p>

<h2>The pages every brand needs</h2>
<table>
  <thead><tr><th>Page</th><th>What it answers</th></tr></thead>
  <tbody>
    <tr><td>Logo and versions</td><td>Which logo do I use here?</td></tr>
    <tr><td>Clear space and minimum size</td><td>How close and how small can it go?</td></tr>
    <tr><td>Logo on backgrounds</td><td>Which version works on this colour?</td></tr>
    <tr><td>Logo misuse</td><td>What should I never do to it?</td></tr>
    <tr><td>Colour palette</td><td>What are the exact values?</td></tr>
    <tr><td>Typefaces and hierarchy</td><td>Which font, weight and size?</td></tr>
    <tr><td>Examples</td><td>What does it look like together?</td></tr>
    <tr><td>Files and contact</td><td>Where are the files, and who do I ask?</td></tr>
  </tbody>
</table>

<h2>Logo</h2>
<ul>
  <li><b>Show each version large.</b> Say when to use it in one line.</li>
  <li><b>Set the space.</b> Give <a href="/guides/logo-clear-space-and-minimum-size/">clear space and minimum sizes</a> for screen and print.</li>
  <li><b>Show it on real backgrounds.</b> White, dark and the brand’s colours.</li>
  <li><b>Keep misuse short.</b> Six likely mistakes are more useful than twenty unlikely ones.</li>
  <li><b>Show construction if it explains something.</b> Here’s <a href="/guides/logo-construction-grid-in-figma/">how to draw a construction grid</a>.</li>
</ul>

<h2>Colour</h2>
<ul>
  <li><b>Give every colour a role.</b> Primary, secondary, accent, neutral.</li>
  <li><b>List the values.</b> HEX, RGB and CMYK. Add a spot colour if the brand prints often.</li>
  <li><b>Show the amounts.</b> A palette with one dominant colour looks different from one with five equal ones.</li>
  <li><b>Show text pairs that are easy to read.</b> Check the contrast. WCAG AA asks for 4.5 to 1 for normal text and 3 to 1 for large text.</li>
</ul>
<figure><img src="/img/articles/guideline-palette.webp" width="960" height="540" alt="Colour palette page from the ET Robotics guidelines" loading="lazy"><figcaption>Colour palette page, made with Brandfig for ET Robotics</figcaption></figure>

<h2>Type</h2>
<ul>
  <li><b>Name the fonts and weights.</b> Say where to get them.</li>
  <li><b>Set roles.</b> Headline, subhead, body and caption, with size and line height.</li>
  <li><b>Pick a fallback.</b> For email and slides, where the brand font may not load.</li>
</ul>
<figure><img src="/img/articles/guideline-typefaces.webp" width="960" height="540" alt="Typefaces page from the ET Robotics guidelines" loading="lazy"><figcaption>Typefaces page from the same guide</figcaption></figure>

<h2>Add these when the brand has them</h2>
<ul>
  <li><b>Purpose and values.</b> Short, and in the client’s own words.</li>
  <li><b>Voice.</b> A few traits, with a line written the right way and the wrong way.</li>
  <li><b>Photography.</b> Subject, light and crop, with pictures to follow and to avoid.</li>
  <li><b>Pattern, icons and shapes.</b> How they’re made and where they go.</li>
  <li><b>Stationery, social, packaging, website.</b> Only what the brand will really use.</li>
  <li><b>Motion.</b> If the logo or the type moves.</li>
</ul>
<figure><img src="/img/articles/guideline-app-icons.webp" width="960" height="540" alt="App icons page from the ET Robotics guidelines" loading="lazy"><figcaption>App icons page, built from the mark</figcaption></figure>

<h2>How long should it be?</h2>
<table>
  <thead><tr><th>Brand</th><th>Length</th><th>Cover</th></tr></thead>
  <tbody>
    <tr><td>New or very small</td><td>One page</td><td>Logo, colours, type</td></tr>
    <tr><td>Small business</td><td>10 to 20 pages</td><td>The pages every brand needs</td></tr>
    <tr><td>Growing team</td><td>20 to 40 pages</td><td>Plus voice, imagery and layouts</td></tr>
    <tr><td>Several teams or markets</td><td>40 or more</td><td>Plus each channel and product</td></tr>
  </tbody>
</table>
<p>These are starting points. Leave a page out when it has nothing useful to say.</p>

<h2>Write rules people can follow</h2>
<ul>
  <li><b>Say what to do first.</b> “Use the white logo on photos” is easier to follow than a list of bans.</li>
  <li><b>One idea per page.</b> A short line and a clear picture.</li>
  <li><b>Give the reason when it isn’t obvious.</b> People keep rules they understand.</li>
  <li><b>Add a date.</b> So everyone knows which version they have.</li>
</ul>

<h2>Build them in Figma</h2>
<p>The <a href="/guidelines/">Guidelines tool in Brandfig</a> has pages for the logo, colour, type, graphic elements, photography and applications, in twelve templates. Add your logos, colours and type, choose the pages, and build. There’s also a one-pager.</p>
{loop}
<p>Everything is editable in Figma. Purpose, values and voice come with placeholder text to rewrite, and photo and mockup pages have empty areas for your own work. Save the result as a PDF, or put it in the <a href="/guides/client-logo-package/">client’s logo package</a>.</p>
''',
  'faq': [
    ('What is the most important part of brand guidelines?', 'The logo, colour and type pages. They answer the questions people ask most often.'),
    ('Does a small business need brand guidelines?', 'Yes, but a short set. One page with the logo, colours and type is enough to start.'),
    ('What’s the difference between a brand book and brand guidelines?', 'People use the terms for the same thing. When there’s a difference, a brand book covers the story and values, and guidelines cover how to use the design.'),
    ('Should brand guidelines be a PDF or a website?', 'A PDF is easy to send and keep. A website suits a large team that updates often. Many brands begin with a PDF.'),
    ('How often should brand guidelines be updated?', 'Whenever the logo, colours or type change, or when people keep asking the same question.'),
  ],
}]
CATS = ['Logo design', 'Logo presentations', 'Brand guidelines', 'Bento grids', 'Logo files']   # shown once it has a guide
def cat_id(c): return c.lower().replace(' ', '-')
def guide_card(g, tag='h2'):
    return f'<a class="card" data-cat="{cat_id(g["cat"])}" href="/guides/{g["slug"]}/"><img src="/img/covers/{g["slug"]}.webp" width="1200" height="1200" alt="" loading="lazy"><span class="cat">{g["cat"]}</span><{tag}>{g["h1"]}</{tag}><p>{g["desc"]}</p></a>'
def guides_index():
    title = 'Logo and brand design guides for Figma · Brandfig'
    desc = 'Practical guides for logo and brand designers working in Figma: construction grids, clear space, brand guidelines and logo files.'
    used = [c for c in CATS if any(g['cat'] == c for g in GUIDES)]
    items = ''.join(guide_card(g) for c in used for g in GUIDES if g['cat'] == c)
    tabs = '<button type="button" data-f="" aria-pressed="true">All</button>' + ''.join(f'<button type="button" data-f="{cat_id(c)}" aria-pressed="false">{c}</button>' for c in used)
    crumbs = {'@type': 'BreadcrumbList', 'itemListElement': [
        {'@type': 'ListItem', 'position': 1, 'name': 'Brandfig', 'item': SITE + '/'},
        {'@type': 'ListItem', 'position': 2, 'name': 'Guides', 'item': SITE + '/guides/'}]}
    return head(title, desc, '/guides/', ldjson({'@context': 'https://schema.org', '@graph': [crumbs]})) + f'''
<section class="tool-hero wrap">
  <h1><span class="eyebrow">Guides</span> Logo and brand design in Figma.</h1>
</section>
<section class="wrap library">
  <div class="filter" role="group" aria-label="Category">{tabs}</div>
  <div class="guides">{items}</div>
</section>
<script>
// Category filter; the address keeps the choice (/guides/#logo-files)
const tabs = [...document.querySelectorAll('.filter button')];
function pick(f) {{
  if (!tabs.some(b => b.dataset.f === f)) f = '';
  tabs.forEach(b => b.setAttribute('aria-pressed', b.dataset.f === f));
  document.querySelectorAll('.guides .card').forEach(c => {{ c.hidden = f && c.dataset.cat !== f; }});
}}
tabs.forEach(b => b.addEventListener('click', () => {{ pick(b.dataset.f); history.replaceState(null, '', b.dataset.f ? '#' + b.dataset.f : location.pathname); }}));
addEventListener('hashchange', () => pick(location.hash.slice(1)));
pick(location.hash.slice(1));
</script>
''' + FOOTER + SCRIPT + TAIL
def guide(g):
    url = f"{SITE}/guides/{g['slug']}/"
    crumbs = {'@type': 'BreadcrumbList', 'itemListElement': [
        {'@type': 'ListItem', 'position': 1, 'name': 'Brandfig', 'item': SITE + '/'},
        {'@type': 'ListItem', 'position': 2, 'name': 'Guides', 'item': SITE + '/guides/'},
        {'@type': 'ListItem', 'position': 3, 'name': g['short'], 'item': url}]}
    # three others: the same tool first
    more = ''.join(guide_card(o, 'h3') for o in sorted((o for o in GUIDES if o is not g), key=lambda o: o['tool'] != g['tool'])[:3])
    art = {'@type': 'Article', 'headline': g['h1'], 'description': g['desc'], 'image': f"{SITE}/img/covers/{g['slug']}.jpg", 'mainEntityOfPage': url,
           'datePublished': g['published'], 'dateModified': g['modified'],
           'author': {'@type': 'Person', 'name': 'Nilesh Shukla'}, 'publisher': {'@type': 'Organization', 'name': 'Brandfig', 'url': SITE + '/'}}
    ld = ldjson({'@context': 'https://schema.org', '@graph': [art, crumbs, faq_ld(g['faq'])]})
    return head(g['title'], g['desc'], f"/guides/{g['slug']}/", ld).replace(SITE + '/img/og.jpg', f"{SITE}/img/covers/{g['slug']}.jpg") + f'''
<article class="article wrap">
  <a class="eyebrow" href="/guides/#{cat_id(g['cat'])}">{g['cat']}</a>
  <h1>{g['h1']}</h1>
  <p class="lead">{g['lead']}</p>
  <img class="cover" src="/img/covers/{g['slug']}.webp" width="1200" height="1200" alt="{g['short']}">
  {g['body'].replace('{loop}', loop(g['tool'], g['tool'].title() + ' tool at work'))}
  <h2>Questions, answered.</h2>
  {faq_html(g['faq'])}
</article>
<section class="block wrap library">
  <div class="head"><h2>More guides</h2></div>
  <div class="guides">{more}</div>
</section>
''' + FOOTER + SCRIPT + TAIL

if __name__ == '__main__':
    import os
    open('index.html', 'w', encoding='utf-8').write(home())
    for t in TOOLS:
        os.makedirs(t[0], exist_ok=True)
        open(f'{t[0]}/index.html', 'w', encoding='utf-8').write(tool(t))
    os.makedirs('guides', exist_ok=True)
    open('guides/index.html', 'w', encoding='utf-8').write(guides_index())
    for g in GUIDES:
        os.makedirs(f"guides/{g['slug']}", exist_ok=True)
        open(f"guides/{g['slug']}/index.html", 'w', encoding='utf-8').write(guide(g))
    import datetime
    today = datetime.date.today().isoformat()
    LEGAL_DATE = '2026-10-29'   # last time the legal pages changed
    urls = ['/'] + [f'/{t[0]}/' for t in TOOLS] + ['/guides/'] + [f"/guides/{g['slug']}/" for g in GUIDES] + ['/terms.html', '/privacy.html', '/refund.html']
    sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    sm += [f'  <url><loc>{SITE}{u}</loc><lastmod>{LEGAL_DATE if u.endswith('.html') else today}</lastmod></url>' for u in urls] + ['</urlset>', '']
    open('sitemap.xml', 'w', encoding='utf-8').write(chr(10).join(sm))
    open('robots.txt', 'w', encoding='utf-8').write(chr(10).join(['User-agent: *', 'Allow: /', 'Disallow: /notes/', '', f'Sitemap: {SITE}/sitemap.xml', '']))
    print('built: index.html, ' + ', '.join(f'{t[0]}/' for t in TOOLS))
