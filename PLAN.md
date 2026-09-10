# Feature Implementation Plan - Phase 2: Robust Hebrew Content

**Overall Progress:** `100%` (Steps 1-9 complete; see Pre-launch checklist below)

## TLDR

Pivoting focus away from the English localization (placed on hold) to deeply enrich the 5 Hebrew service pages. We are implementing a centralized Services dropdown menu in the global navigation, enhancing the articles with real-world examples, adding contextual CTAs at the bottom of articles, and performing a rigorous accessibility audit. All changes will be reviewed locally before any production deployment.

## Critical Decisions

- Decision 1: **Hold English Version** - We will pause all active development and routing updates for the `/en/` directory to focus 100% on the core Israeli audience.
- Decision 2: **Content Structure Standard** - Each service page will follow a strict B2B psychological structure: 1) The Core Problem, 2) The Solution (How it works), 3) Real-world Example/Use-case, and 4) Clear ROI/Impact.
- Decision 3: **Visual Examples Alignment** - We will adjust the HTML structure to include dedicated sections for "Use Cases" (e.g., side-by-side text and mockups/icons) so the examples are highly scannable.
- Decision 4: **Global Services Dropdown** - We will update the main navigation header across all pages to feature a hover/click dropdown under "שירותים" (Services), allowing direct jumps to specific articles.
- Decision 5: **Article Footer CTA** - We will add a soft, contextual CTA at the bottom of each article (e.g., "Ready to automate this? Let's talk"). This is necessary because readers who reach the bottom of an article have high intent, and we must capture that momentum without forcing them to hunt for a contact button.

## Tasks

- [x] 🟩 **Step 1: Define the Copy Strategy & Approvals**
  - [x] 🟩 Outline the core arguments and 1 concrete real-world example for each of the 4 services.
  - [x] 🟩 Get user approval on the written concepts.

- [x] 🟩 **Step 2: Implement Navigation Dropdown (Global)**
  - [x] 🟩 Update `public/index.html` and `public/services/*.html` headers to include an accessible dropdown menu for "שירותים".
  - [x] 🟩 Ensure `aria-expanded`, tabindex, and keyboard navigability are correctly implemented.

- [x] 🟩 **Step 2b: Mobile Hamburger Nav (prerequisite for production)**
  - Context: the header nav is `hidden md:flex` with **no mobile fallback** — below 768px it computes to `display: none` and there is no hamburger anywhere in the codebase. The Step 2 dropdown is therefore unreachable on phones; the only header controls left are the logo and the phone pill. This blocks go-live.
  - [x] 🟩 Add a hamburger trigger visible below `md`, hidden at `md` and up.
  - [x] 🟩 Build the panel — slide-out drawer or fullscreen overlay (decide before building).
  - [x] 🟩 Include every nav destination: בית, יצירת קשר, and all 5 service pages (`ai-agents`, `automations`, `crm-systems`, `landing-pages`, `training`).
  - [x] 🟩 Accessibility: `aria-expanded` on the trigger, `aria-controls`, focus trap while open, Escape to close, focus returned to the trigger on close, `inert`/`aria-hidden` on background content.
  - [x] 🟩 RTL: drawer slides from the right; verify no horizontal overflow at 320px.
  - [x] 🟩 Apply across all 6 Hebrew pages (`public/index.html` + `public/services/*.html`). Leave `/en/` alone per Decision 1.
  - [x] 🟩 Keep the panel's show/hide CSS in `input.css` (Tailwind never scans it) or run `npm run build` and bump `styles.css?v=` if new utilities are introduced.
  - Delivered in `2b0b77b` and `bacabb2`. Right-anchored drawer, focus trap, Escape, overlay and link close, `prefers-reduced-motion` respected. Trigger sits at the RTL start (right) with the logo flush left; DOM order matches RTL visual order so focus order stays correct. Verified at 320px, 375px and 1280px.

- [x] 🟩 **Step 3: Restructure Service Page HTML**
  - [x] 🟩 Update the HTML layout templates to support deeper content (Problem/Solution/Example/ROI framework).
  - [x] 🟩 Add contextual CTA block at the bottom of the article.
  - Verified across all 5 service pages: each carries H1 → Problem ("למה רוב X נכשלים?") → Solution → real-world example ("בשטח: …") → ROI list ("השורה התחתונה") → `<!-- Contextual CTA -->` block. Structure only; the copy inside it is Steps 4-8.

- [x] 🟩 **Step 4: Write & Inject AI Agents Copy**
  - Was a near-exact duplicate of `public/services/automations.html` (4 differing lines, all `<img>` swaps). Resolved in commit `7399fc5`.
  - Positioning: automations execute a process defined in advance; an AI agent decides what to do when the enquiry does not fit any template.
  - [x] 🟩 Write full Hebrew copy for the four-part structure (Problem / Solution / "בשטח" example / "השורה התחתונה" ROI) plus the contextual CTA.
  - [x] 🟩 Rewrite `<title>`, meta description, and OG/Twitter title+description so they no longer duplicate Automations.
  - [x] 🟩 Get user approval on the copy before touching the file (CLAUDE.md hard rule).

