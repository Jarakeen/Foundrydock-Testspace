# Phase 15.5 Dependency Census

Status: **initial committed-branch census complete**

This document records the current dependency boundary for the Phase 15.5 FoundryDock runtime.
It is intentionally conservative: a shared module is not treated as legacy merely because it
predates Phase 15.5.

## Executive summary

The Phase 15.5 application shell is independent of the retired application shells.

Validated runtime evidence:

- `app.py` constructs `ui.phase15_raid_plan_window.Phase15RaidPlanWindow` directly.
- The Phase 15.5 main window owns the 21 current pages/routes.
- The Phase 15.5 runtime validation exercises all 21 routes.
- Runtime validation reports no retired UI modules loaded.
- Runtime validation reports no unexpected network attempts.
- Runtime validation closes the application cleanly.
- Real Comp Brainstorm persistence has been manually validated across save, full workflow
  navigation, application close, and reopen.

This means the current dependency problem is mostly **shared-core ownership**, not retired-shell
reachability.

## Classification

### 15.5 native authority

These are the current Phase 15.5 shell/workflow authorities and should remain the application
surface:

- `ui.phase15_raid_plan_window`
- `ui.phase15_landing_page`
- `ui.phase15_raid_plan_page`
- `ui.phase15_roster_page`
- `ui.phase15_comp_maker_page`
- `ui.phase15_comp_engine_page`
- `ui.phase15_assignments_page`
- `ui.phase15_coverage_page`
- `ui.phase15_builds_page`
- `ui.phase15_raid_health_page`
- `ui.phase15_rotations_page`
- `ui.phase15_readiness_page`
- `ui.phase15_strategy_page`
- `ui.phase15_live_raid_page`
- `ui.phase15_optimization_page`
- `ui.phase15_extreme_builder_page`
- `ui.phase15_collectibles_hub`
- `ui.phase15_achievements_page`
- `ui.phase15_top_gear_page`
- `ui.phase15_settings_page`
- `ui.phase15_map_workshop_page`
- `ui.phase15_side_nav`
- `ui.phase15_stage_bar`
- `ui.phase15_save_feedback`
- `ui.phase15_sprite_assets`
- `ui.phase155_new_raid_plan_dialog`
- `ui.raid_stage_controller`

### Shared core: keep

These modules predate Phase 15.5 in some cases, but they currently act as shared domain or
persistence infrastructure rather than retired application UI.

#### User/database and plan infrastructure

- `engine.config`
- `services.eso_database`
- `services.user_database`
- `services.raid_plan_repository`
- `services.raid_plan_stage_repository`
- `services.roster_service`
- `services.roster_workspace_state_service`
- `services.user_safety_snapshot_service`

#### Build authority

`services.build_service.BuildService` remains a central shared dependency of Comp Brainstorm,
Builds, Coverage, Readiness, Optimization, Extreme Builder, roster identity binding, Finch
publishing, and Extreme/minmax services.

**Classification:** shared core, not retirement candidate.

**Deep-pass result:** resolved as shared core. `BuildService` documents `user_data/foundrydock.db` through `CanonicalBuildBridge` as canonical player/character/build persistence; `data/characters.json` and `data/builds.json` are legacy migration inputs only. Do not create a second Phase 15.5-only build persistence stack.

#### Raid-planning intelligence

Examples of current shared services:

- `services.phase15_assignment_state_service`
- `services.raid_plan_offensive_stats_service`
- `services.raid_plan_context_coverage_repository`
- `services.raid_plan_coverage_scope_service`
- `services.saved_build_capability_service`
- `services.raid_named_group_effect_capability_service`
- `services.raid_unique_support_set_capability_service`
- `services.raid_planned_gear_coverage_service`
- `services.raid_planned_skill_coverage_service`
- `services.raid_readiness_evidence_service`
- `services.raid_section_state_service`
- `services.raid_plan_optimizer_adviser_service`
- `services.raid_plan_saved_build_resolution_service`

These belong to the current application intelligence layer and should not be retired simply
because they originated before the 15.5 extraction.

#### Reference/canonical ESO services

- `services.reference_data_service`
- `services.ability_effect_provider_reference_service`
- `services.nonability_effect_provider_reference_service`
- `services.passive_effect_provider_reference_service`
- `services.known_effect_sources_service`
- `services.class_mastery_repository`
- `services.eso_icon_resolver`
- reviewed encounter/reference services consumed by Strategy and Live Raid

These are canonical/reference dependencies and remain shared core.

### Shared UI: keep, but normalize ownership

The Phase 15.5 pages still use a small amount of mature reusable UI instead of duplicating it:

- `ui.components.scribing_dialogs`
- `ui.components.raid_map_editor`
- `ui.components.raid_map_workspace`
- `ui.gear_lookup_page`

These are not retired shells. They are reusable surfaces/components.

**Follow-up:** eventually give any permanently retained shared component a neutral ownership name
when its current name implies an obsolete phase or theme.

## Boundary requiring review

### Raid Map / EncounterBoard behavior stack

`app.py` intentionally installs mature Raid Map behavior before constructing the Phase 15.5
window:

- `ui.encounter_board_accessibility`
- `ui.rylo_raid_map_support`
- `ui.encounter_board_formation_support`
- `ui.encounter_position_gif_export_support`

The current Strategy page uses:

- `ui.components.raid_map_editor`
- `ui.components.raid_map_workspace`
- `services.encounter_raid_map_store`

**Classification:** shared mature subsystem, currently required.

**Deep-pass result:** this is a real shared subsystem, not a retired-shell dependency. Packaging explicitly requires `ui/components/encounter_board.py` plus the current accessibility/custom-label behavior. The current installer pattern remains architectural debt because behavior is attached globally to the EncounterBoard class.\n\n**Action:** keep the subsystem for now. The next architecture slice should wrap/compose these behavior installers behind one neutral Raid Map bootstrap/composition boundary, preserving every current feature and all themes before any old helper name is retired.

### Startup user-data migration

`app.py` still calls `services.user_data_migration_service.migrate_legacy_user_data`.

