# ClearFlow Landing Page

A high-conversion, professional landing page MVP for a B2B Business Automation agency in Israel named ClearFlow.

## Tech Stack

- HTML5
- Tailwind CSS (pre-compiled)

## Project Structure

```text
├── public/           # Static output directory (deployed to Vercel)
│   ├── index.html    # Landing page
│   └── styles.css    # Compiled Tailwind CSS (auto-generated)
├── input.css         # Tailwind source directives
├── tailwind.config.js
├── package.json
└── .gitignore
```

## Local Development

```bash
npm install
npm run dev        # Watch mode — auto-recompiles on changes
```

Open `public/index.html` in your browser to preview.

## Production Build

```bash
npm run build      # Compiles and minifies CSS into public/styles.css
```

## Deployment Notes (Vercel)

- **Build Command:** `npm run build`
- **Output Directory:** `public`
- Vercel will automatically install dependencies, run the build script, and serve the `public/` directory.
- The `vercel.json` file configures custom headers, specifically `X-Robots-Tag: noindex, nofollow` for hidden resources like the lead magnet checklist.

## Data Flow & Automations (Make.com)

All forms on the landing page (Hero, Footer, Lead Magnet) are wired to a single Make.com webhook:
`https://hook.eu1.make.com/p3evkp5wlspqvo3g1ln8qyxanf23h7as`

The universal JSON payload structure sent to Make is:
```json
{
  "fullName": "שם הליד",
  "phone": "0500000000",
  "email": "email@example.com",
  "source": "Hero | Footer | Lead Magnet"
}
```

*Note: Make sure your Airtable module maps fields to `fullName`, `phone`, `email`, and `source`.*

## Brand Assets for Automations

The primary ClearFlow logo is hosted directly in the public folder (`public/logo.svg`).
Once deployed to Vercel, it is accessible at:
`https://[YOUR-VERCEL-DOMAIN]/logo.svg`
*(Use this URL in your Make.com scenario when sending HTML emails to leads).*

## Secret Resources

To support lead magnets, standalone HTML guides are stored in `public/resources/` (e.g., `automation-checklist.html`). The local `vercel.json` file ensures these paths are hidden from search engine indexing to protect gated content.
