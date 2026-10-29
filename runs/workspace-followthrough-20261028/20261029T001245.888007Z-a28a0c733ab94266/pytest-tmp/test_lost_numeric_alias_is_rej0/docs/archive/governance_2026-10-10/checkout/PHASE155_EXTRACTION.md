# Phase 15.5 application extraction

Started 2026-10-03 from `phase15` commit
`c4758519ab16927ccacf68edbd79ed069869e796` (Expect Finch Raid Plan schema 12).

`phase15` remains the active feature/fix branch. `phase15.5` owns extraction work.

## Extraction anti-regression guard

For Phase 15.5, the extracted/native implementation is authoritative over older presentation and roadmap assumptions once replacement behavior has been validated. Historical Phase 15 code remains reference material, not an automatic source to restore from.

- Do not copy an older page/service/router/persistence implementation back into the active Phase 15.5 path merely to satisfy an older roadmap or source-shape test.
- Adopt upstream/older work only when it is still valid under current Phase 15.5 ownership boundaries, and port the smallest compatible slice.
- Preserve canonical shared engines and ESO intelligence, but keep retired presentation authorities retired.
- Before synchronization or conflict resolution, inspect the current target implementation first. Newer Phase 15.5 behavior wins unless there is explicit evidence that it is defective.
- Resolve stale tests to the current contract rather than making the current app imitate retired architecture.
- Never use broad checkout/revert/reset operations over Phase 15.5 extraction work; those can silently restore removed dependencies even when Git reports a clean operation.

The startup/scribing, Rotations, Maps/Workshop, Settings, and Collectibles/Achievements checkpoints are complete in source. Other legacy
UI boundaries and Windows/runtime validation remain.

## Completed first checkpoint

- `app.py` contains only the active Phase 15 launch; removed the unreachable old
  application composition. Existing startup/migration safeguards remain in place.
- Explicitly hide/close the Qt splash on the active path, satisfying the existing
  photosensitive startup contract that previously only appeared in dead code.
- Reusable scribing dialogs and recipe projection moved unchanged into
  `ui/components/scribing_dialogs.py`. Phase 15 Builds imports that component;
  `ui/scribing_support.py` keeps compatibility exports and the legacy installer.
- Release manifest excludes the retired MainWindow, OperationsConsole and old
  application-window composition. Their source remains available for reference.
- Read-only dependency scanner follows local imports, including imports in
  functions and parent package initializers, without importing app code or opening
  databases. `--check` fails on legacy shell paths, parse errors, or unresolved
  dynamic import sites. It does not decide which files can be deleted.
- Workspace helper creates a separate worktree and SQLite backup copies, preserves
  ignored local artwork/runtime files, and redirects writable settings. It refuses
  existing destinations, missing databases, external source user-data overrides,
  symlinked runtime inputs, shared databases and external writable settings paths.

## Rotations checkpoint (2026-10-03)

- Reusable controls, generation, sustain, timeline, artifact handling and PDF export
  live in `ui/components/rotation_workspace.py`. The standalone
  `RotationBuilderPage` keeps its full local context presentation and old handoff.
- `Phase15RotationWorkspace` composes its own plan identity controls and obligations
  directly. No old page construction, hidden context card, or widget reparenting.
- Raid Plan context resolves through `RaidPlanEffectiveContextService`; exact chairs
  resolve through `RaidPlanSavedBuildResolutionService`. Duplicate display names do
  not determine identity. Missing/stale/ambiguous selected builds fail closed.
- General and Trash never select an arbitrary boss. Boss stages use canonical
  encounter identity/name; missing canonical encounter catalog rows block generation.
  Team/trial/difficulty come from the effective plan. Planning suggestions are shown
  as suggestions and do not silently become real saved-build equipment.
- Additive Pydantic `scoped_rotations` records isolate plan, stage, seat and build.
  Native saves atomically retain a build-only latest compatibility record for
  existing Extreme Engine consumers. That latest record is **not stage authority**;
  native reopen/compare use only the exact scoped record, without global fallback.
- Existing standalone build saves remain readable. They are not automatically
  assigned to a stage. Do not copy experimental artifact files back to Phase 15:
  its earlier strict document schema does not know the optional scoped field.
- Stage/seat switches retain generated drafts and notes in memory. Navigation/close
  guards include inactive dirty drafts with Save All/Discard/Cancel. Explicit saves
  read back exactly before clearing dirty state. Reopen restores saved action targets,
  notes, settings and priorities; it does not fabricate sustain/duration evidence.
