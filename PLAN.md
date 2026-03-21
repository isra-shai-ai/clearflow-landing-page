# Project Plan: The Secret Checklist Webpage

## Goal
Transform the existing A4 print-optimized `guide.html` into a fully responsive, mobile-first "Secret Webpage" (`public/checklist.html`) that delivers maximum user experience across all devices and drives immediate WhatsApp conversions.

## Architecture

This will be a static HTML file served by Vercel directly from the `public/` directory, sharing the pre-compiled `styles.css` of the main landing page to ensure styling consistency and blistering fast load times.

## Step-by-Step Changes

### 1. `tailwind.config.js`
- **[MODIFY]** Update the `content` array to scan `public/checklist.html` so that any Tailwind utilities used in the guide are correctly bundled into `styles.css`.

### 2. `public/checklist.html`
- **[NEW]** Create this file by duplicating `guide.html`.
- **Modifications:**
    - **SEO Blocking:** Inject `<meta name="robots" content="noindex, nofollow">` to hide the page from search engines.
    - **Remove Print Styling:** Strip out all `@page`, `.a4-page`, `210mm` width, and page-break CSS.
    - **Make Responsive:** Wrap the body content in a standard `div class="container mx-auto max-w-3xl px-6 py-12"`. This will convert the rigid A4 layout into a fluid, mobile-stacking article format perfect for phones and desktop.
    - **Link Stylesheet:** Remove the Tailwind CDN script from the `<head>` and link directly to `<link rel="stylesheet" href="styles.css">`.
    - **WhatsApp CTA:** Update the bottom CTA link to use the exact pre-filled WhatsApp link: `https://wa.me/972522296269?text=...` ensuring the entire CTA section uses highly visible, rounded buttons perfect for thumb-tapping.

### 3. Build & Verification
- Run `npm run build` to re-compile `public/styles.css` with the new classes extracted from `checklist.html`.
- Verify the responsive fluid layout on mobile widths.

## Verification Required
- You will need to confirm the WhatsApp number `972522296269` currently hardcoded in the guide is correct.

**Reply "The plan is approved" to begin execution.**
