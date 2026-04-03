---
alfred_tags:
- meetings
processed_at: '2026-02-26T20:18:15.847805+00:00'
status: processed
---

# Meeting: Shachar and Rami | Jun 17, 2025 (Transcript)

---

## 1. Meeting Details

| Field | Value |
| :--- | :--- |
| **Date** | 2025-08-02T00:35:28.244Z |
| **Title** | Shachar and Rami | Jun 17, 2025 (Transcript) |
| **Classification** | NEW |
| **Category** | NEW |
| **Meeting Type** | TLZ-RAMI-SHACHAR — Taliaz-level 1:1 (Product/Technical Design) |
| **Source Document** | [https://docs.google.com/document/d/1TVbnkIyqvgrbr6Bea_luSnLLWAhQeHTEZeuY2n5pqRY/edit?usp=drivesdk](https://docs.google.com/document/d/1TVbnkIyqvgrbr6Bea_luSnLLWAhQeHTEZeuY2n5pqRY/edit?usp=drivesdk) |

## 2. Participants

| Name | Role | Confidence |
| :--- | :--- | :--- |
| Dr. Rami Khouri | N/A | N/A |
| Shachar Segev | N/A | N/A |

## 3. Key Topics

* HealthyMind crisis psychiatric consultation service (“קונינות”) end-to-end flow design
* CRM usage/integration and cost considerations (~$50/user/month)
* Telephony setup and call routing strategy (single number, forwarding, future shift-based routing)
* Intake/request mechanism (form vs phone call) and required fields for opening a case
* Operational workflow between social worker, psychiatrist, and the system(s)
* Automation ideas: SMS notifications, workflow automations (e.g., n8n), and task creation
* Data/analytics pipeline considerations (Supabase, BigQuery connections)
* Payment model and tracking (e.g., 350₪ consult, 900₪ exam) and related bookkeeping requirements
* Potential automatic transcription and summarization of calls/consultations

## 4. Full Transcript

> **Note:** Transcript language matches the original meeting language.

---

```
Shachar Segev: תודה רבה. אה,
Dr. Rami Khouri: יש לך. תודה. אה
Shachar Segev: שלח
Shachar Segev: 
Dr. Rami Khouri: כן.
Dr. Rami Khouri: ראה אותי, שומע אותי? כן
Dr. Rami Khouri: אני בינתיים לא רואה אותך
Shachar Segev: לא רואה
Dr. Rami Khouri: לא.
Shachar Segev: כל מי שאין דבר חדש כאן
Shachar Segev: אני רואה את עצמם.
Dr. Rami Khouri: זה יגיע.
Dr. Rami Khouri: בוקר טוב
Dr. Rami Khouri: אז ככה לגבי ההתמוננות
Dr. Rami Khouri: אז התחלנו כמו בקטנה
Dr. Rami Khouri: אבל בגדול
Dr. Rami Khouri: אתה חושב שנוכל באמת לעשות את ה... להשתמש במערך CRM?
Shachar Segev: כן, החסרון היחידי שזה עולה איזה 50 דולר ליוזר לחודש, אבל זה נראה. לשווה.
Dr. Rami Khouri: אם באמת נחתום על ההסכם הזה
Dr. Rami Khouri: זה משהו מאוד מינורי, יחסית למה שהם ישרדו. אוקיי
Shachar Segev: אז בוא נדבר על ה-flow כאילו רגע מה צריך....
Dr. Rami Khouri: אז מבחינת ה... בוא ננסה לחלק את זה למי שפונה, נגיד עובד סוציאלי, יש לנו את הפסיכיאטר ובאמצע יש את המערכת, או את שתי המערכות. השלב הראשון זה שהעובד הסוציאלי צריך לפנות. אז זה יכול להיות... על ידי פתיחת קריאה כלשהי או שהוא פשוט מתקשר
Shachar Segev: ...צריך
Dr. Rami Khouri: מה אנחנו
Shachar Segev: רוצים שהוא יתקשר או רוצים שיהיה איזה שאלון או...
Dr. Rami Khouri: ...לא מבחינתי בהתחלה זה יכול להיות
Shachar Segev: תחת
Dr. Rami Khouri: טלפון פתחת טלפון מה שאני צריך
Shachar Segev: שיהיה... ואיך הוא ידע לאיזה טלפון כאילו...
Dr. Rami Khouri: אז זהו בתור התחלה זה יהיה רק אני
Dr. Rami Khouri: אז אפשר שזה יהיה מספר
Dr. Rami Khouri: לא שלי אנחנו כאילו
```