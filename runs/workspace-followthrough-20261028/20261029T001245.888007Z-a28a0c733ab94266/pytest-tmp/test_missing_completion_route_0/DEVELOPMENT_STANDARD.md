# Wyrdworks — Definition of done (formerly FoundryDock)

**Required for every development increment.** This document is the single home for validation, persistence reliability and acceptance requirements. AGENTS.md routes contributors here; CLAUDE.md requires using it without another user reminder. This is a standard, not a claim that every existing path already meets it.

## Scope gates by current workflow status

Apply acceptance to the changed behavior and its authoritative owner. Raid Plan is the only active raid-planning UI, with Teams, Map, and Readiness columns. For its supporting canonical services and relevant editors, verify the relevant save, reload, stable identity, and handoff behavior when the change touches those paths. Persistence is owned by canonical repositories and services; an active page consuming the same authoritative record does not need a redundant independent persistence proof.

Lantern, Comp Brainstorm, Coverage, Rotations, standalone Readiness, Health, Comp Engine, Optimization, Extreme Build, and Live Raid interfaces are parked. Do not require constructing, navigating to, or demonstrating save/reopen through a parked UI as acceptance for unrelated work. Verify affected underlying records and shared behavior through authoritative repositories/services, retain their regression tests, and preserve safety/identity assertions. A user-requested change to a parked interface still receives the relevant behavioral and persistence checks. This scope rule changes validation applicability, not database safety, migration rules, strict contracts, or the evidence needed for shared owners.

## 1. Declare the outcome

Before changing code, identify the visible result, canonical owner, exact identities/context, persistence impact and affected consumers. Define a small acceptance example. For an intelligence change, identify the raid-lead decision that improves and the actual page or engine that uses it.

A contract, note, unit test, dataset or pretty page alone does not fulfill an end-to-end feature request.

## 2. Validate boundaries with Pydantic

Use existing Pydantic v2 models at external-input, import, persisted-payload, public service-result and engine-handoff boundaries. New or materially changed boundaries require explicit validated schemas; do not quietly bypass them with dictionaries or unchecked deserialization. Do not blanket-convert every internal local variable into a model.

- Use strict types where coercion could hide bad evidence. Reject boolean-as-number, numeric strings, NaN/infinity, illegal ranges, inconsistent enums, duplicate identities and contradictory field combinations as applicable.
- Reject unexpected fields for new contracts (`extra="forbid"`). Compatibility imports use an explicit versioned adapter that preserves/quarantines unrecognized content; do not erase legacy fields just to pass strict validation.
- Validate required identity/scope and cross-field invariants. Distinguish absent, explicitly cleared and zero values. Do not infer identity from display names.
- Freeze evidence snapshots and use immutable collections where shared results must not mutate. Mutable editor drafts may remain mutable but must revalidate at save/evaluation.
- Pydantic alone does not enforce database transactions, foreign keys, concurrency or durability. Those need repository safeguards and behavior tests.
- Validators must not run network calls, write storage or hide expensive mechanics. Mechanical decisions remain with their canonical service.

## 3. Durable persistence contract

The canonical repository owns writes. Reference data and user-owned state stay separate. Never replace either protected working database with test/uploaded data.

For each changed write path, prove the applicable guarantees:

1. Validate the exact payload, scope and intended write set before mutation. A save without an active required plan cannot silently write unscoped state or report success.
2. Use a transaction for coupled SQLite changes; enforce applicable identity, uniqueness, referential and domain constraints. File-backed repositories use atomic replacement in their existing owned location. Choose durability/concurrency settings deliberately for that repository; no universal PRAGMA guess.
3. Detect stale edits with a revision or expected-snapshot check. An old page must not overwrite a newer or richer record.
4. Make repeated saves/imports idempotent or explicitly duplicate-safe. Partial projections cannot erase omitted state. Removal requires an explicit authorized operation.
5. Verify persisted identity and intended fields through the canonical read path before showing Saved or clearing dirty state. Full workflow/phase closeout must include a fresh repository/application reopen.
6. On validation, lock, permission, disk, write, commit or read-back failure, preserve the last verified data and user's draft. Do not report success or navigate away as though saved. Report uncertain post-commit verification honestly; do not assume rollback after a completed commit.
7. Additive migrations are versioned, repeatable and backward-compatible within supported schema scope. Rehearse on copies. Preserve provenance and richer records; invalid rows remain recoverable/quarantined, not silently discarded.
8. Retain appropriate recovery/revision evidence for risky changes. SQLite snapshots use the existing consistent backup path, including committed WAL state; arbitrary file copy while writing is not a proven backup.
9. Multi-store/external operations declare ordering, partial-success behavior, retry and recovery. A local save does not imply remote publication succeeded.

