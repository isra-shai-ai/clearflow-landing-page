---
description: "Pre-flight checklist for launching a ClearFlow client project (Landing Pages, CRM, or Automations) to ensure infrastructure, legal, and UI compliance."
---

# 🚀 ClearFlow Go-Live Checklist

Before handing over a project to a client or turning on live automations, run through this checklist. This ensures ClearFlow delivers enterprise-grade quality, prevents technical debt, and protects the client's domain reputation.

## 1. 📧 Domain & Email Infrastructure (The Deliverability Check)
*If the project involves sending emails (via Make.com, Zapier, CRM, or website forms):*
- [ ] **SPF Verified:** The sending service (e.g., Zoho, Mailgun, Google Workspace) is included in the domain's SPF `TXT` record.
- [ ] **DKIM Verified:** The cryptographic key is generated in the email admin panel and added as a `TXT` record in the DNS.
- [ ] **DMARC Verified:** A `_dmarc` TXT record is present (minimum `p=none` to start monitoring).
- [ ] **Testing:** A test email has been triggered from the live automation to a tool like [Mail-Tester.com](https://www.mail-tester.com/) to verify a 10/10 score.

## 2. ⚖️ Accessibility & Legal Compliance (The Audit)
- [ ] **A11y Widget:** Tabnav (or equivalent) accessibility widget is installed and functioning.
- [ ] **Legal Modals/Pages:** Privacy Policy (מדיניות פרטיות) and Accessibility Statement (הצהרת נגישות) are present, accurate, and localized to Israeli law.
- [ ] **Cookie Consent:** A non-intrusive, compliant cookie banner is active and functional.

## 3. ⚙️ Form & Automation Routing (The Pipeline Check)
- [ ] **Error Handling:** Automations have fallback routes (e.g., if the CRM API fails, the webhook sends an emergency Slack/Email alert so no lead is lost).
- [ ] **End-to-End Test:** A live "test lead" submission has been tracked from the frontend -> Webhook -> CRM -> Auto-responder.
- [ ] **Data Sanitization:** Phone numbers and emails are validated before hitting the CRM database.

## 4. 🎨 UI/UX Final Polish (The Vibe Check)
- [ ] **Mobile Viewport:** Verified layout on actual mobile devices (not just Chrome DevTools).
- [ ] **RTL Consistency:** All Hebrew text flows Right-to-Left perfectly, with no overlapping elements or broken margins.
- [ ] **Performance:** Heavy assets (images, videos) are compressed and loading fast.
