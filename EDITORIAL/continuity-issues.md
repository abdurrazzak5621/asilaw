# Canon and continuity issues, ch1–120 (verified October 2026)

**I found 22 verified issues: 4 that affect the plot or cosmology, 9 number or name slips, and 9 minor ones.** Every item below was checked against the chapter text. Fixes are proposals; none has been applied. Word-level fixes are scripted in `apply_continuity_patch.py` (not applied; needs the author's OK).

### Must fix (plot or cosmology)

| # | Issue | Evidence | Proposed fix |
| --- | --- | --- | --- |
| 1 | **The Chaos Sea arrives too early and is defined as ordinary space** | ch80 title; ch82 "I do not know how to measure the Chaos Sea"; ch83 the Elder: "What you would call space. The dark between the fields"; ch90 the party enters. Bible: tier 6, "Billions of Domains drifting in chaos, walked by Chaos Lords" | No chapter edits (see the special section below). Make "Chaos Sea" the makers' word, which the story later shows to be a mistranslation, and separate visiting, surviving, understanding and ruling. |
| 2 | **"Five Kings on Blue Star" contradicts "nine Kings" in Huaxia alone** | ch1 "One of nine Kings in the entire nation"; Bible says the same; ch89 "There are five Kings on Blue Star"; ch11, 53, 56, 112 "the five Kings" | Make canon that the Five are the peak King of each nation, the one who stands behind a Concordia chair. Edit one sentence in ch89: "There are five of us that thing counted." The other uses already read correctly. |
| 3 | **The faceless one "moved for the first time in thirty-one years"** | ch120. But ch17 log 2,190: "It turned its head today"; ch18: its head turned 3° toward Wanqing's lab seven years ago, then 3° toward Yuanshu | ch120: "…for the first time, it moved on its own. Not three degrees. It turned its head all the way up." |
| 4 | **Dredging "eleven months ago" happens before the spire sank** | ch116 and ch120 (dredge, sale, delivery; "quiet for eleven months"). The spire sank in ch87. The party was away 115 days (ch108), and ch113 is day 139 after the Mouth left, so ch116 is about 9 months after ch87 | Change "eleven months" to "eight months" in ch116 and ch120 (three places). |

### Number and name slips

| # | Issue | Evidence | Proposed fix |
| --- | --- | --- | --- |
| 5 | Party size | ch61 "fourteen of them. Eleven living, three dead"; ch64 "All fourteen"; ch72–73 "eleven living". Only nine living are named: Su Mingli, Yuanshu, Lingyue, Qin Hao, Mo Xing, Mo Shi, Bai Lu, Yan Shuang, Sokolova | "Twelve of them. Nine living, three dead" (ch61); "All twelve" (ch64); "nine living" (ch72, 73) |
| 6 | Kneeling soldiers | ch97 says ten are lost; ch100 "eleven soldiers kneeling"; ch101, 110 and 111 say ten | ch100: "ten soldiers" |
| 7 | Lu Xuanming's appearance in Qi's memory | ch16 "a young man with tired eyes and a black staff". The staff is white bone (ch67), and he was about 52 at the Black Tide (15 at his first raise 68 years ago) | ch16: "a tired man with a white staff" |
| 8 | Old Seven's "sixty years" | ch46, 62, 68, 85, 87 (salute, spear, arm break). He died 31 years ago | Your choice: either "thirty-one years" in ch62, 85 and 87, or one line establishing that Qi held a spear for about 30 years before he died, so "sixty" counts from enlistment |
| 9 | Southern Coalition vs Southern Compact | ch11 (twice) vs ch51 onward | ch11 → "Southern Compact" |
| 10 | Board columns | ch114 Lu reads "the four columns. YES. ASK MY FAMILY. ONLY TO SPEAK. QUIET." when the board has seven (ch108, 113) | "the first four columns" |
| 11 | Gates vs years | ch43 has 1,000 gates, "one for every year", against 1,200 years of watch | "Twelve hundred gates" |
| 12 | Hale's hollow time | ch116 says "hollow… for four months". He was taken at Concordia (ch59) and woke in ch79, about 70 days later (ch75) | "for ten weeks" |
| 13 | Title multiplier | The English subtitle, bible.md and build_site.py say 1000x; the Chinese title says 万倍 (10,000×); the Bible says "ten thousand simulations" | Standardize on 10,000× (title, Bible, site subtitle) |

### Minor (ledger notes, optional text fixes)

| # | Issue | Evidence | Note |
| --- | --- | --- | --- |
| 14 | Death Law gap | ch3 ends at 17.0%; ch9 opens at 18.6% | Ledger: +1.6% from canyon fighting (ch8) |
| 15 | Hunger calls the Kings "SOVEREIGNS" | ch87; Sovereign is realm 7 and the title word | Keep. Later, Seed notes the word is a rough translation ("those who rule") |
| 16 | Jiang Lan "walked beside him forty years" | ch67; from age 15 to death at about 52 is 37 years | Optional: "nearly forty" |
| 17 | Bandaged burn | ch16, left hand; the cause is never shown | Optional one line, or leave |
| 18 | Yamato abstention line | ch39 recalls "Yamato abstains. We have a question first" at Concordia (ch11), where it is not shown | Acceptable as offscreen; recorded |
| 19 | "Three months after the bite" | ch112; by the dates it is about four | Optional: "four months" |
| 20 | Qin Hao's colonel's star | ch106 "with a colonel's star over his heart" is his father's insignia (ch89), not his rank | Ledger note only |
| 21 | Seed's 4,113 | Eleven were released (ch77), but ch114–115 still say "four thousand one hundred and thirteen" | Fine as the group's name; the ledger records 4,102 remaining |
| 22 | The Twins' arrival | 68 days (ch105, 107), but they arrive in about 37 | Already explained in ch107 ("saving everything to fall"); no fix |

**Checked and consistent:** the Third Battalion (141 = 88 yes + 53 quiet, ch63; 88 = 4 sled + 12 escort + 10 quiet + 62 into the Mouth, ch111); the Low Fire (281 million + 19 million = "a few hundred million", ch109); the seven seeds (1 Hearth, 1 Northern Union, 1 Yamato, 3 offshore, 1 Lingzhou, ch116 and 120); Gu's age (9 when harvested, 51 years ago, ch69); and Ama is 16 (ch72, 89).

### Story Bible vs manuscript

The manuscript outranks the Bible, so these are Bible updates.

- **Missing from the Bible:** the Ledger and Charter (Articles Three, Seven, Nine), the keeper and fields, Hungers, the staff and its two doors, the Third Battalion and the 19,402, Hush, the Architects, the Sixth, and the Hunger seeds.
- **Out of date:** Yuanshu is 19 (ch87), not 18. Hu Dabao does not "never leave"; he has been absent since ch39. Qin Hao is a friend, not "a proud rival". Wanqing has returned (ch80).
- **The Bible tier list vs the Chaos Sea:** see below.

### Special section: the early Chaos Sea

**Proposal: keep all published text and make the name a mistranslation the story corrects later.** That turns an early mistake into foreshadowing.

- **What is canon now:** the keeper, the Elder and the narration call the dark between nearby worlds "the Chaos Sea" (ch80–110). Distances are crossed in days to weeks on currents (ch91, 107). Husk worlds, the Lantern world and four Hungers lie within that range.
- **Proposed canon (new material, needs your approval):**
    1. "Chaos Sea" is the makers' word. Their empire knew only one dark, so every dark was "the sea". The Hungers and keepers are wreckage that drifted down out of the true Chaos Sea long ago. That is why the region holds Chaos-Sea-made things without being the Chaos Sea.
    2. Seed's failure to measure it (ch82) becomes the clue. When Seed finally maps it (proposed for ch201–220), the "sea" fits inside one arm of one galaxy: the shallows of the Star Sea.
    3. Rename going forward: "the Shallows" in narration, "the Sea" in characters' speech, and "the true Chaos Sea" for tier 6.
- **The four achievements, kept separate:**

| Achievement | Meaning | Yuanshu at ch120 | Earliest proposed |
| --- | --- | --- | --- |
| Visit | Be carried through by a stronger power | Done (keeper's raft, ch90–110), in the Shallows only | Done |
| Survive | Stay alive there on his own power | No | King realm (ch400 or later) |
| Understand | Model its laws with the ASI Law | No; Seed cannot measure even the Shallows (ch82) | Universe Venerable onward |
| Rule | Command it as a Chaos Lord, the title's promise | No | Final books |

- **Alternative:** edit ch80, 82, 83 and 90 to say "the Star Sea", and retitle Book 2. That is cleaner but costs a book title and four published chapters.
