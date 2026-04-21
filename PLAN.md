# Feature Implementation Plan - Phase 2: Robust Hebrew Content

**Overall Progress:** `15%`

## TLDR

Pivoting focus away from the English localization (placed on hold) to deeply enrich the 4 Hebrew service pages. We are implementing a centralized Services dropdown menu in the global navigation, enhancing the articles with real-world examples, adding contextual CTAs at the bottom of articles, and performing a rigorous accessibility audit. All changes will be reviewed locally before any production deployment.

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

- [ ] 🟨 **Step 2: Implement Navigation Dropdown (Global)**
  - [ ] 🟥 Update `public/index.html` and `public/services/*.html` headers to include an accessible dropdown menu for "שירותים".
  - [ ] 🟥 Ensure `aria-expanded`, tabindex, and keyboard navigability are correctly implemented.

- [ ] 🟥 **Step 3: Restructure Service Page HTML**
  - [ ] 🟥 Update the HTML layout templates to support deeper content (Problem/Solution/Example/ROI framework).
  - [ ] 🟥 Add contextual CTA block at the bottom of the article.

- [ ] 🟥 **Step 4: Write & Inject Landing Pages Copy**
  - [ ] 🟥 Write full Hebrew copy based on the approved strategy and inject it.

- [ ] 🟥 **Step 5: Write & Inject Automations Copy**
  - [ ] 🟥 Write full Hebrew copy based on the approved strategy and inject it.

- [ ] 🟥 **Step 6: Write & Inject CRM Copy**
  - [ ] 🟥 Write full Hebrew copy based on the approved strategy and inject it.

- [ ] 🟥 **Step 7: Write & Inject Training Copy**
  - [ ] 🟥 Write full Hebrew copy based on the approved strategy and inject it.
  
- [ ] 🟥 **Step 8: Final Polish & Accessibility (A11y) Audit**
  - [ ] 🟥 Ensure responsive design holds up with the expanded text.
  - [ ] 🟥 **Mandatory Step**: Run an accessibility audit checking for keyboard focus trapping, ARIA labels, and contrast ratios.
  - [ ] 🟥 Verify `input.css` compilation cleanly handles any new native Tailwind classes.
