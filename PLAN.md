# ⚡ Mobile Form Alignment Fixes (PLAN.md)

## Objective

Address the alignment issues in the Hero form and Footer form when viewed on mobile devices (specifically the `tel` input alignment and the `checkbox` label text wrapping layout).

## CTO Reality Check

The screenshot perfectly reveals the issue:

1. **The Phone Input:** I added `md:text-right md:focus:text-left` previously. Because of the `md:` prefix, the `text-right` property was *only* applying to desktop screens (`md` and up), leaving the mobile view to inherit default browser LTR left-alignment.
2. **The Checkbox Line:** We grouped the text into a `flex flex-wrap` container to remove the gaps. However, on narrow mobile screens, wrapping text causes the flex items to behave unexpectedly based on the parent's alignment. We need to restructure this so the checkbox and the text act as a strict 2-column grid or flex row with `items-start`.

## Proposed Changes

### 1. Fix Phone Input Alignment (Mobile)

- **Target:** `index.html` (Hero Form & Footer Form)
- **Change:** Remove the `md:` breakpoint constraint from the alignment classes. Change it from `text-left md:text-right md:focus:text-left` directly to `text-right focus:text-left`. This forces the placeholder to the right side on *all* device sizes unconditionally.

### 2. Fix Checkbox Text Wrapping (Mobile)

- **Target:** `index.html` (Hero Form & Footer Form)
- **Change:** Refactor the checkbox layout to use an `items-start` flex approach. The checkbox acts as a fixed-width icon on the right, and the text (the label + button + span) wraps naturally as a single continuous paragraph (`<p>`) beside it, rather than individual flex items wrapping out of order.

## User Review Required
>
> [!IMPORTANT]
> The flex text wrapping on mobile is a common Tailwind RTL trap. Does this 2-step layout plan look approved to execute?
