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

---

## Feature: Mobile Header Contact Icons

**Feature Progress:** `100%` (6 / 6 steps)

### TLDR

Put WhatsApp and phone one tap away on mobile. Two round icon buttons in the header next to the hamburger, modeled on hlk.co.il. Below `md` the header currently has only the hamburger and the logo; the phone pill is `hidden md:flex`. The floating WhatsApp becomes redundant on mobile and is hidden there, but stays on desktop. Desktop header is unchanged.

### Key Decisions

- Decision 1: **Mobile only (`md:hidden`)** — desktop already has the amber phone pill; no desktop header change.
- Decision 2: **Hide floating WhatsApp below `md`, keep it at `md`+** — the fixed header makes it redundant on mobile and frees the bottom-left corner.
- Decision 3: **Same `wa.me` URL + prefilled text as the float** — one message template sitewide, `target="_blank" rel="noopener noreferrer"`.
- Decision 4: **Dedicated GA events `click_whatsapp_header` / `click_phone_header`** — measures whether the change drives contact. Header buttons carry `data-track-event="<event name>"`; one handler sends it, and the generic `tel:` handler skips `[data-track-event]`, so a tap fires one event, not two.
- Decision 5: **Round buttons on a fixed light background** (`bg-white/90`, icon in WhatsApp green `#25D366` / `accent`) — readable over the see-through homepage header, the dark scrolled state (`#11223A`), and the `bg-primary` service-page header.
- Decision 6: **Work on branch `feat/header-contact-icons`**, preview-verify, then merge. Main untouched until then.

### Critical Files

- `public/index.html` — header icon group, float `md` gating, GA handler (`load` listener ~line 216)
- `public/services/{ai-agents,automations,crm-systems,landing-pages,training}.html` — same 3 changes (GA handler ~line 196)
- `public/styles.css` — regenerated by `npm run build` (new utilities)
- All HTML files linking `styles.css?v=4` — bump to `?v=5`
- Out of scope: `resources/automation-checklist.html` (no header), `/en/` (removed)

### Tasks

- 🟩 **Step 1: Branch**
  - 🟩 `git checkout -b feat/header-contact-icons` from up-to-date `main`

- 🟩 **Step 2: Header icon group (6 pages)**
  - 🟩 Insert a `md:hidden` flex group right after `#mobileNavToggle`: WhatsApp link, then `tel:0522296269` link
  - 🟩 Each: 44×44px (`w-11 h-11`) circle, Hebrew `aria-label` (WhatsApp one notes "נפתח בחלון חדש"), SVG `aria-hidden="true"`, visible focus ring
  - 🟩 Reuse the float's WhatsApp SVG path; standard phone handset SVG

- 🟩 **Step 3: Gate the float**
  - 🟩 Float `<a>`: `flex` → `hidden md:flex` on all 6 pages

- 🟩 **Step 4: GA tracking**
  - 🟩 Generic `tel:` handler: selector `a[href^="tel:"]:not([data-track])`
  - 🟩 Header buttons fire `gtag('event', 'click_whatsapp_header')` / `gtag('event', 'click_phone_header')`

- 🟩 **Step 5: Build & cache-bust**
  - 🟩 `npm run build` (minified), confirm new classes exist in `styles.css`
  - 🟩 Bump `styles.css?v=4` → `?v=5` in every HTML file that references it (also `resources/automation-checklist.html`, which was stale on `?v=2`)

- 🟩 **Step 6: Verify, a11y audit, ship**
  - 🟩 Checks below pass on local + Vercel preview (320/360/390/800/1280px, GA one event per tap, focus order, drawer; preview serves new markup + `?v=5` on all 6 pages)
  - 🟩 Commit, push branch, PR, merge on approval

### Verification

- `npm run dev`, homepage + 1 service page at 320, 360, 390px and at 768px+:
  - Mobile: hamburger + 2 icons + logo on one row, no overflow or wrap, no horizontal scroll; float WhatsApp gone
  - Desktop: header identical to today; float WhatsApp present
- Homepage header readable at scroll 0 (see-through) and after scroll (dark)
- WhatsApp opens `wa.me/972522296269` with the prefilled text in a new tab; phone opens dialer with `0522296269`
- GA: DevTools `dataLayer` shows exactly one event per tap (`click_whatsapp_header` / `click_phone_header`); desktop pill still sends `phone_call`
- Keyboard: Tab order is hamburger → WhatsApp → phone → logo; focus ring visible; mobile drawer still opens/closes
- Lighthouse a11y on mobile: no new violations (tap target size, names, contrast)
- Preview: `styles.css?v=5` served, new classes present

### Open Questions / Risks

- ~~**Tight fit at small widths.**~~ Resolved. At 320px the logo was pushed into the left padding and touched the icons. Fix: logo `min-w-[120px] md:min-w-[160px]`, header row `gap-2`. Verified 8px gap and no horizontal scroll at 320/360/390px; desktop unchanged.
- **Order differs from the reference.** hlk.co.il puts the logo on the right and the buttons on the left. Ours keeps the hamburger on the right (existing RTL position) with the icons next to it, and the logo on the left. Rebuilding the header layout to match exactly is out of scope.
- **Mobile GA events for WhatsApp start at zero.** The float has no WhatsApp click tracking today, so there's no baseline to compare against. The new header events are the first data.

