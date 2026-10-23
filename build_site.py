#!/usr/bin/env python3
"""Build the ASI Law static site (GitHub Pages) from chapters/chNN.md.

Usage: python3 build_site.py [src_chapters_dir] [out_dir]
Each chapter file starts with '## Chapter N: Title'.
"""
import html, json, os, re, shutil, sys
from datetime import datetime, timezone
import markdown

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, 'chapters')
OUT = sys.argv[2] if len(sys.argv) > 2 else os.path.join(HERE, '_site')
SITE_URL = 'https://abdurrazzak5621.github.io/asilaw/'
TITLE = 'ASI Law: Sovereign of the Chaos Sea'
ALT = 'Global Awakening: Unique Class Calamity Necromancer, My Supreme Intelligence Law Comprehends the Heavens 10,000 Times Faster'
# (first chapter, book title) - add a row when a new book starts
BOOKS = [(1, 'The Grave Under the City'), (81, 'The Star Sea')]
STAR = "<svg aria-hidden='true' viewBox='0 0 24 24'><path d='M12 1.5C12.7 8 16 11.3 22.5 12C16 12.7 12.7 16 12 22.5C11.3 16 8 12.7 1.5 12C8 11.3 11.3 8 12 1.5Z' fill='currentColor'/></svg>"
esc = html.escape


def book_of(n):
    idx = 0
    for i, (start, _) in enumerate(BOOKS):
        if n >= start:
            idx = i
    return idx + 1, BOOKS[idx][1]


def load_chapters():
    chs = {}
    for f in os.listdir(SRC):
        m = re.fullmatch(r'ch(\d+)\.md', f)
        if not m:
            continue
        md = open(os.path.join(SRC, f), encoding='utf-8').read()
        h = re.match(r'\s*## Chapter (\d+): (.+)\n', md)
        n = int(h.group(1))
        assert n == int(m.group(1)), f
        body = md[h.end():].strip()
        html_body = markdown.markdown(body, extensions=['tables', 'sane_lists'])
        first = next((p for p in body.split('\n\n') if p.strip() and not p.startswith(('>', '#', '---', '*'))), '')
        snip = re.sub(r'[*_`>#]', '', first).strip()
        if len(snip) > 200:
            snip = snip[:200].rsplit(' ', 1)[0].rstrip('.,;:!?') + '…'
        words = len(re.findall(r'\S+', body))
        chs[n] = dict(n=n, name=h.group(2).strip(), html=html_body, snip=snip, words=words)
    nums = sorted(chs)
    assert nums == list(range(1, len(nums) + 1)), 'chapter numbers have gaps'
    return [chs[n] for n in nums]


