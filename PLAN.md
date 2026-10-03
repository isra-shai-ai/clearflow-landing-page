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

**Feature Progress:** `100%` (6 / 6 steps)

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
  - ~~Footer email becomes optional.~~ Reverted at review: Shai keeps footer email required.
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
Footer:      { fullName, phone, email, source: "Footer" }    // unchanged: email stays required (Shai, at review)
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
  - ~~Footer email optional~~ reverted at review (Shai keeps it required); email format check added instead
  - 🟩 WhatsApp link inside the network-error text
  - 🟩 Verify honeypot fake success and payload keys are unchanged

- 🟩 **Step 4: Founder block (P1)** (commit 3)
  - 🟩 Copy the headshot to `public/assets/founder/shai-israel.jpg`
  - 🟩 Replace the trust band with the founder block:
    - photo (`alt="שי ישראל"`, width/height set, lazy-loaded)
    - name + role and the 2 lines
    - WhatsApp link (`target="_blank"`, new-window label)
  - 🟩 AI card copy (l.812)
  - 🟩 New FAQ item "של מי המערכות בסוף?" in the `<details>` list and the `FAQPage` JSON-LD (copy above)
  - 🟩 Brand tokens only (primary/accent/amber, Rubik); an H2 for the name, in the correct heading order

- 🟩 **Step 5: Build + verify**
  - 🟩 `npm run build`; bump to `?v=6` on all pages
  - 🟩 Run the checks below, plus `impeccable detect` on `public/index.html` (no new findings). Local checks pass; detector shows 3 new findings, all false positives (light text on the navy hero measured against white; slate-900 on amber, ~8:1). Footer test lead not needed: email stays required (Shai)
  - 🟩 Push the branch and send Shai the Vercel preview link

- 🟩 **Step 6: Shai reviews, then merge**
  - 🟩 Shai approves each of commits 1-3 (can drop any)
  - 🟩 Merge, verify production, clean up

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

---

## Roadmap: Open Items (ranked 2026-10-02)

**Roadmap Progress:** `40%` (2 / 5 sprints)

Every sprint below that touches site files gets its own `## Feature:` section and needs "The plan is approved." before any code. Rank is by **risk first** (legal exposure, lost leads), then **conversion impact**, then **effort**.

### Ranking logic

| Rank | Why it's here |
|---|---|
| 1. Legal exposure | Spam law (per-message statutory damages) and Israeli accessibility regulations (IS 5568) both carry fines without proof of harm. |
| 2. Lead pipeline | A lead or checklist email that silently fails costs a customer. |
| 3. Conversion | Page structure changes that move consult requests. |
| 4. Polish | Visual and wording items with no measurable user impact. |

### 🟩 Sprint 0: Quick checks (Shai, ~15 min, no code) — done 2026-10-03; only the optional Search Console reindex is left

- 🟩 **GA Realtime:** confirmed 2026-10-03 (Shai, real phone tap): `click_whatsapp_header` and `click_phone_header` both arrive. The extra generic `click` event in the same session is GA4 enhanced measurement's automatic outbound-link click (the WhatsApp tap goes to wa.me), not a duplicate from our code.
- 🟩 **Checklist email sender:** Zoho via Make (Shai, 2026-10-02), covered by SPF/DKIM. confirm which service the Make scenario sends the checklist email through. DNS has SPF (`include:zohomail.com`), DKIM (`zmail._domainkey`) and DMARC (`p=none`) for **Zoho only**. If Make sends through Gmail, SendGrid or similar, SPF/DKIM fail and the checklist can land in spam.
- 🟩 **Mail-tester:** 9.5/10 (2026-10-03). SPF, DKIM, DMARC all pass via Zoho; sender IP on the Mailspike whitelist. Only deduction: `HTML_IMAGE_ONLY_28` (too little text vs. image, HTML-only, no plain-text part). Optional fix in Make: add 2-3 lines of body text. Test lead "TEST mail-tester Claude" to delete from Airtable.
- 🟨 **Search Console:** site side verified (2026-10-03): `/index.html` 308 → `/`, apex 301 → `www`, sitemap lists the 6 Hebrew pages. Reindex request itself is optional (Shai).

### 🟩 Sprint 1: Marketing consent (P1, legal) — rescoped 2026-10-02: no marketing is sent, so this became "Consent Cleanup + Privacy Policy", see its Feature section

