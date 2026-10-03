# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

ClearFlow — Hebrew/RTL B2B business-automation agency landing site for the Israeli market. Static HTML + compiled Tailwind, deployed to Vercel from `public/`. No framework, no bundler, no test suite.

## Commands

```bash
npm install
npm run dev      # parallel: tailwind --watch + live-server on public/ :3000
npm run build    # tailwindcss -i input.css -o public/styles.css --minify
```

There are no tests or linters. Verification is manual: `npm run dev`, open http://localhost:3000, click through in both desktop and mobile widths.

Vercel: build command `npm run build`, output dir `public`.

## Hard rules (from `.cursorrules` / `.clinerules`)

1. **Never modify `public/index.html` or other production HTML without explicit approval.** Ask first, every time.
2. Do not "sync" or "align" files outside the immediate scope of the request.

## CSS build coupling — read before touching classes

`public/styles.css` is **generated but committed to git** (`.gitignore` only excludes `node_modules/`). Tailwind scans `./public/**/*.html` only (`tailwind.config.js` `content`). So:

- New Tailwind utilities in any HTML file **do not exist** until `npm run build` runs. "It looks right in my editor" means nothing.
- After a build, commit the regenerated `public/styles.css` along with the HTML.
- Every page links `styles.css?v=N`. When the compiled CSS changes meaningfully, bump `N` in **all** HTML files or returning visitors get stale CSS.
- Custom keyframes/component CSS (blob, marquee/ticker, FAQ `<details>` accordion, `dialog::backdrop`, `.reveal-element`) live in `input.css`, not inline. Tailwind's `content` scan never sees `input.css` — anything hand-written there always ships.

## Page architecture — everything is duplicated

There is no templating layer. Header nav (with the Services dropdown), footer, the WhatsApp float, the cookie banner, and both `<dialog>` modals (`#privacyModal`, `#accessibilityModal`) are **copy-pasted into all 6 main HTML pages** (homepage + 5 service pages). A change to any shared chrome is an N-file change; enumerate the files first and apply consistently, subject to the approval rule above. (`resources/automation-checklist.html` is the exception — it carries only the footer and the cookie-consent script, no banner, header or modals.)

The `<head>` block is duplicated the same way: OG/Twitter tags, JSON-LD and `<link rel="canonical">`. The canonical is a **per-page value** — every page must self-reference its own canonical. (The `hreflang` tags were dropped with the `/en/` pages.) `og:url` / `twitter:url` must equal that page's canonical.

```
public/
  index.html                # Hebrew homepage — hero form, services grid, process, lead magnet, footer form
  services/{ai-agents,automations,crm-systems,landing-pages,training}.html
  resources/automation-checklist.html # gated lead magnet; noindex via vercel.json
research/*.md               # reference material at repo root, outside public/ so it is never deployed
```

The English `/en/` pages were removed (commit `1f5098a`); the site is Hebrew-only. Do not recreate them without being asked.

## Forms → Make.com

All three forms (hero, footer, lead magnet) POST JSON to one webhook, hardcoded in the inline script at the bottom of each page:

`https://hook.eu1.make.com/p3evkp5wlspqvo3g1ln8qyxanf23h7as`

Payload: `{ fullName, phone?, email?, source }` where `source` is `"Hero" | "Footer" | "Lead Magnet"` (a hidden input). The Make/Airtable mapping depends on these exact key names — renaming a field breaks the live lead pipeline silently.

Each form carries a honeypot `<input name="b_title">`. If it is non-empty, the handler **fakes success** (shows the thank-you state, skips the fetch). Preserve that behavior when editing form logic — a real error message would teach bots the check exists.

Success is an inline DOM swap (hide inputs, reveal `#heroFormSuccess` / `#footerSuccess` / `#leadMagnetSuccess`). Never a page reload or redirect.

## Design system

Source of truth: `.claude/skills/brand-identity/` — `design-tokens.json` (colors, glassmorphism, component recipes), `voice-tone.md` (Hebrew copy rules), `tech-stack.md`.

`tailwind.config.js` only defines four semantic colors (`primary #1E3A5F`, `accent #4A6FA5`, `surface`, `alt`) and the Rubik font. Everything else in the tokens file — amber CTAs (`#F59E0B`), dark nav (`#11223A`) — is written as arbitrary values in the HTML.

## Accessibility is a gate, not a nice-to-have

The site targets Israeli standard ת״י 5568 / WCAG 2.1 AA and ships the Tabnav widget. Per `.agents/rules/clearflow-rules.md`, audit before delivering UI code: heading nesting (H1→H2→H3), `aria-label` on every form and interactive control, `aria-hidden="true"` on decorative SVGs, keyboard reachability of the Services dropdown and `<dialog>` modals, contrast. Flag violations and get approval rather than shipping them.

## Conventions

- Every page: `<html dir="rtl" lang="he">`. RTL means `border-r-4`, and arrow icons point *left* for "forward".
- All user-facing copy is Hebrew. Follow `voice-tone.md`: direct, active voice, short sentences, plural "אתם/אנחנו", digits not spelled numbers, no emoji.
- All JS is vanilla and inline at the bottom of `<body>`. No modules, no external JS beyond GA (lazily injected on `load`) and the Tabnav widget.
- Cookie consent persists via `localStorage.cookieAccepted === 'true'`, checked in a separate trailing `<script>` on every page.
- `PLAN.md` is the live execution tracker (emoji status: 🟩 done / 🟨 in progress / 🟥 not started). Update it as work lands.
- `.agents/workflows/go-live.md` is the pre-deploy checklist (SPF/DKIM/DMARC, legal modals, end-to-end lead test, RTL/mobile pass).
- Canonical URLs use the `.html` extension — Vercel `cleanUrls` is off, so `/services/automations` 404s. `/` is the one directory-index exception.
- `public/og-image.jpg` (1200x630) is the share card for every page, referenced 3x per page (og:image, twitter:image, JSON-LD `image`). Regenerate it from `public/logo.png` over the brand gradient if the logo changes.
- `dump_hebrew.py` regenerates `all_content.md`, a flat dump of every Hebrew string across the Hebrew pages — useful for copy review and consistency sweeps. It hardcodes its file list and does not include `ai-agents.html`.
