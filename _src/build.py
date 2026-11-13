"""Build the SHADW Game Suite site: _src/pages/*.html + the layout below -> site/*.html.

    python -I _src/build.py

Each page file starts with three lines: title, description, nav key. The rest is the page's <main> content.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = ROOT / "site"
DOMAIN = "https://shadw-gamesuite-site.shadw.app/"

NAV = [
    ("index", "Overview"),
    ("terrain", "Terrain"),
    ("forge", "Forge"),
    ("keyforge", "KeyForge"),
    ("cloud", "shadw.cloud"),
    ("project-file", "Project file"),
    ("games", "Games"),
    ("roadmap", "Roadmap"),
]

MARK = """<svg viewBox="0 0 32 32" aria-hidden="true"><rect x="2" y="2" width="28" height="28" rx="6" fill="#161e22" stroke="#f3c76b" stroke-width="2"/><path d="M8 10h7v4H8zM17 10h7v4h-7zM8 18h7v4H8z" fill="#4f86a6"/><path d="M17 18h7v4h-7z" fill="#f3c76b"/></svg>"""

LAYOUT = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="{canonical}">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:url" content="{canonical}">
<meta property="og:type" content="website">
<meta property="og:image" content="{domain}img/shipwright-brig.png">
<meta name="theme-color" content="#0f1417">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500&family=Space+Grotesk:wght@400;500;600;700&display=swap">
<link rel="stylesheet" href="css/style.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="top"><div class="wrap">
<a class="brand" href="index.html">{mark}<span>SHADW Game Suite</span></a>
<nav class="main" aria-label="Main">{nav}</nav>
</div></header>
<main id="main">
{body}
</main>
<footer><div class="wrap">
<div><p><strong>SHADW Game Suite</strong><br>One project file and one CLI over SHADW Terrain, Forge, KeyForge, the Game Store and shadw.cloud.</p>
<p>Status on 13 November 2026: G0 built, G1 built except <code>build</code>, G2 started (KeyForge, Game Store v0.1), G3 to G5 planned. Four games pass their tests under Forge. Nothing on this site is a hosted service you can sign up for yet.</p></div>
<div><ul><li><a href="terrain.html">Terrain: make worlds</a></li><li><a href="forge.html">Forge: test in a sandbox</a></li><li><a href="keyforge.html">KeyForge: keys and licences</a></li><li><a href="cloud.html">shadw.cloud: hosting</a></li></ul></div>
<div><ul><li><a href="project-file.html">shadw.game.json and the CLI</a></li><li><a href="games.html">Games made with it</a></li><li><a href="shipwright.html">Brine &amp; Brie: Shipwright</a></li><li><a href="games.html#holy-temple">The Holy Temple</a></li><li><a href="https://shadw-game-store.shadw.app/">SHADW Game Store</a></li><li><a href="roadmap.html">Roadmap and decisions</a></li><li><a href="https://shadw-terrain.shadw.app/">SHADW Terrain site</a></li><li><a href="https://personalportfolio.shadw.app/">SolutionsAsService</a></li></ul></div>
</div></footer>
</body>
</html>
"""


def main():
    pages = sorted((ROOT / "_src" / "pages").glob("*.html"))
    urls = []
    for page in pages:
        title, description, key, *rest = page.read_text(encoding="utf-8").split("\n")
        slug = page.stem
        current = ' aria-current="page"'
        nav = "".join(f'<a href="{k}.html"{current if k == key else ""}>{label}</a>' for k, label in NAV)
        canonical = DOMAIN if slug == "index" else f"{DOMAIN}{slug}"
        html = LAYOUT.format(title=title, description=description, canonical=canonical, domain=DOMAIN,
                             mark=MARK, nav=nav, body="\n".join(rest).strip())
        (SITE / f"{slug}.html").write_text(html, encoding="utf-8")
        urls.append(canonical)
        print(f"site/{slug}.html")
    sitemap = "".join(f"<url><loc>{u}</loc></url>" for u in urls)
    (SITE / "sitemap.xml").write_text(
        f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{sitemap}</urlset>\n',
        encoding="utf-8")
    (SITE / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {DOMAIN}sitemap.xml\n", encoding="utf-8")


if __name__ == "__main__":
    main()
