# SunVex — sunvex.me

**Positioning:** AI automation & websites for Australian small business.
**Not:** An enterprise AI platform. No fake stats (no SOC 2, no uptime claims).
**Audience:** Tradies, local business owners, freelancers.

## Tech Stack

- **Build:** None — pure static HTML + CSS
- **Hosting:** Cloudflare Pages (via GitHub auto-deploy)
- **Domain:** sunvex.me (Cloudflare DNS)
- **Fonts:** Inter, self-hosted plan pending (currently Google Fonts CDN)

## Project Structure

```
sunvex-website/
├── index.html       # Single landing page (all CSS inlined)
├── assets/
│   ├── logos/       # SVG brand logos (synced from brand pack v1.1)
│   └── icons/       # SVG feature icons
├── CNAME            # Legacy GitHub Pages custom domain
├── README.md        # This project overview
├── AGENTS.md        # This file — project rules
└── .gitignore       # Git excludes
```

## Commands

No build step. Push to `main` → Cloudflare Pages auto-deploys.

```bash
# Dev (preview locally)
python3 -m http.server 8000

# Deploy
git push origin main
```

## Git Workflow

- **Default branch:** `main`
- **Branch naming:** `feat/<description>` or `fix/<description>`
- **Commit format:** `[verified] <one-line description>`
- **Pre-push:** Validate HTML (`index.html`) renders without errors

## Brand Alignment

- Colors: obsidian (#0B0B0D), graphite (#2A2A2D), stone (#E8E6E1), amber (#C9A463)
- Logos: source of truth = brand pack v1.1 (`support-internal/brand system/SUNVEX/`)
- Any SVG asset update must copy from brand pack release, never edit manually

## Boundaries

- **Never touch:** `node_modules/`, `.git/`, `dist/` (none exist)
- **Never commit:** credentials, `.env*`, API keys
- **Assets from brand pack only** — no hand-edited SVGs
