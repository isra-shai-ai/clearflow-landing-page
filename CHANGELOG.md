# Changelog

All notable changes to the ClearFlow Landing Page project will be documented in this file.

## [1.1.0] - 2026-03-14 — Architecture Upgrade

### Changed

- **Performance:** Replaced the Tailwind CDN runtime with a pre-compiled, minified CSS bundle (~60x faster DOM load by eliminating client-side JIT compilation).
- **Project Structure:** Restructured the project to output into a `public/` directory, aligning with Vercel's standard static-site deployment expectations.
- **Build Tooling:** Added `npm run build` (minified production CSS) and `npm run dev` (watch mode) scripts to `package.json` with `tailwindcss` as the sole dev dependency.

---

## [Unreleased] MVP - V2 Polish

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
