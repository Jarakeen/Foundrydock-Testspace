## Current UI scope — 2026-10-26

Raid Plan is the only active raid-planning UI, with Teams, Map, and Readiness columns. Kill & Pull Order belongs to its Readiness workflow and existing stage assignment persistence. Live Raid and the other parked interfaces retain their code, tests, services, and data; their historical entries below do not reopen their UI or require page acceptance. Supporting editors and Map Workshop serve Raid Plan through canonical owners.

## 2026-10-28 — Stage-specific team and build details

Raid Plan's Teams panel, selected-build summary, roster review and Readiness role/loadout counts now use the selected stage's saved member overrides through the shared context resolver. Explicitly cleared stage builds remain clear. Saving plan notes retains General's members and the separate stage overrides. Invalid saved stage details show an unavailable message instead of presenting General as the selected stage's evidence.

## 2026-10-25 — Existing runner evidence export

- The existing scheduled runner's local evidence exporter tolerates slow Git object reads with a bounded 120-second timeout and one retry; exhausted timeouts preserve the previous handoff archive and prompt.
- Optional clean-revision Extreme receipts can be bundled with exact-commit source and their original pass/fail status. Scheduled polls and baseline/full results keep their own provenance. Named export output preserves previous handoff artifacts; no scheduled task or polling configuration changes.

## 2026-10-23 — Local tools hub for engine and ESO Logs work

## 2026-10-25 — Calibrated movement review in Map Workshop

- The observed-movement viewer can load a working map calibration and animate the original tracks over its image through the existing route projection. Profiles bind the exact replay content and artwork hash/dimensions; wrong or changed inputs are rejected. Clearing the profile or opening another replay restores unscaled coordinates.
- A Workshop map may retain its paired movement and calibration. **Review ESO Logs Movement** opens these together from the selected map. Duplication and version-2 `.fdmap` packages preserve them; ordinary version-1 packages remain supported. Rejected calibration falls back to unscaled review without modifying a saved map or plan.
- Current Banner Bearer-derived metre scales are empirical estimates, not surveyed walls or independently certified artwork orientation. They do not authorize automatic support reach/delivery verdicts. Observed NPC markers are separate reference copies; airborne/off-platform observations must not define arena floor bounds.


## 2026-10-25 — Paginated log intake and movement review

- Local Engine Lab accepts a downloaded report directory as `--log`, reading one fight at a time through the existing raw importer. Missing pages, incomplete cursors and mismatched event identities are rejected. Reports retain source digests and emit the existing Map Workshop movement bundle.
- Reports include friendly non-self heal/buff delivery counts and paired resource-coordinate separation when available. These are unscaled observed separations, not maximum ability ranges or proof of recipient eligibility.
- The observed movement viewer offers an explicit **Focus central positions** toggle. It fits the central 98% of samples on each axis, states how many samples lie outside the view, and preserves every original observation. Switching it off restores the full extent. This is viewport control, not arena calibration.


- `python tools/engine_lab_ui.py` opens a standalone Wyrdworks tools window. It can run the existing local Combat, Encounter, Extreme, quality, or full validation suites; download selected ESO Logs fights with the already-configured client; analyze a saved raw export; and create Map Workshop movement evidence.
- With a log selected, **Run Selected Work** can save a repeatable engine-growth case under `validation_reports/engine_growth_cases/<source-sha256>/`. Each run records exact code revision, local working-tree state, suite receipts, fight observations and movement bundles. The source log remains where the user saved it; case reports omit player/account/server names and retain only explicit class/race/build fields, gear, talents, stats, combat summaries and raw movement coordinates when present.
- These cases are a local evidence corpus, not automatic engine training. They do not update mechanics or saved characters, and do not claim modeled-versus-observed agreement. Unknown source fields remain unknown; tests use the existing validation runner against the selected code, independently of the fight.
- The tools shelf links to Map Workshop for map-image calibration and movement review, runs the existing procedural slate baker to a user-selected new PNG without overwriting, and runs RAVEN's asset inventory in dry-run mode. The asset action inventories; it does not stage conversions or rewrite references.
- Log observations remain distinct from engine regression tests. This utility does not compare simulated output to a fight or create team advice; those remain future work. Ordinary reports are under `validation_reports/engine_lab_ui/`; growth cases use the separate case library above; a texture is saved to the explicit path selected by the user.

## 2026-10-23 — BTVTools evidence attachment to growth cases

- The local tools hub can optionally attach a structured, screenshot-derived BTVTools benchmark JSON corpus to an anonymized ESO Logs growth case. The existing BTV benchmark service validates encounter/effect scope and uptime ratios; the case retains a source hash, denominator basis, ratios and role/page scope while omitting free-text notes and source paths.
- This makes BTV evidence reusable beside observed log/build/movement evidence. It does not import screenshots or OCR them, infer missing values, turn calibration evidence into canonical mechanics, or automatically train/update an engine. BTV screenshot insights currently enter through the existing JSON fixture contract.

## 2026-10-23 — Collectibles release artwork continuity

- Release packaging includes the active champagne Collectibles image and atlas metadata, preserving the same category artwork used by source runs. Category identities and completion data are unchanged.
- Source-to-package Qt image comparison covers all mapped categories. This is asset inclusion evidence, not an installed EXE certification.

## 2026-10-23 — Encounter reference database routing

- Encounter reads for the application data root honor the existing external ESO database setting while keeping boss JSON and evidence packets in their declared resource directories. Explicit fixture/research roots retain their own database scope.
- Canonical fact and mechanic reads open SQLite in read-only mode. A missing configured external database fails explicitly rather than falling back to a stale local database or creating a new one.
- This does not establish that an external corpus is current or complete; validation receipts must identify its provenance separately.

## 2026-10-22 — Raid Plan module draft and apply continuity

- Builds has **Save Draft** and **Apply to Raid Plan** beside Save Build. Drafts retain the complete editor snapshot under exact plan/stage/seat/build IDs. Apply commits the existing reusable Saved Build and the General or exact stage seat selection together; other plans referencing that Saved Build receive its build changes. Character/player ownership and richer imported fields are preserved.
- Crit/Pen from Raid Plan and Builds saves/restores structured calculator inputs, resistance targets, notes and result/evidence snapshots by exact plan/stage/seat/metric/channel. Drafts remain separate from applied planning decisions. Calculator Apply records a scenario, never equips gear or promotes a manual contribution to verified mechanics. Changed calculation inputs retain historical results for review.
- Both the Assignments page and Raid Plan's compact mechanic dialog can save a separate draft and explicitly apply it. Hidden jobs, support/timing notes and kill/pull priorities remain in the existing canonical stage record. Coverage's active owner dialog likewise retains source/condition drafts by exact plan/stage/effect/seat before applying ownership.
- Stale plan, calculation-context, applied-assignment and draft snapshots reject overwrites. Failures retain editor state; build/plan application is transactional. The plan save clock includes committed module drafts and stage records, using one shared display format.
- Validation uses disposable databases and Qt action/reopen witnesses. This entry describes source behavior, not an installed Windows release or exhaustive manual acceptance. Detailed results and limits are in `RAID_PLAN_SAVE_CONTINUITY_VALIDATION.md`.

## 2026-10-21 — Correct Lokke in-game House Stack numbering and healer sides

- User compared live CrutchAlerts in-game markers with the calibrated map: ground positions on the **right image column bottom-to-top are 1–4** (Brainiac, Pippin, Jaded, N1nja), then **left image column bottom-to-top 5–8** (xClusx, Tunz, Cobble, Aces). Upper healer is **RH**, lower healer is **LH**, opposite the previous raw source label display.
- Added the explicit immutable reference-projection mapping in `services/lokke_house_stack_labels.py`: raw marker 8→ground 1, 5→2, 4→3, 1→4, 7→5, 6→6, 3→7, 2→8; raw LH→display RH and raw RH→display LH. The UI displays both the ground number and the assigned player's name at the already-calibrated anchor.
- **Do not silently reinterpret existing persisted `RaidPlanMember.house_stack_position` values.** The currently saved positional assignment association remains keyed to raw source marker IDs so the currently visible team names stay at their physical anchors. Align persistent assignment editor/database semantics with ground numbers only in an explicit separately-reviewed migration.
- No changes to calibration numbers, physical XYZ source markers, replay, map images, or user databases. Added regression tests for the observed arrangement. Windows GUI visual acceptance not yet run.

## 2026-10-21 — Named CrutchAlerts House Stack positions on the Raid Plan map

- The existing **House Stacks** checkbox shows/hides **larger CrutchAlerts anchor markers (28px nominal)** with readable per-player name labels, using a dark-backed Segoe UI label for contrast against snowy artwork. No new checkbox, second map or scroll surface.
- The source of truth for each DD's position is the canonical `RaidPlanMember.house_stack_position` (falling back to DD seat number for Auto), resolved through `RaidPlanEffectiveContextService` for `boss:lokkestiiz`. This honors boss-stage position swaps rather than assuming seat order; player labels use gamertag first, character name second, then an explicitly unassigned DD seat label.
- Overlay remains **read-only**: CrutchAlerts source marker XYZ, Likke background, saved Raid Plans, observed ESO Logs replay and physical calibration unchanged. These names are planned member assignments, **not** identity matches inferred from ESO Logs actor IDs.
- Added regression tests for positional swap projection, unassigned labels, boss-context projection and House Stacks visibility. Windows rendering/pytest acceptance remains **pending**.

## 2026-10-21 — Fix invisible Lokke ESO Logs actors in editable Raid Plan map

- Reported screenshot: ESO Logs layer checked over saved Likke arena, but players invisible. Root cause: the transient overlay was attached to the raster preview scene, while the visible InlineRaidMap had switched into its editable `board.view` scene (as shown by the editor tool rail).
- Active-layer attachment now resolves the **current visible canvas**: edited board background item for the live editor, preview pixmap only for the raster preview. InlineRaidMap notifies the Raid Plan page after entering/reloading the editor so transient layers reattach without checkpoint/save.
- Initial Fight 22 display now starts at 1000 ms, after the first observed actor samples rather than showing a blank zero-time frame; user may still scrub back to zero.
- Added source regressions for active-scene attachment, editor reattachment, first visible frame and map persistence isolation. Source code committed; pytest and Windows GUI re-check **not executed in this environment**.

## 2026-10-21 — Lokke calibrated ESO Logs / House Stacks as real Raid Plan layers (implementation, acceptance pending)

- Committed the user-reviewed `Lokke arena with cliffs` alignment as source-controlled, read-only reference metadata (ESO Logs 2.01 px/log unit; CrutchAlerts 21.25 px/m) without modifying the original Likke Map Library item or any saved Raid Plan.
- Added a shared transient graphics renderer for positions and paths on existing map art. The active Raid Plan viewport exposes ESO Logs / House Stacks visibility, Fight 22/37/54, Play/Pause, scrub and validated optional replay import; the old separate below-map replay button is hidden. The existing **Hide Layer** menu includes reference visibility.
- Encounters can show the same overlay over a matching saved Likke Workshop preview. Reference data never becomes planned paths or editable map objects.
- Regression tests added for source alignment values, shared UI integration and immutable optional pack imports. **Tests, frozen asset inclusion, map selection under differing local libraries and Windows UI geometry have not been verified yet**.

## 2026-10-21 — ESO Logs replay: calmer movement on Raid Plan and Encounters

- Shared `EncounterReferenceReplay` now displays a **short-gap linear interpolation** between consecutive observed positions when samples are at most 750ms apart and movement speed is within a conservative 120 log-units/second display guard. This is **visual smoothing only**, not a new observation or accepted route, and original samples remain intact.
- Large jumps and gaps are **not** interpolated. Trails are reduced from 6 seconds to 3 seconds, made subtler, and exclude segments that fail those same timing/speed checks.
- This affects both the active Raid Plan and Encounters consumers because they reuse `ui/components/encounter_reference_replay.py`; no saved maps, player assignments or Raid Plan data change.
- Added isolated regression tests for interpolation, missing observations, large jumps, and unchanged raw samples. Windows GUI/pytest witness **still pending**, as is installing the optional replay data pack in the running app.

## 2026-10-21 — Lokke HM CrutchAlerts source anchors and read-only Strategy reference control (partial)

- Imported exactly **20 CrutchAlerts v2.27.0 source anchors** from `icons/WorldIcons.lua` (10 standard two-healer, 10 solo-healer). Each marker preserves raw XYZ and validated planar coordinates in metres, with a distinct `formation_id`. This does not prove player-to-marker assignment or artwork alignment.
- Added read-only **Encounter Reference** action on Strategy / Raid Map, scoped to current boss. It displays available markers/variants and evidence; does not redraw a map, save a plan, or change a user-owned map. Development source manifest must be present at the resource path; packaged runtime inclusion remains to be checked.
- Added focused marker-shape, XYZ-consistency and formation regression tests; Windows execution **not yet performed**. Original snowy west-boss arena artwork was optimized as a separate WebP conversation artifact and is **not committed/bundled** via the GitHub text-file connector.
- Still pending: actual layered reference overlay, verified image/world transform, packaged-art integration, Encounters/Raid Plan wiring and full Windows/RAVEN/FORGE acceptance.

## 2026-10-21 — Sunspire UESP boss pins in encounter spatial references (data foundation only)

- Added evidence-qualified `WorldMapAnchor` supporting strictly normalized map X/Y, positive UESP location ID, map identity and source citation. The read-only Map Workshop, Encounter Guide and Raid Plan projections now include this optional map pin, without rewriting any saved map or plan.
- Recorded three user-supplied UESP ESO Gamemap screenshots: Lokkestiiz location 144139 at (0.586, 0.588), Yolnahkriin 144149 at (0.408, 0.614), Nahviintaas 144162 at (0.517, 0.511). Added separate Yolnahkriin and Nahviintaas reference JSONs; no encounter-local scale or mechanics inferred for those bosses.
- Expanded regression tests for source validation, out-of-range/nonfinite normalized coordinates and the three bundled anchor records. Test execution and actual UI hookup **remain pending**. No database or saved user map modified.

## 2026-10-21 — Reusable trial-boss spatial reference foundation (partial; no UI wiring yet)

- Added strict Pydantic spatial reference schema and read-only projections for Map Workshop, Encounter Guide and Raid Plan in `services/encounter_spatial_reference.py`. It keeps observed combat movement, source-labelled world markers, provisional calibration, phase aliases, optional artwork and team-authored strategy separately identified; it does not save any map, timeline, assignment or plan.
- Indexed the owner in the encounter service catalog and added `tools/validate_encounter_spatial_reference.py` for read-only validation of boss manifest files.
- Added example `data/encounter_spatial_references/sunspire_lokkestiiz_hm.json` documenting report fights 22/37/54, reviewed flight entry casts, observed player extrema and **provisional** 0.101 m/log-unit fit. Raw CrutchAlerts anchor numbers, world/map rotation and packaged background remain unresolved and were not fabricated.
- Added focused validation/consumer-contract tests (`services/tests/test_encounter_spatial_reference.py`), and repeatable boss onboarding instructions (`docs/ENCOUNTER_SPATIAL_REFERENCE_PIPELINE.md`). **Tests have not run in the Windows application environment.**
- Remaining: import exact addon anchor coordinates and verify transform; package generated background; connect live Map Workshop / Encounters / Raid Plan consumers and check saved-plan readback; run Windows regressions then RAVEN/FORGE. No protected database or existing saved map changed.

## 2026-10-21 — Lokke HM reference replay flight evidence (prototype, not integrated UI)

- An **offline standalone** replay of ESO Logs fight 22 now overlays three flight windows based on Wyrdworks' existing reviewed flight-entry signatures `122820`, `122821`, `122822` and first positive boss damage after qualifying airborne gaps. It has a manual time slider, flight jump buttons and a visible phase label; the local HTML preview is **not** yet served by Map Workshop.
- Verified against user-uploaded report `v16hzgGWTV7BZ48f`: fight 22 flight start/damage-resumption seconds 20.000–72.683, 97.243–161.703 and 183.696–247.165. The reference event IDs are *flight-entry evidence*, not identified immunity aura IDs; damage resumption is not a verified animation-landing timestamp.
- `services/tests/test_esologs_reference_flight_windows.py` guards canonical detector use on three synthetic flight cycles and prevents guessing an end without evidence. Native Windows tests have **not** been executed. No saved map, Raid Plan or protected database was changed.

## 2026-10-21 — Builds one-piece monster save readback verification

- User reported Baseline Monster Set uncheck on Pippin's Slimecraw shoulders showed “Saved Build contents differ from the edited Baseline after reloading.” Builds saved the raw editor payload and compared it against canonical readback, while the canonical bridge normalizes the equipment/glyph-level compatibility fields before saving.
- Builds now constructs its expected readback payload using the same non-destructive `BuildGearEnchantmentCompatibilityService.normalize_build` used by the persistence boundary, and still strictly verifies every saved field, including cleared shoulder slots. Any actual mismatch now lists the differing top-level fields for troubleshooting rather than returning only a generic error.
- Added a targeted one-piece shoulder/normalization regression and source guard. Windows execution and manual one-piece save confirmation pending. The code patch does not modify any user database.

## 2026-10-21 — Player PDF boss equipment matrix

- User's 41-page HOUAD export showed every dossier's equipment table had only Baseline; export completeness reported 0 effective differences, despite stage-specific saved-build evidence in coverage pages. This exposed the mistake of making the matrix columns conditional on recorded deltas.
- The player dossier now builds columns from explicitly configured `boss:` stages, then reads the corresponding resolved saved equipment for each seat and boss. Cells display actual equipped sets and weapons even when unchanged from baseline; unresolved stage builds are labeled rather than silently omitted. Baseline and boss names stay across the chart header. It does not guess unsaved equipment or import unrelated builds.
- Added a PDF regression for one changed boss and one unchanged boss. Windows tests and fresh real HOUAD export visual check pending.

## 2026-10-21 — Authored boss alternates in player PDF dossier

- User confirmed “alternate builds” means boss/stage loadouts inside each chair's selected Saved Build, not other separate Saved Builds. The prior PDF included stage rows only when resolved equipment/skills differed from baseline or a Raid Plan override existed, silently omitting intentionally authored sparse BossLoadouts/ContextVariants that inherit unchanged values.
- Publishing's read-only stage-build projection now carries the matched boss-variant name, using the existing canonical `select_context_variant` resolver. The player dossier includes that authored boss context even with no effective delta, labels it explicitly, and states when the sparse loadout inherits baseline values. No unselected character builds are imported and no rows are fabricated from unsaved contexts.
- Added PDF regression for a saved boss variant with inherited effective values. Native Windows execution and real HOUAD PDF visual acceptance remain pending; saved user database untouched.

