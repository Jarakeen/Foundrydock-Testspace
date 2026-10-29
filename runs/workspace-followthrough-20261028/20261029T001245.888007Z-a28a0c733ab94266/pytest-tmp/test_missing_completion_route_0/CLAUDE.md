# Wyrdworks — Shared AI working rules

**Active development branch:** `wyrdworks-dev` supersedes the `phase15.5` branch for ongoing development as of 2026-10-18. Phase 15.5 remains the product/architecture milestone identifier. The approved Granite/fantasy blend is the default style; preserve its shared palette, assets and active workflow updates. The old branch remains available as history.

Read [AGENTS.md](AGENTS.md) first. These rules apply to every assistant, not only Claude. Architecture belongs in [SYSTEM_ARCHITECTURE_RULES.md](SYSTEM_ARCHITECTURE_RULES.md); mandatory validation and completion gates belong in [DEVELOPMENT_STANDARD.md](DEVELOPMENT_STANDARD.md). Link those owners rather than copying their rules here.

## Work on the current product

- Product: **Wyrdworks** (formerly FoundryDock). Repository: `Jarakeen/Wyrdworks`; current product line: **phase15.5**. Windows root: `C:\Dev\BFF\FoundryDock`. Preserve repository, module, database, configuration, and persisted identifiers unless separately authorized.
- Raid Plan is the only active raid-planning UI, with Teams, Map, and Readiness columns; Roster, Assignments, Builds, Map Workshop, and Finch / Collaboration remain supporting capabilities where required by Raid Plan. Lantern, Comp Brainstorm, Coverage, Rotations, standalone Readiness, Health, Comp Engine, Optimization, Extreme Build, and Live Raid interfaces are parked. Parked means their code, data, integrations, shared-service access, and regression tests are retained; it does not authorize page redesign or page-specific acceptance for unrelated work.
- Inspect current head, working changes, applicable instructions, canonical owner and tests before editing. Preserve newer and concurrent work.
- Old roadmap work is additive reconciliation. Never revive retired services, shells, persistence paths or routing to satisfy a stale requirement or test.
- Do not switch branches, create throwaway branches, force-push or broadly reset/revert the checkout as a shortcut. Use focused commits. Confirm current remote head before publishing; merge or port narrowly if it changed.
- Continue authorized work without repeated permission questions. Ask only when a necessary decision or genuinely destructive action lacks authorization.
- Run validation locally by default and verify an exact-commit quality receipt before merging; see DEVELOPMENT_STANDARD.md for the existing runner and gates. Hosted test runs require an explicit request.

## Finish the requested behavior

Start each increment with the user's observable outcome and its acceptance evidence. Implement a small complete path through existing owners; do not stop at a contract, stub, note, background API or screenshot when the request is for working behavior.

Routine audits are part of the work, not tasks the user must remember to request. Apply the development standard automatically. A blocked dependency does not justify claiming completion; report the exact missing evidence and complete independent work.

Prefer closing a real data/relationship/consumer gap in an active workflow to polishing already-sufficient infrastructure. Do not create another engine or tracker because knowledge is inconvenient to discover. Inspect canonical shared mechanics and intelligence owners before adding mechanics; parked pages are not a reason to duplicate or revive an owner.

## Parked UI does not mean parked intelligence

A parked Wyrdworks page is a presentation and navigation decision only. Parking an interface must not disable, discard, duplicate, bypass, or prevent access to its underlying canonical services, validated mechanics, persisted data, research, or intelligence.

Active workflows must reuse relevant authoritative capabilities from Extreme, Combat, Encounter, Rotation, Coverage, Readiness, Health, Comp, Optimization, and other existing systems whenever applicable. Before developing new intelligence, inspect the service catalog, canonical owners, integration inventory, and previously validated capabilities.

Prefer surfacing existing intelligence in active pages over reopening parked interfaces or creating replacement engines. Encounter-aware Raid Plan reviews should combine relevant validated capabilities into explainable, stage-aware findings without inventing unsupported conclusions.

