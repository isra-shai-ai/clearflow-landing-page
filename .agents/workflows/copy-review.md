---
description: Review and improve existing copy — structured audit with scorecard, before/after rewrites, and actionable recommendations.
---

# /copy-review — ClearFlow Copy Review Workflow

> **Pre-requisite**: Read `.agent/copy-agent.md`, `.agent/brand/voice-and-tone.md`, and `.agent/brand/context.md` before starting.

---

## Step 1: Input Collection

Ask the user:

```
📋 מה תרצו שאבדוק?

1. הדביקו את הטקסט הקיים כאן
2. שתפו URL של עמוד קיים
3. צרפו צילום מסך

ואם אפשר — ספרו לי:
- מה לא עובד? (המרות נמוכות? טון לא מתאים? ארוך מדי?)
- מה המטרה של הקופי הזה? (הנעה לפעולה? מודעות? חינוך?)
```

---

## Step 2: Audit (🔍 ביקורת מובנית)

Run the copy through a structured audit. Score each dimension 1-5:

### Output format:

```markdown
## 🔍 ביקורת קופי — Scorecard

| קריטריון | ציון (1-5) | הערות |
|-----------|:----------:|-------|
| **בהירות** — האם ברור תוך 3 שניות מה מציעים? | X | [הערה] |
| **רלוונטיות** — האם מדבר בשפה של הקהל? | X | [הערה] |
| **תועלות vs. תכונות** — האם ממוקד במה הלקוח מרוויח? | X | [הערה] |
| **חיכוך** — האם יש משהו שעוצר את הגולש? | X | [הערה] |
| **CTA** — האם ברור מה לעשות ולמה? | X | [הערה] |
| **טון** — האם מתאים ל-Voice & Tone של ClearFlow? | X | [הערה] |
| **אורך** — האם הכל הכרחי? | X | [הערה] |

**ציון כולל: X/35**

### 🚩 בעיות קריטיות
- [בעיה 1 — הכי דחוף לתקן]
- [בעיה 2]

### 💡 הזדמנויות
- [שיפור שיכול להעלות המרות]
- [שיפור שיכול לחזק אמינות]
```

---

## Step 3: Rewrite (✍️ שכתוב Before/After)

For each critical issue, show a Before/After rewrite:

### Output format:

```markdown
## ✍️ שכתוב מומלץ

### תיקון 1: [שם הבעיה]

**לפני ❌:**
> [הטקסט המקורי]

**אחרי ✅:**
> [הטקסט המשופר]

**למה:** [הסבר קצר — משפט אחד]

---

### תיקון 2: [שם הבעיה]
...
```

---

## Step 4: Summary + Next Steps

```markdown
## סיכום

**3 הדברים הכי חשובים לתקן:**
1. [תיקון בעדיפות 1]
2. [תיקון בעדיפות 2]
3. [תיקון בעדיפות 3]

---

🔄 מה עכשיו?
1. ✅ ליישם את התיקונים
2. ✍️ רוצים שאכתוב גרסה מלאה משוכתבת?
3. 🔀 לעבור ל-`/copy` ולכתוב מאפס
```