---

## Feature: Homepage Conversion Fixes (critique 2026-09-27)

**Feature Progress:** `50%` (3 / 6 steps)

### TLDR

Fix the 3 top issues from the 2026-09-27 `/impeccable critique` of `public/index.html` (21/36):
- the near-invisible hero CTA (P0)
- fragile forms and bundled consent (P1)
- the missing human proof (P1)

Direction: founder-led, existing look kept. Homepage only. Built on a branch, and Shai reviews it on the Vercel preview before anything merges.

### Key Decisions

- Decision 1: **Founder block replaces the slogan "trust band"** (l.668-702). A zero-client agency sells the founder: photo, name, 2 lines, WhatsApp link.
- Decision 2: **Founder copy is first person singular ("אני").** This is a deliberate exception to `voice-tone.md`'s plural voice, scoped to the founder block only. The rest of the page stays "אנחנו".
- Decision 3: **No employer name and no LinkedIn link anywhere on the site.** The outside-work agreement (Aug 2026) forbids:
  - presenting as a firm employee, or implying the services come from the firm, including on a website;
  - showing both occupations in parallel on LinkedIn.

  Experience is described by role and domain only. Verified: no `linkedin`, `sameAs` or employer name exists in `public/` today.
- Decision 4: **Experience claim: "מעל 7 שנים".** Confirmed by Shai: work before and between the listed roles counts.
- Decision 5: **Ownership lives in the FAQ, not the founder block.** True (confirmed by Shai) but felt forced as the founder block closer. New FAQ item instead (Step 4), in the page FAQ *and* the `FAQPage` JSON-LD.
- Decision 6: **Post-submit promise is 24 hours, not same day.** Shai answers the same day *usually*, and the side business is capped at 5 h/week outside work hours. A promise that breaks for an 11pm lead costs more trust than it earns. "תוך 24 שעות" is specific and always keepable.
- Decision 7: **Make payload keys unchanged** (`fullName`, `phone`, `email`, `source`).
  - Footer email becomes optional. The key is omitted when empty, never sent as `""`.
  - Honeypot fake-success behavior is unchanged.
- Decision 8: **Each fix is its own commit**, so any one (especially the founder block) can be dropped without touching the others.

### Copy (exact strings, approve as part of this plan)

**Hero paragraph** (3 clauses → 1 sentence):
> פחות עבודה ידנית, יותר שליטה: אוטומציה שחוסכת לכם שעות ולא נותנת לאף ליד ליפול.

**Hero form heading** stays `לקביעת שיחת ייעוץ ללא עלות`. Its size drops from `text-4xl md:text-5xl` to `text-2xl md:text-3xl`.

**Under the hero button** (new):
> שיחת היכרות של 20 דקות, בלי עלות ובלי התחייבות. נחזור אליכם תוך 24 שעות.

**Hero success** (was "תודה! הפרטים התקבלו בהצלחה."):
> תודה! הפרטים התקבלו. נחזור אליכם תוך 24 שעות. רוצים לדבר כבר עכשיו? [כתבו לנו בוואטסאפ]

**Founder block** (option B, first person, ownership line removed):
> **שי ישראל, מייסד ClearFlow**
> מערכת טובה שווה משהו רק אם הצוות באמת עובד איתה. את זה אני עושה כבר מעל 7 שנים: הטמעת מערכות והדרכת צוותים.
> אני ממפה איתכם את התהליכים, בונה את האוטומציה ומדריך את הצוות שלכם לעבוד איתה.
> [דברו איתי בוואטסאפ]

**AI-agents card** (l.812; removes the "ללא מגע יד אדם" overclaim):
> נציגים וירטואליים שמשתלבים בעבודה שלכם: עונים ללקוחות, מסננים פניות ומבצעים משימות חוזרות סביב השעון, ומעבירים אליכם את מה שדורש החלטה.