def page(title, desc, body, root, path, extra_head='', progress=False):
    canon = SITE_URL + path
    return f"""<!doctype html>
<html lang="en" data-theme="night">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{canon}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:type" content="book">
<meta property="og:url" content="{canon}">
<meta name="theme-color" content="#141726">
<link rel="icon" href="{root}assets/star.svg" type="image/svg+xml">
<link rel="alternate" type="application/rss+xml" title="{esc(TITLE)}" href="{root}feed.xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Literata:ital,opsz,wght@0,7..72,400;0,7..72,600;1,7..72,400&family=Manrope:wght@500;600;700;800&display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Noto+Serif+SC:wght@600&text=%E5%A4%A9%E7%81%BE%E6%AD%BB%E7%81%B5%E8%87%B3%E9%AB%98%E6%99%BA%E8%83%BD%E6%B3%95%E5%88%99&display=swap" rel="stylesheet">
<script>(function(){{var S={{}};try{{S=JSON.parse(localStorage.getItem('cz-read'))||{{}};}}catch(e){{}}var r=document.documentElement;r.setAttribute('data-theme',S.theme||'night');r.setAttribute('data-font',S.font||'serif');r.setAttribute('data-width',S.width||'normal');r.style.setProperty('--fs',(S.fs||19)+'px');}})();</script>
<link rel="stylesheet" href="{root}assets/style.css">
{extra_head}</head>
<body>
<a class="skip" href="#main-content">Skip to content</a>
<header class="site-head">
  <div class="wrap">
    <div class="head-row">
      <a aria-label="czverse home" class="brand" href="{root or './'}">{STAR}czverse</a>
      <nav aria-label="Main" class="nav">
        <a href="{root}chapters.html">Chapters</a>
        <a href="{root}bible.html"><span class="hide-sm">Story&#160;</span>Bible</a>
        <a aria-label="czverse on X" class="hide-sm" href="https://x.com/czverse" rel="noopener" target="_blank">@czverse</a>
        <button aria-controls="cz-panel" aria-expanded="false" aria-label="Reading settings" class="aa" id="cz-aa" type="button">Aa</button>
      </nav>
    </div>
    <div aria-label="Reading settings" class="panel" hidden id="cz-panel" role="dialog">
      <p class="panel-title">Reading settings</p>
      <div class="opt"><span class="opt-label">Theme</span>
        <div class="seg">
          <button data-set="theme" data-val="night" type="button"><span class="dot" style="background:#141726"></span>Night</button>
          <button data-set="theme" data-val="paper" type="button"><span class="dot" style="background:#eee6d3"></span>Paper</button>
          <button data-set="theme" data-val="day" type="button"><span class="dot" style="background:#f6f5f1"></span>Day</button>
        </div></div>
      <div class="opt"><span class="opt-label">Text size</span>
        <div class="sz"><button aria-label="Smaller text" data-fs="-1" type="button">A&#8722;</button><output id="cz-fs">19px</output><button aria-label="Larger text" data-fs="1" type="button">A+</button></div></div>
      <div class="opt"><span class="opt-label">Typeface</span>
        <div class="seg"><button data-set="font" data-val="serif" type="button">Serif</button><button data-set="font" data-val="sans" type="button">Sans</button></div></div>
      <div class="opt"><span class="opt-label">Line width</span>
        <div class="seg"><button data-set="width" data-val="normal" type="button">Comfortable</button><button data-set="width" data-val="wide" type="button">Wide</button></div></div>
    </div>
    {'<span class="progress" id="cz-progress"></span>' if progress else ''}
  </div>
</header>
<main class="wrap" id="main-content">
{body}
</main>
<footer class="site-foot">
  <div class="wrap">
    <div class="foot-row">
      <span class="foot-brand">{STAR}czverse</span>
      <nav aria-label="Footer" class="foot-links">
        <a href="{root}chapters.html">Chapter list</a>
        <a href="{root}bible.html">Story Bible</a>
        <a href="{root}feed.xml">RSS</a>
        <a href="https://x.com/czverse" rel="noopener" target="_blank">Follow @czverse on X</a>
      </nav>
    </div>
    <p class="foot-note">{esc(TITLE)}, an original web novel by czverse. Copyright 2026. All rights reserved.</p>
  </div>
</footer>
<script src="{root}assets/app.js"></script>
</body>
</html>
"""


def row(c, root, snip=True):
    s = f'<span class="ch-snip">{esc(c["snip"])}</span>' if snip else ''
    return (f'<li class="ch-row"><a href="{root}chapter/{c["n"]}.html">'
            f'<span class="ch-num">{c["n"]}</span><span class="ch-title">{esc(c["name"])}</span>{s}</a></li>')