Read-only analysis must not bootstrap schemas, write migration timestamps or seed data. Verify this where that promise matters.

## 4. Test the behavior that can fail

Tests are risk-based and must exercise production behavior. Use focused regression tests for meaningful changes; do not add tests that merely mirror trivial implementation. Shared changes need both the canonical contract and affected consumer/handoff.

| Change | Required relevant evidence |
| --- | --- |
| Validation contract | Valid acceptance plus malformed/coercible/contradictory rejection; serialization roundtrip where persisted |
| Write path | Save → canonical reload → reopen; rejected input; stale edit; repeated save; injected failure preserving data/draft |
| Migration/import | Old supported schema; rerun; partial/malformed/conflicting records; no loss of richer data; isolated source preserved |
| Plan/stage/build handoff | Exact identity; scope mismatch rejection; sparse inheritance; changed-input invalidation |
| Background result/cache | Context changes; stale completion; failure clearing; resolved/unresolved cases; no mutable-cache corruption |
| Shared mechanics/intelligence | Boundary cases, unknown/conflict state, duplicate prevention and one real consumer decision |
| UI/workflow | Real widget/action behavior where relevant; save/leave guards; constrained geometry; accessible statuses |
| Performance claim | Representative measured scope; no weakening correctness; distinguish stubs from actual database/audit latency |
| Page/catalog lifecycle | Cold start + first and second visit, no eager nonessential pages or full-reference enumeration, stable plan/profile/category selection, bounded queries, targeted invalidation, retained dirty draft and live handoffs |
| Scroll/help/theme UI | Qt geometry and wheel test proving one outer vertical scroll at representative sizes including Encounters, meaningful rather than ubiquitous hover help, one Urban Wilderness theme with accessibility and fixed outer-window geometry |
| Asset conversion | Manifest/dry run/idempotence, pixel dimensions/transparency, Qt runtime load, banner/boss/map references and marker alignment, unchanged efficient SVG/PNG sprites, reversible source preservation |

Source-text tests may guard a boundary but do not prove saving, runtime math or working UI. Never weaken meaningful tests or restore retired code merely to get green.

Database-dependent tests use temporary repositories or explicit isolated copies with redirected user state. No test may target the user's working databases. Required real-data witnesses use read-only originals or disposable copies; record source scope/hash and limitations.

Run focused tests before completion. Run an appropriate wider regression for shared changes; full regression is required for phase closeout or broadly coupled engine/authority changes. Classify baseline failures and unavailable corpus separately. Never present collection errors, deselections, unrun tests or inherited failures as a green full suite.

## 5. Grow operational intelligence

Reuse canonical mechanics and `FoundryIntelligenceService`; maintain the existing integration inventory, not another engine. Separate missing facts, missing relationships and missing consumer wiring.

For each finding retain semantic key, source/update/provenance, confidence, scope, prerequisites, canonical owner, consumer, changed decision, test evidence, limitations and next action. Mechanical possibility, planned execution and observed execution remain distinct. Range, duration, recipients, targets and stacking need their own evidence; equipment presence alone proves neither proximity nor uptime.

| Status | Required meaning |
| --- | --- |
| Documented | Recorded with provenance; not established as usable mechanics |
| Validated | Evidence supports a stated scope |
| Integrated | The intended canonical path is connected |
| Operational | Actual consumer behavior is tested within stated scope |

Operational does not mean exhaustive, current-patch verified, real-player validated or installed. Keep those dimensions explicit. A synthetic consumer test can establish bounded operation, but cannot satisfy a phase claiming production real-build readiness.

Fail closed for the exact dependencies of a decision. Unrelated global knowledge gaps remain advisory; they must not block otherwise supported decisions. Logs, popularity, raid convention and hypotheses do not silently become canonical formulas.

## 6. Completion receipt

Before saying done, record briefly in the existing validation report/inventory or commit description:

- requested outcome and actual consumer;
- canonical owner, identities and boundaries;
- validation and persistence impact, with applicable evidence;
- exact checks run, results, code checkpoint and data/fixture scope;
- remaining gaps and what they prevent;
- local/committed/published/installed state.