- **Blocked on:** the research agent's report (running), then Shai's decisions.
- **Scope:** split the consent on all 3 forms into a required privacy checkbox + an optional, unchecked marketing checkbox. Store consent in Airtable (new payload key, so it's a **Data Schema change**: Make mapping + Airtable column, confirmed before code). Decide what to do with leads collected under the bundled consent.
- **Needs from Shai:** decisions on the research recommendations; Make/Airtable changes (Claude has no Make access).
- **Risk if delayed:** every marketing message sent to a lead without valid consent is exposed to statutory damages. Today the risk is dormant only because nothing is sent.

### 🟩 Sprint 2: Accessibility compliance pass (P1, legal) — shipped 2026-10-03 (PR #10), see its Feature section

The site declares IS 5568 / WCAG 2.1 AA in its accessibility statement; the known gaps make that claim inaccurate.

- 🟥 Phone pill: `aria-label="טלפון"` → include the visible number (WCAG 2.5.3), all 6 pages
- 🟥 `aria-hidden="true"` on the 5 original FAQ plus/minus icons
- 🟥 Visible focus rings where `focus:outline-none` has no replacement
- 🟥 `.reveal-element`: content must not stay `opacity: 0` if JS or the observer fails
- 🟥 Marquee/ticker: stop under `prefers-reduced-motion`
- 🟥 Accessibility statement: WCAG 2.0 → 2.1 AA; update the date
- 🟥 Lighthouse (mobile + desktop, homepage + 1 service page) before and after
- 🟥 Screen reader spot check in Hebrew (NVDA) — **Shai**, after the fixes
- **Effort:** small. Mostly attribute and CSS changes, across 6 pages for the shared chrome.

### 🟥 Sprint 3: Conversion structure (P2) — decisions made 2026-10-03, plan awaiting approval, see its Feature section

- 🟥 Lead magnet placement: move after the FAQ, or slim it down, so it stops competing with the consultation right before the final form
- 🟥 Services order: automation first (core offer), landing pages later
- 🟥 One CTA after the process section
- 🟥 Small wording: cookie banner singular "הנך מסכים/ה" → plural; one phone number format sitewide; muddy `bg-white/40` header over the hero on desktop
- **Needs from Shai:** decision on lead-magnet placement and services order (positioning choices, not technical ones).

### 🟥 Sprint 4: Measure, then polish (P3)

- 🟥 Re-run `/impeccable critique` on the homepage (baseline 21/36 on 2026-09-27)
- 🟥 Decide on the design-checker clichés from the new report: gradient text in the H1, glow shadows, nested cards. **Keep** the `border-r-4` service-card edge: it's the project's RTL convention.
- 🟥 `.agents/workflows/go-live.md` as a post-launch audit: error-route alert in Make if the webhook fails (no lead lost), end-to-end test lead, compressed images
- 🟥 Optional: update Impeccable to v4.4.0 (`npx impeccable update`)

### Sequencing

```
Sprint 0 (Shai, now) ──► Sprint 2 (a11y, can start now)
Research report ──► Sprint 1 (consent)          ──► Sprint 4 (measure)
                          Sprint 3 (after 1 and 2) ─┘
```

Sprints 1 and 2 don't touch the same code (forms vs. attributes and CSS), but both edit `public/index.html`, so they run one after the other, not in parallel.

---

## Feature: Sprint 1, Consent Cleanup + Privacy Policy

**Feature Progress:** `100%` (5 / 5 steps)

### TLDR

ClearFlow sends no marketing messages and plans none (no newsletter; leads only, 1-2 jobs a month). So no marketing consent is needed. Remove the bundled "דיוור" clause from all 3 forms, use one identical consent line everywhere, and bring the privacy policy in line with Privacy Protection Law section 11 (Amendment 13): name the controller, say that giving details is voluntary, name the processors, drop the marketing purpose.

Research basis: consent research report, 2026-10-02, primary sources. Key points: the PPA consent opinion (25.2.2026) objects to marketing consent bundled into a required box; Communications Law 30A needs prior opt-in *only* for advertising; replying to a person's own request is not unsolicited advertising.

### Key Decisions

- Decision 1: **No marketing checkbox at all.** Shai sends no marketing and plans none. If that changes, add an optional, unticked checkbox at that point (and get a short legal consult then).
- Decision 2: **One identical consent line on all 3 forms** (Shai's request): `אני מסכים/ה ל[מדיניות הפרטיות].`
- Decision 3: **The checklist email stays as is.** Reviewed 2026-10-02: it delivers only the checklist, a "reply with questions" line and a standard signature. There is no service pitch and no "book a call" CTA, so it's delivery, not advertising. **Rule going forward:** never add a sales CTA or service links to it.
- Decision 4: **No Make / Airtable / payload changes.** Nothing new to store.
- Decision 5: **No lawyer needed in this scope** (Claude's assessment, not legal advice). Revisit if marketing messages ever start.

### Copy (exact strings, approve as part of this plan)

**Consent line, all 3 forms** (hero, footer, lead magnet):
> אני מסכים/ה ל[מדיניות הפרטיות].

- Hero / footer: label "אני מאשר/ת שקראתי את" → "אני מסכים/ה ל", the button text "תנאי מדיניות הפרטיות" (hero) → "מדיניות הפרטיות", and delete `<span>ואת קבלת הדיוור.</span>`.
- Lead magnet: "אני מסכים/ה למדיניות הפרטיות ולקבלת דיוור (אפשר להסיר תמיד)." → the line above.
- Chosen by Shai 2026-10-02 over "אני מאשר/ת את", "מאשר/ת את" and a checkbox-free "בשליחת הטופס..." line: standard wording, active consent (also the basis for the transfer to Airtable), no JS change.

**Privacy modal** (`#privacyModal`, identical on 6 pages). Plural voice (per `voice-tone.md`), "חברת" removed (ClearFlow is an עוסק פטור, not a company):

> **מדיניות פרטיות - ClearFlow**
> ClearFlow, בבעלות שי ישראל ("אנחנו"), מכבדת את פרטיותכם. כאן מוסבר איזה מידע אנחנו אוספים ומה אנחנו עושים איתו.
>
> **1. המידע שאנחנו אוספים:** שם מלא, טלפון ודוא״ל שאתם ממלאים בטפסים, ומידע על השימוש באתר שנאסף אוטומטית באמצעות עוגיות (Cookies).
>
> **2. מסירת המידע:** מסירת הפרטים היא מרצונכם, ואין חובה חוקית למסור אותם. בלי שם ודרך ליצירת קשר לא נוכל לחזור אליכם או לשלוח את הצ'קליסט שביקשתם.
>
> **3. למה אנחנו משתמשים במידע:** כדי לחזור אליכם בנוגע לפנייה שלכם, לשלוח את מה שביקשתם, ולשפר את האתר. אנחנו לא שולחים דיוור שיווקי.
>
> **4. מי עוד רואה את המידע:** אנחנו לא מוכרים ולא משכירים מידע אישי. כדי להפעיל את האתר והטפסים אנחנו משתמשים בספקי שירות: Make (אוטומציה, שרתים באיחוד האירופי), Airtable (שמירת פניות, שרתים בארה״ב), Zoho (משלוח דוא״ל) ו-Google Analytics (סטטיסטיקת שימוש באתר), וכן ספקי שירות נוספים שנדרשים להפעלת האתר והטפסים. המידע נשמר בחשבונות של ClearFlow אצל ספקי השירות האלה, ולכן הוא עשוי להיות מאוחסן בשרתים מחוץ לישראל. בשליחת טופס אתם מסכימים לכך. מידע יימסר לרשויות רק אם החוק מחייב זאת.
>
> **5. אבטחת מידע:** אנחנו מגינים על המידע ומגבילים את הגישה אליו.
>
> **6. הזכויות שלכם:** אתם יכולים לבקש לעיין במידע עליכם, לתקן אותו או למחוק אותו.
>
> **7. יצירת קשר:** בכל שאלה: 052-229-6269 או shai@clearflow.co.il.
>
> *עודכן לאחרונה: {DATE}*

`{DATE}` is the ship date.

### Critical Files

- `public/index.html`: 3 consent lines + privacy modal
- `public/services/{ai-agents,automations,crm-systems,landing-pages,training}.html`: privacy modal only (these pages have no forms)
- Not touched: `resources/automation-checklist.html` (no modal), form JS, payload, Make, Airtable

### Tasks

- 🟩 **Step 1: Branch** `chore/consent-cleanup`
- 🟩 **Step 2: Consent line** on the 3 homepage forms (commit 1). Hero/footer: "ל" moved into the link ("למדיניות הפרטיות") so it doesn't render as "ל מדיניות"
- 🟩 **Step 3: Privacy modal** replaced identically on all 6 pages (commit 2); verify all 6 copies are byte-identical (sha256 match). CSS rebuilt (`text-xs` added, unused `px-1` dropped) → `styles.css?v=7` on all 7 pages
- 🟩 **Step 4: Verify**
  - 🟩 `grep -c 'דיוור'`: the only hit per page is the new policy line "אנחנו לא שולחים דיוור שיווקי"
  - 🟩 Each form still submits; required checkbox still blocks submit; payload unchanged
  - 🟩 Privacy modal opens and closes from the form link, content scrolls
  - 🟩 Preview link to Shai
- 🟩 **Step 5: Shai reviews, merge, verify production, cleanup**

### Verification

- No "דיוור" anywhere in `public/`
- The 3 consent lines are identical text
- 6 privacy modals identical (hash compare)
- Form submit with fetch intercepted: same payload keys as before; checkbox unticked → "יש לאשר את מדיניות הפרטיות."
- Mobile 375px: modal scrolls, close button reachable

### Open Questions / Risks

- **Review changes (Shai, preview):** storage sentence reworded (data sits in ClearFlow's own accounts, not "passed to" providers; legally still a transfer abroad, hence the consent). Security line: generic "מגינים ומגבילים גישה" instead of "סבירים" (weak) or naming 2FA (uncommon on small B2B sites, and Airtable has no 2FA yet). **Shai to enable 2FA on Airtable.**

- **Processor list:** ends with "וכן ספקי שירות נוספים שנדרשים להפעלת האתר והטפסים" (Shai, option 1). When a significant new tool is added (e.g. a CRM), name it in the list and update the date.

- ~~**Which service sends the checklist email?**~~ Resolved: Zoho, via Make. Matches the domain's SPF/DKIM, so the Sprint 0 sender check is closed (mail-tester still open).
- **Airtable data transfer.** Consent at form submission (regulation 2(1)) is the simplest legal basis, and the policy wording above provides it. Airtable's DPA is a second basis, but it's unverified.
- **Checklist email, optional and not required:** its footer says "להסיר את עצמך מרשימת התפוצה" / "הודעות נוספות", which hints at a mailing list that doesn't exist. Shai may soften it in Make (e.g. "לא נשלח לכם הודעות נוספות בלי שתבקשו"). The email also uses singular "שלך/תמצא", while the site voice is plural.
- **Not legal advice.**

---

## Feature: Compact Mobile Header

**Feature Progress:** `100%` (5 / 5 steps)

Mobile header was 76px (68 scrolled) with 44px circles and a 32px logo; mobile norm (Apple / Material) is ~56px with ~24-36px visuals inside 44px tap areas. Approved by Shai in chat 2026-10-02.

- 🟩 **Step 1: Branch** `feat/mobile-header-compact`
- 🟩 **Step 2: Header, all 6 pages (mobile only)**: padding `py-2.5` (header 56px, fixed, no jump on scroll); scroll script swaps `md:py-4`/`md:py-3` only; hamburger 24px icon in 36px box; WhatsApp/phone 36px circles with 20/18px icons; 44px tap areas via `before:-inset-1`; logo `h-7` (28px); first-section top padding reduced to match (home `pt-20`, services `pt-24`)
- 🟩 **Step 3: Build**, `styles.css?v=8`
- 🟩 **Step 4: Verify**: 375/320px header 56-57px, tap 3px outside the circle still hits it, no horizontal scroll, hero button bottom 655 → 639px; desktop unchanged (77px, 69 scrolled)
- 🟩 **Step 4b: Smaller icons (Shai's review)**: circles 36 → 32px (icons 18/16px), menu box 36 → 32px, circle gap 8 → 12px so the 44px tap areas (`before:-inset-1.5`) touch without overlapping; header padding `py-3` keeps it at 56px. CSS v=9
- 🟩 **Step 5: Shai reviews preview on his phone, merge**

---

## Feature: Sprint 2, Accessibility Compliance Pass

**Feature Progress:** `100%` (7 / 7 steps) — shipped 2026-10-03 (PR #10)

### TLDR

The accessibility statement claims ת״י 5568 / WCAG AA. Close the known gaps so the claim is true: accessible names, decorative icons, visible focus, a pausable marquee, respect for the OS "Reduce Motion" setting, and an accurate statement. Attributes, CSS and ~10 lines of JS. No copy changes beyond the statement line, no form logic or payload changes. `/en/` excluded.

### Key Decisions (Shai, 2026-10-03)

- Decision 1: **Reduced motion covers all motion** (marquee, reveal-on-scroll, blobs, smooth scroll). Users without the OS setting see no change.
- Decision 1b (revised 2026-10-03): **No visible pause button (Shai).** Tap/click on the strip toggles pause; keyboard focus pauses; hover pauses on mouse devices only; screen readers hear a hint (`sr-only`). This covers every input, but discoverability is a gray zone: a strict audit could ask for a visible control. Reduce Motion already stops it for the users most at risk. Original: **Marquee gets a pause button** for everyone (WCAG 2.2.2, Level A: auto-moving content > 5s needs pause, decorative included). Hover-only pause doesn't work on touch or keyboard.
- Decision 2: **Phone pill: drop `aria-label`**; the visible number becomes the accessible name.
- Decision 3: **Consent checkboxes: name = visible text.** Remove the hero `aria-label`; restructure so the label reads "אני מסכים/ה למדיניות הפרטיות". Visible text unchanged.
- Decision 4: **Statement:** "WCAG 2.0" → "WCAG 2.1 ברמת AA" + "עודכן לאחרונה: {ship month}" line (same style as the privacy modal).
- Decision 5: **Lighthouse local only**, before and after.
- Decision 6: **Delete the duplicate marquee hover rule** in `input.css` (lines 48-50 duplicate 153-155).

### Changes

**A. Phone pill** (desktop header, 6 pages): remove `aria-label="טלפון"` from `<a href="tel:0522296269">`. Name becomes "052-2296269".

**B. FAQ icons** (`index.html`, 5 svgs ~lines 1016-1084): add `aria-hidden="true"` to every `faq-icon-plus` / `faq-icon-minus` svg that lacks it.

**C. Focus rings** — add `focus-visible:ring-2` (amber-400 on dark, primary on light) where `focus:outline-none` has no replacement:
- Hamburger `#mobileNavToggle` (6 pages)
- Services dropdown toggle (6 pages)
- Mobile nav close button (6 pages)
- Hero + footer "למדיניות הפרטיות" buttons (index)
- Not touched: `h3 tabindex="-1"` success headings (programmatic focus only, never in tab order); dropdown menu items (already have `focus:bg-slate-50`)

**D. Consent checkboxes** (index, hero + footer): remove hero `aria-label="אישור מדיניות פרטיות"`; set `aria-labelledby` on both checkboxes to the label span + policy button so the name is "אני מסכים/ה למדיניות הפרטיות". Clicking the button still opens the modal; clicking the label text still toggles the box.

**E. Motion** (`input.css`):
```css
@media (prefers-reduced-motion: reduce) {
  html { scroll-behavior: auto !important; }
  .blob, .animate-marquee-rtl { animation: none !important; }
  .reveal-element { opacity: 1; transform: none; transition: none; }
}
.marquee-container.is-paused .animate-marquee-rtl { animation-play-state: paused; }
@media (scripting: none) { .reveal-element { opacity: 1; transform: none; } }
```
Reveal JS (7 pages): if `IntersectionObserver` is missing, add `is-revealed` to every `.reveal-element` immediately.

**F. Marquee pause (index only), REVISED, no button:** `.marquee-container` gets `tabindex="0"`, `role="group"`, `aria-labelledby="toolsTickerLabel"`, `aria-describedby` → sr-only "הקישו על פס הלוגואים כדי לעצור או להפעיל את התנועה."; click toggles `.is-paused`; `:focus-visible` pauses with an inset ring; hover pause wrapped in `@media (hover: hover)` because touch keeps `:hover` stuck after a tap and blocked tap-to-resume. *Superseded original:* a small round button next to the ticker, `aria-label="עצירת אנימציית הלוגואים"` / `"הפעלת אנימציית הלוגואים"`, `aria-pressed`, pause/play icon (`aria-hidden`). Toggles `.is-paused` on `.marquee-container`. Hidden under reduced motion (nothing to pause).

**G. Statement** (`#accessibilityModal`, 6 pages, byte-identical): "וכן עומד בהנחיות WCAG 2.0" → "וכן עומד בהנחיות WCAG 2.1 ברמת AA" + `<p class="text-xs text-slate-500">עודכן לאחרונה: {month} 2026</p>`.

**H. Cleanup:** delete `input.css` lines 48-50 (duplicate hover-pause).

### Critical Files

- `public/index.html`: A-G
- `public/services/{ai-agents,automations,crm-systems,landing-pages,training}.html`: A, C (header), E (reveal JS), G
- `input.css`: E, H
- `public/styles.css` (rebuilt) → `styles.css?v=10` on all 7 pages (incl. `resources/automation-checklist.html`, version bump only)

### Tasks

- 🟩 **Step 1: Branch** `fix/a11y-pass`; Lighthouse baseline (perf/a11y/bp/seo): `/` mobile 83/100/100/100, desktop 98/100/100/100; automations mobile 88/100/100/100, desktop 95/100/100/100. a11y was already 100: Lighthouse does not detect any of these gaps
- 🟩 **Step 2: Shared chrome, 6 pages** (A, C header, G); verify modal copies byte-identical (hash)
- 🟩 **Step 3: Homepage-only** (B, C consent buttons, D, F). Pause button keeps one fixed `aria-label` ("עצירת אנימציית הלוגואים") and flips only `aria-pressed`; a label that also flips would announce the state twice
- 🟩 **Step 4: Motion + CSS** (E, H), reveal JS fallback on the 6 pages that use `.reveal-element`; reduced-motion also stops the unused `.ticker-track`
- 🟩 **Step 5: Build**, `?v=10` on all 7 pages
- 🟩 **Step 6: Verify**: headless Chrome checked accessible names (checkboxes "אני מסכים/ה למדיניות הפרטיות", phone pill "052-2296269"), pause by Enter/Space with `aria-pressed` flip, focus rings, reduced motion (marquee/blobs off, reveal visible, button hidden, scroll auto), JS off (reveal visible), normal scroll reveal, hero submit (blocked unticked; payload `{fullName, phone, source}` unchanged), 375px no horizontal scroll. Lighthouse after: a11y 100 on all 4 runs; perf 83/94/89/95. The desktop drop from 98 to 94 is local noise: re-running the `main` code now also gives 93 (FCP 0.9s then, 1.2s now on both)
- 🟩 **Step 6b: Button → tap-to-stop (Shai)**: verified with touch emulation (tap pauses, second tap resumes), keyboard (Tab pauses, Tab away resumes), mouse (hover pauses; click toggles), accessible name and description, reduced motion still off, 375px no horizontal scroll
- 🟩 **Step 7: Shai reviews (incl. NVDA Hebrew spot check), merge, verify production**: Shai passed all points on the preview; production on www checked: v=10 on all 7 pages, statement 2.1 on 6, tap pause/resume, hero submit payload unchanged (fetch intercepted)

### Verification

- `grep 'aria-label="טלפון"'` hits only the two phone `<input>`s
- No `faq-icon` svg without `aria-hidden="true"`
- Keyboard Tab through header, mobile nav, hero form, FAQ, footer form: every stop shows a visible ring
- Accessibility tree (DevTools): hero + footer checkbox name = "אני מסכים/ה למדיניות הפרטיות"; phone pill name = number
- DevTools "Emulate prefers-reduced-motion: reduce": marquee, blobs static; all reveal content visible without scrolling; pause button hidden
- Without emulation: site looks and moves exactly as before; pause button stops/resumes marquee by click, Enter and Space; `aria-pressed` flips
- JS disabled: all reveal content visible
- 6 accessibility modals identical (hash); "WCAG 2.0" gone
- Forms still submit (fetch intercepted, payload unchanged); required checkbox still blocks
- 375px and desktop: no layout change except the pause button
- Lighthouse a11y score ≥ baseline on all 4 runs

### Open Questions / Risks

- **Pause button placement/look:** proposed small circle at the ticker's end edge, muted style. Shai reviews on preview.
- **Tabnav widget** may also offer "stop animations"; we don't rely on it (third-party, may change).
- **Lighthouse ≠ compliance.** It catches ~30% of issues; the NVDA spot check and keyboard pass matter more.
- **Not a legal audit.** A formal 5568 audit by a certified accessibility consultant is the only proof of compliance if challenged.

**Flagged, not fixed (outside this sprint):**
- The lead-magnet consent checkbox name reads "אני מסכים/ה ל מדיניות הפרטיות ." (extra spaces, because the button sits inside the label). Screen readers handle it; tidy it if that form is ever edited.
- The service pages run two identical reveal `IntersectionObserver` scripts. Harmless, but one is redundant.
- Impeccable hook findings on index (gradient H1 text, contrast flags) predate this sprint; they're Sprint 4.

---

## Feature: Sprint 3, Conversion Structure

**Feature Progress:** `86%` (6 / 7 steps)

### TLDR

Make the homepage push one ask: the free consult. Add a booking button where intent peaks (after the 3-step process), move the checklist offer out of the middle of the page into a slim "not ready yet?" strip under the final form, reorder the service cards, and fix 3 small wording/visual issues. Also give checklist downloads their own GA label so Sprint 4 can measure the change. No change to what the forms send, so Make and Airtable are untouched. The site has no `/en/` directory anymore; only the 7 Hebrew pages exist.

### Key Decisions (Shai, 2026-10-03)

- Decision 1: **North Star = consult requests** (hero + footer forms). Checklist downloads are secondary; since Sprint 1 no follow-up is sent to checklist leads.
- Decision 2: **Lead magnet → slim strip below the final contact form** (option a). Consult ask comes first; the strip catches visitors not ready for a call. Accepted trade-off: fewer downloads.
- Decision 3: **Services order: AI agents stays the featured full-width card** (option b, "everyone talks about AI agents"), then automations → CRM → landing pages → training. **Menu must match the cards.** Checked: the desktop dropdown and mobile menu on all 6 pages already read AI → automations → CRM → landing → training, so only the homepage cards move (landing pages goes from 2nd to 4th).
- Decision 4: **Amber CTA "לקביעת שיחת ייעוץ" after the process section**, scrolls to `#contact`, tracked as GA event `click_cta_process`.
- Decision 5a: **Cookie banner in plural** (6 pages).
- Decision 5b: **Visible phone format `052-229-6269`** everywhere. `tel:`, `wa.me` and JSON-LD stay machine format.
- Decision 5c: **Header over the hero: translucent navy until scroll.** Scrolled state (solid `#11223A`) unchanged.
- Decision 6: **Scope:** items 2, 3, 4, 5c, 9 = `index.html` only. Items 5a, 5b = index + 5 service pages. The checklist page has no cookie banner text or visible phone, so it changes only for the CSS version bump.
- Decision 7: **No payload change.** `{ fullName, phone?, email?, source }` and source values stay exactly as they are.
- Decision 8: **Claude drafts all new copy** (below); Shai approves it with this plan.
- Decision 10 (added after preview, Shai 2026-10-03): **Tighter section spacing on the homepage.** Mobile: the 4 middle sections go from 96px to 64px padding per side (`py-16 md:py-24`); desktop unchanged. Contact form bottom padding 128px → 48px mobile / 64px desktop, and the strip top padding 56px → 48px, so the checklist strip reads as a follow-up to the form. Measured content gaps: mobile middle sections 190–233px → 128–169px; contact → strip 226/242px → ~100px visible. Service pages likely have the same mobile padding; left for Sprint 4.
- Decision 9: **Checklist GA label fix:** `generate_lead` from the lead-magnet form gets `event_label: 'lead_magnet'` instead of `'contact_form'`.

### New / changed copy (for approval)

| Where | Current | New |
|---|---|---|
| Process CTA button | (none) | **לקביעת שיחת ייעוץ** |
| Lead-magnet strip H2 | האם העסק שלכם מוכן לאוטומציה? | **לא מוכנים לשיחה עדיין?** |
| Lead-magnet strip line | ודאו שאינכם משאירים כסף על השולחן. הורידו את הצ'ק-ליסט... | **קחו את הצ'ק-ליסט החינמי: 7 נורות האזהרה שמראות איפה בורחות לכם שעות והכנסות.** |
| Cookie banner | אנו משתמשים בעוגיות (Cookies) כדי להעניק לך את החוויה הטובה ביותר. בהמשך הגלישה, הנך מסכים/ה לשימוש בהן. | **אנחנו משתמשים בעוגיות (Cookies) כדי להעניק לכם את החוויה הטובה ביותר. בהמשך הגלישה, אתם מסכימים לשימוש בהן.** |
| Phone (visible + aria-label) | 052-2296269 | **052-229-6269** |

Lead-magnet button text, consent text and success message ("מעולה! הצ'ק-ליסט בדרך אליכם!") stay as they are. The 3 checklist bullets are dropped from the strip (the new line summarizes the first one).

### Critical Files

- `public/index.html`: services card order; process CTA; lead-magnet section moved below `#contact` and slimmed; header unscrolled class + scroll JS; contact-click tracking selector; lead-magnet GA label; cookie text; phone format
- `public/services/{ai-agents,automations,crm-systems,landing-pages,training}.html`: cookie text; phone format
- `public/resources/automation-checklist.html`: `styles.css?v=11` only
- `public/styles.css`: regenerated by `npm run build` (new arbitrary classes, e.g. `bg-[#11223A]/70`)
- `CLAUDE.md`: one-line fix, `/en/` no longer exists (stale docs)

### Data Schema

No change. Webhook URL, keys (`fullName`, `phone`, `email`, `source`), source values (`"Hero" | "Footer" | "Lead Magnet"`), honeypot `b_title` with fake success, and inline success swap all preserved. The lead-magnet form keeps its IDs (`leadMagnetForm`, `leadMagnetSuccess`) so the existing handler works unchanged after the move.

GA events only (no Make/Airtable impact):
- New: `click_cta_process` (process CTA)
- Changed: lead-magnet `generate_lead` label `contact_form` → `lead_magnet`

### Tasks

- 🟩 **Step 1: Branch + baseline**
  - 🟩 `feat/sprint3-conversion` from `main`
  - 🟩 Screenshot homepage at 390px and 1280px (before)

- 🟩 **Step 2: Services order** (`index.html`)
  - 🟩 Move the landing-pages card from 2nd to 4th: AI (featured) → automations → CRM → landing pages → training
  - 🟩 Confirm menu order on all 6 pages still matches (no edit expected)

- 🟩 **Step 3: Process CTA** (`index.html`)
  - 🟩 Amber button under the 3 process cards: `<a href="#contact" data-track-event="click_cta_process">לקביעת שיחת ייעוץ</a>`, brand amber CTA recipe from `design-tokens.json`, visible focus ring, ≥ 44px tap target
  - 🟩 Contact-click tracking selector gets `:not([data-track-event])` (same pattern as the phone handler) so the new button counts once, not twice

- 🟩 **Step 4: Lead magnet → slim strip** (`index.html`)
  - 🟩 Move the section from between process and FAQ to directly after `#contact`, before `<footer>`
  - 🟩 Slim layout: H2 + one line + form in one compact row on desktop, stacked on mobile; drop the 3 bullets, blobs and "מדריך חינם" pill
  - 🟩 Keep form IDs, field names, hidden `source="Lead Magnet"`, honeypot, consent checkbox, success state
  - 🟩 Tidy the consent label spacing (flagged in Sprint 2: "tidy it if that form is ever edited")
  - 🟩 GA label `contact_form` → `lead_magnet` in the lead-magnet handler only

- 🟩 **Step 5: Header over the hero** (`index.html`)
  - 🟩 Unscrolled class `bg-white/40` → `bg-[#11223A]/70` in the `<header>` and both branches of the scroll JS (all widths; mobile has the same issue)

- 🟩 **Step 6: Wording, 6 pages**
  - 🟩 Cookie banner text → plural (index + 5 service pages)
  - 🟩 Phone `052-2296269` → `052-229-6269` in visible text and aria-labels (mobile nav, header icon, desktop pill)
  - 🟩 `grep` every page: 0 hits for `הנך מסכים` and `052-2296269`. Mixed line endings: use `\r?\n` in multi-line replacements
- 🟨 **Step 7: Build, verify, ship**
  - 🟩 `npm run build`; `styles.css?v=10` → `?v=11` on all 7 pages
  - 🟩 Run Verification below; after screenshots
  - 🟩 Spacing pass (Decision 10), rebuilt and re-measured
  - 🟥 Push branch, send Shai the Vercel preview link; merge after approval; verify production

### Verification

- **Section order on index:** hero → ticker → founder → pain/solution → services → process (+CTA) → FAQ → contact → checklist strip → footer
- **Services:** cards read AI → automations → CRM → landing → training; menu (desktop + mobile) shows the same order on all 6 pages
- **Process CTA:** click scrolls to `#contact` without the heading hidden under the fixed header; Tab reaches it with a visible focus ring; GA DebugView shows `click_cta_process` once and no duplicate `cta_contact`
- **Lead-magnet strip (real end-to-end):** submit as "TEST Sprint3 Claude"; success state shows, checklist email arrives, Airtable row has `source = Lead Magnet`; GA shows `generate_lead` with label `lead_magnet`. Shai deletes the test row
- **Honeypot** filled on the strip: fake success, no network request
- **Header:** at 1280px over the hero, icons and nav are clearly readable; after scrolling it turns solid navy as before
- **320 / 390 / 768 / 1280px:** no horizontal scroll; the strip stacks cleanly on mobile
- **grep** on all pages: no `הנך מסכים`, no visible `052-2296269`; `styles.css?v=11` on all 7
- **Heading order** stays H1 → H2 → H3 after the move (strip uses H2, form title H3)

### Open Questions / Risks

- **Fewer checklist downloads** is expected (Decision 2). Judge Sprint 3 by consult requests over 4+ weeks, not by downloads.
- **Measurement baseline:** Sprint 0 GA Realtime confirmed 2026-10-03, so tracking works before this ships.
- **Low traffic:** with few visits per day, a before/after comparison will be noisy. Treat the result as a direction, not proof.
- **CLAUDE.md was stale** about `/en/` (the directory no longer exists). Fixed in the same PR.

**Flagged, not fixed (outside this sprint):**
- `</main>` is missing on all 6 main pages, so the footer sits inside the `main` landmark (screen readers announce it as main content). One line per page; Sprint 4 or the next shared-chrome edit.
- On the lead-magnet strip the consent checkbox comes after the submit button in tab order (same as the old layout). Submitting without it shows the error, so nothing breaks; worth swapping if conversion data shows drop-off.
