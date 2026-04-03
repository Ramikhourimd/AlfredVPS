---
name: project-wrap-up
description: Generate 3 professional deliverables for any completed webdev project — (1) user guide with screenshots, (2) product specification for R&D, (3) introduction email to stakeholders. Use when asked to "wrap up the project", "create documentation", "write a user guide", "product spec", "send project to team", "present the dashboard", or any request to package a finished web application for handoff. Triggers on wrap up, document the project, create deliverables, project handoff, write guide.
---

# Project Wrap-Up

Generate three deliverables for a completed web application: a **User Guide** with screenshots, a **Product Specification** for R&D, and an **Introduction Email** to stakeholders.

## Prerequisites

Ensure Playwright is installed before running the screenshot script:

```bash
sudo pip3 install playwright && playwright install chromium
```

## Workflow

The wrap-up process has 5 steps:

1. Gather project data (read code, schema, routes, todo)
2. Capture screenshots of every page
3. Write the User Guide
4. Write the Product Specification
5. Draft the Introduction Email

## Step 1: Gather Project Data

Read `references/data-gathering.md` for the full checklist. At minimum, collect:

| Source | What to Extract |
|--------|----------------|
| `todo.md` | Feature list, completed items, remaining items |
| `drizzle/schema.ts` | All tables, columns, types, enums, relations |
| `server/routers.ts` | All tRPC procedures (name, type, auth level) |
| `client/src/App.tsx` | All routes and their page components |
| Sidebar/nav component | Navigation structure and section grouping |
| `package.json` | Tech stack (dependencies and versions) |
| `git remote -v` | GitHub repository URL |
| `pnpm test` output | Test count and file coverage |
| `webdev_check_status` | Dev server URL, published domain |

Also collect from the user request:
- **Email recipients** — names and (if known) roles
- **Author name** — who signs the documents
- **Organization name** — for headers and context

## Step 2: Capture Screenshots

Build a pages JSON array from the routes discovered in Step 1. Each entry needs `name` (filename), `path` (route), and `label` (human name).

Run the capture script:

```bash
python /home/ubuntu/skills/project-wrap-up/scripts/capture_screenshots.py \
  "<DEV_SERVER_URL>" \
  "/home/ubuntu/deliverables/screenshots" \
  '<PAGES_JSON>'
```

Example pages JSON:

```json
[
  {"name": "01-dashboard", "path": "/", "label": "Dashboard"},
  {"name": "02-settings", "path": "/settings", "label": "Settings"}
]
```

After capture, upload all screenshots for CDN URLs:

```bash
cd /home/ubuntu/deliverables/screenshots && manus-upload-file *.png
```

Save the CDN URL mapping for use in the documents.

## Step 3: Write the User Guide

Read the template at `templates/user-guide-template.md` for structure. The guide must include:

1. **Introduction** — what the app does, who it's for, scale (e.g., "manages 40 protocols across 6 domains")
2. **Getting Started** — access URL, auth method, navigation structure table
3. **One section per page** — each with:
   - Embedded screenshot (CDN URL from Step 2)
   - Description of every visible feature
   - Sub-sections for distinct UI areas (e.g., "KPI Bar", "Filter Controls", "Activity Feed")
   - Tables for structured information (column descriptions, KPI definitions, button functions)
4. **Key Workflows** — numbered step-by-step walkthroughs of the 2-3 most important user journeys
5. **Glossary** — domain-specific terms in a table

**Writing style:** Professional but accessible. Full paragraphs, not bullet lists. Use tables to organize structured data. Embed every screenshot with descriptive alt text.

Save to `/home/ubuntu/deliverables/{{Project_Name}}_User_Guide.md`.

## Step 4: Write the Product Specification

Read the template at `templates/product-spec-template.md` for structure. The spec must include:

1. **Executive Summary** — what the system is, what it replaces, key capabilities
2. **Architecture Overview** — tech stack table (from package.json), ASCII system diagram, annotated directory structure
3. **Database Schema** — entity-relationship summary table, then detailed column tables for each table from `drizzle/schema.ts`
4. **API Specification** — router hierarchy tree (namespace → procedure → type/auth), auth model table
5. **AI/External Integrations** — for each integration: what it does, how it connects, data flow
6. **Frontend Architecture** — page inventory table (route, auth, description), design system tokens
7. **Testing** — test file table with counts and coverage areas
8. **Environment Variables** — table of all env vars with source and purpose
9. **Deployment** — domain, build command, database, GitHub repo
10. **Security** — auth model, API key handling, input validation
11. **Known Limitations** — table of current state vs. future considerations

**Writing style:** Technical and precise. Use tables extensively. Include code blocks for schemas, API trees, and directory structures. No marketing language.

Save to `/home/ubuntu/deliverables/{{Project_Name}}_Product_Specification.md`.

## Step 5: Draft the Introduction Email

Read the template at `templates/email-template.md` for structure.

### Voice & Persona

The email is written by **Alfred**, Rami's AI Personal Assistant, on behalf of Rami. Alfred writes in first person ("Rami and I..."), uses an excited but professional and respectful tone, and signs off as "Alfred (on behalf of Rami)". Do not include a "Next Steps" or task-assignment section — the email is purely a presentation of what was built.

### Default Recipients

Always include these two recipients:
- **Oren Taliaz** — oren@taliazhealth.com
- **Dekel Taliaz** — dekel@taliazhealth.com

Add any additional recipients specified in the user request. Search Gmail to find their email addresses if not provided.

### Email Content

1. **Header** — From: Alfred (on behalf of Rami). Subject: "Something Rami and I Built — {{Project Name}}"
2. **Opening** — Alfred introduces himself, mentions he's writing on Rami's behalf, expresses pride in what they built together
3. **The Problem** — what pain point the product addresses (2-3 sentences)
4. **What We Built** — brief description of the application and its key capabilities
5. **Key Features** — organized by audience ("For everyone" + role-specific sections). Describe each feature in a short paragraph, not bullet points
6. **Personalized paragraphs** — one for each named recipient explaining what the product means for them specifically, based on their role
7. **Closing** — mention the attached User Guide and Product Spec. Do NOT include task assignments or next steps

**Writing style:** Excited, professional, respectful. Alfred's voice — helpful, proud, warm. Short paragraphs. No jargon.

Save to `/home/ubuntu/deliverables/Email_to_Team.md`.

### Create Gmail Draft with Attachments

After writing the email, convert the User Guide and Product Spec to PDF:

```bash
manus-md-to-pdf /home/ubuntu/deliverables/{{Project_Name}}_User_Guide.md /home/ubuntu/deliverables/{{Project_Name}}_User_Guide.pdf
manus-md-to-pdf /home/ubuntu/deliverables/{{Project_Name}}_Product_Specification.md /home/ubuntu/deliverables/{{Project_Name}}_Product_Specification.pdf
```

Then create a Gmail draft using the `gmail_send_messages` MCP tool. The tool triggers an interactive confirmation — the user chooses "Save to drafts" or "Send". Include both PDFs as attachments:

```bash
manus-mcp-cli tool call gmail_send_messages --server gmail --input '{
  "messages": [{
    "to": ["oren@taliazhealth.com", "dekel@taliazhealth.com", ...additional recipients...],
    "subject": "Something Rami and I Built — {{Project Name}}",
    "content": "<plain text email body — no markdown, no HTML>",
    "attachments": [
      "/home/ubuntu/deliverables/{{Project_Name}}_User_Guide.pdf",
      "/home/ubuntu/deliverables/{{Project_Name}}_Product_Specification.pdf"
    ]
  }]
}'
```

The email content must be plain text (no markdown formatting). Convert bold/headers to plain text equivalents.

## Delivery

Send all three documents to the user as attachments in this order:
1. Email (most immediately actionable)
2. User Guide (most broadly useful)
3. Product Specification (deepest reference)

Confirm that the Gmail draft was created with both PDF attachments. Suggest the user review the draft in Gmail before sending.
