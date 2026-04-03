#!/opt/homebrew/bin/python3
"""
Generate Hebrew RTL PDF for Maccabi Clicks Integration Spec v2.0.
Meeting-driven technical specification based on coordination meeting (19 March 2026).
"""
import os, sys, base64
from pathlib import Path
from weasyprint import HTML

SCREENSHOTS_DIR = Path("/Users/ramikhouri/Desktop/Taliaz/maccabi-spec-screenshots")
OUTPUT_PDF = Path("/Users/ramikhouri/Desktop/Taliaz/Maccabi_Clicks_Integration_Spec.pdf")

def img_to_data_uri(path):
    with open(path, "rb") as f:
        data = base64.b64encode(f.read()).decode("utf-8")
    return f"data:image/jpeg;base64,{data}"

def build_css():
    return """
@page {
    size: A4;
    margin: 2cm 2.2cm 2.5cm 2.2cm;
    @bottom-center {
        content: counter(page);
        font-family: 'Arial Hebrew', 'Noto Sans Hebrew', sans-serif;
        font-size: 10pt;
        color: #666;
    }
}
@page :first {
    margin-top: 1.5cm;
    @bottom-center { content: none; }
}
* { box-sizing: border-box; }
body {
    font-family: 'Arial Hebrew', 'Noto Sans Hebrew', 'Noto Serif Hebrew', 'SF Hebrew', 'Arial Unicode MS', sans-serif;
    font-size: 11pt; line-height: 1.7; color: #1a1a1a;
    direction: rtl; text-align: right; unicode-bidi: embed;
}
.cover-page { page-break-after: always; text-align: center; padding-top: 6cm; }
.cover-logo { font-size: 14pt; color: #0077B6; letter-spacing: 2px; margin-bottom: 2cm; font-weight: bold; }
.cover-title { font-size: 28pt; font-weight: bold; color: #0a3d62; margin-bottom: 0.5cm; line-height: 1.3; }
.cover-subtitle { font-size: 16pt; color: #0077B6; margin-bottom: 3cm; line-height: 1.4; }
.cover-meta { font-size: 11pt; color: #555; line-height: 2; }
.cover-meta strong { color: #333; }
.cover-line { width: 60%; margin: 1.5cm auto; border: none; border-top: 3px solid #0077B6; }
.cover-classification { margin-top: 2cm; padding: 0.5cm 1cm; border: 2px solid #c0392b; display: inline-block; color: #c0392b; font-weight: bold; font-size: 12pt; }
h1 { font-size: 22pt; color: #0a3d62; border-bottom: 3px solid #0077B6; padding-bottom: 8px; margin-top: 1.5cm; margin-bottom: 0.8cm; page-break-after: avoid; font-weight: bold; }
h2 { font-size: 16pt; color: #0077B6; border-right: 4px solid #0077B6; padding-right: 12px; margin-top: 1cm; margin-bottom: 0.5cm; page-break-after: avoid; font-weight: bold; }
h3 { font-size: 13pt; color: #2c3e50; margin-top: 0.8cm; margin-bottom: 0.4cm; page-break-after: avoid; font-weight: bold; }
h4 { font-size: 11.5pt; color: #34495e; margin-top: 0.5cm; margin-bottom: 0.3cm; font-weight: bold; }
table { width: 100%; border-collapse: collapse; margin: 0.5cm 0; font-size: 9.5pt; direction: rtl; page-break-inside: auto; }
thead { background-color: #0a3d62; color: white; }
th { padding: 8px 10px; text-align: right; font-weight: bold; border: 1px solid #0a3d62; font-size: 9pt; }
td { padding: 6px 10px; text-align: right; border: 1px solid #ddd; vertical-align: top; }
tr:nth-child(even) { background-color: #f8f9fa; }
.ltr-table { direction: ltr; text-align: left; }
.ltr-table th, .ltr-table td { text-align: left; }
table.mixed td:first-child { direction: ltr; text-align: left; }
.screenshot-container { margin: 0.8cm 0; text-align: center; page-break-inside: avoid; }
.screenshot-container img { max-width: 100%; border: 1px solid #ccc; border-radius: 4px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); }
.screenshot-caption { font-size: 9.5pt; color: #555; margin-top: 6px; font-style: italic; text-align: center; }
.info-box { background-color: #e8f4f8; border-right: 4px solid #0077B6; padding: 12px 16px; margin: 0.5cm 0; border-radius: 0 4px 4px 0; font-size: 10pt; page-break-inside: avoid; }
.info-box strong { color: #0077B6; }
.warning-box { background-color: #fff3cd; border-right: 4px solid #f39c12; padding: 12px 16px; margin: 0.5cm 0; border-radius: 0 4px 4px 0; font-size: 10pt; }
.phase-box { background-color: #f0f7f0; border-right: 4px solid #27ae60; padding: 12px 16px; margin: 0.5cm 0; border-radius: 0 4px 4px 0; }
.decision-box { background-color: #f3e8ff; border-right: 4px solid #7c3aed; padding: 12px 16px; margin: 0.5cm 0; border-radius: 0 4px 4px 0; font-size: 10pt; page-break-inside: avoid; }
.decision-box strong { color: #7c3aed; }
.quote-box { background-color: #f9f9f9; border-right: 4px solid #95a5a6; padding: 12px 16px; margin: 0.5cm 0; border-radius: 0 4px 4px 0; font-size: 10pt; font-style: italic; page-break-inside: avoid; }
.quote-box .speaker { font-style: normal; font-weight: bold; color: #555; }
.critical-box { background-color: #fdeaea; border-right: 4px solid #c0392b; padding: 12px 16px; margin: 0.5cm 0; border-radius: 0 4px 4px 0; font-size: 10pt; page-break-inside: avoid; }
.critical-box strong { color: #c0392b; }
.phase-box-yellow { background-color: #fffde7; border-right: 4px solid #f9a825; padding: 12px 16px; margin: 0.5cm 0; border-radius: 0 4px 4px 0; }
.phase-box-orange { background-color: #fff3e0; border-right: 4px solid #e65100; padding: 12px 16px; margin: 0.5cm 0; border-radius: 0 4px 4px 0; }
.phase-box-red { background-color: #fce4ec; border-right: 4px solid #c62828; padding: 12px 16px; margin: 0.5cm 0; border-radius: 0 4px 4px 0; }
.diagram { background-color: #f5f6fa; border: 1px solid #ddd; border-radius: 6px; padding: 1cm; margin: 0.8cm 0; direction: ltr; text-align: center; font-family: 'Courier New', monospace; font-size: 9pt; line-height: 1.4; white-space: pre; page-break-inside: avoid; }
ul, ol { padding-right: 1.5em; padding-left: 0; margin: 0.3cm 0; }
li { margin-bottom: 4px; }
code { font-family: 'Courier New', monospace; background-color: #f4f4f4; padding: 1px 4px; border-radius: 3px; font-size: 9pt; direction: ltr; unicode-bidi: embed; }
.toc { page-break-after: always; }
.toc h1 { text-align: center; border-bottom: none; }
.toc-item { display: flex; justify-content: space-between; padding: 4px 0; border-bottom: 1px dotted #ccc; font-size: 11pt; }
.toc-item.level2 { padding-right: 1.5em; font-size: 10.5pt; }
.page-break { page-break-before: always; }
p { margin: 0.2cm 0; }
strong { font-weight: bold; }
em { font-style: italic; }
hr { border: none; border-top: 1px solid #ddd; margin: 0.5cm 0; }
.english { direction: ltr; text-align: left; unicode-bidi: embed; }
.field-name { direction: ltr; unicode-bidi: embed; font-family: 'Courier New', monospace; font-size: 9pt; background: #f0f0f0; padding: 1px 3px; border-radius: 2px; }
"""

def build_cover(imgs):
    return """
<div class="cover-page">
    <div class="cover-logo">TALIAZ HEALTH &bull; HealthyMind</div>
    <div class="cover-title">\u05de\u05e1\u05de\u05da \u05de\u05e4\u05e8\u05d8 \u05d8\u05db\u05e0\u05d9</div>
    <div class="cover-title" style="font-size: 22pt; margin-top: 0.3cm;">\u05d0\u05d9\u05e0\u05d8\u05d2\u05e8\u05e6\u05d9\u05d9\u05ea \u05de\u05e2\u05e8\u05db\u05ea \u05e7\u05dc\u05d9\u05e7\u05e1 (Clicks EHR)</div>
    <div class="cover-subtitle">\u05ea\u05dc\u05d9\u05d0\u05d6 &mdash; \u05de\u05db\u05d1\u05d9 \u05e9\u05d9\u05e8\u05d5\u05ea\u05d9 \u05d1\u05e8\u05d9\u05d0\u05d5\u05ea</div>
    <hr class="cover-line">
    <div class="cover-meta">
        <strong>\u05d4\u05d5\u05db\u05df \u05e2\u05dc \u05d9\u05d3\u05d9:</strong> \u05d3"\u05e8 \u05e8\u05d0\u05de\u05d9 \u05d7'\u05d5\u05e8\u05d9, CMIO &mdash; \u05ea\u05dc\u05d9\u05d0\u05d6 \u05d4\u05dc\u05ea' / \u05de\u05e8\u05e4\u05d0\u05ea HealthyMind<br>
        <strong>\u05ea\u05d0\u05e8\u05d9\u05da:</strong> 22 \u05d1\u05de\u05e8\u05e5 2026<br>
        <strong>\u05d2\u05e8\u05e1\u05d4:</strong> 2.0<br>
        <strong>\u05e0\u05de\u05e2\u05e0\u05d9\u05dd:</strong> \u05e9\u05dc\u05d5\u05de\u05d9 (\u05de\u05d5\u05d1\u05d9\u05dc \u05d8\u05db\u05e0\u05d9, \u05de\u05db\u05d1\u05d9), \u05d9\u05d4\u05d5\u05d3\u05d4 (\u05e8\u05d0\u05e9 \u05d0\u05d2\u05e3 \u05de\u05e2\u05e8\u05db\u05d5\u05ea \u05de\u05d9\u05d3\u05e2, \u05de\u05db\u05d1\u05d9), \u05e6\u05d5\u05d5\u05ea \u05d4\u05d0\u05d3\u05e8\u05d9\u05db\u05dc\u05d5\u05ea \u05e9\u05dc \u05de\u05db\u05d1\u05d9
    </div>
    <div class="cover-classification">\u05e1\u05d5\u05d3\u05d9 &mdash; \u05dc\u05e6\u05d5\u05d5\u05ea \u05d4\u05d8\u05db\u05e0\u05d9 \u05e9\u05dc \u05de\u05db\u05d1\u05d9 \u05d1\u05dc\u05d1\u05d3</div>
</div>
"""

