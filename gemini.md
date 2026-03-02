# Project Goal

Build a high-conversion, professional landing page MVP for a B2B Business Automation agency in Israel named ClearFlow. Output a single `index.html` file using HTML5 and Tailwind CSS (via CDN).

# Vibe & UI/UX Guidelines

- **Aesthetic:** Modern, premium B2B SaaS. Clean, authoritative, and minimalist.
- **Rule:** DO NOT use small "pill" tags above H2s. Rely on typography and spacing.
- **Rule:** DO NOT use cheap, colorful clipart. If icons are needed, use ONLY premium, minimalist, thin-stroke (stroke-width: 1.5) monochrome SVGs.
- **Backgrounds:** Deep Blue (`#1E3A5F`) and Slate (`#4A6FA5`) mesh gradients with glassmorphism (`backdrop-blur-xl`, `bg-white/80`).
- **Direction & Typography:** RTL layout (`dir="rtl" lang="he"`). Google Fonts: 'Rubik' or 'Heebo'.

# Accessibility (A11y) & Legal Infrastructure

- **Tabnav Widget:** Inject this exact script into the `<head>`:
  `<script src="https://widget.tabnav.com/limited-widget.min.js.gz" tnv-data-config='{"language":"he","color":"#405ec3","buttonColor":"#405ec3","buttonSize":"small","widgetSize":"small","widgetLocation":"right","buttonLocation":"bottom"}' defer></script>`
  `<noscript> פתרונות נגישות לאתרי אינטרנט לפי התקן הישראלי 5568<a href="https://tabnav.com/he">הנגשת אתרים</a> </noscript>`
- **Cookie Banner:** A sleek, fixed banner at the bottom. **CRITICAL:** Use CSS (`flex-nowrap`) to force a single line on desktop. Text must use this exact phrasing to avoid hanging letters: "אנו משתמשים בעוגיות (Cookies) כדי להעניק לך את החוויה הטובה ביותר. בהמשך הגלישה, הנך מסכים/ה לשימוש בהן. לקריאה נוספת: [מדיניות הפרטיות] שלנו." (Make bracketed text the button).
- **Legal Modals:** `<dialog>` modals with working "X" close buttons. Use this exact compliant Israeli text:

  - **מדיניות פרטיות:** "**מדיניות פרטיות - ClearFlow**<br>
    חברת ClearFlow ('אנחנו', 'אותנו' או 'שלנו') מכבדת את פרטיותך ומחויבת להגנה על מידע אישי שאתה משתף איתנו. מדיניות זו מסבירה כיצד אנו אוספים ומשתמשים במידע.<br><br>
    **1. המידע שאנו אוספים:** אנו עשויים לאסוף שם מלא, כתובת דוא״ל, מספר טלפון, ומידע על השימוש באתר הנאסף אוטומטית באמצעות עוגיות (Cookies).<br>
    **2. מטרות השימוש במידע:** מתן שירותים, יצירת קשר, תמיכה, ושליחת חומרים שיווקיים (בכפוף להסכמתך).<br>
    **3. שיתוף מידע:** אנו לא נמכור או נשכיר מידע אישי לצדדים שלישיים. מידע עשוי להיות מועבר לספקי שירותים חיצוניים לצורך תפעול האתר בלבד, או לרשויות החוק אם נדרש.<br>
    **4. אבטחת מידע:** אנו נוקטים באמצעי אבטחה מתקדמים להגנה על המידע האישי.<br>
    **5. זכויות המשתמש:** יש לך זכות לעיין במידע, לבקש את תיקונו או מחיקתו.<br>
    **6. יצירת קשר:** לשאלות, ניתן לפנות אלינו בטלפון [הכנס טלפון] או בדוא״ל [הכנס אימייל]."

  - **הצהרת נגישות:** "**הצהרת נגישות - ClearFlow**<br>
    אנו ב-ClearFlow מייחסים חשיבות עליונה להנגשת אתר האינטרנט שלנו. אתר זה הונגש בהתאם להמלצות התקן הישראלי (ת״י 5568) לנגישות תכנים באינטרנט ברמת AA, וכן עומד בהנחיות WCAG 2.0.<br><br>
    **פירוט התאמות:** האתר כולל תמיכה בניווט מקלדת, התאמה לקוראי מסך, ואפשרות להגדלת גופנים ושינוי ניגודיות באמצעות תוסף הנגישות (Tabnav) המותקן באתר.<br>
    **סייגים:** למרות מאמצינו להנגיש את כלל דפי האתר, ייתכן ויתגלו חלקים שטרם הונגשו במלואם.<br>
    **פרטי רכז נגישות:** במידה ונתקלתם בבעיית נגישות, נשמח לקבל משוב ולתקן זאת בהקדם. <br>
    שם הרכז: שי ישראל<br>
    טלפון: [הכנס טלפון]<br>
    דוא״ל: [הכנס אימייל]"