**Consent label:** unchanged on all 3 forms (Shai's decision; marketing consent gets its own sprint).

**New FAQ item** (page `<details>` + `FAQPage` JSON-LD):
> **של מי המערכות בסוף?**
> שלכם. בסוף העבודה, כל מה שנבנה עובר אליכם: המערכות והחשבונות.

**Network error** (all 3 forms): keep the current text, and make "וואטסאפ" a real `wa.me` link.

### Critical Files

- `public/index.html`:
  - hero (l.458-517)
  - trust band → founder block (l.668-702)
  - AI card copy (l.812)
  - 3 forms: hero l.476, lead magnet l.946, footer l.1115
  - form JS: `validateForm` and the 3 submit handlers (~l.1204-1320)
- `public/assets/founder/shai-israel.jpg`: new, from the supplied 500×500 headshot (57 KB)
- `public/styles.css`: regenerated; `styles.css?v=5` → `?v=6` on every page
- Not touched: service pages, header/footer chrome, modals, `vercel.json`

### Data Schema

**Input:** form fields, names unchanged.

**Output** (to the Make webhook; keys unchanged):
```
Hero:        { fullName, phone, source: "Hero" }
Footer:      { fullName, phone, email?, source: "Footer" }   // email now optional: omitted when empty
Lead Magnet: { fullName, email, source: "Lead Magnet" }
```

**Phone check (client side):**
- Strip spaces, dashes and parentheses.
- Accept `^0(5\d|[2-4]|[89]|7\d)\d{7}$`, or the same with a `+972` / `972` prefix in place of the leading 0.
- The value sent stays what the visitor typed (trimmed), so the Airtable data format doesn't change.

**External dependency:** none new. The Make scenario must already accept a footer submission without `email`. **Verify in Step 5 with one real footer test lead (no email) before merge.**

### Tasks

- 🟩 **Step 1: Branch**
  - 🟩 `feat/homepage-conversion` from up-to-date `main`

- 🟩 **Step 2: Hero CTA (P0)** (commit 1)
  - 🟩 Submit button amber (`bg-amber-500 text-slate-900`, hover `bg-amber-400`), matching the other CTAs
  - 🟩 Form H2 smaller; hero paragraph down to 1 sentence; microcopy under the button
  - 🟩 Mobile: reduce `py-32` / `min-h-[85vh]` so the submit button is on the first screen at 375×667 (measured: bottom 655px; 320×568 still below the fold)
  - 🟩 Success state: new copy + WhatsApp link

- 🟩 **Step 3: Forms + consent (P1)** (commit 2)
  - 🟩 Israeli phone check in `validateForm`, with a specific Hebrew error ("מספר הטלפון לא תקין")
  - 🟩 `maxlength` (name 80, email 120, phone 20); `autocomplete` (`name`, `tel`, `email`); `inputmode="tel"`
  - 🟩 Error `<p>`s get `role="alert"`; focus moves to the success heading (`tabindex="-1"`)
  - 🟩 Footer email optional: drop `required`, omit the key when empty
  - 🟩 WhatsApp link inside the network-error text
  - 🟩 Verify honeypot fake success and payload keys are unchanged

- 🟥 **Step 4: Founder block (P1)** (commit 3)
  - 🟥 Copy the headshot to `public/assets/founder/shai-israel.jpg`
  - 🟥 Replace the trust band with the founder block:
    - photo (`alt="שי ישראל"`, width/height set, lazy-loaded)
    - name + role and the 2 lines
    - WhatsApp link (`target="_blank"`, new-window label)
  - 🟥 AI card copy (l.812)
  - 🟥 New FAQ item "של מי המערכות בסוף?" in the `<details>` list and the `FAQPage` JSON-LD (copy above)
  - 🟥 Brand tokens only (primary/accent/amber, Rubik); an H2 for the name, in the correct heading order

- 🟥 **Step 5: Build + verify**
  - 🟥 `npm run build`; bump to `?v=6` on all pages
  - 🟥 Run the checks below, plus `impeccable detect` on `public/index.html` (no new findings)
  - 🟥 Push the branch and send Shai the Vercel preview link

- 🟥 **Step 6: Shai reviews, then merge**
  - 🟥 Shai approves each of commits 1-3 (can drop any)
  - 🟥 Merge, verify production, clean up

### Verification

- **375×667:**
  - hero submit button fully visible without scrolling (cookie banner dismissed)
  - amber, contrast ≥ 4.5:1
- **320, 390, 768 and 1280px:**
  - no horizontal scroll
  - founder block reads well, and the photo doesn't distort
- **Hero, footer and lead-magnet forms:**
  - empty fields → specific errors, announced (`role="alert"`)
  - "abc" as the phone → phone error
  - `050-123 4567` and `+972 50 123 4567` pass
- **Honeypot filled:** fake success, no network request.
- **Network failure** (DevTools offline):
  - error shows with a working WhatsApp link
  - button re-enabled
- **Payload** (DevTools Network):
  - keys exactly as in Data Schema
  - footer without email sends no `email` key
- **Real footer test lead without email** lands in Airtable, which confirms Make accepts it.
- **Keyboard:**
  - Tab reaches every field and both WhatsApp links
  - focus is visible
  - focus lands on the success heading
- **`grep -i 'deloitte\|linkedin' public/`** stays empty.

### Open Questions / Risks

- **Marketing consent: out of scope.** Shai keeps the current bundled consent ("ואת קבלת הדיוור") for now and will handle it in a separate sprint (an opt-out Make automation already exists). Flagged in the critique as a likely compliance risk.
- **FAQ ownership answer: resolved.** Accounts are sometimes opened by the client, sometimes by Shai and transferred; the copy says only that everything is transferred, not how.
- **Hero copy changes are claims.** All new strings are above for approval; nothing else changes.
- **I'm not a lawyer.** The consent change and the reading of the employment agreement are my best reading, not legal advice.
