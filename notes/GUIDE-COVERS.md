# Guide covers

Every guide on /guides/ gets a cover before it is shown to the owner. All covers are **1:1** by default.

## Files
- Source: `notes/covers.py`, one function per guide, drawn as SVG on a 1200 x 1200 canvas.
- `img/covers/<slug>.webp`, 1200 x 1200: the card on /guides/, the More guides cards and the top of the guide.
- `img/covers/<slug>.jpg`, 1200 x 630: the share image. The square sits centred on the same ground. Made automatically.

## Rules
- **Drawn for its topic.** One idea that explains the guide. Never a crop of a finished design, deck, post or plugin screenshot.
- **Breathing space:** everything is drawn at 80% of the canvas (`FIT` in covers.py). Keep artwork inside it; only a full background pattern may run off the edge.
- **Explain it.** The owner prefers diagrams that show how it works (the node graph) over objects and metaphors.
- **One subject, with air.** It must read at card size (about 380 px).
- **Same ground:** flat `#1c1c20`. Same type: Geist, only when the idea needs words.
- **Flat colour only.** No gradients, glows, blur, shadows or 3D. No letter spacing.
- **A different sample brand on each cover,** with its own palette. ET Robotics is only on construction and clear space.
  Make up a simple mark and name for the others. No real companies, no logoipsum.
- **Never Brandfig's icon.** (The owner asked for it to be left out.)
- **No cropped logos.** Objects may bleed off the edge, logos may not.
- **Vary the composition.** Two covers next to each other shouldn't share a layout. Recolouring doesn't count.
- Pink `#ff2d78` is only for construction lines. Blue `#133fff` marks a selection, a measure or a tool.
- UI icons use Lucide's exact paths.
- Other sites' covers (Akrivi's Learn page) are a direction for the thinking, never something to copy.

## Covers so far
| Guide | Idea | Sample brand | Status |
|---|---|---|---|
| Construction grid | Half lines and anchors, half finished mark | ET Robotics, white | Live 25 Nov 2026 |
| Clear space | A crowded grid that keeps its distance | ET Robotics, white and blue | Live 25 Nov 2026 |
| Brand guidelines | The checklist itself: some done, one being ticked, one to go | No brand, lilac | Live 25 Nov 2026 |
| Export logo files | One mark six times, each drawn as its format | Clover mark, orange and cream | Live 25 Nov 2026 |
| Client logo package | A node graph: one logo, its versions, its files, one path lit (the owner's idea) | Kora, mint | Live 25 Nov 2026 |

## Rejected, don't repeat
- Crops of the Community images (25 Nov 2026): "copy pasting our design".
- The same brand on every cover.
- **No containers at all** for the logo package: no box, folder, case, bag or zip. Tried:
  a folder with tiles, an open box (twice), then a swatch fan, a nine-tile poster and a file list, a case laid out like a bento grid, a zip ("what's up with the chain").
- The stack of coloured section tabs for brand guidelines.
- Brandfig’s icon on a cover. The Sola sun brand in the yellow box.

## Adding one
1. Write down the guide's idea in one sentence. If it needs two, pick a simpler one.
2. Add a function to `notes/covers.py` and its slug to `COVERS`.
3. Run `PYTHONUTF8=1 python notes/covers.py`, then look at it full size and at 380 px, next to the others.
4. Add it to the table above, then `PYTHONUTF8=1 python build.py`.
