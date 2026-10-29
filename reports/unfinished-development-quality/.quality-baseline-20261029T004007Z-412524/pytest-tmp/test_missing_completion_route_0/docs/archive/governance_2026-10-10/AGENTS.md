# FoundryDock — Start Here

This is the shared entry point for AI assistants, contributors, code reviews, and development automation working on Black Feather Foundry / FoundryDock. Read this before planning or changing the project.

Intended location: the FoundryDock repository root, normally `C:\Dev\BFF\FoundryDock\AGENTS.md`. Paths below are relative to that root. Use the actual checkout path in other environments.

## 1. Read the current files, not remembered copies

Read these first, in this order:

1. This `AGENTS.md`.
2. `CLAUDE.md` — shared AI working rules, even when the assistant is not Claude.
3. `SYSTEM_ARCHITECTURE_RULES.md` — system-wide ownership, evidence, and integration rules.
4. The current `MASTER_ROADMAP.md` and any current roadmap explicitly designated by the user.
5. `services/service_catalog.py` — canonical service ownership and implementation paths.
6. Any directory-specific instructions that apply to the files being changed.
7. The current implementation, relevant tests, and task-specific evidence.

Inspect the branch, commit, working-tree changes, and applicable instructions before editing. The designated product line is `phase15.5` unless the user changes it. If the checkout differs, investigate before applying changes intended for that branch.

If a required document is missing, find its current equivalent. Report a genuine gap; do not invent its contents or quietly substitute an old copy. Archived roadmaps, handoffs, chat history, and uploaded snapshots are context, not automatic authority over the current checkout.

## 2. Resolve conflicts deliberately

- Follow the AI tool's governing instructions and the user's current explicit instructions.
- Within project guidance, apply the current standing rules and architecture requirements. A more specific instruction may refine them but must not silently bypass shared data or mechanics rules.
- Current `phase15.5` behavior is authoritative over older implementation plans. A roadmap change should improve it additively unless the user explicitly directs otherwise.
- Preserve newer and concurrent work. Do not restore an old implementation simply to satisfy an old roadmap or source-text test.
- If two current requirements cannot both be met, identify the exact conflict and ask only for the decision needed to resolve it. Continue independent authorized work.

## 3. Where to find each kind of truth

| Question | Read here | How to use it |
| --- | --- | --- |
| How should an AI work on this project? | `CLAUDE.md`, this file, applicable directory instructions | Follow the current working rules. |
| What should we build next? | Current Master Roadmap | Use the current product direction; preserve completed behavior. |
| Which component owns this responsibility? | `SYSTEM_ARCHITECTURE_RULES.md`, `services/service_catalog.py` | Reuse or extend the canonical owner before creating a service. |
| What does the app already do? | `FEATURES.md`, current implementation and tests | Treat the feature index as a map; verify behavior in code. |
| What surprising game behavior have we found? | `GAME_MECHANICS_FIELD_NOTES.md` | Read the practical finding and follow its evidence to the canonical implementation. |
| Which ESO sources can we trust for this purpose? | `useful_resources.md` | Check usefulness, confidence, provenance, update, and limitations. |
| What does an ESO numeric ID mean? | `ESO_ID_REFERENCE.md` | Preserve semantic identity and the ID's exact context. |
| Where are detailed effect aliases and raw log tags? | `docs/major_minor_effect_ids.md`, `ESO_LOGS_RAW_TAG_REFERENCE.md` | Use the documented source and event context; do not assume every ID is interchangeable. |
| Is this a game rule or a raid convention? | `ENDGAME_PLAY_PRACTICES.md`, `data/gameplay_policy/`, `services/gameplay_policy_service.py` | Keep mechanical legality separate from customary player choices. |
| What is true for this selected plan and stage? | Canonical effective-context and runtime services identified by the service catalog | Evaluate the authoritative snapshot, including stage changes and assignments. |
| What proves the result? | Relevant executable tests, datasets, research records, and integration inventory | Preserve provenance, assumptions, uncertainty, and scope. |

Some entries are task-dependent. Verify their current paths in the checkout rather than creating duplicate documents because a filename moved.

## 4. Standing development rules

### Protect user data