**Classification:** migration compatibility, intentionally retained.

**Action:** keep until the standalone 15.5 release policy defines when old installs no longer need
migration. This is not evidence that the retired UI is still required.

### Optional broadcast migration

Startup may call `services.broadcast_state_migration.migrate_legacy_broadcast_state` when the
optional broadcast module is enabled.

**Classification:** optional migration compatibility.

**Action:** keep isolated from the default Phase 15.5 runtime boundary and review during packaging
cleanup.

## Explicit retired-shell boundary

The release manifest excludes these retired surfaces from the Phase 15.5 packaged runtime:

- `ui.main_window`
- `ui.operations_console`
- `ui.application_window_composition`
- `ui.phase14_rotation_page`
- `ui.encounters_page`
- `ui.settings_page`
- `ui.achievements_page`
- `ui.collectibles_page`
- `ui.collectibles_dashboard_page`
- `ui.comp_brainstorm_page`
- `old_pages`
- `legacy`
- `deprecated`
- `migration`

Current runtime validation has already demonstrated that these retired UI modules are not loaded
while all 21 Phase 15.5 routes are exercised.

**Current action:** preserve them in source until candidate-by-candidate retirement audits prove
there are no tooling, migration, test, packaging, or persisted-data dependencies.

## Page-level dependency notes

| Page / surface | Current authority | Main dependency class | Census disposition |
|---|---|---|---|
| Landing | Phase 15.5 | plan repository / native dialog | Keep |
| Raid Plan | Phase 15.5 | raid-plan repositories | Keep |
| Roster | Phase 15.5 | RosterService + roster workspace state | Keep; persistence cleanup continues |
| Comp Brainstorm | Phase 15.5 | BuildService + draft services | Keep |
| Assignments | Phase 15.5 | Phase15AssignmentStateService + canonical effect sources | Keep |
| Coverage | Phase 15.5 | saved-build/canonical coverage services | Keep |
| Builds | Phase 15.5 | BuildService + canonical build services | Keep |
| Raid Health | Phase 15.5 | raid-plan intelligence | Keep |
| Rotations | Phase 15.5 | Phase15RotationWorkspace | Keep; inspect workspace internals next |
| Readiness | Phase 15.5 | readiness evidence + section state | Keep |
| Strategy | Phase 15.5 | Raid Map shared subsystem | Keep; normalize subsystem boundary |
| Live Raid | Phase 15.5 | encounter guides/map/assignment state | Keep |
| Optimization | Phase 15.5 | optimizer adviser + saved-build capability | Keep |
| Extreme Builder | Phase 15.5 | Extreme Engine/shared build resolution | Keep |
| Gear | shared page | canonical reference data | Keep; potential future Phase 15.5 wrapper only if needed |
| Collectibles | Phase 15.5 | canonical/user progress services | Keep |
| Achievements | Phase 15.5 | canonical/user progress services | Keep |
| Top Gear | Phase 15.5 | ESO Logs / trend services | Keep |
| Settings | Phase 15.5 | settings service | Keep |
| Map Workshop | Phase 15.5 | Raid Map shared subsystem | Keep; normalize subsystem boundary |

## Retirement candidates: current state

There is **no evidence yet that a live Phase 15.5 route requires a retired application shell**.

Therefore the first retirement pass should target source modules already excluded from packaging
and reported by `tools/audit_code_retirement.py` as test-only, tooling-only, quarantine-only, or
static-orphan candidates.

Do not bulk-delete a directory.

Retire one dependency family at a time:

1. run the static retirement audit;
2. inspect dynamic/string/Qt/release references;
3. remove or quarantine only the proven candidate;
4. run focused tests;
5. run Phase 15.5 runtime validation;
6. periodically run the full suite.

## Rotation runtime boundary

Deep census found that the reusable `ui.components.rotation_workspace` still imported
`services.phase14_rotation_runtime_service.Phase14RotationRuntimeService`, even though the
service itself had no retired-page dependency and already called shared Rotation engine seams.

This has now been normalized:

- current authority: `services.rotation_runtime_service.RotationRuntimeService`
- current result contract: `RotationRuntimeResult`
- the shared Rotation workspace imports the neutral authority
- `services.phase14_rotation_runtime_service` remains only as a compatibility alias for
  retired Phase 14 source/tests until their retirement pass
- a focused regression test guards the boundary

**Classification:** resolved shared core.

## Remaining shared UI/workspace findings

- `ui.gear_lookup_page` is a generic Foundry surface using canonical/reference data. Keep.
- `ui.phase15_top_gear_page` talks directly to ESO Logs trending and Settings services. Keep.
- `ui.phase15_settings_page` embeds `AchievementProgressImportPage`, which itself uses
  canonical achievement/collectible/motif services and generic Foundry components. It is a
  reusable import utility, not a retired Settings authority. Keep.
- `ui.components.settings_workspace` is generic and current. Keep.

## Next work item

**Next deep census pass: remaining shared UI/workspace authorities.**\n\nBuildService is now resolved as shared core. Raid Map is resolved as required shared infrastructure with an installer-composition cleanup target. Next inspect `Phase15RotationWorkspace`, Gear Lookup, Top Gear services, Settings services, and any shared UI helper that is still named after an obsolete phase/theme.


## Retirement-candidate pass

### Retired application cluster

The modules excluded from the Phase 15.5 release are not all independent orphan files. Most belong
to one older application cluster centered on the retired `ui.main_window` shell.

Observed cluster members include:

- `ui.main_window`
- `ui.operations_console`
- `ui.application_window_composition`
- `ui.phase14_rotation_page`
- `ui.encounters_page`
- `ui.settings_page`
- `ui.achievements_page`
- `ui.collectibles_page`
- `ui.collectibles_dashboard_page`
- `ui.comp_brainstorm_page`
- older installer/support modules that monkey-patch or register pages on those surfaces

These modules still have source/test references to one another. That is expected historical
coupling and is **not** evidence that Phase 15.5 requires them.

The decisive runtime evidence remains the Phase 15.5 validation gate: all current routes load while
the retired UI modules remain absent from `sys.modules`.

