"""Google Workspace connector for Alfred.

Provides authenticated Gmail, Calendar, and Drive clients using
existing OAuth tokens from the plaud_automation pipeline.
"""

import os
import json
from pathlib import Path
from datetime import datetime, timedelta

from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# ── Config ──────────────────────────────────────────────────
CLIENT_SECRET_FILE = Path("/Users/ramikhouri/Documents/client_secret_271845292329-8suhoh53na79394jp2qibr9ql1h4bsii.apps.googleusercontent.com.json")
TOKEN_FILE = Path("/Users/ramikhouri/Desktop/Alfred/data/google_token.json")

SCOPES = [
    "https://www.googleapis.com/auth/gmail.readonly",
    "https://www.googleapis.com/auth/gmail.send",
    "https://www.googleapis.com/auth/gmail.modify",
    "https://www.googleapis.com/auth/calendar.readonly",
    "https://www.googleapis.com/auth/calendar.events",
    "https://www.googleapis.com/auth/drive.readonly",
    "https://www.googleapis.com/auth/drive.metadata.readonly",
]


def get_credentials() -> Credentials:
    """Load or refresh Google OAuth2 credentials."""
    creds = None

    if TOKEN_FILE.exists():
        creds = Credentials.from_authorized_user_file(str(TOKEN_FILE), SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
            TOKEN_FILE.write_text(creds.to_json())
        else:
            if not CLIENT_SECRET_FILE.exists():
                raise FileNotFoundError(f"OAuth client secret not found: {CLIENT_SECRET_FILE}")
            flow = InstalledAppFlow.from_client_secrets_file(str(CLIENT_SECRET_FILE), SCOPES)
            creds = flow.run_local_server(port=8089)
            TOKEN_FILE.write_text(creds.to_json())

    return creds


# ── Gmail ───────────────────────────────────────────────────

def gmail_search(query: str, max_results: int = 10) -> list[dict]:
    """Search Gmail messages. Returns list of {id, subject, from, date, snippet}."""
    creds = get_credentials()
    service = build("gmail", "v1", credentials=creds)
    results = service.users().messages().list(
        userId="me", q=query, maxResults=max_results
    ).execute()

    messages = []
    for msg_meta in results.get("messages", []):
        msg = service.users().messages().get(
            userId="me", id=msg_meta["id"], format="metadata",
            metadataHeaders=["Subject", "From", "Date"]
        ).execute()
        headers = {h["name"]: h["value"] for h in msg["payload"]["headers"]}
        messages.append({
            "id": msg["id"],
            "subject": headers.get("Subject", "(no subject)"),
            "from": headers.get("From", ""),
            "date": headers.get("Date", ""),
            "snippet": msg.get("snippet", ""),
        })
    return messages


def gmail_read(message_id: str) -> dict:
    """Read a specific Gmail message. Returns {subject, from, date, body}."""
    creds = get_credentials()
    service = build("gmail", "v1", credentials=creds)
    msg = service.users().messages().get(
        userId="me", id=message_id, format="full"
    ).execute()

    headers = {h["name"]: h["value"] for h in msg["payload"]["headers"]}

    # Extract body text
    body = ""
    payload = msg["payload"]
    if "body" in payload and payload["body"].get("data"):
        import base64
        body = base64.urlsafe_b64decode(payload["body"]["data"]).decode("utf-8", errors="replace")
    elif "parts" in payload:
        for part in payload["parts"]:
            if part["mimeType"] == "text/plain" and part["body"].get("data"):
                import base64
                body = base64.urlsafe_b64decode(part["body"]["data"]).decode("utf-8", errors="replace")
                break

    return {
        "subject": headers.get("Subject", ""),
        "from": headers.get("From", ""),
        "date": headers.get("Date", ""),
        "body": body[:4000],
    }


def gmail_send(to: str, subject: str, body: str) -> str:
    """Send an email. Returns the sent message ID."""
    import base64
    from email.mime.text import MIMEText

    creds = get_credentials()
    service = build("gmail", "v1", credentials=creds)

    message = MIMEText(body)
    message["to"] = to
    message["subject"] = subject
    raw = base64.urlsafe_b64encode(message.as_bytes()).decode()

    result = service.users().messages().send(
        userId="me", body={"raw": raw}
    ).execute()
    return f"Email sent successfully (ID: {result['id']})"


# ── Calendar ────────────────────────────────────────────────

def calendar_list_events(days_ahead: int = 7, max_results: int = 20) -> list[dict]:
    """List upcoming calendar events for the next N days."""
    creds = get_credentials()
    service = build("calendar", "v3", credentials=creds)

    now = datetime.utcnow()
    time_min = now.isoformat() + "Z"
    time_max = (now + timedelta(days=days_ahead)).isoformat() + "Z"

    results = service.events().list(
        calendarId="primary",
        timeMin=time_min,
        timeMax=time_max,
        maxResults=max_results,
        singleEvents=True,
        orderBy="startTime",
    ).execute()

    events = []
    for event in results.get("items", []):
        start = event["start"].get("dateTime", event["start"].get("date"))
        end = event["end"].get("dateTime", event["end"].get("date"))
        events.append({
            "id": event["id"],
            "summary": event.get("summary", "(no title)"),
            "start": start,
            "end": end,
            "location": event.get("location", ""),
            "attendees": [a.get("email", "") for a in event.get("attendees", [])],
        })
    return events


def calendar_create_event(
    summary: str,
    start: str,
    end: str,
    description: str = "",
    attendees: list[str] | None = None,
) -> str:
    """Create a calendar event. start/end should be ISO datetime strings."""
    creds = get_credentials()
    service = build("calendar", "v3", credentials=creds)

    event_body: dict = {
        "summary": summary,
        "description": description,
        "start": {"dateTime": start, "timeZone": "Asia/Jerusalem"},
        "end": {"dateTime": end, "timeZone": "Asia/Jerusalem"},
    }
    if attendees:
        event_body["attendees"] = [{"email": e} for e in attendees]

    event = service.events().insert(calendarId="primary", body=event_body).execute()
    return f"Event created: {event.get('htmlLink')}"


# ── Drive ───────────────────────────────────────────────────

def drive_search(query: str, max_results: int = 10) -> list[dict]:
    """Search Google Drive files. Returns list of {id, name, mimeType, webViewLink}."""
    creds = get_credentials()
    service = build("drive", "v3", credentials=creds)

    results = service.files().list(
        q=f"fullText contains '{query}'",
        pageSize=max_results,
        fields="files(id, name, mimeType, webViewLink, modifiedTime)",
    ).execute()

    return [
        {
            "id": f["id"],
            "name": f["name"],
            "type": f["mimeType"],
            "link": f.get("webViewLink", ""),
            "modified": f.get("modifiedTime", ""),
        }
        for f in results.get("files", [])
    ]


def drive_read(file_id: str) -> str:
    """Read the content of a Google Drive document (text export)."""
    creds = get_credentials()
    service = build("drive", "v3", credentials=creds)

    # Get file metadata
    meta = service.files().get(fileId=file_id, fields="name,mimeType").execute()
    mime = meta["mimeType"]

    # Export Google Docs/Sheets/Slides as plain text
    if "google-apps" in mime:
        export_mime = "text/plain"
        if "spreadsheet" in mime:
            export_mime = "text/csv"
        content = service.files().export(fileId=file_id, mimeType=export_mime).execute()
        if isinstance(content, bytes):
            return content.decode("utf-8", errors="replace")[:4000]
        return str(content)[:4000]
    else:
        # Binary file — just return metadata
        return json.dumps(meta, indent=2)