Never reset, replace, recreate, or seed over `data/eso.db` or `user_data/foundrydock.db`. Use additive, compatible upgrades that preserve existing records. Reference data and user-owned plans, characters, builds, and teams remain separate. Never replace the working user database with a test database or uploaded snapshot.

### Share intelligence through canonical services

Extreme, Combat, Encounter, Rotation, Comp, Coverage, Optimization, Readiness, and Live Raid must consume shared mechanics and structured evidence. Do not recreate engines, duplicate owned formulas, parse display prose into application state, or create feature-local competing runtime truth.

Unknown, unsupported, partial, contradictory, or outdated evidence must remain explicit. Never turn missing information into a favorable score, readiness result, or optimization assumption. Preserve identities and evidence across engine boundaries.

### Harden Python boundaries

Use Pydantic validation wherever appropriate, especially for external inputs, persisted payloads, service contracts, and engine results. Prefer explicit types and strict validation where coercion could hide incorrect data. Reuse current project models and conventions.

### Keep the app accessible and stable

Use the established Urban Wilderness design and assets. Make status understandable without red/green distinctions alone; provide text, symbols, or another visible cue. Avoid flashing, strobing, and unnecessary motion. Outer workspace dimensions must remain at the user's chosen size unless the user resizes them.

### Validate behavior

Run actual relevant pytest tests in the designated working environment. Source-text assertions alone do not prove application behavior. Test shared contracts and the affected consumer when integration changes behavior. Do not weaken meaningful tests to conceal regressions. Report what was tested, what passed or failed, and what remains unverified.

Continue authorized roadmap work without asking permission between routine increments. Do not generate patch downloads or ZIP handoffs when the user has requested in-environment development. Explain results in plain language. Only offer executable commands intended for the user to run.

## 5. Permanent Intelligence Integration Audit

During research, implementation, testing, real-build validation, and encounter analysis:

1. Inspect related existing engine intelligence, documentation, tests, and datasets.
2. Identify validated knowledge that current application decisions do not yet use.
3. Record it in the project's existing integration inventory. Locate that inventory first; do not create a competing tracker. If none exists, establish one explicitly and add its verified path to this directory.
4. Track the mechanic or finding, source and confidence, existing implementation, intended canonical destination, status, and test evidence.
5. Integrate through the existing canonical owner and verify the actual downstream behavior.

Use these status meanings:

| Status | Meaning |
| --- | --- |
| Documented | Recorded with provenance; not yet established as usable engine truth. |
| Validated | Supported within a stated scope by appropriate evidence. |
| Integrated | Connected to the intended canonical service or contract. |
| Operational | An actual application decision consumes it, with executable evidence of that behavior. |

Knowledge is not operational merely because a note, formula, test, or service exists. Show where the app uses it and what decision changes. A result validated for one build, role, encounter, or update must not silently become a universal rule.

## 6. Leave better records

Update the appropriate existing record during the same development increment:

- Mechanically surprising or noteworthy discovery: add a short layman's note to `GAME_MECHANICS_FIELD_NOTES.md`.
- New or materially changed user-visible feature: update `FEATURES.md`.
- Useful ESO research source: update `useful_resources.md` with its purpose, confidence, provenance, and limitations.
- Reusable numeric ESO ID: update `ESO_ID_REFERENCE.md`, preserving previous observations and conflicts.
- New or changed AI working rule: update `CLAUDE.md`; update this directory if routing changes.
- New architectural responsibility: update the canonical service catalog and relevant integrity tests.
- Intelligence integration: update the existing inventory with evidence and an honest status.

Do not put routine refactoring into game-mechanics notes or claim an internal cleanup is a new feature.

## 7. Make this entry point discoverable

Keep this file at the repository root. In each existing AI instruction entry point, add a short instruction to read root `AGENTS.md` first, preserving its existing content. This includes `CLAUDE.md` and any configured Copilot, Cursor, or other assistant instructions actually used by the project. Follow each tool's supported instruction mechanism; do not assume every tool automatically reads this filename.

Automation and code do not automatically obey Markdown. Enforce critical requirements through typed contracts, database migration safeguards, executable tests, and CI checks. Use this file to direct contributors to those owners, not as a replacement for enforcement.

Maintain one rules directory. Keep detailed rules and mechanics with their canonical owners, link to them here, and repair stale links when files move. Never overwrite an existing `AGENTS.md` blindly; merge this entry point with applicable current instructions.