**Disposition:** quarantine/retire as a cluster after test/tool migration, not piecemeal deletion.

### Why not delete the cluster immediately

Several historical tests still assert behavior of the retired shell, and some migration/development
support modules still import the old surfaces. Deleting single files now would create noisy test
failures without improving the Phase 15.5 runtime boundary.

The correct order is:

1. identify tests that protect current shared engine/service behavior versus tests that protect only
   retired UI behavior;
2. move any still-valuable shared assertions to current Phase 15.5/shared-core tests;
3. mark retired-shell-only tests as retirement candidates;
4. confirm packaging and runtime validation remain clean;
5. remove the retired cluster in a dedicated retirement slice.

### Search caveat

Repository-wide GitHub code search may surface references from another indexed commit/default
branch. Retirement decisions must use the checked-out `phase15.5` source plus the branch-local
static audit and runtime validation, not search-result presence alone.

## Current census conclusion

The Phase 15.5 runtime is no longer architecturally dependent on the retired application shell.

Remaining architecture debt is now concentrated in:

1. the shared Raid Map/EncounterBoard global installer composition;
2. compatibility/migration code intentionally retained for old user data;
3. the quarantined retired application cluster and its historical tests/tools;
4. obsolete naming on otherwise-current helpers, to be promoted to neutral shared-core names as
   encountered.

The first obsolete-name promotion is complete: Rotation now uses
`services.rotation_runtime_service.RotationRuntimeService`, while the Phase 14-named module is
only a compatibility shim.


## Retirement-prep test migration

Current/shared guarantees have begun moving away from retired-shell test fixtures.

Completed:

- `ui/tests/test_phase155_settings_workspace.py` now exercises only
  `Phase15SettingsPage`; it no longer instantiates the retired `SettingsPage`.
- the rotation owned-page boundary assertion now expects the neutral
  `RotationRuntimeService` authority used by the shared Rotation workspace.

Clearly retired-shell-oriented test families identified for later quarantine/removal include:

- `ui/tests/test_main_window_lazy_page_support.py`
- `ui/tests/test_operations_console_live_cards.py`
- `ui/tests/test_rotation_dashboard_main_window_route.py`
- Phase 14 shell/layout tests whose assertions are about retired page composition rather than
  current shared Rotation engine behavior
- `ui/tests/test_comp_brainstorm_page.py` where assertions are specifically about registration
  into the retired Raid Engine/MainWindow stack
- older Collectibles/Encounters tests whose subject is the retired page rather than canonical
  service behavior

Tests that must remain even though their names predate Phase 15.5 include shared subsystem tests such
as EncounterBoard packaging/accessibility/formations/GIF export and Rotation engine/evidence tests.
Those protect infrastructure still used by the current app.

**Retirement rule:** migrate useful shared assertions first; delete retired-shell-only tests only in
the same slice that removes their retired implementation family.


## Machine-enforced retirement quarantine

The retirement-prep boundary is now encoded in
`tools/phase155_retirement_manifest.py` instead of living only in this document.

The manifest distinguishes:

- retired UI modules that belong to the old application shell;
- tests whose subject is only that retired shell;
- old-looking tests that intentionally remain because they protect current shared subsystems.

`tools/tests/test_phase155_retirement_manifest.py` enforces that:

1. quarantine paths remain explicit and non-overlapping with retained shared examples;
2. current `ui/phase15*.py` pages do not import any retired UI module;
3. retained shared subsystem tests cannot be accidentally swept into the retired-shell bucket.

This is a preparation gate, not a deletion mechanism. The retired cluster remains in source until
the quarantine guard and focused runtime gate are green on the local Windows checkout.


## Guard correction: retired quick-entry helper

The first local quarantine run exposed
`ui.phase15_comp_brainstorm_quick_entry_support` importing the retired
`ui.comp_brainstorm_page`.

This helper is not part of the current `Phase15CompMakerPage` implementation. It is a monkey-patch
extension for the retired Comp Brainstorm page and is now classified with that retired compatibility
cluster.

The guard was also tightened conceptually: "current Phase 15.5 page" is now an explicit authority
list matching the actual current workflow surfaces, not a filename glob over every `phase15*.py`
helper. This keeps compatibility helpers visible without falsely treating them as native pages.


## Retired-cluster removal slice 1: Comp Brainstorm

Removed from `phase15.5` source:

- `ui.comp_brainstorm_page`
- `ui.phase15_comp_brainstorm_quick_entry_support`
- `ui/tests/test_comp_brainstorm_page.py`

The removed quick-entry helper was a monkey-patch extension of the retired Comp Brainstorm page; it
was not part of `Phase15CompMakerPage`.

Intentionally retained shared/current authorities include:

- `services.comp_brainstorm_draft_service`
- `services.comp_brainstorm_draft_build_service`
- `services.comp_brainstorm_quick_entry_service`
- `services.raid_plan_offensive_stats_service`
- `ui.phase15_comp_maker_page`

No user database or canonical ESO database migration/removal is part of this slice.


## Retired-cluster removal slice 2: application composition helper

Removed from `phase15.5` source:

- `ui.application_window_composition`
- `ui/tests/test_application_window_composition.py`

This helper composed presentation behavior onto the retired `MainWindow` instance after
construction. Current `app.py` constructs `Phase15RaidPlanWindow` directly and does not import
or call this composition layer.

The small helper modules formerly called by this composition file remain in source for independent
classification; they were not removed merely because their old caller was retired.


## Retired-cluster removal slice 3: Collections compatibility shim

Removed from `phase15.5` source:

- `ui.collections_page`

This file was an obsolete alias layer mapping the old `CollectionsPage` name to the retired
Achievements compatibility wrapper. Branch-local search found no remaining consumers.

The current Phase 15.5 Achievements and Collectibles routes continue to use
`ui.components.achievement_workspace` and `ui.components.collectible_workspace` directly through
their native wrappers/hub.


## Retired-cluster removal slice 4: MainWindow lazy-page / DD installer chain

Removed from `phase15.5` source:

