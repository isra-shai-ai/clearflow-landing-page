# Project Goal

Build a high-conversion, professional landing page MVP for a B2B Business Automation agency in Israel named ClearFlow. Output a single `index.html` file using HTML5 and Tailwind CSS (via CDN).

# Vibe & UI/UX Guidelines (Version 2 - Premium SaaS)

- **Aesthetic:** Modern, premium B2B SaaS. We are moving away from flat/rigid layouts.
- **Backgrounds:** Use a modern "mesh gradient" effect. Create large, brightly colored blur blobs (`blur-[100px]`, `opacity-30`) in Deep Blue (`#1E3A5F`) and Slate (`#4A6FA5`) behind the main content to create depth.
- **Glassmorphism:** Use `bg-white/80` (or similar) combined with `backdrop-blur-xl` on the header, hero form, and cards so they look like frosted glass floating over the background gradients.
- **Components:** Extreme rounded corners (`rounded-3xl`), ultra-soft, large, low-opacity drop shadows, and delicate 1px borders (`border-white/50`).
- **Direction & Typography:** RTL layout (`dir="rtl" lang="he"`). Google Fonts: 'Rubik' or 'Heebo'.

# Accessibility (A11y) Infrastructure (CRITICAL)

- Semantic HTML5 (`<header>`, `<main>`, `<section>`, `<footer>`).
- Strict heading hierarchy (One `<h1>`, followed by `<h2>`, then `<h3>`).
- `aria-label` on all inputs, buttons, and links.

# Page Structure & Exact Hebrew Content

## Global Elements

- **Top Navigation Bar:** Right side: ClearFlow logo. Left side: Solid pill button with phone number (052-1234567) and a WhatsApp icon. (Leave links as `href="#"` for now).
- **Sticky WhatsApp:** A floating, circular green WhatsApp icon locked to the bottom-left corner (`href="#"`).
- **Legal Modals:** Create two hidden modals (use HTML `<dialog>` or fixed overlays) for "מדיניות פרטיות" (Privacy Policy) and "הצהרת נגישות" (Accessibility Statement). Leave placeholder text inside them for now. Ensure they have a clear "X" button to close.
- **Accessibility Widget (Tabnav):** Inject this exact script into the code:
  `<script src="https://widget.tabnav.com/limited-widget.min.js.gz" tnv-data-config='{"language":"he","color":"#405ec3","buttonColor":"#405ec3","buttonSize":"small","widgetSize":"small","widgetLocation":"right","buttonLocation":"bottom"}' defer></script>`
  `<noscript> פתרונות נגישות לאתרי אינטרנט לפי התקן הישראלי 5568<a href="https://tabnav.com/he">הנגשת אתרים</a> </noscript>`

## Section 1: Hero (Above the Fold)

- **H1:** אוטומציה עסקית שעושה סדר בבלאגן. פחות עבודה סיזיפית, יותר שליטה. *(Apply a vibrant accent gradient to the words "עושה סדר" to make them pop).*
- **Subtitle:** מערכות מתקדמות (כמו CRM ו-Make) הן רק כלים. אנחנו מחברים אותן כדי למנוע מלידים ליפול בין הכיסאות, לחסוך עשרות שעות בחודש, ולהחזיר לכם את השליטה המלאה על תפעול העסק.
- **Hero Form:** A compact, inline lead capture form (שם מלא, אימייל, טלפון). Dummy submit (`action="#"`).
  - **Checkbox (Mandatory):** Add a required checkbox above the submit button with this text: "הנני מאשר/ת בזאת כי עם מילוי הפרטים ושליחתם אני מסכים/ה לקבל שיחות שיווקיות, הודעות פרסום ב-SMS ו/או במייל גם אם מספר הטלפון שלי רשום במאגר "אל תתקשרו אליי" של הרשות להגנת הצרכן."
  - **Submit Button:** "קבעו שיחת אפיון חינם"
  - **Micro-copy (under button):** *הפרטים שלכם בטוחים איתנו. ללא ספאם.*

## Section 1.5: Social Proof (Trust Building)

