---
processed_at: '2026-02-26T20:07:38.952552+00:00'
status: processed
---

# Meeting: Talk with David (rami khouri) | Feb 20, 2025 (Transcript)

---

## 1. Meeting Details

| Field | Value |
| :--- | :--- |
| **Date** | 2025-08-02T00:03:00.025Z |
| **Title** | Talk with David (rami khouri) | Feb 20, 2025 (Transcript) |
| **Classification** | AI Architecture Consulting Session with David Szabo-Stuban |
| **Category** | N/A |
| **Meeting Type** | N/A |
| **Source Document** | [https://docs.google.com/document/d/1SR97fS_y_u_O2IYvcqkYfh8eGSH8eQ96SL7UDnN4F8g/edit?usp=drivesdk](https://docs.google.com/document/d/1SR97fS_y_u_O2IYvcqkYfh8eGSH8eQ96SL7UDnN4F8g/edit?usp=drivesdk) |

## 2. Participants

| Name | Role | Confidence |
| :--- | :--- | :--- |
| Dr. Rami Khouri | Chief Medical & Innovation Officer / CEO, HealthyMind | 0.98 |
| David Szabo-Stuban | External AI Solutions Architect / Consultant (Hungary-based IT firm) | 0.97 |
| Vivian | Unidentified (briefly present with Rami, did not participate meaningfully) | 0.4 |

## 3. Key Topics

- AI architecture consulting for HealthyMind use-cases
- Clinical workflow augmentation: visit transcription
- summarization
- differential diagnosis support
- Chatbots and multi-agent system design
- Automation/orchestration tools: n8n and Langflow
- Data/backend stack considerations: Supabase
- Integration context: EHR/clinical records and summaries
- LLM evaluation/selection and performance considerations (e.g.
- Gemini Flash mentioned)

## 4. Full Transcript

> **Note:** Transcript language matches the original meeting language.

---

```
David Szabo-Stuban (02:17): Of 
Unknown (02:17): Robbie. 
David Szabo-Stuban (02:18): Hey. 
Dr. Dr. Rami Khouri (02:20): Hi. Can I hear you? 
Dr. Dr. Rami Khouri (02:22): Yep. 
Dr. Dr. Rami Khouri (02:23): Are you? 
David Szabo-Stuban (02:25): Hello. It's been a while. 
Dr. Dr. Rami Khouri (02:28): Yeah. 
Dr. Dr. Rami Khouri (02:30): Alright. 
Dr. Dr. Rami Khouri (02:31): You? 
David Szabo-Stuban (02:32): Good. I'm doing good. I was looking forward to this call. 
Dr. Dr. Rami Khouri (02:38): Yeah. 
David Szabo-Stuban (02:38): We need to we need to catch up. 
Unknown (02:41): conversation. December 
David Szabo-Stuban (02:40): Upon the last was a long time ago. 
Dr. Dr. Rami Khouri (02:45): Yeah. And a lot of things, you know, 
Dr. Dr. Rami Khouri (02:48): changed. And, 
Dr. Dr. Rami Khouri (02:51): We had progress in some of the things 
David Szabo-Stuban (02:54): Mhmm. 
Dr. Dr. Rami Khouri (02:56): So I plan to try and remove something to take you before the 
Dr. Dr. Rami Khouri (03:00): thing, but, didn't go 
Dr. Dr. Rami Khouri (03:03): building to the plan, 
Dr. Dr. Rami Khouri (03:06): So I will try to give you 
Dr. Dr. Rami Khouri (03:10): go over the, documents I sent you. 
David Szabo-Stuban (03:14): I I have briefly, but it's 
Dr. Dr. Rami Khouri (03:16): it's 
David Szabo-Stuban (03:17): in a while ago, and you said, look, if you want to send me some stuff, 
David Szabo-Stuban (03:21): and you need some time. 
David Szabo-Stuban (03:22): We can reschedule. It's fine. 
David Szabo-Stuban (03:25): Okay. I'm not gonna count this as a session. 
David Szabo-Stuban (03:29): If you will if you need to get back into the context or anything. 
David Szabo-Stuban (03:32): So up to you, we can dive right in into it. 
David Szabo-Stuban (03:35): Or if you want to prepare, send me some new stuff based on what happened in the two 
Unknown (03:39): last months. 
David Szabo-Stuban (03:40): We can postpone to and then we can just 
David Szabo-Stuban (03:44): or 
Unknown (03:41): next week Which one 
David Szabo-Stuban (03:45): do you 
David Szabo-Stuban (03:46): which which direction you want to take? 
Dr. Dr. Rami Khouri (03:49): I think I prefer 
Dr. Dr. Rami Khouri (03:51): to 
Dr. Dr. Rami Khouri (03:52): to do the meeting right now. I 
David Szabo-Stuban (03:55): can 
Dr. Dr. Rami Khouri (03:57): a brief few 
Dr. Dr. Rami Khouri (03:58): like, on the the directions, where 
Dr. Dr. Rami Khouri (04:02): want to go to 
Dr. Dr. Rami Khouri (04:03): And, gentlemen, 
David Szabo-Stuban (04:04): Perfect. 
Dr. Dr. Rami Khouri (04:05): And I think that will 
Dr. Dr. Rami Khouri (04:07): help help me proceed. 
Dr. Dr. Rami Khouri (04:12): And, basically, 
Dr. Dr. Rami Khouri (04:15): what we talked about in our last meeting and what 
Dr. Dr. Rami Khouri (04:18): I am sent you 
Dr. Dr. Rami Khouri (04:20): is the overall flow of the clinic 
Dr. Dr. Rami Khouri (04:24): the, say, the clinical flow or the overall 
Dr. Dr. Rami Khouri (04:28): patient journey. 
Dr. Dr. Rami Khouri (04:30): From the smart 
Dr. Dr. Rami Khouri (04:31): and all the relevant aspects 
Dr. Dr. Rami Khouri (04:35): and the clinical flow relevant to what we do and 
Dr. Dr. Rami Khouri (04:40): in our work with with AI. So in general, 
Dr. Dr. Rami Khouri (04:45): we, 
Dr. Dr. Rami Khouri (04:46): focus right now. We're focusing in the automatic 
Dr. Dr. Rami Khouri (04:49): series that we, generate. 
Dr. Dr. Rami Khouri (04:52): And there's, 
Dr. Dr. Rami Khouri (04:54): The questioner, the self, questionnaire of the patients, 
Unknown (04:59): the first, 
Dr. Dr. Rami Khouri (04:58): That is point of entrance of 
Dr. Dr. Rami Khouri (05:02): the for the, AI, there's that 
Unknown (05:06): a manager 
Dr. Dr. Rami Khouri (05:06): case meeting 
Dr. Dr. Rami Khouri (05:08): that is, non psychiatric 
Dr. Dr. Rami Khouri (05:11): mental health 
Unknown (05:11): a professional. 
Unknown (05:15): the psychiatrist 
Dr. Dr. Rami Khouri (05:13): I've seen the patient before do. 
Dr. Dr. Rami Khouri (05:17): This is part of our collaborative model that is 
Dr. Dr. Rami Khouri (05:21): save time and then make our flow more efficient. 
Dr. Dr. Rami Khouri (05:26): Then there's a psychiatric meeting 
Dr. Dr. Rami Khouri (05:29): So after the questionnaire, 
Dr. Dr. Rami Khouri (05:32): automatic, summary generated and sent to the 
Dr. Dr. Rami Khouri (05:36): case 
Unknown (05:37): manager. 
Unknown (05:39): manager 
Dr. Dr. Rami Khouri (05:39): Case review it, and 
Dr. Dr. Rami Khouri (05:41): let's say, 
Dr. Dr. Rami Khouri (05:43): customized, the meeting 
Dr. Dr. Rami Khouri (05:46): based on that report. 
Dr. Dr. Rami Khouri (05:48): And the questions. 
Dr. Dr. Rami Khouri (05:50): So right now, before 
Dr. Dr. Rami Khouri (05:53): The the last time we talked, the there was a report 
Unknown (05:57): report one 
Dr. Dr. Rami Khouri (05:56): general document, that summarized 
Dr. Dr. Rami Khouri (06:00): the patient, according to the question, the questioner 
Dr. Dr. Rami Khouri (06:04): a overview of the patient. Right now, we're working on 
Unknown (06:09): a manager 
Dr. Dr. Rami Khouri (06:08): what you call case agenda that 
Dr. Dr. Rami Khouri (06:11): the same question that the case may ask, the same consent question, 
Dr. Dr. Rami Khouri (06:16): are 
Dr. Dr. Rami Khouri (06:18): So chained 
Dr. Dr. Rami Khouri (06:21): a the LLM 
Dr. Dr. Rami Khouri (06:24): according to the questionnaire, 
Dr. Dr. Rami Khouri (06:25): let's say if there's a question, that 
Unknown (06:30): the manager. 
Dr. Dr. Rami Khouri (06:29): should be asked by case And that same question was asked in the questionnaire, 
Dr. Dr. Rami Khouri (06:34): This question is, converted to a follow-up question. 
Dr. Dr. Rami Khouri (06:39): More to be, like, 
Dr. Dr. Rami Khouri (06:40): it's the same, overall structure. 
Dr. Dr. Rami Khouri (06:44): And, but more personalized to the patient. 
Dr. Dr. Rami Khouri (06:49): After this meeting, we take 
Dr. Dr. Rami Khouri (06:52): also the, a, the, the question, the info for 
Dr. Dr. Rami Khouri (06:56): the questioner, the, 
Unknown (06:57): manager 
Dr. Dr. Rami Khouri (06:57): case transcript and the notes, heroes, and 
Dr. Dr. Rami Khouri (07:03): through the meeting, and we used it 
Dr. Dr. Rami Khouri (07:05): as an input to generate, summary 
Unknown (07:10): the psychiatrist. 
Dr. Dr. Rami Khouri (07:09): and agenda for The summary is, regular EHR. 
Dr. Dr. Rami Khouri (07:14): That contained all as, sections of a psychiatric HR. 
Dr. Dr. Rami Khouri (07:18): Hey. And the agenda is more like a smart 
Dr. Dr. Rami Khouri (07:21): report with insights and 
Dr. Dr. Rami Khouri (07:24): made some, let's say, decision support elements 
Dr. Dr. Rami Khouri (07:29): and diagnosis, differential diagnosis, 
Dr. Dr. Rami Khouri (07:33): what, treatment, to consider some something like that. 
Dr. Dr. Rami Khouri (07:37): This is, a general idea. We can customize it, 
Unknown (07:42): the 
Dr. Dr. Rami Khouri (07:42): based on psychiatrist needs. 
Unknown (07:46): the 
Dr. Dr. Rami Khouri (07:45): After psychiatrist 
Dr. Dr. Rami Khouri (07:49): and and let's say in the meeting, 
Dr. Dr. Rami Khouri (07:52): we produce a summary 
Dr. Dr. Rami Khouri (07:55): based on all the the transcript notes 
Dr. Dr. Rami Khouri (07:58): all the info that we have and generate, 
Dr. Dr. Rami Khouri (08:02): a summary for to send to the patient or 
Unknown (08:03): the psychiatrist the GP. 
Dr. Dr. Rami Khouri (08:06): So 
Dr. Dr. Rami Khouri (08:08): and the the same flow go again and again and the follow-up. 
Unknown (08:15): the manager, 
Dr. Dr. Rami Khouri (08:13): A follow-up, a there there's a follow-up for case a follow-up for them. 
Dr. Dr. Rami Khouri (08:19): So 
Unknown (08:18): Psychaitresterholm. the two 
Dr. Dr. Rami Khouri (08:20): what things that we 
Dr. Dr. Rami Khouri (08:22): changed since our last meeting. 
Unknown (08:25): The manager, 
Dr. Dr. Rami Khouri (08:25): case interview that 
Dr. Dr. Rami Khouri (08:29): Right now, what I do, there's a prompt that 
Dr. Dr. Rami Khouri (08:32): as an input, get all the, 
Dr. Dr. Rami Khouri (08:34): questions, answers and questions from questionnaire inside the prompt. 
Dr. Dr. Rami Khouri (08:39): I answered the, 
Dr. Dr. Rami Khouri (08:41): and he 
Dr. Dr. Rami Khouri (08:44): the general interview 
Dr. Dr. Rami Khouri (08:47): structured interview, all the questions, and 
Dr. Dr. Rami Khouri (08:50): what I get as an output, the new new customized 
Dr. Dr. Rami Khouri (08:54): questions that goes into the UI 
Dr. Dr. Rami Khouri (08:59): in the relevant place. 
Dr. Dr. Rami Khouri (09:02): That's, change we we have done. 
Dr. Dr. Rami Khouri (09:04): A another chain that we talked about real time transcription 
Dr. Dr. Rami Khouri (09:09): and we wanted to 
Dr. Dr. Rami Khouri (09:11): make them, 
Unknown (09:15): the psychiatrist 
Dr. Dr. Rami Khouri (09:13): the the summary of more 
Unknown (09:20): a one 
Dr. Dr. Rami Khouri (09:17): to work on latency and accuracy. We used preview 
Dr. Dr. Rami Khouri (09:23): and and what what 
Unknown (09:24): did two 
Dr. Dr. Rami Khouri (09:24): we things. 
Unknown (09:28): a third 
Dr. Dr. Rami Khouri (09:26): We're now working with party 
Dr. Dr. Rami Khouri (09:30): platform. They send us 
Dr. Dr. Rami Khouri (09:34): as request, captions. 
Dr. Dr. Rami Khouri (09:38): Like, in the middle of the conversation or 
Unknown (09:43): the psychiatrists 
Dr. Dr. Rami Khouri (09:42): when decide that it's time to generate the summary 
Dr. Dr. Rami Khouri (09:47): Not after the meeting. 
Dr. Dr. Rami Khouri (09:49): Throughout the meeting, 
Dr. Dr. Rami Khouri (09:51): let's say in the three 
Unknown (09:52): last minutes, 
Dr. Dr. Rami Khouri (09:54): he clicks on generic summary. We send an 
Unknown (09:58): the third 
Dr. Dr. Rami Khouri (09:58): API to party that has 
Dr. Dr. Rami Khouri (10:01): they have a chat with that 
Dr. Dr. Rami Khouri (10:03): goes 
Unknown (10:04): the psychiatrist 
Dr. Dr. Rami Khouri (10:04): with to the meeting, and they send us 
Dr. Dr. Rami Khouri (10:07): the the caption, the the let's see the transcript. 
Dr. Dr. Rami Khouri (10:11): We generate a summary. 
Unknown (10:13): the psychiatrist 
Dr. Dr. Rami Khouri (10:13): And edit the summary, 
Dr. Dr. Rami Khouri (10:16): before 
Dr. Dr. Rami Khouri (10:18): he he end the ends the meeting. 
Dr. Dr. Rami Khouri (10:21): So this is something that helped us to 
Dr. Dr. Rami Khouri (10:25): save some 
Unknown (10:29): the psychiatrist 
Dr. Dr. Rami Khouri (10:27): administrative time that the needs 
Dr. Dr. Rami Khouri (10:30): before to edit and write the summary after the meeting. 
David Szabo-Stuban (10:34): Oh, so you basically get, like, few human feedback on the 
Unknown (10:39): the psychiatrist 
David Szabo-Stuban (10:38): rated summary, and you need to completely 
David Szabo-Stuban (10:41): prove the summary before the meeting is over. 
Dr. Dr. Rami Khouri (10:44): Yes. 
David Szabo-Stuban (10:45): Okay. That's brilliant. 
Dr. Dr. Rami Khouri (10:47): So for that, we needed, 
Dr. Dr. Rami Khouri (10:49): faster model one because it's, like, you know, it's it's on the 
Unknown (10:50): than the psychiatrist 
Dr. Dr. Rami Khouri (10:55): time of inside the 
David Szabo-Stuban (10:57): meeting. 
Dr. Dr. Rami Khouri (10:57): So we we, right now, I did some evaluation 
Dr. Dr. Rami Khouri (11:01): accuracy evaluation, and I 
Unknown (11:06): the Germany, 
Dr. Dr. Rami Khouri (11:04): We we went to with I think Flash 
Unknown (11:09): Flash two. 
Dr. Dr. Rami Khouri (11:09): in Jimmy It takes the model, 
Dr. Dr. Rami Khouri (11:14): there. 
Dr. Dr. Rami Khouri (11:14): Ten 
Dr. Dr. Rami Khouri (11:16): comparing to 
Dr. Dr. Rami Khouri (11:17): one and a half 
Unknown (11:14): seconds, minute. 
Unknown (11:19): Olauren? 
Dr. Dr. Rami Khouri (11:21): And the quality is good. 
Dr. Dr. Rami Khouri (11:25): We also, you know, it's it's not a final report. Psychiatrists 
Dr. Dr. Rami Khouri (11:29): will edit it. So, right now, it's it's good. It's in, 
Dr. Dr. Rami Khouri (11:35): not, it's in pilot. 
Unknown (11:38): one our psychiatrists 
Dr. Dr. Rami Khouri (11:37): Our, of is, testing this 
Dr. Dr. Rami Khouri (11:41): new method. 
Unknown (11:46): that's one 
Dr. Dr. Rami Khouri (11:45): And of the things we talked about. And we talked if 
Dr. Dr. Rami Khouri (11:50): to use, open AI 
Dr. Dr. Rami Khouri (11:53): advanced forest 
Dr. Dr. Rami Khouri (11:54): to get, real fast, real time transcript or not. 
Unknown (12:00): a third 
Dr. Dr. Rami Khouri (11:58): So in the end, we went to party and sent us the transcript. 
Dr. Dr. Rami Khouri (12:05): So right now, 
Dr. Dr. Rami Khouri (12:07): main projects that we work 
Dr. Dr. Rami Khouri (12:10): and we're working on as to 
Dr. Dr. Rami Khouri (12:14): we are working on, a patient application. 
Dr. Dr. Rami Khouri (12:19): So we want 
Dr. Dr. Rami Khouri (12:20): to 
Dr. Dr. Rami Khouri (12:21): a 
Dr. Dr. Rami Khouri (12:23): as part of the application. We wanted a chat with 
David Szabo-Stuban (12:26): Mhmm. 
David Szabo-Stuban (12:27): So 
Dr. Dr. Rami Khouri (12:27): we are, like, designing the chatbot. We 
Dr. Dr. Rami Khouri (12:32): I think that we're we 
Dr. Dr. Rami Khouri (12:33): we want or it's better to start with a simple 
Unknown (12:37): one agent, 
Dr. Dr. Rami Khouri (12:39): a general information about the clinic. 
Dr. Dr. Rami Khouri (12:42): A in the future, we want to 
Dr. Dr. Rami Khouri (12:46): you know, giving give the, chat with 
Dr. Dr. Rami Khouri (12:48): some tools, functions, link it to the calendar 
Dr. Dr. Rami Khouri (12:52): to a personal knowledge base, to use the 
Dr. Dr. Rami Khouri (12:56): the patient, like, in follow ups, generate customized content, 
Dr. Dr. Rami Khouri (13:01): maybe do some follow ups, questionnaire, questions, 
Dr. Dr. Rami Khouri (13:06): my vision is to, like, make a chatbot that 
Dr. Dr. Rami Khouri (13:11): will be based on a multi agent system. 
Dr. Dr. Rami Khouri (13:15): To do everything. 
Dr. Dr. Rami Khouri (13:16): You know, 
Dr. Dr. Rami Khouri (13:17): But to be, like, with, 
Dr. Dr. Rami Khouri (13:20): And the point of view of the patient, it's the same 
Dr. Dr. Rami Khouri (13:24): system, the same chatbot that he talks to. 
Dr. Dr. Rami Khouri (13:28): And 
Dr. Dr. Rami Khouri (13:30): You know what? 
Dr. Dr. Rami Khouri (13:31): The the system that behind the sale, the ecosystem that 
Dr. Dr. Rami Khouri (13:36): will, work on this 
Dr. Dr. Rami Khouri (13:39): we'll have and, you know, 
Unknown (13:39): an orchestrator agents 
Dr. Dr. Rami Khouri (13:43): and all that. And I think that 
Dr. Dr. Rami Khouri (13:45): In that area, I 
Dr. Dr. Rami Khouri (13:48): I will need your help and your experience on how to do this 
Dr. Dr. Rami Khouri (13:51): professionally, because there's a, 
Dr. Dr. Rami Khouri (13:55): safety con concern the 
David Szabo-Stuban (13:57): fidelity 
Dr. Dr. Rami Khouri (13:58): and all the 
Unknown (14:01): that's The second 
Dr. Dr. Rami Khouri (14:00): So that one like project. is to 
Dr. Dr. Rami Khouri (14:06): We we work with an, 
Dr. Dr. Rami Khouri (14:08): a local, 
Dr. Dr. Rami Khouri (14:12): That's fine. 
Dr. Dr. Rami Khouri (14:15): H M O H A O? A, Like, Organa Health Organization Here In 
Unknown (14:20): Israel. 
Dr. Dr. Rami Khouri (14:21): And they have a different 
Dr. Dr. Rami Khouri (14:24): HR system, 
Dr. Dr. Rami Khouri (14:26): And right now, we don't have an API integration with them. Right now, what 
Dr. Dr. Rami Khouri (14:31): what we 
Dr. Dr. Rami Khouri (14:32): usually do. We 
Dr. Dr. Rami Khouri (14:34): go each time to the 
Dr. Dr. Rami Khouri (14:37): we have access to their platform. We go and copy paste 
Dr. Dr. Rami Khouri (14:42): the 
Dr. Dr. Rami Khouri (14:43): the summary. 
Dr. Dr. Rami Khouri (14:44): And the diagnosis 
Dr. Dr. Rami Khouri (14:46): So 
Dr. Dr. Rami Khouri (14:47): And I don't see how can we get a 
Dr. Dr. Rami Khouri (14:50): API integration with them in the future. So I thought about 
Unknown (14:56): the operator 
Dr. Dr. Rami Khouri (14:55): you know, something like or the 
Dr. Dr. Rami Khouri (14:59): like, a platform with automation to do this for us. 
Dr. Dr. Rami Khouri (15:03): It seems to me 
Dr. Dr. Rami Khouri (15:06): like, what what I checked 
Dr. Dr. Rami Khouri (15:08): the research that I have done, that it's 
Dr. Dr. Rami Khouri (15:11): not simple to do this with the HR platform, but 
Dr. Dr. Rami Khouri (15:15): I wanted the to 
Dr. Dr. Rami Khouri (15:18): you know, to hear what you 
Dr. Dr. Rami Khouri (15:20): have to say in this matter. 
David Szabo-Stuban (15:22): Okay. Before we move on, is there are there any further pro 
David Szabo-Stuban (15:26): I've I've been taking notes, but there's a lot of information. So I want to understand, 
David Szabo-Stuban (15:31): Is there anything you want to add? 
Dr. Dr. Rami Khouri (15:35): Yeah, we have already we have 
Dr. Dr. Rami Khouri (15:38): like, the general auto summary 
Dr. Dr. Rami Khouri (15:41): it project. 
Unknown (15:43): each 
Dr. Dr. Rami Khouri (15:42): And one of this project, we we are working on to, enhance it. 
Dr. Dr. Rami Khouri (15:48): Like, in the psychiatric summary, we want to make, 
Dr. Dr. Rami Khouri (15:53): personalized 
Dr. Dr. Rami Khouri (15:56): agent 
Dr. Dr. Rami Khouri (15:56): to summarize for the specific 
Unknown (15:59): psychiatrists, 
Dr. Dr. Rami Khouri (16:00): like, to phrase like him and to 
Dr. Dr. Rami Khouri (16:03): you know, to 
Dr. Dr. Rami Khouri (16:05): to make it customized for 
Unknown (16:06): the psychiatrist. 
Dr. Dr. Rami Khouri (16:08): We want to add an overview for the patient to be 
Dr. Dr. Rami Khouri (16:13): There's some, like, sub projects inside 
Dr. Dr. Rami Khouri (16:17): automatic summary, 
Dr. Dr. Rami Khouri (16:18): project. 
Dr. Dr. Rami Khouri (16:19): I think I can send you 
Dr. Dr. Rami Khouri (16:22): like, a more detailed 
Dr. Dr. Rami Khouri (16:25): But that's the and overall, that's the project that we're working on right now. 
David Szabo-Stuban (16:30): Okay. 
David Szabo-Stuban (16:32): Cool. So there's a lot of things happening here, which is great. 
David Szabo-Stuban (16:36): Sounds like that you have a lot of work to do. 
Dr. Dr. Rami Khouri (16:40): Yeah. 
David Szabo-Stuban (16:41): Okay. So 
David Szabo-Stuban (16:43): is 
Dr. Dr. Rami Khouri (16:44): here with me. 
Dr. Dr. Rami Khouri (16:45): Hi. How are you? 
Unknown (16:46): Hey, Vivian. 
David Szabo-Stuban (16:47): Hello. 
David Szabo-Stuban (16:50): So 
David Szabo-Stuban (16:50): couple of things that I was thinking about is 
David Szabo-Stuban (16:55): If I understand this correctly, we are trying to find the parts 
David Szabo-Stuban (16:59): that you need help with designing the system 
David Szabo-Stuban (17:02): finding the right models, finding the right providers, basically, coming up 
David Szabo-Stuban (17:07): with the architecture together. And then 
David Szabo-Stuban (17:10): So you have the team that develops this. 
David Szabo-Stuban (17:13): Or or are you working with the with an external 
David Szabo-Stuban (17:16): team or who's going to implement whatever we discuss. 
Dr. Dr. Rami Khouri (17:20): We have 
Dr. Dr. Rami Khouri (17:22): a team 
Dr. Dr. Rami Khouri (17:24): and 
Unknown (17:27): team, 
Dr. Dr. Rami Khouri (17:26): r r and d but, you know, it's always 
Dr. Dr. Rami Khouri (17:31): It depends. I can't give them everything to work 
Dr. Dr. Rami Khouri (17:35): on if there's, 
Dr. Dr. Rami Khouri (17:37): like, for the application, we didn't build it from 
Dr. Dr. Rami Khouri (17:41): scratch me. 
David Szabo-Stuban (17:41): Yeah. We're 
Unknown (17:42): a third 
Dr. Dr. Rami Khouri (17:43): party. So 
Dr. Dr. Rami Khouri (17:44): I can 
David Szabo-Stuban (17:45): I am 
Dr. Dr. Rami Khouri (17:47): Yes? 
David Szabo-Stuban (17:49): The reason why I'm asking this 
Dr. Dr. Rami Khouri (17:51): Yeah. 
Unknown (17:53): because one 
David Szabo-Stuban (17:52): The reason why I'm asking this, thing that 
David Szabo-Stuban (17:55): changed in my life since we last talked is that I started 
David Szabo-Stuban (17:58): working and working as solution for an ID firm here 
Unknown (17:59): a architect in Hungary. 
David Szabo-Stuban (18:03): And, we have people. The company's been around 
David Szabo-Stuban (18:07): twenty 
Unknown (18:04): over 50 for years. 
Unknown (18:09): about $34,000,000 
David Szabo-Stuban (18:09): Make a year. So 
David Szabo-Stuban (18:11): not a big company, and, they have a lot of resources. 
David Szabo-Stuban (18:16): So if you would I I I mostly spend my days 
David Szabo-Stuban (18:21): designing AI architecture for banks. 
David Szabo-Stuban (18:24): Some logistics and manufacturing companies 
David Szabo-Stuban (18:28): we're also talking with a couple biochem companies. So there's a lot of 
David Szabo-Stuban (18:32): multi agent orchestration 
David Szabo-Stuban (18:34): a lot of chat bot chat with your data generate summary. 
David Szabo-Stuban (18:37): All the things that you just explained to me, that's something that 
Unknown (18:41): over 13 
David Szabo-Stuban (18:40): I now have projects on my desk at the same time. 
David Szabo-Stuban (18:45): And what I was thinking is that if you guys 
David Szabo-Stuban (18:49): need help in the implementation part. 
David Szabo-Stuban (18:52): I would just flag this to you to consider 
David Szabo-Stuban (18:55): bringing this team in 
David Szabo-Stuban (18:57): because they are very competitive in the hourly rates 
Unknown (19:01): in Hungary. like, $50 hour 
David Szabo-Stuban (19:00): because it's I think you're, an or something for 
David Szabo-Stuban (19:04): senior debt. And and 
David Szabo-Stuban (19:08): I could bring in that be that team, and then we could you would gather 
Unknown (19:13): owner, a 
David Szabo-Stuban (19:12): product you would get project manager and and 
David Szabo-Stuban (19:17): you know, 
David Szabo-Stuban (19:18): there would there would be a separate ownership for 
David Szabo-Stuban (19:21): for, managing the whole AI project 
David Szabo-Stuban (19:24): to be that putting a lot more strain on r r and d 
Unknown (19:27): your team. 
David Szabo-Stuban (19:29): It's it's not some it's just an idea. It just came to me. I usually 
David Szabo-Stuban (19:33): offer this to every client I work with because, it also 
David Szabo-Stuban (19:38): reduces complexity of the project for a lot in a lot of times. 
David Szabo-Stuban (19:42): If this is not a direction, 
David Szabo-Stuban (19:44): that's viable for you 
David Szabo-Stuban (19:46): then just forget what I said and we can move forward. 
Dr. Dr. Rami Khouri (19:49): I 
David Szabo-Stuban (19:49): mean, my my job won't change. 
David Szabo-Stuban (19:51): Right? I will need to work with you to co create the architecture. 
David Szabo-Stuban (19:55): My job won't change either way. 
David Szabo-Stuban (19:57): But if this helps you guys implement 
David Szabo-Stuban (19:59): then consider it. 
Dr. Dr. Rami Khouri (20:01): Yeah. But, you know, it's it's brilliant. 
Dr. Dr. Rami Khouri (20:04): Idea because we have, 
Dr. Dr. Rami Khouri (20:07): we have limitations I have as 
Dr. Dr. Rami Khouri (20:09): in the innovation 
Dr. Dr. Rami Khouri (20:12): department. I am limited on 
Unknown (20:16): the 
Dr. Dr. Rami Khouri (20:15): how much I can use R and D team 
David Szabo-Stuban (20:17): Okay. 
Dr. Dr. Rami Khouri (20:18): A, so 
Dr. Dr. Rami Khouri (20:19): and 
Dr. Dr. Rami Khouri (20:20): Absolutely. The the 
Dr. Dr. Rami Khouri (20:23): help me if I 
Dr. Dr. Rami Khouri (20:25): get, 
Dr. Dr. Rami Khouri (20:26): you know, on each project, 
Dr. Dr. Rami Khouri (20:30): like, proposition or 
Dr. Dr. Rami Khouri (20:33): something that I can 
Dr. Dr. Rami Khouri (20:36): make a or ask 
Dr. Dr. Rami Khouri (20:38): for, approval that this will make my, work easier and faster 
Dr. Dr. Rami Khouri (20:43): stuff. 
David Szabo-Stuban (20:44): Okay. 
David Szabo-Stuban (20:46): Okay. In that in that case, 
David Szabo-Stuban (20:48): what I think we should do today is 
Unknown (20:53): down two, 
David Szabo-Stuban (20:51): to nail one, or 
Unknown (20:54): three 
David Szabo-Stuban (20:54): projects. It can't be any number of projects, right, it's scalable for 
David Szabo-Stuban (20:58): for the company I work for. So it can be any number of projects 
David Szabo-Stuban (21:01): that we want to pinpoint. I have a lot of documentation you've already sent 
Unknown (21:05): Mees, efar, CEO, 
David Szabo-Stuban (21:07): and we can set up a call 
David Szabo-Stuban (21:09): to discuss 
Unknown (21:13): the team 
David Szabo-Stuban (21:11): what else the company needs and what else sales needs on our end. 
David Szabo-Stuban (21:15): To give you a proposal 
David Szabo-Stuban (21:18): on what it would take 
David Szabo-Stuban (21:19): for us to actually deliver these things. 
David Szabo-Stuban (21:22): And and then you we can move on from there. 
David Szabo-Stuban (21:27): Sure. 
David Szabo-Stuban (21:27): Should we do that? 
Dr. Dr. Rami Khouri (21:30): Yeah. Yeah. I need to 
Dr. Dr. Rami Khouri (21:33): send you, I think, a more 
Dr. Dr. Rami Khouri (21:37): maybe details. 
David Szabo-Stuban (21:41): Yeah. Any document is 
David Szabo-Stuban (21:43): any documentation you have just send over because 
David Szabo-Stuban (21:46): basically, when I'm when I'm pulled into a sales conversation or business development 
David Szabo-Stuban (21:51): restriction, I start asking a bunch of questions, but I already asked you these questions because we work 
David Szabo-Stuban (21:56): together. 
David Szabo-Stuban (21:57): So I already have some context, which is great. 
David Szabo-Stuban (22:01): But if you have any more detailed documentation, I will read this from 
David Szabo-Stuban (22:05): from that angle. 
Dr. Dr. Rami Khouri (22:09): Okay. 
Dr. Dr. Rami Khouri (22:10): Okay. 
Dr. Dr. Rami Khouri (22:12): So I will organize, I will try to, like, 
Dr. Dr. Rami Khouri (22:16): send you, like, a general 
Dr. Dr. Rami Khouri (22:22): a map of 
Dr. Dr. Rami Khouri (22:23): all the projects. And in each project, I will 
Dr. Dr. Rami Khouri (22:26): try to explain 
Dr. Dr. Rami Khouri (22:28): a 
Dr. Dr. Rami Khouri (22:29): what we want to do, what we need 
Dr. Dr. Rami Khouri (22:33): and what are the main 
Dr. Dr. Rami Khouri (22:37): issues or the, 
Dr. Dr. Rami Khouri (22:40): a. 
Dr. Dr. Rami Khouri (22:41): Topics we want to focus on. 
Dr. Dr. Rami Khouri (22:45): And I I already have, you know, 
Dr. Dr. Rami Khouri (22:48): knowledge and, 
Dr. Dr. Rami Khouri (22:50): How it should 
Dr. Dr. Rami Khouri (22:52): in generally in, like, also in the multi agent system. 
Dr. Dr. Rami Khouri (22:56): I can help with 
Dr. Dr. Rami Khouri (22:57): that also 
Dr. Dr. Rami Khouri (22:58): and 
Dr. Dr. Rami Khouri (23:04): Okay? 
David Szabo-Stuban (23:06): Okay. Cool. 
David Szabo-Stuban (23:08): So you send the send those over to me 
Unknown (23:12): our CEO 
David Szabo-Stuban (23:11): I'm gonna sit down and talk to set up a call. We have a conversation. 
David Szabo-Stuban (23:15): We the company sends you a proposal 
David Szabo-Stuban (23:18): And in the meantime, you and I, we work together on on nailing down the architecture. 
Dr. Dr. Rami Khouri (23:26): Okay. 
David Szabo-Stuban (23:28): Awesome. 
Dr. Dr. Rami Khouri (23:28): Awesome. Awesome. 
David Szabo-Stuban (23:31): So we discussed a lot of projects now. 
David Szabo-Stuban (23:34): Is there a single question, or do you have specific problems that you are 
David Szabo-Stuban (23:39): trying to solve right now. 
David Szabo-Stuban (23:41): That you would want to us to focus on today. 
Dr. Dr. Rami Khouri (23:44): Yeah. We have 
Dr. Dr. Rami Khouri (23:46): I think I want to focus on the chat with 
Dr. Dr. Rami Khouri (23:49): because I I need to make a decision if to 
Dr. Dr. Rami Khouri (23:55): Go, 
Dr. Dr. Rami Khouri (23:57): on with this project right now. And the next 
Dr. Dr. Rami Khouri (24:00): months or two delayed, because 
Dr. Dr. Rami Khouri (24:05): you know, we need to 
Dr. Dr. Rami Khouri (24:06): prioritize, our work and 
Dr. Dr. Rami Khouri (24:10): I think that it's it's important to 
Dr. Dr. Rami Khouri (24:13): maybe start with 
Dr. Dr. Rami Khouri (24:15): is something of the multi agent system 
Dr. Dr. Rami Khouri (24:19): because it's important we need to do this 
Dr. Dr. Rami Khouri (24:23): you know, and I think chatbot 
Unknown (24:26): a one 
Dr. Dr. Rami Khouri (24:27): agent may be a good start 
Unknown (24:30): one, 
Dr. Dr. Rami Khouri (24:31): a conversational agent 
Dr. Dr. Rami Khouri (24:33): could be a good start. 
Dr. Dr. Rami Khouri (24:35): I already used some elements of multi agents in the prompts 
Dr. Dr. Rami Khouri (24:39): for the automatic summary, but it's not 
Dr. Dr. Rami Khouri (24:42): You know, it's not really 
Dr. Dr. Rami Khouri (24:47): classic end of the agent system. 
David Szabo-Stuban (24:49): Yeah. 
Dr. Dr. Rami Khouri (24:50): So for I need what I want you to, you know, 
Dr. Dr. Rami Khouri (24:55): same brainstorm or sync with me is what is the the 
Dr. Dr. Rami Khouri (24:59): best way 
Unknown (25:01): the first 
Dr. Dr. Rami Khouri (25:01): to create chatbot 
Dr. Dr. Rami Khouri (25:03): that will be 
Dr. Dr. Rami Khouri (25:05): that will 
Dr. Dr. Rami Khouri (25:07): let's say, give, 
Dr. Dr. Rami Khouri (25:10): general, 
Dr. Dr. Rami Khouri (25:13): answers to the 
Dr. Dr. Rami Khouri (25:15): based on our 
Dr. Dr. Rami Khouri (25:18): you know, knowledge base, 
Dr. Dr. Rami Khouri (25:20): that we give him is it's it's 
Dr. Dr. Rami Khouri (25:23): best to 
Dr. Dr. Rami Khouri (25:24): that. 
Dr. Dr. Rami Khouri (25:25): Like, in in, in the concept of the of prompting to 
Unknown (25:32): an assistant 
Dr. Dr. Rami Khouri (25:30): to get the context inside the prompt or to use with the knowledge base 
Dr. Dr. Rami Khouri (25:36): use a thread for the, 
Dr. Dr. Rami Khouri (25:39): memory or is there 
Dr. Dr. Rami Khouri (25:41): You know, it's it's basic architecture of chatbot with this 
Dr. Dr. Rami Khouri (25:45): a, let's say, basic 
Dr. Dr. Rami Khouri (25:49): and features. 
Dr. Dr. Rami Khouri (25:52): Was 
Dr. Dr. Rami Khouri (25:53): taking on internal consideration, 
Dr. Dr. Rami Khouri (25:56): safety 
Dr. Dr. Rami Khouri (25:57): And 
Dr. Dr. Rami Khouri (25:59): the the concept of, let's say, 
Dr. Dr. Rami Khouri (26:02): hybrid 
Dr. Dr. Rami Khouri (26:03): like, I want the checkbook to to know when to 
Dr. Dr. Rami Khouri (26:08): to, let's say, detect 
Dr. Dr. Rami Khouri (26:14): went to end the conversation and move 
Dr. Dr. Rami Khouri (26:17): on or refer the patient to a human agent. 
David Szabo-Stuban (26:26): Question. 
David Szabo-Stuban (26:28): Is this chatbot going to be embedded? 
David Szabo-Stuban (26:31): Inside the inside your platform. 
David Szabo-Stuban (26:33): Is is this an embedded chatbot or is this a standalone 
Dr. Dr. Rami Khouri (26:38): No. 
David Szabo-Stuban (26:39): Embedded. Okay. 
David Szabo-Stuban (26:43): So I think that what we're looking at right now 
David Szabo-Stuban (26:46): is something that we could build with with, length flow. 
David Szabo-Stuban (26:51): You used langflow before? 
Dr. Dr. Rami Khouri (26:54): No. 
Dr. Dr. Rami Khouri (26:55): Okay. 
David Szabo-Stuban (26:55): Give me one second. 
Dr. Dr. Rami Khouri (26:58): Mainly, I work with 
Dr. Dr. Rami Khouri (27:01): and LLS, 
Unknown (27:03): and make.com. 
Dr. Dr. Rami Khouri (27:05): I saw, in the ten that 
Unknown (27:07): last months m eight 
Dr. Dr. Rami Khouri (27:08): you start to use the m 
David Szabo-Stuban (27:11): Yeah. 
Dr. Dr. Rami Khouri (27:14): Cool. I I didn't have the time to 
Dr. Dr. Rami Khouri (27:17): go deep in this. But, yeah, that's it. It's it's 
Dr. Dr. Rami Khouri (27:22): NOLMs, 
Dr. Dr. Rami Khouri (27:23): basic 
Dr. Dr. Rami Khouri (27:24): and mainly, application or modules that already have 
Dr. Dr. Rami Khouri (27:29): integration make, And I 
Unknown (27:30): with use Google 
Dr. Dr. Rami Khouri (27:34): sheets as my database. 
David Szabo-Stuban (27:36): And it's 
Dr. Dr. Rami Khouri (27:37): not because 
David Szabo-Stuban (27:41): Okay. Let me show you a couple things that might 
David Szabo-Stuban (27:44): help you. 
Unknown (27:48): you four 
David Szabo-Stuban (27:47): I want to show things 
David Szabo-Stuban (27:52): They're all gonna be open source things that you guys can use in your development. 
Unknown (27:58): One 
David Szabo-Stuban (27:59): of the things that I will want to show show. Let me just 
David Szabo-Stuban (28:02): Give me one second. Let me share my 
Dr. Dr. Rami Khouri (28:04): And there is I want 
Dr. Dr. Rami Khouri (28:06): just to mention this, 
David Szabo-Stuban (28:07): yeah, I 
Unknown (28:03): screen first. five. 
Dr. Dr. Rami Khouri (28:09): Forget, do you remember we talked about, 
Unknown (28:14): prompt 
Dr. Dr. Rami Khouri (28:13): platform for engineering So 
Dr. Dr. Rami Khouri (28:16): I'm a find this pro top. I don't know if you 
Dr. Dr. Rami Khouri (28:20): know the platform. 
Dr. Dr. Rami Khouri (28:22): This is the platform that we are working with right now. 
Dr. Dr. Rami Khouri (28:26): It's it's it's okay. It had all the features, but 
Dr. Dr. Rami Khouri (28:31): It's something that I want 
Dr. Dr. Rami Khouri (28:32): you if you can 
Dr. Dr. Rami Khouri (28:35): to have, better ideas 
Dr. Dr. Rami Khouri (28:38): just to consider, 
David Szabo-Stuban (28:41): Okay. 
David Szabo-Stuban (28:42): Okay. I I I put that I put that in the back burner for now. 
David Szabo-Stuban (28:47): So there are a couple of tools that I want to show you. 
David Szabo-Stuban (28:50): You understand them, and then I also gonna 
David Szabo-Stuban (28:52): show you a couple things. So 
Unknown (28:56): The first n eight. 
David Szabo-Stuban (28:57): thing is And I 
Unknown (29:00): an eight, 
David Szabo-Stuban (28:59): fully switched over to and I dropped most of the, 
David Szabo-Stuban (29:03): other tools that I was using mainly because it does 
David Szabo-Stuban (29:06): have Nating AI Native AI agent support. 
David Szabo-Stuban (29:09): So it actually understands AI agents, and you can easily create 
David Szabo-Stuban (29:14): with the agent systems 
David Szabo-Stuban (29:18): it's support it's fully supports 
David Szabo-Stuban (29:20): any control flow. So I can create loops, switches, 
David Szabo-Stuban (29:24): routers, 
David Szabo-Stuban (29:26): and they don't can fork 
David Szabo-Stuban (29:29): the pro processes, I can run parallel processes 
David Szabo-Stuban (29:32): So all of that together means that I can actually orchestrate an AI agent system 
David Szabo-Stuban (29:37): and 
David Szabo-Stuban (29:37): inside an 
Unknown (29:38): a 10. 
David Szabo-Stuban (29:40): Without a problem. 
David Szabo-Stuban (29:41): I can also just send simple 
David Szabo-Stuban (29:44): simple alarm calls, 
David Szabo-Stuban (29:46): And, the way it's structured is, as you can see, 
David Szabo-Stuban (29:49): This is where I'm structuring the 
David Szabo-Stuban (29:51): the prompt 
David Szabo-Stuban (29:52): it's south, 
David Szabo-Stuban (29:53): and then I just attach a model to it. 
David Szabo-Stuban (29:55): So if I want to change it, 
David Szabo-Stuban (29:57): I can just select another model 
David Szabo-Stuban (29:59): and it's gonna be it's gonna be easiest. 
David Szabo-Stuban (30:02): Like, that that that's simple. So it allows me 
Dr. Dr. Rami Khouri (30:05): to try out 
David Szabo-Stuban (30:06): different models really quickly. 
Dr. Dr. Rami Khouri (30:08): It says the prompt. 
Dr. Dr. Rami Khouri (30:10): And all the parameters 
David Szabo-Stuban (30:13): Yes. 
Dr. Dr. Rami Khouri (30:14): Something that make the don't have 
David Szabo-Stuban (30:17): Yeah. It make doesn't 
David Szabo-Stuban (30:18): have that. Also make doesn't support loops. 
David Szabo-Stuban (30:21): So 
Dr. Dr. Rami Khouri (30:21): for 
Unknown (30:22): this one 
David Szabo-Stuban (30:22): right? So does, which is brilliant. 
David Szabo-Stuban (30:26): So 
Unknown (30:27): That's one 
David Szabo-Stuban (30:27): thing. And now since we are here, I want to show you this. 
David Szabo-Stuban (30:31): This is based on 
Unknown (30:34): the team 
David Szabo-Stuban (30:33): the study that Berkeley did 
David Szabo-Stuban (30:36): that where they replicated 
Unknown (30:40): like, $30 
David Szabo-Stuban (30:38): deep sea level reasoning for, of compute 
David Szabo-Stuban (30:43): And the way they did it 
David Szabo-Stuban (30:45): follows a really incredibly simple architecture called budget forcing. 
David Szabo-Stuban (30:49): And, basically, the budget forcing means 
David Szabo-Stuban (30:52): that 
David Szabo-Stuban (30:53): There is a budget for thinking. This can be determined in number 
David Szabo-Stuban (30:58): characters or a number of tokens. 
David Szabo-Stuban (31:00): In this in this, scenario, 
David Szabo-Stuban (31:03): This is, defined by characters. 
David Szabo-Stuban (31:06): For the sake of 
Unknown (31:08): So 8,000 
David Szabo-Stuban (31:07): Example. character is the limit. 
David Szabo-Stuban (31:10): What happens is that 
David Szabo-Stuban (31:12): inside the chatbot when the user sends the chat message. 
David Szabo-Stuban (31:16): It also gets the database schema because this is a text to SQL, 
David Szabo-Stuban (31:21): automation. And what happens is that 
Unknown (31:24): First, 
David Szabo-Stuban (31:26): It fetches from a database 
David Szabo-Stuban (31:28): it fetches all the tokens that have been generated in the process 
David Szabo-Stuban (31:32): so so far. 
David Szabo-Stuban (31:34): And then, 
Unknown (31:36): into one 
David Szabo-Stuban (31:35): joins them string 
David Szabo-Stuban (31:38): And what happens in this 
David Szabo-Stuban (31:39): this model here is that 
David Szabo-Stuban (31:41): it 
David Szabo-Stuban (31:42): reroute the actual prompt. 
David Szabo-Stuban (31:44): And it doesn't generate a response 
David Szabo-Stuban (31:47): it just says that you're an internal monologue of an AI. 
David Szabo-Stuban (31:50): And here is the context 
David Szabo-Stuban (31:52): and try to understand what you want, what the user wants. 
David Szabo-Stuban (31:56): And what happens because of this prompt 
David Szabo-Stuban (31:58): is it generates a couple of things, couple of, ideas 
David Szabo-Stuban (32:02): on 
David Szabo-Stuban (32:03): or like a thinking process on how to solve this 
David Szabo-Stuban (32:06): problem that saves the the thought to the database 
David Szabo-Stuban (32:11): checks the dot total number of characters that have been generated 
David Szabo-Stuban (32:15): and checks if the token budget has been spent. 
Dr. Dr. Rami Khouri (32:18): It 
David Szabo-Stuban (32:18): hasn't been sent, 
David Szabo-Stuban (32:19): then loops over again. 
David Szabo-Stuban (32:21): And it keeps looping 
David Szabo-Stuban (32:22): until the total number of reasoning tokens 
David Szabo-Stuban (32:26): have been exhausted. 
David Szabo-Stuban (32:27): Once it's exhausted, 
David Szabo-Stuban (32:29): then it sends it off to our next LLM, in the chain. 
David Szabo-Stuban (32:33): Which is which is then forces the model 
David Szabo-Stuban (32:36): to actually 
David Szabo-Stuban (32:37): provide a, actually provide a response. 
Dr. Dr. Rami Khouri (32:41): So it's like, level of reasoning. 
Dr. Dr. Rami Khouri (32:44): In the 
Unknown (32:46): o one 
David Szabo-Stuban (32:45): Yeah. It's and o 
David Szabo-Stuban (32:48): pre leveled, but you can use it with any model. 
David Szabo-Stuban (32:52): Right? And and, basically, 
David Szabo-Stuban (32:54): The idea here is that the larger the token budget is 
David Szabo-Stuban (32:58): the smarter the models are becoming. That's something that we just 
David Szabo-Stuban (33:01): realized. So you can use smaller, faster models, 
David Szabo-Stuban (33:05): to generate more tokens. 
David Szabo-Stuban (33:07): So what really actually 
David Szabo-Stuban (33:09): matters, 
David Szabo-Stuban (33:10): in this 
David Szabo-Stuban (33:11): you're selecting the model is not the model's 
David Szabo-Stuban (33:14): models, 
David Szabo-Stuban (33:15): capabilities itself 
Unknown (33:18): per second 
David Szabo-Stuban (33:17): but the token generation. 
David Szabo-Stuban (33:20): Because if you have a if you have a model that generates 
David Szabo-Stuban (33:23): models, generates responses really quickly. 
David Szabo-Stuban (33:27): Then you can reason more even if it's 
David Szabo-Stuban (33:30): dumber, 
David Szabo-Stuban (33:31): than a smarter model. 
David Szabo-Stuban (33:32): And then 
David Szabo-Stuban (33:33): here, for example, once the answer has been prepared, 
David Szabo-Stuban (33:37): it generates a bunch of text and inside that text, 
Dr. Dr. Rami Khouri (33:40): there 
David Szabo-Stuban (33:40): is a SQL query. 
David Szabo-Stuban (33:42): And it sends it over to a tool agent 
David Szabo-Stuban (33:45): that's job is to extract the SQL query 
David Szabo-Stuban (33:48): from the prompt 
David Szabo-Stuban (33:50): And, 
David Szabo-Stuban (33:51): send it off 
David Szabo-Stuban (33:52): to the Postgres database as an execute query. 
David Szabo-Stuban (33:56): So it literally just 
David Szabo-Stuban (33:58): factory is the, 
David Szabo-Stuban (33:59): fetches the query from the AI, runs it 
David Szabo-Stuban (34:03): then once it returns the responses, 
David Szabo-Stuban (34:06): it, drops the response and sends the response off to a conversation agent 
David Szabo-Stuban (34:11): that 
David Szabo-Stuban (34:12): whose job is to 
David Szabo-Stuban (34:13): find answers to the user's problems, 
David Szabo-Stuban (34:16): And then I just say, hey, here here's the thinking process. 
David Szabo-Stuban (34:20): Here's the user's original query. 
David Szabo-Stuban (34:22): Here is your thinking process. 
David Szabo-Stuban (34:23): Here's what we found in the date, the base. 
David Szabo-Stuban (34:26): Based on all that, formulate 
David Szabo-Stuban (34:28): If you send it back to the user, 
Unknown (34:32): with Nathan 
David Szabo-Stuban (34:30): Another thing that's really good is that it has a native 
David Szabo-Stuban (34:34): chatbot integration. So as you build things, you can also test 
David Szabo-Stuban (34:38): things, which is which is brilliant. 
David Szabo-Stuban (34:40): So this is budget forcing, and I want you to consider this when you're evaluating 
David Szabo-Stuban (34:45): models, 
David Szabo-Stuban (34:46): because 
David Szabo-Stuban (34:46): basically 
David Szabo-Stuban (34:48): you can 
David Szabo-Stuban (34:49): you can use grok 
David Szabo-Stuban (34:51): not with the k, but with the q. 
David Szabo-Stuban (34:54): Because they 
Dr. Dr. Rami Khouri (34:54): are 
David Szabo-Stuban (34:55): Have you seen these guys? 
Dr. Dr. Rami Khouri (34:58): Yeah. 
David Szabo-Stuban (34:58): Yeah. So they're they're really good at generating tokens really fast 
David Szabo-Stuban (35:02): asked. 
David Szabo-Stuban (35:03): Lot faster, like, twice as fast as as Gemini Flash. 
David Szabo-Stuban (35:07): And and you can generate an API key 
David Szabo-Stuban (35:10): and NAIT and also allows you to 
David Szabo-Stuban (35:12): to select a model, 
David Szabo-Stuban (35:14): that's, 
David Szabo-Stuban (35:15): Let me show you 
David Szabo-Stuban (35:16): to select the 
Dr. Dr. Rami Khouri (35:17): model. 
Dr. Dr. Rami Khouri (35:18): The framework 
Dr. Dr. Rami Khouri (35:19): my work is 
Dr. Dr. Rami Khouri (35:21): You know, 
Dr. Dr. Rami Khouri (35:23): I find 
Unknown (35:25): o three 
Dr. Dr. Rami Khouri (35:24): let's say, like, o meaning, 
Dr. Dr. Rami Khouri (35:26): it's it's fast, but 
Unknown (35:29): than one, 
Dr. Dr. Rami Khouri (35:29): It's faster but for some reason, it's not good. 
Unknown (35:33): In 
Dr. Dr. Rami Khouri (35:33): Hebrew 
David Szabo-Stuban (35:34): Mhmm. So 
Dr. Dr. Rami Khouri (35:35): there's this 
Dr. Dr. Rami Khouri (35:37): problem. I don't know 
Dr. Dr. Rami Khouri (35:39): have a 
Dr. Dr. Rami Khouri (35:40): what's the logic behind this, but I I need to test it 
Dr. Dr. Rami Khouri (35:44): also because 
David Szabo-Stuban (35:46): Yeah. 
Unknown (35:45): in Hebrew Only one 
Dr. Dr. Rami Khouri (35:47): and 
Dr. Dr. Rami Khouri (35:50): There's they are good 
Unknown (35:48): Germany Claude. in Hebrew. 
Dr. Dr. Rami Khouri (35:53): And let's say, 
Unknown (35:56): three 
Dr. Dr. Rami Khouri (35:56): mini, and 
Dr. Dr. Rami Khouri (35:58): other I I didn't really just, 
Unknown (36:04): here, Rami, 
David Szabo-Stuban (36:03): The important thing is that 
David Szabo-Stuban (36:06): this is a reasoning pros 
David Szabo-Stuban (36:09): says sitting at an architecture level level. It's not reasoning at the model level. 
Unknown (36:15): Gemini point 
David Szabo-Stuban (36:14): So this is using two o Flash. 
David Szabo-Stuban (36:17): It's a it's a reasoning model 
David Szabo-Stuban (36:19): or it's a reasoning architecture 
David Szabo-Stuban (36:21): with a simple AlarmNet 
Dr. Dr. Rami Khouri (36:23): model. Okay. 
David Szabo-Stuban (36:24): Right? 
Unknown (36:26): is one 
David Szabo-Stuban (36:25): Okay. So this thing that I want to show you. 
David Szabo-Stuban (36:29): And as you can see, I'm using Superbase 
David Szabo-Stuban (36:31): for my database. It's Postgres, 
David Szabo-Stuban (36:33): database, 
David Szabo-Stuban (36:35): which is open source. 
David Szabo-Stuban (36:37): So you can self host it. 
David Szabo-Stuban (36:39): And, 
David Szabo-Stuban (36:40): and and 
David Szabo-Stuban (36:41): The reason why I love this is because it can handle 
Unknown (36:48): than Google 
David Szabo-Stuban (36:45): a lot of data, a lot better than sheets or apps. 
David Szabo-Stuban (36:49): Airtable, 
David Szabo-Stuban (36:51): and it also supports backdoor stores. 
David Szabo-Stuban (36:53): So I can create a knowledge base and I can have a database 
David Szabo-Stuban (36:57): and both are going to be running on this 
David Szabo-Stuban (37:01): superbays instance 
David Szabo-Stuban (37:04): which is which is really, really helpful. 
David Szabo-Stuban (37:08): Also, it 
Dr. Dr. Rami Khouri (37:09): will 
David Szabo-Stuban (37:09): automatically generates APIs 
David Szabo-Stuban (37:12): for every table 
David Szabo-Stuban (37:13): it generates an API endpoint for every table. 
David Szabo-Stuban (37:16): You have in your database automatically. 
David Szabo-Stuban (37:19): So it's a it's it's it's a 
Unknown (37:21): like Google 
David Szabo-Stuban (37:21): It's sheets on steroids. 
Dr. Dr. Rami Khouri (37:24): How do you recommend, 
Dr. Dr. Rami Khouri (37:27): for me to start with Superbase and, and I 
Dr. Dr. Rami Khouri (37:31): been made in 
Dr. Dr. Rami Khouri (37:33): like, to 
Dr. Dr. Rami Khouri (37:34): just to use it, or is there any videos or course, 
David Szabo-Stuban (37:39): Actually, here is, I just wrote an article about this 
Unknown (37:44): this 
David Szabo-Stuban (37:43): I think it was one 
David Szabo-Stuban (37:46): So 
David Szabo-Stuban (37:47): There are fundamental, some of you some of 
David Szabo-Stuban (37:49): These or no? 
David Szabo-Stuban (37:51): And then 
Unknown (37:54): an Anita 
David Szabo-Stuban (37:52): I recommend you that you set up account for yourself. 
Unknown (38:00): like, per month, 
David Szabo-Stuban (37:57): I recommend self hosting on a railway because it costs you, $5 and you get unlimited workflows and unlimited operations. You just pay for that. 
Unknown (38:08): you $5 month. 
David Szabo-Stuban (38:06): Server, and that costs a Feel right away. 
David Szabo-Stuban (38:10): So 
David Szabo-Stuban (38:11): that's that, you know, make is a lot more expensive than that. 
David Szabo-Stuban (38:16): Then once you have it set up, 
Unknown (38:19): compiled five 
David Szabo-Stuban (38:19): I starter projects 
David Szabo-Stuban (38:22): that are very different in nature. 
David Szabo-Stuban (38:25): And anything 
Dr. Dr. Rami Khouri (38:26): for 
David Szabo-Stuban (38:28): Yeah. 
Unknown (38:26): the first one. a 10 
David Szabo-Stuban (38:28): And n has this template marketplace. 
David Szabo-Stuban (38:31): So you can just copy the template to the 
David Szabo-Stuban (38:34): clipboard, 
David Szabo-Stuban (38:36): open up a workflow, 
David Szabo-Stuban (38:37): Hit paste, and it paste in the workflow. And then you can start looking at it 
David Szabo-Stuban (38:42): and learning how it works. So 
David Szabo-Stuban (38:45): That's 
Dr. Dr. Rami Khouri (38:45): that's 
David Szabo-Stuban (38:46): how that's how I 
Dr. Dr. Rami Khouri (38:46): suggest 
David Szabo-Stuban (38:47): that you start working 
Unknown (38:48): within Nathan. And one 
Dr. Dr. Rami Khouri (38:50): more question. 
Dr. Dr. Rami Khouri (38:53): Use I use CHAJPT for, you know, 
Dr. Dr. Rami Khouri (38:57): brainstorming, 
Dr. Dr. Rami Khouri (39:00): a lot of conversational, 
Dr. Dr. Rami Khouri (39:03): Design. 
Dr. Dr. Rami Khouri (39:05): Do you use this directly from CHPG 
Dr. Dr. Rami Khouri (39:10): to create 
Dr. Dr. Rami Khouri (39:13): workflows or scenarios into 
Unknown (39:16): one 
Dr. Dr. Rami Khouri (39:16): of these 
Dr. Dr. Rami Khouri (39:18): to save time or 
David Szabo-Stuban (39:21): no. Sometimes it generates 
Unknown (39:25): and eight 
David Szabo-Stuban (39:23): Sometimes it can generate valid end workflows, but it's not there yet. 
Unknown (39:28): And Nathan 
David Szabo-Stuban (39:29): is 
David Szabo-Stuban (39:29): working or allegedly working on a text to an 
David Szabo-Stuban (39:34): automation or agent 
David Szabo-Stuban (39:36): but it's not it it doesn't exist yet. 
David Szabo-Stuban (39:38): So what I usually do 
David Szabo-Stuban (39:40): is, I usually 
David Szabo-Stuban (39:43): use chat GPT to help me think through the automations I already 
David Szabo-Stuban (39:48): I want to build 
David Szabo-Stuban (39:49): and then I I throw a flow chart 
David Szabo-Stuban (39:52): with mermaid. 
David Szabo-Stuban (39:53): And then I start implementing the flowchart manually 
Dr. Dr. Rami Khouri (39:57): on 
Dr. Dr. Rami Khouri (39:58): Yeah. Then that's what that's what I do with make. I 
Unknown (40:01): their agent 
Dr. Dr. Rami Khouri (40:01): the is not 
Dr. Dr. Rami Khouri (40:03): really helpful. 
David Szabo-Stuban (40:05): Yeah. Also, the other the other important 
Unknown (40:11): an ten 
David Szabo-Stuban (40:08): thing, and this is an important distinction between make and eight is that 
David Szabo-Stuban (40:12): make has their own inline functions index. 
David Szabo-Stuban (40:16): Right? So if you want to write inline functions in make, 
David Szabo-Stuban (40:19): like mapping and everything, 
David Szabo-Stuban (40:21): they actually don't use plain JavaScript. 
David Szabo-Stuban (40:24): They use their own syntax, and that makes it won't be because then 
David Szabo-Stuban (40:28): CHGPT cannot help you 
David Szabo-Stuban (40:31): writing those syntaxes because it always 
David Szabo-Stuban (40:34): defaults back to trying to write 
David Szabo-Stuban (40:37): plain JavaScript. 
David Szabo-Stuban (40:39): And and that I found very annoying. 
David Szabo-Stuban (40:42): But inside 
Unknown (40:43): NA 10, 
David Szabo-Stuban (40:44): and it actually uses 
David Szabo-Stuban (40:46): JavaScript. 
David Szabo-Stuban (40:47): So 
David Szabo-Stuban (40:49): That means that I can use JetGPT to write these inline expressions 
David Szabo-Stuban (40:53): for me. 
David Szabo-Stuban (40:55): And it it 
David Szabo-Stuban (40:56): almost never fails. 
David Szabo-Stuban (41:00): So I don't need to I don't need to think about how do I refer 
David Szabo-Stuban (41:03): to different data. 
David Szabo-Stuban (41:05): And that's good because then I can just use JavaScript to transform any data set in 
David Szabo-Stuban (41:10): to any other debt, which means that I can forget about using things like 
David Szabo-Stuban (41:15): array aggregators and iterators and text parsers and whatnot. 
David Szabo-Stuban (41:19): Because I can just use JetGPT 
David Szabo-Stuban (41:21): to write the expression 
David Szabo-Stuban (41:23): or if the expression is not enough, 
David Szabo-Stuban (41:25): I can just use GPT to 
David Szabo-Stuban (41:27): write a piece of JavaScript code for me 
David Szabo-Stuban (41:30): and it can run it 
David Szabo-Stuban (41:32): locally, 
David Szabo-Stuban (41:34): natively, it can run custom codes. 
Dr. Dr. Rami Khouri (41:38): Inside. Hey. You just want to say for me right now, 
Dr. Dr. Rami Khouri (41:43): all the things that 
Dr. Dr. Rami Khouri (41:44): know, the code and the super base. It's 
Dr. Dr. Rami Khouri (41:49): I I have no knowledge. 
Dr. Dr. Rami Khouri (41:51): Background coding. So 
Dr. Dr. Rami Khouri (41:55): I think that 
Dr. Dr. Rami Khouri (41:56): I 
Dr. Dr. Rami Khouri (41:57): can learn the basic concept of this. 
Dr. Dr. Rami Khouri (42:02): How do I start, like, you know, have, 
David Szabo-Stuban (42:06): go through these steps. 
David Szabo-Stuban (42:07): In this article. Just go through the follow the steps 
David Szabo-Stuban (42:11): because this is designed to get you started as quickly as possible. 
Unknown (42:16): these four 
David Szabo-Stuban (42:15): Are these things. I do recommend that you that you look into them. 
David Szabo-Stuban (42:21): I'm I'm I'm preparing articles as well. 
David Szabo-Stuban (42:25): So I just wrote an article on node based thinking that I recommend that you read 
David Szabo-Stuban (42:30): I'm also 
David Szabo-Stuban (42:32): working on an article on data structures 
David Szabo-Stuban (42:36): that will be 
David Szabo-Stuban (42:37): sorry. This has already been written. 
David Szabo-Stuban (42:39): Is gonna go out next week. 
David Szabo-Stuban (42:42): And it explains data structures 
David Szabo-Stuban (42:46): really easily and really well on how to use things in 
Unknown (42:49): NA 10. 
David Szabo-Stuban (42:51): So so you're gonna have these articles 
David Szabo-Stuban (42:54): and 
Unknown (42:55): the HR 
David Szabo-Stuban (42:55): to for article, I created a custom GPT 
David Szabo-Stuban (42:59): that will actually help you understand these topics. 
David Szabo-Stuban (43:02): So 
David Szabo-Stuban (43:03): you can just use these custom GPTs to have 
David Szabo-Stuban (43:07): have you explained these topics even further 
David Szabo-Stuban (43:11): and you can ask questions from it. 
Unknown (43:13): This one 
David Szabo-Stuban (43:14): is specifically designed to explain to you node based thinking. 
Unknown (43:17): This one 
David Szabo-Stuban (43:18): is designed to explain to you data structures 
David Szabo-Stuban (43:21): to control flow, 
David Szabo-Stuban (43:23): So, let's say 
David Szabo-Stuban (43:25): I have a pseudo code 
David Szabo-Stuban (43:28): Here is yours, where is your pseudo code? 
David Szabo-Stuban (43:31): Here's your pseudo code that you sent to me 
David Szabo-Stuban (43:33): So I'm just gonna take the pseudo code that you wrote. 
David Szabo-Stuban (43:36): And, 
David Szabo-Stuban (43:39): Where is it? There you go. 
David Szabo-Stuban (43:41): So I just copy paste and say, 
David Szabo-Stuban (43:43): explain 
David Szabo-Stuban (43:45): the control 
David Szabo-Stuban (43:46): flow of this 
David Szabo-Stuban (43:49): this algorithm 
David Szabo-Stuban (43:50): or 
David Szabo-Stuban (43:51): I just put it in 
Dr. Dr. Rami Khouri (43:57): Thanks. 
Dr. Dr. Rami Khouri (44:01): That's 
David Szabo-Stuban (44:02): And then it starts actually explaining 
David Szabo-Stuban (44:05): the concepts of control flow through your specific example 
David Szabo-Stuban (44:10): And then you can ask follow-up questions. So this is this is I think this is the most effective way for you 
David Szabo-Stuban (44:14): start learning. 
Unknown (44:19): you two 
Dr. Dr. Rami Khouri (44:16): Now. How do you get the custom GPT to give two responses? 
David Szabo-Stuban (44:22): This is randomly allocated. 
David Szabo-Stuban (44:25): At 
David Szabo-Stuban (44:26): x a out. 
Unknown (44:28): every 300 
David Szabo-Stuban (44:27): Once out of prompts I send. 
David Szabo-Stuban (44:30): I 
David Szabo-Stuban (44:31): get these to this, and I don't control it 
Dr. Dr. Rami Khouri (44:35): Okay. 
Unknown (44:37): Okay. One 
Dr. Dr. Rami Khouri (44:37): more thing. You you wanted to talk to him about 
Dr. Dr. Rami Khouri (44:40): in line form. 
David Szabo-Stuban (44:42): Yes. So I'm 
Dr. Dr. Rami Khouri (44:43): not saying 
Dr. Dr. Rami Khouri (44:45): I I will need your help 
Dr. Dr. Rami Khouri (44:48): threw out our, 
Dr. Dr. Rami Khouri (44:52): What 
Dr. Dr. Rami Khouri (44:53): help me, 
Dr. Dr. Rami Khouri (44:55): Like, 
Dr. Dr. Rami Khouri (44:56): I have, prompt engineers 10 and there's software engineers 
Unknown (44:58): and a team. 
Dr. Dr. Rami Khouri (45:03): I'm trying. 
Dr. Dr. Rami Khouri (45:04): To find the 
Dr. Dr. Rami Khouri (45:07): best way to 
Dr. Dr. Rami Khouri (45:09): Okay. 
Dr. Dr. Rami Khouri (45:13): To communicate 
Unknown (45:14): the two 
Dr. Dr. Rami Khouri (45:14): between teams 
Dr. Dr. Rami Khouri (45:16): like finding the best, platform or 
Dr. Dr. Rami Khouri (45:21): language or communication 
Unknown (45:26): that's one that's one 
Dr. Dr. Rami Khouri (45:25): and of the the major 
Dr. Dr. Rami Khouri (45:30): say, 
Dr. Dr. Rami Khouri (45:31): issues on my 
Dr. Dr. Rami Khouri (45:34): they, 
Dr. Dr. Rami Khouri (45:35): day to day work. So if you have any, 
Dr. Dr. Rami Khouri (45:39): experience in this, you 
Dr. Dr. Rami Khouri (45:42): as, 
Dr. Dr. Rami Khouri (45:43): like, 
Dr. Dr. Rami Khouri (45:45): prote or as, software 
Unknown (45:45): engineer engineer, 
Dr. Dr. Rami Khouri (45:50): face those 
David Szabo-Stuban (45:51): Sure. 
David Szabo-Stuban (45:52): So I will give you I will give you a 
David Szabo-Stuban (45:56): an outline of 
David Szabo-Stuban (45:59): a documentation for architecting these 
David Szabo-Stuban (46:02): cognitive workflows and prompt 
David Szabo-Stuban (46:04): structures, 
Unknown (46:06): help engineers 
David Szabo-Stuban (46:06): that will understand what you want to achieve. 
David Szabo-Stuban (46:10): And then also the what I'm about to show you in lag flow 
David Szabo-Stuban (46:15): is that 
David Szabo-Stuban (46:16): is basically the specific way I always recommend 
David Szabo-Stuban (46:20): us to think about 
David Szabo-Stuban (46:21): chatbots and and other land processes. 
Dr. Dr. Rami Khouri (46:24): This 
David Szabo-Stuban (46:24): is 
David Szabo-Stuban (46:25): basically 
David Szabo-Stuban (46:26): Linkflow allows me to 
Unknown (46:29): eight 
David Szabo-Stuban (46:29): Three the AI part as a separate eye 
David Szabo-Stuban (46:32): isolated unit that I can manage without coding. 
Unknown (46:36): then engineers 
David Szabo-Stuban (46:35): And software can connect 
Unknown (46:39): and forth 
David Szabo-Stuban (46:38): back between my apps. So this is basically a container. 
David Szabo-Stuban (46:43): And land flow is also open source 
David Szabo-Stuban (46:46): So as you can see, I'm running this on my own railway server. 
David Szabo-Stuban (46:50): And I can create basic prompt structures. I can create 
David Szabo-Stuban (46:54): documents, vector store, 
David Szabo-Stuban (46:56): I can even create a starter agent 
David Szabo-Stuban (46:59): And there are a lot of templates here. 
David Szabo-Stuban (47:02): That we can we can 
David Szabo-Stuban (47:03): check that you can also check 
David Szabo-Stuban (47:06): and it's pretty good 
David Szabo-Stuban (47:08): and to show you a simple 
David Szabo-Stuban (47:10): Let's say there is a simple agent 
David Szabo-Stuban (47:13): I just click on this and it has these templates. 
David Szabo-Stuban (47:16): And it follows lang chain logic. 
David Szabo-Stuban (47:18): So here's the URL that we retrieved from the chat. 
David Szabo-Stuban (47:21): Here is a calculator tool 
David Szabo-Stuban (47:24): here's the chat input tool. So 
David Szabo-Stuban (47:26): this is the agent. So the agent has multiple tools 
Unknown (47:31): an ten 
David Szabo-Stuban (47:30): This is the exact same thing, what eight has here. 
Unknown (47:32): And Aiden 
David Szabo-Stuban (47:33): has the tools here. 
David Szabo-Stuban (47:35): And langflow has the 
David Szabo-Stuban (47:37): This is the agent. These are the tools. 
David Szabo-Stuban (47:39): Now what happens is that 
David Szabo-Stuban (47:41): The user sends the chat input to the agent 
David Szabo-Stuban (47:44): who decides which tool to call and then gives you a chat out 
David Szabo-Stuban (47:48): So 
David Szabo-Stuban (47:49): This means that 
David Szabo-Stuban (47:51): I in 
David Szabo-Stuban (47:53): All I need to do 
David Szabo-Stuban (47:55): is I can just add more tools if I want to. 
David Szabo-Stuban (47:59): And there are a bunch of 
David Szabo-Stuban (48:01): There are a bunch of specific tools here that I can select from. 
David Szabo-Stuban (48:05): I'm pretty sure that I can 
David Szabo-Stuban (48:06): also customized tools 
David Szabo-Stuban (48:08): to create create customers, 
David Szabo-Stuban (48:10): I will need to take a look. 
David Szabo-Stuban (48:13): Where is it? Tools. There you go. 
Dr. Dr. Rami Khouri (48:15): Integers 
Dr. Dr. Rami Khouri (48:16): How did they decide when to use a tool 
Dr. Dr. Rami Khouri (48:20): or to use another agent 
Dr. Dr. Rami Khouri (48:23): or maybe a tool 
Dr. Dr. Rami Khouri (48:25): Could be considered another agent? 
David Szabo-Stuban (48:27): Yeah. That's usually, 
David Szabo-Stuban (48:30): Let me show you that 
David Szabo-Stuban (48:34): What's the best way to do it? Okay. So 
David Szabo-Stuban (48:37): Let me find you 
Unknown (48:39): an English 
David Szabo-Stuban (48:40): language, 
David Szabo-Stuban (48:41): documents, 
David Szabo-Stuban (48:43): expense. Okay. So the way I do this is usually 
David Szabo-Stuban (48:47): follow these steps. 
David Szabo-Stuban (48:50): You have access to this. 
David Szabo-Stuban (48:53): Scattered lumberjacket as so, and this is also the 
Dr. Dr. Rami Khouri (48:55): cognitive 
David Szabo-Stuban (48:56): architect 
Unknown (48:56): your designer 
David Szabo-Stuban (48:57): work. 
Dr. Dr. Rami Khouri (48:57): I made the the regular article. Yeah. 
David Szabo-Stuban (49:00): So what you what you can do with this 
David Szabo-Stuban (49:04): is you can just copy paste all your notes. 
David Szabo-Stuban (49:07): And 
David Szabo-Stuban (49:07): what's gonna happen in the background. 
David Szabo-Stuban (49:10): Is is this. Let me show you. 
David Szabo-Stuban (49:14): Not 
Unknown (49:14): this one. This one. 
David Szabo-Stuban (49:17): Okay. So this is a complicated workflow. 
David Szabo-Stuban (49:20): And what happens is that once you pay paste in all your notes, 
David Szabo-Stuban (49:25): So let's say I copy paste all the documents you just sent me. 
David Szabo-Stuban (49:29): About your project. And then what happens is that 
David Szabo-Stuban (49:33): it it 
David Szabo-Stuban (49:34): it parses the data. 
David Szabo-Stuban (49:36): That you sent. Sorry. It's it sends it to an LMM 
Unknown (49:42): to three 
David Szabo-Stuban (49:41): that breaks it down main components. 
Unknown (49:44): The three 
David Szabo-Stuban (49:45): main components are gonna be the brief, this 
David Szabo-Stuban (49:47): technical specifications and any other notes that we have. 
David Szabo-Stuban (49:51): It parses it into a valid JSON 
David Szabo-Stuban (49:55): I define the structure here. 
David Szabo-Stuban (49:58): And then it saves the specifications in a data 
David Szabo-Stuban (50:02): base. 
David Szabo-Stuban (50:03): Then, 
David Szabo-Stuban (50:04): it generates that chain of thought 
David Szabo-Stuban (50:06): of thinking, 
David Szabo-Stuban (50:08): process. 
David Szabo-Stuban (50:09): And then generates a bunch of 
Unknown (50:11): artifacts one by one. 
David Szabo-Stuban (50:13): Now, what are the artifacts? 
David Szabo-Stuban (50:15): The artifacts in this case 
David Szabo-Stuban (50:19): are these these big parts, the summary, 
David Szabo-Stuban (50:22): the scope, the user story, etcetera. 
David Szabo-Stuban (50:24): And what happens is 
David Szabo-Stuban (50:26): that this reasoning process 
David Szabo-Stuban (50:29): processes all the docu all the documentation that you just 
David Szabo-Stuban (50:33): sent in. 
David Szabo-Stuban (50:34): And it summarizes the project 
David Szabo-Stuban (50:37): generates a scope description 
David Szabo-Stuban (50:39): creates a detailed user flow 
David Szabo-Stuban (50:43): of what happens from a user perspective. 
David Szabo-Stuban (50:46): Based on the process flows, as you can see, if there are multiple 
David Szabo-Stuban (50:50): gonna generate multiple. 
David Szabo-Stuban (50:52): Then it it generates a list of requirements 
David Szabo-Stuban (50:56): And then it generates 
David Szabo-Stuban (50:58): series of steps 
David Szabo-Stuban (50:59): This is following the input task output breakdown. 
David Szabo-Stuban (51:03): Because basically we are treating this 
David Szabo-Stuban (51:05): as if, you know, we were basically building logic gates and transistors. 
David Szabo-Stuban (51:10): Right? It's like, 
David Szabo-Stuban (51:11): you start with a new delivery, then you receive 
Unknown (51:14): first 
David Szabo-Stuban (51:14): delivery request data, then you end up with a structured delivery request 
David Szabo-Stuban (51:18): and so on. So this is similar to what you've done before. 
David Szabo-Stuban (51:22): And once we have this, 
David Szabo-Stuban (51:24): ITO table, 
David Szabo-Stuban (51:26): Then, 
David Szabo-Stuban (51:27): we create this task modality matrix 
Unknown (51:33): from one 
David Szabo-Stuban (51:30): which is a series of steps on how we move element to another. 
David Szabo-Stuban (51:35): This is when you this is the point when you can make the decision 
Unknown (51:40): an agent or two agents or two 
David Szabo-Stuban (51:39): if you need or a simple LLM call LLM 
David Szabo-Stuban (51:44): cause 
David Szabo-Stuban (51:44): because 
David Szabo-Stuban (51:45): Once you start putting these steps into this table, 
David Szabo-Stuban (51:49): sometimes, 
Unknown (51:52): from one 
David Szabo-Stuban (51:50): you will feel that the jump to 
David Szabo-Stuban (51:53): to another is too big. 
David Szabo-Stuban (51:55): Say let's say that 
David Szabo-Stuban (51:57): in in seven 
Unknown (51:57): step 17 to seventeen to 18. 
David Szabo-Stuban (52:01): Or it it summarized everything together. That's fine. So let's say 
David Szabo-Stuban (52:06): in step 
Unknown (52:07): 17 to 18. 
David Szabo-Stuban (52:09): Let's say that you would need to both 
David Szabo-Stuban (52:12): categorize, generate 
David Szabo-Stuban (52:14): and and create, or parse of an audio from, into text. 
David Szabo-Stuban (52:19): steps, 
Unknown (52:19): That's three not one. 
David Szabo-Stuban (52:21): And if you think about it, 
David Szabo-Stuban (52:23): you will realize that, hold on. This is too much of a step or too big of a step. 
David Szabo-Stuban (52:27): Need to 
Unknown (52:31): to three 
David Szabo-Stuban (52:28): I I need to stop and break it down smaller steps. 
David Szabo-Stuban (52:33): And 
Unknown (52:36): the agent 
David Szabo-Stuban (52:33): Sometimes you can just give the whole thing to and see if it works. 
David Szabo-Stuban (52:38): And if it does, you know, that you don't need to break it down any further. 
David Szabo-Stuban (52:42): And once you've once you've done this, 
David Szabo-Stuban (52:44): there is, like, some extra documentation on further opportunities 
David Szabo-Stuban (52:48): bake, bake 
David Szabo-Stuban (52:49): horizontal expansion means that input 
David Szabo-Stuban (52:53): or not what's 
Unknown (52:51): the first multiple five 
David Szabo-Stuban (52:54): had can be formats and destinations. 
David Szabo-Stuban (52:58): Vertical egg integration means that 
Unknown (53:01): a 
David Szabo-Stuban (53:01): you have zero or even earlier steps that you're adding more steps to this 
David Szabo-Stuban (53:06): process either in the 
David Szabo-Stuban (53:08): in the beginning or at the end of the process. 
David Szabo-Stuban (53:11): This is the doc, and also there are a couple estimations, but these are for my 
David Szabo-Stuban (53:16): self. This is the structure that I create. 
David Szabo-Stuban (53:20): As a baseline of the architecture for all of my clients at my day job. 
David Szabo-Stuban (53:24): And you can do the same thing 
David Szabo-Stuban (53:26): And if you build this, 
David Szabo-Stuban (53:27): then you will be able to follow this logic 
David Szabo-Stuban (53:31): and determine if you need an AI agent or or an all of that 
David Szabo-Stuban (53:34): all our multiple agents 
David Szabo-Stuban (53:37): and also 
Unknown (53:39): your developers 
David Szabo-Stuban (53:38): This is something that will understand a lot better. 
Dr. Dr. Rami Khouri (53:44): Well, okay. And 
Dr. Dr. Rami Khouri (53:48): So I was trying to this this looks 
Dr. Dr. Rami Khouri (53:51): amazing that's, 
Dr. Dr. Rami Khouri (53:53): You can put 
Dr. Dr. Rami Khouri (53:56): every, you 
David Szabo-Stuban (53:57): know, 
David Szabo-Stuban (53:58): Yeah. Just 
Dr. Dr. Rami Khouri (53:59): copy paste 
David Szabo-Stuban (53:59): it. Just copy paste everything in here. 
Unknown (54:03): Because Gemini talks Hebrew. 
David Szabo-Stuban (54:05): And you just said it does. 
David Szabo-Stuban (54:07): Then I think you can try 
Unknown (54:11): your Hebrew, 
David Szabo-Stuban (54:09): putting in your, your, notes 
David Szabo-Stuban (54:13): as well. I 
Dr. Dr. Rami Khouri (54:14): think it's 
David Szabo-Stuban (54:15): gonna 
Dr. Dr. Rami Khouri (54:15): understand. 
David Szabo-Stuban (54:16): It's 
Dr. Dr. Rami Khouri (54:16): not the issue. It's that 
Dr. Dr. Rami Khouri (54:18): and how organized on 
David Szabo-Stuban (54:21): the 
Dr. Dr. Rami Khouri (54:21): organization 
Unknown (54:23): this one 
David Szabo-Stuban (54:22): part is what does. 
David Szabo-Stuban (54:24): So So 
Dr. Dr. Rami Khouri (54:24): I I wanted, and and let's say 
Dr. Dr. Rami Khouri (54:27): I'm trying to organize. I have all the trust 
Dr. Dr. Rami Khouri (54:31): subscriptions, a transcript, record all all our meetings. 
Unknown (54:35): months 
Dr. Dr. Rami Khouri (54:35): Two of meetings on the organization. 
Dr. Dr. Rami Khouri (54:38): The innovation, clinical, business financial, all the 
Dr. Dr. Rami Khouri (54:42): aspects of our organization. I have the meetings. And I am 
Dr. Dr. Rami Khouri (54:47): struggling to 
Dr. Dr. Rami Khouri (54:50): Organize 
Dr. Dr. Rami Khouri (54:52): may create, manual 
Dr. Dr. Rami Khouri (54:54): or an SOP, something that I can use as a start 
Unknown (54:59): an agent 
Dr. Dr. Rami Khouri (54:59): of that I can 
Dr. Dr. Rami Khouri (55:01): use it to create documents to summarize 
Dr. Dr. Rami Khouri (55:04): meetings, something that have a real 
Dr. Dr. Rami Khouri (55:07): actual 
Dr. Dr. Rami Khouri (55:10): context and knowledge of what we do 
Dr. Dr. Rami Khouri (55:13): Is this is this 
Dr. Dr. Rami Khouri (55:14): something that 
Dr. Dr. Rami Khouri (55:16): You know, I, like, tried 
Dr. Dr. Rami Khouri (55:17): a lot of, you know, note notebook, Lamb, I tried to use Owen Pro to 
Dr. Dr. Rami Khouri (55:23): may, did research 
Dr. Dr. Rami Khouri (55:27): I can't 
Dr. Dr. Rami Khouri (55:28): I I I think I need to do something with the transcripts. 
David Szabo-Stuban (55:32): Yeah. 
Dr. Dr. Rami Khouri (55:33): Multiple steps and 
Dr. Dr. Rami Khouri (55:35): I don't know what to do with this. 
David Szabo-Stuban (55:36): Okay. So the 
David Szabo-Stuban (55:38): problem is that what you're trying to do is you're just trying to 
David Szabo-Stuban (55:41): treat this whole thing of, here's a transcript 
David Szabo-Stuban (55:44): turn it into something useful. 
David Szabo-Stuban (55:47): You treat you're treating that as a black box. 
David Szabo-Stuban (55:49): So and you're trying to give the whole box to an AI system. 
David Szabo-Stuban (55:53): And then it fails. 
David Szabo-Stuban (55:55): So what you need to do is you need to open the box. 
David Szabo-Stuban (55:58): And you need to start 
David Szabo-Stuban (55:59): he can get apart. 
Unknown (56:01): into five 
David Szabo-Stuban (56:01): And turn it smaller boxes. 
David Szabo-Stuban (56:04): And some of the some of those boxes 
David Szabo-Stuban (56:06): will be something that AI can handle. Some other boxes are gonna be stuff that 
David Szabo-Stuban (56:11): simple software can handle. 
David Szabo-Stuban (56:14): That's what you need to really think through. 
David Szabo-Stuban (56:16): That if if the task cannot be done by AI, 
David Szabo-Stuban (56:20): then how can I 
David Szabo-Stuban (56:22): How can I break it down to big 
Unknown (56:25): components, three 
Dr. Dr. Rami Khouri (56:26): or components, and try again? 
Dr. Dr. Rami Khouri (56:28): To give it to another AI 
Dr. Dr. Rami Khouri (56:30): because I don't have the 
Dr. Dr. Rami Khouri (56:32): the time That's 
David Szabo-Stuban (56:33): that's but then you're repeating the same 
Unknown (56:35): mistake, Rami. 
David Szabo-Stuban (56:36): Because what you're trying to do is you're trying to give the same 
David Szabo-Stuban (56:41): thing 
David Szabo-Stuban (56:41): to different AI systems. 
David Szabo-Stuban (56:43): But what you need to change is not the system. 
David Szabo-Stuban (56:46): What you need to change is what you give to the system. You cannot give the entire 
Unknown (56:52): the agent 
David Szabo-Stuban (56:51): problem to because it will fail. You already told so. 
David Szabo-Stuban (56:55): What you need to do is take that task. Hey, here is a trans 
David Szabo-Stuban (56:59): shift. I want to turn it into some meeting memo 
David Szabo-Stuban (57:02): good. 
David Szabo-Stuban (57:02): Now take that problem. 
Unknown (57:06): not one 
David Szabo-Stuban (57:05): And dissect it. It's one step. If you do it, 
David Szabo-Stuban (57:09): manually. You're not doing it 
David Szabo-Stuban (57:11): it's not a black box when you put in 
David Szabo-Stuban (57:14): a a transcript and you get a and you get a meeting memo. 
David Szabo-Stuban (57:17): There are multiple steps involved. 
David Szabo-Stuban (57:19): Uncover what those steps are. 
David Szabo-Stuban (57:21): You need to think through what the what's the process 
David Szabo-Stuban (57:25): of you creating a transcript. If you had to do it manually, 
David Szabo-Stuban (57:29): Think about what the process you need to do actually is. 
David Szabo-Stuban (57:32): And then write that down. 
David Szabo-Stuban (57:34): Because what you're currently doing 
David Szabo-Stuban (57:37): is 
David Szabo-Stuban (57:38): basically let me show you. Basically, 
David Szabo-Stuban (57:41): You take this 
David Szabo-Stuban (57:43): You take this table, 
David Szabo-Stuban (57:44): And what you're currently saying is 
David Szabo-Stuban (57:47): Here, an input I have transcript. 
David Szabo-Stuban (57:50): And here in output, I have meeting memo. 
Unknown (57:52): And one 
David Szabo-Stuban (57:53): step. 
David Szabo-Stuban (57:55): And then you just give the whole thing to the to 
David Szabo-Stuban (57:57): to a reasoning model and see, think about it and do it. 
David Szabo-Stuban (58:01): And it fails. 
David Szabo-Stuban (58:03): And 
David Szabo-Stuban (58:03): And it doesn't matter why it fails. What matters to is that it fails. 
David Szabo-Stuban (58:07): Which means that the task is too complicated. 
David Szabo-Stuban (58:10): It confuses the model. 
David Szabo-Stuban (58:12): So you need to turn it into 
David Szabo-Stuban (58:14): tasks, 
Unknown (58:14): four not one. 
David Szabo-Stuban (58:16): And then try again for each and every one of those. 
David Szabo-Stuban (58:19): And if you do this enough times, 
David Szabo-Stuban (58:22): you will find the breakdown 
David Szabo-Stuban (58:24): where you actually can solve the problem. 
David Szabo-Stuban (58:28): And you what you will find is that in some cases, 
David Szabo-Stuban (58:32): some of these tasks 
David Szabo-Stuban (58:33): are not actually going to be Allah based. 
David Szabo-Stuban (58:36): They're not going to be done by AI. It's just gonna be simpler software. Like, look at this. 
Unknown (58:42): the first 
David Szabo-Stuban (58:41): Here, task is validation. 
David Szabo-Stuban (58:44): That's not an AI task. That's just software. 
David Szabo-Stuban (58:48): categorization, that's AI. 
Unknown (58:47): The second one Third one, 
David Szabo-Stuban (58:51): LLM, 
David Szabo-Stuban (58:52): Okay. That's also AI. 
Unknown (58:54): Fourth one, 
David Szabo-Stuban (58:55): capture and store user data. 
David Szabo-Stuban (58:58): That's not AI. That's just software. 
David Szabo-Stuban (59:00): Display user friendly error message. 
David Szabo-Stuban (59:02): That's just the software. 
David Szabo-Stuban (59:04): Trigled fallback mechanism. 
David Szabo-Stuban (59:06): That's also software. Generate reports. That's AI. 
David Szabo-Stuban (59:10): Analyze and process that's AI. It's electronic relevant proposal templates. 
David Szabo-Stuban (59:15): Selection of the template 
David Szabo-Stuban (59:16): is an AI, but then storing them 
David Szabo-Stuban (59:19): is not an AI. So it's a mix. 
Unknown (59:23): one 
Dr. Dr. Rami Khouri (59:22): Yeah. So, last question. 
Dr. Dr. Rami Khouri (59:25): I I think that who was gonna doing 
Dr. Dr. Rami Khouri (59:28): This is project 
Unknown (59:29): our manager. 
Dr. Dr. Rami Khouri (59:31): Aim, 
Dr. Dr. Rami Khouri (59:32): Do you think that 
Dr. Dr. Rami Khouri (59:33): we need someone with, 
Dr. Dr. Rami Khouri (59:36): background and 
Dr. Dr. Rami Khouri (59:38): a I 
Dr. Dr. Rami Khouri (59:40): to do this or we can I can give this to 
Unknown (59:45): manager 
Dr. Dr. Rami Khouri (59:43): our current, product and 
Dr. Dr. Rami Khouri (59:46): just like 
Dr. Dr. Rami Khouri (59:47): use it? 
David Szabo-Stuban (59:50): This well, this this won't be enough. 
Unknown (59:54): a engineer 
David Szabo-Stuban (59:54): For software to build the whole thing. 
David Szabo-Stuban (59:57): But this will be enough to start working out 
David Szabo-Stuban (00:01): how does the architecture need to look right? 
Unknown (00:06): a architect 
David Szabo-Stuban (00:03): What you're currently lacking is solution that 
David Szabo-Stuban (00:07): specializes in AI. 
David Szabo-Stuban (00:09): And I know that's my that's what I do as a day job. 
David Szabo-Stuban (00:12): That's what I do for these banks. And I can tell you that 
Unknown (00:17): single one 
David Szabo-Stuban (00:16): every of these banks are trying to find people like this 
David Szabo-Stuban (00:20): and these people are basically nonexistent. 
David Szabo-Stuban (00:24): So it it it is a big it is a big challenge. 
Unknown (00:29): our CEO 
David Szabo-Stuban (00:28): But let let me talk to and see if 
David Szabo-Stuban (00:31): we can provide you with the resources 
Unknown (00:37): the two 
David Szabo-Stuban (00:35): to to bridge that gap between teams. 
Unknown (00:41): our manager 
Dr. Dr. Rami Khouri (00:40): Yeah. Because we product is 
Dr. Dr. Rami Khouri (00:43): leaving 
Dr. Dr. Rami Khouri (00:44): and 
Dr. Dr. Rami Khouri (00:46): So I I'm thinking 
Dr. Dr. Rami Khouri (00:47): on the the next hire 
Dr. Dr. Rami Khouri (00:51): if I need to, you know, to search for someone with 
Dr. Dr. Rami Khouri (00:55): a background because 
Dr. Dr. Rami Khouri (00:57): I'm 
Unknown (00:59): a clinician. 
Dr. Dr. Rami Khouri (01:00): That 
Dr. Dr. Rami Khouri (01:01): I left the that trick 
Unknown (01:03): actual kremonk. 
Dr. Dr. Rami Khouri (01:04): I 
Dr. Dr. Rami Khouri (01:05): video now is 
Dr. Dr. Rami Khouri (01:06): managing and, you know, the the whole innovation 
Dr. Dr. Rami Khouri (01:12): design and enter 
Dr. Dr. Rami Khouri (01:14): for new ship 
Dr. Dr. Rami Khouri (01:15): of the this thing, but but I'm not 
Unknown (01:17): a manager, a manager. 
Dr. Dr. Rami Khouri (01:18): product I I have a team. I'm not good at it. 
Dr. Dr. Rami Khouri (01:22): So I need another person that have an a knowledge and I think 
Dr. Dr. Rami Khouri (01:26): that I have uh-uh an answers. 
David Szabo-Stuban (01:29): Okay. Look, so 
Unknown (01:32): you two 
David Szabo-Stuban (01:31): I'm gonna send email addresses here. 
David Szabo-Stuban (01:35): And, 
David Szabo-Stuban (01:36): What I would like you to do is 
David Szabo-Stuban (01:40): Drop me an email, please. 
David Szabo-Stuban (01:42): With all the with with 
David Szabo-Stuban (01:45): briefs, 
David Szabo-Stuban (01:46): in the project. Let's just assume that I'm a complete stranger, and I have no 
David Szabo-Stuban (01:51): previous background in what you're doing. 
David Szabo-Stuban (01:54): And you just hired me 
David Szabo-Stuban (01:56): help you build these things out. 
David Szabo-Stuban (01:58): And solve these projects. 
David Szabo-Stuban (02:01): Send me all the documentation that you have 
David Szabo-Stuban (02:04): And here are email addresses. This is my email and my 
Unknown (02:05): these two CEO's 
David Szabo-Stuban (02:09): email. 
David Szabo-Stuban (02:10): And 
David Szabo-Stuban (02:11): Once you send this, 
David Szabo-Stuban (02:12): brief 
Unknown (02:14): my CEO 
David Szabo-Stuban (02:13): I can talk to about 
David Szabo-Stuban (02:17): giving you guys a, a rundown of this. 
David Szabo-Stuban (02:20): So for every project, 
David Szabo-Stuban (02:22): we will 
David Szabo-Stuban (02:23): If we start this conversation, 
David Szabo-Stuban (02:25): For every project, we can build this documentation for you for free. 
David Szabo-Stuban (02:30): That's not a problem. 
David Szabo-Stuban (02:32): As long as, you know, 
David Szabo-Stuban (02:34): there is a potential for a company to do business with you 
David Szabo-Stuban (02:37): then this is usually something that we already generate for 
David Szabo-Stuban (02:41): the proposal stage 
David Szabo-Stuban (02:42): anyway. 
Dr. Dr. Rami Khouri (02:44): Okay. 
Dr. Dr. Rami Khouri (02:47): Where did you send me the mails? 
David Szabo-Stuban (02:49): It's in the chat. 
David Szabo-Stuban (02:50): Here in Meet. 
Unknown (02:51): the Google First. 
Dr. Dr. Rami Khouri (02:52): Okay. 
David Szabo-Stuban (02:53): Because it's it's a it's each 
David Szabo-Stuban (02:55): Should be my email, not, 
David Szabo-Stuban (02:58): Not my private email. 
Dr. Dr. Rami Khouri (03:04): So, basically, 
Dr. Dr. Rami Khouri (03:07): I think, right now, I 
Unknown (03:16): three, 
David Szabo-Stuban (03:17): I'm here. 
Dr. Dr. Rami Khouri (03:20): I I 
Dr. Dr. Rami Khouri (03:21): contacting you, through 
Dr. Dr. Rami Khouri (03:25): subscribe. 
David Szabo-Stuban (03:27): Yeah. 
Dr. Dr. Rami Khouri (03:29): Where do you prefer if I have a question or something to send you a message? 
David Szabo-Stuban (03:34): Send me emails. 
Unknown (03:36): best one. 
David Szabo-Stuban (03:36): That's the The 
David Szabo-Stuban (03:38): Right? So if you have questions for me personally, 
David Szabo-Stuban (03:42): send me emails to my, to my private email address. 
Dr. Dr. Rami Khouri (03:47): Okay. 
Unknown (03:51): the group 
David Szabo-Stuban (03:48): Okay. And do do send me the documentation to Stylers email address, please, and we will get back to you on that. 
Dr. Dr. Rami Khouri (03:58): Hi. 
Dr. Dr. Rami Khouri (03:59): Thank you. 
David Szabo-Stuban (04:00): Cool. Our time is over for today. When should we talk next 
Dr. Dr. Rami Khouri (04:12): Hi. Thanks. 
Dr. Dr. Rami Khouri (04:16): I 
Unknown (04:17): first 
Dr. Dr. Rami Khouri (04:17): time. 
Dr. Dr. Rami Khouri (04:18): One 
Unknown (04:19): week. 
David Szabo-Stuban (04:20): Okay. How's next Friday? 
David Szabo-Stuban (04:23): This time 
David Szabo-Stuban (04:26): Say 
Dr. Dr. Rami Khouri (04:26): same time 
David Szabo-Stuban (04:27): slot, but next Friday. 
David Szabo-Stuban (04:29): Five 
Dr. Dr. Rami Khouri (04:32): Friday, 
Dr. Dr. Rami Khouri (04:36): And on Fridays, I'm I work to, 
Dr. Dr. Rami Khouri (04:40): twelve Israel Times. 
Dr. Dr. Rami Khouri (04:48): I may generally, I I do not prefer to 
Dr. Dr. Rami Khouri (04:52): I have meetings, Fridays. 
David Szabo-Stuban (04:54): Okay. 
David Szabo-Stuban (04:56): Then we can do Thursday too. 
Dr. Dr. Rami Khouri (04:59): Thursday. 
David Szabo-Stuban (05:00): Okay. 
David Szabo-Stuban (05:04): Okay. I'm sending you the invite. 
Dr. Dr. Rami Khouri (05:07): Thank you. 
David Szabo-Stuban (05:09): Okay. It might send 
David Szabo-Stuban (05:12): alright. 
David Szabo-Stuban (05:13): Chummy. 
David Szabo-Stuban (05:14): Thank you so much for your time today. 
Dr. Dr. Rami Khouri (05:15): Looking forward 
David Szabo-Stuban (05:16): to getting the emails from you. 
Dr. Dr. Rami Khouri (05:18): Thank you. Thank you very much. 
David Szabo-Stuban (05:20): Alright. 
Dr. Dr. Rami Khouri (05:21): Take 
David Szabo-Stuban (05:21): care. 
David Szabo-Stuban (05:22): Bye
```