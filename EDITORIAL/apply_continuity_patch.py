#!/usr/bin/env python3
"""Proposed word-level continuity fixes for chapters 1-120 (see continuity-issues.md).

NOT APPLIED. Run only after the author approves:
    python3 EDITORIAL/apply_continuity_patch.py            # dry run: shows what would change
    python3 EDITORIAL/apply_continuity_patch.py --apply    # writes the files
    python3 EDITORIAL/apply_continuity_patch.py --apply --multiplier   # also 1000x -> 10,000x
Each fix must match exactly once, or the script stops without writing anything.
"""
import os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

FIXES = [
    # (issue #, file, old, new)
    (3, "chapters/ch120.md", "for the first time in thirty-one years, the faceless one moved.",
        "for the first time since it turned toward you, the faceless one moved. Not three degrees."),
    (4, "chapters/ch116.md", "Deepwater Recovery. Eleven months ago. To dredge",
        "Deepwater Recovery. Eight months ago. To dredge"),
    (4, "chapters/ch120.md", "\"The sixth was delivered,\" he said. \"Eleven months ago.",
        "\"The sixth was delivered,\" he said. \"Eight months ago."),
    (4, "chapters/ch120.md", "It has been quiet for eleven months.", "It has been quiet for eight months."),
    (2, "chapters/ch89.md", "\"There are five Kings on Blue Star,\" said Su Mingli. \"That thing counted us. *Significant. Finite.*\"",
        "\"There are five of us that thing counted,\" said Su Mingli. \"*Significant. Finite.*\""),
    (5, "chapters/ch61.md", "There were fourteen of them. Eleven living, three dead.",
        "There were twelve of them. Nine living, three dead."),
    (5, "chapters/ch64.md", "All fourteen of them, and the eighty-eight", "All twelve of them, and the eighty-eight"),
    (5, "chapters/ch72.md", "around the eleven living, a hundred meters", "around the nine living, a hundred meters"),
    (5, "chapters/ch73.md", "on the ice, eleven living people lay", "on the ice, nine living people lay"),
    (5, "chapters/ch73.md", "across the eleven living in their tight circle", "across the nine living in their tight circle"),
    (5, "chapters/ch73.md", "Eleven living people could not stay silent", "Nine living people could not stay silent"),
    (5, "chapters/ch73.md", "Behind him, the eleven living lay", "Behind him, the nine living lay"),
    (6, "chapters/ch100.md", "eleven soldiers kneeling, quiet, facing inward", "ten soldiers kneeling, quiet, facing inward"),
    (7, "chapters/ch16.md", "a young man with tired eyes and a black staff", "a tired man with a white staff"),
    (9, "chapters/ch11.md", "fishing village on the Southern Coalition coast", "fishing village on the Southern Compact coast"),
    (9, "chapters/ch11.md", "The Southern Coalition's vote", "The Southern Compact's vote"),
    (10, "chapters/ch114.md", "At the four columns. YES.", "At the first four columns. YES."),
    (11, "chapters/ch43.md", "\"A thousand gates,\" said Shirasagi Ren.", "\"Twelve hundred gates,\" said Shirasagi Ren."),
    (12, "chapters/ch116.md", "In the rain. For four months.", "In the rain. For ten weeks."),
]
MULTIPLIER = [
    (13, "bible.md", "Comprehends the Heavens 1000x Faster", "Comprehends the Heavens 10,000 Times Faster"),
    (13, "build_site.py", "Comprehends the Heavens 1000x Faster", "Comprehends the Heavens 10,000 Times Faster"),
]

def main():
    apply = "--apply" in sys.argv
    fixes = FIXES + (MULTIPLIER if "--multiplier" in sys.argv else [])
    texts = {}
    for n, f, old, new in fixes:
        p = os.path.join(ROOT, f)
        texts.setdefault(p, open(p, encoding="utf-8").read())
        c = texts[p].count(old)
        if c != 1:
            sys.exit(f"STOP: issue {n}: expected 1 match in {f}, found {c}: {old[:60]!r}")
        texts[p] = texts[p].replace(old, new)
        print(f"#{n:<3} {f}: {old[:50]!r} -> {new[:50]!r}")
    if apply:
        for p, t in texts.items():
            open(p, "w", encoding="utf-8").write(t)
        print(f"Applied {len(fixes)} fixes to {len(texts)} files. Rebuild: python3 build_site.py chapters docs")
    else:
        print(f"Dry run: {len(fixes)} fixes OK. Nothing written.")

if __name__ == "__main__":
    main()
