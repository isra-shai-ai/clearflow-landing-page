---
description: Main copywriting workflow — handles all channels (landing page, email, social, ads, blog/SEO, WhatsApp/SMS) with a structured 4-phase process (Brief → Strategy → Draft → Visual).
---

# /copy — ClearFlow Copywriting Workflow

> **Pre-requisite**: Read `.agents/skills/clearflow-copy-skill` before starting. It contains all brand context, voice rules, tone guidelines, and the visual identity spec.

---

## Step 0: Channel Selection

Present the following menu to the user:

```
🎯 מה נכתוב היום?

1. 🖥️ לנדינג פייג׳ / Web Copy
2. 📧 אימייל (סיקוונס / ניוזלטר)
3. 📱 סושיאל (LinkedIn / Facebook / Instagram / X)
4. 📣 מודעות (Google Ads / Meta Ads)
5. 📝 בלוג / מאמר SEO
6. 💬 WhatsApp / SMS

בחרו מספר, או תארו מה אתם צריכים:
```

Wait for user selection before proceeding.

---

## Phase 1: Brief (📋 איסוף מידע)

Ask **channel-specific** questions. Use the base questions below + the channel-specific additions.

### Base Questions (all channels)

1. מה המטרה? (מודעות / engagement / לידים / מכירות ישירות?)
2. למי פונים? (אם שונה מה-ICP ב-`context.md` — פרטו)
3. יש טקסט קיים לשיפור? (אם כן — הדביקו)
4. העדפת טון מיוחדת? (ברירת מחדל: מקצועי, ישיר, בגובה העיניים)

### Channel-Specific Additions

#### 🖥️ Landing Page

5. איזה סוג עמוד? (מוצר / שירות / קמפיין / Event)
2. מה ה-CTA הרצוי? (טופס / WhatsApp / הזמנה / הורדה)
3. יש הוכחה חברתית? (ציטוטים / לוגואים / מספרים)

#### 📧 Email

5. סוג: אימייל בודד / סיקוונס / ניוזלטר?
2. אם סיקוונס — כמה מיילים? מה הטריגר?
3. טמפרטורת קהל: קר / חם / לוהט?

#### 📱 Social

5. איזו פלטפורמה? (LinkedIn / Facebook / Instagram / X)
2. פורמט: פוסט טקסט / קרוסלה / סטורי / Reel?
3. יש ויז׳ואל מתוכנן? (תמונה / סרטון / גרפיקה)

#### 📣 Ads

5. פלטפורמה: Google Search / Google Display / Meta (FB+IG)?
2. סוג מודעה: Search / Display / Video / Stories?
3. יש לנדינג פייג׳ שאליו מפנים? (שתפו URL)

#### 📝 Blog / SEO

5. מילת מפתח מרכזית (Target Keyword)?
2. כוונת חיפוש: מידעית / ניווטית / מסחרית?
3. אורך רצוי: קצר (500) / בינוני (1,000) / ארוך (2,000+)?

#### 💬 WhatsApp / SMS

5. מה הטריגר? (ליד חדש / תזכורת / מעקב / מבצע)
2. הודעה בודדת או סיקוונס?
3. יש Merge Fields? (שם, שם עסק, תאריך)

---

## Phase 2: Strategy (🧠 ניתוח אסטרטגי)

After receiving the brief, present a strategic analysis. **Do NOT write copy yet.**

### Output format

```markdown
## 🧠 ניתוח אסטרטגי

**ערוץ:** [שם הערוץ]
**מטרה:** [מה רוצים להשיג]

### מצב ראש הקהל
[מה הגולש מרגיש/חושב כשהוא נחשף לקופי הזה? 2-3 משפטים]

### התנגדות מרכזית
[מה ההתנגדות #1 שצריך לנטרל?]

### זווית הקופי (Angle)
[מה הגישה שלנו? איך נבנה את הארגומנט?]

### מבנה מוצע
[רשימה ממוספרת של הבלוקים / סקשנים שהקופי יכלול]
```

### ⏸️ GATE — אישור המשתמש

Present the strategy and ask:

```
✅ מאשרים את הכיוון? או רוצים לשנות משהו?
```

**Do NOT proceed to Phase 3 until the user explicitly approves.**

---

## Phase 3: Draft (✍️ כתיבת הקופי)

Write the copy according to the approved strategy. Use **channel-specific output formats**:

### 🖥️ Landing Page Output Format

