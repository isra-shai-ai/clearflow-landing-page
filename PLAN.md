# 📝 PLAN.md - Make.com Webhook Integration

## 🎯 Phase 1: Explore & Plan

### Goals

1. **Connect forms to Make.com Webhook**: Replace dummy logic in both Hero and Footer forms with a live `fetch()` request to the provided Make.com URL (`https://hook.eu1.make.com/p3evkp5wlspqvo3g1ln8qyxanf23h7as`).
2. **Standardize Payload (`formData`)**: Ensure the request payload structure contains `fullName`, `email`, and `phone` values.
3. **Preserve UI State**: Ensure the form disappears and the "Thank You!" success message appears upon a successful fetch response.
4. **Error Handling**: Add `console.error` logging and a Hebrew `alert()` for any fetch failures.

### Identified Gap (Please Note)

- **The Hero Form currently does not have an Email field.** (It only asks for Name and Phone).
- *Solution:* To satisfy the webhook's structure expectation, the script will pass an empty string `""` for the `email` field when the submission originates from the Hero Form. The Make.com scenario should be prepared to handle an empty email when `source` is "Hero Form".

### Scope of Changes

- **`index.html`**:
  - Update the `<script>` tag at the bottom of the document.
  - Create a reusable `submitToWebhook(formElement, payload, successCallback)` async function.
  - Capture values explicitly from the inputs (using native DOM querying targeting ID or `name` attributes).
  - Handle the `submit` event for `#contactForm` (Footer).
  - Handle the `submit` event for `section form` (Hero).
  - Implement `try/catch` with `alert('אירעה שגיאה בשליחת הטופס. אנא נסו שוב מאוחר יותר.')` and console logging.
  - Disable the submit button and show "שולח..." during the fetch to prevent duplicate submissions.

---

## 🚀 Execution Steps (Phase 3)

| Status | File | Task Description |
| :---: | :--- | :--- |
| ✅ | `index.html` | Create the shared webhook submission function (`fetch` wrapper with error handling). |
| ✅ | `index.html` | Update Footer form logic to build payload and call webhook. |
| ✅ | `index.html` | Update Hero form logic to build payload (with empty email) and call webhook. |

*Status tracking:* ⏳ Pending | 🚧 In Progress | ✅ Completed | ❌ Blocked
