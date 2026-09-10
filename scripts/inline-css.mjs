/**
 * Inlines public/styles.css into the Hebrew pages between the
 * <!-- inline-css:start --> / <!-- inline-css:end --> markers.
 *
 * Runs as part of `npm run build`, straight after Tailwind regenerates the
 * stylesheet, so the inlined copy can never drift from the compiled one.
 *
 * The stylesheet is ~7.7 KB gzipped. Inlining it removes a render-blocking
 * request whose cost on mobile is round-trip latency rather than bytes.
 * /en/ still links styles.css externally and is untouched.
 */
import { readFile, writeFile } from 'node:fs/promises';
import { fileURLToPath } from 'node:url';
import { dirname, join } from 'node:path';

const root = join(dirname(fileURLToPath(import.meta.url)), '..');
const cssPath = join(root, 'public', 'styles.css');

const PAGES = [
    'public/index.html',
    'public/services/ai-agents.html',
    'public/services/automations.html',
    'public/services/crm-systems.html',
    'public/services/landing-pages.html',
    'public/services/training.html',
];

const START = '<!-- inline-css:start -->';
const END = '<!-- inline-css:end -->';

const css = (await readFile(cssPath, 'utf8')).trim();
if (css.includes('</style')) {
    console.error('inline-css: stylesheet contains "</style" and cannot be inlined safely');
    process.exit(1);
}

let failed = false;
for (const rel of PAGES) {
    const file = join(root, rel);
    const html = await readFile(file, 'utf8');
    const a = html.indexOf(START);
    const b = html.indexOf(END);
    if (a === -1 || b === -1 || b < a) {
        console.error(`inline-css: markers missing in ${rel}`);
        failed = true;
        continue;
    }
    const block = `${START}\n    <style>${css}</style>\n    ${END}`;
    const next = html.slice(0, a) + block + html.slice(b + END.length);
    if (next !== html) await writeFile(file, next);
    console.log(`inline-css: ${rel} (${(Buffer.byteLength(css) / 1024).toFixed(1)} KB inlined)`);
}
process.exit(failed ? 1 : 0);