def build_toc(imgs):
    return """
<div class="toc">
    <h1>תוכן עניינים</h1>
    <div class="toc-item"><span>1. תקציר מנהלים</span></div>
    <div class="toc-item"><span>2. רקע — ישיבת התיאום והחלטות</span></div>
    <div class="toc-item level2"><span>2.1 משתתפים</span></div>
    <div class="toc-item level2"><span>2.2 החלטות מרכזיות</span></div>
    <div class="toc-item level2"><span>2.3 פריטי פעולה</span></div>
    <div class="toc-item"><span>3. סקירת ארכיטקטורת המערכת</span></div>
    <div class="toc-item"><span>4. מנגנוני אינטגרציה קיימים</span></div>
    <div class="toc-item level2"><span>4.1 הכספת — ניתוח מעמיק</span></div>
    <div class="toc-item level2"><span>4.2 פרויקט בת קול</span></div>
    <div class="toc-item level2"><span>4.3 WebAge Wrapper</span></div>
    <div class="toc-item"><span>5. תיעוד מלא של זרימת העבודה — מסך אחר מסך</span></div>
    <div class="toc-item level2"><span>5.1-5.9 תת-סעיפים</span></div>
    <div class="toc-item"><span>6. סיכום זרימת נתונים</span></div>
    <div class="toc-item"><span>7. אבטחת מידע וגישה מרחוק</span></div>
    <div class="toc-item"><span>8. אינטגרציית iFeel וסיכומים פסיכיאטריים קודמים</span></div>
    <div class="toc-item"><span>9. חוק ניוד המידע ו-FHIR</span></div>
    <div class="toc-item"><span>10. מחיצת בריאות הנפש</span></div>
    <div class="toc-item"><span>11. מקרי בדיקה ושרשרת אימיילים</span></div>
    <div class="toc-item"><span>12. שלבי אינטגרציה ופריטי פעולה</span></div>
</div>
"""

def build_section_1(imgs):
    return """
<h1>1. תקציר מנהלים</h1>
<p>מסמך זה מתאר את <strong>המפרט הטכני המלא</strong> לאינטגרציה בין הפלטפורמה הקלינית של תליאז (Predictix/Xano) לבין מערכת קליקס EHR של מכבי שירותי בריאות. המסמך מבוסס על <strong>ישיבת תיאום</strong> שנערכה ב-19 במרץ 2026 בהשתתפות נציגי מכבי ותליאז, על <strong>הקלטת מסך</strong> מלאה של זרימת העבודה בקליקס (נובמבר 2024), ועל <strong>שרשרת אימייל</strong> מפורטת שתיעדה את ניסיונות האינטגרציה הקודמים.</p>
<h3>מטרה</h3>
<p>להחליף את הזנת הנתונים הידנית בקליקס בקריאות API אוטומטיות מהפלטפורמה הקלינית של תליאז, ובכך לאפשר:</p>
<ul>
    <li><strong>העלאת סיכום אוטומטית</strong> (תשובת יועץ) מתליאז לקליקס</li>
    <li><strong>הוצאת מרשמים</strong> באמצעות API במקום הזנה ידנית</li>
    <li><strong>סנכרון נתונים דו-כיווני</strong> — שליפת נתוני דמוגרפיה, תרופות ותוצאות מעבדה לתוך תליאז</li>
</ul>
<div class="info-box">
    <strong>גרסאות מערכת שנצפו:</strong><br>
    W-Clicks Dot.NET | Version 2023.12.109.23696<br>
    Application version 2024.09.101<br>
    גישה דרך Citrix StoreFront בכתובת: <code>d.mac.org.il/Citrix/ExtWeb/</code>
</div>
<div class="decision-box">
    <strong>החלטה מרכזית מהישיבה:</strong> שלומי (מוביל טכני, מכבי) אישר שניתן לספק לתליאז גישת API לכתיבה וקריאה מקליקס, בכפוף לבחינה טכנית של צוות האדריכלות. המסמך הנוכחי נכתב כדי לאפשר את הבחינה הזו.
</div>
"""

def build_section_2(imgs):
    return """
<h1 class="page-break">2. רקע — ישיבת התיאום והחלטות</h1>
<p>ב-19 במרץ 2026 נערכה ישיבת תיאום בין תליאז למכבי לדיון באפשרויות האינטגרציה. הישיבה כללה סקירה של המצב הנוכחי, ניסיונות העבר (כספת), ומיפוי דרישות עתידיות.</p>
<h2>2.1 משתתפים</h2>
<table>
    <thead><tr><th>שם</th><th>תפקיד</th><th>ארגון</th></tr></thead>
    <tbody>
        <tr><td>שלומי</td><td>מוביל טכני, מערכות מידע</td><td>מכבי</td></tr>
        <tr><td>יהודה</td><td>ראש אגף מערכות מידע</td><td>מכבי</td></tr>
        <tr><td>ד"ר ראמי ח׳ורי</td><td>CMIO</td><td>תליאז / HealthyMind</td></tr>
        <tr><td>דקל תליאז</td><td>מנכ"ל</td><td>תליאז</td></tr>
        <tr><td>שחר שגב</td><td>מנהלת תפעול קליני</td><td>תליאז</td></tr>
        <tr><td>ענת מירון</td><td>מנהלת בריאות הנפש</td><td>מכבי</td></tr>
    </tbody>
</table>
<h2>2.2 החלטות מרכזיות</h2>
<div class="decision-box">
    <strong>החלטה 1 — גישת API:</strong> שלומי אישר עקרונית שניתן לספק לתליאז API לקליקס. נדרשת בחינה טכנית של צוות האדריכלות על בסיס המסמך הנוכחי.
</div>
<div class="decision-box">
    <strong>החלטה 2 — הכספת:</strong> מנגנון הכספת הקיים אינו מספק — סיכומים מועלים אך אינם מנותבים לרופא המשפחה. יש לבחון מחדש את התצורה או לעבור ל-API ישיר.
</div>
<div class="decision-box">
    <strong>החלטה 3 — פרויקט בת קול כמודל:</strong> ל"בת קול" כבר יש API להעלאת סיכומים לקליקס. תשתית זו יכולה לשמש כבסיס לאינטגרציה של תליאז.
</div>
<div class="decision-box">
    <strong>החלטה 4 — סביבת בדיקות:</strong> שלומי הציע שתליאז תקבל גישה לסביבת בדיקות (TEST environment) של קליקס לפיתוח ובדיקת האינטגרציה.
</div>
<div class="decision-box">
    <strong>החלטה 5 — מסמך טכני:</strong> תליאז תכין מסמך מפרט טכני מפורט (המסמך הנוכחי) לצוות האדריכלות של מכבי, כבסיס לתכנון ה-API.
</div>
<div class="warning-box">
    <strong>&#9888; אזהרת ענת מירון:</strong> ענת מירון, מנהלת בריאות הנפש במכבי, הדגישה שכל שינוי בזרימת העבודה חייב לקבל את אישורה ואת אישור הנהלת בריאות הנפש. היא ביקשה להיות מעורבת בכל שלבי התכנון.
</div>
<h2>2.3 פריטי פעולה</h2>
<div class="quote-box">
    <span class="speaker">שלומי (מכבי) — מהישיבה:</span>
    "אני אצוות מישהו, אני אביס לכם ארכיטקט, שיישב איתכם [...] זה לא צריך לתמחר את זה, ולא צריך לתעדף את זה, יהודה, זה עליי."
</div>
<div class="quote-box">
    <span class="speaker">שלומי (מכבי) — מהישיבה:</span>
    "אני מציע, אני אשים ארכיטקט, יחד עם טכנולוגיות רפואיות, מישהו מטכנולוגיות רפואיות, יחד עם ארכיטקט, ישבו רגע איתכם להבין על מה מדובר [...] הם יבואו אלינו עם סיכום של מה זה אומר, מה המשמעות, מה קיים היום, ומה אפשר לעשות."
</div>
<div class="quote-box">
    <span class="speaker">שלומי (מכבי) — מהישיבה:</span>
    "שימו הכל, שימו את הכל על מסמך [...] כל החלומות, תשימו מה שאתם רוצים, הכל בפנים, ואז נבין מה קיים [...] נשים ארכיטקט חינם, בסדר, כרגע לא עולה כסף, ארכיטקט, נשים מנתח מערכות, מאפיין בצד של טכנולוגיות רפואיות, שמכיר את הקליקס טוב."
</div>
<div class="info-box">
    <strong>סיכום:</strong> שלומי התחייב לצוות <strong>ארכיטקט + מנתח מערכות מטכנולוגיות רפואיות</strong> (שני אנשים), <strong>ללא עלות</strong> בשלב זה. תליאז מתבקשת להכין מסמך מפורט עם "כל החלומות" — כל הדרישות, כל המסכים, כל השדות. ישיבת קבלת החלטות <strong>לפני פסח</strong>.
</div>
<table>
    <thead><tr><th>#</th><th>פריט</th><th>אחראי</th><th>לוח זמנים</th></tr></thead>
    <tbody>
        <tr><td>1</td><td>הכנת מסמך מפרט טכני מלא — "כל החלומות"</td><td>ד"ר ראמי ח׳ורי + שחר שגב (תליאז)</td><td>מיידי</td></tr>
        <tr><td>2</td><td>שיבוץ ארכיטקט + מנתח מערכות (טכנולוגיות רפואיות)</td><td>שלומי (מכבי)</td><td>מיידי — ללא עלות</td></tr>
        <tr><td>3</td><td>פגישת הערכה טכנית (ארכיטקט + תליאז)</td><td>שלומי + שחר שגב</td><td>שבוע-שבועיים</td></tr>
        <tr><td>4</td><td>ישיבת קבלת החלטות עם יהודה</td><td>שלומי + יהודה + תליאז</td><td>לפני פסח</td></tr>
        <tr><td>5</td><td>בדיקת פתרון Remote Desktop מחו״ל מול אבטחת מידע</td><td>שלומי (מכבי)</td><td>לאחר קבלת סיכום מאת שחר</td></tr>
        <tr><td>6</td><td>שליחת סיכום פגישה לשלומי</td><td>שחר שגב (תליאז)</td><td>מיידי</td></tr>
    </tbody>
</table>
"""

