---
alfred_tags:
- rami/meetings
- zoom-sessions
processed_at: '2026-02-26T20:05:53.669530+00:00'
status: processed
---

# Meeting: rami and Yaron Meeting | Jan 28, 2025 (Transcript)

---

## 1. Meeting Details

| Field | Value |
| :--- | :--- |
| **Date** | 2025-08-01T23:44:19.294Z |
| **Title** | rami and Yaron Meeting | Jan 28, 2025 (Transcript) |
| **Classification** | Rami-Yaron Advisory Session |
| **Category** | External |
| **Meeting Type** | External — 1:1 Advisory / Onboarding Session |
| **Source Document** | [https://docs.google.com/document/d/1tIbWPwNTU43KPxbo2XlWjUoz1zecnBYQ13mngvRTNQo/edit?usp=drivesdk](https://docs.google.com/document/d/1tIbWPwNTU43KPxbo2XlWjUoz1zecnBYQ13mngvRTNQo/edit?usp=drivesdk) |

## 2. Participants

| Name | Role | Confidence |
| :--- | :--- | :--- |
| Dr. Rami Khouri | Host / domain expert (clinical + product/AI) | N/A |
| Yaron Goren | External advisor / consultant | N/A |

## 3. Key Topics

- Case Manager (CM) workflow and division of responsibilities between CM and psychiatrist, Product UI/screen design for the CM experience (what appears on screen and in what order), AI/model evolution: transition from the older Predictics-based approach to transcript-based models, Clinical questionnaires and structured assessments (SCID/MINI)
- including use of guided question sets, Pediatric assessment flow
- including providing CM with a PDF of guiding questions, Operational/meeting logistics issues: audio/connectivity problems and screen-share permission troubleshooting

## 4. Full Transcript

> **Note:** Transcript language matches the original meeting language.

---

```
Yaron Goren (08:00): ‫תודה רבה. Ctar fpv cptv cpx cpx ccpx cpx ctrl r cpx cctrl r ccpx cpx cpx cpx cpx ‫תודה רבה. 
Dr. Rami Khouri (10:17): ‫תודה רבה. ‫שמעתי 
Yaron Goren (10:20): משהו. 
Dr. Rami Khouri (10:22): ‫שמעתי. ‫אני 
Yaron Goren (10:24): מומד בקושר, רגע, ‫אני רוצה להגבר. שלום, שומע? שמעתי משהו. מה שומעתי? אני מראה בקושר, רגע, נעשה להגבר. 
Dr. Rami Khouri (10:28): נדבר 
Yaron Goren (10:28): עוד פעם, או הנה עכשיו אני שומע. אוקיי, 
Dr. Rami Khouri (10:32): נשאר לי המצלמה שנייה. עכשיו אם היה, עכשיו אני שומע. אוקיי, אני שואל מהמצלמה השנייה. תשובים, נהיה. רידיו. ‫בוא, בוא שמים, נתחיל בלי מצלמה. ‫בסדר, אני בכל מקרה... ובכל מקרה. מסך. אז. חזרתי. אני סלוחה עכשיו. יותר. להתמקד. אני. חזרתי. אני. חזרתי. אני. חזרתי. אני. בסוף מסך. טוב, אז חזרתי. אני צריך עכשיו יותר להתמקד. תקשיבי לי קצת, מה היה בפגישה שלך עם נדב ולי, מה הבנת יותר, איזה שאלות יש לך, תשובות. בגדול אני אגיד לך, נתמקד איתך עכשיו, באג'נדה של הסייר. 
Yaron Goren (11:50): בסיר, הייתה לי שיחה מאוד כללית איתן, ‫בעיקר להבין את התהליך ‫של מה הם עושים ‫ומה הם היו רוצים שיהיה שם, ‫ויש לי כזה מין גם התחלה של הבנות וגם שאלות ברמה, ברמות הגבוהות יותר קודם כל, של מה בעצם, מה החלוקת תפקידים בין הקייס מנג'ר לפסיכיאטר, ואיך היינו רוצים שהרעיון של הקייס מנג'ר יתנהל ואחרי זה מה שהם עכשיו מתעסקים בו בגרפית, איך זה ראה על המסך ואז רק אחרי זה יש את ה... אתה יודע, נכנס התוכן של מה רוצים להכניס שם וכאילו יש לי כזה מין... לא יודע כמה זה משהו שכבר ישבתם וחשבתם עליו, או שזה כאילו, אז אני אשמח לשמוע ממך קצת, כאילו הם הסבירו לי פחות או יותר איך הם מבינים את זה, אבל לא לגמרי יושב לי ברור. 
Dr. Rami Khouri (12:47): טוב, אז אני אגיד שהיום אנחנו מציגים ‫ל-CM, ‫אפשר להגיד, במסך הנוכחי ‫יש כזה מין רובריקות ‫שה-CM נכנס למחלה נוכחית, ‫ואז יש לו דיכאון, ושאלות של דיכאון זה הוא מסמן. בהתחלה היה לנו גם את ה-predictics, האלגוריתם הישן, שהם נוצרים סימונים של שאלות מסוימות, ‫וגם הייתי משתמש בסימונים, ‫זאת אומרת, הסימון של האם... ‫לתשובה של השאלה הספקטיפית ‫היה חלק מה-input לפרוט. ‫עכשיו, כשהמודלים התפתחו והתקדמו, ‫ראינו שמספיק הטרנסקריפט בעצם. ‫לא צריך להכניס למודל מה שאלתי ומה המטופל ענה. אז החלק הזה של לסמן במסך, הוא הופך להיות פחות רלוונטי. פחות רלוונטי כשאנחנו מדברים על יוצרת החיקור. עכשיו נגיד בילדים המשכנו את זה והצגנו ל-CM מסמך, PDF של שאלות מנחות. זה בעצם הקונספט בגדול של להקפיג את השאלות, שאלות מנחות. שהשאלון הזה הוא בנוי על רעיון פסיכיאטרי. אפשר להגיד שזה מין כזה שילוב של משהו מותאם אישית על סמך סקיד או המיני. כשסתכלתי שם, כל מיני עשיתי שינויים לזה, אבל זה אותו העיקרון, זה רעיון פסיכיאטרי שבודק סימפטומים, והוספתי לזה את החלק של ההתפתחות, רקע, כאילו שאלות כלליות, ‫ממש אין... קונספטואלית, ‫אין שאלות חדשות. ‫זאת אומרת, המחשבה עכשיו, ‫מהמעבר כאילו למודל החדש, ‫זה להשתמש באינפוט ‫שיש לנו בשאלון, ‫ולהמשיך כאילו משם. ‫בשתי סיבות. ‫אחד, זה יכול להיות יותר נכון וחכם, זה יעזור לנו לנצל את הזמן. עדיין, הרבה פעמים מתופלים היום את העצבינים, מסמלים נגיד, משהו בשאלון, ואתה שואל, כאילו אתה מלאתי את השאלות. אז מה שההשאלה שלי הייתה, ‫אני אשתף שנייה את ה... ‫מה קורה פה? ‫שזה לא יבקש... ושזה לא יבקש, אני מנסה לגבי הרשאה, טוב, אני מצטרך להצלצת ולהיכנס, כדי לתת הרשאה לזום, לשתף מסך, אני גם חושב חדש, אז אני יוצא ונכנס, בסדר? אז אני עוצר אני חושב שזה
```