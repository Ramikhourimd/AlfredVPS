---
alfred_tags:
- alfred/web-search
- duckduckgo/integration
based_on:
- '[[decision/Add Native Web Search via DuckDuckGo Package]]'
challenged_by: []
confidence: medium
created: '2026-03-31'
name: Web Search Package Installation Does Not Persist Across Alfred Deployments
project:
- '[[project/Alfred Development]]'
related:
- '[[assumption/Free DuckDuckGo Search API Is Adequate for Alfred Web Queries]]'
relationships:
- confidence: 0.85
  context: Persistence issue informs package decision
  source: assumption/Web Search Package Installation Does Not Persist Across Alfred
    Deployments.md
  target: decision/Add Native Web Search via DuckDuckGo Package.md
  type: supports
source: 'Conversation evidence: ddgs unavailable on 2026-03-31 despite prior installation
  decision'
source_date: '2026-03-31'
status: active
tags:
- web-search
- deployment
- persistence
type: assumption
---

# Web Search Package Installation Does Not Persist Across Alfred Deployments

## Claim

The DuckDuckGo search package (`ddgs`) does not persist across Alfred session restarts or redeployments. Despite a prior decision to add native web search (2026-03-03), the package was found missing again on 2026-03-31, requiring runtime reinstallation.

## Basis

On 2026-03-31, a user asked Alfred for a global news summary. Alfred reported: "Web search is currently unavailable — the ddgs (DuckDuckGo Search) package isn't installed." After reinstallation during the session, it worked. This occurred weeks after the original decision to add the package, suggesting the installation was ephemeral (pip install in a transient environment) rather than baked into the deployment.

## Evidence Trail

- 2026-03-03: Decision made to add DuckDuckGo search (decision record exists)
- 2026-03-31: Package found missing, reinstalled at runtime — evidence that installation did not persist

## Impact

- Web search is unreliable as a capability — it depends on whether the package survived the latest deployment
- Users encounter failures when they expect web search to work, requiring a fix-then-retry cycle
- The deployment pipeline or requirements.txt/pyproject.toml may not include `duckduckgo_search` as a dependency