- `ui.performance_dashboard_dd_support`
- `ui.main_window_lazy_page_support`
- `ui/tests/test_performance_dashboard_dd_support.py`
- `ui/tests/test_main_window_lazy_page_support.py`

The DD support module patched the retired Performance Dashboard and then installed the retired
MainWindow lazy-page materialization layer. Current `app.py` does not import that installer chain.

Lower-level DD analysis/services and related shared helpers remain in source for independent
classification; they were not removed merely because this retired presentation/bootstrap layer was.


## Retired-cluster removal slice 5: performance dashboard bootstrap / OperationsConsole focus

Removed from `phase15.5` source:

- `ui.application_performance_dashboard_bootstrap`
- `ui.operations_console_focus_support`
- `ui/tests/test_application_performance_dashboard_bootstrap.py`

The bootstrap existed to install an old MainWindow-era Performance Dashboard extension chain and an
OperationsConsole focus patch. Current `phase15.5` `app.py` does not import this bootstrap.

Underlying performance analysis/services and reusable dashboard helpers remain in source for
independent classification.


## Retired-cluster removal slice 6: OperationsConsole schedule/progression patches

Removed from `phase15.5` source:

- `ui.operations_console_schedule_support`
- `ui.phase5_operations_progression_support`

Both modules only patched methods onto the retired `OperationsConsole`. The durable authorities they
consumed remain intact:

- team schedules remain owned by `RosterService`;
- MinMax progression remains owned by `MinmaxCharacterProgressionAdapter`.

Current workspace-bootstrap and user-database-routing tests were retained, with only stale assertions
about the removed OperationsConsole schedule patch deleted.


## Retired-cluster removal slice 7: Collectibles profile installer

Removed from `phase15.5` source:

- `ui.collectibles_profile_support`

The current shared Collectibles workspace imports and constructs
`ProfiledCollectibleService` directly, so profile-aware storage no longer depends on the retired
installer. Tests now assert the current shared authority instead of the removed monkey-patch layer.

Profile migration and merge semantics remain covered at the service level.


## Retired-cluster removal slice 8: Encounters evidence presentation chain

Removed from `phase15.5` source:

- `ui.encounters_evidence_guide_support`
- `ui.encounter_identity_correction_support`
- `ui/tests/test_encounters_evidence_guide_support.py`
- `ui/tests/test_encounters_overview_evidence_support.py`

These modules existed to project reviewed encounter evidence into the retired `EncountersPage`
surface and to install encounter identity filtering through that UI chain.

Durable encounter authorities remain intact and independently tested:

- `services.raid_encounter_identity_service`
- `services.encounter_guide_evidence_projection_service`
- current live-raid encounter projection services and their service tests.


## Retired-cluster removal slice 9: global UI safety installer

Removed from `phase15.5` source:

- `ui.application_ui_safety_support`

Current Phase 15.5 pages own their persistence/dirty-state boundaries directly. The retained safety
contract test now checks native `Phase15MapWorkshopPage` discard guards and
`Phase15RaidPlanWindow` close/flush behavior instead of the retired global monkey-patch installer.

Shared `ui.ui_safety` helpers remain intact.


## Retired-cluster removal slice 10: Settings decorator helpers

Removed from `phase15.5` source:

- `ui.encounter_research_support`
- `ui.icon_consistency`
- `ui/tests/test_icon_consistency.py`

Both helpers mutated the retired `SettingsPage` and are not installed by current Phase 15.5 startup.
The legacy `ui.settings_page` module itself remains temporarily because retired `MainWindow`
still imports it; it will be removed with that shell cluster.


## Retired-cluster removal slice 11: team prescription template decorator

Removed from `phase15.5` source:

- `ui.team_prescription_template_support`

This module decorated the retired `ui.optimization_page.OptimizationPage` and chained into the
already-retired roster-transfer helper. The underlying team-prescription services, template sources,
slot constraints, and generation logic remain intact.


## Retired-cluster removal slice 12: Phase 14 Optimization presentation shell

Removed from `phase15.5` source:

- `ui.team_optimization_phase14_shell_support`
- `tools/profile_team_optimization_startup.py`
- `tools/profile_team_optimization_legacy_baseline.py`
- `ui/tests/test_team_optimization_phase14_shell_support.py`
- `ui/tests/test_team_optimization_phase14_lazy_startup.py`

The retired Raid Engine dashboard installer was also updated to stop installing this shell.

Optimizer adviser/services and current `ui.phase15_optimization_page` remain intact.


## Retired-cluster removal slice 13: MainWindow Help registration

Removed from `phase15.5` source:

- `ui.help_support`
- `ui/tests/test_help_native_registration.py`

The retired `MainWindow` no longer installs that registration layer. Reusable help topic data and
the standalone Help page remain in source for future/native reuse.


## Retired-cluster removal slice 14: team prescription roster projection extraction

Added shared service authority:

- `services.team_prescription_roster_projection_service`

Removed retired UI wrapper:

- `ui.team_prescription_roster_transfer_support`

The deterministic prescription -> roster-draft projection and concise preview logic were moved out of
the old Qt/MainWindow patch layer into a pure service API with explicit prescription and roster-member
inputs. Existing service tests now target that authority directly.

The retired UI handoff/install code was removed after branch-local consumer checks.


## Retired-cluster removal slice 15: Raid Engine dashboard polish

Removed from `phase15.5` source:

- `ui.raid_engine_dashboard_polish_support`
- `ui/tests/test_raid_engine_dashboard_polish_support.py`

The retired Raid Engine dashboard hub no longer installs this polish layer, and its now-unused safe
rewire helper/import were removed from that hub as well.


## Retired-cluster removal slice 16: roster top-back presentation helper

Removed from `phase15.5` source:

- `ui.roster_top_back_control_support`

The retired Raid Engine dashboard hub no longer installs that helper. Broader roster and Urban
Wilderness tests were retained with only the obsolete back-control assertions removed.


## Retired-cluster removal slice 17: build screenshot-disable presentation patch

Removed from `phase15.5` source:

- `ui.build_screenshot_import_disable_support`
- `ui/tests/test_build_screenshot_import_disabled.py`