## 2026-10-21 — Publishing: stage alternate labels and saved strategy maps

- Each player PDF dossier already includes baseline-versus-saved-stage equipment columns, skill differences and full equipment appendix. Saved stage alternates now carry explicit **ALTERNATE / Stage / Build Name** labels on their main dossier page; unrelated unassigned builds are not silently exported.
- The PDF strategy map picker now includes and preselects the exact map linked to the saved Raid Plan boss stage; users can choose another background or No image for this PDF. The picker selection is authoritative (including No image) rather than silently restoring earlier link choices.
- Fixed exported strategy spread matching between stage contexts (`boss:lokkestiiz`) and saved-map encounter slugs (`lokkestiiz`). Added PDF landscape-spread regression and export-picker wiring tests. Full native validation and rendered PDF acceptance pending.
- Stored maps and map links are read-only during publishing; original assets and protected databases are unchanged.

## 2026-10-21 — Raid Plan middle column: viewport-driven geometry (Windows visual verification pending)

- User confirmed plan-linked map persistence now works, but the center Fight/Map column still collapses when the hover sidebar closes. Earlier size-policy and Resize event changes passed source-focused tests without solving the visual issue.
- Responsive columns now reserve per-column minimum widths from the **actual scroll viewport** after body margins and grid gaps; recalculated on both sidebar states, including when the responsive mode itself stays unchanged. Wide mode follows the existing 30:48:27 ratios; two-column mode reserves 42:58; stacked mode clears the reservations. This targets the underlying QGridLayout width allocation rather than only invalidating and relaying out unchanged size hints.
- Added regression test for viewport-derived column reservations. Native Windows visual acceptance not yet run. Saved-map implementation left unchanged; protected databases untouched.

## 2026-10-21 — Raid Plan middle-column and linked-map preview regression

- Windows screenshots exposed a Raid **Plan** middle-column resize problem, distinct from the Strategy editor. The Fight/Map column now requests expandable horizontal space and the scroll viewport's Resize event triggers responsive column reflow even when the window itself does not resize during sidebar hover/collapse.
- The Raid Plan preview previously picked the first boss map from the general encounter catalog, ignoring the saved plan's explicit linked map. It now prioritizes the matching `RaidSectionStateService.linked_raid_map_id(plan_id, encounter_id)` record and falls back to catalog maps only if unavailable. Inline saving immediately refreshes the visible Raid Plan map preview.
- Added source regressions to `ui/tests/test_team_gear_warning_source.py`. Windows layout and actual-stage map reopen witness pending. Original map source and protected databases untouched. Live Raid remains parked.

## 2026-10-21 — Strategy map expansion and active saved-map selection

- The Strategy center map page and board now request Expanding sizing on both axes instead of Ignored. This addresses collapse of the center column while preserving the tool rail and fixed inspector. A source regression guards its layout policy.
- Saved plan/stage editable maps now record an atomic `active_layout_id.txt` pointer after validated layout/timeline persistence. Reopening selects that explicit version rather than guessing from filesystem modification time, including when a previously saved content-hash version is saved again. Prior versions and original library sources are not deleted. Existing plans without a pointer continue using the legacy newest-by-mtime fallback. Tests guard reuse of prior version without losing history.
- Windows GUI geometry and saved map reopen remain to be witnessed; focused test execution pending. Live Raid remains parked, and no user database changes are part of this patch.

## 2026-10-20 — Task 4 scope adjusted: Live Raid parked; named-stage map paths fixed

- Per user direction, **Live Raid is parked**. Its data/code remain intact, but Live Raid display/handoff and page tests are no longer Task 4 acceptance gates.
- Fixed Windows-invalid named-stage map keys: `RaidMapWorkspaceScope.map_key` retains legacy boss slugs and simple `general`/`trash`, while assigning deterministic safe `stage-<hash>` identifiers to context keys containing colons or forbidden filename characters. Strategy map selector and calibration lookup now reuse that same canonical scope, avoiding stage-key disagreement.
- Added regression coverage for named Trash stage save, switch, reopen, and cross-plan key stability in `ui/tests/test_phase155_raid_map_workspace.py`. Awaiting execution on Windows. No live databases modified.
- Remaining active Task 4 goals: Strategy / Raid Map stage save/reopen and source-original preservation; Kill & Pull ordering and stage-scoped persistence. Do not require Live Raid.

## 2026-10-20 — Windows Task 4 map test fixture correction

- User's focused Windows suite reported **33 passed, 1 failed**: the new map-preservation regression attempted to create `boss:lokkestiiz` directly as a filesystem directory, which is illegal on Windows. Actual Strategy boss-map persistence converts `boss:lokkestiiz` to `lokkestiiz` via `_map_scope_key`. Corrected fixture to use production boss map keys (`lokkestiiz`, `yolnahkriin`) and retained source immutability, version retention, plan/stage isolation checks. Rerun pending. No live databases modified.

## 2026-10-20 — Task 4 user witnesses and map-copy preservation test

- User confirmed the Raid Planner map is editable and Kill & Pull Order presents phase-appropriate enemy targets in the running app. Original library-map preservation on save is **not yet verified by a Windows witness**.
- Source audit: `EncounterRaidMapStore.save_plan_layout` validates board JSON and writes a content-hash-named copy under the exact plan/stage scope, leaving original source and previous saved layouts in place. Map Workshop replacements use a separate explicit workflow. Added disposable-path regression `test_plan_map_edits_preserve_original_and_other_stage_copies` covering library source immutability, previous version retention, and isolation across stages/plans; pytest execution pending.
- Remaining Task 4 acceptance: pass regression, Windows save/reopen on disposable plan, and validate saved-stage map consumption in Live Raid. No existing user database modified.

## 2026-10-20 — Task 4 Strategy / Raid Map and Kill & Pull Order started

- Reviewed the current `Phase15StrategyPage` / `KillPullOrderDialog` against the active product roadmap. Confirmed Kill & Pull Order uses canonical stage-scoped `Phase15AssignmentStateService`, optimistic expected-state saves, exact read-back of priorities, and opt-in encounter enemy candidates. The Strategy page has explicit current-stage map saving, dirty-board protection and a map library workflow.
- Corrected candidate detail presentation in Kill & Pull Order: actual line breaks now separate phase/response, explanatory note, and evidence. Added source contract regression `ui/tests/test_kill_pull_candidate_details.py`.
- **Still open:** real-plan Stage map save/reload and Live Raid handoff, reusable map selection, Kill & Pull cross-encounter candidate completeness, deleting/reordering targets, geometry under changing stage/side menu sizes, and native Windows acceptance. No execution or data edits in this chat; do not call Task 4 complete yet.

## 2026-10-20 — Team selection geometry and one-piece monster-set correction (source published)

- Selecting a Team player now schedules the same adaptive workspace reflow used for sidebar/resize changes. The selected-player detail layout is activated before the Team panel's required height is measured, so a growing baseline or warning-pill panel reserves space *below* the roster instead of overlapping player rows. Source regression added. Native Windows visual smoke test pending.
- Builds monster simple mode now treats the unchecked **Also equip matching shoulder** box as authoritative when changing sets: it clears a stale matching shoulder from the old or newly selected monster set while preserving an intentionally different shoulder set. The physical metadata readiness service already checks only occupied armor slots, so a truly empty shoulder is not a missing-gear warning. Regression coverage added; test execution pending.
- No user data/database changes; existing saved builds are not automatically rewritten. Re-save an affected monster configuration in Builds to clear any stale shoulder recorded previously.

## 2026-10-20 — One-piece monster sets no longer imply a phantom shoulder (Windows verification pending)

- Builds' **Monster** gear editor now has explicit **Also equip matching shoulder (2 pieces)** selection. Simple mode equips the selected Head; Shoulder receives the same set only when the checkbox is enabled. Existing matching two-piece layouts load with that checkbox selected, and clearing it removes the matching second piece. An unrelated occupied Shoulder slot is preserved. Advanced mode supports an actually blank monster slot rather than falling back to the common set.
- Gear metadata readiness remains correctly scoped to each saved equipped slot with a set; it should no longer warn about a shoulder created implicitly by the simple editor. Previously persisted mistaken shoulders are **not automatically rewritten**: open Monster, uncheck the shoulder, and Save Build to remove the extra piece safely.
- Added a source-contract test. GitHub source committed; actual Windows interaction and pytest execution are pending. No live data touched.

## 2026-10-20 — Unified selected-player warning pills (source committed, Windows acceptance pending)

- Added `services/raid_plan_player_warning_projection.py` as a read-only per-chair view of existing canonical evidence. Builds supplies missing/unresolved build and missing physical gear metadata, stage Assignments supplies missing support-ultimate ownership, and `RaidReadinessEvidenceService` supplies supported, explicit per-chair Coverage gap/review states (only when a named coverage duty is assigned). An unknown provider is a neutral review, never a fabricated gap.
- The selected-player Team detail now renders compact clickable warnings with source-specific tooltips. Build warnings open the selected-player build editor, Assignments warnings open the current stage Assignments dialog, Coverage warnings open the existing inspector. Warnings regenerate on player selection and after those editors close; corrected saved data naturally removes its corresponding pill. The Team list remains uncluttered; baseline/current-stage build text remains visible.
- Added pure projection and source-wiring regression tests. **No local pytest or native Windows GUI execution in this chat**; treat as source-published pending acceptance. Live databases untouched.

## 2026-10-20 — Selected-player Team detail, baseline, and warnings

- Following user review, moved the gear-metadata warning **off Team row cards** into the larger selected-player detail panel beneath Team. The panel now shows the selected Saved Build's baseline armor sets and weapon types separately from the effective current Raid Stage loadout, and uses the existing physical-metadata readiness detector to list missing fields only for the selected build.
- The panel also distinguishes no selected build, an unresolved selected BuildId, missing gear fields, clean metadata, and unavailable metadata verification. Warning styling resets on player change. This is read-only; no user gear, plan, or database is rewritten. Updated `ui/tests/test_team_gear_warning_source.py` to reflect panel ownership. Source committed; native Qt sizing and pytest remain pending.

## 2026-10-20 — Readiness tab labels and team gear metadata warning (runtime verification pending)

- The Raid Plan Readiness segmented tabs now share available width and use compact horizontal padding/11px text to keep **Group Setup** and **Mechanics** visible without clipping.
- Team individual player cards project the **exact selected Saved Build** through the same physical gear metadata readiness gap detector as Builds. A compact amber `⚠ Gear N` pill appears only for identified missing metadata; the hover tooltip explains the count and directs the raid lead to Builds. Unknown/unselected builds are not mislabeled as confirmed gear gaps. The warnings are read-only and do not modify gear.
- Added source regression assertions. Changes were committed to `wyrdworks-dev`, but native Windows visual check and pytest execution remain pending; no user databases were modified.

## 2026-10-20 — Task 3 executable acceptance coverage added (not yet executed)

- Added a disposable-SQLite cross-trial regression to `services/tests/test_phase15_assignment_state_service.py`: Nahviintaas, Archcustodian, and Reef Guardian stage scopes must retain Kill & Pull priorities through unrelated Assignments writes and new service instances. An outdated expected snapshot must raise a conflict instead of overwriting.
- Previous source changes include Copy Build non-destructive identity and explicit raid-seat selection, the source-contract tests, and general encounter enemy projection tests. Current chat verified file contents through the connected `wyrdworks-dev` repository; it did **not** execute repository pytest, RAVEN/FORGE, Windows Qt interactions or saved real-plan reopen. Completion status remains pending those execution gates. No live user data accessed.

## 2026-10-20 — Copy Build raid-seat ownership correction (source verified; runtime pending)

- Corrected the initial Copy Build implementation so making a duplicate does not silently switch the active chair/editor away from its original selected BuildId. The new build remains independently saved and available in the Saved Build picker; choosing it is an explicit raid-lead action. Added a source regression assertion. Existing canonical builds, assignments, stage variants, and player identities are not rewritten by this source change.
- GitHub source is confirmed on `wyrdworks-dev`. The full repository tests, Windows Qt UI, database roundtrip, and cross-trial end-to-end acceptance remain **not executed** in this chat. No live database touched.

## 2026-10-20 — Copy Saved Build (source published; native acceptance pending)

- Builds now provides **Copy Build** for the currently selected saved build. The action requires exact PlayerId / CharacterId ownership, asks for a distinct name, deep-copies the entire saved payload (including stage variants and boss loadouts), assigns a fresh BuildId, resets Ready for Raid, and removes copied plan/seat provenance. It saves additively through the canonical BuildService and verifies exact copied contents and unchanged original after reload. Unsaved edits use the existing Save / Discard / Cancel dialog.
- Added a source-contract regression test. The test, native Windows Qt interaction, representative save/reopen, failure paths, and cross-trial workflow have **not** been executed or certified in this chat. No live user database was opened, modified or replaced.

## 2026-10-20 — General encounter-aware target suggestions (runtime verification pending)

- Replaced the one-boss Nahviintaas classification switch with a reusable, read-only projection of structured encounter `add_group` facts and explicit `kill_order_target` mechanic facts for any encounter ID. Source-backed phase/trigger, response, and optional per-member context flow into Kill & Pull Order. The same enemy may appear in multiple distinct phases; ability names without target evidence are excluded.
- Nahviintaas portal and main-arena behavior is recorded in its structured evidence packet rather than hardcoded in the service. Added synthetic regression coverage for Archcustodian, Nahviintaas and a repeated target across phases. No automatic authoring, overwrites or new database tables. This is a general consumer of *existing structured evidence*, not proof that every researched encounter has a complete structured target roster. Tests and native Windows inspection remain pending.

## 2026-10-20 — Encounter-context Kill & Pull suggestions (source published, Windows validation pending)

- Nahviintaas candidate enemies now include reviewed main-arena add names alongside the Eternal Servant and expose phase, recommended response and caveats in the popup. The portal Eternal Servant is a 90-second kill there, not a generic upstairs kill target; HM Vigil Statue is conditional-vulnerability control, while execute Flame Atronachs are gather/cleave.
- Suggestions remain opt-in. Clicking a candidate adds a manually editable row with phase and source note; the exact plan/stage and existing assignment persistence contract remain in place. Unknown encounters still get manual editing, not inferred kills. Added a focused projection regression, but Windows Qt, service tests, stage save/reopen and actual encounter visuals remain unverified. No database edits.

## 2026-10-20 — Assignments save preserves Kill & Pull priorities (Windows verification pending)

- The active Assignments page now reads the exact existing Plan/Stage record before saving its own fields, copies forward the Kill & Pull priorities owned by the separate editor, and uses the canonical service's optimistic concurrency check. An intervening write is rejected rather than silently overwritten. The canonical service already verifies a durable read-back before displaying Saved.
- Updated the existing source regression assertion for the new lossless save call. GitHub source published on `wyrdworks-dev`; live Windows interaction, executable focused tests, and representative copy save/reopen have not been verified in this environment. No live data was opened or altered.

## 2026-10-20 — Park visible FD.my publishing controls

- Hide the existing FD.my publishing buttons on the Raid Plan header, Builds, Strategy / Map Workshop and the older Raid Plan persistence page. Hide the associated FD.my-only status labels in Builds and Strategy. This is UI-only: preserve publishing handlers, service integrations, saved plan/build/map data and all local Save controls. No database migration or reset. Source published on `wyrdworks-dev`; native Windows visual smoke check remains pending.

## 2026-10-20 — Atomic Roster editor save and failure retention

- Edit Player now calls `RosterService.save_personnel_editor` to update the Personnel record, team memberships, and seven-day availability in a **single SQLite transaction** on the existing user database, with Pydantic v2 payload validation, stale-snapshot verification under a write lock, read-back validation before commit, and rollback on error. No database replacement, schema reset, or identity rewrite.
- The editor now keeps its dialog and entered values open when that atomic save fails. Saved is shown only after successful verification. Avatar/catalog portrait writes remain a **separate storage boundary**; if avatar saving fails after the SQLite commit, the editor stays open for avatar retry, with already-committed field controls locked to avoid misleading unsaved edits.
- Four isolated regression tests have been added for save/reopen, stale edits, invalid availability, and injected database failure rollback. **Not yet executed:** pytest, Windows Qt interaction, and fresh installed-app validation. This is committed source work, not an installed or validated Windows build.

## 2026-10-20 — Roster editor preflight validation and stale-edit guard

- The unified Edit Player action prevalidates its complete Personnel and availability payload using existing strict Pydantic v2 schemas, checks an optional new team name, and compares current persisted Personnel/availability records against the records shown when the popup opened. If an intervening edit is detected, it refuses to overwrite the newer record.
- These checks occur before the first write, while existing canonical save/read-back checks remain in place. **Incomplete gates:** edits are still performed as separate persisted operations; there is no verified atomic all-fields commit, closed-on-error draft retention, database-reopen test, race-safe commit-time revision check, or Windows Qt test. This source increment must not be labeled fully AGENTS.md/DEVELOPMENT_STANDARD.md compliant.
- Source-only change published to `wyrdworks-dev`; user-owned databases were not touched by this change.

## 2026-10-20 — Unified Personnel editor fields, teams and availability

- The Roster Edit Player popup now includes the existing Personnel fields: Player/ESO name, main character, Discord name, YouTube, Twitch, preferred ESO class, primary/secondary roles, status and private notes, plus avatar selection. Exact canonical player and character IDs remain protected rather than exposing raw identity keys as editable text.
- Team memberships can be checked from existing teams or extended with a new team name. Seven-day availability, preferred times and availability notes are edited in the same scrollable popup. Changes reuse the existing RosterService and RosterWorkspaceStateService, with explicit read-back checks. If availability or avatar persistence fails after personnel saves, a partial-success warning is displayed instead of claiming all fields were saved.
- GitHub source published. Windows Qt popup interaction, database-reopen persistence, stale edit safety and failure-injection regression remain unverified. Existing user databases are not modified by this source update.

## 2026-10-20 — Roster profile action placement and avatar editor

- Move **Edit Player…** beside **Merge Player…** at the bottom of the selected player's Profile. Remove the standalone Avatar button and the avatar-click editor from the Profile; choose or clear a portrait from inside the Edit Player dialog instead. Avatar selection is staged until Save, then written through the existing canonical player catalog with read-back verification. Personnel details are saved first; if avatar saving fails, show a partial-success warning rather than a false Saved message. Existing identities and databases remain unchanged. GitHub source published; Windows Qt interaction and restart persistence still require validation.

## 2026-10-20 — Visible Roster player editing controls

