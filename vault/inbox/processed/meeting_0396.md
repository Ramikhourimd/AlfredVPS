---
alfred_tags:
- meetings
processed_at: '2026-02-26T20:26:44.810618+00:00'
status: processed
---

# Meeting: 02-23 פגישה: הגדרת מדדי KPI ופיתוח סוכן AI

---

## 1. Meeting Details

| Field | Value |
| :--- | :--- |
| **Date** | 2026-02-23T11:55:25.112Z |
| **Title** | 02-23 פגישה: הגדרת מדדי KPI ופיתוח סוכן AI |
| **Classification** | {"meeting_id":"TLZ-RAMI-OHAD","meeting_name":"ישיבה רמי-אוהד (Rami-Ohad Meeting)","confidence":0.82,"confidence_level":"HIGH","category":"Taliaz Company Meetings","is_active":true,"is_new_suggestion":false} |
| **Category** | Taliaz Company Meetings |
| **Meeting Type** | TLZ-RAMI-OHAD — ישיבה רמי-אוהד (Rami-Ohad Meeting) |
| **Source Document** | [https://docs.google.com/document/d/1p9lttb8Tdx3Dfr441N0MnA8qeJdQu2a_YVvlbwF0Nc4/edit?usp=drivesdk](https://docs.google.com/document/d/1p9lttb8Tdx3Dfr441N0MnA8qeJdQu2a_YVvlbwF0Nc4/edit?usp=drivesdk) |

## 2. Participants

| Name | Role | Confidence |
| :--- | :--- | :--- |
| Ohad Edri | N/A | 0.78 |
| Rami Khouri | N/A | 0.91 |


## 3. Key Topics

- Slack support/SLA response-time monitoring and Slack analysis access
- Agentic AI skill-building plan and workflow design
- KPI definition algorithm: defined → measurable → in use → in data warehouse → clean entity
- Processing Basel’s KPI metrics table into a structured
- validated KPI table
- Data warehouse integration and entity/table creation (BigQuery
- Supabase)
- Ownership/roles for KPI implementation (project management + domain experts; handoffs to R&D for DWH work)
- Target output schema for KPI catalog (category
- type
- definition
- tool
- frequency
- subject
- RACI
- current value
- numeric target)

## 4. Full Transcript

> **Note:** Transcript language matches the original meeting language.

---

```
Ohad Edri 00:00:00<br>בטמיכה טכנית זה זה, בדיקת זמני תגובה, זמן תגובה לבניות צוות בסלאק, כאילו מה שאני רואה שכאילו זה ואז כאילו שחר עונה או. SLA, כאילו, סלאק אנלסיס, יש לזה גישה רפון או בדקתי. <br>Rami Khouri 00:00:21<br>כן כן, קודם כל, המאנוס פה מכוון לסלאק שלי, אוקיי, אז אתה יכול. להגיד לו, תבדוק האם זה. מדי דברים להסתיר שם, אבל תגיד לו, זה משהו שאתה יכול לבדוק.<br>Ohad Edri 00:00:44<br>כי יש לו את הטול, כן, אוקיי.<br>Rami Khouri 00:00:49<br>מה עוד? אז ככה בוא נחזור על זה שנייה אני מקליט, כן קליט עם לול ואז נבנה את הסקיל עכשיו, אז מה שאנחנו רוצים לעשות זה להכניס את הטבלה שבאסל שלח שהיא מורכבת מהצעות למדדים.<br>Rami Khouri 00:01:19<br>אנחנו רוצים להעביר אותה לפי את החלטות שבודק האם המדד הזה מוגדר אם הוא לא מוגדר היטב צריך להגדיר אותו אם הוא מוגדר צריך לבדוק האם הוא מדיד אם הוא מדיד אם הוא לא מדיד צריך לעשות לזה break down או הגדרה מחדש זאת אומרת אם זה מדד כללי ואפשר לפרק את זה לכמה אז אפשר לעשות את זה ככה.<br>Rami Khouri 00:01:54<br>או אם לא אז צריך להגדיר אותו בצורה אחרת, אם הוא מדיד, האם הוא בשימוש בפרקטיקה היום, אם לא, אז צריך להגדיר KPI וכלי מדידה, שזה הולך בעצם ל-EAL, שהיא מנהלת הפרויקטים, ול-Domain Expert, לפי סוג ה-KPI. אם הוא בשימוש בפרקטיקה, האם הוא נמצא בדאטה ווירהאוס, בקסאנו או בביקווירי, אם לא, אז צריך לבנות טבלה חדשה או אנטיטי חדש בתוך טבלה קיימת בדאטה ווירהאוס שלנו, שזה לשחרר.<br>Rami Khouri 00:02:46<br>אם כן, אז האם הוא אנטיטי נקי, זאת אומרת נפרד עצמאי. אם לא אז צריך לבדוק מה הלוגיקה האם צריך לחבר כמה entities כדי לבנות אותו או לעשות שינוי מסוים וגם זה הולך לשחר או שמוליק ואם כן אז סיימנו אחרי שאנחנו עוברים על כל המדדים האלה צריך לבנות טבלה חדשה שיש בה.<br>Rami Khouri 00:03:23<br>KPI שמחולק לפי קטגוריה שזה קליני אדמנסטרטיבי פיננסי וכו' סוג שזה בעצם מה זה זה סביעות רצון זה מדד שיפור מדד רמיסיה בעצם מה ההגדרה שלו מה הכלי הטול טייפ הפרקונסי שבה אנחנו עושים אותו הסאבג'ק טייפ מה אנחנו בודקים.<br>Rami Khouri 00:03:55<br>מי responsible מי accountable ומה kpi שהוא נכון להיום מה היעד מספרית מצוין עכשיו אנחנו צריכים לבנות skills agentic skills שישתמשו בעצם הם מקבלים כמדד מוצא draft משתמשים בbigquery mcp בסופה בייס דרייב ג'ימייל.<br>Rami Khouri 00:04:32<br>ובעצם עושים את החלוקה הזאת עוברים לפי האלגוריתם הזה ובונים בסוף את הטבלה הסופית
```