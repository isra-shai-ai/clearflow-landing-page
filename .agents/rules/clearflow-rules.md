---
trigger: always_on
---

# ClearFlow MVP - Project Context

**Goal:** An Israeli B2B automation MVP landing page. High-converting, trustworthy, and fast.

## Tech Stack & Coding Standards

- **Core:** HTML5, utility-first CSS via Tailwind.
- **Language/Direction:** Native support for Hebrew. All text must flow Right-to-Left (RTL) using `dir="rtl"`.
- **Styling Aesthetics:** Modern UI patterns, glassmorphism, soft shadows, ample whitespace. Move away from casual "Tachles" to a premium, professional B2B tone.

## Accessibility (Mandatory Gate)

You must act as a strict WCAG Accessibility Auditor. Before finalizing any UI code, you must internally simulate an `axe-core` audit:

- Check for missing ARIA labels (especially on SVGs/forms)
- Ensure proper structural nesting (H1 -> H2 -> H3)
- Verify `lang` and `dir` tags are present
- Verify sufficient color contrast
If you detect violations, you must flag them and request my approval before delivering the final code.