The retired Raid Engine dashboard had already stopped installing this monkey patch. The module only
hid and disabled the legacy `BuildsPage` screenshot-import button at runtime; it did not own OCR,
import parsing, canonical build persistence, or Phase 15.5 Builds behavior.

The obsolete presentation-only test was removed with the patch and both paths are now recorded in the
retirement manifest. No build data, user database state, OCR service, or canonical ESO data was
changed by this slice.


## Retired-cluster removal slice 18: Coverage Raid Plan scope adapter

Removed from `phase15.5` source:

- `ui.coverage_raid_plan_scope_support`
- `ui/tests/test_raid_plan_coverage_support.py`

The retired Raid Engine dashboard no longer installs the old Coverage monkey-patch layer.

Before removal, the useful guarantees were checked against native
`ui.phase15_coverage_page.Phase15CoveragePage`. The current page already owns:

- saved Raid Plan resolution through `RaidPlanRepository`;
- stage/context resolution through `RaidPlanContextCoverageRepository`;
- canonical saved-build scope composition through `RaidPlanCoverageScopeService`;
- named group-effect and unique-support-set overlays;
- reviewed planned-gear overlays;
- reviewed planned-skill/class overlays;
- explicit conditional/unresolved states that remain Needs Review instead of becoming false certainty.

A new current regression file, `ui/tests/test_phase155_coverage_authority.py`, protects those native
boundaries without depending on the retired `CoveragePage` or Raid Engine shell.

No build records, Raid Plans, Coverage provider rows, user database state, or ESO reference data were
deleted or migrated by this slice.


## Retired-cluster removal slice 19: Raid Engine dashboard registration hub

Removed from `phase15.5` source:

- `ui.raid_engine_dashboard_support`

The retired `application_team_optimization_bootstrap` no longer installs that hub. Current
`app.py` constructs `Phase15RaidPlanWindow` directly and does not call the old Team Optimization
bootstrap, so this registration layer is outside the Phase 15.5 startup path.

The underlying `ui.raid_engine_dashboard_page` was intentionally retained for now because its pure
chair normalization and readiness-score helpers still have independent tests. The test file was
retargeted away from MainWindow registration assertions so reusable logic is not discarded merely
because its old presentation shell is retired.

No Raid Plans, roster seats, readiness decisions, builds, or database records were changed by this
slice.


## Retired bootstrap graph quarantine

Current `phase15.5` `app.py` does not import or invoke the old workspace, Team Optimization, or
Extreme Optimization application bootstraps. It constructs `Phase15RaidPlanWindow` directly.

The following modules are therefore classified as retired application-composition authorities while
they remain temporarily in source for historical-test migration:

- `ui.application_workspace_bootstrap`
- `ui.application_team_optimization_bootstrap`
- `ui.application_extreme_optimization_bootstrap`

The following tests are now explicitly quarantined as retired-shell startup tests:

- `ui/tests/test_application_team_optimization_bootstrap.py`
- `ui/tests/test_application_extreme_optimization_bootstrap.py`
- `ui/tests/test_comp_builder_end_to_end_wiring.py`

This classification does **not** retire the underlying Comp, Extreme, Rotation, roster, gear, or
optimization services. Each underlying helper/service must still be independently classified or
migrated before deletion.


## Retired-cluster removal slice 20: Coverage capability-gap presentation patch

Removed from `phase15.5` source:

- `ui.coverage_capability_gap_visibility_support`

Its only branch-local consumer was the already-quarantined
`ui.application_workspace_bootstrap`. The module monkey-patched the retired
`ui.coverage_page.CoveragePage` to display capability-resolution gap text.

Canonical capability auditing remains intact through `SavedBuildCapabilityService` and the native
Phase 15.5 Coverage page continues to preserve unresolved/incomplete build evidence as Needs Review.

No Coverage provider data, builds, Raid Plans, or database records were changed.


## Retired-cluster removal slice 21: Coverage group-effect catalog decorator

Removed from `phase15.5` source:

- `ui.coverage_group_effect_catalog_support`
- `ui/tests/test_coverage_group_effect_catalog_support.py`
- `ui/tests/test_coverage_quick_notes_provider_sources.py`

The decorator only patched the retired `CoveragePage`. Native Phase 15.5 Coverage already composes
named group effects and unique support sets directly, while `KnownEffectSourcesService` owns the
human-readable source registry.

Useful guarantees remain covered by:

- `ui/tests/test_phase155_coverage_authority.py`
- `services/tests/test_known_effect_sources_service.py`
- `services/tests/test_known_effect_sources_major_savagery.py`
- provider-reference service tests for abilities, passives, and non-ability sources.

The underlying canonical provider-reference services, raid group-effect catalog, unique support-set
catalog, and capability services remain intact.

No user-owned or canonical database data was changed.


## Retired-cluster removal slice 22: Roster template-button cleanup patch

Removed from `phase15.5` source:

- `ui.roster_template_button_cleanup_support`

The module only hid `view_template_button` on the retired `ui.themed_roster_page.RosterPage`.
Its sole branch-local consumer was the already-quarantined Team Optimization bootstrap.

No roster service, team membership, generated roster data, build template data, or user database
state was changed.


## Retired-cluster removal slice 23: Comp Builder ESO Logs chair layout patch

Removed from `phase15.5` source:

- `ui.comp_builder_esologs_chair_layout`

The module only reordered the selected-chair and aggregate ESO Logs labels inside the retired
`CompBuilderPage`. Its sole branch-local consumer was the already-quarantined Team Optimization
bootstrap.

ESO Logs data services, trend/snapshot logic, candidate evidence, and current Phase 15.5 Top Gear
remain untouched.


## Retired-cluster removal slice 24: Comp Builder assignment cue presentation patch

Removed from `phase15.5` source:

- `ui.comp_builder_assignment_cue_support`
- `services/tests/test_comp_builder_assignment_cue.py`

The patch only decorated the retired Comp Builder with a selected-build/target-chair cue and
assignment accent properties. Candidate selection, duplicate-player guards, canonical assignment
callbacks, Comp planning state, and candidate scoring remain intact.