# Page Structure & Exact Hebrew Content

## Global Elements

- **Top Navigation Bar:** Transparent transitioning to solid dark blue (`bg-[#11223A]`) on scroll. Text `text-white`. 3-part flex layout. The phone number MUST be a high-contrast pill (`bg-amber-500 text-white`).
- **Sticky WhatsApp:** Locked to bottom-left. **CRITICAL:** Use a completely new, perfectly symmetrical SVG path for the WhatsApp icon and center it flawlessly using `flex items-center justify-center`.

## Section 1: Hero (Dark Enterprise Theme)

- **Background:** Rich, dark blue gradient (`bg-gradient-to-b from-[#11223A] to-primary`).
- **H1:** אוטומציה עסקית שעושה סדר. *(Text white. Apply an amber gradient to "עושה סדר").*
- **Subtitle:** פחות עבודה ידנית, יותר שליטה. אנחנו חוסכים לכם שעות, מונעים מלידים ליפול, ומחזירים לכם את השליטה המלאה על התפעול. (`text-blue-100`).
- **Inline Hero Form:**
  - **Wrapper:** Premium glass effect (`bg-white/10 backdrop-blur-md border border-white/20`), heavily rounded.
  - **Title:** `text-4xl` or `text-5xl` white text ABOVE the inputs: "לקביעת שיחת ייעוץ ללא עלות".
  - **Inputs Layout:** Single horizontal row. Submit button text: "שליחה".
  - **JS Logic:** Form submits locally (hides inputs, shows inline "תודה!" message).

## Section 2: The Pain vs. The Solution

- **H2:** העסק צומח, אבל התפעול תוקע אתכם מאחור?
- **Comparison Layout:** Side-by-side boxes.
  - **Box 1 (The Problem - Red 'X' marks):** - לידים חמים נופלים בין הכיסאות. | עובדים שורפים שעות על העתק-הדבק. | תהליכי קליטת לקוחות מסורבלים ואיטיים.
  - **Box 2 (The Solution - Green 'Check' marks):** - מעקב אוטומטי אחר כל פנייה וליד. | סנכרון נתונים שקוף בין כל המערכות. | תהליכי Onboarding מהירים ואוטומטיים.

## Section 3: Our Services (Premium Redesign)

- **Anchor:** `id="services"`
- **H2:** השירותים שלנו
- **Design Rules:** Clean 2x2 grid. To fix the "dull" look, cards must have a soft background tint (e.g., `bg-slate-50`), a thick accent border on the right, and a smooth hover lift. **NEW:** Add a premium, thin-stroke (Lucide style) monochrome SVG icon to the top-right of each card in the primary brand color to act as a visual anchor.
  - **Card 1: דפי נחיתה** - עיצוב ובניית דפי נחיתה מהירים ומתקדמים, שבנויים פסיכולוגית וטכנית להמיר גולשים ללקוחות. *(Icon idea: Browser window or Layout)*
  - **Card 2: אוטומציות** - חיבור חכם בין כל המערכות שלכם (Make/Zapier) כדי למנוע פעולות כפולות ולחסוך שעות של עבודה ידנית. *(Icon idea: Lightning bolt or Workflow nodes)*
  - **Card 3: מערכות CRM** - אפיון, הקמה והטמעה של מערכות ניהול לקוחות (CRM) שמותאמות בדיוק למידות של העסק שלכם. *(Icon idea: Users or Database)*
  - **Card 4: הדרכה והטמעה** - אנחנו לא משאירים אתכם באוויר. העברת מקל מסודרת והדרכה מקיפה לצוות כדי שתנהלו את המערכת בעצמאות. *(Icon idea: Graduation cap or Presentation board)*

## Section 4: The Process (3-Step Grid)

- **H2:** מתהליך מסורבל למכונה משומנת ב-3 שלבים:
- *(Keep existing 3 steps exactly the same)*

## Section 5: FAQ

- *(Keep existing 5 questions exactly the same)*

## Section 6: Footer / Full Contact Form

- **H2:** מוכנים להתחיל לחסוך בזמן?
- **Subtitle:** השאירו פרטים לשיחת מיפוי קצרה (ללא עלות), בה נזהה איפה הכסף והזמן שלכם בורחים. Button: "בואו נדבר תכל'ס". (JS success state implemented).
- **Minimalist Bottom Footer:** `border-t border-slate-700`, `flex justify-between`. Text `text-slate-300`. Copyright flush right. Links (פרטיות, הצהרת נגישות, עוגיות) flush left.
