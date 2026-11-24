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
            ('What’s the difference between a base grid and a construction grid?', 'A base grid comes first: it’s what you sketch the logo on. Construction comes after: it shows the lines and circles behind the finished shape. The Logo tool makes both.'),
            ('How is clear space measured?', 'By the cap height of the type, the width of the mark or a pixel value you set. Minimum sizes for screen and print sit beside it.'),
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
    'faq': [('What should brand guidelines include?', 'The logo and its versions, clear space, minimum sizes, the colour palette, typefaces and how it all comes together. You choose which pages go in and add your own words.'),
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
            ('Which logo files should I give a client?', 'Vector files for print and design work (AI, EPS, PDF, SVG) and PNG or JPG for everyday screen use, in colour, reversed, black and white.'),
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
    <div><h4>Product</h4><a href="/#pricing">Pricing</a><a href="/#faq">FAQ</a><a href="{FIGMA}">Figma Community</a><a href="/guides/export-logo-files-from-figma/">Logo export guide</a></div>
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

<h2>What to put in a client’s logo package</h2>
<ul>
  <li><b>Every version.</b> The full logo, the mark and the logotype.</li>
  <li><b>Every colour it needs.</b> Full colour, reversed, black and white. Grey helps for single-ink jobs.</li>
  <li><b>Vector and pixel files.</b> AI, EPS, PDF and SVG, with PNG in a few widths.</li>
  <li><b>Clear names.</b> Brand, version, colour, size: <b>Northwind-Mark-Black-1024px.png</b>.</li>
  <li><b>A short guide.</b> One page that says which file to use where, next to the <a href="/guidelines/">brand guidelines</a>.</li>
</ul>
<p>Colour on screen is RGB and print is CMYK, so agree the CMYK values with the printer and ask for a proof before a big run.</p>
''',
  'faq': [
    ('Can Figma export AI files?', 'No. Figma exports PNG, JPG, SVG and PDF. Open the SVG or PDF in Illustrator and save it as AI, or use a plugin such as <a href="/export/">Brandfig</a> that saves AI files from Figma.'),
    ('Can Figma export EPS files?', 'No. Save the EPS from Illustrator, or make it in Figma with a plugin such as <a href="/export/">Brandfig</a>.'),
    ('Is SVG or PNG better for a logo?', 'SVG for websites and apps, because it stays sharp at any size. PNG wherever SVG isn’t accepted, such as documents and social media.'),
    ('What size should a PNG logo be?', 'At least as wide as it will show, and twice that for sharp phone and laptop screens. 512, 1024 and 2048 px cover most uses.'),
    ('Why does the font change when a client opens the logo?', 'The type is still live text and the client doesn’t have the font. Outline the type before you export.'),
  ],
}]
def guide(g):
    url = f"{SITE}/guides/{g['slug']}/"
    crumbs = {'@type': 'BreadcrumbList', 'itemListElement': [
        {'@type': 'ListItem', 'position': 1, 'name': 'Brandfig', 'item': SITE + '/'},
        {'@type': 'ListItem', 'position': 2, 'name': g['short'], 'item': url}]}
    art = {'@type': 'Article', 'headline': g['h1'], 'description': g['desc'], 'image': SITE + '/img/og.jpg', 'mainEntityOfPage': url,
           'datePublished': g['published'], 'dateModified': g['modified'],
           'author': {'@type': 'Person', 'name': 'Nilesh Shukla'}, 'publisher': {'@type': 'Organization', 'name': 'Brandfig', 'url': SITE + '/'}}
    ld = ldjson({'@context': 'https://schema.org', '@graph': [art, crumbs, faq_ld(g['faq'])]})
    return head(g['title'], g['desc'], f"/guides/{g['slug']}/", ld) + f'''
<article class="article wrap">
  <h1><span class="eyebrow">Guide</span> {g['h1']}</h1>
  <p class="lead">{g['lead']}</p>
  {g['body'].replace('{loop}', loop('export', 'Export tool at work'))}
  <h2>Questions, answered.</h2>
  {faq_html(g['faq'])}
</article>
''' + FOOTER + SCRIPT + TAIL

if __name__ == '__main__':
    import os
    open('index.html', 'w', encoding='utf-8').write(home())
    for t in TOOLS:
        os.makedirs(t[0], exist_ok=True)
        open(f'{t[0]}/index.html', 'w', encoding='utf-8').write(tool(t))
    for g in GUIDES:
        os.makedirs(f"guides/{g['slug']}", exist_ok=True)
        open(f"guides/{g['slug']}/index.html", 'w', encoding='utf-8').write(guide(g))
    import datetime
    today = datetime.date.today().isoformat()
    LEGAL_DATE = '2026-10-29'   # last time the legal pages changed
    urls = ['/'] + [f'/{t[0]}/' for t in TOOLS] + [f"/guides/{g['slug']}/" for g in GUIDES] + ['/terms.html', '/privacy.html', '/refund.html']
    sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    sm += [f'  <url><loc>{SITE}{u}</loc><lastmod>{LEGAL_DATE if u.endswith('.html') else today}</lastmod></url>' for u in urls] + ['</urlset>', '']
    open('sitemap.xml', 'w', encoding='utf-8').write(chr(10).join(sm))
    open('robots.txt', 'w', encoding='utf-8').write(chr(10).join(['User-agent: *', 'Allow: /', 'Disallow: /notes/', '', f'Sitemap: {SITE}/sitemap.xml', '']))
    print('built: index.html, ' + ', '.join(f'{t[0]}/' for t in TOOLS))
