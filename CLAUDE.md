# ASI Law: Sovereign of the Chaos Sea — project instructions

Web novel by czverse, co-written with Claude. Site: https://czverse.github.io/asilaw/ (GitHub Pages from `docs/`).

## Files

- `chapters/chNN.md` (ch01 … ch120): one chapter per file, first line `## Chapter N: Title`. **The manuscript is canon.**
- `CANON/`: the verified ledger of what ch1–120 establish. Read the relevant files before writing; update them after.
- `EDITORIAL/continuity-issues.md`: known contradictions. `EDITORIAL/apply_continuity_patch.py`: the continuity fixes applied on 2026-10-23 (kept for the record).
- `EDITORIAL/style-guide.md`: tic budgets, voices, ASI and combat scene rules.
- `bible.md`: the original pitch Bible (older than CANON; CANON wins where they differ).
- `build_site.py`, `assets/`: site generator. `docs/` is generated output; never edit it by hand.

## Publishing a chapter

1. Add `chapters/chNN.md` (for example `ch121.md`).
2. Run `python3 build_site.py chapters docs`.
3. Commit as `czverse <abdulrazzakmirg@gmail.com>` and push to `main`.
4. Check the live chapter page.

## Writing a chapter (every time)

1. **Read first:** the previous three chapters in full, `CANON/cultivation-ledger.md`, `CANON/undead-army.md`, and any chapter that set up what this one pays off. Never write from memory of a chapter you have not reread.
2. **Plan:** what follows from the last scene, what Yuanshu wants, what opposes him, what changes. One central development per chapter, ideally two areas advanced.
3. **Write:** 2,000–3,000 words, third-person limited, in the established voice. Follow `EDITORIAL/style-guide.md`.
4. **Edit:** continuity, power-system accuracy, the tic budget, and repetition of images and resolutions.
5. **Record:** after the chapter, a short editorial note (kept out of the chapter file): word count, canon changes, ability or resource changes, mysteries advanced, new obligations. Update `CANON/` in the same commit.

## Non-negotiables

- Single heroine (Shen Lingyue), no harem.
- Every raise asks first (Rule One). Article Seven: the dead may defend, never conquer.
- No new power without a cause in canon. Seed is never omniscient: limits are listed in `CANON/cultivation-ledger.md`.
- Do not rush realms: Lord no earlier than about ch160, King no earlier than about ch400.
- Never reverse a sacrifice or silently change a character's history, ability or location.
- Do not change published chapter text without the author's explicit OK.