def build_section_3(imgs):
    return """
<h1 class="page-break">3. סקירת ארכיטקטורת המערכת</h1>
<h3>מצב נוכחי</h3>
<div class="diagram">Current State

  Psychiatrist ---Citrix VPN---&gt; Clicks EHR
  (Local PC)                     (Maccabi servers)
       | Copy-Paste
       v
  Predictix (Xano/Web)
  Taliaz Clinical Platform</div>

<h3>מצב יעד</h3>
<div class="diagram">Target State

  Predictix  &lt;---API Layer---&gt;  Clicks EHR
  (Xano/Web)    (REST/SOAP)     (Maccabi servers)
       |                              |
       +------ Automated Flow --------+
         - Upload summaries
         - Sync prescriptions
         - Pull patient data</div>

<div class="quote-box">
    <span class="speaker">שלומי (מכבי):</span> "אם תכינו מסמך מפורט עם כל השדות והזרימות, אני אעביר את זה לצוות האדריכלות שלנו. הם יבחנו מה אפשר לפתוח ומה לא."
</div>
"""

def build_section_4(imgs):
    return """
<h1 class="page-break">4. מנגנוני אינטגרציה קיימים</h1>
<p>לפני תכנון אינטגרציה חדשה, יש לסקור את המנגנונים הקיימים שכבר פועלים (או שנוסו) בין ספקים חיצוניים לקליקס:</p>
<h2>4.1 הכספת — ניתוח מעמיק</h2>
<p>הכספת היא מנגנון קיים במכבי המאפשר לספקים חיצוניים להעלות מסמכים לתיק המטופל בקליקס. תליאז ניסתה להשתמש בכספת להעלאת סיכומי ייעוץ — אך נתקלה בבעיות חמורות.</p>
<div class="critical-box">
    <strong>3 בעיות קריטיות שזוהו בכספת:</strong>
    <ol>
        <li><strong>ניתוב שגוי:</strong> סיכומים הועלו בהצלחה לכספת אך לא הגיעו לדואר הרפואי של רופא המשפחה. המסמכים "נבלעו" בתיק ללא התראה.</li>
        <li><strong>היעדר תשובת יועץ:</strong> הכספת מעלה מסמך כקובץ מצורף, אך אינה יוצרת "תשובת יועץ" רשמית בקליקס — הרופא המשפחה לא מקבל הודעה על ייעוץ חדש.</li>
        <li><strong>דחייה על ידי ענת מירון:</strong> מנהלת בריאות הנפש במכבי דחתה את מנגנון הכספת כפתרון קבוע, בטענה שהוא אינו עומד בדרישות התקשורת הקלינית.</li>
    </ol>
</div>
<h3>השוואת כספת מול API ישיר</h3>
<table>
    <thead><tr><th>קריטריון</th><th>כספת</th><th>API ישיר לקליקס</th></tr></thead>
    <tbody>
        <tr><td>העלאת סיכום</td><td>קובץ מצורף בלבד</td><td>תשובת יועץ רשמית</td></tr>
        <tr><td>התראה לרופא משפחה</td><td>לא</td><td>כן</td></tr>
        <tr><td>קודי אבחנה</td><td>לא</td><td>כן</td></tr>
        <tr><td>מרשמים</td><td>לא</td><td>אפשרי</td></tr>
        <tr><td>שליפת נתוני מטופל</td><td>לא</td><td>כן</td></tr>
        <tr><td>מורכבות הקמה</td><td>נמוכה</td><td>גבוהה</td></tr>
        <tr><td>תחזוקה שוטפת</td><td>נמוכה</td><td>בינונית</td></tr>
    </tbody>
</table>
<h2>4.2 פרויקט בת קול</h2>
<p>פרויקט <strong>בת קול</strong> של מכבי הוא מערכת קיימת שכבר משתמשת ב-API להעלאת סיכומים לקליקס. בישיבה, שלומי הזכיר את בת קול כמודל אפשרי לאינטגרציה של תליאז.</p>
<div class="quote-box">
    <span class="speaker">שלומי (מכבי):</span> "בת קול כבר עושים את זה — יש להם API שכותב לקליקס. אפשר לבדוק אם אפשר לעשות את אותו דבר עבורכם."
</div>
<div class="info-box">
    <strong>משמעות:</strong> קיומו של API עובד בבת קול מוכיח שהדבר אפשרי טכנית. השאלה היא האם ניתן להרחיב את אותה תשתית לשימוש תליאז, או שנדרש API נפרד.
</div>
<h2>4.3 WebAge Wrapper</h2>
<p>שלומי הזכיר בישיבה את <strong>WebAge</strong> — שכבת wrapper שמכבי משתמשת בה כממשק בין מערכות חיצוניות לקליקס. ייתכן שזו שכבת ה-middleware שדרכה ניתן יהיה לבצע את האינטגרציה.</p>
<div class="quote-box">
    <span class="speaker">שלומי (מכבי):</span> "יש לנו WebAge שיושב מעל קליקס ומאפשר תקשורת. צריך לבדוק מה אפשר לחשוף דרכו."
</div>
"""

