# Wyrdworks — Start here

**Active development branch:** `wyrdworks-dev` supersedes the `phase15.5` branch for ongoing development as of 2026-10-18. Phase 15.5 remains the product/architecture milestone identifier. The approved Granite/fantasy blend is the default style; preserve its shared palette, assets and active workflow updates. The old branch remains available as history.

This is the entry point for every assistant, contributor and review. **Wyrdworks** is the current product name; FoundryDock remains the repository and selected technical identifier. Paths are relative to the actual repository root; the usual Windows location is `C:\Dev\BFF\FoundryDock`.

## Required reading

1. Read [CLAUDE.md](CLAUDE.md), regardless of assistant name.
2. Read [SYSTEM_ARCHITECTURE_RULES.md](SYSTEM_ARCHITECTURE_RULES.md).
3. Read [DEVELOPMENT_STANDARD.md](DEVELOPMENT_STANDARD.md) before implementation and use its completion gates before reporting done.
4. Read the active slice of [MASTER_ROADMAP.md](MASTER_ROADMAP.md), `services/service_catalog.py`, applicable directory instructions, current code and relevant tests.

Inspect branch, head and working changes first. The designated product line is **phase15.5**. Raid Plan is the only active raid-planning UI, with Teams, Map, and Readiness columns; Roster, Assignments, Builds, Map Workshop, and Finch / Collaboration remain supporting capabilities where required by Raid Plan. Lantern, Comp Brainstorm, Coverage, Rotations, standalone Readiness, Health, Comp Engine, Optimization, Extreme Build, and Live Raid interfaces are parked; their code, records, shared data, and regression coverage remain protected. See the roadmap for current scope. Historical uploads and old handoffs do not replace newer working code. Re-read affected files before writing when other workstreams are active. Never overwrite a newer version from memory.

## One home for each topic

| Need | Authoritative document / owner |
| --- | --- |
| AI work, scope, concurrency and reporting | [CLAUDE.md](CLAUDE.md) |
| Startup/lazy pages, scoped data, refresh, tooltip/scroll/theme rules, RAVEN-FORGE image formats | [SYSTEM_ARCHITECTURE_RULES.md](SYSTEM_ARCHITECTURE_RULES.md) → Phase 15.5 performance, interaction and asset invariants; test gates in [DEVELOPMENT_STANDARD.md](DEVELOPMENT_STANDARD.md) |
| Service/page ownership, identity and shared mechanics | [SYSTEM_ARCHITECTURE_RULES.md](SYSTEM_ARCHITECTURE_RULES.md), `services/service_catalog.py` |
| Strict validation, durable saves, tests and completion | [DEVELOPMENT_STANDARD.md](DEVELOPMENT_STANDARD.md) |
| What to deliver next | [MASTER_ROADMAP.md](MASTER_ROADMAP.md) |
| What the app offers | [FEATURES.md](FEATURES.md), verified against current code |
| Surprising game behavior | [GAME_MECHANICS_FIELD_NOTES.md](GAME_MECHANICS_FIELD_NOTES.md) |
| Sources, URLs and suitability | [useful_resources.md](useful_resources.md) |
| Semantic identity and numeric aliases | [ESO_ID_REFERENCE.md](ESO_ID_REFERENCE.md) |
| Raw event tags, correlation and clipping | [ESO_LOGS_RAW_TAG_REFERENCE.md](ESO_LOGS_RAW_TAG_REFERENCE.md) |
| Raid conventions and exceptions | [ENDGAME_PLAY_PRACTICES.md](ENDGAME_PLAY_PRACTICES.md), `data/gameplay_policy/` |
| Sparse build inheritance | [BUILD_CONTEXT_VARIANT_BEHAVIOR.md](BUILD_CONTEXT_VARIANT_BEHAVIOR.md) |
| Knowledge reaching actual app decisions | [INTELLIGENCE_INTEGRATION.md](INTELLIGENCE_INTEGRATION.md) |
| Extraction and retirement evidence | [PHASE155_EXTRACTION.md](PHASE155_EXTRACTION.md), [PHASE155_DEPENDENCY_CENSUS.md](PHASE155_DEPENDENCY_CENSUS.md) |
| Historical workstream and validation reports | [PHASE13_5_CONCURRENT_WORK.md](PHASE13_5_CONCURRENT_WORK.md), [Milestone 2 report](PHASE155_INTELLIGENCE_MILESTONE2_VALIDATION.md) |

Follow governing tool instructions and the user's explicit current direction first. Specific project rules refine shared rules; they do not silently bypass data or evidence safeguards. If a real conflict remains, name it and request only the missing decision while continuing independent work.

For focused agent/developer pytest runs, use the shared TestSpace launcher and its required `--` separator as documented in [DEVELOPMENT_STANDARD.md](DEVELOPMENT_STANDARD.md#testspace-focused-pytest-runs-phase-1-pilot). Do not run focused pytest selections directly into repository-local `.pytest-*` paths.

Do not read every historical report for every edit. Follow this routing table and task-relevant evidence. Missing documents or owners are explicit gaps, not permission to invent them.

## Temporary workspace lifecycle

Every agent must own the lifecycle of worktrees, task-scoped pytest directories, and generated artifacts it creates: **create → validate → integrate → verify preservation → clean up or report retention**. Follow the mandatory safety/completion checks in [DEVELOPMENT_STANDARD.md](DEVELOPMENT_STANDARD.md). Do not force-remove worktrees, discard dirty or unique work, or delete databases, logs, recovery evidence, or another agent's files merely to tidy the checkout. For squash merges, prove content is preserved; commit ancestry alone is not the test.
