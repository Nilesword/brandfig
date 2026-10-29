# getbrandfig.com v2: redesign working notes

**Live since 2026-10-26.** The site now lives at the repo root: `build.py` writes `index.html` and `logo/`, `concepts/`,
`guidelines/`, `bento/`, `export/` (clean URLs), styled by `site.css`; assets in `img/` (decks, guides, loops, panels,
steps). Edit copy in `build.py`, run `python build.py`, commit, push. These notes are excluded from the published site
(`_config.yml`).

**2026-10-29 refinements:** the hero stage shrinks with the window (`--stage-h` in `site.css`) so the headline, sub-line
and buttons show on load on laptops; the panel stays whole and scales with it. Hero pages and panel are WebP (half the
weight). Link previews: `img/og.jpg` (made from `notes/og.html`), Open Graph and Twitter tags and a canonical URL on every
page, `img/apple-touch-icon.png`. Old screenshots removed from `img/`. Older paths below that start with `v2/` or `img/...` inside v2 now live at the root.

Read this first when working on the new site. It holds every decision so far, so a new chat can pick up without
losing context. Keep it current after each session. The live site (`../index.html`, `../style.css`) is untouched
until the owner says to ship; nothing here is committed or pushed yet.

Sources of truth: product facts in `../../brandkit-figma-plugin/README.md`, voice in
`../../brandkit-figma-plugin/docs/brand-voice.md`, art direction in
`../../brandkit-figma-plugin/docs/community-design-direction.md`, the original page brief in
`../../brandkit-figma-plugin/docs/website-redesign-brief.md`.

## Process
- **Figma first**, then code. Design lives in the lab file (key `KiYNaekzc3oc3scGcuDK2c`), page **Website · v2**:
  desktop frame `getbrandfig.com · desktop 1440`, and the section **Website assets · panels** holds every panel image
  made for the site, with a note on how each was made. Every new panel goes there too.
- Motion and responsive behaviour are tried in a live prototype here (`hero-prototype.html`), because Figma can't play
  them. Preview it with the `brandfig-site` entry in `GitHub/.claude/launch.json` (port 5210):
  `http://localhost:5210/v2/hero-prototype.html`.

