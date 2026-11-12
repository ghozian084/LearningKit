# Mr. Ghozi Learning Kit — notes for Claude

## Publishing
- When a task is finished and all checks pass, **push directly to `main`** (`git push origin HEAD:main`).
  The teacher does not want to merge pull requests by hand. Do not open a pull request unless asked.
- Only fast-forward `main`: fetch first, base the work on the latest `origin/main`, and never force-push `main`.

## Kit conventions
- Content lives in `dm/g{grade}/t{nn}-{slug}/`; every new file must be registered in `data.js`.
- Files per topic: `lp.html` (lesson plan), `bd-01.html` (board), `im-0n.html` (interactive media),
  `ws-0n.html` (worksheets, one per meeting), `ha-0n.html` (hands-on, one per meeting).
- Worksheets and hands-on files are fixed full A4 pages (`.page` = one sheet; no half-empty pages, nothing split).
- Every hands-on activity needs an interactive-media twin, so the teacher can skip printing.
- Students in Grade 9 work individually (no fixed groups).
- Chapter tests (with answer keys) are encrypted with the teacher password before their first commit;
  never commit an unlocked test.
- Verify every numerical answer by computation before publishing.
- Direct Teaching boards: use the `/directteach` skill (`.claude/skills/directteach/`) — same engine, slide order
  (Lecture → I Do → We Do → You Do) and fit check for every topic; keep existing boards and add the next `bd-0N`.
