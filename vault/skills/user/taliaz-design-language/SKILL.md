---
name: taliaz-design-language
description: Taliaz brand design language with color tokens, typography, spacing, and component patterns. Apply when building any Taliaz visual output — dashboards, web apps, presentations, reports, PDFs, or slide decks. Provides exact hex/OKLCH color values, font stacks, spacing system, and reusable component patterns extracted from official Taliaz brand guidelines. Triggers on any Taliaz UI work, "make it look like Taliaz", "use Taliaz branding", "apply brand colors", or when creating any visual deliverable for Taliaz/HealthyMind.
---

# Taliaz Design Language

Brand-aligned design system for all Taliaz and HealthyMind visual outputs. Extracted from official brand guidelines (2024-2026).

## Quick Reference — Core Colors

| Role | Name | Hex | When to Use |
|---|---|---|---|
| **Primary text** | Navy | `#1B3A5C` | Headings, logo wordmark |
| **Primary action** | Teal | `#3BA99C` | Buttons, links, active states, Healthy Mind brand |
| **Accent/CTA** | Orange | `#F08C28` | CTAs, warnings, emphasis headings, logo dot |
| **Display text** | Blue Deep | `#0048AC` | Bold display numbers, emphasis blocks |
| **Icon/UI** | Accent Blue | `#64A4F8` | Icons, progress bars, interactive elements |
| **Page background** | BG Page | `#E8ECF8` | Default light background (lavender-blue) |
| **Card fill** | BG Card | `#B4D0F4` | KPI cards, stat blocks |
| **Table fill** | BG Table | `#CCD8F4` | Table cells, table headers |

## Quick Reference — Typography

| Context | Font | Weights |
|---|---|---|
| English UI | `Inter` | 400, 500, 600, 700 |
| Hebrew text | `Heebo` | 400, 500, 700, 800 |
| Data/code | `JetBrains Mono` | 400 |

Google Fonts CDN:
```html
<link href="https://fonts.googleapis.com/css2?family=Heebo:wght@300;400;500;700;800&family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
```

## Brand Identity

Two brand marks exist:

1. **Taliaz** (corporate): "iTALIAZ" wordmark in navy. The "i" is replaced by a stacked 3-circle icon — two teal circles with an orange dot on top. Used bottom-left on presentations, top-left in dashboards.

2. **Healthy Mind** (clinic service): Teal leaf/brain icon + "Healthy Mind" text in teal, with Hebrew subtitle "שירות פסיכיאטרי אינטגרטיבי". Used on clinical-facing materials.

## Design Principles

The Taliaz visual identity communicates **clinical trust** through a cool blue-lavender palette, **warmth** through orange accents, and **innovation** through the teal brand color. Key principles:

1. **Light, airy backgrounds** — The signature lavender-blue (`#E8ECF8`) creates a calm, clinical feel. Never use pure white as the page background.
2. **Generous whitespace** — Spacing is generous. Use the 4px-base spacing system. Cards and sections breathe.
3. **Flat, clean icons** — Blue-toned, flat or lightly outlined. No 3D, no gradients on icons.
4. **Orange for emphasis only** — Orange draws the eye. Use it sparingly for CTAs, accent lines, and warning text. Never as a large background fill.
5. **Rounded corners everywhere** — Cards use 12-16px radius. No sharp corners on interactive elements.
6. **Subtle decorative curves** — Soft teal/blue wave shapes at page edges add visual softness without competing with content.

## Application by Context

### Web Dashboards (like HealthyMind Dashboard)

Read `references/color-tokens.md` for the dark theme adaptation table. Dashboards typically use a dark sidebar with teal active-state accent, and either light or dark content area. KPI cards use the `--bg-card` fill in light mode or slate-800 in dark mode.

### Presentations & Slides

Use `--bg-page` (#E8ECF8) as the slide background. Headings in navy or orange. Stat cards in `--bg-card`. Logo bottom-left. Orange accent line (4px x 60-80px) under section headings.

### Reports & PDFs

Light background. Navy headings. Tables with `--bg-table` cell fills. Teal for positive indicators, orange for warnings. Logo in header.

### Web Applications

Read `templates/tailwind-theme.css` for a ready-to-use Tailwind v4 theme block. Apply `font-sans: Inter` for English, `font-hebrew: Heebo` for Hebrew content.

## Detailed References

Read these as needed — do not load all at once:

- **`references/color-tokens.md`** — Full color palette with CSS custom properties, Tailwind OKLCH values, semantic mappings, and dark theme adaptation
- **`references/typography-spacing.md`** — Type scale, font stacks, spacing system (4px base), border radius, and shadow tokens
- **`references/component-patterns.md`** — Visual patterns for KPI cards, tables, section headers, testimonials, decorative waves, icon style, logo placement, and dashboard layout
- **`templates/tailwind-theme.css`** — Copy-paste Tailwind v4 theme block with all brand colors and fonts
