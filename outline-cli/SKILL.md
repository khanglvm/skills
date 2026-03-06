---
name: outline-cli
description: Use the local Outline CLI (`outline-cli`, legacy alias `outline-agent`) for deterministic, token-efficient Outline workflows. Trigger when tasks involve profile setup, tool contract discovery, searching/listing/reading docs or collections, safe mutations (revision guards + `performAction`), delete read-token flow, templates/comments/shares/revisions lifecycle, graph or issue-link analysis, federated sync/ACL snapshots, or workspace admin wrappers.
---

# Goal
Execute Outline operations with low-token calls, explicit safety gates, and reproducible machine-readable output.

# Instructions

## Command Surface
- Use `outline-cli` by default.
- Accept `outline-agent` only when the user explicitly asks for that alias.
- Prefer `invoke` + structured JSON args, then `batch` for multi-step operations.

## Session Bootstrap (Always)
1. Verify binary and help surfaces:
   ```bash
   outline-cli --version
   outline-cli tools help --view summary
   ```
2. Refresh source-of-truth contracts:
   ```bash
   outline-cli tools contract all --result-mode inline
   ```
3. Verify profile/auth before any mutation:
   ```bash
   outline-cli profile list --pretty
   outline-cli profile test
   outline-cli invoke auth.info --args '{"view":"summary"}'
   ```

## Capability Map (Use Minimal Tooling)
- Retrieval and navigation:
  - `documents.search`, `documents.list`, `documents.info`, `documents.resolve`, `documents.resolve_urls`, `documents.canonicalize_candidates`
  - `collections.list`, `collections.info`, `collections.tree`
  - `search.expand`, `search.research`
- Safe document mutation:
  - `documents.update`, `documents.safe_update`, `documents.diff`, `documents.apply_patch`, `documents.apply_patch_safe`, `documents.batch_update`
  - `documents.plan_batch_update`, `documents.plan_terminology_refactor`, `documents.apply_batch_plan`
- Lifecycle and collaboration:
  - `revisions.*`, `shares.*`, `templates.*`, `documents.templatize`, `comments.*`, `events.list`
- Knowledge and linkage workflows:
  - `documents.answer`, `documents.answer_batch`
  - `documents.backlinks`, `documents.graph_neighbors`, `documents.graph_report`
  - `documents.issue_refs`, `documents.issue_ref_report`
- Integration/admin wrappers:
  - `federated.sync_manifest`, `federated.sync_probe`, `federated.permission_snapshot`, `capabilities.map`
  - `users.*`, `groups.*`, `collections.*_memberships`, `documents.*_memberships`, `documents.users`
  - `oauth_clients.*`, `oauth_authentications.*`, `oauthClients.delete`, `oauthAuthentications.delete`
  - `webhooks.*`, `file_operations.*`, `documents.import_file`, `documents.create_from_template`, `documents.cleanup_test`
- Escape hatch:
  - `api.call` for endpoints not yet wrapped as dedicated tools.

## Retrieval-First Pattern (Default)
1. Discover candidates with `view:"ids"` or `view:"summary"`.
2. Hydrate only selected IDs (`documents.info` / `collections.info`).
3. Escalate to `view:"full"` only for final documents that require full text.
4. Prefer multi-query/multi-id args (`queries[]`, `ids[]`) over repetitive single calls.

## Mutation Pattern (Safe + Explicit)
1. Read current state first.
2. Use minimal edits (`append`/`prepend`, patch, or targeted update).
3. Use revision guards (`expectedRevision`) for concurrent environments.
4. Set `performAction:true` only on the final confirmed mutation call.
5. Verify via read-back and, for high-impact flows, `events.list`/`revisions.list`.

## Delete Pattern (Mandatory)
1. Arm delete read:
   ```bash
   outline-cli invoke documents.info --args '{"id":"<doc-id>","armDelete":true,"view":"summary"}'
   ```
2. Extract `deleteReadReceipt.token`.
3. Execute delete:
   ```bash
   outline-cli invoke documents.delete --args '{"id":"<doc-id>","readToken":"<token>","performAction":true}'
   ```
4. If token is stale/mismatched/expired, re-run step 1 immediately and retry once.

## Output and Token Controls
- Formats:
  - `--output json` (default)
  - `--output ndjson` for stream-friendly automation
- Result modes:
  - `--result-mode auto` (default offload when payload is large)
  - `--result-mode inline`
  - `--result-mode file`
- Use `--args-file` / `--ops-file` for large payloads.
- If output is offloaded, inspect only required fields:
  ```bash
  outline-cli tmp cat /absolute/path/from/result.json
  ```
- Periodic cleanup:
  ```bash
  outline-cli tmp gc --older-than-hours 24
  ```

## Built-in Agent Guidance
- Beginner onboarding playbook:
  ```bash
  outline-cli tools help quick-start-agent --view full
  ```
- Scenario playbooks (14 workflows):
  ```bash
  outline-cli tools help ai-skills --view full
  ```

# Constraints
- Never run mutating operations without explicit `performAction:true`.
- Never delete without a fresh read token from `documents.info armDelete:true`.
- Never default to `view:"full"` for discovery.
- Never assume profile context; verify `profile list/test` + `auth.info`.
- Never hardcode old contracts; refresh with `tools contract all` before long automation runs.

# Examples

## Example 1: Research retrieval in one call
```bash
outline-cli invoke search.research --args '{
  "question": "How do we run incident communication and escalation?",
  "queries": ["incident comms", "escalation matrix"],
  "precisionMode": "precision",
  "limitPerQuery": 8,
  "perQueryView": "ids",
  "perQueryHitLimit": 4,
  "expandLimit": 4,
  "view": "summary"
}'
```

## Example 2: Template placeholder extraction + strict instantiation
```bash
outline-cli invoke templates.extract_placeholders --args '{"id":"template-id"}'

outline-cli invoke documents.create_from_template --args '{
  "templateId": "template-id",
  "title": "Service A - Incident Postmortem",
  "placeholderValues": {"service_name":"Service A","owner":"SRE Team"},
  "strictPlaceholders": true,
  "publish": true,
  "performAction": true,
  "view": "summary"
}'
```

## Example 3: Safe patch update with revision guard
```bash
outline-cli invoke documents.info --args '{"id":"doc-a","view":"summary"}'

outline-cli invoke documents.apply_patch_safe --args '{
  "id": "doc-a",
  "expectedRevision": 12,
  "mode": "unified",
  "patch": "@@ -1,1 +1,1 @@\n-Old\n+New",
  "performAction": true,
  "view": "summary"
}'
```

## Example 4: Federated sync + ACL snapshot
```bash
outline-cli invoke federated.sync_manifest --args '{
  "collectionId": "collection-id",
  "since": "2026-03-01T00:00:00.000Z",
  "limit": 100,
  "offset": 0
}'

outline-cli invoke federated.permission_snapshot --args '{
  "ids": ["doc-1", "doc-2"],
  "includeDocumentMemberships": true,
  "includeCollectionMemberships": true
}'
```

# Read Next
Load command recipes only when needed:
- `references/tool-playbook.md`
