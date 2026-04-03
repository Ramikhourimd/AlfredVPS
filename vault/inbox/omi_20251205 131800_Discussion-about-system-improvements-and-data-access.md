---
alfred_tags:
- business/strategy
- healthcare/scaling
category: business
created: '2025-12-05T15:18:00'
from: Omi Recording
input_type: transcript
omi_session_id: 36
received: '2025-12-05T15:18:00'
relationships:
- confidence: 0.75
  context: related strategic discussions
  source: inbox/omi_20251205 131800_Discussion-about-system-improvements-and-data-access.md
  target: inbox/omi_20260310 103001_Strategic-Model-For-Scaling-Psychiatric-Services.md
  type: related-to
- confidence: 0.75
  context: related strategic discussions
  source: inbox/omi_20251205 131800_Discussion-about-system-improvements-and-data-access.md
  target: inbox/processed/omi_20251204 172103_A-strategic-discussion-on-company-goals-financial-targets-an.md
  type: related-to
- confidence: 0.75
  context: related strategic discussions
  source: inbox/omi_20251205 131800_Discussion-about-system-improvements-and-data-access.md
  target: inbox/processed/omi_20251204 172103_A-strategic-discussion-on-company-goals-financial-targets.md
  type: related-to
- confidence: 1.0
  context: raw and processed versions
  source: inbox/omi_20251205 131800_Discussion-about-system-improvements-and-data-access.md
  target: inbox/processed/omi_20251205 131800_Discussion-about-system-improvements-and-data-access.md
  type: related-to
- confidence: 0.75
  context: related strategic discussions
  source: inbox/omi_20251205 131800_Discussion-about-system-improvements-and-data-access.md
  target: inbox/processed/omi_20260310 103001_Strategic-Model-For-Scaling-Psychiatric-Services.md
  type: related-to
source: omi
status: unprocessed
tags:
- omi
- business
type: input
---

# Discussion about system improvements and data access

**Source:** Omi (limitless)
**Date:** 2025-12-05 15:18:00
**Category:** business
**Emoji:** 🧩

## Summary

The user and another speaker discuss priorities for improving their clinical management/CRM systems over the next six months, focusing on what is critical versus nice-to-have. They identify two main tracks: (1) immediate needs in the current Retool-based system, mainly KPI reporting and possibly fixing login issues for therapists whose sessions are disrupted, and (2) planning the design and UI of a new system and potential functional additions. A major operational issue raised is problematic Microsoft Teams-based video sessions that contribute to patient no-shows and lost revenue; they consider either switching to Zoom or integrating video directly into the app, possibly by hiring an external contractor for a 3–4 month project. The user notes that budget is less of a constraint due to growth. They agree the user will compile a prioritized list of critical requirements (for psychiatrists, clinic staff, and secretaries) and hold discussions with various teams (e.g., Rena, the clinic staff) to refine feature needs. On the data side, they clarify that all columns from the legacy system are present in BigQuery, but questionnaire data and meeting text content are not fully replicated; text data is stored in a separate database table and is not directly accessible to the user yet. The user requests stable, self-service access to these texts instead of ad-hoc requests, and the other speaker agrees to find a secure way to provide it. The user plans to review what data exists in the database before coming back with more precise requests.

## Action Items

- [ ] Prepare list of critical Retool requirements for first six months
- [ ] Create prioritized list of issues including Teams no‑show problem
- [ ] Coordinate meetings with Renée, the team, and the clinic to gather requirements
- [ ] Review database to see which data and texts exist and are missing
- [ ] Get direct access solution to meeting text data instead of requesting each time

## Transcript