Preserve exact plan, encounter, stage, player, seat, and build identities. Distinguish planned capability, simulated results, observed execution, and unknown evidence. Never promote incomplete research or historical test results into verified mechanics.

Perform expensive evaluations on demand and off the UI thread. Invalidate or reject stale results when their plan, stage, builds, assignments, or source evidence changes.

The goal is to make Wyrdworks smarter through integration, not to accumulate isolated features.

## Shared Foundry intelligence rule

Extreme, Combat, Encounter, Rotation, Coverage and Readiness must consume reviewed facts through their canonical owners. Reuse the existing `services/foundry_intelligence_service.py` for shared intelligence instead of inventing another engine or silently promoting raw research into verified mechanics. Preserve evidence provenance, uncertainty and stage/plan identity. Integration requires a consumer-level regression test before claiming a rule influences a decision.

## Permanent UI / performance / RAVEN-FORGE rule

Before modifying startup, pages, catalog lookups, theme, tooltips, scrolling or images, follow **SYSTEM_ARCHITECTURE_RULES.md → Phase 15.5 performance, interaction and asset invariants**. Do not let a later integration restore eager page construction, full-catalog loading, repeated unchanged-context refresh, ubiquitous hover help, nested primary scrollbars or multiple selectable themes. Do not treat SVG icons or efficient transparent PNG sprites as mandatory WebP conversions; WebP is preferred for banners, boss art, maps and large illustrations. Extend the existing page/asset owners and regression tests rather than creating parallel infrastructure. Any deliberate exception requires evidence and an explicit architecture note. Verify cold startup, first and repeat use, and saved-state integrity before claiming an optimization.

## Protect the work

Never reset/replace/recreate/seed over `data/eso.db` or `user_data/foundrydock.db`. Tests and migration rehearsal use disposable databases. Additive compatible upgrades are permitted through canonical owners. Preserve raw provenance, richer records, saved identities and dirty drafts.

Deep inference belongs on explicit background actions, with context-aware invalidation and stale-result rejection. Keep navigation and saves responsive and the outer workspace at the user's chosen dimensions. Follow Urban Wilderness assets, text/symbol status cues and seizure-safe behavior.

## Leave useful records

| Trigger | Update in the same increment |
| --- | --- |
| A new/materially changed visible capability | FEATURES.md |
| A surprising or easy-to-misread game mechanic | GAME_MECHANICS_FIELD_NOTES.md, in plain language |
| A useful research URL | useful_resources.md, including use, confidence and limits |
| A numeric alias or event tag | ESO_ID_REFERENCE.md or ESO_LOGS_RAW_TAG_REFERENCE.md according to ownership |
| Knowledge wired to a decision | INTELLIGENCE_INTEGRATION.md, with canonical destination and consumer test |
| New architectural responsibility | service catalog and architecture/integrity tests |
| New AI working requirement | This file; route detail through AGENTS.md |

Do not pad field notes with ordinary refactoring or turn internal plumbing into a new product feature. Preserve contradictory observations; do not dedupe away their context.

## Report honestly

Use plain language. State changed behavior, actual test results, material limits and whether work is local, committed, published or installed. Never equate a commit with Windows deployment or historical green tests with a new validation. Give copy/paste commands only when they are the intended commands to run. Do not generate patch downloads when the user asked for development inside the test environment.

Search current owners first: relevant `services/`, `models/`, `minmax/`, `engine/`, UI and tests. Search archival branches, raw logs and backups only when the task or a live dependency warrants it.

## Project organization and recoverable session completion

Use [the ownership map](docs/PROJECT_OWNERSHIP.md) and [workspace guide](docs/workspace.md) before adding folders or moving files. Keep one repository with its existing domain owners. A VS Code folder is enough; extra workspaces do not establish Python package or persistence boundaries.

Before editing, inspect repository root, branch, HEAD, worktrees, status and upstream; fetch and check incoming commits. Record pre-existing changes and leave them with their owner. For substantial concurrent work, use a clearly named isolated worktree/branch from the verified development head; never switch the dirty primary checkout. Do not duplicate user databases into a new checkout as an organization shortcut. The main checkout is not a staging area for another session's files.

