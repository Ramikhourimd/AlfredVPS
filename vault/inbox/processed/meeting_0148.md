---
alfred_tags:
- meetings
processed_at: '2026-02-26T20:15:09.300123+00:00'
status: processed
---

# Meeting: פגישת ניהול אדמיניסטרציה | May 26, 2025 (Transcript)

---

## 1. Meeting Details

| Field | Value |
| :--- | :--- |
| **Date** | 2025-08-02T00:29:52.954Z |
| **Title** | פגישת ניהול אדמיניסטרציה | May 26, 2025 (Transcript) |
| **Classification** | NEW |
| **Category** | NEW |
| **Meeting Type** | NEW — No known recurring meeting matched |
| **Source Document** | [https://docs.google.com/document/d/1u82xqzlyHdhzofRrL2nUKGTQLvLAKdG3VHPrgDvzZl8/edit?usp=drivesdk](https://docs.google.com/document/d/1u82xqzlyHdhzofRrL2nUKGTQLvLAKdG3VHPrgDvzZl8/edit?usp=drivesdk) |

## 2. Participants

| Name | Role | Confidence |
| :--- | :--- | :--- |
| Dr. Rami Khouri | N/A | 0.99 |
| Shachar Segev | VP R&D | 0.98 |

## 3. Key Topics

* Patient intake/onboarding flow changes: handling 'obligation' (התחייבות/obligation) and 'review obligation' steps; temporary guidance to mark NA when no obligation number exists
* Removing the obligation requirement from the Maccabi intake questionnaire (aligning with Hosneh flow) to reduce friction and improve campaign conversion
* MDH (מד"ח) process: understanding how it works (web/API) and exploring automation/simulation; identifying who has access (Rana, Shira, Ori)
* Operational alignment with Alex and Dekel on guidelines/eligibility: who can be admitted to treatment without an obligation and how to handle patients already in the obligation process
* AI summarization evaluation pipeline: Stav running weekly evaluations; generating a recurring dataset of sessions/patients (target sample ~10–30 per week) for controlled prompt/model comparisons
* Data schema needs for the dataset: ensuring required variables exist (e.g., an 'up to date' column/flag) and including relevant summaries/fields
* Request for KPI/satisfaction tables: pulling a comprehensive table including patient, therapist/psychiatrist, case manager, sections, and free-text fields (weekly cadence starting next month; immediate snapshot acceptable)

## 4. Full Transcript

> **Note:** Transcript language matches the original meeting language.

---

```
Shachar Segev (02:07): מה? 
Dr. Rami Khouri (02:09): כן, שומע. בסדר. תביאו מקסימה? מה זה? תביאו מקסימה? לא, אני 
Shachar Segev (02:28): בא אותו. טוב. 
Dr. Rami Khouri (02:29): אה... אם... עדיף שנעשה את זה אחר כך זה לא כזה דחוף סתם רציתי לדבר על מקום. כל דבר אוקיי. 
Shachar Segev (02:48): עשיתי או אפילו לא הייתי צריך לעשות כלום אבל נראה לי הפתרון הראשוני. כתבתי את זה באימייל. כאילו הבדיקה כאילו צריך לעשות בדיקה במדע. ואז ברגע שמישהו מאושר במדע אפשר לטבל. אז מה שכתבתי להם זה שלא משנה אם הוא כבר הביא אובליגיישן או לא, כל מה שהם צריכים הם צריכים לאשר את האובליגיישן. עכשיו אם הוא לא הביא אובליגיישן, אז שיכתבו NA במספר אובליגיישן, ורק יעשו רביו שמואשר. ברגע שהם אומרים שהוא מואשר והאובליגיישן לא ריק, אז אני מכניס אותו לטיפול. 
Dr. Rami Khouri (03:36): ננתי. 
Shachar Segev (03:39): אז זה עכשיו כשעוד לא ברור מי כן מי לא, זה נראה לי צריך לסגור עם אלכס דקל, את מי מכניסים את מי לא, אבל עקרון מה שהם רוצים להכניס עכשיו לטיפול בלי התחייבות, הם יכולות. 
Dr. Rami Khouri (03:53): סבבה. זאת אומרת מהבחינה הזאת בינתיים. נראה 
Shachar Segev (03:56): אם אנחנו נעשה לו רביו אובליגיישן, ולשים משהו באובליגיישן, נגיד נושא איני שהיה מוסימן של זה, נדע שזה לא באמת כאיבות תחלתי לקבל זימונים. 
Dr. Rami Khouri (04:10): אוקיי. 
Shachar Segev (04:12): זה נראה לי, עכשיו צריך לסגור, נראה לי מה שקצת היה וייק בפגישה עם אלכס ודקל, אני לא הצלחתי להבין מי כן, מי לא, זה נראה לי אתם צריכים לסגור איתם, כאילו את הגייזם. 
Dr. Rami Khouri (04:25): כן. את זה אנחנו נסגור, אני אנסה לדחוף כמה שיותר שזה ייכנס אליי. 
Shachar Segev (04:33): עכשיו ביניים אבל עוד רגע זה נראה לי ייפתח פשוט לכולם בלי התחייבויות וזהו אבל יש לנו אחורה את כל אלה שאחורה שכאילו התחילו להביא התחייבות אני גם לא כל כך מבין למה לא פשוט להגיד להם שמור לא צריך התחייבות וזהו יאללה בואו תתפילו הוא 
Dr. Rami Khouri (04:53): נותן מדי לזהרים למה יעיד 
Shachar Segev (04:56): כן אז זה נראה לי תראו איתם את הגיידליין אולי תדברו אם הבן אדם עוד לא ביקש התחייבות אז אפשר לדלג לו על זה נגיד אם הוא כבר ביקש אז אולי עוד רגע תהיה לו אז זה לא משנה כל כך. 
Dr. Rami Khouri (05:11): אני בכל זאת מטופלים כאלה שהם ביקשו מחכים או מהזה, נסה לדחוף אותם אני מדבר עם אלכס כי באמת חבל על הזמן. השאלה עכשיו בוא נגיד בשלב הבא שבו כל המטופלים יעבור דרך הפלור הזה. בעצם מה שנעשה. באמת 
Shachar Segev (05:36): הצעד, עוד רגע, עוד צעד שאנחנו צריכים לעשות, זה אנחנו צריכים להוריד את ההתחייבות מהתופס של מקאבי, מהשאלון של מקאבי. 
Dr. Rami Khouri (05:43): נכון. 
Shachar Segev (05:44): כי היום, האלה של חוסן, אז הם בלי התחייבות, אנחנו מחכים להתחייבות. אלה של מקאבי, גם, נוריד להם את ההתחייבות, ופשוט נכניס אותם, רק צריכים לבדוק מדך, וכאילו יעשו review obligation ויפניסו אותם הם לא צריכים להביא התחייבות בשביל למלא את השאלון זה מה שהבנתי מאלכס שמי הראשון ליוני. כאילו שסוף שבוע נוריד את ההתחייבויות מהשאלון מקאבי. כן, שזה גם יקל מאוד. כאילו אז הקמפיינים של הדין נראה לי הצליחו יותר. 
Dr. Rami Khouri (06:23): כן, זה משנה משמעותית. 
Shachar Segev (06:27): כן, כן, כאילו אתה לא צריך לעשות כלום, אתה רק צריך מלאות שאלון, כמו שהיה בחוסן. כל המחסום זה רק לבלות שאלון. 
Dr. Rami Khouri (06:37): תגיד, המדח זה וב? 
Shachar Segev (06:42): זהו, זה נראה לי אנחנו צריכים לבדוק איך זה עובד, ואם יש API או שאפשר אולי לעשות לו סימולציה, כאילו באמת אני חושב שהדבר הרבה זה לעשות, לעשות האוטומציה של המדח הזה. למי יש אקסס לזה, לרנה? 
Dr. Rami Khouri (06:57): רנה, שירה, אורי. עשיתם איזה סשן שיראו לי איך זה נראה ואני רואה אם אני יכול להתגבר על זה. בסדר. עוד שני דברים שרציתי לבקש ממוסד, אחד, סתיו תתחיל עכשיו לעשות איבלואציות לסיכומים, כל שבוע, סתיו יש, זה שם שלו, שמוליק. הוא חניף לי פעם דאטה סט מלא לעשרה מטופלים ולשלושים מטופלים. אני צריך כזה כל שבוע. זאת אומרת, מטופלים שעברו... כאילו, כשאתה 
Shachar Segev (07:46): עבור על הדאטה סט הזה, כאילו, לפי זה היית... 
Dr. Rami Khouri (07:50): כן, אנחנו פלוט נריץ את זה. יש שתי בדיקות שאנחנו נעשה. אחת. בדיקה שוטפת כל הזמן כדי לבדוק אם אותו פרומט, אם אפשר לשפר אותו, או נעשה בדיקות בין פרומטים שכל הזמן כזה נבחר לנו פרומטים באופן, כאילו נעשה שינויים מבוקרים, ובין מודלים. עכשיו העניין הוא שבא... 
Shachar Segev (08:26): איך אתה כאילו מה 30 כאילו מה ששמו לי קצת להריץ 30 כאלה או ש... אה... 
Dr. Rami Khouri (08:37): אני לא זוכר אז לפי איך הוא בחר את ה30 אתה לא או ש... אז מה שאמרתי לו זה היה קצת אקראי אבל אני לא זוכר אם שם כאילו... 
Shachar Segev (08:45): לא אתה עומדת לא 30 
Dr. Rami Khouri (08:46): כל פעם. לא לא אני צריך את לא 30 אני צריך את כל המטופלים. הרי הטבלה הזאת היא לפי פנישה את כל הפגישות שהיו במהלך השבוע הזה כל 
Shachar Segev (09:00): המטופלים שעשו פגישות בשבוע האחרון 
Dr. Rami Khouri (09:03): או אתה יודע מה, דגימות אם זה הרבה אז דגימות כי אני צריך משהו שכוון אז כאילו 
Shachar Segev (09:10): כמה אתה 
Dr. Rami Khouri (09:11): רוצה 
Shachar Segev (09:14): לכוון 
Dr. Rami Khouri (09:27): בוא נתחיל מנגיד עשרה, בוא נגיד שלושים. שלושים כל 
Shachar Segev (09:36): שבוע, מתוך אלה שהיו להם פגישות השבוע. 
Dr. Rami Khouri (09:40): כן. 
Shachar Segev (09:42): נשאל לך אם 
Dr. Rami Khouri (09:42): זה פגישות 
Shachar Segev (09:43): קייס מנג'ר או פסיכיאטר או לא משנה. איך הוא 
Dr. Rami Khouri (09:48): שלח לי את זה? זה... לא. הדאטה סט מכיל את הכל. זה לא לשחית פגישה. 
Shachar Segev (09:55): כן, כן, לא, אבל שאני מסתכל... 
Dr. Rami Khouri (09:56): זה לפי מטופל, זה לפי מטופל. 
Shachar Segev (09:59): כן, כן, ברור, אבל אני אקח רק מטופלים שהיו להם פגישות השבוע, השאלה איזה פגישה כל פייש, לא משנה איזה פייש שהייתה להם השבוע, או שנגיד רק פיישת פסיכיאטר השבוע? 
Dr. Rami Khouri (10:13): לא, אני בניתי כאילו בתוך הפרומט הפרוג'קט לכל פרומט, אז אני צריך משהו שיעבוד לי על כל הפרומטים. טוב, לכל המטופל פסדה... 
Shachar Segev (10:24): יש לך את הסיכומים גם של ה... יש לך את כל הסיכומים שלו, נכון? 
Dr. Rami Khouri (10:30): של מי? של 
Shachar Segev (10:32): המטופל הזה. 
Dr. Rami Khouri (10:34): מה שיש לי בדאטה סט זה כל כל כל וריבל שאנחנו משתמשים בו, בכל הפרונטים כל וריבל לא, לא, אתם סיכומים אני יצא אז פה צריך לבין מטופלים 
Shachar Segev (10:55): שיש להם וריבל, שיש להם דאטה 
Dr. Rami Khouri (11:00): כן, אך כבר מה שכחסר לי שם, אמרתי לו, אז לא ידעתנו איך להגדיר לאובריו, כי אני מגדיר לך כל מה שהיה עד עכשיו, אני לא יודע איך אתה עושה את זה. 
Shachar Segev (11:17): סופט, כאילו כמו שאני רוצה את 
Dr. Rami Khouri (11:18): זה לפורט. אז פשוט כן, תעשה לי עמודה וריאבל, לא משנה איך תקרא לו, נגיד, up to date. בדיוק וסבבה 
Shachar Segev (11:42): אוקיי 
Dr. Rami Khouri (11:42): אם יש שם משהו חסר לך והדבר השני אני צריך גם אתה זוכר ביקשתי טבלה של הסביבות רצון עכשיו 
Shachar Segev (11:55): תרף 
Dr. Rami Khouri (11:56): מחודש הבא תיקון שבועי כזה כי אני צריך, אנחנו נושמים KPIs למטפלים, אבל בינתיים, כן, הם צריכים כאילו לעמוד בצבירות רצון במיוצא כזה, אבל בינתיים מה שאני צריך כרגע, זה יכול לחכות ליוני, מה שאני צריך כרגע זה תבלה כמו ששלחת לי פעם שיש בה את הכל, מטופל, פסיכיאל, מי מנתיק. מנהלתי את פסיכיאטר, שלחת לי. זה 
Shachar Segev (12:33): משקל. 
Dr. Rami Khouri (12:34): אוקיי, אז 
Shachar Segev (12:34): מותקן פשוט. 
Dr. Rami Khouri (12:36): מאוד קל, כן. עם כל הסיפים והטקסט החופשי. 
Shachar Segev (12:41): כן, אוקיי. יופי. 
Dr. Rami Khouri (12:45): ציון. תודה שאתה. טוב, טוב, 
Shachar Segev (12:48): וכן. 
Dr. Rami Khouri (12:48): יאללה.
```