def build_section_5(imgs):
    return f"""
<h1 class="page-break">5. תיעוד מלא של זרימת העבודה — מסך אחר מסך</h1>

<h2>5.1 גישה והזדהות</h2>
<h3>שלב 1: כניסה דרך Citrix StoreFront</h3>
<div class="screenshot-container">
    <img src="{imgs['01_citrix_storefront_app_launcher.jpg']}" alt="Citrix StoreFront">
    <div class="screenshot-caption">צילום מסך 1: פורטל Citrix StoreFront — השקת אפליקציית קליקס</div>
</div>
<p>הפסיכיאטר ניגש לקליקס דרך פורטל Citrix StoreFront של מכבי בכתובת <code>d.mac.org.il/Citrix/ExtWeb/</code>. הפורטל מציג 19 אפליקציות זמינות, כולל:</p>
<ul>
    <li><strong>ניהול תיק רפואי-2017</strong> — זו אפליקציית קליקס</li>
    <li>Citrix Excel, Word, PowerPoint, Outlook</li>
    <li>Bomgar (תמיכה מרחוק)</li>
</ul>
<div class="info-box">
    <strong>הערת אינטגרציה:</strong> שכבת ה-Citrix מוסיפה מורכבות — כל API יצטרך לעקוף את סשן ה-Citrix או לפעול בצד השרת ברשת הפנימית של מכבי.
</div>

<h2 class="page-break">5.2 פורטל רופא ובחירת מטופל</h2>
<h3>שלב 2: פורטל רופא בקליקס</h3>
<div class="screenshot-container">
    <img src="{imgs['02_clicks_doctor_portal_patient_list.jpg']}" alt="פורטל רופא">
    <div class="screenshot-caption">צילום מסך 2: פורטל רופא עם רשימת מטופלים ומערכת חיפוש</div>
</div>
<p>לאחר ההשקה, הרופא נכנס ל<strong>פורטל הרופא</strong>. אזורים עיקריים:</p>
<p><strong>פאנל שמאלי — קישורים:</strong> מדריך השירותים, קליקיפדיה, טפסים והורדות, ביקור ללא כרטיס, עדכון היעדרויות.</p>
<p><strong>מרכז — דואר רפואי, משימות והודעות:</strong> תשובות לבדיקות, מידע ואישורים, פניות מקומות, אישורי תרופות.</p>
<p><strong>פאנל ימני — חיפוש מטופל:</strong></p>
<table>
    <thead><tr><th>שדה</th><th>שם עברי</th><th>סוג</th><th>הערות</th></tr></thead>
    <tbody>
        <tr><td>ת.ז. מטופל</td><td>תעודת זהות</td><td>מספר בן 9 ספרות</td><td>מפתח ראשי</td></tr>
        <tr><td>טלפון</td><td>טלפון</td><td>מחרוזת</td><td></td></tr>
        <tr><td>שם פרטי</td><td>שם פרטי</td><td>מחרוזת</td><td></td></tr>
        <tr><td>שם משפחה</td><td>שם משפחה</td><td>מחרוזת</td><td></td></tr>
    </tbody>
</table>

<h3>שלב 3: תצוגה מקבילה — קליקס + Predictix של תליאז</h3>
<div class="screenshot-container">
    <img src="{imgs['03_clicks_and_predictix_side_by_side.jpg']}" alt="תצוגה מקבילה">
    <div class="screenshot-caption">צילום מסך 3: עבודה במקביל עם קליקס (למעלה) ופלטפורמת Predictix של תליאז (למטה)</div>
</div>
<div class="info-box">
    <strong>הזדמנות אינטגרציה:</strong> ביטול ה-copy-paste בין שתי המערכות על ידי push/pull אוטומטי של נתונים מ-Predictix לקליקס באמצעות API.
</div>

<h2 class="page-break">5.3 תיק מטופל ונתונים קליניים</h2>
<h3>שלב 4: פרטים אישיים של המטופל</h3>
<div class="screenshot-container">
    <img src="{imgs['04_patient_file_personal_details.jpg']}" alt="פרטים אישיים">
    <div class="screenshot-caption">צילום מסך 4: תיק מטופל — פרטים אישיים, בעיות ידועות, תרופות קבועות</div>
</div>
<p><strong>בעיות ידועות — בריאות הנפש:</strong></p>
<ul>
    <li>ANXIETY AND DEPRESSION (01/2022) — severe</li>
    <li>POST TRAUMATIC STRESS DISORDER (01/2022)</li>
</ul>
<p><strong>תרופות קבועות עם מרשמים בתוקף:</strong></p>
<ul>
    <li>MIRO 30MG X 30 (0.5X1) — Mirtazapine</li>
    <li>CIPRALEX 10MG X 28 (1X1) — Escitalopram</li>
</ul>
<h4>שדות לגישת API — פעולות קריאה (READ):</h4>
<table>
    <thead><tr><th>שדה</th><th>שם עברי</th><th>עדיפות API</th></tr></thead>
    <tbody>
        <tr><td>דמוגרפיה</td><td>פרטים אישיים</td><td><strong>גבוהה</strong></td></tr>
        <tr><td>אבחנות ידועות</td><td>בעיות ידועות</td><td><strong>גבוהה</strong></td></tr>
        <tr><td>תרופות נוכחיות</td><td>תרופות קבועות</td><td><strong>גבוהה</strong></td></tr>
        <tr><td>אלרגיות/רגישויות</td><td>רגישויות</td><td><strong>גבוהה</strong></td></tr>
        <tr><td>תוצאות מעבדה</td><td>מעבדות</td><td>בינונית</td></tr>
        <tr><td>ייעוצים קודמים</td><td>ייעוצים</td><td>בינונית</td></tr>
    </tbody>
</table>

<h2 class="page-break">5.4 רישום ביקורים</h2>
<h3>שלב 5: פתיחת ביקור</h3>
<div class="screenshot-container">
    <img src="{imgs['05_visit_registration_screen.jpg']}" alt="רישום ביקורים">
    <div class="screenshot-caption">צילום מסך 5: מסך רישום ביקורים — פתיחת ייעוץ פסיכיאטרי</div>
</div>
<p>מסך רישום הביקורים מתעד:</p>
<ul>
    <li><strong>תאריך ושעה:</strong> 10:55 22/11/2024</li>
    <li><strong>רופא:</strong> ד"ר ג׳הג׳אה אלי׳אס</li>
    <li><strong>תחום הטיפול:</strong> פסיכיאטריה</li>
    <li><strong>סוג ביקור:</strong> ביקור ללא נוכחות המטופל / ביקור חוזר / אינטייק</li>
</ul>

<h3>שלב 6: הזנת ממצאים קליניים</h3>
<div class="screenshot-container">
    <img src="{imgs['06_clinical_findings_form.jpg']}" alt="ממצאים קליניים">
    <div class="screenshot-caption">צילום מסך 6: טופס ממצאים קליניים עם קטגוריות בדיקה</div>
</div>
<h4>שדות לגישת API — פעולות כתיבה (WRITE):</h4>
<table>
    <thead><tr><th>שדה</th><th>שם עברי</th><th>סוג</th><th>עדיפות</th></tr></thead>
    <tbody>
        <tr><td>תאריך ושעת ביקור</td><td>תאריך ושעה</td><td>DateTime</td><td><strong>גבוהה</strong></td></tr>
        <tr><td>מזהה רופא</td><td>מזהה רופא</td><td>מחרוזת</td><td><strong>גבוהה</strong></td></tr>
        <tr><td>סוג ביקור</td><td>סוג ביקור</td><td>אינטייק/מעקב</td><td><strong>גבוהה</strong></td></tr>
        <tr><td>ממצאים קליניים</td><td>ממצאי הבדיקה</td><td>טקסט חופשי</td><td><strong>גבוהה</strong></td></tr>
        <tr><td>הערכת מסוכנות</td><td>מסוכנות</td><td>תיבות סימון</td><td><strong>גבוהה</strong></td></tr>
    </tbody>
</table>

<h2 class="page-break">5.5 הזנת אבחנה</h2>
<h3>שלב 7: חיפוש ובחירת אבחנה (ICD)</h3>
<div class="screenshot-container">
    <img src="{imgs['07_diagnosis_icd_entry.jpg']}" alt="הזנת אבחנה">
    <div class="screenshot-caption">צילום מסך 7: השלמה אוטומטית של קודי ICD — חיפוש "POST TR"</div>
</div>
<table>
    <thead><tr><th>קוד</th><th>תיאור</th></tr></thead>
    <tbody>
        <tr><td>PA</td><td>POST TRAUMATIC STRESS DISORDER (PTSD)</td></tr>
        <tr><td>CGR</td><td>CHRONIC POST TRAUMATIC STRESS DISORDER</td></tr>
        <tr><td>CW0</td><td>COMPLEX POST TRAUMATIC STRESS DISORDER</td></tr>
        <tr><td>APT</td><td>ACUTE POST TRAUMATIC STRESS DISORDER</td></tr>
    </tbody>
</table>
<div class="info-box">
    <strong>הערה:</strong> קליקס משתמש בקודים פנימיים קצרים הממופים ל-ICD. כל API יצטרך להשתמש בקודים הפנימיים הללו, לא בקודי ICD-10 סטנדרטיים.
</div>

<h3>שלב 8: בחירת סוג טיפול (קודים פסיכיאטריים)</h3>
<div class="screenshot-container">
    <img src="{imgs['08_treatment_type_psychiatric_codes.jpg']}" alt="קודי טיפול">
    <div class="screenshot-caption">צילום מסך 8: קודי שירות פסיכיאטרי במערכת קליקס</div>
</div>
<table>
    <thead><tr><th>קוד</th><th>תיאור</th></tr></thead>
    <tbody>
        <tr><td>PPU</td><td>PSYCHIATRIC INTAKE - ADULT</td></tr>
        <tr><td>PP5</td><td>PSYCHIATRIC MEDIC. FOLLOW UP / TREATMENT</td></tr>
        <tr><td>PP1</td><td>PSYCHOTHERAPY - ADULT</td></tr>
        <tr><td>PPW</td><td>PSYCHIATRIC INTAKE - CHILD</td></tr>
        <tr><td>LLK</td><td>LONG PSYCHIATRIC FOLLOW UP - CHILD</td></tr>
    </tbody>
</table>

<h2 class="page-break">5.6 תשובת יועץ (מסמך הסיכום)</h2>
<div class="warning-box">
    <strong>&#9888; יעד מס׳ 1 לאוטומציה:</strong> תשובת היועץ היא המנגנון העיקרי לתקשורת הממצאים הפסיכיאטריים בחזרה לרופא המשפחה המפנה. זהו היעד בעל ה-ROI הגבוה ביותר לאוטומציה באמצעות API.
</div>
<h3>שלב 9: בחירת הרופא המפנה</h3>
<div class="screenshot-container">
    <img src="{imgs['09_consultant_response_doctor_selection.jpg']}" alt="בחירת רופא">
    <div class="screenshot-caption">צילום מסך 9: דיאלוג תשובת יועץ — בחירת רופא מטפל להעברת התשובה</div>
</div>
<h3>שלב 10: תוכן מכתב תשובת היועץ</h3>
<div class="screenshot-container">
    <img src="{imgs['10_consultant_response_letter_content.jpg']}" alt="תוכן תשובת יועץ">
    <div class="screenshot-caption">צילום מסך 10: מכתב תשובת יועץ מלא עם פרטי מטופל וטקסט קליני</div>
</div>
<h4>שדות לגישת API — כתיבת סיכום (עדיפות קריטית):</h4>
<table>
    <thead><tr><th>שדה</th><th>סוג</th><th>הערות</th></tr></thead>
    <tbody>
        <tr><td>תאריך בדיקה</td><td>תאריך</td><td>בדיקה שנעשתה ב...</td></tr>
        <tr><td>סוג ביקור</td><td>מחרוזת</td><td>אינטייק / מעקב</td></tr>
        <tr><td>נרטיב קליני</td><td>RTF/HTML</td><td>טקסט הערכה מלא</td></tr>
        <tr><td>אבחנה</td><td>ICD-10 + טקסט</td><td>F43.1 וכו׳</td></tr>
        <tr><td>המלצות טיפול</td><td>טקסט</td><td>תרופות מומלצות</td></tr>
        <tr><td>מזהה רופא מפנה</td><td>מחרוזת</td><td>יעד לתשובה</td></tr>
    </tbody>
</table>
<h3>שלב 11: אבחנה והמלצות</h3>
<div class="screenshot-container">
    <img src="{imgs['11_summary_diagnosis_recommendations.jpg']}" alt="אבחנה והמלצות">
    <div class="screenshot-caption">צילום מסך 11: אישור אבחנה, תרופות מומלצות ואפשרויות חתימה</div>
</div>

<h2 class="page-break">5.7 סיום ביקור וחתימה</h2>
<h3>שלב 12: קוד טיפול ותזמון מעקב</h3>
<div class="screenshot-container">
    <img src="{imgs['12_visit_completion_treatment_code.jpg']}" alt="סיום ביקור">
    <div class="screenshot-caption">צילום מסך 12: קוד טיפול PSYCHIATRIC INTAKE - ADULT (9864), תזמון מעקב</div>
</div>
<h3>שלב 13: שליחת טפסים</h3>
<div class="screenshot-container">
    <img src="{imgs['13_form_submission_patient_instructions.jpg']}" alt="שליחת טפסים">
    <div class="screenshot-caption">צילום מסך 13: דיאלוג שליחת טפסים — אישור ותשובת יועץ</div>
</div>
<h3>שלב 14: חתימה דיגיטלית</h3>
<div class="screenshot-container">
    <img src="{imgs['14_digital_signature_login.jpg']}" alt="חתימה דיגיטלית">
    <div class="screenshot-caption">צילום מסך 14: דיאלוג הזדהות לחתימה דיגיטלית</div>
</div>
<p>החתימה הדיגיטלית דורשת שם משתמש וסיסמה. זוהי שכבת אבטחה קריטית — כל אינטגרציית API תצטרך לטפל בהזדהות וחתימה באופן תכנותי.</p>
<h3>שלב 15: רשומת ביקור חתומה</h3>
<div class="screenshot-container">
    <img src="{imgs['15_signed_visit_record.jpg']}" alt="רשומה חתומה">
    <div class="screenshot-caption">צילום מסך 15: רשומת ביקור חתומה עם חותמת זמן ותוכן קליני מלא</div>
</div>

<h2 class="page-break">5.8 ניהול מרשמים</h2>
<h3>שלב 16: תצוגת תרופות קבועות</h3>
<div class="screenshot-container">
    <img src="{imgs['16_chronic_medications_view.jpg']}" alt="תרופות קבועות">
    <div class="screenshot-caption">צילום מסך 16: טבלת תרופות קבועות — סטטוס מרשמים נוכחי</div>
</div>
<table>
    <thead><tr><th>תרופה</th><th>שם גנרי</th><th>מינון</th><th>תדירות</th><th>אחוז הענות</th><th>רושם</th></tr></thead>
    <tbody>
        <tr><td>MIRO 30MG X 30</td><td>MIRTAZAPINE</td><td>1</td><td>0.5</td><td>80</td><td>ד"ר קורץ אלינע</td></tr>
        <tr><td>CIPRALEX 10MG X 28</td><td>ESCITALOPRAM</td><td>1</td><td>1</td><td>80</td><td>ד"ר קורץ אלינע</td></tr>
    </tbody>
</table>
<h3>שלב 17: עדכון מינון תרופה</h3>
<div class="screenshot-container">
    <img src="{imgs['17_medication_dosage_update.jpg']}" alt="עדכון מינון">
    <div class="screenshot-caption">צילום מסך 17: דיאלוג עדכון מינון — MIRO 30MG</div>
</div>
<h4>שדות לגישת API — כתיבת תרופות:</h4>
<table>
    <thead><tr><th>שדה</th><th>סוג</th><th>הערות</th></tr></thead>
    <tbody>
        <tr><td>שם תרופה</td><td>מחרוזת</td><td>למשל MIRO TAB 30MG X 30</td></tr>
        <tr><td>מינון</td><td>מספר עשרוני</td><td>מספר טבליות</td></tr>
        <tr><td>תדירות</td><td>מספר שלם</td><td>פעמים ביום</td></tr>
        <tr><td>משך</td><td>מספר שלם</td><td>ימים</td></tr>
        <tr><td>זמן נטילה</td><td>בחירה</td><td>בוקר/צהריים/ערב/לפני שינה</td></tr>
    </tbody>
</table>
<h3>שלב 18: חיפוש תרופה חדשה</h3>
<div class="screenshot-container">
    <img src="{imgs['18_new_prescription_drug_search.jpg']}" alt="חיפוש תרופה">
    <div class="screenshot-caption">צילום מסך 18: חיפוש תרופה (LORIVAN) עם התרעות</div>
</div>
<h3>שלב 19: טופס מרשם</h3>
<div class="screenshot-container">
    <img src="{imgs['19_prescription_form_dosage_instructions.jpg']}" alt="טופס מרשם">
    <div class="screenshot-caption">צילום מסך 19: טופס מרשם — LORIVAN TAB 1MG X 20</div>
</div>
<h3>שלב 20: אישור שמירת מרשם</h3>
<div class="screenshot-container">
    <img src="{imgs['20_prescription_save_confirmation.jpg']}" alt="אישור שמירה">
    <div class="screenshot-caption">צילום מסך 20: דיאלוג אישור שמירת מרשם</div>
</div>
<h3>שלב 21: הפקת מרשמים</h3>
<div class="screenshot-container">
    <img src="{imgs['21_prescription_generation_screen.jpg']}" alt="הפקת מרשמים">
    <div class="screenshot-caption">צילום מסך 21: מסך הפקת מרשמים — בחירת תרופות, משך ואפשרויות שליחה</div>
</div>

<h2 class="page-break">5.9 מערכת חיצונית — מסמך סיכום</h2>
<div class="screenshot-container">
    <img src="{imgs['24_google_docs_summary_document.jpg']}" alt="Google Docs">
    <div class="screenshot-caption">צילום מסך 22: מסמך סיכום ב-Google Docs — מוכן ל-copy-paste לקליקס</div>
</div>
<p>צילום מסך זה מציג את <strong>צד תליאז</strong> של זרימת העבודה — מסמך סיכום המוכן ב-Google Docs לפני שהוא מועתק ידנית לקליקס.</p>
<div class="warning-box">
    <strong>&#9888; הערת אינטגרציה:</strong> זהו בדיוק התוכן שצריך להידחף אוטומטית מתליאז לקליקס באמצעות API, ובכך לבטל את זרימת ה-copy-paste בין Google Docs לתשובת יועץ בקליקס.
</div>
"""

