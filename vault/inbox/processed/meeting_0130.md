---
alfred_tags:
- meetings/processing
- data/json-to-markdown
processed_at: '2026-02-26T20:12:24.946805+00:00'
relationships:
- confidence: 0.75
  context: similar processed meetings
  source: inbox/processed/meeting_0130.md
  target: inbox/processed/meeting_0248.md
  type: related-to
- confidence: 0.95
  context: derived from raw notes
  source: inbox/processed/meeting_0130.md
  target: inbox/meeting_0130.md
  type: depends-on
status: processed
---

_ = r"""
import json

# Load all the necessary data
with open("/home/ubuntu/row_data/row_0130.json", "r") as f:
    meeting_data = json.load(f)

with open("/home/ubuntu/participants.json", "r") as f:
    participants_data = json.load(f)

with open("/home/ubuntu/transcript_updated.txt", "r") as f:
    transcript = f.read()

# Extract data for the markdown file
transcript_title = meeting_data.get("transcript_title", "N/A")
date = meeting_data.get("date", "N/A")
classification = meeting_data.get("classification", "N/A")
category = meeting_data.get("category", "N/A")
meeting_title = meeting_data.get("meeting_title", "N/A")
transcript_url = meeting_data.get("transcript_url", "N/A")
main_topics = meeting_data.get("main_topics", "").split(', ')

# Create the participants table
participants_table = "| Name | Role | Confidence |\n| :--- | :--- | :--- |\n"
for p in participants_data:
    participants_table += f'| {p["Name"]} | {p["Role"]} | {p["Confidence"]} |\n'

# Create the topics list
topics_list = ""
for topic in main_topics:
    topics_list += f"- {topic}\n"

# Assemble the final markdown content
markdown_content = f"""
# Meeting: {transcript_title}

---

## 1. Meeting Details

| Field | Value |
| :--- | :--- |
| **Date** | {date} |
| **Title** | {transcript_title} |
| **Classification** | {classification if classification else "N/A"} |
| **Category** | {category if category else "N/A"} |
| **Meeting Type** | {meeting_title if meeting_title else "N/A"} |
| **Source Document** | [{transcript_url}]({transcript_url}) |

## 2. Participants

{participants_table}

## 3. Key Topics

{topics_list}

## 4. Full Transcript

> **Note:** Transcript language matches the original meeting language.

---

```
{transcript}
```
"""

# Write the markdown file
with open(f'/home/ubuntu/meeting_{meeting_data["index"]:04d}.md', "w") as f:
    f.write(markdown_content)

print("Markdown file created successfully.")
"""
import json

# Load all the necessary data
with open("/home/ubuntu/row_data/row_0130.json", "r") as f:
    meeting_data = json.load(f)

with open("/home/ubuntu/participants.json", "r") as f:
    participants_data = json.load(f)

with open("/home/ubuntu/transcript_updated.txt", "r") as f:
    transcript = f.read()

# Extract data for the markdown file
transcript_title = meeting_data.get("transcript_title", "N/A")
date = meeting_data.get("date", "N/A")
classification = meeting_data.get("classification", "N/A")
category = meeting_data.get("category", "N/A")
meeting_title = meeting_data.get("meeting_title", "N/A")
transcript_url = meeting_data.get("transcript_url", "N/A")
main_topics = meeting_data.get("main_topics", "").split(', ')

# Create the participants table
participants_table = "| Name | Role | Confidence |\n| :--- | :--- | :--- |\n"
for p in participants_data:
    participants_table += f'| {p["Name"]} | {p["Role"]} | {p["Confidence"]} |\n'

# Create the topics list
topics_list = ""
for topic in main_topics:
    topics_list += f"- {topic}\n"

# Assemble the final markdown content
markdown_content = f"""
# Meeting: {transcript_title}

---

## 1. Meeting Details

| Field | Value |
| :--- | :--- |
| **Date** | {date} |
| **Title** | {transcript_title} |
| **Classification** | {classification if classification else "N/A"} |
| **Category** | {category if category else "N/A"} |
| **Meeting Type** | {meeting_title if meeting_title else "N/A"} |
| **Source Document** | [{transcript_url}]({transcript_url}) |

## 2. Participants

{participants_table}

## 3. Key Topics

{topics_list}

## 4. Full Transcript

> **Note:** Transcript language matches the original meeting language.

---

```
{transcript}
```
"""

# Write the markdown file
with open(f'/home/ubuntu/meeting_{meeting_data["index"]:04d}.md', "w") as f:
    f.write(markdown_content)

print("Markdown file created successfully.")