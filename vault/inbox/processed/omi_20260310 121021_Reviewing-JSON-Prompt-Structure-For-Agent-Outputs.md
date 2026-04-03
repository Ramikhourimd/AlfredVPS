---
processed_at: '2026-03-17T16:23:03.311536+00:00'
status: processed
---

# Reviewing JSON Prompt Structure For Agent Outputs

**Source:** Omi (omi)
**Date:** 2026-03-10 12:10:21
**Language:** en
**Category:** technology

## Summary

The speaker discusses work on a system where prompt fields are fully reflected in a JSON-based result. They explain that they collaborated with someone named Sethi ("Seti") to understand which fields the model returns and how the prompt processes and transforms them. The conversation mentions building all the agents and flows, and wanting to connect the understanding module to inspect how the data is processed. The goal is for the result to include a string containing all fields so Sethi can later refine the prompt—adding or fixing missing lines or fields—without being tied to a specific agent implementation. They also talk about choosing the output language and making output interpretation less dependent on any particular model or agent, so the system can robustly parse and understand results regardless of which agent generates them.

## Transcript

**SPEAKER_0:** Hey. אי אמי, מה נשמע? אתה יכול לא כול זה מ שהו שזה זה מ שהו ש אל לא מה העניינים? بس يا جماعه Telefon telefon lütfen. ב או לי יו מיים של פר סה אח רו נים שה כאילו אתה יודע את ה נ תונ ים ב הת חלה וא ז ו כל ה ס דות ב תוך ה רי זול ט. זאת אומרת כל ה כל כל ש דה מ תוך ה פרו מ ט מו פיע לו בתוך ה רי ט כדי שה וא בעצם יו כל לקלוט את זה.
**SPEAKER_0:** אוקיי? אוקיי. ע כשיו, ע בד תי עם עב דתי עם סת יו כדי ל דעת מה בע צם ה ס דות שה יא מח זיר ה, זאת אומרת איז ה ש דות מ גי עים? מה ה פו מ ט עושה? איך הוא מ אבד את זה?
**SPEAKER_0:** . Și Zesi cum סי כום ק יס מ נ דר כאילו לפני הפסי כי אטר, אחרי לפני פ גישה פסיכיאטר. ו ר אית כל הר צ פים בנו יים, זאת אומרת כל הסו כ נים בנויים וזה.
**SPEAKER_0:** ור ציתי לח בר כבר את המ וד ה בי נה ל ראות באמת ש איך ה עיב וד יו צא, זאת אומר ת ש סת ו תו כל כבר ל ש נות את ה פרו מ ט ב ה ם ל מה ש צריך, כאילו נ גיד אם ח סר שור ה, ח סר זה, ח סר זה, אבל זאת אומרת ב מ ב נה ג'יי סון, ש בר זול ט מו פיע סט רינ ג של כל ה ס דות, וא ז הוא אומר לי אחרי ש אני אק בל את זה ככ ה, מ צי די תע בור חוד ש על הפרומט.
**SPEAKER_0:** ב איזה ש פה הוא רו צה ש נו ציא לו את זה. וא ז זה פ חות יש נה בין סו כן ל סו כן, כי אז הוא א ז הוא י בין את ה או ט פו ט, ש זה לא יהיה משהו ש ת לוי ב פרו מ פ ב סו כן מ סוים, אתם מבין?
**SPEAKER_0:** כן. או קיי. כי אז לא עשינו כלום.