# Feature Implementation Plan - Phase 2: Robust Hebrew Content

**Overall Progress:** `60%`

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

- [ ] 🟥 **Step 2b: Mobile Hamburger Nav (prerequisite for production)**
  - Context: the header nav is `hidden md:flex` with **no mobile fallback** — below 768px it computes to `display: none` and there is no hamburger anywhere in the codebase. The Step 2 dropdown is therefore unreachable on phones; the only header controls left are the logo and the phone pill. This blocks go-live.
  - [ ] 🟥 Add a hamburger trigger visible below `md`, hidden at `md` and up.
  - [ ] 🟥 Build the panel — slide-out drawer or fullscreen overlay (decide before building).
  - [ ] 🟥 Include every nav destination: בית, יצירת קשר, and all 5 service pages (`ai-agents`, `automations`, `crm-systems`, `landing-pages`, `training`).
  - [ ] 🟥 Accessibility: `aria-expanded` on the trigger, `aria-controls`, focus trap while open, Escape to close, focus returned to the trigger on close, `inert`/`aria-hidden` on background content.
  - [ ] 🟥 RTL: drawer slides from the right; verify no horizontal overflow at 320px.
  - [ ] 🟥 Apply across all 6 Hebrew pages (`public/index.html` + `public/services/*.html`). Leave `/en/` alone per Decision 1.
  - [ ] 🟥 Keep the panel's show/hide CSS in `input.css` (Tailwind never scans it) or run `npm run build` and bump `styles.css?v=` if new utilities are introduced.

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

- [ ] 🟥 **Step 6: Write & Inject Automations Copy**
  - [ ] 🟥 Write full Hebrew copy based on the approved strategy and inject it.

- [ ] 🟥 **Step 7: Write & Inject CRM Copy**
  - [ ] 🟥 Write full Hebrew copy based on the approved strategy and inject it.

- [ ] 🟥 **Step 8: Write & Inject Training Copy**
  - [ ] 🟥 Write full Hebrew copy based on the approved strategy and inject it.
  
- [ ] 🟥 **Step 9: Final Polish & Accessibility (A11y) Audit**
  - [ ] 🟥 Ensure responsive design holds up with the expanded text.
  - [ ] 🟥 **Mandatory Step**: Run an accessibility audit checking for keyboard focus trapping, ARIA labels, and contrast ratios.
  - [ ] 🟥 Verify `input.css` compilation cleanly handles any new native Tailwind classes.

## Findings

- **No em dashes or en dashes in user-facing copy.** Shai flags them as an AI writing tell. Use commas, periods or colons instead. Applies to every Hebrew string across the site.
- **Automations page still stars an AI agent** in its own `בשטח` example ("תשתמש בסוכן בינה מלאכותית..."). Now that Step 4 claims the judgment ground for AI Agents, trim that mention in Step 6 or the two pages still blur.
