# Raid Plan save continuity — 2026-10-22

## Delivered behavior and ownership

The active Builds page and contextual player-build modal expose Save Draft and
Apply to Raid Plan. Merely choosing a different build no longer writes General.
The draft retains exact plan/stage/seat/build IDs and the complete editor snapshot;
reopening recovers the selected alternative as well as its authored edits. Apply
uses RaidPlanRepository's transaction with BuildCatalogService and the existing
context-override owner. General and non-General selection writes stay separate.
It updates the reusable Saved Build: other plans using that same BuildId receive
those build changes. The UI explains this before applying. Player/character
ownership, other catalog records, progression, and imported extension fields are
preserved. This does not replace the existing named sparse-variant inheritance
system with a new build engine.

Crit/Pen opened from either Builds or Raid Plan now uses the stage-aware canonical
calculation owner. Structured version-1 state retains the exact plan/stage/seat,
metric and physical/spell channel, source selections, resistance targets, numeric
loaded/scenario/effective totals, evidence text and Raid Lead notes. Draft and
applied decisions are separate; applying consumes the matching draft. A changed
calculation fingerprint retains historical results for review rather than replaying
old source adjustments into new calculations. Calculator Apply never equips gear,
changes assignments, or makes manual scenario contributions verified mechanics.
Legacy formatted plan-note decisions remain readable. Unsaved notes survive seat,
metric and channel changes, and a cancelled close preserves the editor.

Assignments retains its canonical Phase15AssignmentStateService record. Both the
full page and compact Raid Plan dialog can persist a separate draft before Apply.
Hidden jobs, support/timing notes and kill/pull priorities remain protected. The
full page compares the loaded applied snapshot instead of adopting a fresh snapshot
at save time. Saving/navigating a draft does not silently apply it. A matching draft
is consumed only when its contents are successfully applied.

The active Coverage owner's dialog saves a source/condition draft per exact
plan/stage/effect/seat before applying through the existing General/context owner.
Changing the selected chair retains local unsaved source/note values. Stale drafts
stay recoverable; source evidence does not become a claim of range, recipients or
uptime. The parked Coverage page retains its existing save/checkpoint behavior.

The canonical save clock now includes committed SQLite module drafts and stage
records. The Raid Plan footer and module statuses share one UTC-to-local display
format, refreshed after returning from modal editors. A clock-read failure says
the time is unavailable rather than changing the verified data-save result. Map
layouts and route-note files retain their existing independent save owners; the
SQLite save clock is not a claim that every external file was saved.

## Persistence and safety

- Existing SQLite owners perform additive, repeatable draft-table creation. Existing
  Raid Plan payloads default to no calculator states; no database reset, reseeding,
  file replacement, or migration of user-owned data was used for validation.
- New persisted envelopes use Pydantic contracts with forbidden unexpected fields.
  The existing explicitly extensible build-snapshot adapter preserves imported
  extensions. Strict finite calculator values reject coercible strings, booleans,
  infinity, NaN and duplicate sources. Database identity and payload scope must agree.
- Context tokens conservatively include the plan, its stage/assignment/coverage
  records and canonical build catalog. An unrelated stage/build edit can require
  reopening. This is deliberate stale rejection, not automatic conflict merging.
- Coupled build/plan/stage writes use one transaction. Injected failure after the
  catalog mutation rolls back the compound write and retains the saved draft.
  Post-commit verification failure is reported as unverified; the editor is kept,
  without pretending that the committed write rolled back.
- Tests use temporary databases and redirected application user data beneath ignored
  validation_reports directories. They do not use the user's working databases as
  disposable fixtures. Generated scratch is retained there for diagnosis.

## Validation receipt

Machine-readable local receipts are generated under ignored `validation_reports/`;
they are not an installed-Windows or hosted-CI claim. Checks overlap and must not
be added together as a unique-test count.

| Check | Observed result | Local receipt |
| --- | --- | --- |
| Focused model, repository, module UI and contextual modal acceptance | 182 passed, no skipped tests | validation_reports/raid_save_acceptance.xml |
| Latest physical/spell isolation and calculator/build regression | 20 passed | validation_reports/raid_save_edges.xml |
| Full contextual Builds modal tests after lifecycle/selection fixes | 8 passed | validation_reports/raid_save_modal.xml |
| Latest strict-value, build rollback/ownership, legacy-read and editor-reload checks | 19 passed | validation_reports/raid_save_failures.xml |
| Latest Coverage draft reopen and stale-editor/chair-switch checks | 9 passed | validation_reports/raid_save_coverage.xml |
| Documentation routing and whitespace checks | 0 documentation issues; diff check passed | command output |
| Repeated local quality baseline | 359 regression tests and 16 encounter tests passed; dependency check passed; strict architecture audit: 0 errors, 333 warnings, 0 closeout blockers | validation_reports/raid_save_quality_final_quality.json |

An initial complete local quality baseline passed: 359 regression tests, 16
encounter tests, documentation contract, dependency boundary, and strict architecture
audit (0 errors, 333 warnings, 0 closeout blockers). The local encounter corpus was
available; those 16 encounter tests were not reported using deselections.

The wider legacy target
`ui/tests/test_coverage_context_provider_persistence.py` cannot collect because it
imports the absent `ui.coverage_raid_plan_scope_support` module. That module is
absent from the starting/current committed tree and is not supplied by this
increment. This is an explicit remaining baseline collection gap; no green full
repository suite or repaired parked-page compatibility is claimed.

Windows manual visual acceptance, installation/release packaging, and hosted CI
were not performed. Offscreen Qt tests exercise real active editor actions and
reopening, with bounded fixtures; they do not establish exhaustive production data
coverage. No ESO mechanic was introduced or researched, so
GAME_MECHANICS_FIELD_NOTES.md and useful_resources.md require no new entry.

## Repository preservation

Work began on wyrdworks-dev at 7a233c47a. A concurrent tracking/documentation/assets
cleanup advanced HEAD to faa8bb2ef without overlapping these save-path edits; it
was preserved. Existing tracked local changes in .vscode/tasks.json and the four
data files (achievement_progress.json, builds.json, characters.json, eso.db), plus
the separately tracked/untracked local assets, documents, archive probes and old
UI experiments, are excluded from this feature commit. No blanket add, reset,
clean, stash, checkout replacement or destructive Git cleanup was used.

The final remaining-file inventory is saved locally as
`validation_reports/raid_save_remaining_state.json`, with every remaining modified
or untracked path rather than a claim of a clean worktree. The feature commit and
push identity are supplied in the session's completion receipt. The repository's
own unrelated data/assets/documents remain outside that commit.