- Add a subtle, greyscale ticker/row of client logos (or standard placeholders) right below the Hero section to build immediate trust.

## Section 2: Trust Banner & Pain Points

- **Trust Banner:** 3 minimal, icon-driven stats bridging the Hero and Pain sections.
  - "מקסימום" / סדר ארגוני וחיסכון בזמן
  - "100%" / שליטה וסגירת עסקאות
  - "מינימום" / טעויות אנוש והזנת נתונים
- **H2:** העסק צומח, אבל התפעול תוקע אתכם מאחור?
- **Pain Points:** - לידים חמים נופלים בין הכיסאות כי אין מעקב מסודר.
  - עובדים שורפים שעות יקרות על העתק-הדבק והעברת מידע ידנית.
  - תהליכי קליטת לקוחות (Onboarding) מסורבלים שלוקחים ימים במקום דקות.
- **Agitation & Solution Statement:** כל יום שעובר ככה, אתם מפסידים לקוחות למתחרים ושורפים כסף על זמן עבודה מבוזבז. זה לא חייב להיות ככה.

## Section 3: Core Services (Bento-Box Layout)

- **H2:** מתהליך מסורבל למכונה משומנת ב-3 שלבים:
- **Design:** Build this as a dynamic, modern "bento-box" grid rather than 3 identical columns.
- **Step 1:** מיפוי חסר פשרות (לא מתחילים לבנות לפני שמבינים. שיחת עומק אסטרטגית שבה מפרקים את צווארי הבקבוק, מזהים איפה הכסף בורח, ובונים תוכנית פעולה תכל'ס.)
- **Step 2:** ארכיטקטורה ואוטומציה (בניית תהליכים אוטומטיים שקופים ואמינים. קליטת לידים ישירות ל-CRM, הפקת חשבוניות אוטומטית, וסנכרון מלא בין כל מחלקות העסק.)
- **Step 3:** הדרכה, שקיפות והעברת מקל (אנחנו לא משאירים אתכם עם קופסה שחורה. בסיום ההטמעה, הצוות שלכם מקבל הדרכה מקיפה וליווי צמוד כדי שהם ינהלו את המערכת בעצמאות ובביטחון מלא.)

## Section 4: FAQ (Handling Objections)

- **H2:** שאלות נפוצות
- **UI Component:** Interactive Accordion style (click a question to expand/collapse the answer). Use `<details>` and `<summary>` tags or JS with smooth CSS transitions for the opening and closing animation.
- **Q1:** האם צריך ידע טכני כדי להשתמש במערכת?
  - **A:** ממש לא. אנחנו בונים את המערכת כך שתהיה פשוטה ואינטואיטיבית, ודואגים להדריך את הצוות שלכם עד שהם שולטים בה לחלוטין.
- **Q2:** כמה זמן לוקח תהליך ההטמעה?
  - **A:** משתנה בהתאם למורכבות, אבל לרוב מדובר בתהליך ממוקד ומהיר שמתחיל לייצר תוצאות וחיסכון בזמן כבר בשבועות הראשונים.

## Section 5: Footer / Full Contact Form

- **H2:** מוכנים להפסיק לבזבז זמן?
- **Subtitle:** השאירו פרטים לשיחת מיפוי קצרה (ללא עלות), בה נזהה איפה הכסף והזמן שלכם בורחים.
- **Form:** Full-size safety net form: שם מלא, אימייל, טלפון.
  - **Checkbox (Mandatory):** Add a required checkbox above the submit button with this text: "הנני מאשר/ת בזאת כי עם מילוי הפרטים ושליחתם אני מסכים/ה לקבל שיחות שיווקיות, הודעות פרסום ב-SMS ו/או במייל גם אם מספר הטלפון שלי רשום במאגר "אל תתקשרו אליי" של הרשות להגנת הצרכן."
  - **Submit Button:** "בואו נדבר תכל'ס"
- **Footer Links:** At the very bottom of the page, add simple text links for "מדיניות פרטיות" and "הצהרת נגישות" that trigger their respective modals when clicked. Add a copyright line: "© 2026 ClearFlow. כל הזכויות שמורות."
