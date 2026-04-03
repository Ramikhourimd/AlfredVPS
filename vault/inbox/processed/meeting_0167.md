---
alfred_tags:
- rami/meetings
- zoom-sessions
processed_at: '2026-02-26T20:17:53.644297+00:00'
status: processed
---

# Meeting: rami's Zoom Session | Jun 16, 2025 (Transcript)

---

## 1. Meeting Details

| Field | Value |
| :--- | :--- |
| **Date** | 2025-08-02T00:34:53.174Z |
| **Title** | rami's Zoom Session | Jun 16, 2025 (Transcript) |
| **Classification** | NEW |
| **Category** | NEW |
| **Meeting Type** | Ad-hoc 1:1 Technical Sync (Taliaz — CMO ↔ VP R&D) |
| **Source Document** | [https://docs.google.com/document/d/1xjI-jVvpZOZt0eTaqepkcNlKuyoKaX8iug1q1cdlELs/edit?usp=drivesdk](https://docs.google.com/document/d/1xjI-jVvpZOZt0eTaqepkcNlKuyoKaX8iug1q1cdlELs/edit?usp=drivesdk) |

## 2. Participants

| Name | Role | Confidence |
| :--- | :--- | :--- |
| Dr. Rami Khouri | Chief Medical & Innovation Officer | 0.97 |
| Shachar Segev | VP R&D | 0.97 |


## 3. Key Topics

* CSV data export automation and processing of new files
* Treatment response labeling/modeling (full response / partial response / no response / remission) and defining reliable logic
* Using CRM to track and document phone calls (who called
* when
* and outcomes)
* Phone call transcription needs and workflow integration
* Clinic intake flow design: lead creation → send short questionnaire → open clinic flow (separate from standard treatment series)
* Legal/privacy considerations: avoiding patient-identifying details during calls
* Automated email summary after calls (sending brief recommendations and next steps)

## 4. Full Transcript

> **Note:** Transcript language matches the original meeting language.

---

```
Dr. Rami Khouri (59.83): אתה 
Shachar Segev (60.11): מיוט? אתה שומע אותי? כן. 
Dr. Rami Khouri (66.76): שומעתי. 
Shachar Segev (73.52): כן, 
Dr. Rami Khouri (73.69): כן, אתה שומע אותי? 
Shachar Segev (77.08): כן. 
Dr. Rami Khouri (77.76): אוקיי. 
Shachar Segev (78.29): אז בגדול, 
Shachar Segev (83.19): לגבי 
Dr. Rami Khouri (83.68): הדאטה, שלחתי לך, אם 
Dr. Rami Khouri (89.24): זה... של אחת הדוגמאות, 
Dr. Rami Khouri (95.65): שמפה 
Shachar Segev (96.27): אני 
Dr. Rami Khouri (96.45): יכול בקלות להוציא טבלת CSV. אם 
Dr. Rami Khouri (101.54): אני 
Dr. Rami Khouri (110.86): רוצה, אני בונה אוטומציה, שתעבור על 
Dr. Rami Khouri (116.69): כל קובץ חדש, 
Dr. Rami Khouri (119.39): פשוט צריך להסתכל 
Shachar Segev (120.99): פה 
Dr. Rami Khouri (121.22): על אם זה מספיק לנו, כי 
Shachar Segev (123.32): חבל 
Dr. Rami Khouri (123.92): לעשות את זה שוב, להכניס כמה שיותר מתונים. 
Shachar Segev (153.54): אני רוצה 
Dr. Rami Khouri (154.22): להכניס כמה 
Shachar Segev (155.2): שיותר 
Shachar Segev (157.02): ו... 
Dr. Rami Khouri (157.15): בסדר, אז זה באותה תקיעה? 
Shachar Segev (160.09): הלכת 
Dr. Rami Khouri (160.39): לי את התקיעה? 
Dr. Rami Khouri (162.29): כן, אני חושב שזה לא מצב, אני לא קרופסוליסט אני גם לא צריך, כאילו, מבחינתי יכול לעבוד על 
Dr. Rami Khouri (171.9): כבר כל פעם 
Dr. Rami Khouri (177.69): השימות הם 
Shachar Segev (179.03): כאילו 
Dr. Rami Khouri (179.37): אותו לוגיקה נכון? אג' אם הקליניקה ומספר. 
Dr. Rami Khouri (188.09): סבבה. 
Shachar Segev (190.03): נראה 
Dr. Rami Khouri (190.23): לי אני גם כזה כשהיא מספיק, 
Shachar Segev (192.32): אני אעשה 
Dr. Rami Khouri (192.68): גם להוציא דאטה בעצמי. 
Shachar Segev (197.9): נחמד, 
Dr. Rami Khouri (198.28): יש לא מעט, יש לך רעיונות 
Shachar Segev (201.81): למה 
Dr. Rami Khouri (202.03): להוציא משם? 
Dr. Rami Khouri (205.06): אם כבר... 
Dr. Rami Khouri (213.95): יש לי דברים שהם לא טוב כלומים? לא, אבל כשנפנד את הפונק, תגידו לגידה, סיכמים, עזרד, אקויוטים. כן, זה נתוח. כן, מה היה בתקדול, לעומת מה היה בסיכום. 
Dr. Rami Khouri (233.74): אני מתכוון לדאטה, כאילו דאטה ממש... זה לא מי ידע את זה. כן. לא ידע את זה, לא ידע את זה 
Shachar Segev (243.95): לנתן. 
Dr. Rami Khouri (244.27): רוקו מיישב. 
Shachar Segev (246.77): אז 
Dr. Rami Khouri (246.91): כאילו שמתי פה מין כזה, 
Dr. Rami Khouri (249.61): responded to treatment, 
Dr. Rami Khouri (252.13): אז הגדלתי לו 
Shachar Segev (253.05): full 
Dr. Rami Khouri (253.41): partial no response, וremission. 
Dr. Rami Khouri (256.92): כן צריך להגדיר לו לוגיקה, לפחות 
Shachar Segev (260.6): שזה 
Dr. Rami Khouri (260.86): יהיה אמין. 
Shachar Segev (265.16): אני חושב 
Dr. Rami Khouri (265.56): שבתוך הטקסט דיברנו על הטראומה עצמה להגדיר אותה אם 
Shachar Segev (269.88): זה דרדת שונה 
Dr. Rami Khouri (270.88): או 
Shachar Segev (271.14): איזה שהיא העובדנות. 
Shachar Segev (276.17): תופעות 
Dr. Rami Khouri (276.67): לבי אייקול. 
Shachar Segev (278.97): נסתפק 
Dr. Rami Khouri (279.41): בזה בינתיים מקסימום נריץ שוב. תסתכל, תראה אם אמרים שאלו שם, אם היית 
Shachar Segev (288.44): בעירואלים, 
Dr. Rami Khouri (290.47): לא זוכר אם תבוא, אין שם כמה שאלה. 
Dr. Rami Khouri (298.52): אה... 
Dr. Rami Khouri (300.18): בסדר נעשה מחר את השיחה, ניכנס ממש לפרטים, 
Dr. Rami Khouri (306.16): אבל בגדול, 
Dr. Rami Khouri (308.5): יכול להיות שאפשר גם להשתמש בCRM, כי זה שיחות טלפון, 
Shachar Segev (315.32): חושב 
Dr. Rami Khouri (315.74): שרוב הבניות יהיו בשיחות טלפון, 
Shachar Segev (318.46): צריך 
Dr. Rami Khouri (318.67): גם למצוא דרך לתמלל אותן, זה 
Shachar Segev (320.54): שאלון לפני זה 
Dr. Rami Khouri (321.81): ממש 
Shachar Segev (322.57): ראשון, 
Dr. Rami Khouri (326.1): וגם, יש שני דברים שאני מתלבט איך לעשות אותם. יש, 
Dr. Rami Khouri (332.73): על שיחות הטלפון אני בכוונה רוצה שמול המטפל, מול הפונה, שזה לא יהיה עם פרטים 
Shachar Segev (341.07): של 
Dr. Rami Khouri (341.21): המטופל, כדי שאני 
Shachar Segev (342.93): אהיה 
Dr. Rami Khouri (343.16): מכוסי 
Shachar Segev (344.93): משפטי. זאת 
Dr. Rami Khouri (346.07): אומרת, הוא יתקשר, אגיד לי יש לי מטופל שסובל מי זה זה זה, מה אפשר לעשות? 
Shachar Segev (352.3): עכשיו 
Dr. Rami Khouri (352.56): אם אני חושב שזה לא מתקשר זה 
Dr. Rami Khouri (366.06): לא מתקשר. תודה רבה. אני רוצה לתאד ואני רוצה גם לדעת שכאילו בסוף החודש אנחנו נשלח להם דרישת השלום 
Dr. Rami Khouri (373.64): או לא דרישת השלום לא יודע 
Shachar Segev (375.36): כן 
Dr. Rami Khouri (375.56): דרישת השלום. שיהיה מתועד 
Shachar Segev (377.89): מתי 
Dr. Rami Khouri (379.4): מי עשה את השיחה ומתי כל כל הדברים ואז אם אני מחליט בשיחה לבדוק את המטופל אז לשלוח לו 
Shachar Segev (389.06): שאלות. 
Dr. Rami Khouri (392.54): ואז נקשור נשאר בנושאים. בדיוק כן. עוד צריך לקשור. עוד צריך לקשור 
Dr. Rami Khouri (400.16): בשאלון. 
Dr. Rami Khouri (407.98): אני חושבת שאני נגיד אני מקבל שיחה אז נפתח 
Dr. Rami Khouri (414.28): ליד או 
Shachar Segev (414.98): משהו בסגנון 
Dr. Rami Khouri (417.89): במערכת ואז מתוכו 
Shachar Segev (420.59): מתוך 
Dr. Rami Khouri (421.05): הליד הזה אני שולח שאלון. 
Dr. Rami Khouri (431.3): שאלה לא ידעת קליניקה זה משהו נפרד. 
Dr. Rami Khouri (440.69): אז יש שאלון גם אחר. זה לא 
Dr. Rami Khouri (444.28): סדרת טיפולים הרגילה שלנו. זה שאלון מאוד קצר זה שאלון פשוט שהם יכניס את הפרטים של המטופל. אבל כן צריך לפתוח גם קליניקה עם איזה פלו חדש. שהיא רק בדיקה של ספירת. 
Shachar Segev (460.05): זה 
Dr. Rami Khouri (463.63): לא עולה 
Shachar Segev (463.79): עכשיו 
Dr. Rami Khouri (467.15): לקיסר מנדרינט כבר בו. זה עוד, אני צריך להגיע את ה-flow. ה-flow של הקליניקה, כבר עד שהוא ייכנס לקליניקה. 
Shachar Segev (473.29): כן, 
Dr. Rami Khouri (473.45): וגם בלי נמליש של תרפת הקליניקה. עוד 3,000 אונלוסים, אני חייב להגיע לסייט. אני חייב להגיע לסייט, 
Dr. Rami Khouri (485.34): אבל... 
Dr. Rami Khouri (486.98): עמדים על הסטים עמדים גם במטה מקשר 
Shachar Segev (490.02): לא 
Dr. Rami Khouri (490.18): מתופעת רק רוצה לדעת שהוא מגיע מי. את הסיכוי עצמאי. אין 
Shachar Segev (498.35): משהו. 
Dr. Rami Khouri (498.83): כן אני רוצה לשלוח להם במייל סיכום שלה. כי יכול 
Shachar Segev (503.01): אני. 
Dr. Rami Khouri (504.06): בשיחה עצמה יש מצב שאני אתן להם המלצות כלליות. 
Dr. Rami Khouri (509.84): אז אני שולח לך. ‫לבוא לי מסכום קצר, כן, ‫לשלוח אותו 
Shachar Segev (513.74): במי. 
Shachar Segev (518.65): אז 
Dr. Rami Khouri (518.79): שתהיה. קרובים 
Shachar Segev (520.11): סטייפ לגירוי 
Dr. Rami Khouri (520.71): ועוד. קרובים סטייפ לגירוי ועוד. קרובים סטייפ לגירוי ועוד. אז לדבר על זה, מספר את רציתי לתת לך כיוון 
Dr. Rami Khouri (529.02): מהפלור. 
Shachar Segev (529.76): אה. כן, 
Dr. Rami Khouri (530.82): היה נחמד, גירוי, די בא לי להתאמש בסרטון. אולי כי זה יותר קל לי לחוקר שם. אני חוקר, אני חוקר מהם. אני חוקר 
Dr. Rami Khouri (540.77): שם, יש לי פיצ'רים כאילו שקורדים בחינם. תודה. 
Dr. Rami Khouri (548.65): אם כל זה לא אפילי כממש, סיפרים אטומטיים וזה, אז... אני 
Dr. Rami Khouri (553.83): איתך שחוק. אח, תודה רבה. 
Shachar Segev (559.1): תודה. ביי 
Dr. Rami Khouri (564.8): ביי.
```