The surviving candidate-picker regression no longer asserts the retired cue placement.


## Retired-cluster removal slice 25: Comp Builder Rylo presentation skin

Removed from `phase15.5` source:

- `ui.comp_builder_rylo_support`

The module was a Phase 14/Rylo QSS decorator for the retired Comp Builder. It did not own
candidate ranking, composition-style policy, roster/build assignment, ESO Logs evidence, or
canonical planning state.

Rylo-specific presentation assertions were removed from the surviving candidate-picker,
workspace, and composition-style tests; their behavior/service assertions remain.


## Retired-cluster removal slice 26: Stickerbook and Gear Lookup bookmark UI decorators

Removed from `phase15.5` source:

- `ui.stickerbook_bookmark_support`
- `ui.gear_lookup_bookmark_support`
- `services/tests/test_gear_lookup_bookmark_support.py`

The removed modules only injected Phase 14 shortlist controls into legacy Stickerbook/Gear Lookup
pages through the quarantined Team Optimization bootstrap.

`services.stickerbook_bookmark_service.StickerbookBookmarkService` remains authoritative and its
profile-aware bookmark, toggle, note, and persistence regressions remain in place. User bookmark
storage was not altered by this retirement slice.


## Retired-cluster removal slice 27: Comp Builder team-progress and polish patches

Removed from `phase15.5` source:

- `ui.team_progress_support`
- `ui.comp_builder_polish_support`
- `services/tests/test_comp_builder_polish_support.py`

These two modules formed a retired presentation layer around the old Comp Builder's team-health tiles,
label wording, and candidate-display polish. Their coverage helpers were not consumed by current
Phase 15.5 pages.

Current Phase 15.5 Coverage remains authoritative for raid-plan/stage scope, known sources,
planned gear/skill overlays, unresolved evidence, and saved-build capability evidence.


## Retired-cluster removal slice 28: Comp Builder layout and main-controls patches

Removed from `phase15.5` source:

- `ui.comp_builder_layout_support`
- `ui.comp_builder_main_controls_support`

These modules only rearranged the retired Comp Builder into a two-column workspace, moved buttons,
renamed controls, and hid legacy presentation fields. They did not own candidate generation,
composition-style policy, trial mapping, ESO Logs evidence, or canonical Comp planning state.

Surviving trial-flow, ESO Logs snapshot, and composition-style tests now assert service behavior
and meaningful installer order without depending on the retired presentation choreography.


## Retired-cluster removal slice 29: Comp Builder send-feedback presentation patch

Removed from `phase15.5` source:

- `ui.comp_builder_send_feedback_support`
- `services/tests/test_comp_builder_send_feedback_support.py`

The module only added transient "Sending" / "Sent" UI feedback around the retired Comp Builder send
action. It did not own Raid Plan persistence, canonical Comp state, candidate application, or
generated-roster quarantine behavior.

Candidate-application regressions remain and now test the actual send/persistence ownership without
depending on the retired feedback wrapper.


## Retired-cluster removal slice 30: stale Phase 14 startup contract tests

Removed from `phase15.5` tests:

- `ui/tests/test_application_team_optimization_bootstrap.py`
- `ui/tests/test_application_extreme_optimization_bootstrap.py`
- `ui/tests/test_comp_builder_end_to_end_wiring.py`

These tests asserted the retired `MainWindow` bootstrap order and old Comp Builder route/composition
contracts. Current Phase 15.5 starts directly through `Phase15RaidPlanWindow`, so keeping those
tests would protect a startup path the product no longer uses.

The underlying Team Optimization, Extreme Engine, Comp candidate, provider-workload, and ESO Logs
services remain in place for explicit migration into current Phase 15.5 surfaces.


## Retired-cluster removal slice 31: MainWindow rotation route test

Removed from `phase15.5` tests:

- `ui/tests/test_rotation_dashboard_main_window_route.py`

The deleted test only verified the retired `MainWindow` route to the retired Phase 14 rotation page.
Current Phase 15.5 uses the native Phase 15 Rotations page while retaining the shared rotation
runtime/service authority.


## Retired-cluster removal slice 32: Phase 14 build inspector title-style test

Removed from `phase15.5` tests:

- `ui/tests/test_phase14_build_inspector_title_style.py`

The test only asserted a presentation property on the retired Phase 14 build inspector. Native
Phase 15.5 Builds does not import that inspector support, so this test no longer protects a current
product surface.


## Retired-cluster removal slice 33: Phase 14 Comp Builder shell tests

Removed from `phase15.5` tests:

- `ui/tests/test_comp_builder_phase14_shell_support.py`
- `ui/tests/test_comp_builder_phase14_team_health.py`

These tests primarily protected the quarantined Phase 14 Comp Builder presentation shell and its
legacy route choreography. The meaningful rules they overlapped with remain covered by canonical
Comp state, health, autofill, candidate-application, persistence, planned-gear coverage, and
readiness service tests.

The Phase 14 shell module itself remains quarantined for now because it still contains migration-era
behavior that must be extracted deliberately before source removal.


## Retired-cluster removal slice 34: Operations Console test

Removed:

- `ui/tests/test_operations_console_live_cards.py`

The test covered the retired Operations Console UI. Current Coverage and health service tests still
protect evidence-state handling, and readiness remains service/model owned.


## Retired-cluster removal slice 35: Phase 14 build lifecycle guard test

Removed:

- `ui/tests/test_phase14_build_lifecycle_guard_support.py`

The test only protected repair behavior for the retired themed Phase 14 Builds page. Native Phase
15.5 Builds does not import the Phase 14 lifecycle guard or themed Builds UI chain.


## Retired-cluster removal slice 36: shared icon contract extraction

Added current Phase 15.5 coverage:

- `ui/tests/test_phase155_shared_icon_contract.py`

Removed retired shell coverage:

- `ui/tests/test_phase14_visual_target_support.py`

Reusable semantic-icon guarantees were moved into the current shared test before the Phase 14
visual-target test was retired. The remaining deleted assertions only described the old Phase 14
Builds/Rotations presentation chain.


