# Changelog

All notable changes to the ClearFlow Landing Page project will be documented in this file.

## [1.1.0] - 2026-03-14 — Architecture Upgrade

### Changed

- **Performance:** Replaced the Tailwind CDN runtime with a pre-compiled, minified CSS bundle (~60x faster DOM load by eliminating client-side JIT compilation).
- **Project Structure:** Restructured the project to output into a `public/` directory, aligning with Vercel's standard static-site deployment expectations.
- **Build Tooling:** Added `npm run build` (minified production CSS) and `npm run dev` (watch mode) scripts to `package.json` with `tailwindcss` as the sole dev dependency.

---

## [Unreleased] MVP - V2 Polish

### Added
- **SEO:** Added `<link rel="canonical">` to all 11 pages, plus reciprocal `hreflang` (`he` / `en` / `x-default`) linking the Hebrew and English homepages and the 4 paired service articles. `ai-agents.html` is canonical-only — it has no English counterpart.
- **Social:** Created `public/og-image.jpg` (1200x630, brand gradient + logo + amber rule). The URL had been referenced 33 times across the site while returning HTTP 404, so every WhatsApp/LinkedIn/Twitter share rendered without an image.
- **AI Agents Service:** Created a new dedicated service page (`ai-agents.html`) focusing on autonomous digital workers, complete with custom 3D abstract illustrations.
- **Navigation:** Added the "AI Agents" service to the global dropdown menu across all pages.

### Fixed
- **Social:** `og:url` and `twitter:url` were hardcoded to the homepage (`https://clearflow.co.il/`) on all 11 pages, so sharing any service article rendered the homepage identity. Both now match each page's canonical.

### Changed
- **Homepage Layout:** Redesigned the "Our Services" grid into a "1 + 4 Hero Layout". The new AI Agents card spans the full top width to serve as an anchor, while the legacy 4 services sit symmetrically beneath it.
- **Copywriting:** Rewrote all service cards on the homepage to be strictly outcome-led (e.g. "Digital infrastructure that converts" instead of "Landing Pages").
- **Typography:** Updated sub-headline text constraints on service pages, introducing `text-balance` and wider max-widths to prevent typographical orphans while maintaining readability.
- **UX Consistency:** Changed all card CTAs from "Read More" to the gender-neutral, professional "לפרטים נוספים".
- **Asset Pipeline:** Re-compiled the Tailwind `styles.css` and injected cache-busting `?v=2` query strings to ensure returning visitors fetch the newly structured grid CSS.

### Changed

- **Performance:** Deferred Google Analytics and preloaded Google Fonts to improve mobile LCP and unblock the main rendering thread.
- **UI:** Rebuilt the "Our Services" bento-box cards with premium hover effects, an accent border tint, and dynamic Lucide SVG icons.
- **UI/RTL:** Refactored form inputs to unconditionally force `text-right` alignment for the "טלפון" placeholder on all mobile breakpoints.
- **UI/RTL:** Rebuilt the privacy policy checkbox wrappers into an `items-start` flex row, preventing text wrapping fragmentation on narrow screens.
- **UX:** Converted the header phone number pill into a clickable `<a href="tel:...">` anchor for immediate mobile dialing.

### Fixed

- **Accessibility (WCAG 2.1 AA):** Injected proper `aria-label`s on all forms, added a "דלג לתוכן המרכזי" (Skip to main content) anchor, and masked all decorative SVGs from screen readers via `aria-hidden="true"`.
- **Accessibility:** Resolved a hidden grammatical typo ("הא באתר" -> "האתר") inside the Legal Accessibility Modal payload.
- **Accessibility:** Removed `role="button"` from the `בית` (Home) navigation anchor and mapped it correctly to `#main-content`.
- **Production Readiness:** Completely purged the `submitToWebhook` function of native browser `alert()` popups and `console.error` logs, replacing them with graceful, inline HTML error messages that clear on input.
- **Form Layout:** Removed redundant visible label tags from the footer contact form, relying wholly on minimalist placeholders to match the Hero form aesthetic.
