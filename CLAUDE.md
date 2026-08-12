# Heritage Hearth — Raksha Bandhan storefront

A festive e-commerce site for Raksha Bandhan (a "festive occasions" storefront,
starting with Rakhi). Warm, colourful, "Modern Heritage" aesthetic.

## Design system — READ FIRST

`DESIGN.md` is the single source of truth for colour, type, spacing, shape, and
components. Honor it for every new page or change. Key points:

- **Colours** — Primary Deep Crimson `#8f000d`; Secondary Royal Gold `#fed65b`
  / `#735c00`; Tertiary Marigold `#7c5500`; Emerald accent for success/eco.
  Backgrounds are warm cream/parchment (`#fbf9f1` … `#e4e3db`) — never pure white.
- **Type** — Playfair Display for display/headline/product names; Montserrat for
  everything functional. `label-bold` for nav and badges.
- **Shadows** — warm crimson/brown tint at 5–8% opacity, never pure black.
- **Shape** — rounded; 0.5rem standard, up to 1.5rem for feature imagery.
- **Signature components** — gold-bottom-border primary buttons; Marigold
  "Bestseller" + Emerald "In Stock" pill badges; the "Rakhi Ribbon" decorative
  divider; marigold-flower / diamond bullets in product copy.

## Pages

- `index.html` — Home / landing (hero + live Rakhi countdown, shop-by-category,
  trending rakhis, build-a-hamper band, trust tiles, newsletter).
- `designer-rakhis.html` — Designer Rakhis (product listing + filters).
- `gift-hampers.html` — Gift Hampers (hero, ready-to-ship grid, Build-Your-Own-Box).

Header nav links Home / Designer Rakhis / Gift Hampers across all three pages;
Sweets & Treats / My Orders are `#` placeholders until built.

The Home countdown targets Raksha Bandhan (currently `2026-08-28` in the inline
script) — confirm/adjust the date there.

## Conventions

- **Self-contained pages.** Each page is a single HTML file with no external
  requests: Playfair Display + Montserrat are embedded as base64 `woff2`
  `@font-face` rules, icons are inline SVG, and product imagery is inline SVG
  placeholders captioned "Product photo" for easy swap with real photography.
- No build step, framework, or CDN. Plain HTML + hand-written CSS driven by the
  DESIGN.md tokens (mirrored as CSS custom properties in each page's `<style>`).
- Interactions (cart, filters, nav actions) are currently visual only.
