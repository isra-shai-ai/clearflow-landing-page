# ClearFlow Implementation Rules

**Scope:** durable design and coding constraints only.

This file deliberately does **not** describe the build setup, output files, page inventory, deploy target, or the form submission pipeline. Those change; documenting them here is how this file rotted last time. For any of that, read:

- **`CLAUDE.md`** (project root) — build/CSS coupling, page architecture, form pipeline, accessibility gate, conventions
- **`package.json`** — the actual commands

If a rule below ever conflicts with observed code, the code wins — fix the rule, don't fix the code to match it.

## Core Stack

| Layer | Technology | Notes |
|---|---|---|
| **Icons** | Inline SVG only | Lucide-style, thin-stroke (stroke-width: 1.5), monochrome |
| **Fonts** | Google Fonts — Heebo / Rubik | Load via `<link>` in `<head>` |
| **JS** | Vanilla JS inline | No frameworks. Keep scripts minimal and inline |

## Layout Rules

- **Direction:** Always RTL. Every page must have `<html dir="rtl" lang="he">`.
- **Layout engine:** Tailwind Flexbox and Grid utilities only.
- **Responsive:** Mobile-first. Use `md:` and `lg:` breakpoints.

## Implementation Guidelines

### Navigation
- Transparent on load → `bg-[#11223A]` on scroll (JS `scroll` event listener)
- Text `text-white`. Phone number must render as amber pill.

### Hero Section
- Background: `bg-gradient-to-b from-[#11223A] to-[#1E3A5F]`
- Glassmorphism form wrapper: `bg-white/10 backdrop-blur-md border border-white/20`
- Inputs: single horizontal row on desktop, stacked on mobile

### Cards (Services section)
- Base: `bg-slate-50` with `border-r-4 border-r-[#1E3A5F]`
- Hover: `hover:-translate-y-1 transition-all duration-200`
- Icon: top-right corner, primary color, SVG only

### Forms
- Inline success state: hide inputs, show "תודה!" — no page reload, no redirect
- The submission mechanism itself is documented in `CLAUDE.md` — match the existing handler, don't invent a new one

### Sticky Elements
- WhatsApp button: bottom-left, perfectly centered SVG icon using `flex items-center justify-center`
- Cookie banner: fixed bottom, single line on desktop using `flex-nowrap`

## Forbidden Patterns

- ❌ No jQuery
- ❌ No Bootstrap
- ❌ No React / Vue / Angular (unless explicitly requested)
- ❌ No "pill" tags above H2 headings
- ❌ No colorful clipart or emoji-style icons — SVG only