- [x] 🟩 **Step 5: Write & Inject Landing Pages Copy**
  - [x] 🟩 Write full Hebrew copy based on the approved strategy and inject it.
  - Body copy already existed and was page-specific. What was outstanding and is now done: page-specific `meta description`, `og:title`/`og:description` and `twitter:title`/`twitter:description` (commit `8799b20`), one en dash removed by rewriting an ungrammatical sentence, and the `בשטח` example expanded from 40 to 119 words with a concrete before/after (commit `ac85ad8`).

- [x] 🟩 **Step 6: Write & Inject Automations Copy**
  - [x] 🟩 Write full Hebrew copy based on the approved strategy and inject it.
  - Body copy already existed. Fixed in commit `9a164cc`: removed an unsourced third-party statistic (foodora / 26% churn), removed literal `**` markdown that rendered as visible asterisks, and rewrote the scenario to be deterministic end to end (57 to 111 words). Metadata and dashes were handled in `8799b20`, illustrative framing in `9cb1f1f`.

- [x] 🟩 **Step 7: Write & Inject CRM Copy**
  - [x] 🟩 Write full Hebrew copy based on the approved strategy and inject it.
  - Body copy already existed. Metadata and dashes fixed in `8799b20`, illustrative framing in `9cb1f1f`, scenario expanded to the three-beat arc in `db65fa7`, unsourced 20% claim removed in `7a92b95`.

- [x] 🟩 **Step 8: Write & Inject Training Copy**
  - [x] 🟩 Write full Hebrew copy based on the approved strategy and inject it.
  - Scenario rewritten to the three-beat adoption arc in `e299ac5` (43 to 132 words); spaced hyphen removed from the lede in `ae7c25b`.
  
- [x] 🟩 **Step 9: Final Polish & Accessibility (A11y) Audit**
  - [x] 🟩 Ensure responsive design holds up with the expanded text.
  - [x] 🟩 **Mandatory Step**: Run an accessibility audit checking for keyboard focus trapping, ARIA labels, and contrast ratios.
  - [x] 🟩 Verify `input.css` compilation cleanly handles any new native Tailwind classes.
  - Audit in `40f7444`: `aria-label` added to the footer form inputs, three `h2` to `h4` skips corrected, eight English `alt` strings translated. Focus indicators, keyboard order, `lang`/`dir`, link text, reduced motion and page titles all passed. Contrast tweaks follow in this commit.

## Findings

- **No em dashes or en dashes in user-facing copy.** Shai flags them as an AI writing tell. Use commas, periods or colons instead. Applies to every Hebrew string across the site.
- ~~Automations page stars an AI agent in its own example~~ Resolved in `9a164cc`. The Automations scenario is now deterministic and closes on "אין כאן פרשנות ואין החלטות", which is the boundary against the AI Agents page.
- **No client work exists yet.** Scenario sections must read as illustrations, never as delivered projects. All 5 service pages use the heading `דוגמה:` and open with "כך זה יכול להיראות אצלכם." (commit `9cb1f1f`). Same rule applies to any new copy.
- **No invented statistics.** No client metrics exist to cite. Keep ROI claims qualitative until Shai supplies real numbers.

## Pre-launch checklist

Steps 1-9 are complete. These are gates before the site goes live, not build work.

- [ ] 🟥 **Verify the Deloitte / Google citation.** `public/services/landing-pages.html` cites "Milliseconds Make Millions" for a 0.1 second mobile speed improvement and an 8.4% conversion lift. It is the only statistic left on the site. Confirm the exact figure, year and wording against the published report before launch. Note the 8.4% is the retail vertical specifically. An earlier Yottaa 2025 claim and an Akamai 100ms claim were both replaced and no longer appear anywhere.
- [ ] 🟥 **Run a Lighthouse audit** on the homepage and one service page, mobile and desktop. Check performance, accessibility, best practices and SEO. The a11y work in Step 9 was verified by hand and by scripted DOM checks, not by Lighthouse.
- [ ] 🟥 **Screen reader spot check** with NVDA or VoiceOver in Hebrew. Automated checks cannot confirm how the RTL content and the nav drawer actually announce.
- [ ] 🟥 **Run `npm run build` before committing.** `npm run dev` starts `tailwindcss --watch`, which rewrites `public/styles.css` unminified. Committing after a dev session ships a 3,000 line stylesheet instead of the minified one.
- [ ] 🟥 **`/en/` is still frozen** at Decision 1. It has no services dropdown, no mobile nav, stale copy, and `styles.css?v=2` while the Hebrew pages are on `?v=4`. Decide whether to unfreeze or noindex it before launch.
- [ ] 🟥 Work through `.agents/workflows/go-live.md` (SPF/DKIM/DMARC, legal modals, end to end lead test, RTL and mobile pass).
