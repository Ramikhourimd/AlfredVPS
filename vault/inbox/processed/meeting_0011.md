---
processed_at: '2026-02-26T20:05:44.442378+00:00'
status: processed
---

# Meeting: Nadav's Jira and Work Plan Presentation | Jan 14, 2025 (Transcript)

---

## 1. Meeting Details

| Field | Value |
| :--- | :--- |
| **Date** | 2025-08-01T23:40:06.255Z |
| **Title** | Nadav's Jira and Work Plan Presentation | Jan 14, 2025 (Transcript) |
| **Classification** | Rami-Ohad Sprint Planning & Jira Onboarding |
| **Category** | Taliaz Company Meetings |
| **Meeting Type** | TLZ-RAMI-OHAD |
| **Source Document** | [https://docs.google.com/document/d/1T1KYuIUucLQB-JmqsisZr_HC45yoCZkOYiJIYvvruVQ/edit?usp=drivesdk](https://docs.google.com/document/d/1T1KYuIUucLQB-JmqsisZr_HC45yoCZkOYiJIYvvruVQ/edit?usp=drivesdk) |

## 2. Participants

| Name | Role | Confidence |
| :--- | :--- | :--- |
| Rami Khouri | Moderation/ownership of sprint structure and Jira process, HealthyMind clinical/product context (case manager intake, effort-low test), Requests time estimates per sprint and Gantt tracking, Schedules/coordinates meeting with Shachar | HIGH |
| Ohad Edri | AI/infra vocabulary (multi-agent ecosystem, API, data-sector, front-end, automated input), Acts as main technical executor responding to estimation/task breakdown requests, Focus on implementation constraints and sequencing | HIGH |
| Unknown (possible Rivi Idelman) | Very few/short turns, Coordination/liaison behavior (sent a message to the group), No strong domain/role-specific markers to confirm identity | POSSIBLE |

## 3. Key Topics

- Jira setup and workflow discipline (issues
- descriptions
- attachments
- status tracking), Sprint planning: breaking work into tasks/milestones and producing time estimates per sprint, Gantt-style tracking and weekly cadence/check-ins, AI agent development planning (multi-agent ecosystem
- recap/prompt corrections), Infrastructure/data integration needs (data-sector
- APIs
- front-end vs backend split
- automated inputs), Clinical workflow components mentioned (case manager intake
- Effort-Low test), Coordination with Shachar on technical requirements / playbook ("labook") and next steps

## 4. Full Transcript

> **Note:** Transcript language matches the original meeting language.

---

```
Rami Khouri (00:00): צריכים לשנות את ה כאילו יש תיקונים שצריך לעשות את הפרונקס 
Ohad Edri (00:11): אה סיפור ראשון או שמשאירים זה ומוסיפים עוד פרונקס את ה-recap נכון או שמבקשים משנים את הפרונק ככה שהוא יוסיף בסוף ריקאפ 
Rami Khouri (00:21): עכשיו שיתכנתי לך עכשיו שיתכנתי לך עכשיו שיתכנתי לך עכשיו שיתכנתי לך זה היה רמי הראשון נלחץ פה עוד בולטים רמיים פה ב-chatbot לא ידעתי לפרק את זה את התי משימות את הדבר הזה אני אשמח שתעזור לי לאיזה משימות או מייסטונס ברבהת השלבים ולא משימות כשאתם מחלקים את הפרויקט הזה מעבר לברור שזה אי-פיון פיתוח אם יש לך משהו יותר עמוק לתת שם 
Ohad Edri (01:01): בהתחלה צריך להפיין את ה זה לפיישנט יש כדור לפיישנט אפשר גם עוד 
Rami Khouri (01:18): לא אפשר כשנהפיין לפרק את המשימות וכרגע שיהיה איזה רק בסדר 
Ohad Edri (01:30): איקוסיסטים עם מולטי איג'נט מתחיל מ-2 איג'נטים עד 20 זה מתייחס עכשיו נכתוב 
Unknown (possible Rivi Idelman) (01:40): לי את הטרמינום יכולים לתחיל 
Ohad Edri (01:43): את העפר זה המער זה שאני שוכח לפתוח בו מייל אירון 
Unknown (possible Rivi Idelman) (01:52): אה זה רואים 
Rami Khouri (01:55): אני אשמח להערכות זמנים לכל ספרינט זאת אומרת אתה תוכל לעבור על זה לתת איזה ערכת זמנים של שבוע שבועיים שלושה תחמיר איתי כאילו לוקח את הזמן שאתה באמת צריך ובמקרה הטוב תעשה לפני כדי שאני כבר אחלק את זה לספרינטים ואני אוכל גם נוכל לראות את זה בגנט כאילו שיש לנו ונוכל לעקוב אחריו בפגישות השבועית מה קציר טוב נגיד ספרינט 1 שבועיים ספרינט 2 שלושה שבועות אני גם מבין לפי זה אם חילקתי את הספרינטים בצורה נכונה או שאולי ימחתי אותם מדי על הספרינט אחד 
Ohad Edri (02:29): קשה לי להמיד לך פשוט כל מה דברים שאני עושה בשעה אני אקח כנראה לאחד הדברים 
Rami Khouri (02:42): אוקיי אז בוא נלמד את הספרינטר הראשון ואחרי שנסיים אותו אני כן אקשט 
Ohad Edri (02:46): תן איזה שבועיים כולל השבוע שאני לא נמצא 
Rami Khouri (02:50): אה משהו שבוע הבא סבבה דבר אחרון אז זה היה בעצם הספרים הראשון פה בג'ירו יש פה את המשימות שדיברנו עליהם עכשיו בעצם הטסט של האפורט לואו הקייס מנג'ר אינטק אג'נדה ואת התריאה שחילקתי לשלוש משימות כאילו שלושה שאלונים יכול להיות שלא צריך 
Ohad Edri (03:09): אני כן צריך אבל כדי להתחיל לעבור את ה-data-sector לכל דוקימנט נגיד פה אנחנו באינטקט אני צריך את ההרצאה של האינטקט אני מחלק את זה פרונט לא צריך יש לי אותו אבל אינפוט אוטו 
Rami Khouri (03:38): אז מה אתה אומר שאני אזמן לנו בחמישי הקרוב עם שחר פגישה מוקדת רק על זה שנבין מה צריך כאילו אני מקובלעי עכשיו כל המסביב של הגדרות מלא עבודה מה ספציפית זה שתוכל לבד שבוע הבא להתקליט את זה 
Ohad Edri (03:52): זה מה שלחתי לשפר לגבי הלבוק כן הוא יחסית 
Unknown (possible Rivi Idelman) (03:54): כל המסביב של הגדרות מהעבודה מספציפית לזה כי יש לו חלק בשבוע והמתיק תורה חדשה זה מה שלחתי לשפר לך היום בבוקר הוא 
Rami Khouri (03:55): יחסית לא זה לא מה את זה שכחת לרדת 
Unknown (possible Rivi Idelman) (04:01): לא שוכחים אני לא שוכח 
Ohad Edri (04:03): בוא תשבי אחת לשתינו 
Unknown (possible Rivi Idelman) (04:06): למה לא אתה רמת את ה יש כל מיני דוגמים מסוכרים זה מספר זה לא רצוע לא זה סופר די פשוט שלב אחד שתיתן לך את החולשי שלך זה נגיד מהנחות לווי-פיי זה נגיד מהנחות לווי-פיי כן לא לא הוא לא יד 23 
Rami Khouri (04:35): זה לא בא למטה של הקופסא אתה רוצה שאני אזמין לו פגישה היתר בחמישה אתה נותן בפנים בגבי הפגישה 
Ohad Edri (04:49): תכתוב לו את זה יש לך מבקש 
Unknown (possible Rivi Idelman) (04:50): לשמור על קלומטור אתה לא תבקש לא לגבי הפגישה תכתוב 
Rami Khouri (04:50): לא יותר בקיצור הג'ירה גם לנו כשלידרית ספר בעצם עברנו לעבוד בצורה מסוגלת בג'ירה ולקחנו זמן כי זה בהתחלה קצת מעיק לטעת את הדברים וזה אנחנו עובדים בצוות מי כן כי זה קצת מעיק בהתחלה אבל כשעובדים בצוות זה מאוד מאוד חשוב אז אני רוצה שנתרגל כבר מעכשיו לקח כבר מראש את ה מה אתה רוצה 
Unknown (possible Rivi Idelman) (05:19): חבר יש 
Ohad Edri (05:20): פה api בטוח 
Rami Khouri (05:24): אמא שכן 
Ohad Edri (05:29): תראה איך את צריכה כזה לחזק זה 
Rami Khouri (05:35): קלאסי מהמשימות בתור התחלה אני אסמך שתיקח את המשימות האלה ונכניס את האיפיון לפה באיזשהו פורמט שנסכים עליו זה יכול להיות פה ב-description אפשר לצרף את זה כקובץ חיצוני אם אתה רגיל ואוהב להפיין במסמך וורד או מנדי או לא יודע מה אפשר לצריך שם קובץ אבל שכאילו ה-ipu נהיה מצורף לנו פה בדבר הזה ואני מציע לך ברמות הניהול עבודה לעבוד ממש פר נשימות כי אז יש לנו בקרה לסטטוסים אם אני נותן נגיד לדער אותך נשימה מאוד גדולה אז קשה לי להעריך איפה הם נמצאים בתוכה אבל אם אני אפרק להם את זה אז אני יכול ממש להבין מה בתוך זה הם כבר עשו וזה פשוט עוזר לי עם כמה זמנים לסייח את תכניתו בתור זהו ננסה לא יעבוד לנו פה נמצא שיטה אחרת רק שנכניס פה את האפיונים ונעבור לה אז גם שאתה לא נמצא נגיד אגב אם האפיונים יהיו פה ואני מכיר את הפרומט של אפיונים אני יכול לפנות שאלות אליי ולא יודע ואני גם אוכל כאילו לדבר איתם אז בטח אז אלה עכשיו בדיזיין מבחינתה 
Unknown (possible Rivi Idelman) (06:56): ראית את הודעה ששלחתי לכם 
Ohad Edri (07:01): כן לא אותך כן לא התחלתי גדול לעבור על אף אחד מהם בסדר בבקשה תתחיל תעביר 
Rami Khouri (07:08): אם זה יכול את כל אחד לדעת איך הפרויקט ימולות 
Unknown (possible Rivi Idelman) (07:12): אה חכה חכה חכה תודה רבה
```