## Retired-cluster removal slice 37: Phase 14 command-center presentation test

Removed:

- `ui/tests/test_phase14_command_center_support.py`

This omnibus test targeted the retired Phase 14 Builds/Rotations presentation chain. Dedicated tests
remain for any support modules that still matter independently, while current Phase 15.5 Builds
uses its native page.


## Retirement manifest completion invariant

The pending retired-shell test bucket may now be empty. The manifest regression continues to require
that removed tests are absent, shared examples exist, and all retirement/shared buckets remain
disjoint.


## Retired-cluster removal slice 38: Team Optimization application bootstrap

Removed from `phase15.5` source:

- `ui/application_team_optimization_bootstrap.py`

Current `app.py` does not import or invoke this bootstrap. Surviving tests were detached from its
installer-order choreography while retaining direct behavior coverage for constraints, candidate
selection, ESO Logs snapshots, strategy, provider workload, saved rotations, and canonical Comp
state.

The underlying services/support modules were not bulk-deleted; they remain available for explicit
migration into current Phase 15.5 surfaces.


## Retired-cluster removal slice 39: Extreme Optimization application bootstrap

Removed from `phase15.5` source:

- `ui/application_extreme_optimization_bootstrap.py`

Current `app.py` does not import or invoke this bootstrap. The three recovery-record tests were
detached from installer-order assertions while retaining direct record-support coverage. Extreme
engine/services and record support modules remain intact.


## Retired-cluster removal slice 40: Workspace application bootstrap

Removed from `phase15.5` source:

- `ui/application_workspace_bootstrap.py`

Removed obsolete composition test:

- `ui/tests/test_application_workspace_bootstrap.py`

Current `app.py` does not import or invoke the legacy Workspace bootstrap. Surviving Roster,
import, assignment, Builds, and Rotation tests were detached from installer-order choreography
while retaining their direct behavior coverage.

The old startup call to `merge_duplicate_roster_players(...)` was deliberately **not** migrated
into native Phase 15.5 startup. That service can delete redundant Personnel rows after moving
related state, so it remains an explicit repair operation rather than an automatic launch side
effect. The user database was not mutated by this source-retirement slice.


## Retired-cluster removal slice 41: Phase 14 build lifecycle guard

Removed from `phase15.5` source:

- `ui/phase14_build_lifecycle_guard_support.py`

After Workspace bootstrap retirement, this presentation-only Qt repair layer had no current
Phase 15.5 consumer. It touched no build data or database state. The native Phase 15.5 Builds page
does not import the Phase 14 command-center/themed Builds lifecycle chain.


## Retired-cluster removal slice 42: Phase 14 build visual-return pair

Removed from `phase15.5` source:

- `ui/phase14_build_visual_target_support.py`
- `ui/phase14_build_edit_return_support.py`

Both modules were presentation/navigation wrappers for the retired themed Phase 14 Builds shell.
Neither owned canonical build persistence or database state, and no current Phase 15.5 consumer
remained after Workspace bootstrap retirement.


## Retired-cluster removal slice 43: Phase 14 build icon polish installer

Removed from `phase15.5` source:

- `ui/phase14_build_icon_polish_support.py`

The only live dependency was its skill-row rendering helper from
`ui/phase14_build_focused_editors_support.py`. That helper was internalized there before the
installer was removed, preserving the existing ability-icon lookup and row rendering behavior.


## Retired-cluster removal slice 44: Phase 14 Builds UI cluster

Removed from `phase15.5` source:

- `ui/phase14_build_focused_editors_support.py`
- `ui/phase14_build_inspector_support.py`
- `ui/phase14_build_profile_support.py`
- `ui/phase14_builds_command_center_support.py`

These modules formed an isolated legacy Builds presentation cluster after Workspace bootstrap
retirement. Phase 14-only source-contract assertions were removed from surviving tests first.

Preserved:
- canonical Build persistence and services;
- `BuildProfileService` and build-profile data;
- character progression services;
- rotation artifact services;
- native Phase 15.5 Builds;
- native player/build navigation tests.


## Retired-cluster removal slice 45: legacy Builds rotation artifact viewer

Removed from `phase15.5` source:

- `ui/build_rotation_artifact_support.py`

This module only injected a saved-Rotation viewer tab into the retired themed Builds workspace.
The durable authority remains `services/build_rotation_artifact_service.py`, including atomic
artifact persistence, scoped rotations, canonical build-id resolution, and RotationPlan restoration.


## Retired-cluster removal slice 46: obsolete Rylo theme layer

Removed from `phase15.5` source:

- `ui/rylo_build_surface_theme_refresh.py`
- `ui/rylo_surface_icon_fix.py`

Removed eight tests that exclusively protected that retired theme/monkey-patch layer. Current
`app.py`, `Phase15RaidPlanWindow`, and native Phase 15.5 Builds do not import either module.
Urban Wilderness/native Phase 15.5 palette assets remain intact.


## Retired-cluster removal slice 47: legacy inline Builds editor compatibility island

Removed from `phase15.5` source:

- `ui/build_editor_inline_compat.py`
- `ui/build_editor_performance.py`
- `ui/build_workspace_edit_fix.py`

Removed three tests that exclusively protected those retired UI monkey patches. The useful
standalone scribing simulator/navigation coverage in
`ui/tests/test_scribing_character_builder_support.py` was preserved; only its old permanent
Build-workspace source-contract assertion was removed.

Native Phase 15.5 Builds, canonical build persistence, character progression, U51 scribing
services, and user-owned build state remain intact.


## Retired-cluster removal slice 48: themed Builds wrapper

Removed from `phase15.5` source:

- `ui/themed_builds_page.py`

Its only live source consumer was the already-retired `ui/main_window.py`. The surviving
build-delete test now covers `phase5_build_delete_support` directly instead of the wrapper
composition. Native Phase 15.5 Builds remains independent.


## Retired-cluster removal slice 49: build creation/progression wrappers

Removed from `phase15.5` source:

- `ui/phase14_build_creation_bridge.py`
- `ui/build_progression_scroll_fix.py`

