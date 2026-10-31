# SHADW Game Suite site

The public site for the SHADW Game Suite: one project file and one CLI over SHADW Terrain, Forge, KeyForge and
shadw.cloud. Static and multi-page. Live address once deployed: https://shadw-gamesuite-site.shadw.app/

## Edit

Page bodies live in `_src/pages/*.html` (first three lines: title, description, nav key). The shared header, footer,
sitemap and robots file come from `_src/build.py`:

```bash
python -I _src/build.py
```

Styles are in `site/css/style.css`. Images in `site/img/` are real outputs: the Tidewatch map from SHADW Terrain,
the voxel demo rendered by Godot, and captures of Brine & Brie: Shipwright.

## Deploy

No build step on the host. The root `vercel.json` serves `site/`, `site/vercel.json` covers a Root Directory set to
`site`, and the root `index.html` redirects to `site/` for plain static hosts. All links are relative.

Design decisions and critique rounds: `DESIGN-LOG.md`.
