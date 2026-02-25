# Project Goal

Build a high-conversion, professional landing page for a B2B Business Automation agency in Israel named ClearFlow. The goal is to have a simple, reliable page potential clients can visit to understand the service. Output a single `index.html` file using HTML5 and Tailwind CSS (via CDN).

# Vibe & UI/UX Guidelines

- DO NOT use dark "cyberpunk", "matrix", "hacker", or "global corporate" aesthetics.
- DO USE a clean, bright, trustworthy, and practical B2B operational design. Use plenty of whitespace, light gray/off-white backgrounds, and a strong, stable primary color (like Deep Blue or Slate).
- Direction & Typography: RTL (Right-to-Left) layout `<html dir="rtl" lang="he">`. Import and use Google Fonts: 'Heebo' or 'Rubik'.
- Mobile-First: Ensure the layout is fully responsive. Use clean, subtle shadows and rounded corners.

# Accessibility (A11y) Infrastructure (CRITICAL)

The underlying code must be perfectly structured to support a third-party accessibility overlay plugin later:

- Use strict semantic HTML5 (`<header>`, `<main>`, `<section>`, `<footer>`).
- Maintain strict heading hierarchy (Exactly one `<h1>`, followed by `<h2>`, then `<h3>`). Do not skip heading levels.
- Add `aria-label` to any buttons, links, or form elements.
- Ensure high color contrast between text and background.

# Page Structure & Exact Hebrew Content

## Section 1: Header & Hero

- Logo Text: ClearFlow
- H1: אוטומציה עסקית שעושה סדר. בלי באזוורדס, רק תכל'ס.
- Subtitle: מערכות שעובדות בשבילך. אנחנו מחברים את המערכות שלכם כדי לחסוך זמן, למנוע טעויות אנוש, ולתת לכם בחזרה את השליטה על התפעול של העסק.
- CTA Button: בואו נעשה סדר

## Section 2: The Pain / Problem

- H2: הופכים כאוס לבהירות: העסק צומח, אבל התפעול תוקע אתכם?
- List of pain points (Use clean bullet points/icons):
  - לידים נופלים בין הכיסאות כי שוכחים לחזור אליהם.
  - העברת מידע בין מחלקות נעשית ידנית (וכוללת טעויות).
  - קליטת לקוח חדש או עובד לוקחת שעות של ניירת.
- Closing statement: זה לא חייב להיות ככה. כשהמערכות מדברות אחת עם השנייה – דברים פשוט קורים.

## Section 3: Core Services & Process

Design this as a logical 3-step process (e.g., Timeline or 3 clean connected cards). Highlight the third card visually.

- H2: מתהליך מסורבל לזרימה חלקה ב-3 שלבים:
- Card 1:
  - H3: 1. מיפוי, אפיון וסדר בבלאגן
  - Text: שיחת עומק שבה מפרקים את תהליכי העבודה הקיימים, מזהים איפה מבזבזים זמן, ובונים תוכנית פעולה מציאותית.
  - Highlight: המסר: לא מתחילים לבנות כלום לפני שמבינים את הצורך.
- Card 2:
  - H3: 2. בניית אוטומציות וחיבור מערכות
  - Text: בניית תהליכים אוטומטיים במערכות (כמו Make). קליטת לידים ל-CRM, הפקת חשבוניות, ותהליכי Onboarding מסודרים.
  - Highlight: המסר: המערכות עובדות כדי שאתם לא תעשו עבודה שחורה פעמיים.
- Card 3:
  - H3: 3. הדרכה והעברת מקל
  - Text: לאחר ההטמעה, העברת הדרכה מסודרת לצוות על תפעול המערכת ביום-יום. ליווי קרוב בחודש הראשון.
  - Highlight: המסר: לא משאירים אתכם עם "קופסה שחורה". נותנים לכם את השליטה.

## Section 4: Footer / Contact

- H2: מוכנים להפסיק לבזבז זמן?
- Form: Clean, simple inputs for: שם מלא (Full Name), אימייל (Email), טלפון (Phone).
- Submit Button: שלח הודעה
