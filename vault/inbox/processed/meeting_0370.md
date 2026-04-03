---
alfred_tags:
- healthcare/clinic-operations
- finance/payroll-billing
- hr/team-management
processed_at: '2026-02-26T20:23:58.016854+00:00'
relationships:
- confidence: 0.85
  context: Semantically clustered meetings
  source: inbox/processed/meeting_0370.md
  target: inbox/processed/meeting_0378.md
  type: related-to
- confidence: 0.85
  context: Semantically clustered meetings
  source: inbox/processed/meeting_0370.md
  target: inbox/processed/meeting_0393.md
  type: related-to
- confidence: 0.85
  context: Semantically clustered meetings
  source: inbox/processed/meeting_0370.md
  target: inbox/processed/meeting_0399.md
  type: related-to
status: processed
---

# Meeting: 01-18 تحسين عملية استقبال المرضى للخدمات النفسية

---

## 1. Meeting Details

| Field | Value |
| :--- | :--- |
| **Date** | 2026-01-22T10:55:27.639Z |
| **Title** | 01-18 تحسين عملية استقبال المرضى للخدمات النفسية |
| **Classification** | {"meeting_id":"HM-BASEL-WEEKLY","meeting_name":"Meeting with Basel","category":"HealthyMind Clinical Operations","confidence":0.76,"confidence_level":"HIGH","is_active":true,"is_new_suggestion":false} |
| **Category** | HealthyMind Clinical Operations |
| **Meeting Type** | HealthyMind Clinical Operations — Recurring Weekly 1:1 (with additional attendees) |
| **Source Document** | [https://docs.google.com/document/d/15jgPJU9iyGAeqfMPxofvZAfYAGlHGkreUSofrvmQUPY/edit?usp=drivesdk](https://docs.google.com/document/d/15jgPJU9iyGAeqfMPxofvZAfYAGlHGkreUSofrvmQUPY/edit?usp=drivesdk) |

## 2. Participants

| Name | Role | Confidence |
| :--- | :--- | :--- |
| Rami Khouri | Chief Medical & Innovation Officer | 0.91 |
| Basel Kanaaneh | General Director of Operations | 0.72 |
| Unknown (possible junior staff/admin) | Unidentified | 0.25 |
| Shachar Segev | VP R&D | 0.61 |
| Unknown (background/external participant or audio artifact) | Unidentified | 0.1 |


## 3. Key Topics

* Maccabi/HealthTech integration and patient intake workflow design
* Psychiatrist referral pipeline and routing patients after Xander screening
* Xander patient flow and operational handoffs to psychiatry
* Operational metrics
* volumes
* and cost/finance considerations
* Product roles and resourcing (Product Manager / Product Designer; exec assistant/admin workload)
* Maccabi app behavior and bugs (filters
* adult vs youth visibility
* 'App Review Needed' flow)

## 4. Full Transcript

> **Note:** Transcript language matches the original meeting language.

---

```
Rami Khouri 00:00:01<br>تسقوا بالعليوت, انا اللي بستخيارات 18000 مكلفني اكتر, اللي مش تنام لقالي عشان بتفاولي عالي بس عالي.<br>Basel Kanaaneh 00:00:12<br>سيد همني لعبنا على هالوطن. مكلفنا عاليش؟ مكلفنا سبعة.<br>Rami Khouri 00:00:29<br>اسمها يودا بدو في شركة اسمها ايفي. ايفيل اللي هي كنارية اخذت مخلص تبع تكنولوجيا في قلب مكابي, مكابي. هدول بيعملوا زي شو احنا بنعمل من نهاية كل شيء. فيودا بدو انه هني يحليف.<br>Rami Khouri 00:00:60<br>يصير يبعتلنا امتكام للبسيخياتر دغري بعد ما يمرقوا على خاندر.<br>Basel Kanaaneh 00:01:09<br>المدفع اللي يمرق على خاندر باي فيل ويجل عنا لانت بسيخياتر دغري.<br>Rami Khouri 00:01:13<br>اه.<br>Basel Kanaaneh 00:01:14<br>يعني يفشش لها في شألون فيش منها فيك.<br>Rami Khouri 00:01:17<br>في اشياء الحيوبي, واحد التهليق الشليكتسي اللي معناش هيك اليوم, فحصيح لانه بكب انه كبار عبارة شليكتسية كبار هاي مش بتصل لك وبيكون بده بسيخولك بطلع بده بسيخياتر وبيكون بده بعشو, اثنين انا بغضب هني بدنا نشوف في ناحية الكاليت ما زقنا.<br>Rami Khouri 00:01:47<br>لانه اليوم احنا منقبض على انتك بسيخياتر وانتك من الهالتيك, منو يقف هنيك اصلا, اللي هوش تب يشوفك اذا بدرون احنا يقصوه, لبقشة واحدة. ينزلوا 300 شيء يقصوه بالنص, ادفعولنا بس على بقشات في اصلا هاي الكود, نص ما نقولي بس بعرف شو هذا, بس بو نجيب انهم تمحروه اتو.<br>Rami Khouri 00:02:23<br>نص بعيدي اذا قاموا كيف يخول جزء من هالتيك حسب بياحس واحد احنا شو بنفع نيجي نعمل, بنفع نيجي نعمل شغلتين نخلي بقشاتي من هالتيك, كجزء من الفلاش الاولين مع الموتوفار.<br>Rami Khouri 00:02:57<br>بطريقتين الابتسية الاولى هي, أنه يكون مفقاش كتساب زي معكاف, على نفس كود المعكاف, بس قبل جيشات البسيخياتر, يعني إذا إجا آيفيل كفعوه أنا أعطيهن يوماً لبسيخياتر, كفعوه, كفعت بسيخياتر لعشرين شهر أنا باجي وبحط ربع ساعة قبل جيشات البسيخياتر, سحامة من هالتيك.<br>Rami Khouri 00:03:30<br>اللي هي تخينته من ناحية يفوت من هالتيك يشرح له عنه.<br>Basel Kanaaneh 00:03:33<br>بعد ما نبلش نشتغل فيه أصدق إنه يصير عندنا التهليخ ساعتها إنه بالأول فيه هالتيك اللي هي زي المعكاف وبعد شهرين, وبعدين أنت البسيخياتر.<br>Rami Khouri 00:03:45<br>آه هاي الأبتية الأولى, الأبتية الثانية.<br>Basel Kanaaneh 00:03:49<br>ونظل نأخذ نفس التعريف على هالأبتية.<br>Rami Khouri 00:03:51<br>اللي هو منوية 80 ملايك, بقى بعرفش كيف شو بده نعمل بالمنوية 80 ملايك بقى أنا بقدر أجي أحسبها هيك معكاف, معكف من الهيل تيك, اللي احنا بنربح عليه منيها. او بحطه بعد بجيشات لبسيخيات. يعني بسيخيات اللي بيعمل ان تيك بيفوت من الهيل تيك بعدين من ساكين بيفحص هل كل شي كان تمام فيمت الهاملات صوت تتتت.<br>Rami Khouri 00:04:21<br>وهدا انا اللي رح اقوم انا اللي مهم ليه اخليها على بجيشات من الهيل تيك, متكونش ساحة تليفون يكون في بجيشة واحد لواحد بالاول عشان تتعرف مين هذا البنادر, او اذا قمت اشيالي, وساعتها تصلك تليفون يعني مين انتي شو بدك ميني, لا اعملهاش من المنفع تخليها نشوف, اعملها مع كم كفو يعني متكونش عشر دقايق تكون ربع ساعة عشان تلفي فيديو.<br>Rami Khouri 00:04:52<br>بدك وقت وكذا, بس زي يخلي يوت معنين, بتلك كمان. كمان وسط السلكتيا وكمان نحن نجيب نغير هون بالمياعل يعني, نعمل جيشا جديد لمنهالتيك اللي هي اكتر يعيلا على اسم اخمداع اللي اخدناه من بره اهو عم بعملوا غادر انتك ونك كمان مش بس شئ لونك.<br>Rami Khouri 00:05:23<br>متعلق بقداش اخوت الحمر اللي منوخدو من هون منيحة اذا منيحة فساعتها منبعتو دغري لبسيخياتي, انتي مشوة؟ مشوة, لا مش كتير واضح لاني ليه انا.<br>Basel Kanaaneh 00:05:43<br>لابس, بطع فيديو على الغمر.<br>Unknown (possible junior staff/admin) 00:05:56<br>سبلت هون.<br>Rami Khouri 00:06:05<br>بس شو المشكلة؟ واحد احنا مقابدين من الداتا ده اللي احنا بحاجة لإجابة.<br>Rami Khouri 00:06:58<br>بالشتاء اكتبت حتى لو هتسمدت من ال تيك قبل البسيخיאטרيا انت ضلو بالبسيخיאטרيا هون, لانو لازم تكون البشاة تسمودة ازا عملتها قبل زي كيف اليوم المتوبال يحسن وشو يعني كمان بجاشتي مع اي فيل وكمان ما من ال تيك وعن البسيخיאטרيا ازا عملتهم تسمودة وتخلص من ناحيتو هاي البشاة التخياتر تفوت حدا قبل بحضروا يعني.<br>Rami Khouri 00:07:29<br>ويكون على نفس اللينك من ناحية يعني لازم شاحر يزبط الاشي انو نفس اللينك المتوبال بيفوت وخلص يعني بس خاطر ما تسترب لنفسك فما يحسش المتوبال اسا انو اطلع فروض اطلع, عايش وانت مفروض ما تريد معاك, بدنا نشوف شو ازا كده كل متفرر يصدير يعني بس ده نشتغل على الفلو انا وياك, نفكر فيه شو لازم نيوتون.<br>Basel Kanaaneh 00:07:59<br>وانت انت هالاسبوع عندك كم. <br>Unknown (possible junior staff/admin) 00:08:07<br>33 صباحاً. وسبت شوية كم عامل حينك. <br>Rami Khouri 00:08:26<br>3 اربعه 12.<br>Unknown (possible junior staff/admin) 00:08:28<br>انا 13 عام 12.<br>Basel Kanaaneh 00:08:44<br>لانه برضو هون طالب مني, بده يعني الاشي مماشي السعراء عن شبوع بقى.<br>Basel Kanaaneh 00:09:43<br>موسيقى. لا أعرف ماذا تسمينها Product Manager Product Designer تفهم أن القطار الخاص بنا هو أخيب.<br>Basel Kanaaneh 00:10:16<br>أنا أقوم بعمله. لازم يشد راق, لا لا أنا مش فاعل, آخر مرة يوم الفميس سألها أنت لماذا تعلمت. طيب لماذا أنت تعملي القطار هي عملت القطار. تحليته هي رؤات حشبون هي عرق الدين.<br>Basel Kanaaneh 00:10:47<br>Product Designer.<br>Rami Khouri 00:11:22<br>قال لي واحد اتصاف تلات منستراتيفي. بتاكن الاتكانيم اللي مفروض توحرانها شو؟ 26 كيدايني جايز فيه حدا بالنصرامة لاني, كعزارة شيء لو بحاجة لحدا ان في كتير شغلات.<br>Rami Khouri 00:11:60<br>نشأبيه مكتر من اللازم للاشياء حتى انتي, ودارك عيش اوبراسيا تنشأب للمنستراتي, بالرمال هايبل كبس, انت حس انه في عندك كفاية كلم انك تفتصيع اوبراسيا. انا في كتير مرات بضيع وانا حاسس انك انت عم بص ببلش يصيبك مس الشي.<br>Rami Khouri 00:12:32<br>مش عشان في خلود لانه النهول هاد شوت هو كبير. شوت حدا اللي هو يكون جزء من المسارات تبعته يعني عزب انا مش حاجة استعملوه اللي عندي ناس من الحدشة نوت لا الك.<br>Rami Khouri 00:13:09<br>بس عزيزة يعني executive assistant. بدي اسه هيك بدي تطلعلي هيك بدي مهما شبه خمسين مرة بيعمل.<br>Unknown (possible junior staff/admin) 00:13:30<br>ما رأيك بالتصورخ بالأول. <br>Basel Kanaaneh 00:13:39<br>أعتقد أنه لازم، لكن مش عارف بعض التصورخ لأنه بسريط ولا لأنه بسريط. تنساش وعليك مش واصل.<br>Rami Khouri 00:14:08<br>عندك يبنى هذا ما لازم. يعني ليه بعدك مش واصل. <br>Basel Kanaaneh 00:14:17<br>أوليش بدي يوم كامل أعطا فرج جريد أعمل جريد على.<br>Unknown (possible junior staff/admin) 00:14:36<br>اشتركوا في القناة.<br>Unknown (possible junior staff/admin) 00:16:29<br>اوه جميل. بخلال الامر يجب ان اعلم انها محبوبة.<br>Rami Khouri 00:17:22<br>انها محبوبة نفسيا. سلام, انا احب.<br>Basel Kanaaneh 00:17:41<br>اشتركوا في القناة.<br>Rami Khouri 00:19:17<br>انا قررت اتفوت هون يعني اتشتغلف كمان شوية.<br>Unknown (possible junior staff/admin) 00:19:25<br>تبقى المسلوك مع احنا ب...<br>Rami Khouri 00:20:47<br>انتم تعملوا.<br>Rami Khouri 00:22:27<br>قبل يومين فوتت لو كنا بمص الشهر كنا كبار فيه قريب الـ 600 متوبرال جدا راح نقبط سيفة تبعالكس. مدريعة زماننا متناه بس هو مدريعة. أفشار الخطعمات بياعد زمان الهامتنان.<br>Rami Khouri 00:22:59<br>بس مش بياعد الفينانسي. بياعد الفينانسي.<br>Basel Kanaaneh 00:23:03<br>بياعد متوكليم حداشين مش زمان الهامتنان متوكليم حداشين.<br>Shachar Segev 00:23:09<br>يعني يوم الأحد الماضي كان كيانات ساعة أبناء.<br>Rami Khouri 00:23:16<br>إنت بالآخر لازم توصل لوضع, اللي يكون فيه عدد من إنتكام من أهلاتك وعدد من إنتكام بسيخיאטרيا أنت جارتي متسيل بسيخיאטרيا نعم.<br>Shachar Segev 00:23:25<br>نحن في هذا الجزائر نشتغلوا ثلاثة يوم الأحد.<br>Basel Kanaaneh 00:23:37<br>عارفة ليه؟ מכבי ب... لما اللي كوح يكون على قطار تبعها ندور على بسيخיאטרيا كان يطلع لهن الرفاقين, إسه صار يطلع لهن الرفاقين بس مع سرقيل كفوة أنه فيه إفشاروت لبسيخיאטרيا. كنا دائما نبين بصفحات زينا زي الباقي بس صلنا من مصابيال.<br>Shachar Segev 00:24:02<br>وفي ايش كمان صار غريب في اخر عنا كنت مدقفوت اعمل اشير מכבי بالابليكيجين ريبيو نيديد كان يبين كل حدا מכבי, وصطلع ان الولاد لحال والبوغارين لحال من ولادها قلبي شان.<br>Basel Kanaaneh 00:24:24<br>ما كانوش يبينوا مع بعض فما كنتش تشوف الأولادين.<br>Shachar Segev 00:24:29<br>كانوا يبينوا مع بعض اول, راحت باتتلي شيرة عادي قلت لي في واحدة فعلت امرأة بلادات ثلاثي مش مبينة مش مبينة, فكر غلط اسم واحد بياندر عم بيستنى الاشارة تفجر الشمال.<br>Unknown (possible junior staff/admin) 00:24:57<br>اشارتي نعيمة 120 احد انا سمعت عن فلم فلسطين.<br>Shachar Segev 00:25:18<br>انا سمعت عن مريض جاسي. انا سمعت عن فلم فلسطين انا سمعت عن مريض جاسي.<br>Basel Kanaaneh 00:26:26<br>كل يوم بيجي بيشي.<br>Rami Khouri 00:26:27<br>شوف لتليرس.<br>Basel Kanaaneh 00:26:28<br>بدل ما رامي علم شام شام عم تعلم رامي.<br>Rami Khouri 00:26:34<br>واسا كابوتشينو اساسينـو.<br>Basel Kanaaneh 00:26:37<br>كل يوم بيجي بيشـي. ولسا مخـوت اللي وريـت.<br>Rami Khouri 00:26:43<br>اسمع اليوم الصبح فاتحة تليفون أماني وعم بتخط على فيديوهات, وعندن الفيديوهات كان لعلاء عزام, ليلة الميلاد وعندن الفيديوهات كان لعلاء عزام, عم بيغني مولاي. اه وتركتها تركتها تسمع انو ما علبتش الفيديو حطته تسمع ولا ماني انتبهت شو صار لسه, سمعت مولاي وتركتها اللي تنشأش سمعتها رب.<br>Rami Khouri 00:27:15<br>بدي اسمعها لعلاق. يا الله ياعلاق لو انك مجنيني خلص.<br>Shachar Segev 00:27:30<br>مراتـه رفيـع مراتـه كاسم رفيـع.<br>Rami Khouri 00:27:33<br>مراتـه سطـل الله ومن سنة الثلج.<br>Shachar Segev 00:27:38<br>جـوز رفيـع.<br>Rami Khouri 00:27:44<br>مسيحية كانت لا هي أرثوذكس حتى ومش مسيحية ومسلمة. كان بدو يجدد بس.<br>Unknown (possible junior staff/admin) 00:28:09<br>مجدد.<br>Rami Khouri 00:28:17<br>بعتـيها دخـول اماني. بالمنـوصل مش منها بيوتيوب. اماني بعتـيلي مولاي بسرعة بالمنـوصل بدي اسمعها.<br>Shachar Segev 00:28:43<br>مولاي. <br>Rami Khouri 00:28:46<br>تابعـت علاء.<br>Unknown (possible junior staff/admin) 00:28:49<br>يلا باي.<br>Rami Khouri 00:29:16<br>المشكلة فيها أمر. لأنها تخـونها تبعيد عند كل عمر.<br>Basel Kanaaneh 00:29:42<br>شفت هذا الفيديو اللي اتنين قاعدين مقابلة مرة مصرية وأخرى واحدة, أبصر شو واحد المذيع بسألهن على بموضوع الطاقة وأبصر إيش مهم إنه حكى يعني المذيع وبعدين سأل السؤال سألني اتنين قاعدين أظنك واحد ومش حاكي يعني المرة بالأول, أظنك حكى سأل السؤال أرضك دغري أنا أفكر إني أختلف مع السيدون.<br>Basel Kanaaneh 00:30:23<br>اشتركوا في القناة.<br>Unknown (background/external participant or audio artifact) 00:30:55<br>اشوف سمادراك. مالك.<br>Unknown (background/external participant or audio artifact) 00:31:26<br>موسيقى
```