- Build/context fingerprints prevent changed inputs from reopening a stale schedule
  as current. Previous saves remain intact and regeneration is required.

The generation request remains the existing saved-build rotation request. Selecting
an encounter exposes its reviewed demand policy; this extraction does not add new
encounter-execution mechanics, prove a stage schedule mechanically complete, or make
build-only Extreme Engine readers stage-aware. Those remain separate reviewed work.

Validation: **46 focused tests passed** across native/standalone UI, scoped saves,
Pydantic persistence, runtime, sustain, timeline, PDF and isolation tooling. Expanded
selection: **93 passed, 7 inherited failures**. The seven names reproduce on upstream
`e64c63a` (Comp statistics source assertion, three shared-stage source assertions,
and three canonical-build fixture failures); their affected production sources are
unchanged by the later `2cb1b3e` synchronization. Tests of native UI use isolated
artifacts and injected plan/build fixtures, not the user's live Windows database.

The static startup closure is now **564 modules**, with no path to the three retired
shells or the standalone old Rotation page, no scan failures or recognized dynamic
imports. A fresh shell import confirms those four modules remain unloaded. Their
source is retained and packaging excludes them from the default new app. Generation,
sustain, priority, timeline rendering, evidence and PDF export method ASTs match the
adopted Phase 15 source. The reference database Git hash remains unchanged.

## Strategy / Raid Map and Workshop checkpoint (2026-10-03)

- Strategy now uses `Phase15RaidMapWorkspace`; it does not construct or hide
  `EncountersPage`. Shared map persistence, member-name projection and publishing
  orchestration live in `ui/raid_plan_map_workspace.py`; the old standalone page
  inherits those methods and retains its presentation/reference tabs.
- `RaidMapEditorMixin` owns common inspectors/actions for both native Strategy
  and standalone Workshop. Workshop no longer imports Strategy or aliases its
  methods. Existing board, formation, theme/accessibility and GIF capabilities
  remain shared; this checkpoint does not rewrite their editing math.
- Pydantic path/scope contracts configure board state and image paths before
  board construction. Workshop never loads the old shared authoring file first.
  Legacy callers still use their original filenames unless given explicit paths.
- Native Strategy drafts and timeline stores are isolated by exact plan/context.
  General, named Trash, Boss and Predot have distinct drafts. A stage without a
  saved layout starts with a blank map rather than carrying the previous stage's
  markers, image or animation. The old global files remain untouched; they are
  not automatically guessed into a plan or stage.
- Stage activation preflights layout, background assets and Pydantic keyframes
  before rebinding. Invalid targets keep the existing editor scope. Failed
  same-plan stage transitions restore the previous shared stage selection.
- Saved plan layouts and Workshop entries include optional validated timeline
  sidecars. Workshop keeps copied imported backgrounds self-contained. Layout
  reload restores backgrounds, reference locks, formations and animation steps.
  Older layouts with no timeline sidecar reopen with an empty timeline; old
  global choreography is not silently attached to an unrelated map.
- Plan-layout listing excludes timeline sidecars. Editable layouts retain stable
  seat identity; player-name projection is only used for Live Raid/Finch images.
  Snapshot/export errors restore seat labels before returning to the editor.
- Local editable saves, raster capture and GIF export were exercised with
  isolated fixtures. Finch publishing orchestration retains the existing service
  and explicit action; tests use fake network clients, and no live plan/map was
  published to FD.my during validation.

Validation: **73 focused tests passed** across native maps, Workshop wiring,
geometry, formations, timelines, custom labels, imported backgrounds, Pydantic
board persistence, Finch service contracts and worktree isolation. **12 Rotations
regression tests passed**. The wider map selection initially reported 79 passes
and four failures, all reproduced on latest Phase 15 `6e7cd0c`: two accessibility
source/default expectations and two older map-store fixture/error expectations.
Additional older shell/navigation source assertions remain; source-test ownership
was updated where methods moved, without replacing their semantic assertions.

Static closure: **566 modules**, no retired shell/Rotation/Encounters page paths,
no scan failures or recognized dynamic imports. A fresh Phase 15.5 shell import
leaves `ui.encounters_page` unloaded. Its source remains available and its module
is excluded from default new-app packaging. Reference database hash unchanged.
Live Windows data, EXE packaging and visual/theme testing on that workstation
remain completion gates; this is not yet the entire app extraction.

## Parallel development on Windows

Run the preparation tool from the Phase 15.5 source after fetching that branch, or
invoke the same file from any checkout containing this checkpoint. For the user's
usual repository, source is `C:\Dev\BFF\FoundryDock` on `phase15`; destination is a
new sibling such as `C:\Dev\BFF\FoundryDock-15.5`.