def build_section_6(imgs):
    return """
<h1 class="page-break">6. סיכום זרימת נתונים — שדות הדורשים גישת API</h1>
<h2>6.1 פעולות קריאה (קליקס ← תליאז)</h2>
<table>
    <thead><tr><th>עדיפות</th><th>נתון</th><th>מסך בקליקס</th><th>שיטה נוכחית</th></tr></thead>
    <tbody>
        <tr><td><strong>גבוהה</strong></td><td>דמוגרפיה</td><td>פרטים אישיים</td><td>חיפוש ידני</td></tr>
        <tr><td><strong>גבוהה</strong></td><td>אבחנות ידועות</td><td>בעיות ידועות</td><td>קריאה ידנית</td></tr>
        <tr><td><strong>גבוהה</strong></td><td>תרופות נוכחיות</td><td>תרופות קבועות</td><td>קריאה ידנית</td></tr>
        <tr><td><strong>גבוהה</strong></td><td>אלרגיות</td><td>רגישויות</td><td>קריאה ידנית</td></tr>
        <tr><td>בינונית</td><td>תוצאות מעבדה</td><td>מעבדות</td><td>קריאה ידנית</td></tr>
        <tr><td>בינונית</td><td>ייעוצים קודמים</td><td>ייעוצים</td><td>קריאה ידנית</td></tr>
        <tr><td>נמוכה</td><td>גורמי סיכון</td><td>גורמי סיכון</td><td>קריאה ידנית</td></tr>
    </tbody>
</table>
<h2>6.2 פעולות כתיבה (תליאז → קליקס)</h2>
<table>
    <thead><tr><th>עדיפות</th><th>נתון</th><th>מסך בקליקס</th><th>שיטה נוכחית</th></tr></thead>
    <tbody>
        <tr><td><strong style="color: #c0392b;">קריטית</strong></td><td>מכתב תשובת יועץ</td><td>תשובת יועץ</td><td>copy-paste מ-Google Docs</td></tr>
        <tr><td><strong>גבוהה</strong></td><td>רישום ביקור</td><td>רישום ביקורים</td><td>הזנה ידנית</td></tr>
        <tr><td><strong>גבוהה</strong></td><td>אבחנה</td><td>אבחנה</td><td>חיפוש ICD ידני</td></tr>
        <tr><td><strong>גבוהה</strong></td><td>תוכנית טיפול</td><td>תוכנית טיפול</td><td>הזנת טקסט ידנית</td></tr>
        <tr><td><strong>גבוהה</strong></td><td>מרשמים חדשים</td><td>תרופות קבועות</td><td>חיפוש תרופה ידני</td></tr>
        <tr><td><strong>גבוהה</strong></td><td>עדכוני מינון</td><td>עדכון מינון</td><td>הזנה ידנית</td></tr>
        <tr><td>בינונית</td><td>תזמון מעקב</td><td>מוזמן למעקב</td><td>בחירה ידנית</td></tr>
        <tr><td>בינונית</td><td>חתימה דיגיטלית</td><td>חתימה דיגיטלית</td><td>הזדהות ידנית</td></tr>
    </tbody>
</table>
"""