At every session end, run relevant checks, inspect status and account for every modified/untracked file. Commit only this session's validated work in focused increments. Push its corresponding branch when authorized and safe, refresh remote refs and verify synchronization. Follow DEVELOPMENT_STANDARD.md for exact-commit quality receipts and hook gates. Preserve incomplete work as a clearly named WIP checkpoint; never silently discard it. Exclude generated scratch through existing ignored output owners without deleting valuable files. Report branch, commit, push/synchronization state, exact tests/blockers and remaining changes, distinguishing the isolated checkout from pre-existing primary work. Do not claim completion when validation or synchronization failed.

## Built-in boss map package authoring

Extend the registered manifests consumed by services/workshop_map_package_service.py and the existing EncounterRaidMapStore/EncounterBoard paths. Built-ins are immutable application assets without player/plan identities; custom edits stay with Workshop or exact plan/stage saves. Never infer a fixed spawn or confirmed player intent from a teaching route. Preserve raid-lead strategy, observed event evidence, provisional calibration and unknowns separately. For Lokke, preserve the three different flight sequences and unrestricted cage roles recorded in GAME_MECHANICS_FIELD_NOTES.md.

Default Raid Plan boss-package navigation is automatic and read-only. Encounter phase to tactical phase bindings are authored in package manifests, not configured by raid leads through normal UI. Keep manifest-declared flight headings (80/50/20 percent for Lokke) and five compact controls (Arena, Strategy, Play/Pause, Names, Edit). Thresholds, timeline events, named phase routes, teaching focus and playback share one cursor. Route selection must not construct the editor. Keep one grouped strategy route per main phase; DD cage departures are separate duties, not a per-player route menu. Reference actors remain separate from roster identities. Authoring stays in Workshop, with verified recoverable autosave before navigation; library publication remains explicit. Do not restore an editing toolbar or file writes on phase/layer clicks.

Routine testing pushes use focused pre-push checks by default at the user's request. Keep user data isolated. Run meaningful task-specific regressions before committing. Use FOUNDRYDOCK_PUSH_CHECKS=full and the existing exact-commit receipt for integration/release validation; do not automatically repeat broad suites on every small push. See DEVELOPMENT_STANDARD.md.

Keep Raid Plan Health Timeline's reviewed health rail and mechanic/attack cards when a boss package is active. Percentage selections link to package phase/replay anchors; untimed mechanic selections must not invent replay times. Health rails read 100% left to 0% right. Do not replace this panel with recorded cast-event tiles.

Boss package consumers must read heading thresholds and phase ordering from each manifest; do not apply Lokke's phase indices, cages, houses or Barrier wording to another encounter. A provisional observed-coordinate schematic is not validated arena artwork or lower-floor geometry. Keep recorded group summaries distinct from confirmed strategy and retain unassigned portal duties when participants are unknown.

Reference actor duties belong to one report/fight timeline, never directly to current roster seats or another pull with the same actor numbers. For Nahvi reference fight 44, portal DDs 154/156/8 are raid-lead confirmed; upstairs group summaries exclude them without asserting their exact floor at every timestamp. Keep artwork, replay and route orientation consistent. Approximate dragon-body guides must not become hitbox/safe-zone verdicts.

Map labels must remain readable over pale or busy artwork: use dark opaque backings and adequate bold text for instructions and reference actor labels. Version changed package background filenames and retain previous assets so saved layouts do not silently inherit a different coordinate system.

## Agent workspace cleanup

These requirements apply to Claude, Codex, Copilot, and other coding assistants: track your own temporary worktrees and pytest artifacts, verify safe disposal at task completion, and report **Workspace Cleanup: CLEAN / RETAINED WITH REASON / BLOCKED**. Do not alter another agent's workspace or discard unverified data. The authoritative cleanup and squash-merge checks live in [DEVELOPMENT_STANDARD.md](DEVELOPMENT_STANDARD.md).
