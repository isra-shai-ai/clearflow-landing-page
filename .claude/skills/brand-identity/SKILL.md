---
name: brand-identity
description: Use when building or editing any user-facing ClearFlow asset — UI components, page sections, styling, Hebrew copy, CTAs, icons, forms — or when picking a color, font, radius, card style, or wording and the correct value is not already visible in the file being edited. Also use before reviewing UI or copy for brand consistency.
---

# Brand Identity & Guidelines — ClearFlow

**Brand Name:** ClearFlow (קלירפלו)
**Market:** B2B Business Automation Agency, Israeli market
**Language & Direction:** Hebrew, RTL (`dir="rtl" lang="he"`)

This skill defines the core constraints for visual design, technical implementation, and copywriting for ClearFlow. Adhere to these guidelines strictly.

## Reference Documentation

Consult the specific resource file based on your task. Do not guess brand elements.

### For Visual Design & UI Styling
Exact colors, fonts, border radii, spacing, and glassmorphism values:
👉 **[`resources/design-tokens.json`](resources/design-tokens.json)**

### For Coding & Component Implementation
Durable implementation rules and forbidden patterns:
👉 **[`resources/tech-stack.md`](resources/tech-stack.md)**

### For Copywriting & Content Generation
Hebrew voice, tone, persona, and terminology rules:
👉 **[`resources/voice-tone.md`](resources/voice-tone.md)**

## Scope Boundary

This skill covers **durable brand decisions only** — things that stay true across refactors.

Build setup, file layout, commands, deploy config, and the form pipeline are **not** here. They live in `CLAUDE.md` (project root) and `package.json`. Read those for anything mechanical; do not re-document them in this skill.
