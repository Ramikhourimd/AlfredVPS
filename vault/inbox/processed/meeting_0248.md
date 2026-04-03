---
alfred_tags:
- meetings/processing
- data/json-to-markdown
processed_at: '2026-02-26T20:22:45.810112+00:00'
relationships:
- confidence: 0.95
  context: derived from raw notes
  source: inbox/processed/meeting_0248.md
  target: inbox/meeting_0248.md
  type: depends-on
status: processed
---

'''
import json
import re
import sys

def generate_markdown():
    try:
        # 1. Read data file
        with open("/home/ubuntu/row_data/row_0248.json", "r") as f:
            data = json.load(f)

        row_index = data["index"]
        date = data["date"].split("T")[0]
        transcript_title = data["transcript_title"]
        classification = data.get("classification") or "N/A"
        category = data.get("category") or "N/A"
        meeting_title = data.get("meeting_title") or "N/A"
        speakers_json_str = data["speakers"]
        transcript_url = data["transcript_url"]
        main_topics_str = data.get("main_topics", "")

        # 2. Read and clean transcript
        with open("transcript.txt", "r", encoding="utf-8") as f:
            transcript_text = f.read()
        
        if transcript_text.startswith("\ufeff"):
            transcript_text = transcript_text[1:]
        
        transcript_length = len(transcript_text)

        # 3. Parse speakers and create replacement map
        speakers_json_str_fixed = f'[{speakers_json_str}]'.replace("}, {", "},{")
        try:
            speakers_data = json.loads(speakers_json_str_fixed)
        except json.JSONDecodeError as e:
            speakers_data = []

        replacement_map = {}
        participants_table_rows = []
        for speaker in speakers_data:
            name = speaker.get("name")
            label = speaker.get("label_in_transcript")
            role = speaker.get("role", "N/A")
            confidence = speaker.get("confidence", "N/A")
            
            if label and name:
                clean_name = name.split("(")[0].strip()
                replacement_map[label] = clean_name
            
            participants_table_rows.append(f"| {name} | {role} | {confidence} |")

        participants_table = "\n".join(participants_table_rows)

        # 4. Replace speaker labels in transcript
        speakers_replaced_count = 0
        modified_transcript = transcript_text
        for label, name in replacement_map.items():
            pattern = re.compile(f"^{re.escape(label)}\\s*\\(.*\\):", re.MULTILINE)
            occurrences = len(re.findall(pattern, modified_transcript))
            speakers_replaced_count += occurrences
            modified_transcript = re.sub(pattern, f"{name}:", modified_transcript)

        # 5. Format main topics
        main_topics_list = [f"- {topic.strip()}" for topic in main_topics_str.split(',') if topic.strip()]
        main_topics = "\n".join(main_topics_list)

        # 6. Generate Markdown file content
        md_content = f"""
# Meeting: {transcript_title}

---

## 1. Meeting Details

| Field | Value |
| :--- | :--- |
| **Date** | {date} |
| **Title** | {transcript_title} |
| **Classification** | {classification} |
| **Category** | {category} |
| **Meeting Type** | {meeting_title} |
| **Source Document** | [{transcript_url}]({transcript_url}) |

## 2. Participants

| Name | Role | Confidence |
| :--- | :--- | :--- |
{participants_table}

## 3. Key Topics

{main_topics}

## 4. Full Transcript

> **Note:** Transcript language matches the original meeting language.

---

```
{modified_transcript}
```
"""

        # 7. Save the Markdown file
        md_filename = f"meeting_{row_index:04d}.md"
        with open(md_filename, "w", encoding="utf-8") as f:
            f.write(md_content)

        result = {
            "md_file": f"/home/ubuntu/{md_filename}",
            "status": "success",
            "row_index": row_index,
            "transcript_length": transcript_length,
            "speakers_replaced": speakers_replaced_count
        }
        print(json.dumps(result))

    except Exception as e:
        result = {
            "status": f"error: {str(e)}",
            "row_index": data.get('index', -1) if 'data' in locals() else -1,
            "transcript_length": 0,
            "speakers_replaced": 0,
            "md_file": None
        }
        print(json.dumps(result))

if __name__ == "__main__":
    generate_markdown()
'''