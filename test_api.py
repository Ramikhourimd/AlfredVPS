import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()
OPENROUTER_API_KEY = os.environ.get("OPENROUTER_API_KEY")

SYSTEM_PROMPT = """You are Alfred, a highly intelligent and capable assistant.
Your goal is to help Rami Khouri manage his vault (a local markdown knowledge base).
You can read records, edit them, create new ones, and delete them.
When asked to perform a task, use the tools provided to you.
You are running locally on his Mac Studio.
Be concise but helpful."""

QA_MODE_PROMPT = """# KNOWLEDGE BASE REFINEMENT MODE (Q&A)

You are now in a specialized Q&A mode. Your objective is ONLY to refine the knowledge base to ensure data integrity, completeness, and accuracy.

## Directives:

1.  **Audit the Vault First:** Before asking any questions, use `vault_search` to audit existing records. Look for missing information, empty fields, or contradictions.
2.  **Smart, Close-Ended Questions:** Only ask highly specific questions, preferably **Yes/No** or multiple-choice questions. DO NOT ask open-ended questions.
3.  **Provide Context:** Before asking, show the user what you found. (e.g., "I see the record for John Doe is missing a job title.")
4.  **Acknowledge Uncertainty:** Always provide an explicit option for the user to answer with "Not relevant" or "Not enough information".
5.  **Cluster Questions:** To be efficient, ask questions in clusters of 3-5 at a time, numbered clearly.
6.  **Take Action:** Once the user answers, immediately use the appropriate `vault_*` tools to update the records. DO NOT just say "I will update this." Queue the tool calls.
7.  **Iterate:** After taking action, proceed to finding the next batch of missing or contradictory data.

Example format:
"1. Is the email address for Jane Smith 'jane@example.com'? (Yes / No / Not sure)
 2. Should I delete the duplicate record for 'Project X' created on 2026-01-01? (Yes / No / Keep both)"
"""

def call_llm(messages, tools=None):
    headers = {"Authorization": f"Bearer {OPENROUTER_API_KEY}", "Content-Type": "application/json"}
    body = {
        "model": "anthropic/claude-sonnet-4.6",
        "messages": messages,
        "reasoning": {"effort": "high"},
    }
    if tools:
        body["tools"] = tools
    resp = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=body)
    if resp.status_code != 200:
        err_msg = f"API error {resp.status_code}: {resp.text[:200]}"
        print(err_msg)
        return None, err_msg
    try:
        resp_json = resp.json()
        choice = resp_json["choices"][0]
        return choice["message"], None
    except Exception as e:
        print(f"Error parsing API response: {e}\nResponse text: {resp.text[:500]}")
        return None, f"Parsing error: {e}"

llm_msgs = [{"role": "system", "content": SYSTEM_PROMPT + "\n\n" + QA_MODE_PROMPT}]
llm_msgs.append({"role": "assistant", "content": "Hello! I'm initiating a Q&A session to refine your knowledge base. I will audit existing records, find missing or contradictory data, and ask you specific questions to fill in the gaps. Let's start!"})

TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "vault_search",
            "description": "Search the vault for records matching a query. Returns the top 5 most similar records with their content.",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {"type": "string", "description": "The search query text"}
                },
                "required": ["query"]
            }
        }
    }
]

print("Testing QA mode llm call...")
reply, err = call_llm(llm_msgs, tools=TOOLS)

if err:
    print(f"ERROR: {err}")
else:
    print(f"SUCCESS: {reply}")