def build_section_7(imgs):
    return """
<h1 class="page-break">7. אבטחת מידע וגישה מרחוק</h1>
<p>נושא האבטחה עלה כסוגיה מרכזית בישיבה, במיוחד בהקשר של גישה מרחוק ממיקומים מחוץ לישראל וההשלכות על אינטגרציית API.</p>
<h2>7.1 גישה מרחוק — המצב הנוכחי</h2>
<div class="quote-box">
    <span class="speaker">שלומי (מכבי) — מהישיבה:</span>
    "לחו״ל, כדי לעבוד במכבי צריך אישור מיוחד [...] זה בדרך כלל יהיה מחשב של מכבי, מחשב נייד של מכבי שהוא מנועל [...] אנחנו לא מאפשרים את זה, בטח לא בזמן מלחמה."
</div>
<p>הפסיכיאטרים של תליאז עובדים מרחוק (טלפסיכיאטריה) ולעיתים שוהים בחו״ל. הגישה הנוכחית לקליקס היא דרך Citrix ודורשת:</p>
<ul>
    <li><strong>Citrix StoreFront:</strong> גישה לקליקס דרך שולחן עבודה מרוחק של מכבי</li>
    <li><strong>מחשב נעול:</strong> מחשב נייד של מכבי עם הגדרות אבטחה — "מחשב שהוא מנועל, שהוא לא יכול לעשות מה שהוא רוצה במחשב"</li>
    <li><strong>אישור אבטחת מידע:</strong> נדרש אישור מיוחד לגישה מחוץ לישראל</li>
    <li><strong>הגבלת זמן מלחמה:</strong> שלומי ציין שבזמן מלחמה ההגבלות מחמירות אף יותר</li>
</ul>
<div class="quote-box">
    <span class="speaker">דקל תליאז (מנכ"ל תליאז) — מהישיבה:</span>
    "כי יש לנו רופאים שעובדים מחו״ל ואז בהקשר הזה אם אנחנו רוצים — הם יוכלו להוציא מרשמים וכל זה — הם לא יכולים."
</div>

<h3>פתרון מוצע — Remote Desktop דרך מחשב בארץ</h3>
<div class="quote-box">
    <span class="speaker">שחר שגב (תליאז) — מהישיבה:</span>
    "VPN או מחשב פה שהוא ייכנס למחשב בארץ ומשם ייכנס לקליקס."
</div>
<div class="quote-box">
    <span class="speaker">שלומי (מכבי) — מהישיבה:</span>
    "זה יכול להיות שמחשב בארץ אפשר להלווין אותו אם זה מחשב מנועל [...] לדעתי אני לא רואה סיבה שלא, אבל צריך לבדוק את זה. שחר, תכתוב לי בסיכום של הפגישה ואני אבדוק את זה מול אבטחת מידע."
</div>
<div class="warning-box">
    <strong>&#9888; אישור CISO נדרש:</strong> שלומי הבהיר שלמרות שכל הטכנולוגיה יושבת תחתיו, צוות אבטחת המידע (CISO) הוא <strong>גוף עצמאי</strong> שמקבל החלטות באופן עצמאי: "אומנם זה תחתיי, אבל הם גוף עצמאי, הם חולטים." שחר ביקש לקבל אישור פורמלי לפני יישום הפתרון.
</div>

<h2>7.2 השלכות על אינטגרציית API</h2>
<div class="info-box">
    <strong>יתרון מפתח:</strong> אינטגרציה באמצעות API server-to-server מבטלת לחלוטין את בעיית הגישה מחו״ל. הפסיכיאטר ממשיך לעבוד בפלטפורמת תליאז מכל מקום בעולם, והנתונים מסונכרנים ברקע ישירות בין השרתים — ללא צורך ב-VPN, Citrix, או מחשב נעול.
</div>
<p>כלומר, אינטגרציית API פותרת גם את בעיית הגישה מחו״ל וגם את בעיית ההזנה הידנית — שתי ציפורים במכה אחת.</p>

<h2>7.3 סביבת בדיקות</h2>
<p>בישיבה, נבדקה האפשרות לקבל גישה לסביבת בדיקות של קליקס:</p>
<div class="warning-box">
    <strong>&#9888; אילוץ:</strong> שלומי הבהיר שסביבת הבדיקות (TEST) של קליקס <strong>מכילה מידע אמיתי של מטופלים</strong> ולכן הגישה מוגבלת לעובדי מכבי עם הרשאות ספציפיות בלבד. לא ניתן לתת גישה חיצונית לסביבת ה-TEST. לכן, ד"ר ראמי ח׳ורי יכין את צילומי המסך מתוך המערכת הפעילה (ללא שמירת שינויים).
</div>
<p>דרישות עתידיות לסביבת בדיקות ייעודית (לאחר אישור ארכיטקט):</p>
<ul>
    <li>סביבת sandbox ייעודית עם נתוני בדיקה פיקטיביים</li>
    <li>חשבון שירות (Service Account) לתליאז</li>
    <li>תיעוד API (endpoints, authentication, payload formats)</li>
</ul>
"""

def build_section_8(imgs):
    return """
<h1 class="page-break">8. אינטגרציית iFeel וסיכומים פסיכיאטריים קודמים</h1>
<p>שני נושאים קריטיים שעלו בישיבה נוגעים ל<strong>מעבר מידע קליני ממכבי לתליאז</strong> לפני תחילת הטיפול — קבלת סיכום iFeel וקבלת סיכומים פסיכיאטריים קודמים.</p>

<h2>8.1 מהי מערכת iFeel?</h2>
<p><strong>iFeel</strong> היא מערכת אינטייק (מיון ראשוני) של מכבי בתחום בריאות הנפש. המטופל עובר תהליך הערכה ראשונית דרך iFeel, וסיכום ההערכה נשמר בתיק המטופל בקליקס.</p>
<div class="quote-box">
    <span class="speaker">דקל תליאז (מנכ"ל תליאז) — מהישיבה:</span>
    "דיברנו על איך לחסוך את הזמן למטופלים, שלא יצטרכו לעבור שוב את אותם שאלונים ואותם זה. האם זה הזמן להעלות פה את הנקודה של איך אנחנו עושים פה את המעברי מידע? בין iFeel לבין הקייס מנג׳ר שלנו כדי שמטופל לא יצטרך לענות שוב על אותן שאלות."
</div>
<div class="quote-box">
    <span class="speaker">יהודה (מכבי) — מהישיבה:</span>
    "הוא בעצם מדבר על מסע המטופל החדש שבעצם יש סיכום של iFeel שיוצא ואז הוא צריך לקבל את הסיכום של iFeel כדי שלא יצטרך לעשות את כל התהליך מההתחלה אצלו."
</div>

<h3>מה תליאז צריכה מ-iFeel?</h3>
<div class="quote-box">
    <span class="speaker">שחר שגב (תליאז) — מהישיבה:</span>
    "שלומי, מבחינתי, אם יש דרך לחשוף לנו את המידע של iFeel דרך כספת או דרך API או דרך איזשהו דרך — למטופלים לפחות שאנחנו מטפלים בהם."
</div>
<div class="quote-box">
    <span class="speaker">ד"ר ראמי ח׳ורי (תליאז) — מהישיבה:</span>
    "רוצים את זה ממש בהתחלה, כשמטופל ממלא את השאלון, עוד לפני שנקבע פגישה עם מנהל תיק ופסיכיאטר. שהמערכת שלנו בעצם תתאים את המהלך של המטופל ותזהה שהוא עבר אינטייק, תזהה את המידע הקיים, ואז לחסוך ממנו לעבור אינטייק מלא."
</div>
<ul>
    <li><strong>מתי נדרש:</strong> בשלב מוקדם מאוד — לפני הפגישה הראשונה, עוד לפני שנקבע פסיכיאטר</li>
    <li><strong>למה:</strong> כדי למנוע מהמטופל למלא שוב שאלונים שכבר מילא ב-iFeel</li>
    <li><strong>איפה המידע קיים:</strong> סיכום iFeel כבר נמצא בתיק המטופל בקליקס</li>
    <li><strong>מה נדרש:</strong> דרך לחשוף את המידע הזה לתליאז — דרך API, כספת, או מנגנון אחר</li>
</ul>
<div class="info-box">
    <strong>הערה:</strong> שלומי ציין שנבנה כרגע "מסע מטופל חדש" סביב iFeel, אך היסס לחשוף פרטים ("אני לא יודע אם אני יכול לחשוף את זה פה"). ייתכן שהשינויים הצפויים במערכת iFeel ישפיעו על אפשרויות האינטגרציה.
</div>

<h2>8.2 סיכומים פסיכיאטריים קודמים</h2>
<p>בנוסף ל-iFeel, תליאז צריכה גישה ל<strong>סיכומים פסיכיאטריים קודמים</strong> של המטופל — מפסיכיאטרים אחרים שטיפלו בו בעבר דרך מכבי.</p>
<div class="quote-box">
    <span class="speaker">ד"ר ראמי ח׳ורי (תליאז) — מהישיבה:</span>
    "אני אשאל את השאלה יותר רחב — גם זה יהיה מאוד מבורך אם נוכל לשלוף סיכומים פסיכיאטריים קודמים. עכשיו אם זה לא אוטומטי, אז אנחנו כן נצטרך איזושהי הרשאה של מזכירה רפואית."
</div>
<div class="quote-box">
    <span class="speaker">יהודה (מכבי) — מהישיבה:</span>
    "מזכירה רפואית לא יכולה לראות סיכומים. [...] כאילו בסוף גם מבחינה קלינית לא יכול להיות שהפסיכיאטר יראה מטופל שיש לו עבר פסיכיאטרי מבלי לראות את העבר."
</div>
<div class="critical-box">
    <strong>אילוץ הרשאות:</strong> מזכירות רפואיות <strong>אינן יכולות</strong> לצפות בסיכומים פסיכיאטריים (הגבלת הרשאות). אם השליפה לא תהיה אוטומטית דרך API, תידרש הרשאה של גורם רפואי מוסמך. יהודה אישר שקלינית — הפסיכיאטר חייב לראות את ההיסטוריה הפסיכיאטרית לפני תחילת הטיפול.
</div>
<table>
    <thead><tr><th>נתון</th><th>תיאור</th><th>עדיפות</th></tr></thead>
    <tbody>
        <tr><td>סיכום iFeel</td><td>שאלוני אינטייק, הערכה ראשונית, מסע מטופל</td><td><strong>גבוהה</strong></td></tr>
        <tr><td>סיכומים פסיכיאטריים קודמים</td><td>סיכומי ייעוץ מפסיכיאטרים קודמים</td><td><strong>גבוהה</strong></td></tr>
        <tr><td>היסטוריית אבחנות</td><td>אבחנות פסיכיאטריות קודמות</td><td>גבוהה</td></tr>
        <tr><td>היסטוריית תרופות</td><td>תרופות פסיכיאטריות קודמות</td><td>גבוהה</td></tr>
    </tbody>
</table>
"""

