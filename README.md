# ClearFlow Landing Page

A high-conversion, professional landing page MVP for a B2B Business Automation agency in Israel named ClearFlow.

## Tech Stack

- HTML5
- Tailwind CSS (via CDN)

## Deployment Notes (Vercel)

**Important considerations for deploying to Vercel:**

- The `package.json` file was explicitly removed from this repository.
- **Why?** Vercel attempts to install dependencies and run build scripts if it detects a `package.json`. In our case, `axe-core` in the `test:ally` script caused the Vercel build to fail because Vercel instances do not have a full Chrome Headless environment installed out-of-the-box (resulting in an exit code 127).
- By removing `package.json`, Vercel recognizes this as a static site and will deploy the `index.html` file seamlessly without trying to execute npm commands.
