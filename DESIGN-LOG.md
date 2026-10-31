# DADA log: SHADW Game Suite site

## 1. Traversal Plan (run 1, 2026-10-31)

**Brief in one sentence:** a multi-page static site that sells the SHADW Game Suite (one project file and one CLI
over SHADW Terrain, Forge, KeyForge and shadw.cloud) to game studios, honest that G0–G1 are built and G2–G5 are
planned, and shows the games made with it, including Brine & Brie: Shipwright.

- **Mode: Adaptive.** The site serves a public (studios, the owner's portfolio visitors). Governing criterion: MAYA.
- **Run type: Full** (new work).
- **Bound:** the owner's standing rule caps critic rounds at a fixed number; set to **2 WHOLE rounds**. The panel is
  **single-voice** (one writer takes each seat in turn from its seat file, no subagents) to keep token use modest,
  which the task asked for. Single-voice is not an independent panel; the Compliance Check says so.

### Tooling inventory

| Job | Tool used |
|---|---|
| Anchor graph and Frontier | none available beyond the Mermaid text; Frontier kept by hand below |
| Workflow state | the app's task list (update_plan) |
| Panel | single-voice, sequential; no subagents |
| Choose the panel | `scripts/pick_panel.py --mode adaptive --run-type full` |
| Measure the artifact | the built-in browser (screenshots, `javascript_tool` bounding-box and overflow probes) |
| Persist the log | this file |

### Seed

- Stance: "An Incomplete Manifesto for Growth (Bruce Mau)"
- Rules: "Grid Systems in Graphic Design (Josef Müller-Brockmann)" -> codifies -> "International Typographic Style
  (Swiss Style)"; "Designing Programmes (Karl Gerstner)" -> programme method of -> the same.
- Breaker: "Making and Breaking the Grid (Timothy Samara)"
- Counterpoint by dotted edge: "Making and Breaking the Grid (Timothy Samara)" -.-> loosens -> "Grid Systems in
  Graphic Design (Josef Müller-Brockmann)"
- Welcome: "MAYA: Most Advanced Yet Acceptable (Raymond Loewy)"

### Panel (from pick_panel.py, copied)

| Seat | Why |
|---|---|
| Critic: Provocateur (Debord) | required (adaptive) |
| Critic: Provocateur (Shklovsky) | required (adaptive) |
| Critic: Inclusion (Holmes) | required (adaptive) |
| Critic: Inclusion (Mace) | required (adaptive) |
| Critic: Evidence (Cairo) | rated 0.859 / 49 rounds |
| Critic: Usability (Krug) | rated 0.813 / 62 rounds |
| Critic: Craft (Bringhurst) | rated 0.727 / 33 rounds |
| Critic: Aestheticist (Gautier) | rotation seat |

Dotted pairs: Debord -.- Krug, Shklovsky -.- Krug. Content-owner witness: the shadw-gamesuite README and
GAME-SUITE.md (Annex V); every status claim is checked against them.

### Inventory (for the landing summary)

Pages: Home; Terrain (worlds); Forge (sandboxed tests); KeyForge (keys, G2); shadw.cloud (hosting, G3); Project file
and CLI; Games (Tidewatch, Shadow Duel, Brine & Brie: Shipwright); Shipwright (its own page); Roadmap (G0–G5).

### Landing concept

The hero is the product's own worked example drawn large: **the `shadw.game.json` file itself, as a wiring figure.**
Each section of the file is a row that names the product it calls, a glyph made from that product's real output
(the Tidewatch map Terrain generated; the hash chain of a real Forge run; key tiers; cloud cells), a status stamp
(built / planned, as text, not colour alone) and a link to that product's page. A games strip and a G0–G5 meter
close the figure, so the first screen names every page. Breaker: the real Terrain map bleeds out of the grid on the
right edge (Samara), the one image that breaks the Swiss grid every other element keeps.

### Frontier

| Candidate | Reached via | From anchor | Status |
|---|---|---|---|
| Wiring-figure hero from the real project file | seed | Gerstner | TAKEN (M1) |
| Map bleeds past the grid (BREAK) | Samara -.-> loosens -> Müller-Brockmann | Samara | TAKEN (M2) |
| Phone first-screen form (map becomes a row glyph) | First screen rule | MAYA | TAKEN (M3) |
| Product pages from one programme (same blocks per page) | programme method | Gerstner | TAKEN (M4) |
| Live Terrain map on the page (interactive) | Mau | Mau | DEFERRED (Terrain site already does it; link out) |

## 2. Decision Records

## Move M1: the project file as the hero  (KEEP-THE-RULE)
Depends on: none
Anchors: Stance An Incomplete Manifesto for Growth (Bruce Mau) | Rule Designing Programmes (Karl Gerstner) | Rule Grid Systems in Graphic Design (Josef Müller-Brockmann)
Intent: the first screen is the suite's one real artifact, `shadw.game.json`, with each section wired to the product that fills it, so the landing summarizes every page.
Formal argument: the suite's claim is "one file over four products"; showing the file with its wiring is the claim itself (Gerstner: the programme is the design). A strict column grid keeps six rows legible at both widths (Müller-Brockmann).
Alternatives rejected: (a) four product cards in a row: six cards is not a form, and it hides the file that ties them; (b) a big Terrain map alone: strong, but summarizes one product of four.
Consequence: copy must be short; each row carries one figure only.
Fence: n/a (no rule broken).
Frontier effect: opens M2 (break), M3 (phone form), M4 (page programme).
Mode field: Advanced pole: a config file as a hero (Gerstner). Acceptable pole: every row is a plain link with a text status (Krug).

## Move M2: the real map bleeds out of the grid  (BREAK)
Depends on: M1
Anchors: Breaker Making and Breaking the Grid (Timothy Samara) | Counterpoint Grid Systems in Graphic Design (Josef Müller-Brockmann) (dotted edge from Samara: loosens)
Intent: the Tidewatch map Terrain generated sits beside the file, larger than its column, and runs off the right edge of the page.
Formal argument: everything else keeps the grid, so the one element that breaks it is the world, which is what Terrain makes; the break says "this is generated, not laid out".
Alternatives rejected: (a) map inside a card: tame, reads as a thumbnail; (b) map as a full-bleed background: fights the text and fails contrast.
Consequence: horizontal overflow must be clipped at the page, never scroll; measured.
Fence: the grid exists so rows align and scan; the bleed is only on the right, outside the text columns.
Frontier effect: phone form (M3).
Mode field: Advanced pole: Samara's break. Acceptable pole: the map is captioned with its seed and content hash.

## Move M3: a phone first screen that fits
Depends on: M1, M2
Anchors: Welcome MAYA: Most Advanced Yet Acceptable (Raymond Loewy)
Intent: at 375 px the big map leaves the hero (it moves below) and becomes the `world` row's glyph; the figure stays complete above the fold.
Formal argument: the First screen rule asks the whole summary to be visible; the map's size is not the summary, the wiring is.
Alternatives rejected: (a) shrink the desktop layout: unreadable rows; (b) horizontal scroll of the figure: forbidden.
Consequence: two forms of one hero; both measured.
Fence: n/a. Frontier effect: none.
Mode field: Advanced: same figure. Acceptable: no sideways scroll.

## Move M4: one programme for every product page
Depends on: M1
Anchors: Rule Designing Programmes (Karl Gerstner)
Intent: each product page has the same blocks in the same order: what it does for a game, the section of the file it fills, a real output, status, and what is not built.
Formal argument: a programme lets a reader compare products; "what is not built" in the same slot on every page keeps the site honest.
Alternatives rejected: (a) free-form pages: drift; (b) one long products page: the owner's multi-page rule.
Consequence: pages are short. Frontier effect: none.
Mode field: Advanced: none needed. Acceptable: predictable pages (Krug).

## 3. Panel Reports

### Panel, WHOLE, round 1 (built site served locally; captures at 1280x800 and 375x812; link and box probes). Single-voice.

| Critic | Anchor used | Observed in the work | Verdict | Requested change |
|---|---|---|---|---|
| Critic: Evidence (Cairo) | First screen rule | Figure bottom at 807 px against an 800 px fold on desktop (fails by 7 px); 808 of 812 on phone; no sideways scroll (docW 1265 / 375); 18 internal links, 0 broken; one h1 per page | OBJECT | Bring the desktop figure above the fold |
| Critic: Provocateur (Debord) | MAYA | Headline "One file runs your game through four products" while two of the four rows say planned | OBJECT | Make the headline say what is true |
| Critic: Provocateur (Shklovsky) | Making and Breaking the Grid (Timothy Samara) | The map running off the right edge is the only thing that leaves the grid; it reads as made, not placed | PASS | — |
| Critic: Usability (Krug) | five-second test | Suite name, four products and three games readable on the first screen; on the phone the nav row is cut at "sha" with no cue that it scrolls | OBJECT | Show that the nav scrolls |
| Critic: Inclusion (Mace) | focus visibility | 3 px gold focus ring on every link; status is text plus a filled or empty square, not colour alone | PASS | — |
| Critic: Inclusion (Holmes) | mismatch | Mono labels at 11.2 px on the phone rows are the smallest text | PASS | (watch; logged) |
| Critic: Craft (Bringhurst) | measure and scale | Body lines under 70 characters; two type families only | PASS | — |
| Critic: Aestheticist (Gautier) | form for its own sake | The pixel map against the dark, quiet grid is the page's beauty | PASS | — |

Statements of meaning: a config file is the product, and the world it makes is the picture.
Andon pulled: no.

| Finding | Resolution |
|---|---|
| Cairo: desktop figure 7 px below the fold | ADAPT: hero padding 26 -> 18 px, h1 max 3.6 -> 3.2 rem; measured 785 of 800 |
| Debord: headline overclaims | ADAPT: "One file. Four products. Two already work." |
| Krug: phone nav has no scroll cue | ADAPT: fade mask on the nav's right edge at narrow widths |

### Panel, WHOLE, round 2 (same probes after the ADAPTs). Single-voice.

| Critic | Observed | Verdict |
|---|---|---|
| Critic: Evidence (Cairo) | desktop 785 of 800, phone 808 of 812, docW 1265 and 375, 0 broken links | PASS |
| Critic: Provocateur (Debord) | headline matches the stamps | PASS |
| Critic: Usability (Krug) | nav fades at the right edge on the phone | PASS |
| Others | no change in their regions | PASS |

Andon pulled: no.

## 4. Anchor Ledger

| Anchor | Role | Status | Evidence |
|---|---|---|---|
| An Incomplete Manifesto for Growth (Bruce Mau) | Stance | KEEP | survived Debord's overclaim objection once the headline changed |
| Grid Systems in Graphic Design (Josef Müller-Brockmann) | Rule | KEEP | six rows align at both widths; rows 46–47 px on the phone |
| Designing Programmes (Karl Gerstner) | Rule | KEEP | every product page has the same blocks, ending in "Not built yet" |
| Making and Breaking the Grid (Timothy Samara) | Breaker | KEEP | Shklovsky PASS; no sideways scroll measured |
| MAYA: Most Advanced Yet Acceptable (Raymond Loewy) | Welcome | KEEP | phone form of the hero complete above the fold |

## 5. Final-state figures (Step 2g)

| Figure on the site | Procedure | Value | State |
|---|---|---|---|
| Tidewatch 9,216 tiles, 1,309 blocking, 8 spawns, 24 structures | shadw-gamesuite README, check_scene.gd output | as printed | reproducible |
| contentHash 857fa8c9… | `world.lock.json` / SVG `desc` | 857fa8c9dba8… | reproducible |
| Forge run exec-42275c0f, 4,479 ms, summary 3,627 B, sha256 7d4b084c… | brine-shipwright `.shadw/runs/exec-42275c0f…/result.json` | as printed | reproducible |
| Chain prev hashes ed797a57ab5c, b1229f0e7c56 | same run's `events.ndjson` | as printed | reproducible |
| 25 / 25 checks; 186.8 s and 72.6 s | brine-shipwright `summary.json` | as printed | reproducible |
| Tidewatch 6 / 14 wins; Shadow Duel 12 / 8, 19.5 turns | shadw-gamesuite README table | as printed | reproducible (owner's repo) |
| 15,473 faces, 4 chunks | shadw-gamesuite README, check_voxels.gd | as printed | reproducible |

## 6. Stop test and close

- S1 met: open items below are DEFERRED with reasons. S2 met in round 2 (single-voice). S3 not met: the bound
  allows two rounds, and round 1 had ADAPTs. S4 not done: the map bleed was not pushed further, since a larger map
  narrows the file column and pushes the figure below the fold; logged. S5 met: the Samara -> Müller-Brockmann
  dotted edge was applied (the break is one element; everything else keeps the grid).
- **Run incomplete under the owner's round bound (S3, S4).** Resume point: an S4 push on the map (e.g. spawn
  markers drawn over it, or the map animating its seed), then a real multi-voice panel.

Double loop: the panel being single-voice is the weak link; one writer caught three defects, all measurable, but
could not disagree with itself on taste. Graph amendment: none. Carry-forward: Python's `http.server` lets the
browser cache CSS across navigations, so re-measure after reloading the stylesheet (the first re-measure read 807
from the stale file).

Compliance: tooling inventory done (§1); mode and bound stated; panel from pick_panel.py, single-voice not briefed
from seat files (skipped); seed with dotted counterpoint; run type Full; landing summarizes every page and is
measured complete at both sizes; BREAK move M2 taken; records before moves; Panel Reports per round; OBJECTs
resolved; figures re-measured; Anchor Ledger done; run **not** recorded in the dada ledger (import_log.py not run).