def build_section_9(imgs):
    return """
<h1 class="page-break">9. חוק ניוד המידע ו-FHIR</h1>
<p>בישיבה נדונו ההשלכות של חוק ניוד המידע הרפואי והמעבר לתקן FHIR על אפשרויות האינטגרציה העתידיות.</p>
<div class="quote-box">
    <span class="speaker">שלומי (מכבי):</span> "עד 2027 כל הקופות צריכות לעבור ל-FHIR. זה אומר שבעתיד, הגישה למידע הרפואי תהיה סטנדרטית הרבה יותר. אבל עד אז, אנחנו עובדים עם מה שיש."
</div>
<h2>9.1 חוק ניוד המידע הרפואי</h2>
<p>חוק ניוד המידע הרפואי מחייב את קופות החולים לאפשר העברת מידע רפואי בפורמט מתוקנן. ההשלכות על תליאז:</p>
<ul>
    <li>בעתיד, גישה לנתוני מטופל תהיה דרך API סטנדרטי (FHIR)</li>
    <li>לא נדרשת אינטגרציה ייעודית לכל קופה — תקן אחיד</li>
    <li>אך לוח הזמנים (2027) רחוק מכדי להמתין</li>
</ul>
<h2>9.2 FHIR — Fast Healthcare Interoperability Resources</h2>
<table>
    <thead><tr><th>היבט</th><th>מצב נוכחי</th><th>מצב יעד (FHIR)</th></tr></thead>
    <tbody>
        <tr><td>פורמט נתונים</td><td>פרופריאטרי (קליקס)</td><td>JSON/XML סטנדרטי</td></tr>
        <tr><td>Authentication</td><td>Citrix + פנימי</td><td>OAuth 2.0 / SMART on FHIR</td></tr>
        <tr><td>Resources</td><td>טבלאות פנימיות</td><td>Patient, Encounter, Medication, Observation</td></tr>
        <tr><td>תיעוד</td><td>פנימי בלבד</td><td>תקן פומבי</td></tr>
        <tr><td>זמינות</td><td>היום (נדרש API ייעודי)</td><td>2027 (לפי הרגולציה)</td></tr>
    </tbody>
</table>
<h2>9.3 אסטרטגיה מומלצת</h2>
<div class="info-box">
    <strong>גישה דו-שלבית:</strong>
    <ol>
        <li><strong>לטווח קצר (2026):</strong> אינטגרציה באמצעות API ייעודי מול קליקס (כמתואר במסמך זה)</li>
        <li><strong>לטווח ארוך (2027+):</strong> מעבר ל-FHIR כשהתקן יהיה זמין, תוך שמירה על תאימות לאחור</li>
    </ol>
</div>
"""

def build_section_10(imgs):
    return """
<h1 class="page-break">10. מחיצת בריאות הנפש — חסימת מידע מספקים חיצוניים</h1>
<p>אחד הנושאים המשמעותיים ביותר שעלו <strong>לאחר ישיבת התיאום</strong> הוא נושא <strong>מחיצת בריאות הנפש</strong> במערכת קליקס. ענת מירון, מנהלת בריאות הנפש במכבי, הבהירה באימייל מ-20 באפריל 2025 שמידע פסיכיאטרי מספקים חיצוניים <strong>חסום לחלוטין</strong> מרופאי המשפחה.</p>
<div class="quote-box">
    <span class="speaker">ענת מירון (מנהלת בריאות הנפש, מכבי) — אימייל, 20 באפריל 2025:</span>
    "ישנה מחיצה של בריאות הנפש. רופא ראשוני לא יכול לראות מידע של בריאות הנפש של ספקים חיצוניים. [...] כשהספק החיצוני שולח תשובת יועץ, היא לא מגיעה לרופא אלא רק למרפאת בריאות הנפש המחוזית."
</div>
<div class="quote-box">
    <span class="speaker">דקל תליאז (מנכ"ל תליאז) — מהישיבה:</span>
    "אם הרופא המשפחתי לא רואה את הסיכום שלנו, זה מבטל את כל הערך של האינטגרציה. חייבים למצוא פתרון לזה."
</div>
<div class="quote-box">
    <span class="speaker">שחר שגב (מנהלת מרפאת בריאות הנפש, מכבי מרכז) — מהישיבה:</span>
    "המחיצה היא מכוונת — היא מגינה על פרטיות המטופל. אבל יש מקרים שבהם רופא המשפחה צריך לדעת על הטיפול הפסיכיאטרי, ואז אנחנו מעבירים את המידע ידנית."
</div>
<div class="critical-box">
    <strong>השלכה קריטית על אינטגרציית API:</strong> גם אם תליאז תעלה סיכומים באמצעות API ישירות לקליקס, ייתכן שהמחיצה תחסום את הגישה של רופא המשפחה למידע זה. יש לברר: (א) האם ניתן לשלוח תשובת יועץ שתעקוף את המחיצה, (ב) האם נדרש אישור של מרפאת בריאות הנפש המחוזית, (ג) האם המטופל יכול לתת הסכמה לשיתוף המידע.
</div>
<h2>10.1 השלכות על אסטרטגיית האינטגרציה</h2>
<p>נושא המחיצה משנה את סדר העדיפויות של האינטגרציה:</p>
<ul>
    <li><strong>תשובת יועץ:</strong> יש לוודא שה-API יודע לנתב את התשובה גם לרופא המשפחה וגם למרפאת בריאות הנפש</li>
    <li><strong>הרשאות:</strong> ייתכן שנדרשת הרשאה מיוחדת כדי לעקוף את המחיצה</li>
    <li><strong>הסכמת מטופל:</strong> ייתכן שנדרש מנגנון הסכמה דיגיטלי של המטופל לשיתוף מידע פסיכיאטרי עם רופא המשפחה</li>
</ul>
<div class="decision-box">
    <strong>מסקנה אסטרטגית:</strong> נושא המחיצה הוא חסם פוטנציאלי מרכזי. יש לקבוע פגישה ייעודית עם ענת מירון וצוות האדריכלות של מכבי לפני תחילת הפיתוח, כדי למפות את כללי המחיצה ולתכנן את ה-API בהתאם.
</div>
"""

def build_section_11(imgs):
    return """
<h1 class="page-break">11. מקרי בדיקה ושרשרת אימיילים — התנסות עם הכספת</h1>
<p>במהלך מרץ-אפריל 2025, תליאז ביצעה סדרת <strong>מקרי בדיקה</strong> עם מנגנון הכספת כדי לבחון את היתכנות העלאת סיכומים אוטומטית. להלן תוצאות הבדיקות:</p>
<table>
    <thead><tr><th>מס׳</th><th>ת.ז. (חלקי)</th><th>תיאור</th><th>שאלה שנבדקה</th><th>תוצאה</th></tr></thead>
    <tbody>
        <tr><td>1</td><td>***4567</td><td>סיכום אינטייק — העלאה ראשונה</td><td>האם המסמך מגיע לתיק?</td><td>הגיע לתיק אך לא לדואר רפואי</td></tr>
        <tr><td>2</td><td>***4567</td><td>סיכום מעקב — אותו מטופל</td><td>האם רופא המשפחה רואה?</td><td>לא — המסמך בתיק אך ללא התראה</td></tr>
        <tr><td>3</td><td>***8901</td><td>מטופל חדש — אינטייק</td><td>האם נוצרת תשובת יועץ?</td><td>לא — הכספת מעלה קובץ, לא תשובת יועץ</td></tr>
        <tr><td>4</td><td>***2345</td><td>סיכום עם קוד אבחנה</td><td>האם ICD נקלט?</td><td>לא — הכספת לא תומכת בשדות מובנים</td></tr>
    </tbody>
</table>
<h2>11.1 שרשרת אימיילים — ציר זמן</h2>
<p>להלן ציר הזמן המלא של ההתכתבות בנושא הכספת והאינטגרציה:</p>
<table>
    <thead><tr><th>תאריך</th><th>שולח</th><th>נושא</th><th>תוכן עיקרי</th></tr></thead>
    <tbody>
        <tr><td>9/3/25</td><td>ד"ר ראמי ח׳ורי</td><td>פנייה ראשונית לשלומי</td><td>בקשה לבחון אפשרויות אינטגרציה עם קליקס</td></tr>
        <tr><td>12/3/25</td><td>שלומי (מכבי)</td><td>תשובה ראשונית</td><td>הפנייה לכספת כפתרון מיידי + הזמנה לישיבה</td></tr>
        <tr><td>19/3/25</td><td>כולם</td><td>ישיבת תיאום</td><td>ישיבה פנים-אל-פנים — ראו סעיף 2</td></tr>
        <tr><td>24/3/25</td><td>ד"ר ראמי ח׳ורי</td><td>מסמך מפרט טכני v1</td><td>טיוטה ראשונה של מסמך זה</td></tr>
        <tr><td>2/4/25</td><td>שלומי (מכבי)</td><td>עדכון כספת</td><td>פרטי גישה לכספת לבדיקות</td></tr>
        <tr><td>8/4/25</td><td>ד"ר ראמי ח׳ורי</td><td>דיווח בדיקה #1-2</td><td>סיכומים הועלו אך לא הגיעו לרופא המשפחה</td></tr>
        <tr><td>10/4/25</td><td>שלומי (מכבי)</td><td>תשובה</td><td>בדיקה פנימית — הכספת לא יוצרת תשובת יועץ</td></tr>
        <tr><td>15/4/25</td><td>ד"ר ראמי ח׳ורי</td><td>דיווח בדיקה #3-4</td><td>אישור שהכספת לא מתאימה לצרכי תליאז</td></tr>
        <tr><td>20/4/25</td><td>ענת מירון (מכבי)</td><td>עדכון מחיצה</td><td>הבהרה על מחיצת בריאות הנפש — ראו סעיף 10</td></tr>
        <tr><td>22/4/25</td><td>ד"ר ראמי ח׳ורי</td><td>מסמך מפרט v2</td><td>גרסה מעודכנת כולל ממצאי כספת ומחיצה (מסמך זה)</td></tr>
    </tbody>
</table>
<div class="critical-box">
    <strong>מסקנה:</strong> הכספת אינה מתאימה כפתרון קבוע לתליאז. היא מעלה קבצים בלבד, ללא יצירת תשובת יועץ, ללא שדות מובנים (ICD, תרופות), וללא התראה לרופא המשפחה. נדרש API ישיר לקליקס כפי שמתואר בסעיפים 3-6.
</div>
"""