## Decided
- **Message:** everything is about Brandfig doing the repetitive parts so designers hand over faster. Tagline
  "Brand work, automated." Category line "Automation for brand designers, inside Figma". Sub-line (2026-10-20, automation voice): "Brandfig automates your brand design workflow, from construction
  to the final files. Create faster, ship sooner." Never relief framing ("no more redrawing", "tired of").
  Under the buttons: "3 days free, then $7/month. Cancel anytime." (no free tier since 2026-10-20) then
  the platforms as buttons, in the site's pill style (owner: small tags didn't fit): **Get it on Figma** with the Figma
  logo (links to the Community page, on every page), and a quieter, non-clickable **Adobe Illustrator · Coming soon** pill
  (dark #141418, the Illustrator app icon: #330000 square, orange #FF9A00 "Ai" in Geist). Hero only (owner removed it from Pricing). Never
  "Figma plugin today", never a date (the Illustrator panel is in development in `../../brandfig-illustrator`).
- **Structure:** the tools are told as three stages, not five separate blocks: **Create faster** (construction, base
  grids, clear space, lockups) · **Present sooner** (concept decks, bento) · **Hand over ready** (guidelines, export).
- **Look:** dark ink #0A0A0C, text #EDEDEA, quiet #8B8B93, Brandfig blue #133FFF for the main button. Flat colour, no
  glow or gradients. Geist only, letter spacing 0. Wide side margins (content 1200 px).
- **Panel rule:** never a crop of a panel that hides what it is, and never a redrawn one. Show the **real panel**
  (the plugin's current `ui.html`), whole, at the size Figma opens it: **360 × 720**, no Figma title bar. The content
  past 720 px is cut off by that size, just as in Figma. It is **filled** so it looks in use.
- **Hero panel:** Logo tool, **Construction** tab (owner's pick 2026-10-20: the tab looks better and shows we do
  construction too, while the rows show decks and guidelines). Horizontal, Vertical, Diagonal, Circles and Anchors on,
  Key lines, Draw construction ready, "Redraw when the logo changes" on. Caption under the hero: "Construction, concept
  decks and brand guidelines, built from your brand. Everything stays editable."
  The earlier Concepts-tab panel (Northwind / Wayfinder, `img/panels/concepts-filled@2x.png`) is kept for the
  Present sooner section.
- **Hero motion:** two rows of real template pages flow out to the right from **behind** the panel (desktop: nothing
  shows left of the panel). Top row 80 s loop, bottom 110 s. Never pauses on hover (owner's call);
  still under reduced motion. Phone (≤ 760 px): the rows run full width above
  the panel, which overlaps the lower row by 72 px; panel 300 px wide.
- **Slides (curated):** real plugin output only. "Northwind" appears once (the deck cover). No placeholder pages
  (the guide's construction / clear space / business card pages are intentionally "run the tool here" areas) and no
  Logoipsum wordmark. No "Overview" dividers and at most two type pages, so nothing repeats.
  - Top row: Northwind, Transit dot pattern, Kestrel, Fieldwork, Sundae, Riot Club, Basalt.
  - Bottom row: Northwind colour, Funhaus typefaces, Kestrel brief, Full Circle pattern, Fieldwork concept opener,
    Arcadia palette, Basalt type, Riot Club next steps, Transit contents, Sundae three words, Basalt thanks.
    Northwind's colour page comes first so it matches the panel. Only two colour pages (owner: too many palettes).
  - Owner swapped out (2026-10-20): Full Circle "Overview" divider, Transit app icons, Kestrel type. Many deck pages
    (Digital, Side by side, In use, References) are out because they show the Logoipsum wordmark or empty photo areas;
    the guides' pattern pages are empty "place the pattern" areas except Full Circle and Transit.
- **Not doing (for now):** running the Logo tool in Figma to make construction / clear space slides.

## Assets (`img/`)
- `img/decks/*.png`, `img/guides/*.png`: 960 × 540 exports of the lab file's template pages (Presentation designs,
  Plugin build · lab templates). Guide file names use the current template names (Northlight = signal, Blocklab =
  module, Loudhouse = statement, Funhaus = play, Full Circle = shape, Ribbon = bands, Bluebird = tone, Arcadia = arch).
- `img/panels/logo-construction@2x.png`: the hero panel, 720 × 1440 (2x).
- `img/panels/concepts-filled@2x.png`: Concepts tab filled with Northwind, for the Present sooner section.
- `img/wordmark.svg`: copy of `../img/wordmark.svg`.
- `slide-set.png`: both rows in order, for review. `hero-motion-preview.mp4`, `hero-phone-preview.png`: earlier previews.

## How to remake a panel image
In `../../brandfig-video`: `node sync-plugin-ui.mjs` (copies the plugin's current `ui.html`), then
`node panel-window.mjs <tool> <mode> <out.png> [on]`, e.g. `node panel-window.mjs logo construction out/panel.png draft.showCircles,draft.liveRedraw`
(`on` switches on controls by their `data-p`).
`panel-window.html` boots the real panel the way Figma does and answers its requests (logo previews, font list);
edit its `DOC` for different content. Then copy the PNG into `img/panels/` and upload it to the Figma assets section.

## Site structure (owner, 2026-10-20: split instead of one huge page)
- **Home** (`getbrandfig.com · desktop 1440`): hero · How it works · Tools (tabs showcase with the loops) · Pricing ·
  FAQ · footer. The "Why it's faster" band was removed (owner, 2026-10-22): the Tools loops already show it.
- **One page per tool** (`getbrandfig.com/<tool> · desktop 1440`, side by side on the Figma page): nav · tool hero
  (stage · tool, headline from the bank, sub-line, buttons) · real filled panel(s) + result · What's inside (one card per
  mode) · footer CTA.
  - `/logo` (Create faster): Clear space panel + the owner's real construction run on the pinwheel.
  - `/concepts` (Present sooner): Concepts panel + six Northwind deck pages.
  - `/guidelines` (Hand over ready): Brand assets panel + six Transit guide pages.
  - `/bento` (Present sooner): Bento panel (frame selected) + result area. **To do (owner):** run Bento on a 1920 × 1080
    frame and paste it in (note above that page in Figma).
  - `/export` (Hand over ready): two panels, Logos and Files ("Export 87 files"), plus "What's in the zip": the
    real folder tree from `src/main/export.js` with default settings (Northwind.zip > Northwind > Mark / Logotype /
    Full logo, each AI EPS PDF PNG SVG; Fonts.txt, Which file to use.pdf, guidelines PDF; 87 files).
- Home middle sections, each with its own look (owner: the card run felt bland): How it works steps each lead with a
  picture (the pinwheel selected with Figma's selection box; the five tool icons with Concepts on; the owner's real
  construction); Tools is a **tabs showcase** (owner picked it after two misses on cards): the five tools down the left (icon +
  name; the selected one shows its line and "See the … tool"), and on the right that tool's real filled panel plus its
  output. Figma shows Concepts selected (concepts panel + six Northwind pages). On the site each tab swaps in its own
  pair: Logo = Clear space panel + the construction run; Guidelines = Brand assets panel + Transit pages; Bento = Bento
  panel + (real bento still to come); Export = Files panel + the zip tree; Why it's faster is a full-width blue band of big white lines, no cards.
- Home Tools cards carry each tool's panel icon (Lucide, same as the plugin tabs). Pricing ends with the Illustrator
  "Coming soon" line.
- **Support email: contact@getbrandfig.com** (footer, Contact links). Already in the plugin; the live site's
  index/privacy/refund/terms now use it too (edited locally, not pushed).
- Panels in `img/panels/` (all also in the Figma assets section): logo-construction (home hero), logo-clear,
  concepts-filled, guidelines-assets, bento (`FRAME=1`), export-logos, export-files.
  `panel-window.html` holds Northwind's brand assets (`doc.brand`) so Guidelines and Export fill in.

- Transit's Typefaces page now has its own fuller layout in the plugin (`S.typefacesPage` in `src/main/skins.js`:
  specimen, name, use, a short note on how to set it, character set). The other templates keep the shared page.
  Lab page 406:731 and its copy on the Guidelines page match it; not committed.

## Footer (2026-10-22, all six pages)
Closing CTA ("Brand work, automated.", "Try every tool free for 3 days. Cancel anytime.", Start free trial + Get it on Figma),
then columns: wordmark + category line + contact@getbrandfig.com · Tools (five) · Product (Pricing, FAQ, Figma Community)
· Follow (Instagram, Threads) · Legal (Terms, Privacy, Refunds); bottom line "© 2026 Brandfig" and "Made by Nilesh Shukla
(Nilesword)" (no country). Space only, no rules.

## Tool loops (2026-10-21)
- `img/loops/<tool>.mp4` + `<tool>.jpg` (logo, concepts, guidelines, bento, export): silent, seamless loops of the real
  panel doing each tool's steps with the real output beside it (from `../../brandfig-video/features.html` loop mode;
  remake with `node render-loops.mjs` there). 1404 × 1080, H.264, 0.2 to 0.6 MB. Poster = the finished state.
- Used in the home Tools showcase (tab list narrowed to 232 px, video 936 × 720) and on each tool page (1200 × 923),
  replacing the panel + result images. In code: `<video autoplay muted loop playsinline preload="none" poster>`; load
  the clip when its tab opens; reduced motion shows the poster only.

## Built in code (2026-10-24, not live yet)
`build.py` writes `index.html` and the five tool pages (`logo.html`, `concepts.html`, `guidelines.html`, `bento.html`,
`export.html`) from shared parts (nav, buttons, footer, FAQ), styled by `site.css`. Edit copy in `build.py`, then
`python build.py`. Uses the Dodo checkout links (monthly, yearly) and the Community link from the live site; Instagram
and Threads point to @getbrandfig; legal links go to the live `../terms.html` etc. Loops lazy-load and play only when
visible; reduced motion shows the posters. Preview: `http://localhost:5210/v2/index.html`. The live site (`../index.html`)
is untouched until the owner says to ship; nothing committed.

## Next
- **Hero is layout B, product first (owner, 2026-10-20; the old eyebrow / headline / sub / buttons stack read like
  Akrivi's):** nav, then the stage (panel left, pages flowing out from behind it), then a one-line "Brand work,
  automated." (104 px), the sub-line, the three buttons in one row and the price note. No eyebrow, no caption.
0. **Done 2026-10-20:** no free tier. Every tool is Pro with the 3-day card trial; the plugin opens a welcome sheet on
   first launch and settings stay explorable without a license. Hero note, prototype and the live site's pricing and
   FAQ are updated.
   **Plan choice (no monthly/yearly toggle on v2):** the two pricing cards are the choice. "Monthly · $7/month" and
   "Yearly · $56/year, save 33%" (blue, featured), each with its own "Start free trial" button that opens that
   plan's Dodo checkout (both products carry the 3-day trial). Every other trial button on the site (nav "Try free
   for 3 days", hero, footer, tool pages) scrolls to `#pricing` instead of going straight to a checkout. Subhead:
   "Every tool, one key for two computers. Pick a plan; both start with 3 free days."
1. Owner reviews home + tool pages in Figma; runs Bento for the Bento page.
2. Build the pages in code (`index.html` + one HTML per tool, shared `style.css`); phone at 375 px; keep the Dodo and
   Community links.

## Open ideas (not decided)
- A one-time "build moment" on load: a cursor clicks the panel's main button, then the rows start flowing.