The command interface is `python tools/phase155_workspace.py prepare --source
<phase15-root> --destination <new-sibling-root>`. It does not switch the source
branch, commit source changes, reset databases, or publish anything.

Start the new workspace through `python tools/phase155_workspace.py run` from its
root. The launcher validates the local marker, branch, databases and writable
settings paths, then overrides any inherited user-data directory with the copied
workspace directory. Direct `app.py` launch bypasses these development checks.

SQLite online backup includes committed WAL transactions. The two databases are
copied separately; pause app edits during preparation when a consistent pair is
needed. The source's user data remains authoritative. Never copy 15.5 experimental
databases back over the working Phase 15 databases.

Historical `data/eso.db` is still tracked in this repository despite its ignore
rule. Preparation uses per-worktree sparse checkout to keep database paths out of
the new Git checkout before copying live snapshots. It does not delete or replace
the source database. Do not disable those sparse exclusions or check out database
paths over the runtime copies during synchronization.

Preparation does not overwrite an existing target. On failure, the new worktree
remains inspectable and no valid launch marker is written. There is no automatic
cleanup that deletes a user's workspace.

## Remaining UI boundaries

| Phase 15 surface | Retained older dependency | Next extraction |
|---|---|---|
| Rotations | Shared `ui.components.rotation_workspace` and canonical services | Old page removed from active import closure; validate live data/Windows packaging |
| Strategy / Raid Map + Workshop | Shared board capabilities and canonical map/timeline services | Old page removed from active closure; validate live data, themes and Windows packaging |
| Settings | Subclasses `ui.settings_page.SettingsPage` | Retain canonical SettingsService/schema; separate reusable controls and behavior |
| Collectibles | Dashboard/category pages and presentation installers | Keep profile/progress persistence and category drill-down while separating presentation |
| Achievements | Subclasses `ui.achievements_page.AchievementsPage` | Preserve progress/import workflows; separate reusable workspace |
| Gear | Directly uses `ui.gear_lookup_page.GearLookupPage` | Treat as retained research workspace until a replacement is needed |
| Startup Quick Entry installer | Targets `ui.comp_brainstorm_page.CompBrainstormPage` | Review its applicability to native Comp Maker before adapting or retiring it |

File age and phase numbers do not define retirement. Canonical models, repositories,
services, reference evidence, provider/coverage semantics, exports and Extreme Engine
remain shared application foundations. Do not duplicate or simplify their ESO math.

## Upstream synchronization

Adopted Phase 15 through `6e7cd0ca6b46c3ca1397148a6f9f1c0342161b05`.
This adds Workshop import/background-copy behavior and editor-control parity after
`2cb1b3e19fcbf0a1a011664c57a854f9379b6a62`.
The latest sync adds Map Workshop context/load guards and menu spacing fixes, after
`e64c63a` (Index standalone Phase 15 Map Workshop).
This carries forward Health workflow/footer changes, Raid Map geometry containment,
and the Pydantic Map Workshop/library while preserving the extraction changes.
The feature index conflict was resolved by retaining both branches' entries.

## Synchronization and completion gates

1. Record each upstream Phase 15 commit adopted into 15.5. Bring over small changes
   at checkpoints and resolve overlapping UI changes deliberately.
2. Review incoming database paths separately; no database replacement through Git,
   copy commands or migration shortcuts. Source user data is not a merge payload.
3. Run `python tools/audit_phase155_dependencies.py --check` after boundary changes.
4. Run focused behavior/persistence tests and compare wider failures against the
   same upstream checkpoint. Do not declare unrelated inherited failures fixed.
5. Before retiring each old UI dependency, verify load/edit/save/reopen and stage
   transitions against isolated real data, plus applicable exports and publishing.
6. Before 15.5 takes over: actual Windows packaged launch, theme/assets, current
   plan restoration, 12-chair/build identity, saved draft/build handoff, assignments,
   Coverage, Rotations, Readiness/Raid Health, map save/reopen, and FD.my export.

## Initial validation

The conservative cleaned-startup closure contained 598 local Python modules after the upstream synchronization, no
paths to the three retired shell modules, no parse failures, and no recognized
dynamic import sites. This is static evidence, not a full runtime/package proof.

The wider Phase 15 selection initially reported 12 inherited failures; the same
selection on the extraction base reported those same 12 plus the splash-close
failure repaired here. No new failure names were introduced. Several inherited
assertions are source-string expectations for older routes/captions; retain their
failure record until behavior is reviewed rather than blindly changing tests.

