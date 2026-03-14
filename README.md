# ClearFlow Landing Page

A high-conversion, professional landing page MVP for a B2B Business Automation agency in Israel named ClearFlow.

## Tech Stack

- HTML5
- Tailwind CSS (via CDN)

## Deployment Notes (Vercel)

**Important considerations for deploying to Vercel:**

- Vercel automatically detects the `package.json` and will run the `build` script (`npm run build`) to compile the Tailwind CSS file (`styles.css`) before deploying the static site. Ensure this script is present.
- Previous issues with `axe-core` breaking Vercel builds due to missing Chrome Headless environment dependencies have been resolved by moving to Playwright tests running locally, leaving `package.json` with only the `tailwindcss` dependency and build script.