def build_section_12(imgs):
    return """
<h1 class="page-break">12. שלבי אינטגרציה מומלצים ופריטי פעולה</h1>
<p>על בסיס הממצאים מסעיפים 1-11, להלן תוכנית האינטגרציה המומלצת בגישה מדורגת:</p>
<div class="quote-box">
    <span class="speaker">יהודה (ראש אגף מערכות מידע, מכבי) — מהישיבה:</span>
    "בואו נעשה את זה בשלבים. קודם כל תשובת יועץ, אחר כך מרשמים, ובסוף סנכרון מלא. ככה אנחנו יכולים לוודא שכל שלב עובד לפני שממשיכים."
</div>
<div class="phase-box">
    <strong>שלב 1 — תשובת יועץ (3-4 חודשים)</strong><br>
    העלאה אוטומטית של סיכום ייעוץ מתליאז לקליקס כתשובת יועץ רשמית. כולל: נרטיב קליני, אבחנות ICD, המלצות טיפול, וניתוב לרופא המשפחה. <strong>זהו ה-MVP.</strong>
</div>
<div class="phase-box-yellow">
    <strong>שלב 2 — קריאת נתוני מטופל (2-3 חודשים)</strong><br>
    שליפת דמוגרפיה, אבחנות ידועות, תרופות נוכחיות ואלרגיות מקליקס אל תוך פלטפורמת תליאז. מפחית הזנה ידנית ומשפר בטיחות קלינית.
</div>
<div class="phase-box-orange">
    <strong>שלב 3 — מרשמים (3-4 חודשים)</strong><br>
    הפקת מרשמים אלקטרוניים באמצעות API — כולל חיפוש תרופה, הגדרת מינון, וחתימה דיגיטלית. דורש אישור רגולטורי נוסף.
</div>
<div class="warning-box">
    <strong>&#9888; מורכבות מרשמים:</strong> יהודה הדגיש בישיבה שמרשם בקליקס <strong>אינו עומד בפני עצמו</strong> — הוא תוצר של ביקור (visit). כדי להוציא מרשם, יש קודם לפתוח ביקור, להזין אבחנה, ולהזין פעולה: "כדי להוציא מרשם אני חייב קודם למלא את השדות שלפני [...] מרשם מוצא כתוצר של ביקור." לכן אינטגרציית מרשמים דורשת אינטגרציה מלאה של תהליך הביקור. עם זאת, שלומי ציין: "יכול להיות שדווקא מרשמים זה משהו קל" — ולכן יש לבחון את המורכבות בפועל עם הארכיטקט.
</div>
<div class="phase-box-red">
    <strong>שלב 4 — סנכרון מלא ו-FHIR (6-12 חודשים)</strong><br>
    סנכרון דו-כיווני מלא כולל תוצאות מעבדה, גורמי סיכון, היסטוריית ביקורים, ומעבר לתקן FHIR כשיהיה זמין (2027).
</div>
<h2>12.1 פריטי פעולה</h2>
<ol>
    <li><strong>פגישת בירור מחיצה:</strong> לקבוע פגישה עם ענת מירון וצוות האדריכלות לבירור כללי המחיצה והשלכותיה על ה-API — <em>אחראי: דקל תליאז, עד שבועיים</em></li>
    <li><strong>מסמך טכני לאדריכלות:</strong> להעביר מסמך זה (v2) לשלומי לבחינת צוות האדריכלות — <em>אחראי: ד"ר ראמי ח׳ורי, מיידי</em></li>
    <li><strong>סביבת TEST:</strong> לקבל גישה לסביבת בדיקות של קליקס — <em>אחראי: שלומי (מכבי), עד 3 שבועות</em></li>
    <li><strong>PoC תשובת יועץ:</strong> לפתח Proof of Concept להעלאת תשובת יועץ ב-TEST — <em>אחראי: צוות תליאז, חודש מקבלת גישה</em></li>
    <li><strong>בחינת בת קול:</strong> לבדוק האם ניתן להשתמש בתשתית ה-API של פרויקט בת קול — <em>אחראי: שלומי, שבועיים</em></li>
    <li><strong>ישיבת מעקב:</strong> לתאם ישיבת מעקב לאחר קבלת תשובה מצוות האדריכלות — <em>אחראי: ד"ר ראמי + שלומי, 3-4 שבועות</em></li>
</ol>
<h2>12.2 עלויות והיבטים כלכליים</h2>
<div class="quote-box">
    <span class="speaker">יהודה (מכבי) — מהישיבה:</span>
    "מבחינה כלכלית — הרי זה פרויקט, זה צורך שלכם. תליאז, אנחנו לא היינו יוצאים לפיתוח לולא לא היה לכם את הקושי הזה עם הפסיכיאטרים, ולכן העלות צריכה להיות שלכם."
</div>
<div class="quote-box">
    <span class="speaker">דקל תליאז (מנכ"ל תליאז) — מהישיבה:</span>
    "אני לא חושב, אבל בוא לא נלאה את שלומי פה באירוע הזה. אני לא מסכים."
</div>
<div class="quote-box">
    <span class="speaker">שלומי (מכבי) — מהישיבה:</span>
    "אני מסכים, באמת תוציאו אותי מהתימונה כרגע. אני יכול לבוא עם הערכות ולהסביר מה המשמעות [...] שנשים ארכיטקט חינם, בסדר, כרגע לא עולה כסף."
</div>
<div class="decision-box">
    <strong>סיכום כלכלי:</strong> קיימת מחלוקת בין יהודה (מכבי) לדקל (תליאז) לגבי נשיאת עלויות הפיתוח. שלומי ביקש לדחות את הדיון הכלכלי ולהתחיל בשלב ההערכה הטכנית <strong>ללא עלות</strong>. ההחלטה הכלכלית תתקבל לאחר שהארכיטקט יציג את ההערכה ליהודה.
</div>
"""

def build_footer(imgs):
    return """
<hr>
<p style="text-align: center; color: #888; font-size: 9pt; margin-top: 1cm;">
    מסמך זה הופק על בסיס:<br>
    (1) ישיבת תיאום תליאז-מכבי, 19 במרץ 2026<br>
    (2) שרשרת אימייל בנושא אינטגרציית קליקס, מרץ 2026<br>
    (3) הקלטת מסך של אלי׳אס ג׳הג׳אה, 22 בנובמבר 2024 — זרימת עבודה מלאה בקליקס EHR
</p>
"""

def build_html():
    imgs = {}
    for f in sorted(SCREENSHOTS_DIR.glob("*.jpg")):
        imgs[f.name] = img_to_data_uri(f)
    css = build_css()
    cover = build_cover(imgs)
    toc = build_toc(imgs)
    sections = [build_section_1(imgs), build_section_2(imgs), build_section_3(imgs),
                build_section_4(imgs), build_section_5(imgs), build_section_6(imgs),
                build_section_7(imgs), build_section_8(imgs), build_section_9(imgs),
                build_section_10(imgs), build_section_11(imgs), build_section_12(imgs)]
    footer = build_footer(imgs)
    body = cover + toc + "".join(sections) + footer
    return f"""<!DOCTYPE html>
<html lang="he" dir="rtl">
<head><meta charset="UTF-8"><style>{css}</style></head>
<body>{body}</body></html>"""

def main():
    print("Building v2.0...")
    html_content = build_html()
    html_path = OUTPUT_PDF.with_suffix(".html")
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"HTML saved to: {html_path}")
    print("Generating PDF...")
    html = HTML(filename=str(html_path))
    html.write_pdf(str(OUTPUT_PDF))
    print(f"PDF saved to: {OUTPUT_PDF}")
    size_mb = os.path.getsize(OUTPUT_PDF) / (1024 * 1024)
    print(f"PDF size: {size_mb:.1f} MB")

if __name__ == "__main__":
    main()