```markdown
## [Hero Section — המסך הראשון]

**H1:** [כותרת ראשית — 4-7 מילים, פותרת את הבעיה]
**H2:** [כותרת משנה — מסבירה, מוסיפה אמינות, עד 2 שורות]
**CTA כפתור:** [טקסט מניע ממוקד תועלת]
**Micro-copy:** [2-3 מילים מתחת לכפתור שמורידות חשש]

---

## [Body — גוף העמוד | מודל PAS/AIDA]

**הבעיה / הזדהות:**
[2-3 שורות שמתארות את הכאב בגובה העיניים]

**פתרון / תועלות (Bullets):**
- [תועלת 1]
- [תועלת 2]
- [תועלת 3]
- [תועלת 4]

**הוכחה חברתית / סגירת התנגדויות:**
[פסקה קצרה + מיקום מוצע לציטוט לקוח]

---

## [CTA סופי]

**כותרת סיום:** [עניינית, הנעה חלקה]
**CTA כפתור:** [טקסט כפתור]
**Micro-copy:** [מתחת לכפתור]
```

### 📧 Email Output Format

```markdown
## אימייל [מספר] מתוך [סה"כ]

**Subject Line:** [כותרת]
**Subject Line (A/B):** [וריאנט]
**Preview Text:** [טקסט תצוגה מקדימה]

---

**פתיחה (Hook):**
[1-2 משפטים]

**גוף:**
[פסקאות קצרות + bullets]

**CTA:**
[כפתור / לינק + טקסט]

**P.S.:**
[אופציונלי — משפט סגירה]
```

### 📱 Social Output Format

```markdown
## פוסט [שם הפלטפורמה]

**Hook (שורה ראשונה):**
[השורה שגורמת לעצור את הגלילה]

**גוף:**
[תוכן הפוסט]

**CTA:**
[הנעה לפעולה]

**האשטגים:**
[3-5 האשטגים רלוונטיים]

---

📐 וריאנט B:
[גרסה חלופית]
```

### 📣 Ads Output Format

```markdown
## מודעה [פלטפורמה] — [סוג]

### גרסה A:
**Headline 1:** [max 30 תווים — Google / ללא הגבלה — Meta]
**Headline 2:** [max 30 תווים]
**Headline 3:** [max 30 תווים]
**Description 1:** [max 90 תווים]
**Description 2:** [max 90 תווים]
**Primary Text (Meta):** [טקסט ראשי]
**CTA Button:** [טקסט כפתור]

### גרסה B:
[וריאנט חלופי לA/B]
```

### 📝 Blog Output Format

```markdown
## SEO Meta

**Title Tag:** [max 60 תווים]
**Meta Description:** [max 155 תווים]
**Slug:** [url-friendly]
**Target Keyword:** [מילת מפתח]

---

## מאמר

### [H1 — כותרת ראשית]

[פתיחה — Hook + הבטחת ערך]

### [H2 — סקשן 1]
[תוכן]

### [H2 — סקשן 2]
[תוכן]

...

### סיכום + CTA
[פסקת סיכום + הנעה לפעולה]
```

### 💬 WhatsApp / SMS Output Format

```markdown
## הודעה [מספר] — [טריגר]

**הודעה:**
[טקסט ההודעה עם {merge_fields}]

**וריאנט B:**
[גרסה חלופית]

---

📐 הערות:
- אורך: [מספר תווים]
- Merge Fields: [{field_name}]
- תזמון מומלץ: [מתי לשלוח]
```

---

### ⏸️ GATE — אישור הדראפט

After presenting the draft:

```
✍️ הקופי מוכן! כמה אפשרויות:

1. ✅ מאשרים — ונעבור ל-prompt ויז׳ואלי (אם רלוונטי לערוץ)
2. 🔄 תיקונים — ספרו מה לשנות
3. 🔀 וריאנט חדש — רוצים כיוון אחר?
4. ➕ להמשיך לערוץ נוסף — חזרה לתפריט
```

---

## Phase 4: Visual (🎨 prompt לתמונה)

> **Applies to**: Landing Page, Ads, Social, Blog, Email (minimal). **Skip for**: WhatsApp/SMS.

After the user approves the draft copy, generate an **English** image prompt using the **ClearFlow Transformation visual concept** defined in `.agents/skills/clearflow-copy-skill` (Visual Identity section).

Refer to the skill for: brand colors, fixed visual elements, style rules, what to avoid, and channel-specific prompt types.

### Output format

```markdown
## 🎨 Visual Prompt

**Channel:** [channel name]
**Visual Type:** [Full scene / Focused variation / Topic-adapted / Minimal]

**Prompt (English):**
> [Full English prompt per the visual spec in the skill file]

**Recommended aspect ratio:** [16:9 / 1:1 / 9:16 / 4:5]
**Recommended tool:** [Midjourney / DALL-E / other]
```

---

### ⏸️ GATE — אישור סופי

```
🎨 הקופי + הוויז׳ואל מוכנים! מה עכשיו?

1. ✅ מאשרים הכל
2. 🔄 שינויים ב-prompt התמונה
3. ➕ להמשיך לערוץ נוסף — חזרה לתפריט
```