Focused extraction/startup/research-route/scribing checks: **43 passed** before
synchronization. The post-sync focused selection also includes scribing recipe
round-trips and Map Workshop wiring: **53 passed**. The
Phase 15.5 shell imports successfully without importing the retired main window
or operations console; legacy scribing callers resolve the same shared dialogs.

No live Windows user database was available in this execution environment. Tests
of worktree setup and backup isolation use temporary Git repositories and SQLite
fixtures, including an open committed WAL. A Windows EXE build has not been run.

Post-sync Map Workshop/store/Health selection: 31 passed, 3 failed. The same
three failures are reproduced on upstream `e64c63a`: two map-store fixture/error
expectations and the existing Health service-docstring assertion. They are
inherited and are not hidden by the extraction checks.

## Settings checkpoint (2026-10-03)

Adopted Phase 15 through `8ec6b4919cd265ad1c723c75cc65af136ab4b4d7`
(roadmap consolidation only since the Maps checkpoint).

- `ui/components/settings_workspace.py` owns shared construction lifecycle,
  browse controls, dirty/flush guards, reload/save, and explicit Finch/OBS tests.
  `SettingsService` remains the catalogued persistence owner; its validation,
  keyring behavior, atomic write/read-back, and settings schema are unchanged.
- Native `Phase15SettingsPage` inherits the shared workspace directly. The old
  `SettingsPage` retains its rail presentation as a compatibility subclass.
  Shared behavior/helper method ASTs match the previous owner exactly.
- Native appearance/accessibility cards, optional Broadcast controls, embedded
  achievement import, and safe snapshot actions remain unchanged. No new theme
  styling or database migrations were introduced.
- Packaging and closure audit now exclude `ui.settings_page`. The closure has
  566 local modules, no retired UI paths, parse issues, or recognized dynamic
  imports. A fresh native Settings import does not load the old page.
- Focused Settings/service/persistence selection: 41 passed, one unrelated
  Comp Maker source assertion deselected after reproducing it on Phase 15.
  Extraction-tool checks plus the updated Settings route check: 10 passed.
  Both presentations cover save/reload, secret controls, failed-save draft
  retention, browse cancellation, optional Broadcast preservation, and mocked
  Finch success/error responses; no live external requests were sent.
- Initial constructor tests exposed an existing embedded achievement importer
  updating the checkout reference DB's `collectibles_sidebar_v2` migration
  timestamp. Logical dumps show only that timestamp changed. The DB is excluded
  from the checkpoint and was not replaced/reset; Settings tests now stub that
  embedded workspace to avoid opening databases. Review this existing side
  effect during the Collectibles/Achievements extraction.

Next boundary: Collectibles/Achievements. Actual Windows packaging, all-theme
visual checks, and live user-data validation remain completion gates.

## Collectibles/Achievements checkpoint (2026-10-03)

Phase 15 remains at the adopted `8ec6b49` checkpoint.

- Shared UI now lives in `ui/components/collectible_workspace.py`,
  `collectible_dashboard.py`, and `achievement_workspace.py`. Native routes
  import these owners directly. Old page modules provide compatibility imports,
  including named private helpers and public star exports; they no longer own
  workspace implementations. Legacy installers now patch the shared collectible
  owners rather than copying or changing the native page implementation.
- Existing catalogue, named-profile ownership, achievement progress, import,
  export, summary and strict Pydantic persistence services remain the authorities.
  No new service, progress schema, or database relocation was introduced.
- Achievements uses canonical `get_settings_path()` instead of a working-directory
  settings file. Dashboard asset lookup uses `get_resource_path()` after the
  move, preserving historical and current theme paths in source/packaged runs.
  No palette or badge selection changes were made.
- Collectible startup inserts an existing sidebar migration marker with
  `INSERT OR IGNORE`, preserving its original timestamp instead of replacing it
  at each construction. Existing additive setup/category updates still run.
  This code change does not modify either checkout database; the pre-existing
  test timestamp change remains uncommitted and excluded from publication.
- Packaging/audit exclude all three old page modules. The static closure has
  566 modules, no retired paths, parse issues, or recognized dynamic imports.
  Fresh native imports plus theme installation do not import old collection pages.
- Moved class/method ASTs match their prior owners except the two documented
  settings/resource path fixes.
