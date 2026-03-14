# ClearFlow Landing Page

A high-conversion, professional landing page MVP for a B2B Business Automation agency in Israel named ClearFlow.

## Tech Stack

- HTML5
- Tailwind CSS (pre-compiled)

## Project Structure

```
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
- The only devDependency is `tailwindcss` — no heavy testing frameworks that could break CI.
