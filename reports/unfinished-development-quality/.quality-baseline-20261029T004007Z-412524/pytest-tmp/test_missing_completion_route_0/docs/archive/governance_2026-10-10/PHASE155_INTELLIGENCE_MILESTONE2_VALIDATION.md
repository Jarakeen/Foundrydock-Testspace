# Phase 15.5 Intelligence Milestone 2 validation

2026-10-09. Integrated against `c6b5d32c2bcede475356cf2e8a90749c3ebddaf9`, preserving newer Field Guide and Strategy/Raid Map work. The earlier transient checkout and uncommitted draft were unavailable; implementation and tests were rebuilt against fresh GitHub source.

## Implemented boundary

`RaidReadinessEvidenceService.evaluate_encounter` consumes the authoritative effective stage, exact selected Saved Builds and existing Assignments snapshots. It delegates mechanical capability, encounter requirements, difficulty-aware handling and explicit provider conflicts to canonical services. Passive strict contracts keep assignment, applicable build support, source-backed handling, scoped execution observations, group/window availability and identified risks separate. An empty corpus or known handling method cannot produce encounter-ready status.

The existing Readiness page exposes **Check Boss Mechanics** through a background worker. Navigation does not trigger this deeper evaluation. Results are rejected after build, assignment or selected-stage changes; refresh invalidates them. Findings and evidence/actions appear in the existing player checklist, with full detail in tooltips. The outer geometry, three large engine buttons and Field Guide remain intact. Strategy/Raid Map authoring and manual readiness never prove execution.

No Comp Engine, Optimization or database schema changes. Assignments gained a read-only snapshot reader that never bootstraps a database or schema. Analysis uses existing build services and does not create another optimizer.

## Actual results

- Focused encounter/Readiness/UI checks: **43 passed in 1.18s**.
- Final isolated integration checkpoint including selected-stage/build resolution, Assignments and service registry regressions: **203 passed in 2.85s**.
- Wider encounter/Readiness regression attempt: **457 passed, 34 failed, 1 collection error**. Real-corpus tests cannot use the checked-in database because `encounter_canonical_fact` is absent. The remaining three Readiness redesign failures are obsolete source assertions; the unchanged branch head also gives **3 failed, 2 passed** for that file. The collection error imports retired `ui.encounter_identity_correction_support`.
- Separate unrelated learning-panel test cannot collect: it imports retired `ui.comp_builder_phase14_shell_support`. Its Phase 14-specific expectations are obsolete; disclosure/plain-text safety could be tested on a current consumer. No retired module was restored.
- Dependency audit: **703 reachable modules; zero scan issues, dynamic import sites or retired shell paths**. `git diff --check` passed.
- Database-dependent regressions ran in a separate source/reference database copy with isolated user state. The checked-in ESO database remains SHA-256 `1d8fc9b0e4cb51ca1be5e214727e10612b51fd10c1cd80e2111824d8e4c82ce7`. Analysis on the isolated reference database also preserved its hash. No production/user database was modified.

Commands: `python -m pytest -q` over the new encounter integration/projection tests, Readiness evidence/coverage tests, effective-context and selected-build tests, Assignments tests, service catalog/integrity tests, and Readiness effective-context/worker tests; `python tools/audit_phase155_dependencies.py --check`. The wider run selected `services/tests/test_encounter*.py` and used `--continue-on-collection-errors` to expose independent failures.

## Evidence and performance limits

- Reviewed planning identity resolves Twins to both Lylanar and Turlassil and keeps trial identity scoped to Dreadsail Reef. Raw Reef Guardian records contain overland provenance; no trial health/damage thresholds were inferred from them.
- The current checked-in reference database cannot supply canonical encounter facts. The app explicitly reports that gap. The earlier attached richer ESO snapshot is no longer present in this runtime, so no current real-corpus readiness claim is made.
- Existing Assignments data does not provide typed Reef initial/return/solo continuation or Taleria bridge/window strategy bindings, nor reviewed observed execution. The UI reports them as missing; it does not reconstruct them from notes or generic portal chair lists. Strict supplemental contracts allow those evidence-producing canonical consumers to supply scoped facts later without assigning readiness now. No observation import/editor or new storage authority was added.
- Synthetic twelve-seat witnesses verify pair-entry evidence cannot establish second-Heart solo execution, the three-player Reef alternative needs three participants, Taleria one-person bridges are excluded by raid-lead policy, and two-/three-person bridge teams remain unverified until evidence exists. These are contract tests, not measured player damage or survival.
- Group availability never follows from roster/build presence or assumed proximity. Backup capability/availability/execution remains explicit. Source-backed conflict evidence is required to declare double-duty conflict.
- Final synthetic twelve-seat review (30 iterations, stub capability audits): **5.17 ms median, 13.15 ms maximum**. Reference-corpus failure-closed review: **25.1 ms**, also with stub capability audits. These measurements do not bound real Saved Build audit latency. Actual evaluation is off the UI thread; existing routine Readiness calculations were not redesigned or benchmarked.
- UI checks ran offscreen, including background completion, stale rejection, navigation invalidation, 1200×800 size preservation, retained bottom buttons and Field Guide. No Windows native screenshot validation was performed.
- The concurrently added `INTELLIGENCE_INTEGRATION.md` references an inventory JSON and regeneration tool absent from this GitHub source. That document was preserved; no second inventory authority was created.
