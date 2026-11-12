---
name: directteach
description: Build a Direct Teaching board (Lecture → I Do → We Do → You Do slides with step-by-step reveals, hidden We-Do answers and You-Do countdown timers) for a topic in the learning kit. Use when the teacher types /directteach or asks for a "direct teaching" / "direct instruction" board for a topic.
---

# /directteach — Direct Teaching board for a topic

Usage: `/directteach <grade> <topic>` (e.g. `/directteach 9 perimeter area volume`, `/directteach 12 differentiation`).
If the topic is unclear, list the topics in `data.js` and pick the one the teacher named.

The board format is the one the teacher approved for G12 Differentiation (`dm/g12/t05-differentiation/bd-01.html`)
and G9 Perimeter, Area & Volume (`dm/g09/t07-perimeter-area-and-volume/bd-02.html`). Keep it identical.

## What the board must contain
- Title slide (Lecture → I Do → We Do → You Do chips) and a roadmap slide (table of meetings + key formulas + WILT).
- For **every meeting in the lesson plan**, in this order:
  1. **📢 Lecture** — hook (meaningful/local context from the LP), then the rule(s) in `.rule` boxes, each revealed as a step;
     a `.warn` box for the classic mistake. Split a crowded lecture into two slides rather than shrinking text.
  2. **👩‍🏫 I Do** — 1–2 worked-example slides: `.question` first, then one `S('label', ...)` step per line of working,
     ending in `<span class="final">answer</span>`. Use the LP's own examples when it gives them.
  3. **🤝 We Do** — mini-whiteboard questions ("Boards up on 3 – 2 – 1"), each answer hidden as a step.
     Use new numbers: never copy worksheet or chapter-test questions.
  4. **✍️ You Do** — `Board.youdo('Worksheet N', minutes, [checklist...])` with `timer=minutes` (minutes from the LP).
- The final meeting: review slides (summary chart / "which rule?" cold call with hidden answers) and the test slide
  with its timer (e.g. 45 or 55 min) — never put test questions on the board.
- Students work individually; every numerical answer is verified by computation (sympy / Python) before publishing.

## How to build it
1. Read the topic's `lp.html` (meetings, timings, examples, exit tickets) and the worksheet titles in `data.js`.
2. Copy `examples/g09_t07_perimeter_area_volume.py` to a new file in `examples/` named after the topic and replace the content.
   The engine is `engine/directteach.py` (`Board`, `S`); its docstring lists the CSS blocks you can use.
   **Write all HTML/TeX in raw triple-double-quoted strings `r"""..."""`** — primes (`u'`) and backslashes (`\frac`) break
   ordinary strings; `build()` refuses output containing control characters.
3. Compute and check every answer first (keep the numbers in a quick Python/sympy check).
4. Build: `python3 .claude/skills/directteach/examples/<file>.py .` → writes `dm/g{grade}/{topic}/bd-0N.html`.
   Use the next free board number; keep any existing (e.g. Discovery/PBL) boards.
5. Check: `NODE_PATH=$(npm root -g) node .claude/skills/directteach/engine/check_board.js <board> [mathjax-es5-dir]`
   (MathJax can be installed locally with `npm i mathjax@3` in the scratchpad and the `es5` dir passed in).
   It must print "all slides fit" at 1280×720, 1366×768 and 1920×1080, no JS/MathJax errors, and 0 steps left hidden.
   Then screenshot the slides with diagrams and look at them.
6. Register the board in `data.js` (`bd` section, title `"Board N (Direct Teaching)"`) and add one line to the topic's LP
   materials box saying the direct-teaching board exists.
7. Commit and push straight to `main` as `CLAUDE.md` says.

## Teacher controls (already in the engine)
Space / → / PageDown / clicker: reveal next step, then next slide · ← previous slide · ↑ hide last step ·
toolbar: pen, eraser, colour, meeting jump menu, countdown timer (▶ ⏸ ↺, preset by You-Do slides), clear slide.
