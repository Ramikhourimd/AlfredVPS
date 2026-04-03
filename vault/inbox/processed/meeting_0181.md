---
alfred_tags:
- meetings
processed_at: '2026-02-26T20:19:30.988127+00:00'
status: processed
---

# Meeting: Innovation Team | Jun 26, 2025 (Transcript)

---

## 1. Meeting Details

| Field | Value |
| :--- | :--- |
| **Date** | 2025-08-02T00:40:12.890Z |
| **Title** | Innovation Team | Jun 26, 2025 (Transcript) |
| **Classification** | {\"meeting_id\":\"HM-STAV-WEEKLY\",\"meeting_name\":\"Meeting with Stav\",\"confidence\":0.82,\"confidence_level\":\"HIGH\",\"category\":\"HealthyMind Clinical Operations\",\"is_active\":true,\"is_new_suggestion\":false} |
| **Category** | HealthyMind Clinical Operations |
| **Meeting Type** | HM-STAV-WEEKLY |
| **Source Document** | [https://docs.google.com/document/d/1DMlIfOdOUsozyg3btggEohfhjHRHT_k5c1yqLPRZ1hA/edit?usp=drivesdk](https://docs.google.com/document/d/1DMlIfOdOUsozyg3btggEohfhjHRHT_k5c1yqLPRZ1hA/edit?usp=drivesdk) |

## 2. Participants

| Name | Role | Confidence |
| :--- | :--- | :--- |
| Dr. Rami Khouri | N/A | 0.97 |
| Stav Zamir | N/A | 0.92 |

## 3. Key Topics

- AI agent architecture and workflow planning
-  Prompt engineering and prompt iteration workflow
-  Grader/evaluator design for prompts and outputs
-  PromptHub usage and dashboard/monitoring needs
-  Dashboard building and “vibe coding” tools (Lovable/Base44)
-  Clinical summary improvements (including removing the trauma section for Maccabi patients)
-  Workload and scheduling balance between clinic responsibilities and innovation work
-  Mentions of related collaborators and tasks (Ahmad on dashboard
-  Shachar on prompts
-  Shira clinic ops
-  David external AI consulting)

## 4. Full Transcript

> **Note:** Transcript language matches the original meeting language.

---

```
Dr. Rami Khouri (15.31): היי סתיו 
Stav Zamir (26.2): שמעים אותי? 
Dr. Rami Khouri (27.95): אנחנו שומעים אותך 
Stav Zamir (30.76): אני לא רואה אתכם 
Stav Zamir (38.25): עכשיו. 
Dr. Rami Khouri (41.69): נשמע. 
Stav Zamir (43.79): בסדר. שלומכם. 
Dr. Rami Khouri (47.72): בסדר. 
Stav Zamir (51.01): שחוזרים לשגרה. 
Dr. Rami Khouri (54.56): כן. 
Dr. Rami Khouri (57.11): בינתיים. 
Stav Zamir (59.03): בינתיים אתה אומר. מעניין. 
Dr. Rami Khouri (66.1): עד שביבי ירד תשוב פעם בזכרון. 
Stav Zamir (70.14): נכון. 
Dr. Rami Khouri (72.89): טוב, אז 
Dr. Rami Khouri (75.41): תעזור לשנייה, אני פשוט, 
Dr. Rami Khouri (78.97): עם המון דברים במקביל בראש, איפה עצרנו פעם אחרונה? 
Stav Zamir (83.98): אז בדיוק עברתי על הסיכום של הפגישה, 
Stav Zamir (87.32): דיברנו על... 
Stav Zamir (92.88): גם על בדיקת האמינות לאינטקים של ה-CM, 
Stav Zamir (99.77): רגע נעלמתם לי, אוקיי, 
Stav Zamir (103.83): ודיברנו על המודל ריזונינג, תארת אז 
Stav Zamir (115.62): על הפרויקט של השיווק, של הוציא להם דאטה. כן, זה עשיתי. 
Dr. Rami Khouri (126.71): אני לא אכניס אתכם בינתיים לזה כי זה קצת מסובך אבל סיימתי את זה 
Dr. Rami Khouri (139.3): יצא לך קצת להיכנס ל-pwnthub להבין 
Dr. Rami Khouri (146.94): מה... 
Stav Zamir (148.1): זהו, זה הייתי אמורה לחשוב על איך לשפר את הגריידר שבניתי, ולא כל כך יצא לי להתעסק בזה, 
Stav Zamir (159.48): אני יודעת לתעסק בזה היום אחרי הפגישה שלנו. 
Dr. Rami Khouri (167.72): אולי קצת קפצנו לנושא של הגריידר, לפני שבאמת 
Dr. Rami Khouri (174.26): אפיין מה צריך לשפר ואיך. 
Dr. Rami Khouri (179.17): שכדאי שלב ראשון 
Dr. Rami Khouri (183.88): לעשות צוות שוב לרשום 
Dr. Rami Khouri (189.5): שגם בפובץ ששלחתי לך וגם 
Dr. Rami Khouri (193.04): שינו תבלאות שמציגות את כל הפרומטים לפי 
Dr. Rami Khouri (199.85): אז ממש כזה כל הפלואו קליני שלנו 
Dr. Rami Khouri (204.24): מה יש שם איפה. 
Dr. Rami Khouri (207.18): נכנס מה הוא מקבל מה הוא מאבד איך ומה הוא מוציא 
Stav Zamir (213.11): כתמונה 
Dr. Rami Khouri (213.57): פרלית 
Dr. Rami Khouri (216.01): ואז כמו שעשינו פה כל אחד מה 
Dr. Rami Khouri (220.32): נקרא לזה שלבי כניסה של האיי 
Dr. Rami Khouri (225.79): הוא בעצם פרויקט 
Dr. Rami Khouri (228.3): שהפרויקט הזה צריך אפיון 
Dr. Rami Khouri (235.01): שבעצם האפיון הוא כולל וגדול, 
Dr. Rami Khouri (242.32): לכל אחד נקרא 
Dr. Rami Khouri (244.42): agent, בסדר? אז 
Dr. Rami Khouri (247.04): מה שמאפיין agents זה שהם 
Dr. Rami Khouri (250.79): מרגישים את הסביבה, 
Dr. Rami Khouri (255.07): עושים פעולה 
Dr. Rami Khouri (257.86): ונותנים תוצאה. אם נגיד agent הוא... 
Dr. Rami Khouri (264.98): גלי השן 
Dr. Rami Khouri (266.76): אז הוא בודק 
Dr. Rami Khouri (268.62): אם יש השן ונותן התוואה 
Stav Zamir (272.88): זה 
Dr. Rami Khouri (273.24): בגדול האפיון של agent agent 
Dr. Rami Khouri (278.04): זאת מכונה שיש לה יכולת 
Dr. Rami Khouri (284.23): לבדוק משהו 
Dr. Rami Khouri (286.4): ולתת משהו בחזק עכשיו יש agents שהם 
Dr. Rami Khouri (291.2): שקוראים להם operators אופרטור זה לא רק שהוא יכול לאבד ולתת תוצאה של ריבוד, אלא יכול לבצע פעולה פוטשי. אנחנו לא שם 
Dr. Rami Khouri (307.26): עדיין אבל אם נתקלתם במונח operator זה סוג קצת משוכלל של agent. 
Dr. Rami Khouri (315.99): אם אנחנו קוראים לכל פרויקט כזה agent 
Dr. Rami Khouri (320.09): אז צריך באמת להגדיר מה הסביבה שהוא עובר. 
Dr. Rami Khouri (326.77): מה האינפוטים שלו 
Dr. Rami Khouri (329.4): מה הוא עושה. 
Dr. Rami Khouri (331.0): ובלי להיכנס עדיין לפרומטור מה הוא עושה ומה הוא נותן עכשיו אם מבינים טוב 
Dr. Rami Khouri (340.27): מה. 
Dr. Rami Khouri (348.12): מה הפרפס של האג\'נט עצמו אז יותר קל אחר כך לבוא ולבנות את הגריידר. 
Dr. Rami Khouri (357.17): כאילו בהתחלה לבנות את הגריידר כי. 
Dr. Rami Khouri (361.87): מן 
Dr. Rami Khouri (363.27): סכמה כזאת שכמו שיש נגיד למי שבודק בגרויות אז שולחים לו תופס אתה נותן ציון אם יש אם חסר ככה 
Dr. Rami Khouri (374.84): אז לבנות כזה 
Dr. Rami Khouri (378.3): ואז אנחנו נהפוך אותו לגרדר יהיה הרבה יותר קל מלהתחיל. במה זה גרדר ואיך מה זה סכמה של פי של 
Dr. Rami Khouri (387.73): ג\'ייסון בכל הדברים. 
Dr. Rami Khouri (394.5): עכשיו אני חושב אם הפרומטאב סביבה נוחה לעבודה או שעדיף אולי כן לבנות איזשהו דשבורד שהוא יותר. איך כשאת נכנסת לפרוג\'קט כאילו בסופו העבודה עצמה תהיה בפרומטאב אבל מבחינת מעקב מבחינת משהו שיהיה ויזואלית יותר קל. לעקוב אחרי העבודה שלנו. 
Stav Zamir (430.31): יכול להיות שאפשר 
Stav Zamir (432.69): לחשוב על משהו פשוט יותר, כאילו זה לא מסובך כל כך, אבל אני עוד לא מרגישה שאני לגמרי... 
Dr. Rami Khouri (444.27): ככה, 
Dr. Rami Khouri (446.26): המשימה שלך מתהיה 
Dr. Rami Khouri (448.63): לבנות 
Dr. Rami Khouri (450.94): דשבוט כזה. 
Dr. Rami Khouri (454.39): כאילו אתר 
Dr. Rami Khouri (456.19): שבלנו 
Dr. Rami Khouri (458.57): דרך לבאבי. 
Dr. Rami Khouri (461.08): את מכנת לבאבי? לא. אז לבאבי בגדול בגדול לפני שאנחנו 
Dr. Rami Khouri (470.69): פשוטי העם השתלטנו על הפיתוח. 
Stav Zamir (474.89): מי 
Dr. Rami Khouri (475.1): שרצה לבנות אפליקציה אתר כל ממשק 
Dr. Rami Khouri (480.69): שעובד על תוכנה. 
Dr. Rami Khouri (483.42): אז בגדול מחלקים את העבודה בין back-end וfront-end. 
Stav Zamir (489.51): נכון. 
Dr. Rami Khouri (492.51): מי שהיה בfront-end זה כל מהצווי ה-UX, ובבק-אנד יש את המתכנתים. 
Stav Zamir (499.77): עכשיו, 
Dr. Rami Khouri (501.9): Lavabelle זאת פלטפורמה שאת יכולה לדבר איתה, 
Dr. Rami Khouri (507.23): יש שם מודל שפה, והוא כותב את הקוד. 
Dr. Rami Khouri (512.84): עכשיו הוא כותב את הקוד 
Dr. Rami Khouri (516.54): והופך אותו לממשק. 
Stav Zamir (521.41): אם 
Dr. Rami Khouri (521.53): את אומרת לו תבנה לי 
Dr. Rami Khouri (525.79): יומן כזה שמתעדכן, 
Dr. Rami Khouri (529.15): רקע בצבע צהוב, 
Dr. Rami Khouri (531.98): אז הוא ממש מתחיל לבנות, ואת יכולה 
Dr. Rami Khouri (536.12): לדבר איתו ואלה שם. עכשיו החיסרון היחיד בממשק הזה זה שאת לא יכולה... 
Dr. Rami Khouri (543.24): לשנות 
Dr. Rami Khouri (546.22): בממשק עצמו החיצוני מה שאת יכולה לעשות או להגיד לו תשנה נגיד אם יש משפט 
Dr. Rami Khouri (554.08): שאת רוצה להוריד אות אז או שאת אומרת לו מהמשפט הזה תוריד את האות הזאת כאילו אין לך גישה באמת להרנדה או שאת פותחת את הקוד ומשנה שם 
Dr. Rami Khouri (569.24): זה בגלל שזה נו קוד זאת המגבלה של הנו קוד 
Dr. Rami Khouri (574.62): אבל בגדול בגדול הפלטפורמות האלה ישתברות זה נקרא וייב קודינג יש תל אבאבל יש בייס 44 שזה אחר כך זה סטארטאפ ישראלי ובולט. 
Dr. Rami Khouri (588.29): אלה שלושת הפלטפורמות הכי 
Dr. Rami Khouri (591.97): שכיחות לוייב קודינג. 
Dr. Rami Khouri (596.84): ואפשר לעשות שם הרבה דברים נחמדים. באמת מאוד שימושיים. 
Stav Zamir (607.54): כן אני רואה שיש להם טמפלטים וכאלו. 
Dr. Rami Khouri (610.95): כן. 
Dr. Rami Khouri (616.29): בהזדמנות אני אראה לכם באמת דברים שעשיתי שממש נחמדים, אבל 
Dr. Rami Khouri (623.93): אני אעבוד עם אחמד על לבנות פלטפורם. 
Dr. Rami Khouri (628.48): זה יהיה דשבורד שהמטרה שלו זה ממש לתת לנו מין ראיית 
Dr. Rami Khouri (639.96): איגל ויז\'ן 
Dr. Rami Khouri (641.96): של הכל 
Dr. Rami Khouri (643.8): והיכולת להיכנס פנימה 
Dr. Rami Khouri (647.83): ולסמן עבדתי על זה היא לא תהיה 
Dr. Rami Khouri (652.0): מקושרת לפרומטאב כי אני עדיין לא יודע איך להשתמש ב API של הפרומטאפ, 
Stav Zamir (660.7): ואני 
Dr. Rami Khouri (660.95): לא חושב שזה הדמיין להתעסק עם זה, אבל אנחנו נסמן שם, עבדנו על זה, עבדנו על זה, 
Dr. Rami Khouri (668.74): דברים כאלה. אפשר גם לקשר אותה לפגישות שלנו, ואז אחרי כל פגישה יהיה סיכום, וזה יעדכן שם את המשימות לבד, נוכל לשפר את זה תוך כדי, אבל הכוונה כרגע, זה באמת שזה ייתן לנו איזשהו סכמה לעבוד. 
Stav Zamir (686.85): כן. 
Dr. Rami Khouri (689.37): ומה שאני צריך ממך 
Dr. Rami Khouri (692.13): זה 
Dr. Rami Khouri (693.5): לכל פרויקט 
Dr. Rami Khouri (696.1): ממש לבנות אפיון, 
Dr. Rami Khouri (702.34): לתת שם לאג\'נט הזה. אני חושב שעשיתי את זה אולי באופן נעקיף בתוך המסמך. או בתוך התבלעה אפשר להוציא משם את כל הרקע, תכל\'ס אפשר לשים את כל הקבצים שיש לנו לתוך שאד ג\'י פי טי ולבקש ממנו לכתוב את זה, 
Dr. Rami Khouri (723.39): אבל החלוקה היא ההגדרה, מה הוא עושה, 
Stav Zamir (731.41): ואז 
Dr. Rami Khouri (732.02): את הפרומט עצמו, 
Dr. Rami Khouri (739.03): אימפוט ואוט. 
Dr. Rami Khouri (746.11): בסוף אחרי שאת מכינה את זה 
Dr. Rami Khouri (751.58): לכתוב בעצם אנחנו צריכים שני דברים. אתם צריכים איזה זה אהלט פוט 
Dr. Rami Khouri (759.72): איך נראה דוגמה למשהו טוב 
Dr. Rami Khouri (766.03): ו. 
Dr. Rami Khouri (773.07): אבל 
Dr. Rami Khouri (786.03): לא חייב להיות. 
Dr. Rami Khouri (790.01): אבל כן לגעת בדברים העיקריים שלפחות מופיעים בפרומט עצמו כשפרומט כתוב מה אומרים לו תבדוק ככה. 
Dr. Rami Khouri (803.79): נעבוד 
Dr. Rami Khouri (807.91): על הקרייטריה, 
Dr. Rami Khouri (810.09): נדייק אותם, 
Dr. Rami Khouri (812.55): ואז אחרי שנסיים נכתוב את הסקורינג. 
Dr. Rami Khouri (817.69): כשיהיה לנו קרייטריה מדריך לסקורינג, 
Dr. Rami Khouri (822.92): הכי פשוט זה להכניס את הכל, ל-GPT ולהגיד לו תכתוב לי פרומט לגריידר. 
Dr. Rami Khouri (837.45): לא משנה אם סכימה איך 
Stav Zamir (838.47): שאנחנו. בסביב זה אני צריכה בעצם את הטבלה 
Stav Zamir (842.31): ולעבור כאילו שלב שלב 
Stav Zamir (845.85): ולאפיין כל agents כאילו כל 
Stav Zamir (851.52): זמן שהAI נכנס לפלור. כן 
Dr. Rami Khouri (856.4): אז פה יש את הזלה מהgoogle docs ששילים. כן מה שיש ביישבו גוגל דוקס 
Dr. Rami Khouri (864.74): שלחתי לה. 
Stav Zamir (866.92): מה יש את מה? 
Dr. Rami Khouri (869.72): גוגל דוקס שמפרט את כל. 
Stav Zamir (873.89): כן הטבלה של הפרומט ליסט. 
Dr. Rami Khouri (877.87): לא יש שתי טבלו. 
Stav Zamir (880.01): גוגל דוקס שאתה כתב כן כן כן. 
Dr. Rami Khouri (883.15): אוקיי אז יש את הגוגל הזה ו... 
Dr. Rami Khouri (889.45): ויש 
Dr. Rami Khouri (891.29): שתי שיטס, 
Dr. Rami Khouri (893.27): אחד קליסט ואחד פרומץ משהו כזה, שבגדול הם דומים, 
Dr. Rami Khouri (899.42): ניסינו לסדר לעשות מן גרסה שופרת 
Dr. Rami Khouri (904.15): של הפרומפט ליסט 
Dr. Rami Khouri (906.17): ונתקענו בדרך 
Dr. Rami Khouri (912.15): אז תשתמשי במה שיש שם 
Dr. Rami Khouri (915.9): לנו יש מוצא וואטסאפ? לא. נסכים לצאת וואטסאפ ובוא נעשה גם תוך כדי. 
Stav Zamir (927.36): לא 
Dr. Rami Khouri (927.49): יודע אם יש שאלות, אם יש, 
Dr. Rami Khouri (937.48): שזה השלב הראשון, במקביל, 
Dr. Rami Khouri (942.36): מה שכן יכול לעזור לך לשפר את הקריטיריה, 
Dr. Rami Khouri (949.27): זה לבדוק בשטח, לפחות פידבקים על הסיכום, 
Dr. Rami Khouri (958.71): כאילו עכשיו אנחנו לוקחים את הפרומט. 
Dr. Rami Khouri (967.02): זה הדבר. אז אם תחלת לעשות את 
Dr. Rami Khouri (973.24): זה או אם תחלת לעשות את זה יש לך פגישות כבר קבעת זה זה. פשוט תסדרי את זה במקום מסוים שיהיה לנו את הדאטה הזה. 
Stav Zamir (985.31): ראית את מה ששלחתי לך שיש בינתיים לגבי הפגישות עם כאילו כי התחלתי קצת. 
Dr. Rami Khouri (995.27): כל נכון אני זוכר ש... כאילו 
Stav Zamir (999.38): יש כמה הערות אז 
Stav Zamir (1001.65): בינתיים סידרתי את זה בגוגל דוקס כזה לפי 
Stav Zamir (1006.02): מה שהם אמרו 
Stav Zamir (1009.65): אבל אני חושבת גם איך לסדר את זה שיהיה לנו נוח. 
Dr. Rami Khouri (1014.4): סבבה, 
Dr. Rami Khouri (1015.88): לשניכם יש גישה ל-GPT של החגלה? כן, 
Stav Zamir (1020.53): לי 
Dr. Rami Khouri (1020.67): יש. 
Dr. Rami Khouri (1021.93): לי יש שלך, זה אותו לך? לא, לא, עדיף שנעבוד על ה... 
Dr. Rami Khouri (1028.65): אני צריך לעבור. 
Dr. Rami Khouri (1031.92): אני גם לא... שיהיה 
Stav Zamir (1034.24): שלך תשענות שאי אפשר, 
Stav Zamir (1037.92): כאילו לרקד שם את ה... 
Stav Zamir (1043.08): תדברו עם שלון. 
Dr. Rami Khouri (1045.85): אני כנס. 
Dr. Rami Khouri (1077.24): יש לך את המשתמש והססמה בשלום? 
Stav Zamir (1082.78): אני אבדוק, נראה לי שלי שלחה לי ואז אני 
Stav Zamir (1103.84): מעבירה לך. 
Dr. Rami Khouri (1133.13): תודה. 
Dr. Rami Khouri (1135.38): לי. 
Stav Zamir (1138.74): מה? 
Dr. Rami Khouri (1140.54): שמי יש גישה למייל הזה? לי. 
Stav Zamir (1143.29): אה כן. אה זה דורש אימות. 
Stav Zamir (1150.29): כן אני מאמינה שהגישה אצלה. 
Dr. Rami Khouri (1182.56): אנחנו נפתח שם פרויקט 
Dr. Rami Khouri (1185.32): לנו, 
Dr. Rami Khouri (1187.11): ואחזיר לאט גם 
Dr. Rami Khouri (1191.53): להשתמש מדי פעם ב-O3 Pro, 
Stav Zamir (1196.36): זה 
Dr. Rami Khouri (1196.47): עדיין פרו, 
Dr. Rami Khouri (1227.24): אה לא, אני אמפור צמחלן. זה עייפ למון. 
Dr. Rami Khouri (1243.9): טוב, כן, בכל מקרה, 
Dr. Rami Khouri (1
```