**SPEAKER_01:** כן, אני לא צריך מה עם כל השאר? כל הדברים שכתבת לי בזמנו אז בוואטסאפ? כל הדברים שבגדול אני כן רוצה כלים שאתה יודע, שיעזרו, שיהיה יותר נוח לפסיכיאטרים. אבל זה לא קריטי מבחינתי כרגע. אני יכול עם קצת עבודה ידנית, מה שנקרא, גם לשפר את הפרומפטים, גם זאת אומרת לא צריך פיצ'רים חדשים.
**SPEAKER_01:** אה אני מדבר רגע על ה על המערכת ניהול תיקים. אבל ב CRM אני באמת צריך לבדוק. לא הטמעתי מה כן, מה לא, מה בתוכנית.
**SPEAKER_02:** לא, אבל נראה לי אבל זאת העבודה שאנחנו צריכים לעשות, כאילו להחליט.
**SPEAKER_02:** כאילו, מבחינתי יש עכשיו שני טרקים.
**SPEAKER_02:** מה קריטי לך בחצי שנה הראשונה במערכת של ה Retool?
**SPEAKER_02:** ואם אני מה שאני שומע ממך שזה בעיקר בעיקר זה KPI. ואז בוא נגדיר איזה KPI ומה מה קריטי ומה צריך לעשות שם. אה אם יש עוד דברים שצריכים חייבים לעשות. בוא נגיד אני נגיד חשבתי בהתכתבות עם ה עם ה עם המטפלים וזה, יש לנושא של הלוגין שהם נתקע להם המערכת כל פעם בגלל הלוגין. כאילו אז אני חשבתי שאת זה צריך לסדר כאילו כי זה אפשר לסדר את זה. זה זה לא מעט עבודה, אבל כאילו חשבתי שכן שווה לסדר את זה. לא יודע, תגידו אתם אם זה אם זה קריטי או לא.
**SPEAKER_02:** אה כן. ואם יש עוד דברים. אה כאילו אני צריך פרק אחד של מה קריטי לך שנעשה על ה Retool אה לבשביל עד יוני. אה האמת היא פרק שני זה מה זה אולי אנחנו צריכים לעשות ביחד אבל.
**SPEAKER_02:** אבל איזה שיפורים אנחנו כבר רוצים לעשות במערכת החדשה מראש? כאילו אתה יודע, בגלל שאני בונה מחדש, אז נגיד אם רוצים שה UI יראה אחרת או זה, אז כדאי אני זה כבר לא שינוי, זה פשוט נבנה את זה ככה מראש. זה אותה עבודה בשבילי. כאילו לנסות לחשוב מה מה איך רוצים שהמערכת החדשה תראה בכלל. אה ואז דבר שלישי זה תוספות ל תוספות כאילו פונקציונליות על על ה שכבר נעשה במערכת החדשה אה מעבר למה שיש היום.
**SPEAKER_01:** הבנתי. זה אני בטוח שיש דברים שהם שהם כן קריטיים ו ושזה עם הגדילה ומספר מטופלים זה יהיה בעייתי. אני יודע אני חושב עכשיו על ה Teams. אני חושב שזה משהו שצריך למצוא לו פתרון, או שעוברים לזום או שאם יש פתרון קל יחסית להכניס את זה לתוך ה בתוך האפליקציה. אה לא יודע.
**SPEAKER_02:** כן, או שאלה אם זה נראה לך קריטי לפחות החצי לא יודע, באיזה שלב זה, באיזה עדיפות זה.
**SPEAKER_01:** ה Teams בעייתי, אני אגיד לך למה. החלק מהנו שו זה בגלל מטופלים שמתעכבים בכניסה בגלל בעיה. עכשיו נו שו, שתבין, אנחנו משלמים חצי מהבדיקה ואנחנו בזמן הזה היינו יכולים להכניס כסף. זאת אומרת, משהו כמו 10% או קצת יותר אה מפוטנציאל הכנסה או אפילו רווח רווח גולמי הולך. עכשיו ברור לי שיש עוד עוד דברים שמשפיעים על הנו שו. אה אבל זה אחד מהם.
**SPEAKER_02:** אז בוא אז בוא בוא נשים את זה, בוא נשים ברשימה ונעשה דיון. אתה יודע, נגיד זה משהו לפתור את הבעיה הזאת, זה בכסף אפשר לפתור. זה אולי יקח לו בטח שלושה ארבעה חודשי עבודה, אבל אפשר לקחת קבלן, מישהו שיפתור לנו את הבעיה הזאת.
**SPEAKER_01:** כן, אני מבחינתי כסף זה פחות בעיה כרגע, כי עם גדילה כזאת אפשר לשים.
**SPEAKER_02:** כן, אז בוא אז בוא אני אומר בדיוק אז צריך את הרשימה הזאת. אה ולעשות על זה דיון ולראות ואז לעשות תוכנית עבודה.
**SPEAKER_01:** סבבה. אז זה הבדל לעשות את זה, אני צריך לעשות את זה גם עם הקליניקה, גם עם הזה.
**SPEAKER_02:** כן, אותו דבר נראה לי אם אם יש דברים קריטיים למזכירות. אם יש.
**SPEAKER_01:** ותאמת שסתיו התחילה לעשות. יש לי חלק אבל.
**SPEAKER_02:** יש לא כאילו להגיד מה הדברים הארבע.
**SPEAKER_01:** אני לא שומע אותך.
**SPEAKER_02:** שנה ראשונה, אז אולי בחצי שנה אחרי זה, בחצי שנה.
**SPEAKER_01:** מה?
**SPEAKER_01:** אתה מקוטע.
**SPEAKER_02:** אני נראה לי בסדר, נראה לי שהבנת. כן, כן, נראה לי שהבנתי.
**SPEAKER_02:** כן, אתה תנסה לחשוב על זה. בסדר, נראה לי שצריך להמשיך לעבוד את זה כאילו אני שאתה צריך לעבור עכשיו בראש של מה הדברים שאתה לא יכול לחיות בלעדיהם בחצי שנה הראשונה.
**SPEAKER_01:** שאלה, יש יש עוד דברים שנמצאים, נגיד נתונים שיש אותם בקסנו ואין אותם בביקוורי, נכון?
**SPEAKER_02:** אה לא. זאת אומרת הכל נמצא בזה, אמרתי לך לא כל הדאטה של השאלונים, אבל מבחינת העמודות הכל נמצא.
**SPEAKER_01:** הכל נמצא. אז מה שחסר לי בינתיים, מה ש נגיד שמה בדוקס הID קיים, אני יכול להגיע אליו, אבל קבצים אין לי גישה אליהם.
**SPEAKER_02:** כן, זהו, אני די ירדתי לקבצים. יש האמת היא הטקסטים לא נמצאים בביקרי, אבל כמובן שכל הטקסט
**SPEAKER_01:** איפה, איפה זה נמצא?
**SPEAKER_02:** יש טבלה של מיטינג טקסט, כאילו.
**SPEAKER_02:** אני לא מעתיק את, אני לא מעתיק את הדטה הזה לביקרי, גם מבחינת סקיוריטי וגם מבחינת כמויות, אבל
**SPEAKER_01:** כן, ראיתי. שם יש כאילו מזהה של של הקובץ. שאלה איפה הקובץ נמצא.
**SPEAKER_02:** לא, אני כבר לא שומר את זה בקבצים. הקבצים שם זה יותר ישן. אני שומר את זה ממש בטקסטים בדטאבייס. לא משנה, אני יכול לתת לך
**SPEAKER_01:** איך אני אתן לך את זה באיזשהי צורה אם תרצה. אז זה מה שחסר לי וזה חשוב.
**SPEAKER_02:** אתה לא יכול לגשת לזה לבד, אבל אני אנסה לתת לך. כן, ברור, אני צריך למצוא לזה פתרון, איך אני יכול לתת לך גישה לזה.
**SPEAKER_01:** פתרון זה לא יהיה בביקרי.
**SPEAKER_01:** כן. כאילו גישה. מה? אני מדבר על גישה לטקסטים ולא שכל פעם אני מבקש.
**SPEAKER_02:** כן, כן, ברור.
**SPEAKER_01:** אה סבבה, אז אני עושה גם, אני מנסה לעשות את זה כדי לא לבוא אליך עם אחרי שבדקתי מה יש ומה אין בדטאבייס. אה וחוץ מזה לגבי הפיצ'רים והפיתוחים, אז אני אעשה אעשה כבר השבוע לעשות כל הפגישות גם עם רנה והבנות וגם בקליניקה, להבין יותר לעומק מה