Mark non-applicable gates with a reason. If a relevant gate cannot pass, call the result implemented/partially validated/blocked, with scope, rather than complete. No additional permission is required for routine authorized checks.

## 7. Executable enforcement

The existing pytest suite, service-registry integrity checks, dependency audit and architecture audit are the enforcement tools. Local Windows execution is the default as of 2026-10-23. Repository test workflows, including `.github/workflows/phase155-quality-gates.yml`, retain their jobs but accept only explicit `workflow_dispatch`; ordinary development pushes and PRs do not start them. Release and dependency/security workflows are outside this test-only change. The baseline supplements task-specific and full regression; it cannot certify every path, all Pydantic models or filesystem power-loss durability.

Run the free local baseline through the existing Windows runner: `python tools/run_phase155_validation.py --suite quality`. It runs the workflow's documentation check, focused regression targets, corpus-aware encounter projection tests, dependency guard and strict architecture audit. It redirects application user data and pytest scratch into a uniquely named ignored directory under `validation_reports/`, reads the local reference database in read-only mode, and records the starting/finishing revision and dirty state. Install the open-source test dependencies once with `python -m pip install -r requirements-build.txt pytest` if needed. A passing local receipt is evidence for that exact checkout; it does not establish hosted execution, installed-Windows behavior, or full-suite completion. If encounter facts are unavailable, the receipt keeps the six source-backed assertions marked not verified and cannot serve as merge evidence.

Before merging, reviewers and agents must run `python tools/run_phase155_validation.py --suite quality --verify-receipt` from the clean isolated checkout of the exact PR head. It checks the suite-specific quality receipt even if another suite has overwritten `latest.json`. All five checks and source-backed assertions must have passed, without pytest overrides, on the same revision with clean start/end states. A stale, missing, filtered, failed or dirty receipt is rejected. Historical receipts without the new provenance fields require a fresh run. Preserve dirty user work in its original checkout; do not reset databases or stage someone else's work to satisfy this gate. Use the already-supported `FOUNDRYDOCK_ESO_DATA_DIR` for a provenance-backed external reference snapshot when needed.

The GitHub account currently returns HTTP 403 for private-repository branch protection/rulesets, requesting a paid plan or public repository. No plan/access change is authorized by this policy. The receipt command is a local merge requirement, not a server-enforced GitHub status or cryptographic attestation; the browser merge button cannot enforce it. GitHub-managed security scans and historical branch definitions remain independent. Hosted account billing need not be changed to run local tests.

For long Windows paths, `--report <short-path>/latest.json` or `FOUNDRYDOCK_VALIDATION_REPORT=<short-path>/latest.json` selects the existing runner's receipt/scratch root. Use the same selection for receipt verification and the pre-push hook. No extra runner is introduced. Existing scheduled FoundryDock validation and allowlisted report-publishing tasks remain in place; an `unchanged` poll is not a new test pass.


Run the engine regressions locally with `python tools/run_phase155_validation.py --suite combat`, `--suite encounter`, or `--suite extreme`. `--suite engines` runs these three development gates sequentially and stops at the first failure. `--suite extreme-full` runs the expanded sweep of every discovered Extreme service and audit test module. Each run isolates app data, Python temporary files, and pytest scratch under a unique folder in `validation_reports/`, and writes a suite-specific receipt (`latest_combat.json`, `latest_encounter.json`, `latest_extreme.json`, `latest_extreme-full.json`, or `latest_engines.json`). The Extreme development gate covers candidate assembly/search, proof-safe bounds, and actual-heal admission; the expanded sweep discovers new service/audit modules automatically. Encounter covers its service/evidence owners, retained trial-guide projections, and the active Raid Plan projection handoff. Combat uses the same targets as `.github/workflows/phase155-combat-simulation.yml`. These checks support local engine iteration without hosted Actions; they do not prove a complete real saved-build fight or a global Extreme optimum.

To enable automatic local checks before pushing, set `git config --local core.hooksPath .githooks`. The existing pre-push hook runs quality and verifies its exact-commit receipt for every outgoing checked-out commit, then runs only the affected engine suites: Combat, Encounter and Extreme. No-op updates/deletions run no tests. A failed gate, wrong checked-out ref or unreadable diff blocks publication. Changes to the runner/hook itself select all three engine suites. The hook setting is local Git configuration and is not installed for another contributor by cloning. A dirty primary checkout may still run exploratory tests but cannot supply merge evidence; use a clean isolated checkout without touching its user data.