- Focused UI/profile/service/persistence/catalogue/extraction checks: 54 passed.
  Settings regression checks: 23 passed. UI tests use SQLite online backups into
  new temporary fixtures and verify the checkout reference DB hash is unchanged.
  Verified collectible details/ownership save and reopen, profile isolation,
  failed-save navigation blocking, achievement edits, external-import refresh,
  canonical settings path, migration timestamp stability, compatibility identity,
  and routing for all four retained theme expressions. No live Google/Finch
  imports or publishing were performed.
- Wider selection: 36 passed, six older dashboard/theme/sidebar assertions failed;
  those same six reproduce on Phase 15. Another older Live Raid layout source
  assertion also reproduces upstream. These failures were not hidden or repaired
  by rewriting behavior expectations.

Next: audit remaining research/advanced composition and packaging dependencies,
then validate the complete application in an isolated runtime. Windows EXE,
actual theme rendering/assets, and live user-data checks remain pending.

## Composition audit and isolated launch checkpoint (2026-10-03)

Adopted concurrent Phase 15.5 fixes through `3e35aa9` before publication, including
Windows fixture connection cleanup and current persistence/audit contract fixes.
Phase 15 remains at the previously adopted `8ec6b49` checkpoint.

### Remaining runtime ownership

| Area | Runtime owner | Extraction finding |
| --- | --- | --- |
| Startup and navigation | `app.py`, `Phase15RaidPlanWindow` | Native composition; old window shells excluded |
| Raid planning | Native Phase 15 Roster, Raid Plan, Brainstorm, Assignments, Builds, Coverage, Health, Readiness, Live Raid | Shared canonical repositories and stage controller retained |
| Rotations | Native page/workspace plus shared rotation component | Old standalone builder outside the runtime |
| Strategy and Map Workshop | Native hosts, shared editor/board/map workspace | Old Encounters page outside the runtime |
| Collectibles and Achievements | Shared components behind native routes | Old page adapters outside the runtime |
| Settings | Native presentation and shared settings workspace | Old rail page outside the runtime |
| Gear Lookup | Independent reusable catalogue browser | No legacy shell/page construction; retain its canonical cleanup owner |
| Top Gear and advanced tools | Native Top Gear, Comp Engine, Optimization, Extreme Builder | Retain canonical ESO Logs/evidence/Extreme Engine services |
| Themes and support widgets | ThemeManager, stylesheet loaders, reusable widgets | Older names alone do not imply a retired page; these remain shared foundations |

The audit found one remaining old-page import: startup installed Quick Entry on
`ui.comp_brainstorm_page.CompBrainstormPage`, which the native shell never creates.
Removed that import/call from Phase 15.5 startup, retained the installer in source
for older callers, and excluded the retired page from packaging and dependency
checks. Native Brainstorm owns its own freeform notes and draft persistence.
The isolated launch explicitly saves and reopens those notes after removing the
unused installer. No native editor capability was removed.

### Actual verification

- Dependency closure: 562 local modules, no retired UI paths, scan issues, or
  recognized dynamic imports. Ten retired shell/page modules are excluded.
- Strict release candidate audit: PASS; all 64 external runtime data entries and
  three runtime directories classified, zero unclassified top-level data files.
  This is the existing release boundary audit, not an EXE build.
- New `tools/validate_phase155_runtime.py` runs actual `app.main()` in a child
  process from a disposable code/resource copy. It uses the existing SQLite
  online-backup helper for new fixture DBs, empty test credentials, an isolated
  user-data directory, and blocks retired UI imports and external requests.
  It never loads the source settings file or OS keyring.
- Offscreen source startup: 21 pages constructed, 17 main routes plus four
  advanced/home paths opened, one visible top-level main window after splash
  handoff, native Brainstorm notes saved/reopened, and clean window shutdown.
  No retired modules loaded, external requests attempted, unexpected errors,
  or missing approved runtime assets. Source DB hashes match before/after.
- A fresh Workshop draft raises its existing unsaved-changes confirmation. The
  validator chooses Discard only in the disposable fixture and records that
  confirmation; it does not bypass dirty guards or discard source/user work.
- Focused startup/extraction/runtime selection: 21 passed. The new validator
  reports unavailable or unprepared sources as failure and checks source DB
  hashes even when the child fails or times out.

This launch test covers cold startup and navigation with no selected live Raid
Plan. It does not certify real builds, occupied-chair identity, active-stage
editing, external imports/publishing, visual appearance, or a packaged Windows
EXE. Those remaining gates require isolated representative plan/build fixtures
and the Windows workstation's current data/assets. Broader pytest error repairs
are being handled separately; this checkpoint does not claim the full suite passes.