Removed two tests that exclusively protected the old embedded progression/startup ordering. Preserved
the compact progression bulk-purchase behavior and progression readiness helper/tests.

These wrappers only patched the retired `ui/builds_page.py` workspace and are not used by native
Phase 15.5 Builds.


## Retired-cluster removal slice 50: scribing editor compatibility adapter

Removed from `phase15.5` source:

- `ui/scribing_editor_compat.py`

The stable synthetic-ID/texture helper used by live scribing simulation was internalized into
`ui/scribing_simulator_support.py` first. The removed adapter only patched the retired
`BuildsPage._editor` factory.


## Retired-cluster removal slice 51: legacy Builds screenshot import UI

Removed from `phase15.5` source:

- `ui/build_screenshot_import_support.py`

This module only staged screenshots through the retired `BuildsPage` UI. The reusable
`BuildScreenshotImportService` remains intact for any future native Phase 15.5 review-first
screenshot intake flow.


## Retired-cluster removal slice 52: build reuse/searchable selector UI

Removed from `phase15.5` source:

- `ui/build_reuse_template_support.py`
- `ui/components/searchable_build_selectors.py`

The durable `BuildReuseService` remains intact and independently covered by service tests,
including template and migration behavior. The removed modules only patched the retired Builds UI.


## Retired-cluster removal slice 53: legacy Easy Mode build creation shell

Removed from `phase15.5` source:

- `ui/character_creation_easy_mode_support.py`

Before retirement, native `ui/phase15_builds_page.py` gained a `New Saved Build` action backed
by `CharacterCreationService`. The native path preserves available Personnel player/character
IDs, saves through canonical BuildService, and requires verified read-back with a stable BuildId.

Preserved:
- `CharacterCreationService`;
- canonical Build identity generation/merge behavior;
- Phase 5 build actions unrelated to the retired Easy Mode shell.


## Retired-cluster removal slice 54: legacy BuildEditor context variant adapter

Removed from `phase15.5` source:

- `ui/build_context_variant_support.py`

Removed presentation/source-contract tests that only protected the retired BuildEditor adapter,
while preserving mixed lifecycle and user-database tests for surviving behavior.

Durable Context Variant semantics remain in:
- `models.build_model.BuildContextVariant`;
- `services/build_context_variant_service.py`;
- native `ui/phase15_builds_page.py`;
- service/model/rotation/export/reuse tests.


## Retired-cluster removal slice 55: legacy scribing installer pair

Removed from `phase15.5` source:

- `ui/scribing_support.py`
- `ui/scribing_simulator_support.py`

The native Phase 15.5 Builds page already uses `ui/components/scribing_dialogs.py` directly.
Model recipe tests now import `_recipes_for` / `_store_recipes` from that shared component.

Preserved:
- `models.scribing_recipe`;
- PlayerBuild scribing serialization;
- U51 scribing catalog/service/icon behavior;
- native Phase 15.5 scribing dialogs.


## Retired-cluster removal slice 56: extracted Phase 5 Builds UI installer

Removed from `phase15.5` source:

- `ui/phase5_build_ui_support.py`

Reusable progression behavior was first extracted to
`ui/character_progression_support.py`, and native `ui/phase15_builds_page.py`
now exposes Character Progression directly with canonical save/read-back verification.

Preserved:
- Character Progression dialog and helpers;
- racial/passive filtering behavior;
- compact progression cards;
- endgame gear helper behavior;
- `CharacterProgressionService`.


## Retired-cluster removal slice 57: neutralize racial progression filter

Retired old Phase 5 names:

- `ui/phase5_racial_filter_fix.py`
- `minmax/tests/test_phase5_generic_racial_filter.py`

Replaced by:

- `ui/character_progression_racial_filter_support.py`
- `minmax/tests/test_character_progression_racial_filter.py`

Native Phase 15.5 Builds now installs the neutral racial progression filter before opening the
Character Progression dialog.


## Retired-cluster removal slice 58: Builds tab layout patch

Removed from `phase15.5` source:

- `ui/build_workspace_tab_layout_fix.py`

The shared rounded tab geometry was moved into the Urban Wilderness theme stylesheet first.
The remaining Builds-specific tab relabel/reordering behavior belonged only to the retired
legacy Builds workspace.


## Retired-cluster removal slice 59: native progression readiness

Removed from `phase15.5` source:

- `ui/build_progression_readiness_support.py`

Neutral readiness text/calculation now lives in
`ui/character_progression_readiness_support.py`, and native
`ui/phase15_builds_page.py` displays canonical Magicka/Stamina rotation-cost readiness directly.


## Retired-cluster removal slice 60: native roster-import variant verification

Removed from `phase15.5` source:

- `ui/roster_import_variant_persistence_guard_support.py`

`ui/roster_import_workflow.apply_roster_import()` now performs Context Variant verification
directly after canonical Build save, repairs reviewed variants if needed, and requires canonical
read-back after repair. The old legacy Builds sidebar-label patch was not migrated.


## Retired-cluster removal slice 61: legacy Builds page

Removed from `phase15.5` source:

- `ui/builds_page.py`

Before removal, the remaining behavior-bearing dependencies were migrated:
- fresh Saved Build creation -> native `ui/phase15_builds_page.py`;
- Character Progression -> neutral progression support + native Phase 15.5 action;
- rotation-cost progression readiness -> native Phase 15.5 preview;
- Context Variant import verification -> `ui/roster_import_workflow.py`;
- shared tab geometry -> Urban Wilderness theme;
- scribing -> shared `ui/components/scribing_dialogs.py`.

Native `ui/phase15_builds_page.py` is now the sole Builds page in the Phase 15.5 product line.


## Retired-cluster removal slice 62: legacy MainWindow shell

Removed from `phase15.5` source:

- `ui/main_window.py`

Before removal, surviving safety, roster, raid-plan, comp-state, and workflow tests were detached
from obsolete MainWindow source choreography or migrated to the native
`ui/phase15_raid_plan_window.py` contract.

Current `app.py` already launches `Phase15RaidPlanWindow` directly. The old shell no longer
has any live Phase 15.5 consumer.