- Roster personnel table retains click-on-name editing and now offers a clearly labeled **Edit Player…** button beside the selected player's heading. Clicking the heading also opens the editor, and double-clicking a non-name table cell opens the selected personnel record. The button is disabled without a saved selection; clicking the name does not double-open the editor on double-click. The existing RosterService update and UI read-back check are reused without database changes. GitHub source has been published, but Windows interaction and restart persistence have not yet been executed against live user data.

## 2026-10-20 — Roster player-name editing

- On the active Roster page, clicking a player's name in the first table column opens the existing saved Personnel editor for that selected record. Clicking other cells continues to select without opening the editor. The editor keeps the existing canonical RosterService write and read-back comparison before displaying Saved. Source change is published; Windows Qt interaction, fresh database reopen and failure-path tests remain unverified.

# Wyrdworks — Feature index

## 2026-10-20 — Retain reviewed encounter selector corrections

The shared boss-guide selector applies the existing reviewed encounter-identity exclusions, retaining named Blackheart Haven bosses and same-named records in other content. Raw source records remain stored and directly accessible; no database migration or new game-mechanic claim is introduced.

## 2026-10-20 — Explicit Live Raid assignment read failures

The existing Live Raid assignment projection distinguishes an unsuccessful saved-state read from a stage with no saved assignments. A failed read clears old jobs and notes, shows a retry/review message, and recovers on the next verified read. Plan/stage scope checks, shared Trash inheritance, the canonical assignment store, current navigation availability, and theme remain unchanged. This is a bounded projection repair; it does not re-enable hidden navigation or certify an installed Windows workflow.

## 2026-10-20 — Anchored inline map toolbar

The compact map toolbar stays six pixels inside the visible map corner during preview dragging, editor hand/middle-button panning, wheel zoom, fitting and resizing. It overlays the view frame rather than scrolling with the map image. Existing tools, masks, map geometry and save owners remain unchanged.

## 2026-10-19 — Recover Builds workshop and Stage Assignments UI (GitHub source; Windows verification pending)

Selectively restored the October 19 Builds page, single-player contextual build editor, new PlayerBuildWorkshop, stage assignments dialogs and Assignments page from the recovery checkpoint, along with targeted UI tests. Preserved newer slim Builds scrollbar CSS from wyrdworks-dev. No broad recovery-branch merge, no database or legacy-data replacement. This restores interface source, not proven Windows runtime compatibility: run targeted Builds/Assignments tests and inspect the pages before further feature edits.


## 2026-10-19 — Recover new Raid Plan Coverage Inspector (GitHub source; Windows verification pending)

Recovered the recent stage-aware Raid Plan Coverage Inspector and its canonical evaluation service, dialog styling, and focused service/UI tests from the October 19 recovery branch. Redirected Raid Plan Team buffs & debuffs / View to this inspector instead of the legacy snapshot or standalone Coverage route. No broad branch merge, database change, or unrelated UI replacement. This supersedes the prior temporary navigation change to standalone Coverage. Native Windows, UI, and persistence regression checks remain pending.


## 2026-10-19 — Raid Plan Coverage opens the existing full Coverage module (GitHub source; Windows validation pending)

The Raid Plan Team buffs & debuffs action now emits its existing Coverage navigation signal instead of opening the legacy provider-record popup. The main window connects that signal to the full stage-aware Coverage page, preserving its recent UI, provider/source planning, Known Sources, Connections & Timing inspector, and searchable grouped source picker. The older popup implementations remain in source but are no longer reached through this Raid Plan action. No Coverage computations, manual assignments, databases, or persistence models were changed. Native Qt navigation and saved-state validation are pending.


## 2026-10-19 — Grouped, searchable Coverage source picker (GitHub source; Qt validation pending)

The existing Coverage Source combo retains its layout and editable selection while grouping the complete Known Sources list under non-selectable Skills and ultimates, Passives, Equipment, Potions, and Other documented sources headings. Type-ahead substring completion is case-insensitive. Original source strings remain the saved values; duplicate exact labels are not repeated, and a saved source absent from the current catalog remains selectable. These groups describe *source type*, not evidence that the selected player can equip or use it. No provider eligibility inference, database mutation, or changes to manual override persistence were added. Native Qt and regression acceptance remain pending.


## 2026-10-19 — Collectible item artwork: optional WebP atlases (Windows validation pending)

Added `tools/asset_packs/build_collectible_icons_pack.py` to scan the existing `content_packs/collectible_icons` ID-prefixed PNG cache, reject duplicate IDs, preserve source files, and construct lossless 128px-cell WebP atlas pages plus a strict SHA-256 checked manifest under an external build root. Added an explicit non-overwriting verified installer (`install_collectible_icons_pack.py`), a lazy Qt sprite reader (`ui/collectible_item_atlas_artwork.py`) that validates only the requested page, and synthetic PNG/Qt integration tests. The *existing* individual collectible-details artwork slot now prefers the optional `collectible_item` atlas and falls back to the established `CollectibleIconCatalog` file lookup. The finished category badges, geometry and visual styles remain untouched. No database writes, bulk runtime file scans or redistribution of artwork. The 13,089 source PNGs remain on the user's Windows computer; pack generation, tests and installation are not yet executed there.


## 2026-10-19 — Coverage status wording clarified (GitHub source; runtime validation pending)

The existing Coverage layout, saved manual choices, planning calculations, Known Sources and three summary filters are preserved. The effect-status display now distinguishes **Covered** (supported planning capability), **Assigned** (Raid Lead choice awaiting source validation), **Available** (build-backed source without an assignment), **Needs Review** (conditional or incomplete evidence), **Unknown** (evaluation unavailable) and **Missing** (no provider in completed evidence). The three existing summary cards continue to group Assigned, Available, Needs Review and Unknown under Needs Review; detailed evaluator labels and original states remain in status tooltips, item metadata and evidence details. This is presentation-layer clarification, not observed uptime/delivery verification or a new coverage calculation. Windows Qt and focused regression acceptance are pending.


## 2026-10-19 — Optional achievement art in existing Achievements UI (Windows validation pending)

The existing Achievements page now requests achievement-ID artwork from an independently installed, integrity-verified WebP atlas pack when no bundled per-ID artwork is available, retaining the exact UI, bundled-art priority, and semantic-icon fallback. Qt decoding and cropped sprite lookups are cached on first use; no startup downloads or artwork scans. Added explicit verified local installation tool at `tools/asset_packs/install_achievement_pack.py` with non-overwriting version destination under `%LOCALAPPDATA%/Wyrdworks/asset_packs` and synthetic Qt integration tests. The real 3,909-mapping / 11-page pack remains built in local research staging until the user installs it. No database or Collectibles changes.


## 2026-10-19 — Achievement WebP atlas pack builder (GitHub source; Windows validation pending)

Added an explicit offline build tool that reads the reviewed achievement-ID icon index and completed staged PNG report, verifies original icon hashes and decoded dimensions, deduplicates by texture identity, generates 64px sprites in 1024px lossless WebP atlas pages, and writes a strict versioned manifest plus build report. Existing source images are preserved. The builder refuses incomplete staging and overwriting an existing pack version. Isolated synthetic-image tests cover shared-icon identity, integrity verification and tamper rejection. No theme, page, database, automatic installation, or public distribution changes; Windows Qt decoding and runtime page integration remain pending.


## 2026-10-19 — Opt-in achievement PNG staging (GitHub source; Windows validation pending)

Added `tools/asset_packs/stage_achievement_icons.py` to stage unique UESP achievement PNG candidates outside application data, with an explicit input index/output root, fixed HTTPS UESP host, disabled redirects, bounded response size/image dimensions, decoded PNG checks, reused local staging files and per-icon success/failure report. Uses original texture path as the deduplication identity; no live UESP download is yet verified. Added isolated synthetic-PNG tests for deduplication, cache reuse and failed-image handling. This does not build or activate atlases, alter either database, load artwork at startup or change any UI/theme. Source redistribution permissions still need review.


## 2026-10-19 — Achievement icon source index (GitHub source; tests pending)

Added `tools/asset_packs/index_achievement_icons.py`, a builder-side indexer reading the existing achievement JSON `achievements` array or an explicitly selected SQLite achievement table in read-only mode. It maps stable numeric achievement IDs and original texture paths to candidate UESP PNG URLs, deduplicates original textures, and reports missing/rejected icons. It does not download images, modify application databases, replace existing artwork or alter the theme. URL resolution is still a candidate mapping because the live UESP endpoint could not be confirmed from this environment; tests are written but not executed. Attribution/licensing, network fetch, atlas packing and optional UI consumption remain future validation gates.


## 2026-10-19 — Optional Visual Asset Library foundation (GitHub source; tests pending)

Added strict Pydantic v2 manifests for versioned atlas packs, read-only SHA-256/byte-count verification of installed local pages, namespace/key sprite lookup, and focused tests for valid, corrupt, traversal, out-of-bounds and unsupported-schema contracts. Discovery is explicit/on-demand; neither artwork downloads nor image loading are initiated at startup. This first increment is infrastructure only: no pack builder, install/update/uninstall flow, Qt pixel decoding or page integration yet. The current validation does not prove an image can decode and must not be treated as release pack verification until actual decoded image dimensions/format are checked. No theme, user database or ESO database changes.



Wyrdworks is the current product name; FoundryDock remains the repository and technical identifier. This index includes historical implementation notes and does not certify the current branch or installed build.

## 2026-10-19 — Gear details readability adjustment (GitHub source; Windows check pending)

Removed the Gear Field Guide subtitle and hidden its unused header label. The selected set name now wraps as a larger 27px heading above 17px acquisition/weight metadata and 17px piece-bonus descriptions. The Set Details card heading stays at the shared card size. No database, search, or filtering behavior changes.

## 2026-10-19 — Gear Field Guide presentation (GitHub source, runtime validation pending)

The retained read-only Gear page is titled Gear Field Guide, with its existing Weight, Bonus and Acquisition filters above a set-search field immediately adjacent to the scrollable set list. Filtering retains the stable selected catalog ID when the set still matches. An explicit **Unknown Source** acquisition filter and detail label distinguish missing acquisition classification from confirmed drop locations; the displayed unknown count continues to derive from current catalog rows rather than a hardcoded value. The selected item receives a motion-free brass outline and contrasting text, and canonical piece bonuses display in aligned, wrapping rows with original wording preserved. No ESO/reference or user database writes, new inference, or Builds/Comp integration are introduced. This is a source change; Qt geometry and Windows executable validation are still pending.

## 2026-10-15 — Workshop startup artwork

Startup prefers the new Wyrdworks Workshop artwork, displayed statically at its original proportions with the complete lettering visible. A bundled WebP copy preserves the original PNG, and existing splash fallbacks remain available. Buttons pictured in the artwork are decorative.

## 2026-10-15 — Blue-slate Granite surfaces

Granite remains the sole appearance. The rejected cracked-stone background is removed. Outer workspace and navigation surfaces stay quiet and blue-black; content cards use blue-slate shading, ivory text, readable muted labels, brass/gold and dusty violet accents. Existing dimensions, lazy pages, drafts and color-vision role cues are retained. No flashing effects or new persistence are introduced.

## 2026-10-15 — Framed Wyrdworks raid dashboard

Raid Plan now uses the supplied fjord header, Wyrdworks brand artwork, fine brass panel frames, dark inset player cards and working All/Tank/Healer/DD filters. The roster keeps canonical seat selection and saved-build references. A compact readiness summary counts the existing Covered/Review/Unknown/Planned checks; tabs expose the original setup, mechanics and sources evidence, and raid notes keep their existing save path. No numeric readiness percentage, observed delivery or new map authoring tool is inferred from the reference artwork. The supplied timeline art decorates actual recorded health thresholds using the shared Metrics tokens. Violet stays limited to small selected accents and healer identity; the rejected cracked-stone background is removed. Team filters keep content top-aligned and restore the complete roster height after rail toggles. Readiness reserves its own visible content height and can extend below the map through the existing outer scrollbar, keeping notes and controls below the checklist. Parked routes remain parked.

## 2026-10-15 — Wyrdworks roster identity