Markdown does not make code comply. Any newly discovered noncompliant path needs a focused fix and regression through its existing owner. Do not rewrite all historical models or add a parallel compliance engine.

## Routine push validation — raid-lead preference, 2026-10-27

Routine development pushes run focused tests selected from changed Python files and their directly corresponding test files, in isolated disposable user data. They do not automatically run the broad quality baseline and all affected engine suites. Set FOUNDRYDOCK_PUSH_CHECKS=full to request the previous broad push checks. Task-specific behavior and cross-boundary checks remain the agent's responsibility; unmatched files are explicitly reported. Broad clean exact-commit validation remains required for deliberate integration/release approval, rather than every testing push. This user-requested policy supersedes the every-push wording above.

## Temporary workspace and test-artifact completion gate

- At task start, inventory and identify **only the worktrees, branches, pytest base-temporary directories, and generated artifacts created or owned by this task**. Prefer a unique task-scoped pytest `--basetemp` outside the application source tree; never reuse or empty a shared location.
- At completion, inspect `git status` including untracked/ignored files, branch divergence, unique commits, databases, report receipts, and process/runner dependencies before removing any task-owned directory. Preserve failure evidence and anything of uncertain provenance or recovery value.
- Once work is integrated, verify the intended destination contains the relevant **file content and evidence**. Squash merges and rebases can preserve content without preserving commit ancestry; check content equivalence instead of requiring original commit SHAs to be ancestors.
- Remove a clean, unused, fully integrated **task-owned** worktree only through `git worktree remove` without `--force`; do not delete its branch automatically. Do not remove a worktree, branch, or artifact owned by another task without explicit authorization. Never reset dirty work to make cleanup pass.
- Remove only independently verified disposable, reproducible pytest caches and task-scoped test artifacts after tests finish. Do not blindly delete directories containing SQLite databases, runtime evidence, logs, snapshots, or reports; confirm ownership, retention, and recovery first. Failed runs keep useful diagnostic evidence.
- Each completion report must state **Workspace Cleanup: CLEAN**, **RETAINED WITH REASON**, or **BLOCKED**, and give exact retained paths and reasons. A blocked cleanup does not authorize destructive shortcuts or prevent an honest report of otherwise completed work.
- Apply this lifecycle prospectively. Legacy cleanup requires separate inventory and approval, not automatic sweeping.

## TestSpace focused pytest runs — Phase 1 pilot

For focused agent/developer pytest selections, use the shared launcher instead of invoking pytest directly:

```powershell
python tools/run_tests_in_testspace.py --task engine-growth-20261028-001 -- tools/tests/test_phase155_combat_pre_push.py -q
```

The existing TestSpace defaults to `C:\Dev\Wyrdworks-TestSpace`; set `WYRDWORKS_TESTSPACE_ROOT` or pass `--testspace-root` only to select another already-existing root outside the application checkout. Each invocation gets a new `runs/<task>/<run-id>/pytest-tmp` and `cache/<task>/<run-id>`, keeping disposable runs within the existing per-agent/task folders. The launcher also routes Python `TEMP`/`TMP`, user-owned application data, and `FOUNDRYDOCK_VALIDATION_REPORT` into that run, and writes an owner/command/revision/timestamp/artifact manifest under `reports/`. It removes inherited `PYTEST_ADDOPTS` so hidden pytest arguments cannot redirect scratch paths. Pass pytest targets/options only after `--`; the launcher rejects basetemp and ini-override arguments.

Failures retain pytest scratch and a diagnostic log under `failures/`. Phase 1 performs no automatic cleanup for successful or failed runs: cache, temporary files, database snapshots, and unique evidence remain available for review. The pilot does not redirect the canonical ESO reference database; tests that need it must use its established read-only boundary. Existing `tools/run_phase155_validation.py`, scheduled RAVEN/FORGE validation, pre-push checks, and report publishing remain unchanged and continue using their existing validation-report scratch paths. Direct VS Code Test Explorer and other direct pytest invocations are not yet routed through TestSpace; use the documented launcher for focused agent runs until Phase 2 addresses those entry points.

New-branch focused pushes compare against the common ancestor with fetched `origin/wyrdworks-dev`; fetch that reference first. They do not treat the entire repository as newly changed. Existing remote branches continue to compare against their outgoing remote revision.