def build():
    chs = load_chapters()
    last = chs[-1]
    total = len(chs)
    if os.path.isdir(OUT):
        shutil.rmtree(OUT)
    os.makedirs(os.path.join(OUT, 'chapter'))
    os.makedirs(os.path.join(OUT, 'assets'))
    for f in ('style.css', 'app.js', 'star.svg'):
        shutil.copy(os.path.join(HERE, 'assets', f), os.path.join(OUT, 'assets', f))
    open(os.path.join(OUT, '.nojekyll'), 'w').close()
    meta = f'<meta name="cz-latest" content="{last["n"]}">\n'

    # chapters
    for i, c in enumerate(chs):
        bk, bt = book_of(c['n'])
        prev = chs[i - 1] if i > 0 else None
        nxt = chs[i + 1] if i + 1 < total else None
        pv = (f'<a class="cn-prev" href="{prev["n"]}.html" rel="prev"><small>Previous: Chapter {prev["n"]}</small><b>{esc(prev["name"])}</b></a>'
              if prev else '<a class="cn-prev" hidden></a>')
        nx = (f'<a class="cn-next" href="{nxt["n"]}.html" rel="next"><small>Next: Chapter {nxt["n"]}</small><b>{esc(nxt["name"])}</b></a>'
              if nxt else f'<a class="cn-next is-end"><small>Next: Chapter {c["n"] + 1}</small><b>Being written now</b></a>')
        mins = max(1, round(c['words'] / 230))
        body = f"""<article class="reader" data-ch="{c['n']}" data-name="{esc(c['name'])}">
  <header class="reader-head">
    <p class="kicker">Book {bk}: {esc(bt)}</p>
    <h1 class="reader-title"><span class="ch-label">Chapter {c['n']}</span><span class="ch-name">{esc(c['name'])}</span></h1>
    <p class="reader-meta"><span class="by">czverse</span><span>{mins} min read</span></p>
  </header>
  <div class="post-body" id="post-body">
{c['html']}
  </div>
  <nav aria-label="Chapter navigation" class="chapter-nav">{pv}<a class="cn-all" href="../chapters.html">All chapters</a>{nx}</nav>
  <p class="keys">Use the &#8592; and &#8594; keys to move between chapters</p>
</article>"""
        title = f'Chapter {c["n"]}: {c["name"]} | ASI Law'
        with open(os.path.join(OUT, 'chapter', f'{c["n"]}.html'), 'w', encoding='utf-8') as fh:
            fh.write(page(title, c['snip'], body, '../', f'chapter/{c["n"]}.html', meta, progress=True))

    # home
    latest = ''.join(row(c, '') for c in reversed(chs[-10:]))
    bk, bt = book_of(last['n'])
    home = f"""<section aria-labelledby="cz-title" class="hero">
  <div aria-hidden="true" class="stele-wrap">
    <div class="stele">
      <p class="stele-col main">天灾死灵</p>
      <p class="stele-col sub">至高智能法则</p>
      <span class="stele-mark">{STAR}</span>
    </div>
  </div>
  <div class="hero-text">
    <h1 class="hero-title" id="cz-title">{esc(TITLE)}</h1>
    <p class="hero-alt">{esc(ALT)}</p>
    <div class="hero-lede">
      <p>Forty years after the Rift Catastrophe tore open the sky over Blue Star, every eighteen-year-old touches the Awakening Stele. When Zhou Yuanshu lays his hand on it, all eleven Steles on the planet go black at once.</p>
      <p>His class has never existed: Calamity Necromancer. His talent is a law the Chaos Lords erased a hundred billion years ago. Everyone else spends a lifetime grasping one percent of a law. He needs one look.</p>
    </div>
    <div class="actions">
      <a class="btn btn-primary" href="chapter/1.html">Start reading Chapter 1</a>
      <a class="btn btn-quiet" href="chapter/{last['n']}.html" id="cz-latest">Read the latest: Chapter {last['n']}</a>
    </div>
    <dl class="facts">
      <div><dt>Status</dt><dd>Ongoing</dd></div>
      <div><dt>Now publishing</dt><dd>Book {bk}: {esc(bt)}</dd></div>
      <div><dt>Chapters</dt><dd>{total}</dd></div>
      <div><dt>Written by</dt><dd>czverse</dd></div>
    </dl>
  </div>
</section>
<div class="list-head"><h2>Latest chapters</h2><a href="chapters.html">Full chapter list</a></div>
<ul class="ch-rows">{latest}</ul>
<div class="book">
  <p>Book {bk}: {esc(bt)} &middot; {total} chapters published</p>
  <div class="book-bar"><span style="width:{max(1.5, min(100, total / 40)):.2f}%"></span></div>
</div>"""
    with open(os.path.join(OUT, 'index.html'), 'w', encoding='utf-8') as fh:
        fh.write(page(TITLE, 'Read ' + TITLE + ', an original web novel by czverse. Free, ongoing, ' + str(total) + ' chapters.', home, '', '', meta))

    # full list, grouped by book
    parts = ['<div class="list-head list-top"><h1>All chapters</h1><a href="chapter/%d.html">Latest: Chapter %d</a></div>' % (last['n'], last['n'])]
    jump = []
    for i, (start, bt) in enumerate(BOOKS):
        end = BOOKS[i + 1][0] - 1 if i + 1 < len(BOOKS) else last['n']
        group = [c for c in chs if start <= c['n'] <= end]
        if not group:
            continue
        jump.append(f'<a href="#book-{i + 1}">Book {i + 1}</a>')
        parts.append(f'<h2 class="book-head" id="book-{i + 1}">Book {i + 1}: {esc(bt)} <span>Chapters {start}&#8211;{end}</span></h2>')
        parts.append('<ul class="ch-rows compact">' + ''.join(row(c, '', snip=False) for c in group) + '</ul>')
    parts.insert(1, '<p class="book-jump">' + ' '.join(jump) + '</p>')
    with open(os.path.join(OUT, 'chapters.html'), 'w', encoding='utf-8') as fh:
        fh.write(page('All chapters | ASI Law', 'Full chapter list for ' + TITLE + '.', '\n'.join(parts), '', 'chapters.html', meta))

    # bible
    bmd = open(os.path.join(HERE, 'bible.md'), encoding='utf-8').read()
    bible = '<article class="reader"><header class="reader-head"><p class="kicker">Story Bible</p><h1 class="reader-title">' + esc(TITLE) + '</h1></header><div class="post-body">' + markdown.markdown(bmd, extensions=['tables', 'sane_lists']) + '</div><nav class="chapter-nav"><a class="cn-prev" hidden></a><a class="cn-all" href="chapters.html">All chapters</a><a class="cn-next" href="chapter/1.html"><small>Start reading</small><b>Chapter 1</b></a></nav></article>'
    with open(os.path.join(OUT, 'bible.html'), 'w', encoding='utf-8') as fh:
        fh.write(page('Story Bible | ASI Law', 'The world, power system and cast of ' + TITLE + '.', bible, '', 'bible.html'))

    # 404
    nf = '<div class="empty"><h1>Page not found</h1><p>That page does not exist. <a href="/asilaw/chapters.html">Go to the chapter list</a>.</p></div>'
    with open(os.path.join(OUT, '404.html'), 'w', encoding='utf-8') as fh:
        fh.write(page('Not found | ASI Law', 'Page not found.', nf, '/asilaw/', '404.html'))

    # feed, sitemap, robots, json
    now = datetime.now(timezone.utc).strftime('%a, %d %b %Y %H:%M:%S +0000')
    items = ''.join(
        f'<item><title>{esc("Chapter %d: %s" % (c["n"], c["name"]))}</title><link>{SITE_URL}chapter/{c["n"]}.html</link>'
        f'<guid>{SITE_URL}chapter/{c["n"]}.html</guid><description>{esc(c["snip"])}</description></item>'
        for c in reversed(chs[-20:]))
    with open(os.path.join(OUT, 'feed.xml'), 'w', encoding='utf-8') as fh:
        fh.write(f'<?xml version="1.0" encoding="UTF-8"?><rss version="2.0"><channel><title>{esc(TITLE)}</title><link>{SITE_URL}</link>'
                 f'<description>An original web novel by czverse.</description><lastBuildDate>{now}</lastBuildDate>{items}</channel></rss>')
    urls = [SITE_URL, SITE_URL + 'chapters.html', SITE_URL + 'bible.html'] + [f'{SITE_URL}chapter/{c["n"]}.html' for c in chs]
    with open(os.path.join(OUT, 'sitemap.xml'), 'w', encoding='utf-8') as fh:
        fh.write('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' + ''.join(f'<url><loc>{u}</loc></url>' for u in urls) + '</urlset>')
    with open(os.path.join(OUT, 'robots.txt'), 'w') as fh:
        fh.write(f'User-agent: *\nAllow: /\nSitemap: {SITE_URL}sitemap.xml\n')
    with open(os.path.join(OUT, 'chapters.json'), 'w', encoding='utf-8') as fh:
        json.dump([{'n': c['n'], 'name': c['name']} for c in chs], fh, ensure_ascii=False)
    print(f'built {total} chapters into {OUT}')


if __name__ == '__main__':
    build()
