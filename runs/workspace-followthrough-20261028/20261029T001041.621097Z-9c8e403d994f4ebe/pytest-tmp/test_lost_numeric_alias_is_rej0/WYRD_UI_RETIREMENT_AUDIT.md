# Wyrdworks: UI/theme retirement audit

**Status:** preliminary source audit, 2026-10-15. No files approved for deletion yet.

## Repository and safety
- Repository: `Jarakeen/Wyrdworks` (renamed from `Jarakeen/BFF`).
- Working cleanup branch: `wyrd`. Historical checkpoint: `archive/pre-wyrdworks-consolidation-2026-10-15`.
- The checked-in branch is an older Urban Wilderness implementation. The newer Granite/Wyrdworks UI files previously supplied separately may not be committed. **Never overwrite local newer files with older branch sources.**
- Do not reset or replace `data/eso.db` or `user_data/foundrydock.db`. Git branches are not database backups.

## Verified source-level startup chain
```text
app.py
  -> ui.theme.ThemeManager().apply(app)
      -> load_grimoire_stylesheet() + URBAN_WILDERNESS_OVERRIDES
      -> QApplication.setStyleSheet(...)
  -> ui.phase15_raid_plan_window.Phase15RaidPlanWindow
      -> ui.phase15_raid_plan_workspace.Phase15RaidPlanWorkspace
          -> ui.phase15_raid_plan_page.Phase15RaidPlanPage (persistence inherited)
      -> ui.phase15_side_nav.Phase15SideNav
      -> other pages lazy-loaded on navigation
```
The remote `wyrd` tree does not currently contain `ui/granite_theme.py`; the latest Granite implementation must be reconciled from the local working tree. This is a static trace, not proof of effective Qt styling.

## Keep / park / inspect
| Module or group | Decision | Reason |
|---|---|---|
| `app.py` | KEEP | Active entrypoint, theme invocation |
| `ui/theme/theme_manager.py`, `ui/theme/colors.py` | KEEP / CONSOLIDATE | Central API, currently stacks Grimoire and Urban Wilderness |
| `ui/phase15_raid_plan_window.py` | KEEP | Native shell and lazy routes |
| `ui/phase15_raid_plan_workspace.py` | KEEP / CONSOLIDATE STYLING | Active landing page, also defines page QSS |
| `ui/phase15_raid_plan_page.py` | KEEP | Workspace imports/inherits persistence from it |
| `ui/phase15_side_nav.py` | KEEP / CONSOLIDATE STYLING | Instantiated by native window, owns its own QSS |
| `ui/components/raid_map_workspace.py` | KEEP | Shared map board composition and strict workspace paths |
| `ui/components/encounter_board.py` | KEEP | Shared tactical board implementation and viewport painting |
| `ui/phase15_map_workshop_page.py` | KEEP | Plan-independent map authoring; not a redundant Strategy page |
| Pages hidden by `HIDDEN_ROUTES` | PARK | Hidden route does not mean unused dependencies or data |
| `old_pages/` / archived implementations | CANDIDATES ONLY | Need import, packaging, migration and test evidence before deletion |
| `phase155-runtime-*/` scratch copies | REVIEW LOCAL ONLY | Inflated Theme Detective counts; their on-disk status is not established by GitHub branch |

## Confirmed styling fragmentation
1. `ui/theme/theme_manager.py` applies global Grimoire plus Urban Wilderness QSS.
2. `ui/phase15_raid_plan_workspace.py` applies generic `QWidget`, `QFrame` and button styles.
3. `ui/phase15_side_nav.py` separately applies sidebar and control QSS.
4. `ui/phase15_map_workshop_page.py` separately applies map-editor QSS.
5. `ui/components/encounter_board.py` directly sets a dark viewport background brush.

These are ownership findings, not proof that a particular selector won at runtime.

## Map default concern
`ui/components/raid_map_workspace.py::blank_map_layout` currently sets `background_map` to an empty string. Review it alongside EncounterBoard initialization and preview fallback logic before setting `assets/raid_maps/built_in/midnight_astrolabe.webp` as the blank-map default. **Never replace a saved/custom map background or markers.**

## Next evidence gates
1. In the Windows checkout: inspect `git status --short`, current branch, and divergence before switching to `wyrd`.
2. Run the existing `tools/audit_phase155_dependencies.py` and `tools/audit_system_architecture.py` against the real working tree; isolate temporary `phase155-runtime-*` directories from UI theme reports.
3. Reconcile the newer Granite theme files with the current remote baseline without overwriting either.
4. Produce an import/caller, package-manifest and regression-test witness for each proposed deletion.
5. Consolidate visual styling centrally and validate real Qt screenshots, startup, page navigation and saved-state integrity.

Reference: `AGENTS.md`, `CLAUDE.md`, `SYSTEM_ARCHITECTURE_RULES.md`, `DEVELOPMENT_STANDARD.md`, `PHASE155_DEPENDENCY_CENSUS.md`.
