# ClearFlow — Infrastructure & Accounts

## Domain
- **Registrar:** Box.co.il (domains.box.co.il)
- **Domain:** clearflow.co.il
- **Nameservers:** ns1.vercel-dns.com / ns2.vercel-dns.com (DNS is managed in Vercel, not Box)

## Hosting & Deployment
- **Platform:** Vercel
- **Deploy trigger:** Push to `main` branch → auto-deploys
- **www redirect:** Vercel 301 redirect from apex (clearflow.co.il) → www.clearflow.co.il
- **All canonical URLs use www**

## DNS (managed in Vercel)
- To add/edit DNS records: vercel.com → ClearFlow project → Domains → clearflow.co.il → DNS Records
- Records to be aware of: A/CNAME pointing to Vercel, Google Search Console TXT verification record

## Build
- `npm run build` — compiles Tailwind CSS → public/styles.css (must run before committing CSS changes)
- `npm run dev` — watch mode (unminified output — do NOT commit without rebuilding)
- Deployed files are in `public/`

## Analytics
- **Platform:** Google Analytics 4
- **Property ID:** G-BXPWS2RHVV
- GA loads on first user interaction (scroll/click/move) with 7-second fallback — intentional for Lighthouse performance

## Forms & Automation
- **Contact form → Make.com → Airtable**
- Make.com OAuth may need periodic reauthorization if the flow goes inactive
- Test by submitting a real lead and confirming it appears in Airtable

## SEO / Search Console
- **Google Search Console:** Domain property for clearflow.co.il
- **Verification method:** DNS TXT record (added in Vercel DNS)
- **Sitemap:** https://www.clearflow.co.il/sitemap.xml — submit in GSC after verifying

## Pages
- 6 Hebrew pages (index + 5 services) — actively maintained
- /en/ pages removed (2026-09-11) — can be rebuilt if English market becomes a priority

## Key files
| File | Purpose |
|------|---------|
| `public/index.html` | Homepage |
| `public/services/*.html` | Service pages (5 pages) |
| `public/styles.css` | Compiled Tailwind (do not edit directly) |
| `input.css` | Tailwind source — edit this |
| `tailwind.config.js` | Tailwind config |
| `public/sitemap.xml` | XML sitemap for search engines |
| `public/robots.txt` | Crawler directives |
| `PLAN.md` | Project plan (completed) |
| `INFRA.md` | This file |
| `vercel.json` | Vercel config — sends `noindex, nofollow` header for the gated checklist page |
| `public/resources/automation-checklist.html` | Lead magnet page (gated, noindex) |
| `public/research/` | Internal reference markdown files — robots.txt blocks crawlers but files are publicly accessible via direct URL; move out of `public/` if they should be private |