Raid Plan player cards and the active Personnel roster now separate three signals: the left bar identifies Tank (#82AFC5), Healer (#A884C2), DD (#C1AA80) or Support DD (#D08D5C); the circular forged emblem identifies class; a restrained violet outline identifies selection. Role/class text and accessible identity labels accompany the paint. Unknown roles use neutral paint and unknown classes never borrow a different emblem. Selected-player panels use the same cached class assets and preserve player-owned avatars.

The supplied transparent class sheet is repacked into a 1024×512 atlas with seven 256-pixel cells and an empty reserved cell. A JSON manifest, labeled reference sheet and seven individual transparent fallbacks live in assets/themes/granite/class_emblems. Packaged resource paths and high-DPI helpers are shared by the UI. Existing 46-pixel Raid Plan cards and Personnel table geometry remain intact. The top fjord bar uses only the supplied Wyrdworks Name Logo; plan selectors remain accessible under Plan details. Granite remains the sole supported appearance.

## Current workflow scope (2026-10-15)

**Active workflow pages:** Raid Plan, Roster, Assignments, Builds, Strategy / Raid Map, Live Raid, and Finch / Collaboration where applicable. Continue maintaining supporting systems and research when they serve these workflows.

**Parked interfaces:** Lantern, Comp Brainstorm, Coverage, Rotations, Readiness, Health, Comp Engine, Optimization, and Extreme Build. Parked interfaces remain in the codebase with their existing data, behavior, integrations, and regression coverage. Their underlying information may still be consumed through shared services by active workflows. “Parked” is a prioritization status, not a deletion or deprecation claim.

Status language in this index is scoped: **implemented** means the code path exists; **parked** means an interface is retained but not an active development priority; **active** means current workflow work is prioritized; **unverified** means the stated behavior lacks its required current witness. Entries below describe dated capabilities and evidence at their stated checkpoints. Treat explicit “unverified,” “pending,” or “historical” limits as material; do not infer current operational or installed status from an entry alone.

## 2026-10-15 — Read-only Support Windows in Assignments

Assignments now includes a Support Windows tab with an explicit **Review current
assignments** action. It shows the four support chairs, assigned ultimates,
encounter-event link status, manual timing notes and unresolved delivery evidence.
The action can inspect unsaved drafts without saving them; edits, saves and stage
changes clear old review cards. Reviewed clock-event identities come from the last
stage load using exact encounter/trial identity, without display-name matching or
whole-catalog fallback. Missing/unavailable evidence remains explicit.

This is assignment readiness, not a numeric timeline, build-capability audit or
observed coverage report. Free-text notes never establish activation intervals.
The view uses one outer scrollbar, the existing Granite theme and no new storage
or validation runner. Disposable Qt action/save-reopen/geometry tests and adjacent
regressions pass locally; source checkout only, no packaged-install claim.

# 2026-10-14 — Raid Plan roster, map lookup and rail balance

The Team panel now follows the Prototype's two-tab structure: Raid Roster (12) for player/role/class and Stage Loadouts for saved build references. The Fight map has an inline named-attack search that narrows the selected encounter's recorded attacks before showing its evidence, and Readiness uses compact status labels with the full explanation beneath each heading. The supplied FD compass is larger in the collapsed rail, while the existing menu sprites are smaller and slightly dimmer. Saved assignments and build identities remain unchanged; selected build names are still plan-level references, with stage-specific gear and skills reviewed in Builds.

Raid Plan now recomputes its responsive columns when the page is shown and resized, including before any plan is loaded. Map zoom stays in the map box, with controls below the map and left-aligned; square authored maps stay square while older images use their own aspect ratio, avoiding blank bands without changing saved marker coordinates. The old popup/duplicate control row is gone. The DD offensive review shows each damage dealer's personal critical chance and the same value with that player's recorded personal Savagery, personal and plan-supported penetration, and capped critical damage. Major/Minor Savagery applies only to the assigned player's row; group buffs and target debuffs remain shared inputs. Coverage source choices expand safe multi-source catalog entries into individual options, using the local reviewed source data without claiming observed delivery. Crit/Pen public service results now cross immutable strict Pydantic contracts. Focused UI and service verification passed 50 tests; service-catalog audit reported no errors and 315 existing registration warnings; dependency and strict architecture audit results are recorded with the local commit. Packaged Windows rendering remains unchecked.

## 2026-10-13 — Raid Plan focused startup and icon-led workspace (local; packaged acceptance pending)

The app opens directly into Raid Plan and constructs only that workspace at startup. The lantern landing page and the requested side-rail routes (Roster, Comp Brainstorm, Assignments, Coverage, Health, Rotations, Readiness, Strategy / Raid Map, Live Raid and Brittle Uptime) are omitted from navigation and remain unconstructed. The Raid Plan keeps a compact trial/challenge/saved-plan row, editable plan/team details on demand, a horizontally navigable stage strip, a responsive Team / Fight / Readiness layout, and a stage map with phase flow. Named attacks remain available through a one-click lookup dialog instead of a permanent list over the map. Existing authored gold sprites and Sunspire artwork are reused. Focused UI/navigation checks pass. The disposable native runtime exercised 13 pages and 14 routes with no app errors, but its source-database guard reported a logical database change during workspace preparation; the overall run is therefore not certified, and no packaged behavior is claimed.

The Raid Plan workspace now matches plan chair IDs such as `tank-1` to the display labels such as `Tank 1`, so saved team members and build references appear in the Team table. Quick Entry opens a compact editor for the active plan's twelve seats and writes through `RaidPlanRepository` with exact read-back; replacing a free-text player clears that chair's old player and build identity. Responsive layout uses display-equivalent width, so Windows scaling does not incorrectly collapse a wide monitor to one column; the map keeps the widest share. A focused UI test covers the seat mapping, dialog save/reopen, and high-DPI responsive layout.

The Raid Plan Team panel now has a full-width Roster view for complete player names and saved-build references while keeping Quick Entry for editing. Readiness cards place their status beside the heading and give the explanation the full card width with a taller minimum height, so larger text remains readable. Readiness remains planning evidence: member/role/build counts, planned Coverage provider records, encounter-guide records and linked map evidence are displayed with their current limits; kill order, authored callouts and backup plans are not yet verified automatically.

The Raid Plan side rail uses the supplied gold FD compass with a `FOUNDRYDOCK` wordmark while expanded; the wordmark hides with the existing collapsed rail. The duplicate BFF mark has been removed from the trial banner. The approved logo file is included in the release asset allowlist.

## 2026-10-13 — Penetration support review and U51 Sorcerer group source

Raid Plan Readiness and Health now include U51 Sorcerer Exploitation as 2,974 group Offensive Penetration when the plan contains a Sorcerer seat with its endgame-passive assumption enabled. The source is counted once and kept separate from target armor reduction. When confirmed penetration is below the PvE target but the existing support ceiling can reach it, the player is marked for review of magnitude and uptime instead of being called short. Alkosh remains a ceiling until its activation-scaled amount is established; dynamic Force of Nature target stacks are not inferred. The four affected test modules pass 48 focused checks on the local working tree; installed Windows behavior remains unverified.

## 2026-10-12 — Provisional Hard Mode research preview (developer integration; not game-engine canon)

FoundryDock's existing `EncounterService.provisional_research(exact_encounter_id, difficulty, packet_path)` now provides **explicit opt-in, read-only** lookup of the 32-entry HM/veteran research inventory at `data/encounter_research/provisional_hm_mechanics_20261012.json`. The packet is validated with strict Pydantic v2 input schemas: exact snapshot encounter IDs and difficulty scope, source-key integrity, nonblank identities, unique finding IDs, no silent `reviewed` status or authoritative packet state, and constrained numerical damage observations. The method deliberately does **not** feed canonical `requirements()`, `evidence_facts()`, Combat Engine damage, or survivability decisions. A focused synthetic/committed-packet test was added; native Windows and full suite execution remain unverified. Source-level interpretation, contradictory timings, actor-specific attack attribution, patch relevance and combat-log magnitudes still require review before authority promotion.

## 2026-10-12 — Encounters three-column research guide restored (Windows visual acceptance pending)

The existing Encounters page again uses a three-column splitter for the encounter browser, scrolling boss/mechanics field guide, and independent Phases/Timeline/Sources inspector. The previous middle-column maximum-size constraint and reference-inspector insertion below mechanics were removed to prevent long text from expanding beneath a neighboring column. The outer workspace remains owned by the application shell. Source-level layout regression coverage was added; native Windows geometry, text wrapping, and all window-size acceptance checks remain pending. This increment does not import candidate mechanics, change canonical ESO reference data, or assert that an attack is safe to absorb.

## 2026-10-12 — Raid Plan Endgame Ready visible in Health (Windows acceptance pending)

Health's selected-player details now display the exact Raid Plan seat's strict Pydantic Endgame Ready assumption: positive confirmation or not confirmed. This is read-only; it does **not** invent character-owned passive ranks, CP purchase, gear item quality, glyphs, stat calculations, or human readiness. Stage selection retains the plan-scoped baseline; unconfirmed chairs stay unconfirmed. A focused test is added to the integration track. UI acceptance and tests after this change remain unrun.


This is a capability map, not a fresh completion certificate. Verify current implementation and consumer tests. Add or update one entry per visible capability; keep detailed dated evidence in validation reports.

## 2026-10-11 — Three-profile executable packaging (source committed; Windows build unverified)

A package-only `packaging/build.ps1` entry point offers Personal/Test (Jarakeen), Friend (Rylo), and Public (generic/Rik via recipient) builds. Release archives are versioned by profile and recipient under `releases/`; existing archive names are never overwritten. An optional supplied user database is converted into a privacy-limited first-install raid seed by the existing canonical seed exporter, with optional Raid Plan filtering. The source database is not modified. The packages no longer include updater credentials or update payloads. Separate `packaging/test_release.ps1` owns validation; packaging does not invoke pytest. Version is 0.2.2. Windows executable construction, fresh installation and launch checks remain outstanding.

## 2026-10-11 — EXE visual acceptance follow-up (partial source fixes, Windows validation pending)

The Achievement Details panel now uses an 18-point title and 12-point description instead of 24/20 points, reducing text overflow. Settings Help now exposes Assignments, Builds and Coverage Field Guide entries, and the help router looks for their numbered image directories under `resources/help/raid_planner/`. The actual presence of these image assets in a Windows EXE is unverified; missing folders continue to fall back to offline text. Other reported EXE defects (global font/gear theme, Readiness delay, Map Workshop right-side controls, badge alignment and Finch exclusion) are open and must not be represented as fixed. No new executable has been built.

## 2026-10-11 — Map Workshop compact side-panel source change

Map Workshop's trial/encounter, map name/tags, actions and reusable-map library have been relocated from full-width rows to a 340-pixel right-hand controls column alongside the map and inspector. The saved-map list uses compact vertical rows. This is committed source only, awaiting focused Qt layout testing and Windows EXE visual acceptance; map persistence remains unchanged.

## 2026-10-11 — Comp Brainstorm Baseline / Trash draft stage guard

Comp Brainstorm now attributes late dropdown text-change events to the context actually displayed in its editor, preventing a Baseline field edit from accidentally writing into Trash during stage changes. Stage-change handling attempts to flush dirty plan-scoped drafts before redrawing and refuses to redraw after failed persistence. This is a source-level correction, not yet verified through mouse-driven Windows Qt tests or a fresh application reopen. The stage controller may already have switched after a failed flush, so additional full workflow validation is required.

## Native Coverage connections — current local checkpoint

Mechanical evidence is scoped to the selected relationship. The team-wide build-audit backlog is retained in shared review records but is not displayed as Coverage evidence.

The existing Coverage page has an effects/source/planning table, visible connection nodes, independent reach/duration/refresh cards, evidence disclosure and retained override controls. Strict shared evidence preserves multiple exact sources and status-only extension boundaries. Offscreen targeted tests passed; Windows appearance and executed group delivery remain unverified. See `docs/phase155_coverage_connections_validation.md`.

## Current highlights

### 2026-10-10 — Explicit map scale validation foundation

Support coordination now has a strict Pydantic contract for optional meters-per-drawing-unit calibration, including plan/stage scope, provenance and review status. A pure distance review reports unscaled, unreviewed or cross-stage calibrations as unresolved; only explicitly reviewed, matching calibrations produce a planned distance in meters. Even a computed planned distance never verifies actual delivery. This is service groundwork only: the Raid Map editor does not yet capture/persist calibration, and Live Raid does not yet show scaled distance. Tests are committed but not executed against the current branch.


### 2026-10-10 — Live Raid Raid Map positioning evidence handoff

Live Raid Support Ultimate cards can distinguish whether an exact-plan boss Raid Map has a saved support-chair marker, lacks the chair marker, or cannot supply usable plan-scoped positioning evidence. The range evaluation remains explicitly unresolved because saved map coordinates have no verified meters scale or recipient delivery evidence. Cross-plan layouts are rejected, and this read-only integration never changes Raid Map or databases. A typed service regression was added; UI runtime and Windows regression execution remain unverified.



### 2026-10-10 — Live Raid support evidence conflict warning

Live Raid now consolidates range and duration measurements for each assigned support chair. When fresh, stage-matched canonical build evidence supplies contradictory measurements for the same assigned ultimate, the card warns that the affected measurement needs source review instead of presenting conflicting numbers as established facts. Matching measurements are shown once. Positioning, recipients, activation and successful delivery remain unverified. A source-level regression guard is committed; current-branch runtime pytest remains unverified.



### 2026-10-09 — Health evidence classification regression repair

Health now classifies twelve legacy Craft/Fitness CP passives as non-sheet mechanics rather than false static-stat evidence gaps. Reviewed stat-sheet CP still fail closed when their calculations cannot be verified; unknown CP remains visible. Necromancer Health Avarice recognizes the saved-build Banner / Banner Bearer shorthand through the canonical Support Scribing line and continues flagging unknown skills. The Ambidextrous off-hand CP160 Gold quality warning remains an actionable saved-item proof gap until the exact off-hand quality is persisted and read back.

### 2026-10-09 — Builds inspector and bulk gear completion

The Builds right inspector now uses independent scrollable Summary, Details, and Validate tabs with persistent Save Build and To FD.my controls. Existing Scribing, Crit/Pen, gear topology, screenshot evidence, and completion actions are retained. Validate highlights canonical missing physical gear metadata with an amber border and count; the existing multi-field completion dialog now scrolls without hiding Save/Cancel. Inherited/stage-specific build behavior and database persistence are unchanged.

### 2026-10-09 — Coverage delivery-limit review

The selected-effect inspector now flags source-specific delivery risks for Pillager and Nazaray (recipient range and positioning), timed support effects including Roaring Opportunist (trigger/duration/cooldown), and status-only limits for Serpent's Disdain. Brittle prompts explicit target/application/duration review. These are review prompts, not simulated radius, activation, or observed uptime. Stage-scoped planning coverage remains separate from demonstrated execution.

### 2026-10-09 — Coverage recognizes normal support procs

Coverage counts equipped Ozezan on a healer and equipped Nazaray / Master Architect / War Machine with a recorded qualifying-bar Ultimate as normal planned support, rather than asking the raid lead to re-activate ordinary procs. Exact set-piece thresholds still apply. The shared strict planning record preserves trigger, source, bar context and explanation without converting mechanical Conditional evidence into demonstrated uptime. Optimization honors explicit manual Coverage choices and stops generic conditional warnings for these supported procs; missing sources, wrong assigned providers, backups and redundancy remain reviewable. Full context is retained in the discovery index.

### 2026-10-09 — Builds Champion Point layout and eligibility repair

Baseline and stage CP editing share three labeled Blue / Red / Green groups, each with two rows of two dropdowns. Only reference-proven slottable stars appear; Reference discipline IDs and client UI indexes are normalized separately; Green legacy ID 0 also remains readable. Saved stars regroup by discipline rather than compressed list position, retained selections keep their point values, and duplicate choices block Save. Unknown, retired passive or excess saved entries remain visible and require explicit removal before this edit can save; Cancel preserves the original build. Current U45 Craft passives are excluded even when an older reference snapshot still calls them slottable. Full context is retained in the discovery index.

### 2026-10-09 — Raid Lead Workbench for Comp Engine and Optimization

Comp Engine presents browsable Saved Build, reference and optional public-log alternatives for the selected seat and effective stage. Its bounded eight-candidate pool includes different available source families instead of letting a large log pool hide every local/reference alternative. Damage, support and independent-duty review lenses expose the questions to check, not new performance rankings. Canonical learning explanations show benefits, displaced coverage, requirements and provenance; blocked candidates remain comparable but cannot be adopted. Selection is a temporary review basket, not a Saved Build write. Full context is retained in the discovery index.

### 2026-10-09 — Encounter-aware Readiness review

Readiness offers an explicit background **Check Boss Mechanics** action for the selected effective Raid Plan boss stage. It resolves exact Saved Builds, composes canonical roster/handling evidence, and presents assignments, build support, handling knowledge, observed execution, location/window availability and risks separately. Results invalidate after stage, build or assignment changes. Missing corpus, strategy bindings and observed execution remain unresolved; maps and manual readiness do not prove encounter execution. Scoped supplemental strategy/observation contracts exist for canonical consumers; the current UI does not fabricate or import those observations. Full context is retained in the discovery index.

### BFF / FoundryDock Feature Index

- **Comp Brainstorm draft workspace** — Team → Comp Brainstorm provides a low-authority 12-seat composition notebook with Trash / Boss 1 / Boss 2 / Boss 3 contexts, per-seat Saved Build binding plus Armor / Mythic / Monster Set / Weapons notes, live Crit/Pen preview through the canonical Raid Plan offensive-stats service, an exactly-12-item persistent manual checklist matching the default required raid effects, named brainstorm saves in additive user-database tables, and an explicit current-context promotion to a new Raid Plan. Checklist state never feeds Coverage, Comp Maker, Optimizer, or Crit/Pen calculations; no autosave or hidden Raid Plan mutation occurs. Full context is retained in the discovery index.

### Phase 15.5 Field Guide Access
- Assignments, Builds, Coverage, and Readiness show a compact `?` help control in the page header. Each opens the shared offline Field Guide with practical page-specific text guidance while dedicated illustrated help assets are not yet available. Existing help pages and planning data remain unchanged.

- **Shared named-buff interaction evidence (Phase 15.5, initial slice):** Canonical named-effect resolver now exposes immutable, strict evidence for duplicate-source suppression and compatible Major/Minor variants on the same modeled objective. Mechanical-only output does not infer execution, recipients, or raid DPS. Coverage UI wiring and wider cross-reactivity families are pending validation.

- **Phase 15.5 Coverage connections and delivery inspector (2026-10-09):** Native Coverage links selected effects to shared exact-build interaction evidence, including compatible named effects, routine support sources, Orb supply and canonical status-only duration modifiers. An explicit background review exposes beneficiaries, prerequisites, per-source range/duration/cooldown and unresolved access/execution; refresh invalidates results and late stale results are rejected. Provider/source search, manual overrides and Known Sources remain available. Unknown values stay unknown; no universal group reach or uptime is inferred.

## Full discovery index

Search these retained entries for older knowledge; dates do not imply a fresh validation.

- [2026-10-09 — Health evidence classification regression repair](docs/archive/governance_2026-10-10/FEATURES.md)
- [2026-10-09 — Builds inspector and bulk gear completion](docs/archive/governance_2026-10-10/FEATURES.md)
- [2026-10-09 — Coverage delivery-limit review](docs/archive/governance_2026-10-10/FEATURES.md)
- [2026-10-09 — Coverage recognizes normal support procs](docs/archive/governance_2026-10-10/FEATURES.md)
- [2026-10-09 — Builds Champion Point layout and eligibility repair](docs/archive/governance_2026-10-10/FEATURES.md)
- [2026-10-09 — Raid Lead Workbench for Comp Engine and Optimization](docs/archive/governance_2026-10-10/FEATURES.md)
- [2026-10-09 — Encounter-aware Readiness review](docs/archive/governance_2026-10-10/FEATURES.md)
- [BFF / FoundryDock Feature Index](docs/archive/governance_2026-10-10/FEATURES.md)
- [App / General](docs/archive/governance_2026-10-10/FEATURES.md)
- [Character & Build Management](docs/archive/governance_2026-10-10/FEATURES.md)
- [Build Import](docs/archive/governance_2026-10-10/FEATURES.md)
- [Exports & Sharing](docs/archive/governance_2026-10-10/FEATURES.md)
- [Character Overview Dashboard](docs/archive/governance_2026-10-10/FEATURES.md)
- [Builds Editor](docs/archive/governance_2026-10-10/FEATURES.md)
- [Rotation Builder](docs/archive/governance_2026-10-10/FEATURES.md)
- [Performance Dashboard](docs/archive/governance_2026-10-10/FEATURES.md)
- [Combat Reference](docs/archive/governance_2026-10-10/FEATURES.md)
- [Roster](docs/archive/governance_2026-10-10/FEATURES.md)
- [Phase 14 Builds progression ownership](docs/archive/governance_2026-10-10/FEATURES.md)
- [Rumors collection ledger](docs/archive/governance_2026-10-10/FEATURES.md)
- [Team Discord links](docs/archive/governance_2026-10-10/FEATURES.md)
- [Personnel lifecycle and history](docs/archive/governance_2026-10-10/FEATURES.md)
- [Team deletion and cleanup](docs/archive/governance_2026-10-10/FEATURES.md)
- [Live Raid encounter context](docs/archive/governance_2026-10-10/FEATURES.md)
- [Live Raid linked Raid Maps](docs/archive/governance_2026-10-10/FEATURES.md)
- [Objective #32 theoretical closure hardening](docs/archive/governance_2026-10-10/FEATURES.md)
- [Objective #32 weapon standing passive runtime coverage](docs/archive/governance_2026-10-10/FEATURES.md)
- [Objective #32 passive rank evidence authority](docs/archive/governance_2026-10-10/FEATURES.md)
- [Objective #32 shared sustain evidence hard gates](docs/archive/governance_2026-10-10/FEATURES.md)
- [Raid Plan save hardening and overview consolidation](docs/archive/governance_2026-10-10/FEATURES.md)
- [Comp Maker saved-Build source separation](docs/archive/governance_2026-10-10/FEATURES.md)
- [Saved Build / Template / Raid Plan assignment boundary](docs/archive/governance_2026-10-10/FEATURES.md)
- [Reface performance and focused workspace tabs](docs/archive/governance_2026-10-10/FEATURES.md)
- [Live Raid raid-speed reface](docs/archive/governance_2026-10-10/FEATURES.md)
- [Readiness guided reface](docs/archive/governance_2026-10-10/FEATURES.md)
- [Strategy / Raid Map map-first reface](docs/archive/governance_2026-10-10/FEATURES.md)
- [Raid Plan first-order authoring + startup shell hardening](docs/archive/governance_2026-10-10/FEATURES.md)
- [Comp Maker learning explanations (2026-09-28)](docs/archive/governance_2026-10-10/FEATURES.md)
- [Raid Planner Home Wiring](docs/archive/governance_2026-10-10/FEATURES.md)
- [Phase 15 Clean-Shell Raid Plan Island](docs/archive/governance_2026-10-10/FEATURES.md)
- [Phase 15 Raid Plan clean-page boundary](docs/archive/governance_2026-10-10/FEATURES.md)
- [Phase 15 Urban Wilderness visual system refresh (2026-09-29)](docs/archive/governance_2026-10-10/FEATURES.md)
- [Phase 15 Readiness Command Board](docs/archive/governance_2026-10-10/FEATURES.md)
- [Phase 15 Strategy / Raid Map contextual editor (2026-09-30)](docs/archive/governance_2026-10-10/FEATURES.md)
- [Phase 15 shared navigation sprite icons](docs/archive/governance_2026-10-10/FEATURES.md)
- [Phase 15 Finch / FD.my publishing controls (2026-10-01)](docs/archive/governance_2026-10-10/FEATURES.md)
- [Phase 15 semantic sprite icon system](docs/archive/governance_2026-10-10/FEATURES.md)
- [Phase 15 Raid Plan Optimization](docs/archive/governance_2026-10-10/FEATURES.md)
- [Canonical physical gear metadata preservation (Phase 14 validation)](docs/archive/governance_2026-10-10/FEATURES.md)
- [Phase 14 — Damage-family-scoped Champion Point power](docs/archive/governance_2026-10-10/FEATURES.md)
- [Saved-build physical metadata readiness audit](docs/archive/governance_2026-10-10/FEATURES.md)
- [Canonical gear-evidence physical metadata backfill](docs/archive/governance_2026-10-10/FEATURES.md)
- [Builds — Missing Physical Metadata Completion](docs/archive/governance_2026-10-10/FEATURES.md)
- [Phase 14 — Saved-build runtime authority and reviewed Templar damage components](docs/archive/governance_2026-10-10/FEATURES.md)
- [Phase 15 encounter recommendation staging](docs/archive/governance_2026-10-10/FEATURES.md)
- [Phase 15 encounter team-plan conflict aggregation](docs/archive/governance_2026-10-10/FEATURES.md)
- [Phase 15 encounter team-impact summary](docs/archive/governance_2026-10-10/FEATURES.md)
- [Phase 15 — Encounter Team Verdict](docs/archive/governance_2026-10-10/FEATURES.md)
- [Phase 15 encounter decision record](docs/archive/governance_2026-10-10/FEATURES.md)
- [Phase 15 encounter approval packet](docs/archive/governance_2026-10-10/FEATURES.md)
- [Phase 15 approved apply bridge](docs/archive/governance_2026-10-10/FEATURES.md)
- [Phase 15 approved Raid Plan persistence](docs/archive/governance_2026-10-10/FEATURES.md)
- [Phase 15 Optimization UI — Encounter Decision Review](docs/archive/governance_2026-10-10/FEATURES.md)
- [Phase 15 Encounter Review Receipt](docs/archive/governance_2026-10-10/FEATURES.md)
- [Phase 15.5 Field Guide Access](docs/archive/governance_2026-10-10/FEATURES.md)

Full original evidence and wording: [dated source](docs/archive/governance_2026-10-10/FEATURES.md). Historical counts and completion claims apply only to their recorded checkpoint.

## Concurrent branch evidence retained

Newer shared-branch records were preserved during integration: [checkpoint f08ff6f15](docs/archive/governance_2026-10-10/concurrent_f08ff6f15/FEATURES.md). This evidence includes cached Coverage/Comp handoffs and plan/stage invalidation checks; its original confidence and CI status remain scoped to that checkpoint.

## Coverage interaction wiring — 2026-10-10 UTC

The native selected-effect inspector consumes exact plan/stage Saved Build audits through the shared intelligence service. Every source remains visible with separate delivery values; Pillager equipment capability uses reviewed piece thresholds and does not imply activation. Source-specific delivery notes, retained override/Known Sources controls and Review in Rotations use existing owners/routes. Cached Coverage-to-Comp evidence and support-set handoffs remain connected and scoped. Review runs on demand in a background worker, rejects stale results and waits safely at shutdown.

- **Planned Support Ultimate map reach (service foundation):** Derives an explicit plan/stage-scoped scale from two reviewed-reference coordinates and a user-supplied known distance; shared evaluation distinguishes missing markers, unknown range, unscaled/unreviewed/mismatched calibration, and inside/outside planned range. This is planning evidence only, never proof of activation or delivery. Persistence, Raid Map editing, and UI consumers remain pending; regression tests committed but current-branch execution not yet verified.

- **Raid Map calibration persistence foundation:** Plan/stage-scoped reference points and user-supplied known distance now have versioned validated user-data persistence, verified read-back, atomic writes and stale-edit checks in `EncounterRaidMapStore`. This does not yet provide editor controls or live consumers; workflow remains incomplete and tests are not yet executed against this branch.

- **Raid Map calibration editor (initial workflow):** Existing Strategy/Raid Map inspector now has a Calibrate Map Distance action. It accepts two manual drawing-coordinate pairs, a known meter distance, provenance and an explicit reviewed/unreviewed decision; uses stage- and plan-scoped read-back persistence with revision checking. This is not yet graphical point selection or Live Raid/Coverage/Readiness reach integration. Real-build UI and pytest execution are not yet verified.

- **Live Raid canonical map loading correction:** Live Raid now acquires `EncounterRaidMapStore.for_application()`, matching Strategy/Raid Map's user-owned map location and additive legacy handling instead of opening reference data storage directly. Structural wiring regression: `tests/test_live_raid_plan_map_store_wiring.py`. Does not yet render calibrated recipient-range verdicts; current-branch runtime validation remains pending.

- **Live Raid calibrated-scale visibility:** Support Ultimate cards now read the exact-plan/boss `distance_reference.json` record through canonical user map storage and display reviewed vs unreviewed meters-per-drawing-unit scale with explicit recipient-reach and delivery limitations. Does not yet compute per-recipient distances or prove combat delivery. Focused source-wiring regression committed; executable UI/pytest validation pending.

- **Live Raid preliminary calibrated seat-distance display:** When the exact plan/boss map has unique seat markers, a reviewed scale, and one nonconflicting build-backed Ultimate radius, Live Raid uses the shared planned-reach evaluator to show mapped seat distances as within/outside that radius. Seat presence does not prove recipient eligibility or actual effect delivery. Duplicate seat markers are omitted. UI/runtime and pytest verification remain pending; Coverage and Readiness consumers remain open.

- **Calibration input hardening (2026-10-10):** The persisted reference-point Pydantic model now rejects NaN/infinite coordinates and whitespace-only plan, stage, or provenance fields at its own validation boundary rather than relying on a later scale calculation. Regression cases committed; current branch execution remains unverified.

- **Cross-stage calibrated-position guard:** Live Raid skips calibrated support map coordinates and reference-scale presentation when the selected assignment stage differs from the displayed boss encounter id. Prevents a map scale/seat position from being reused across unrelated contexts; dedicated structural regressions added. Full current-branch runtime execution remains outstanding.

- **Live Raid range-geometry evidence wording (2026-10-10):** Calibrated seat separation is compared against the reported ability range without assuming that generic `InteractionSource.range_meters` is an area-effect radius. Targeting geometry, recipient eligibility, and activation/delivery remain unverified. Stage-matching guard now applies to presence markers as well as coordinates and scales. Regression expectations updated; current-branch execution remains pending.

- **Support range geometry contract (2026-10-10):** `InteractionSource` now carries optional `range_geometry` (`unknown` default, `cast_distance`, `effect_radius`); the support review preserves it. Live Raid now withholds planned effect-radius reach conclusions unless the source explicitly says `effect_radius`. Numeric range alone is not proof of radius, eligibility, or delivery. Regressions committed; current-branch runtime execution remains pending.

- **Live Raid radius-evidence messaging:** In the explicit effect-radius path, the UI now acknowledges sourced radius geometry while continuing to mark recipient eligibility, activation and actual delivery unverified. Updated its regression assertion. No new effect-specific targets are inferred.

- **Range geometry evidence consistency (2026-10-10):** Strict `InteractionSource` now rejects explicit cast-distance/effect-radius classifications when no numeric `range_meters` fact exists. Legacy sources with unknown geometry and no range remain valid. Targeted regressions committed, but current-branch execution and UI consumer testing are still pending.

- **Live Raid boss context identity correction (2026-10-10):** Calibrated map reads now check saved assignments against the active Raid Plan and full stage-controller key (`boss:<id>`) instead of comparing that key with the bare encounter guide ID. The old comparison could suppress legitimate boss map evidence. Structural stage-wiring regression updated; current-branch tests and UI interaction remain unverified.

- **Assignments JSON-array save compatibility (2026-10-10):** Strict Pydantic assignment save now accepts genuine list/tuple inputs for jobs and seat groups, explicitly normalizing them to tuples before nested validation. Strings, dictionaries, numbers and null remain invalid. A real failure in the uploaded sandbox was reproduced and fixed (3 assignment tests passed); GitHub regression committed but full current-branch test execution is pending.

- **Calibration layout-revision binding (2026-10-10):** Newly saved Raid Map references record the saved diagram's map ID. Live Raid now withholds calibrated-range evidence when the layout changed, is absent, or calibration predates layout binding. Older calibrations remain loadable but require recalibration before providing reach conclusions. Structural regressions committed; current-branch Qt and pytest execution remain pending.

- **Finch collaboration native Phase 15.5 navigation (2026-10-10):** The existing read-only collaboration overview is now registered in the native shell with an explicit Finch research route. Its page/workspace signals are connected to existing owning pages; remote snapshot context does not automatically bind or overwrite local plan/stage selection. Native-shell structural regressions added; Windows user interaction acceptance remains outstanding.

## 2026-10-15 — Granite is the default Wyrdworks appearance

## 2026-10-15 — Granite is the default Wyrdworks appearance

Granite now applies automatically, including when an older install saved Urban Wilderness. Settings reports the fixed appearance instead of offering theme selection. Cards use static, low-contrast stone texture, rounded clipping and inset stone borders; controls use smooth graphite, muted brass selected states and ivory text. Lavender is reserved for conflict cues. Backgrounds retain stone texture while cards use quiet graphite shading.

Existing page and inline teal styles are normalized for Granite, and collectible meters consume its neutral palette. Thirty-seven recreated collectible badges are packed into one transparent, padded atlas at `assets/themes/granite/collectibles` and loaded through the existing lazy sprite cache; the stone texture is at `assets/themes/granite/granite_stone.png`.

Original badge files and all saved plans, builds, databases, maps and outer-window dimensions are retained. See `docs/granite_theme_validation.md` for actual validation scope and remaining packaged acceptance.

## 2026-10-15 — Smooth charcoal dashboard and lean plan header

The latest Wyrdworks direction supersedes the earlier blue-slate palette: neutral charcoal backgrounds and smooth, worn soapstone surfaces use soft gray edges instead of gold box outlines. Brass remains in the brand, section accents and FD.my action; violet is a restrained selection cue independent of role bars.

The persistent lean header uses the supplied name logo and fjord artwork, a sidebar hamburger, current team/encounter, actual assigned-player count and saved meeting schedule. Plan Details opens the existing identity fields; the three-dot control expands the existing plan loader.

Share / Export produces the canonical saved-plan JSON backup, and Send to FD.my reuses the existing Finch publisher asynchronously, requiring a saved, unchanged plan. Roster schedule lookup is read-only. Databases, parked functionality and saved data are retained.

## 2026-10-15 — Granite Collectibles cabinet treatment (GitHub source)

The Granite Collectibles dashboard uses the packed atlas JSON's explicit trimmed frame rectangles for its 24 active collection navigation cards, preserving the varied shield, book, medallion and artifact silhouettes instead of assuming uniform 8×5 cells.

Armor Styles and Weapon Styles remain distinct. The Granite-only presentation now uses dark beach-stone slate, warm ivory, subdued aged brass progress tracks and 62px contained badge artwork within unchanged 72px image slots.

The real owned/total counts now also show a numeric percentage per category; profile-driven totals and category navigation are unchanged. The Granite Collectibles hub gains coordinated dark-stone surfaces without repainting other themes.

GitHub edits are source-only and require local PySide6 visual/runtime validation; no database changes.

## 2026-10-15 — Builds and Workshop layout repairs (source-only checkpoint)

Builds roster font increased to 15px and row padding restored to separate player identity lines. The Builds inspector's existing functional Summary, Details and Validate tabs now have clearer tab geometry and selected-state contrast.

Map Workshop's Map Library/Selected Item tab labels, right-column bounds and library button grid receive additional spacing. The redundant Phase 15 workflow footer previous/next buttons are hidden; the primary sidebar still owns navigation.

These are GitHub source commits only; the user's running Windows executable was not updated and Qt geometry/runtime tests have not run.

Built-in Workshop default-background selection and the duplicate top hamburger/wordmark header still require investigation. No saved data or schema changes.

- **Soapstone button refinement:** Adapted the supplied Wyrdworks component reference into existing Granite and Raid Plan style owners: softer corners, a gray lifted hover, inset charcoal pressed state and visible warm keyboard-focus edges. Selected controls retain restrained violet accents. Existing dimensions, actions and role colors are preserved; no replacement widget framework or selectable theme was added.

## 2026-10-15 — Museum Collectibles artwork

The Granite Collectibles dashboard loads 24 museum exhibit illustrations from the bundled `assets/themes/granite/museum_collectibles/` runtime directory using `museum_collectibles_manifest.json` and canonical category keys. Missing or unreadable exhibits fall back to the existing Granite badge atlas without disturbing counts, navigation, or the original 37 images. Focused local PySide6 tests verify asset decoding, runtime selection and fallback behavior; packaged Windows visual acceptance remains outstanding.

## 2026-10-15 — Wyrdworks Raid Ribbon (locally validated; packaged acceptance pending)

Raid Plan now constructs `WyrdRaidRibbon` from `ui/components/wyrd_raid_ribbon.py` in place of the old compressible stage strip. The ribbon reads the existing saved stage sequence and calls the existing stage-selection method; it owns no order or persistence data. Stages have a fixed, image-backed size, a hidden horizontal scrollbar, conditional brass navigation arrows, gentle edge-hover navigation, Shift+wheel scrolling, and automatic reveal of the active stage. Repeated Trash stages remain distinct through their persisted context keys. Artwork is resolved from matching files in `assets/raid_plans/trial_banners/<trial folder>/` using the boss name or shared Trash image, with trial-banner and dark-panel fallbacks. No image editing or new image registry is required. Stage insertion, removal, and rearrangement remain owned by existing Raid Plan services, **not** the ribbon. Focused Windows Qt regressions cover stage ordering, repeated Trash identities and constrained geometry; packaged/manual visual acceptance remains outstanding. The original shared `Phase15StageBar` remains intact for other consumers.
## Compact instrument-panel Raid Plan header

The fixed 72px header uses thin_top_bar_logo.png and the existing mountain art beneath a static 70% charcoal overlay. Five native controls share centralized, beveled charcoal/brass styles with gold FD.my primary, static keyboard focus and distinct disabled/pressed states; ordinary header states contain no violet. Sidebar collapse remains on the rail. Plan Details and overflow expose existing details/loader controls, export and FD.my reuse existing handlers. Duplicate saves and verifies a new RaidPlan snapshot without replacing its source; independent map layouts and stage assignments are not cloned. Existing window dimensions and data owners remain intact.

Header metadata now pairs small people/calendar symbols with player count and the saved schedule. Matching weekly blocks compact to “Mon & Wed 9:00 - 11:00 pm”; distinct blocks remain distinct and the original schedule/timezone stays in the accessible tooltip. Transparent padding is cropped at runtime to enlarge the supplied logo within the same 72px header. Stored times and source artwork are unchanged.

## Oversized logo and editable team meeting schedule

The header now adds a stronger static charcoal fade on the left and deliberately oversized brand artwork within the existing header slot; the logo yields space at narrow widths instead of enlarging the window. The calendar icon opens a compact native modal for the existing team's meeting days, start/end times and timezone. Save uses the existing RosterService validation/write owner with transaction, expected-snapshot protection and exact readback; opening and Cancel do not bootstrap or write the database. Team focus/Discord metadata, other teams and unsaved Raid Plan notes remain intact. Failed/stale saves retain the modal draft. No database replacement, new schema or game-mechanics change.

- Header button assembly now sits 5px higher to give the lower bevels additional clearance, retaining the 72px header and existing window geometry.


## Raid Plan inline tactical map tools

The middle map now exposes a compact, collapsible Granite tool rail and contextual object inspector without navigating away from Raid Plan. Editing constructs the existing EncounterBoard only on the first tool action and binds the exact saved plan/stage through Phase15RaidMapWorkspace. Select uses native drag/marquee selection plus Shift-click, keyboard delete/Escape and undo/redo; wheel zoom and middle-drag pan stay on the canvas, without added zoom buttons or compass artwork. Circle, rectangular analysis region, mechanic marker, text, precision/freehand movement path, arc/sweep, target, existing roster-seat placement and non-destructive layer visibility are available. Objects can be labelled, moved, resized, associated with phase/seat/mechanic references, locked or hidden through contextual fields where applicable. Hidden objects remain available in the object picker. Existing formation templates remain owned by the shared board.

Ordered route knots and cubic handles are preserved as validated normalized-scene geometry in the existing EncounterBoard layout, with stable annotation identity, direction, line style, designed-route provenance and analysis-region flags. Routes can be reshaped with handles, smoothed, reversed, duplicated and have individual points inserted/removed. Shared token/zone records retain object identity, lock/visibility and phase fields; circular zones retain fill opacity and map-relative radius semantics. No meter radius or observed movement/heatmap statistic is inferred.

Edits retain per-plan/stage drafts; Save map revalidates the visible context and uses the existing plan-map save, preview and linkage owners. Existing image markings cannot be reconstructed as editable objects: raster-only maps remain background art and no default boss/player positions are invented. Original reusable maps, assignments, plan records, the outer window and surrounding dashboard layout remain owned by their existing components.

The inline map inspector has a keyboard-accessible collapse/restore edge tab with a remembered UI preference, returning its width to the canvas. Add map imports a local image, selects bundled encounter artwork or copies a matching reusable Workshop layout into the active stage draft. Image changes retain existing objects; editable library replacement is explicit and undoable, and the source map remains unchanged. Save map remains the action that links the draft to its exact Raid Plan stage.

New inline maps without a saved or linked background use the supplied assets/raid_maps/built_in/granite_astrolabe_map.webp. Add map also offers actual built-in backgrounds alongside encounter artwork. Saved stage backgrounds remain authoritative.

### Map Workshop corner frame experiment
Workshop-only, reversible ornamental overlays frame the canvas, tool rail and inspector. Centralized Granite profiles use 1.5px straight brass edges, 20/18/16px corners respectively, and a narrow recessed inner edge. Four independent corner slots reuse existing transparent brass artwork; no new decorative assets were generated. Content padding keeps decoration clear of controls.

Workshop frame layering experiment: recessed perimeter, connecting brass rails, soft corner shadows, independent transparent ornaments and final restrained highlights. Facing rail/editor corners are quieter without resizing artwork or changing layout.

Workshop material experiment: Stone & Brass on the editable workspace, Frosted Soapstone on the drawing rail/library and Weathered Brass on Selected Item. Static frame-only rail gradients and 85% ornament artwork retain existing anchors, inset shadows and layout.

Readiness Summary now places four substantial status tiles above Top Items, with separate title/status typography and an attention count. The stage ribbon fills the content width, adapting short strips and retaining horizontal navigation for long strips, with a darker text scrim. Raid Plan map offers a Hand tool for left-drag panning and a selection-aware toolbar Delete action using existing lock protection and undo. Workshop material frames retain size/artwork with slightly stronger recess, highlights and lower-edge depth.

Sidebar width changes now preserve the Raid Plan outer-page scroll offset through adaptive reflow, including temporary range clamps; explicit scrollbar/wheel input cancels restoration. Header secondary controls retain their geometry and use a visible stone lower bevel rather than a nearly black disappearing edge.

Raid Plan frame experiment: Team, Fight and Readiness share Weathered Brass frames; Selected Build, Overall Readiness, Top Items, Raid Lead Notes and mechanics/timeline content use quieter Frosted Soapstone. Existing corner renderer, artwork, shadow layering and 85% ornament scale are reused. Experiment is reversible without altering layout or map state.

### Raid Plan Fight workspace refinement (2026-10-16)
Small independent corner fasteners, nearly opaque ribbon label backing and an inset horizontally navigable stage rail follow the mockup. Raid Plan drawing controls use a charcoal/brass rail with Hand, protected Delete, Add Map, Undo, Redo and verified Save; routine instructions and the Planned Route strip are hidden. Jewel controls collapse the rail/properties. The default map fills the frame by cropping at the viewport, preserving artwork aspect ratio and normalized object coordinates; wheel zoom and pan remain available. Named-attack search is hidden reversibly. Compact recorded flight/downtime controls sit above the map; the four lower controls are Mechanics, Health Timeline, Assignments and Route Notes, with no ordinary violet selection. Health runs 0% left to 100% right. Portrait cards below show other source-backed mechanics and short descriptions, with explicit unknown health triggers. Assignments opens a compact stage modal over the existing canonical state, retaining hidden/unrelated fields and rejecting stale writes. Route Notes saves with the stage map and can highlight an existing visible editable movement path; unsaved note text is retained in memory when using Show Route. No heatmap or observed movement inference is claimed.


Readiness surface refinement: bundled charcoal stone on the Raid Plan Readiness surface and overview, with a clearer fine rail and deeper recessed edge. Small fasteners, layout and status meanings are unchanged.

Raid Plan frame rails now retain subtly rounded continuous corners beneath the existing small corner fasteners, removing diagonal clipped joins.

Raid Plan map surround uses a stronger 2px Stone & Brass rail and recessed inner edge through the shared frame renderer, retaining small corner hardware.

### Dark fantasy visual branch — 2026-10-17
Shared Qt controls use graphite surfaces, moonstone silver trim, ivory text and smoky amethyst selection. Raid Plan uses the supplied Wyrdworks logo; semantic icons resolve to the supplied dark fantasy sheet. Experimental brass/stacked-stone appearance layers are disconnected. This is a local visual development branch; full active-workflow visual acceptance is pending.

The detailed dark fantasy treatments now include distinct textured application/workspace/panel/card/raised surfaces, six control states, segmented/tab rails, bevel inputs, silver dividers, native modal blur/dimming, and a context footer with working map zoom. Footer text reflects actual context; it does not assert that drafts were saved. These changes remain on the isolated visual branch.

The reference sidebar now uses compact flat navigation, ivory outline icons, a small wordmark, thin group dividers and a single amethyst active row. Its icon-only rail expands temporarily on hover without changing the saved collapse preference.

Image-based stone surface textures are removed from the application, workspace, cards, controls, dialogs and footer. Palette colors, code-drawn gradients/bevels, borders, shadows, outline navigation and artwork remain.

Input fields use a recessed graphite bevel with muted placeholders and steady silver focus, including native dropdown arrow separators and single-bordered editable combo/spin editors. All surfaces remain code-drawn.

Action buttons now show six distinct code-drawn reference states: beveled normal, brighter hover, recessed pressed, amethyst selection, bright-rimmed primary/default and muted disabled. State transitions keep border width fixed and disabled clicks remain native.

Raid Plan now uses joined amethyst/graphite segment rails, a boss/stage bar pinned above its scroll, and a compact map toolbar with advanced tools under More. Quick notes save to the exact plan/stage through existing map storage and appear in the published map consumed by Live Raid. Mouse zoom/pan remains; the footer zoom slider and percentage display are removed.

### Contextual Raid Plan refinements (2026-10-17)

The latest layout direction supersedes the full-width pinned boss bar: the existing boss/stage ribbon now sits inside the center Fight column, immediately above its encounter content and square map, between Team and Readiness. Roster has no boss bar or reserved bar space. No Predot slider or map zoom/percentage controls are added.

Mechanics, Health Timeline, Assignments and Route Notes are four views of the same active Raid Plan and stage. The information viewport scrolls independently at a stable height; tab changes retain the map object, coordinates and window size. Mechanics expand inline to show explicitly linked saved jobs, source links and stage notes. The health rail runs 100% to 0%, supports keyboard/mouse threshold selection, and keeps incomplete thresholds explicit. Stage assignments group actual players/build references and responsibilities; focused edits reuse the existing guarded assignment dialog. Route Notes reads the same stage map's paths, movement instructions and text annotations, including retained local drafts; editing and highlighting reuse existing map actions.

Team → selected player → Edit Build and Readiness → Stage loadouts open the same existing Builds editor in a resizable modal. Its local selector browses Baseline, saved bosses, enabled Predot setups and separate Trash encounters without changing the shared selected boss or rebuilding the map. Each boss has one Combat configuration shared by its mechanic phases. Existing sparse build variants, saved identity, equipment/skills/CP/scribing editors, validation, calculations and save/readback remain authoritative. Predot setups explicitly require switching before engagement and do not claim effects persist after source gear removal. The Team summary resolves the saved build for the active encounter.

The sidebar now uses the supplied large menu-sheet icons. Shared semantic controls use the supplied silver/amethyst action sheet; remaining vector fallbacks are neutral silver. Typography follows the central Forum/Montserrat families and system fallbacks.

The latest surface palette is darker: background `#070809`, surface `#111315`, secondary surface `#212427`, panel `#16181A`, raised surface `#2B2E32`, sidebar and empty map canvas `#0D0F11`. Existing page/theme rules resolve through the shared palette, including modal and local card projections; artwork is preserved.

The header's lower edge fades into the same dark app background as the page gutter, removing the lighter strip above Team and the other workspace panels.

The header logo has a subtle static black drop shadow, styled centrally and confined to the logo's existing space.

Startup uses the supplied harbor splash illustration without cropping its lettering. The Windows application and packaged executable use the new knot artwork, encoded as a proper icon with standard shell sizes.

The Collectibles dashboard uses the new fantasy badge atlas and collection-room background. Display crops remove the badges' baked-in caption plaques; live category titles, progress and category navigation retain their existing identities. The badge grid reserves enough height to keep artwork clear of the progress bars.

### Larger navigation and frameless map tools

The navigation header uses a hamburger button in both expanded and collapsed modes, without the wordmark or spearhead emblem. Sidebar icons use the supplied warm champagne artwork with purple accents; shared interface actions use the matching champagne atlas for the same finish. Menu text is 16px with 32px icons and 46px rows; the expanded/collapsed widths are 232px/58px. Hover expansion and existing navigation remain available.

The five compact map controls float directly at the map's upper-left corner. Their container occupies no side column and only the button areas intercept input. Both side-strip collapse handles are hidden; object properties remain available under More. The square map fills available center-column space up to 760px, retaining mouse zoom/pan and saved coordinates.

When no map is selected, the Map panel shows the supplied Ashen Vale map. Encounter maps and saved drafts take precedence; the decorative default does not count as a reviewed encounter map.

The Fight heading places its sword beside the title with the divider directly below; its contextual tabs use a close-fitting frame. Map Workshop keeps step editing in Animate and places the existing playback buttons at the bottom of that Position Timeline inspector, with no duplicate timeline rows above the canvas.

Large outer workflow panels currently preview the supplied stone tablet artwork with more rounded corners. The frame uses fixed-size corners and a continuous center texture; nested cards, controls and map artwork retain their existing appearance.

Per the latest direction, the health rail runs 0% left to 100% right. It uses a recessed colored band, restrained ticks and compact icon-labelled phase cards in increasing health order. Bands split only at recorded health thresholds; unknown thresholds remain explicit and no percentages or elapsed times are invented.


### Granite / fantasy blend preview (2026-10-18)
The current blend uses Granite charcoal palette and raised grey inner surfaces with the supplied `assets/themes/granite/panel_bg.png` on large outer workflow panels. Dark-fantasy navigation, champagne icons, branding, splash, Windows icon, footer, modals and contextual Fight/map behavior remain. The boss ribbon now spans above all three Team/Fight/Readiness columns on its own matching backing, superseding the center-only placement above. Granite segment painting retains the portrait on the left and names over the dark right half. Stage identity/order/selection remain owned by the existing Raid Plan; backing and painting own no saved data. The short ribbon backing explicitly qualifies for the same cached paint-only surface; nested cards remain raised grey.


### Raid Plan stone layers (2026-10-18)
The stone slab preview is now restricted to Raid Plan, superseding its earlier use on other workflows. Roster, Builds, Assignments, Strategy and Map Workshop retain smooth code-painted surfaces. Raid Plan retains `panel_bg.png` on its three large columns. Its map uses `granite_top_panel_smooth.png` behind the map with a 2px visible rim, fixed vertical sizing and no surplus vertical padding. Only the full-width boss ribbon backing uses `granite_top_panel_rough.png`; rough texture is not spread across inner cards. Raid Plan action buttons use `granite_button_grey.png`, with muted-purple checked states, pressed/focus/disabled treatments and unchanged border metrics. Titles use champagne serif lettering with a restrained shadow, ivory for the readiness summary title, and champagne atlas icons on the contextual map tabs. Original PNGs remain unchanged, decoded/cropped at runtime or sliced by native Qt; no additional theme, preference, data or save owner is introduced.

The Raid Plan stone loader accepts replacement artwork at different resolutions and scales its gutter crop proportionally, instead of suppressing panels when image dimensions change. Restart the app to reload a replaced image from the existing decoded-image cache.

Raid Plan now previews a darker stone finish: a cached 36% obsidian wash darkens the main slab texture while preserving transparency and original PNG bytes. Code-painted details use Blackstone #0B0B0B, Charcoal #111111, Graphite #161616, Dark Slate #1B1B1B, Slate #222222, Stone #2F2F2F and Pewter #646464; deepest shadows/map surround use Obsidian #040404. Champagne text/icons and semantic/selected accents remain readable.

The new Wyrdworks Dark Fantasy Icon Atlas supplies 44 transparent gold navigation, role and action symbols through the existing shared icon resolver. Presentation labels and decorative tiles are excluded; the full supplied sheet is preserved. Matching sidebar and application actions share these glyphs; unsupported specialist icons retain existing fallbacks. Navigation and parked-page scope are unchanged.

Boss ribbon names and subtitles now begin beyond the portrait, on the dark right-hand backing. Narrow stage cards reduce title size slightly and elide overflow; the full stage label remains available in its tooltip. Stage identity and card dimensions are unchanged.

Inner card backgrounds, including Overall Readiness and Top Items, now use a dark blue-charcoal gradient (#141D23 → #10181E → #0C1217) with cooler recessed edges, matching a darker relative of the button artwork. Stone slabs, image files, warm titles/icons and selection/status cues are retained.

The four readiness status tiles now have a cool raised face, restrained top/left bevel and short dark shadow instead of continuous state-colored outlines. Badge colors, counts, labels and layout remain unchanged.

Team, Fight and Readiness column titles no longer show divider lines beneath them; the hidden compatibility widgets reserve no layout space.

Gear, Gear Trends, Achievements, Collectibles and Finch now use the five matching symbols from the supplemental Dark Fantasy Icon Atlas. The crystal retains its purple facets, and Finch uses the new bird instead of the notes fallback. Existing sidebar routes, sizes and hover behavior are preserved.


### Smooth ribbon bevel and standalone-button preview (2026-10-18)
Raid Plan's full-width boss ribbon now uses the smooth panel material with an 8px rounded bevel and neutral cool shadow instead of rough stone. The stage cards have rounded artwork clipping, cool dark label backing, restrained raised edges and 6px separation; existing plan stage order, identity, selection and horizontal reveal remain authoritative. The supplied wide/square nine-slice button images preview only on ungrouped Raid Plan controls, including its separately hosted header. Icon-only controls use square artwork and text controls use wide artwork. Grouped tabs/filters, phase buttons and map tools retain prior styling, and other pages are excluded. Native QSS uses fixed 5px borders and authored transparent corners (no additional radius clipping), with cached prebuilt hover/pressed/selected/disabled variants. Original PNGs are preserved; compact transparent UI derivatives and crop/source hashes are recorded in the asset receipt. No new theme selector or persisted setting is added.


### App-wide stone-derived palette (2026-10-18)
The user's new palette now replaces the earlier neutral/cool palette throughout the existing Granite theme: background #101112, panel #1C1D1F, card #242527, button #303134, hover #3B3D40, selected #44474B, divider #484B50, control border #85898E, selection outline #C8CDD2, text #F0EDE6, secondary text #B9B8B3, gold heading #D8C39F. Status colors are covered #9FC4DD, review #E2BE77, unknown #B9B8B3 and blocked/conflict #E6A477. Existing readiness key Planned remains Planned; color changes do not equate it with observed blockage or alter saved statuses. Shared palette/QSS normalization, native roster/ribbon painters and readiness badges use the same tokens. Role identity colors, supplied stone/icon artwork, scoped Raid Plan button geometry and existing status symbols remain. The button preview stays Raid-Plan-only; only its selected derivative tint changes from purple to neutral grey. No theme selector, new state owner, migration or data interpretation is introduced.

The sidebar hamburger now uses the supplied three-bar gold artwork, with the surrounding presentation glow/background removed. Existing 32px display, accessibility labels, hover expansion and collapse behavior remain unchanged.

The boss ribbon retains its full-width back panel and now uses the same panel_bg stone artwork and 36% obsidian tint as the main columns, with its compact 8px rounded bevel. This replaces the previous smoother blue-tinted ribbon material.

The new snowy Wyrdworks arena is the default planning map in Raid Plan and Map Workshop when no saved/selected map is available. Saved maps retain priority, and fallback art is not marked reviewed encounter evidence. The original 1254x1254 PNG is preserved; runtime uses a pixel-identical lossless WebP.

Grouped buttons and tabs now share the app-wide stone palette: charcoal normal faces, lighter grey hover, slate selected faces and silver selection edges. Includes Builds stage/inspector tabs and Raid Plan readiness, roster, phase and map groups; standalone Raid Plan button artwork remains in place.

Boss ribbon cards have individually raised bevels, bounded cast shadows, wider separation and a static champagne selection halo. The existing full-width obsidian stone backing and canonical stage selection remain; grouped control styling is unchanged.

The boss ribbon scroll viewport and content are transparent, revealing the obsidian stone backing between raised cards rather than a flat grey track.

Map Workshop's **Trial** selector now filters the shared encounter catalog through the existing recognized ESO trial-name registry. Dungeon and arena entries no longer appear in the trial picker; live encounter identities, trial-specific encounter choices, and previously saved map records remain unchanged. A focused regression guard covers this distinction.

Builds page lists, comparison tables, and inspectors now explicitly apply the shared 9px slim scrollbar treatment in both directions; the scoped style avoids changing scrollbars on other pages or altering build data.

External ESO database directory override restored: setting `FOUNDRYDOCK_ESO_DATA_DIR` routes the central ESO database resolver to `<directory>/eso.db` while keeping JSON/resources under `data/`. Explicitly configured missing ESO databases fail without seed replacement. Shared user database/migration selectors recognize the external ESO path. This is a partial recovery: remaining direct database references, persistent launch configuration, Git untracking, and real-device validation are outstanding.

External database routing follow-up: Gear Field Guide, Collectibles Hub, Raid Map workspace and Settings database-path display now use the canonical ESO database resolver. Existing resource directories and user database paths are preserved. Source-level regression guard added; full routing audit, Windows runtime validation and Git database untracking remain outstanding.

External database routing now covers Achievements, achievement import, the shared achievement workspace, collectible ownership/catalog identity, Build enchant choices, and reference-page assembly. Default ESO paths honor `FOUNDRYDOCK_ESO_DATA_DIR` while explicit research directory overrides remain intact. Regression guards added; this does not mean all legacy tools are routed or Windows startup/data migration has been validated.

External ESO database routing extended to the reference data model, reference catalogs and provider relationships, roster gear-alias importing, skill-choice defaults and rotation runtime character context. JSON-resource directories remain separate from the configurable ESO database. Routing contract tests expanded; Windows runtime verification and Git database untracking remain pending.

Granite Collectibles category cards now prefer the bundled 24-category museum exhibit artwork via its existing manifest, falling back to the old atlas only when an exhibit cannot be loaded. No collectible IDs, counts, progress, or data persistence rules change.

Collectibles artwork preference corrected: the Granite cabinet now loads the locally supplied Wyrdworks champagne 2048×1024 badge atlas from `assets/themes/wyrdworks/collectibles_champagne.png` with `wyrdworks_collectibles_atlas.json`, then falls back to the prior Granite atlas if the new pack is absent or invalid. The illustrated museum exhibits are no longer the primary badges. No category progress or databases are changed.

Achievements page integration from `codex/achievements-header-criteria`: consolidated header controls in the Raid Plan shell, refreshed Collections/Achievements browsing, search/sort selection retention, recorded criteria and optional stable-ID artwork lookups. Achievement data and saved progress are not rewritten. The branch's focused UI regression tests and artwork documentation accompany the change; Windows runtime validation remains required.

## 2026-10-19 — Raid Plan endgame defaults

Raid Plan's **Assume Max Passives, CP & Gold Gear** action opens a standard
warning with **Cancel** as the default. **Apply to All Players** changes only the
assigned seats in the current draft; Save persists the plan through its existing
repository and readback. It assumes maximum applicable passives, maximum
non-slottable CP, and CP160 Gold items and selected glyphs. Gear identities,
skills, slottable CP and empty equipment slots stay intact.

**Use CP160 Gold Gear & Glyphs** inherits the global Hardmode default when no
plan override exists; an explicit saved True or False takes precedence without
changing Settings. Each player button opens compact plan-only progression and
equipment exceptions. Those choices survive Save/reopen and apply after sparse
encounter inheritance in offensive and Health calculations. Clear Assumptions
disables the bulk defaults while retaining individually entered equipment
exceptions. Reapplying the confirmed bulk action replaces equipment exceptions.

Original character progression, Saved Builds and builds.json are unchanged.
Roster assignment is sufficient human readiness; historical Human Ready records
and their optional controls remain available. Coverage, missing build evidence,
assignments, conditional effects and observed execution remain separate checks.
Unsupported mechanics remain unresolved; assumed equipment is never verified gear.

## 2026-10-19 — Compact mechanics and shared scrollbars

Raid Plan mechanic cards show the name and wrapped description. Recorded health
thresholds stay on Health Timeline, and stage assignments keep their existing
editor and persistence. The selected Fight pane derives its height from Qt's
wrapped content, replacing the 330px nested scroll viewport and stale card
minimums. Long stages grow through the primary page scroll; short stages shrink.
Hidden panes no longer reserve space. The square map and recovered Coverage,
Build workshop and Stage assignments workflows remain intact.

The shared Granite theme owns 9px graphite scrollbars with rounded handles,
champagne hover and no arrow buttons. Legacy page-local scrollbar rules defer
to this owner while unrelated selectors keep their styling.

Validation uses real offscreen Qt widgets with temporary user repositories and
an isolated reference database. Resize/sidebar/stage, wrapped text, outer wheel,
timeline and assignment preservation, and scrollbar metric checks cover this
change. The rendered short-stage screen was visually inspected. This does not
certify installed-app behavior with the user's live plans or databases.

Closeout evidence: the combined endgame/workspace run passed 55 tests; its two
failures were resolved by matching the recovered assignment empty-state wording
and allowing the existing 40ms adaptive-layout timer to settle. Final affected
checks passed 10/10 plus 1/1. One pre-existing source-backed route test remains
excluded because the isolated reference corpus lacks its three phase records.
Dependency audit (`--check`), architecture audit (`--strict`), Python parsing
and staged whitespace checks passed. No user database was used for these tests.
Endgame implementation checkpoint: `14b8d1cd9`. Pre-existing source in the older
worktree is preserved locally on `codex/wip-preserved-granite-20261019` at
`42bbe11ad`; it is unvalidated and is not part of this published feature.


## Crit / Pen source calculators (2026-10-20)

Raid Plan's Crit / Pen review and the Builds Crit / Pen button now open the same
Coverage-styled module. The Overview includes every raid seat (tanks, healers and
DDs), keeping missing values explicit. Player selection follows across Penetration,
Crit Damage and Crit Chance. Each calculator exposes searchable source options,
pre-checks the canonical saved-build/stage contributions, labels their provenance,
and supports included-only filtering and per-player temporary scenario drafts.
Physical and spell penetration stay separate. Reset restores the loaded scenario;
no calculator control saves a build or assignment. Full evidence notes are collapsed.

Totals begin with the canonical stage result, then apply explicit additive scenario
differences. Crit chance traces use the higher weapon/spell channel, matching the
existing total. Fixed available buffs reuse canonical constants. Variable or
unresolved discovery options require a manual contribution rather than importing
values from another site's screenshot; non-additive traces remain read-only.
The option list includes the requested source families plus every relevant nonzero
trace returned by Wyrdworks, but does not certify exhaustive current-patch mechanics,
conditional eligibility, delivery or uptime. Calculations load on a background task;
failed loads leave the calculators disabled and show the error.

- **Raid Plan stage-scoped Kill & Pull Order editor (2026-10-20, initial implementation)** — Strategy & Mechanics displays authored enemy priorities for the selected stage and an Edit Order action. A manual editor saves ordered enemy rows (pull label, enemy, response, assigned seat and notes) through the existing strict Phase15AssignmentState per-plan/per-context persistence, retaining mechanic assignments and checking stale snapshots. The status stays Unknown until instructions are authored; this is not encounter-verified intelligence. Live Raid handoff and dedicated pull IDs/drag-reordering are not yet implemented. Runtime/UI validation still pending.

Crit / Pen evidence notes open in a separate, bounded read-only viewer with a scrollbar, Close notes button and Escape support. Opening even very long notes leaves the calculator window at its existing size.

- **Kill & Pull Order first-row and narrow-panel follow-up (2026-10-20)** — The empty kill-order modal now starts with an editable target row rather than a blank expanse; Strategy & Mechanics readiness cards use width-forgiving Qt size policies to let text wrap in narrow layouts. Encounter enemies are **not** yet automatically populated from mechanics; the present stage editor is manual-first. Pending runtime geometry and UI testing.

- **Kill & Pull evidence candidates and responsive layout correction (2026-10-20)** — Stage editor now shows selectable enemy candidates from explicit encounter add-group evidence plus the named Nahviintaas Eternal Servant record; candidates require raid-lead action before becoming saved instructions, and ability/phase names are not automatically treated as enemies. The Raid Plan switches from three columns to a two-column layout sooner (display width below 2200) to avoid squeezing/clipping Strategy & Mechanics. Source-backed projection has an isolated regression test. Pending local Qt geometry and full integration validation.

### Raid Plan Publishing foundation (in development)
- Added a read-only, strict-Pydantic publishing snapshot for saved Raid Plan roster references, explicit plan coverage assertions and saved stage assignment/kill-pull/Raid Lead notes.
- Added a bounded Discord briefing generator that labels authored encounter priorities and coverage as planned, not verified.
- Full saved builds, maps, crit/pen, PDF/DOCX/XLSX adapters and Export Center UI remain pending. See `docs/RAID_PLAN_PUBLISHING.md`.

- Granite Field Guide PDF renderer added with dark granite and light print editions, cover, roster, authored stage strategy, kill/pull order, planned coverage, and honest completeness flags. Renderer tests added; UI integration and real-build validation pending.

- Added a read-only per-stage build selection diff projection using canonical Raid Plan context overrides; distinguishes saved build references and planned gear/skills from unresolved full saved-build contents.

- Raid Plan Publishing now reads baseline Raid Plans and stage context overrides through validated, read-only decoders, adds saved stage build selection differences to the shared snapshot, and renders them in the Granite Field Guide PDF. Full saved gear resolution remains pending.

- Added exact saved PlayerBuild export projection (equipment, traits, enchantments, front/back bars, CP, scribing, food and potion), with unresolved identity warnings; Granite PDF renders provided snapshots. Canonical build catalog loading is not yet wired into snapshot creation.

- Raid Plan Publishing now loads the existing canonical saved-build catalog through its read-only loader, resolves selected build identities, and populates full saved-build details for the Granite PDF. Missing/ambiguous builds remain explicitly unresolved; validation tests added (not executed).

- Raid Plan Publishing now projects full stage-specific saved-build loadouts by combining plan context overrides with exact saved-build identities and saved boss-context variants. Granite PDF includes effective stage gear, skill bars, CP and Mundus with explicit unresolved states; full Windows validation remains outstanding.

- Raid Plan Publishing has a typed canonical Crit/Pen report adapter and Granite PDF table preserving calculator outputs, unresolved fields and assumptions. Automatic invocation of the calculator remains pending.

- Added typed Coverage source-inventory projection for Raid Plan Publishing, preserving saved-build versus planned gear/skills, provider assignments, and unresolved evidence in the Granite PDF. This is not a verified buff-uptime calculation; automatic Coverage service invocation remains pending.

- Raid Plan Publishing now automatically includes authored-label Coverage source inventories for General and saved stage overrides using the canonical scope service; results retain planned vs saved provenance and unresolved diagnostics. This is not the full 74-effect verified Coverage audit. Integration test added, execution pending.

- Raid Plan Share / Export header now offers Granite PDF, Light Print PDF or the existing JSON backup; PDFs consume the read-only saved snapshot with export-completeness warnings. UI integration needs Windows smoke testing before merge.

- Granite PDF visual refinement pass: larger table text, page breaks between saved character loadouts, hide unassigned template jobs, summarize coverage set evidence instead of reprinting every skill, and dedicate a page to export completeness. PDF review/test rerun pending.

- Field Guide PDF cover now supports per-export editable team name (default saved plan team) and optional raid date, without modifying saved plan data. Default illustrations and saved map integration remain pending.

- Raid Plan Publishing PDF now embeds existing player-labelled raster snapshots only when explicitly linked to that plan and encounter. Map source lookup never migrates or writes files; editable layout JSON is not rendered yet. Focused test added, Windows visual validation pending.

- Hide plan ID and publication timestamp from Field Guide cover; alert user when saved-map images cannot be found in the current user-data location instead of silently generating a mapless PDF.

- Added read-only saved-map export diagnostics and `python -m tools.inspect_raid_plan_publish_maps PLAN_ID`. Missing linked images now report no map, editable-layout-only, broken link, absent image file or ready; no data migration and no unapproved fallback images.

- Field Guide PDF export now offers an export-only per-boss image picker with previews for existing Sunspire arena maps in external user data and bundled trial assets. Explicit selections appear on matching stage strategy pages; files and persistent map links remain unchanged. Tests written, Windows run pending.

- Field Guide visual pass: reusable, code-drawn compass/field-note cover for Granite and Light Print PDF, dynamic team/date retained; saved-build sections now use character identity headers and six-slot front/back skill grids. Class emblems, avatars, actual skill-icon assets and illustrated graphic covers remain separate future enhancements. Regression tests authored; Windows visual validation pending.

- Field Guide pagination refinement: PDF now keeps front and back saved-build skill bars with their heading as one unit instead of splitting rows across pages; Windows validation and fresh visual inspection pending.

- Raid Plan Field Guide: tighter PDF body/table typography and reduced cell padding; each saved player build now includes a Boss Variants comparison for explicitly authored stage overrides, with planned gear/skill/Mundus changes and resolved effective bar/equipment differences where available. No invented variants. Windows validation and visual review pending.

- Boss variant publishing now also projects saved PlayerBuild ContextVariants and legacy BossLoadouts for existing assignment stage keys even without a Raid Plan member override; per-player dossier prints only actual resolved changes. Added legacy loadout resolution test. Windows validation and real HOUAD PDF review pending.


### Raid Plan Publishing adapters and saved variants (2026-10-20)
- Team Build Plan now starts on its own PDF page after Build Summary. Publishing applies the canonical auto-endgame equipment projection after boss inheritance: populated gear becomes CP160 Gold, existing glyphs become Gold Truly Superb, explicit plan-off and individual equipment exceptions remain authoritative. PDF rows show item level, gear quality and glyph quality; Excel preserves the same values and assumption labels. Reusable builds and databases remain unchanged.
- Illustrated Field Guides now use reusable Sunspire dragon-and-ruins Dark/Light cover plates with native editable publication text, fine gold page borders, serif headings, automatic page-numbered contents, a two-column roster and grouped build summary. Selected maps open landscape three-column strategy spreads with full authored records continued in portrait. Equipment rows are compact; identical Coverage inventories are shown once with every applicable stage named. Artwork is decorative and does not supply mechanics, player positions, numeric reports or missing skill icons.
- Field Guides flow stages without maps together instead of reserving an almost-empty page per stage; mapped stages retain dedicated openings and headings stay with following content. Verified on the uploaded HOUAD plan.
- Share / Export now groups Dark PDF, Light Print PDF, Excel, Discord text/preview and the existing JSON backup in one settings dialog. Team/date overrides affect only the export; preparation/rendering run off the UI thread.
- Publishing reads plan, catalog, overrides and current stage order in one read-only transaction. Saved Build Editor ContextVariants/legacy BossLoadouts resolve through the shared resolver, including reviewed boss aliases, team precedence, named Trash and other-trial exact encounter names. Removed stages do not reappear from stale assignments.
- Dossiers include exact slot/property, skill-slot, ultimate, CP, Mundus, consumable, poison, scribing and note differences. Unknown identities are reported; known unrelated-trial variants are excluded.
- Both Field Guides use reusable lantern/compass covers with Wyrdworks name artwork, full dynamic text, compact illustrated skill cards, actual class emblems and saved-player avatar support. Exact skill-art identity is connected to the existing reference data and local optional packs; no pack is bundled or downloaded automatically. Missing art remains a neutral placeholder.
- Excel exports Overview, Roster, Boss Loadouts, Assignments, Coverage, Crit & Pen, Build Details and Strategy Notes with filters, frozen headers, wrapped text and literal user-authored strings. Discord provides bounded ordered messages, per-message Copy and .txt output. Neither writes back or posts messages.
- PDF/XLSX/TXT writes are atomic: failed exports preserve the previous file. Export Completeness separates saved data, partial inventories, unresolved artwork and unimplemented annotated-layout rendering. See docs/RAID_PLAN_PUBLISHING.md for executed checks and remaining real-data/artwork gates.
- Raid Plan workspace footer reads the most recent successful plan save timestamp from the canonical Raid Plan SQLite record, presents it in local time, and marks outstanding unsaved edits without manufacturing a save time. Legacy JSON plans explicitly show unavailable save time.

- Crit/Pen's stage-scoped calculator now offers a real Save decision to Raid Plan action. It records the selected seat, metric, channel, calculated scenario snapshot, manually adjusted contributions, and Raid Lead explanation in a bounded plan-owned note, with canonical repository save/read-back verification. It does not silently change active builds or claim simulated uptime.

- Crit/Pen Raid Lead decisions now reload into the editor for their exact stage, seat and metric. Closing the dialog refreshes the owning Raid Plan snapshot to prevent a later stale save from overwriting its note, and refreshes the persisted last-saved footer.




- PDF: player dossiers now prioritize a compact baseline-versus-saved-stage equipment comparison with skill bars and changed ability/CP/Mundus notes on the same bounded reference page; full trait, enchant, glyph, quality and level detail retained in a separate appendix. Added rendered PDF regression fixture; Windows validation and real-plan visual review pending.

### 2026-10-21 — Selected Build stays below the roster
Raid Plan now reserves the selected build card's full wrapped content height before sizing the Team column, including frame insets and warning controls. Long build names wrap within the column. The summary remains below every visible player when changing role filters, selection or window width; the primary page scroll carries the expanded content. No player, build, plan or database records change.

Validation: reproduced overlap with native Segoe UI/Georgia metrics, long build text and warning controls; the regression passes after the fix. Six focused Qt layout tests passed, covering all 12 players, DD/tank filters, multiple window sizes, wrapped mechanics and primary scrolling. The corrected rendered screen was visually inspected. Dependency and strict architecture audits passed. Tests used temporary user state and an isolated reference database; this is source/runtime validation, not an installed-app deployment.


## 2026-10-23 — Stage-aware Kill & Pull Order (issue #10)

The existing Raid Plan checklist editor now saves independent pulls with stable IDs, separately movable pull sequence and enemy focus order, optional enemy key, reason, response, seat, map marker reference and notes. Same-name pulls remain independent. The selected stage card previews three saved targets and says Planned only for saved raid-lead instructions; absent instructions stay Unknown. Boss-health phases are never converted into pull names.

The canonical Phase15AssignmentStateService owns strict payload validation, expected-snapshot saves and verified readback; no new database/table/schema migration is introduced. Legacy flat priorities receive deterministic pull identities on read. Cancel, conflicts and save/readback failures retain editor input. Shared Trash jobs may inherit, but authored pull instructions stay exact-stage; inherited assignment snapshots are also guarded against stale saves. Other plan and assignment saves retain priorities.

Reference enemy lookup is explicit and separate from authored rows. The existing enemy-candidate projection reconciles guide facts and excludes conflicting references and observed logs. Adding a reference creates an editable draft with its source retained; only Save makes it an instruction. Live Raid Now projects the saved order, seats and marker references from the canonical stage state and clears it when scope changes. Marker references are readable opaque IDs, not validated map links or map highlighting.

Windows Python/Qt offscreen tests cover Boss, Predot, entrance Trash and after-boss Trash, save/reopen, independent reorder, stale conflicts, cancellation, failure preservation and actual checklist/summary/consumer behavior. Editor geometry is checked at 780×560 and 640×480; Raid Plan at 1540×1000, 1390×900 and 1024×768. See docs/validation/issue10_kill_pull_order.md for exact results and the existing corpus-dependent UI failure. No interactive desktop, EXE build or installed acceptance is claimed.
## 2026-10-23 — Local ESO Logs movement evidence for Map Workshop

- The local Engine Lab extracts timestamped player XY observations from raw ESO Logs event exports into the existing validated replay-bundle format. It preserves fight/kill status and role, omits names and report codes, and keeps coordinates in unscaled log space.
- Map Workshop can open these bundles in a read-only movement viewer; this does not alter saved maps, author paths, align arena art, or turn observations into reviewed strategy. This creates a reusable foundation for later reviewed path comparisons and heat maps.
- Validation: focused local-engine, movement-contract, Map Workshop and viewer checks passed (40 tests). Reef Guardian fight 32 generated 12 role-labelled tracks / 12,743 observed XY samples and retained its wipe status. This validates extraction and display only, not arena alignment, reviewed tactics, heat-map conclusions or engine learning.

### Phase role teaching paths (2026-10-26)

Map Workshop can add a simplified DD, tank or healer teaching path from a chosen actor and exact time window on a loaded calibrated map. Phase selection keeps ground and boss-flight duties separate without rewriting replay data. One chosen DD can represent the shared stack only after review; split duties remain separate. Routes retain source fingerprint/actor/time and are editable through existing annotation handles.

Lokkestiiz duty slots 1a/1b, 2a/2b and 3a/3b have independent team-seat associations. Re-authoring a phase/slot replaces that duty only; saving, reopening, duplication and portable packages preserve the assignment. These are reusable seat associations, not automatic assignment to a person or proof of freeze immunity. Historical guide timing is advisory; live cage detection, cooldown eligibility and a complete teaching animation remain future work.

### Fresh-checkout local validation fix — 2026-10-26

Engine-growth cases with a custom output directory now create the existing shallow validation scratch folder before running a selected suite. A fresh checkout no longer requires an earlier validation run to create that folder. Case identity, privacy, evidence rules and the existing runner remain unchanged.

## 2026-10-26 — Current-development Track A/B/C validation

The existing A/B/C jobs can validate current `wyrdworks-dev` with separate intelligence, UI and integration suites, while preserving historical track reports. Summaries identify the tested source branch and suite. Each local track isolates user state and scratch; scheduled archive evidence retains revision provenance without claiming a clean Git receipt. Raid Plan remains the sole active raid-planning UI. See `docs/validation/track_abc_repair_20261026.md` for scope and execution evidence.

### Sunspire dragon guide additions — 2026-10-26

The existing encounter-reference projection now includes the raid lead supplied code65536 guide for Lokkestiiz, Yolnahkriin and Nahviintaas. Source lineage and per-dragon identity remain attached. Existing source disagreements are retained; the guide is not excluded based on its publication date. These records supply reference explanations, not automatic combat-event detection.

### Simple fight-flow waypoints and path contrast

Workshop paths now have a white/dark contrast outline and saved ink choices for light maps, dark maps, red, blue and gold. The control colors selected paths or all paths when none is selected, and survives save/reopen and portable export.

The Lokkestiiz SIMPLE fight-flow guide follows the raid lead's authored sequence rather than raw trajectory traces: ground damage with two temporary cage branches; flights 1/3 sweep atronachs from one end to the other, stack middle, then house stacks; flight 2 goes directly middle/Barrier to house stacks. House stacks show two four-DD squares in front of two left-side healers facing Lokke on the right. Each house position and cage rotation slot is separately assignable; duplicate simultaneous house seats are rejected. Cage A is nearest the bottom entrance, Cage B farther away. Positions are editable schematic instructions, not surveyed coordinates. Original replay/maps remain available.


### Built-in boss map packages — initial manifest (2026-10-27, WIP)

A versioned Lokkestiiz package manifest now lives at `assets/raid_maps/sunspire/lokkestiiz_package.json` on the isolated development branch. It declares an Empty arena view, Simple Routes strategy view, Movement replay view, main-arena perspective, seven independently named Workshop phases, and six ice cage slots eligible for **tank, healer or DD**. An off-tank is often an appropriate cage volunteer; role eligibility remains unrestricted. The manifest explicitly marks strategy/replay as **not installed** until the saved Workshop assets are bundled and validated. This is an internal integration foundation, **not yet a working Raid Plan map picker, overlay renderer, or installed package**. Raid Plan-specific player assignments must remain outside built-in resources. No user database or Workshop save is migrated or replaced.

## 2026-10-27 — Reusable boss map packages

Raid Plan selects a registered built-in boss package when no plan map exists. Lokkestiiz ships with an editable teaching view and blank arena; Add map offers package views, manual tactical phase/view links, unrestricted roster duty bindings, and a blank Workshop handoff. Workshop’s Attach to Raid Plan copies a saved custom map to the selected plan/boss and verifies the existing plan-map save. Plan drafts and saved maps retain precedence; packages contain no roster identities. Layer choices and phase links travel with editable layouts. Other bosses can register manifests in assets/raid_maps/boss_packages.json; Yolnahkriin and Nahviintaas packages are not yet authored.

Teaching routes are generalized strategy, not fixed cage/atronach spawns or observed intent. Flights 1/2/3 have different raid-lead sequences; replay alignment remains provisional.

## 2026-10-27 — Automatic map phases and five layer controls

Raid Plan’s Map panel selects package tactical phases through a compact encounter-phase selector and the source-backed timeline. Lokkestiiz 80/50/20 flights map internally to Flights 1/2/3; Ground 4 is separate. The normal map toolbar is replaced by Arena, View, Tactics, Guidance and Duties controls. Manual phase linking is absent from normal navigation. Package presentation is read-only; phase/layer changes do not construct EncounterBoard or save drafts. Blank editing remains in Workshop, and successful custom-map attachment returns to the read-only map.

## 2026-10-27 — Integrated boss package playback and Workshop recovery

Raid Plan restores the 80/50/20 percent headings and combines Arena, Strategy, Play/Pause, Names and Edit below the map. A shared cursor synchronizes the selected reference pull, observed timeline events, teaching focus, named phase routes and phase assignment context. Lokkestiiz supplies seven grouped strategy routes (four ground, three flight), rather than per-player Movement path entries. Playback animates recorded actors from three bundled reference pulls, supports seek/restart/speed and next phase/event, and reuses retained graphics. Reference actors never silently become current roster members; planned house names reuse canonical roster house assignments. Calibration remains provisional.

Normal phase/route/layer navigation remains read-only and cannot construct the hidden editor. Edit opens the selected map/phase in Workshop after a dismissible screen-change warning and saves a verified recovery draft. Workshop uses isolated session files, strict recovery validation, content-addressed history and stale-write checks. Autosave recovers drafts; Save to Map Library explicitly publishes them. Databases and existing user maps are not replaced.

Routine development pushes now run focused directly related tests in disposable user data. Broad quality and engine checks remain explicitly available with FOUNDRYDOCK_PUSH_CHECKS=full for integration/release work. Focused push success is not a full quality receipt.

Raid Plan Health Timeline restores its banded health rail and reviewed phase/mechanic/attack cards for built-in packages. Health runs from 100% at left to 0% at right. Percentage cards and rail thresholds seek the matching authored package phase and reference replay section; untimed attacks retain mechanic/assignment details without inventing timestamps. Recorded replay events remain available through playback controls rather than replacing the mechanic cards.
## 2026-10-27 — Dreadsail Reef ribbon artwork framing

The Raid Plan ribbon retains its original 65% image coverage and cover-style scaling for Dreadsail Reef stage artwork, using face-focused vertical crop positions for Trash, Lylanar & Turlassil, Reef Guardian and Tideborn Taleria. Unlike the earlier contain-fit attempt, portraits do not shrink within the image slot. Other trials retain their established crop behavior. Native Windows visual verification remains outstanding.

Timeline restoration also avoids rebuilding unchanged house-name markers during flight phase switches. A focused widget regression preserves marker identity and measured 200 phase switches in 0.916 seconds on this checkout; live app performance still requires retesting.

## 2026-10-27 — Nahviintaas first playable reference package

Nahviintaas now has an automatic built-in schematic package with Play/Pause/seek, Arena, Strategy, Names and Workshop Edit. Successful observed fight 44 supplies 12-player playback and nine named health-band routes. Top headings are the 80/60/40% add flights; 100/90/70/50/33/31% phase bindings support the corresponding opening, portal and late-fight views. Three portal duties start unassigned. The static route is a simplified median of fresh DD observations; individual actors remain intact in playback. Missing samples/large jumps split paths. No portal identity, lower-floor geometry, player intent, or arena artwork alignment is inferred.

This first version uses a labeled coordinate schematic, not illustrated arena artwork. Phase boundaries are observed boss HP samples and do not detect exact takeoff, landing, or portal completion. Historical 33% meteor-onset and 31% execute records remain distinct. Failed attempts 30/62 informed comparison notes but are not offered as complete phase timelines. No upstairs Eternal Servant kill duty is created; the raid lead identifies his upstairs appearance as portal failure. See docs/validation/NAHVI_PACKAGE_20261027.md.

Nahvi package revision: existing Sky Island arena artwork is reused unchanged with boss-at-top projection, matching the raid lead's selected strategy orientation. Main-group routes exclude confirmed reference portal DDs 154/156/8, while all actor samples remain in playback and plan duties stay unassigned. Three observed add-cycle blasts have advance statue-cover callouts; the grounded body guide represents approximate visual size, not collision or safe-space geometry. Reference group identities are report/fight scoped and strictly validated against the replay. This supersedes the first version's schematic presentation.

Nahvi label contrast: phase notes, grounded-body labels, portal duty labels and statue-cover reminders use larger bold text on opaque dark plaques. Replay actor labels use matching dark backings with white lettering and move inward at the right edge. Cue reminders render above moving actor labels. The north-facing arena asset has its own filename; the previous schematic background remains available for saved layouts that reference it.

## 2026-10-27 — Raid Plan premium styling experiment (isolated branch)

On `codex/raid-plan-premium-mockup-20261027`, Raid Plan has an initial scoped charcoal/graphite and champagne-gold styling pass in the shared page-style owner, plus quieter actual roster card painting in the existing delegate. This changes headings, panel materials, buttons, field borders, tables and thin vertical scrollbars without changing page layout, mechanics, persistence or database records. It is the first visual pass, **not yet a faithful reproduction of the complete mockup**. The reference image's extra timers, resource cards, and redesigned lower dashboard layout have not been implemented; no hardcoded example combat data was introduced. Native Windows screenshot and focused test validation remain outstanding.

## 2026-10-27 — Raid Plan premium panel rendering experiment

The existing `ForgedPanel` now renders flat graphite panels with a quiet border and a faint champagne top accent when it is beneath `raidPlanWorkspace`. This replaces the inherited ornate panel paint on the actual Team/Fight/Readiness surfaces and map shell without touching their layout or backing data. Outside Raid Plan, it defers to ordinary Qt rendering. This is a visual increment toward the reference mockup, not full layout parity; native Qt screenshot comparison and tests remain outstanding.

The existing boss ribbon now uses a single subtle shadow and selected gold border instead of stacked embossed bevels; image crop, stage identity, and navigation remain unchanged.

## 2026-10-27 — Global premium graphite theme experiment

On the isolated premium mockup branch, the canonical StonePalette and Granite global stylesheet now apply the graphite / charcoal / champagne palette to shared panels, form controls, tables, tabs, buttons, progress bars and headings across the application. This replaces older silver/amethyst control styles in globally styled widgets while retaining text/icon statuses, keyboard focus borders and no animated effects. Raid Plan-specific custom painters were refined separately. Custom image-based surfaces and page-specific styles can still override the shared theme, and full mockup layout parity has **not** been achieved. Native Windows screenshot comparison and automated test execution remain pending; this experiment is not approved for merging.

## 2026-10-27 — Granite restoration and independent Obsidian experiment

On the isolated branch, the Granite palette, Granite skin and page stylesheet were restored byte-for-byte from `wyrdworks-dev`. A new `ui/obsidian_theme.py` supplies separate graphite/champagne QSS. Existing `ThemeManager` routes selected `wyrdworks_obsidian` to that skin and preserves Granite as the other choice; accessibility preferences now permit either persisted theme key. The Obsidian application skin intentionally does not append Granite's nine-slice layered-surface stylesheet. Raid Plan panel layout and engine bindings were not changed. **Not yet validated on a native Windows screenshot; custom-drawn frame code and local styles may still produce stone ornamentation.** Theme-choice UI integration and older Granite-only tests need review before acceptance. Do not merge this experimental branch without those gates.

## 2026-10-27 — Theme selector in Settings (experimental)

Settings → Appearance & Accessibility now exposes a Granite/Obsidian combo box instead of a read-only Granite label. Changing the selection persists the existing validated accessibility preference and reapplies the chosen theme to the running Qt application. No raid-plan data migrations or database changes are involved. Native Windows runtime and regression tests remain outstanding; do not merge without verifying switching back to Granite and the saved preference on restart.

## 2026-10-27 — Obsidian Collectibles champagne atlas and neutral surfaces

Obsidian Collectibles now uses the existing Wyrdworks champagne atlas in `assets/themes/wyrdworks/collectibles_champagne.png`, via the established `wyrdworks_collectibles_atlas.json` category frame mapping, with the Granite atlas fallback. It retains the same category identities, badge cropping and counts, while using Obsidian charcoal/graphite paint rather than the legacy BFF teal palette. Scoped Obsidian Roster, Collectibles and Settings surfaces also receive neutral backgrounds and controls; Granite remains unchanged. Native Windows validation and full cross-page visual acceptance are outstanding.

## 2026-10-27 — Obsidian neutral black and grey page styling

Obsidian now converts known legacy blue-green page-style literals to graphite, charcoal, neutral borders, and warm-grey text when Roster, Builds and Settings load in the Obsidian profile. The color translation is isolated in `ui/obsidian_theme.py` and applies only when that theme is active; Granite retains the original page colors. The Wyrdworks champagne collectible badge atlas remains selected. No Raid Plan panels, combat formulas or databases were altered. These page-level changes require reopening affected pages after theme selection; existing custom painters and native Windows visual regression remain unverified.

## 2026-10-27 — Cross-page Obsidian neutral styling continuation

The Obsidian-only historical CSS color translator now correctly matches hex colors (previously a mistakenly double-escaped regex prevented replacement). Neutral-surface translation has been connected to Top Gear, Encounters, Map Workshop and the Collectibles hub, in addition to existing Roster, Builds and Settings coverage. The Wyrdworks champagne collectible badge artwork remains unchanged. Granite retains its original page styles. Added `ui/tests/test_obsidian_page_palette.py` to check known neutral colors, page integration and the translator behavior. **Automated tests and Windows visual verification have not run yet**, and custom painters or inline widget-level styles may still need dedicated visual cleanup.

## 2026-10-27 — Builds-matched Obsidian surface pass

Obsidian now uses the neutral Builds graphite palette on shared stacked/scroll surfaces, raised and readiness panels, and Raid Plan shell panels. Its boss ribbon paints a neutral charcoal base while retaining image coverage and selected-stage behavior. Granite continues to use the existing palette. All panels, layouts, map content and databases remain untouched. Windows visual validation and focused Qt regression tests are not yet complete; compare the full loaded Raid Plan and each page before accepting.

## 2026-10-27 — Obsidian missed style owners

The shared Phase15StageBar now passes its independent teal stage-button stylesheet through the Obsidian color translator; Builds boss tabs retain their size, icons, states and stage controller. Raid Plan's top-level locally applied `RAID_PLAN_WORKSPACE_STYLE` also uses the Obsidian-only translation. Achievements' locally applied stylesheet maps its pale champagne `#D8C39F` to the shared gold `#D4B36A` while Granite preserves its original declarations. These fixes address three previously bypassed CSS owners, not the whole renderer. Test and on-screen Windows acceptance remain outstanding; no panels, saved plans or databases were modified.

## 2026-10-27 — Obsidian Raid Plan visual finish, preserved layout

The experimental Obsidian profile now applies a dedicated final Raid Plan stylesheet after the original page rules. It aims for the approved compact graphite/champagne screenshot: neutral surfaces, subdued borders, gold Forum headings, smaller Montserrat controls, flatter selected filters and phase tabs, matching readiness count cards and seven-pixel scrollbars. All original Team/Fight/Readiness widgets, boss ribbon, map, lower mechanics, notes, and engine integrations remain in place. Granite returns the original page stylesheet and no longer uses the experimental ForgedPanel graphite painter. Added visual-contract regression checks in `ui/tests/test_obsidian_page_palette.py`.

**Status:** committed on the isolated branch, but native Qt image comparison and pytest execution are still outstanding; do not claim pixel parity or merge acceptance. Saved databases are outside this styling change.

## 2026-10-28 — Roster-reference Obsidian finish for Raid Plan and Map Workshop

Obsidian's existing Raid Plan styling and its actual ForgedPanel painter now use deeper Roster-reference charcoal instead of the lighter grey panel treatment. Map Workshop has a separate Obsidian-only finishing stylesheet for its existing tool buttons, tabs, input fields, headings and panels. Original geometry, map canvas, interaction wiring, lower Raid Plan panels and saved data are unchanged. Granite is not restyled. Visual acceptance and native Qt test execution still require Windows review; these commits are not a verified screenshot match.

## 2026-10-28 — Obsidian page heading and Raid Plan picker star

Added a centralized Obsidian page heading visual contract modeled on Collectibles' CABINET OF CURIOSITIES: uppercase, bold champagne-gold Montserrat with consistent tracking. Existing FoundryHeader-based pages now use it without a leading page icon; Roster, Builds, Top Gear, Encounters and Map Workshop have explicit adoption. The small upper-right Raid Plan picker control now uses a gold star glyph instead of the overflow/menu icon, with its original toggle and accessible name retained. These changes are scoped to Obsidian for headings, while the picker glyph is shared. No layouts, engines, plan records or external databases were changed. Native Windows visual regression and tests remain pending. Some page-specific heading implementations may still require migration.

## 2026-10-28 — Header consolidation (partial, experimental)

Obsidian Raid Plan now parks the legacy header Plan Details, Duplicate, Share/Export and FD.my buttons and hides the old Raid Planning title/subtitle. The existing gold-star plan loader remains wired; the existing New Plan action reveals the original Plan Name/Team fields and trial picker. These are incremental steps toward the requested shared slim header, **not** the finished shared schedule/team dropdown, settings cog or team-filtered Roster navigation. Existing plans and databases are not modified by these presentation changes. Native Windows and pytest validation outstanding; do not merge this incomplete iteration.

## 2026-10-28 — Compact Obsidian header navigation (experimental)

The persistent Raid Plan header (shown throughout the existing multi-page shell) now places the existing wired team-schedule calendar and schedule label in the right-side strip, followed by a group shortcut, saved-plan/team selector, and Settings cog. The older Raid Planning title/subtitle and duplicate/export/FD.my/Plan Details actions remain parked in Obsidian. The selector lists existing saved plans by team or plan name and ends with **New Plan**, which invokes the canonical New Plan flow and reveals the existing Plan Name/Team Name and trial controls. Selecting a saved plan reuses the existing loader and stops when the current plan has unsaved changes. The group icon navigates to the existing Roster and selects its team filter; when a matching active Raid Plan exists, it additionally filters to its assigned seat identities instead of all team members. Ordinary Roster navigation clears this temporary filter. The cog routes to the existing Settings page. Granite styles, saved data and plan/map geometry remain unchanged. Added wiring-contract tests.

**Validation pending:** Native Windows Qt execution, tests and full header visual acceptance have not been run. The Roster seat filter relies on matching saved roster names to plan gamertags/character names; identities that differ may not appear and require reconciliation. Do not merge until checked.

## 2026-10-28 — Shared Obsidian header cleanup

The persistent Raid Plan-owned shell header now enforces the Obsidian presentation on summary refresh, including when another page shares the shell: the vertical divider after the Wyrdworks logo and the legacy Plan Details, Duplicate, Share/Export and FD.my actions are hidden, along with the retired Raid Planning title/subtitle. The existing calendar button is kept visible immediately before the group button even without a saved team schedule; the schedule label appears between calendar and group only when a real team schedule is available. Existing team selector, Roster shortcut and Settings cog remain. The independent Achievements header is not changed. Granite retains its original header appearance. Added source-contract tests; native Qt visual tests still need to be run.

## 2026-10-28 — Header layout and action visibility correction

The Obsidian shell now anchors the brand to its natural width and pushes the calendar, optional schedule text, group icon, team picker, and settings cog together to the right. It reasserts the active theme's header visibility on Qt show and every page navigation, with a persisted theme fallback to avoid accidentally exposing parked Plan Details/Duplicate/Share/FD.my actions. Achievements retains its independent header. The original calendar and navigation callbacks are unchanged. Windows visual verification and pytest execution remain pending.

## 2026-10-28 — Header logo and map containment regression fix

The Obsidian header logo now receives a fixed 320px width rather than an ignored width hint that let Qt's right-aligned action group collapse it. The Raid Plan map preview now uses `KeepAspectRatio` instead of `KeepAspectRatioByExpanding` to prevent its artwork being cropped when sidebar width changes. No arena coordinates or map source images were altered. This improves image containment but does **not yet prove** the whole map and playback controls fit simultaneously in a single viewport; native Windows layout validation is still required. No database changes.

## 2026-10-28 — Viewport-budgeted Raid Plan map experiment

The map now budgets its square canvas and all visible playback/layer controls against the scroll viewport height. Collapsing the navigation rail no longer grows the map past its controls; responsive mode and the width ceiling use the expanded rail as a stable baseline. Actual Team/Fight/Readiness widths still use the available viewport, with consistent 42/58 allocation in two-column mode. Stacked layouts retain a usable map when scrolled to Fight. Scrolling itself does not resize the map. All lower mechanics, timeline, assignments, route notes, readiness and plan data remain mounted through their existing owners and one outer scroll.

The inline map's height-for-width now includes the controls below its canvas rather than reporting only its first row. Native testing also exposed stale positional header-layout lookups; the shell now uses the existing title and actions by named references, keeping the logo and theme visibility rules intact. No theme assets, map coordinates, protected databases or persistence owners changed.

Validation: native Windows Qt screenshots with actual Lokke package artwork/playback, a disposable empty-roster plan and eight synthetic short/long mechanic descriptions; repeated sidebar toggles, whole-map/control bounds, scroll stability, bounded wrapped cards and window-height reduction pass for both Obsidian and Granite. Initial generic-editor and boss-package edit/Workshop failures also reproduced with original fe11ac1b4 modules, but passed when rerun with a short disposable Windows scratch path; deep generated paths exceeded Windows path limits. During integration, the stale Map Workshop source contract was corrected to recognize its specialized wrapper; a runtime check verifies that wrapper applies the shared Obsidian palette and returns Granite styling unchanged. This experiment is not integration/release approval.
