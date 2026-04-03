---
authority: Google OAuth2 token lifecycle
created: '2026-03-30'
janitor_note: 'LINK001 — Base view embeds (learn-constraint.base#Affected Projects,
  #Related) reference _bases/learn-constraint.base which does not exist — vault-wide
  infrastructure gap, embeds preserved.'
name: Alfred Gmail and Calendar OAuth Token Invalid Preventing Data Retrieval
project:
- '[[project/Alfred Development]]'
related:
- '[[conversation/Alfred Chat — Untitled Chat 2026-03-30]]'
source: Gmail/Google Calendar OAuth2 integration
source_date: '2026-03-30'
status: active
type: constraint
---

# Alfred Gmail and Calendar OAuth Token Invalid Preventing Data Retrieval

## Constraint

Alfred's Gmail and Google Calendar integrations return an "invalid grant" authentication error, blocking all email and calendar data retrieval. This prevents Alfred from generating complete activity summaries that include email threads and calendar events.

## Source

Google OAuth2 token expiry or revocation. The error surfaced during a weekly activity summary request on 2026-03-30. The specific error is an "invalid grant" response from the Google API, indicating the stored refresh token is no longer valid.

## Implications

- Alfred cannot pull Gmail messages or Google Calendar events until the OAuth token is re-authenticated
- Activity summaries fall back to vault-only data, which may miss unprocessed emails and calendar events
- Any workflow that depends on live Gmail/Calendar data (e.g., work-periodic-summary, personal-crm) is degraded
- The user may not be aware of the gap in data coverage unless explicitly told

## Expiry / Review

This constraint expires once the OAuth tokens are re-authenticated. Should be resolved as soon as possible to restore full Alfred functionality.

![[learn-constraint.base#Affected Projects]]
![[learn-constraint.base#Related]]
