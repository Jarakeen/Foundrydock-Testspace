# Wyrdworks — Intelligence integration inventory

## 2026-10-25 — Map-bound replay and empirical scale review

| Finding | Source / scope | Canonical owner and consumer | Status | Limits |
| --- | --- | --- | --- | --- |
| Original movement can be projected onto a particular map without rewriting samples. | Exact strict replay-content fingerprint, adjacent image SHA-256 and decoded dimensions, explicit projection | `services/encounter_replay_bundle.py` and existing `encounter_movement_route_preview._project` → `EncounterReferenceReplay` → Map Workshop | Implemented; focused service/UI/storage/package checks and real-file calibration receipt recorded locally | Profile evidence remains `provisional_fit`; image registration, physical scale confidence and actual delivery are separate questions. |
| Calibration companions need to survive map copies and sharing. | Validated replay + calibration + identical background bytes | `EncounterRaidMapStore`, `WorkshopMapPackageService` (v2 for calibrated packages; v1 retained) | Save/reload, duplicate, package/import and active Workshop consumer covered | Stale or mismatched profiles must fail closed; raw-coordinate review remains available. |
| Banner Bearer provides a user-identified 8 m actor-centred reference. | Local ability 217699 radius 800 raw units; user-confirmed visible ring. Stable buff-state fits against recent player resource coordinates, per API map ID | Local calibration evidence → provisional map profiles, not canonical Combat/Encounter formula changes | Empirical working scale; pull-held-out mean buff-state agreement roughly 93–97% on the four main map groups | Buff-state agreement is not physical error accuracy. Provider switching, update lag, missing snapshots and elevation remain confounders. Side bosses have one pull only. |
| Nahvi appears off-platform during Lokke. | User's explicit observation; NPC tracks retained separately | Lokke ground-reference artifact and map-marker review | Off-platform Nahvi and known flight intervals excluded from Lokke ground marker fitting | Do not erase distant actors from raw evidence or treat NPC XY alone as ground contact. |


## 2026-10-25 — Three-report movement and support evidence increment

| Finding | Source / confidence | Canonical destination / consumer | Status / evidence | Limits / next action |
| --- | --- | --- | --- | --- |
| Complete paginated reports need a bounded-memory adapter to reach existing log consumers. | Three user-authorized report exports, 127 fights, 4,544,701 events; receipt/page hashes kept outside Git | `services/esologs_raw_importer.py:iter_paginated_report` → existing Local Engine Lab → Map Workshop observed movement viewer | Integrated; focused intake/extractor/importer/growth-case/viewer/Map Workshop checks: 43 passed. Real-data intake processed 127 fights and emitted 43 movement bundles, 617,916 samples. | Observations do not validate Combat/Encounter model predictions or change reviewed mechanics. Full-suite certification is not claimed. |
| Extreme observed XY can make the full-fit replay unreadable. | Direct observed samples in Cloudrest, Reef and Lokke exports; outlying coordinates remain unclassified | Existing `ObservedMovementCanvas` | Operational bounded UI: explicit reversible central-position fit; source-preservation test | A cropped viewport is not collision geometry, a portal classifier or outlier deletion. |
| Budding Seeds has an 8 m effect radius and 28 m cast range; cast position does not establish ground-effect centre. | User confirmation; local ability records 85840/93805/93806; 821 candidate casts in three reports | Ground-effect calibration review, existing stage/map calibration owners | Documented; candidate cast receipts retained locally | Visible boundary, exact log/video time alignment and ground-plane perspective are still required before metric calibration. No radius is inferred from provider-recipient separation. |


This is the existing human-readable integration inventory, not another mechanics engine. Status definitions and evidence requirements live in [DEVELOPMENT_STANDARD.md](DEVELOPMENT_STANDARD.md). The tables below retain reported snapshot evidence; dates, test scope and limits matter. They do not certify the present branch, Windows install or a different reference database.

## Current scope note (2026-10-15)

Wyrdworks is the product name; FoundryDock remains the repository and technical identifier. Active workflow pages are Raid Plan, Roster, Assignments, Builds, Strategy / Raid Map, Live Raid, and Finch / Collaboration where applicable. Lantern, Comp Brainstorm, Coverage, Rotations, Readiness, Health, Comp Engine, Optimization, and Extreme Build interfaces are parked. Existing inventory rows that name parked pages record historical/retained consumers and evidence; they do not reopen page development. Continue maintaining canonical intelligence and shared services where needed by active workflows. Do not promote any row beyond its stated provenance, scope, test, or checkpoint limits.

## 2026-10-23 — Local ESO Logs observed movement intake

| Finding | Source / confidence | Existing implementation | Destination | Status | Test evidence | Limits / next action |
| --- | --- | --- | --- | --- | --- | --- |
| A user-provided Reef Guardian wipe contains player XY coordinates in combat event resource payloads. | Local raw export SHA-256 `d976da48c38c8f6a3775dc5877572762019aa5aa6a3f59459c011e09289fd793`; direct observed coordinates; no route interpretation | `services/esologs_reference_movement.py` extracts timestamped player tracks; `tools/local_engine_lab.py` emits a strict replay bundle; Map Workshop opens it in the read-only movement canvas | Map Workshop observed movement review; future map alignment and heat-map research | Locally integrated and source-tested; commit/push pending | Local Engine Lab, movement contracts, Map Workshop and viewer tests: 40 passed. Local Reef fight 32 produced a separate wipe-labelled movement bundle and concise observation report: 12 tracks, 12,743 XY samples. | Coordinates remain unscaled and unaligned; names and ESO Logs report code are omitted. Wipes are usable as observations, not successful reference routes. Do not convert these tracks to authored paths or strategy without reviewed arena alignment and interpretation. |

## 2026-10-23 — BTVTools benchmark intake for growth cases

| Finding | Source / confidence | Existing implementation | Destination | Status | Test evidence | Limits / next action |
| --- | --- | --- | --- | --- | --- | --- |
| Screenshot-derived BTV uptime benchmarks can be attached to a matching local ESO Logs growth case. | Structured BTV benchmark JSON hash; values retain their provided encounter/effect/page/role scope and downtime denominator; no OCR or identity mapping | `BTVBenchmarkEvidenceService` validates the existing benchmark contract; `tools/engine_growth_case.py` stores strict ratio fields and provenance hash while omitting free-text notes; Engine Lab offers a file picker | Local growth case library | Local evidence intake integrated; no engine decision or mechanics changed | Focused growth-case, Engine Lab, and BTV benchmark tests: 34 passed; final BTV attachment guard tests: 3 passed. | Current contract covers effect uptime ratios, not every BTV panel metric. Screenshot OCR/import, exact log-to-BTV player mapping, and modeled-versus-observed comparisons remain unimplemented. Next acceptance: structured entry for non-uptime group metrics, then a reviewed same-fight comparison consumer. |

## 2026-10-11 — Yolna Nightblade recording evidence intake

| Finding | Source / confidence | Existing implementation | Destination | Status | Test evidence | Limits / next action |
| --- | --- | --- | --- | --- | --- | --- |
| User-provided Nightblade setup and dummy-combat video labeled Yolna, source key `USER_VIDEO_YOLNA_BLADE_20261011` | MP4, SHA-256 `c60916ae02caf1e56eeec4872e550949f73816f0d3f71909be012f77f74a4a58`; direct clip identification high; mechanic inference low | Video source and metadata registered in `useful_resources.md`; no executable mechanic added | Existing Combat/Rotation evidence review, then canonical `services/foundry_intelligence_service.py` only for individually corroborated claims | **Captured / not promoted** | File existence and duration/hash checked at intake; no combat consumer tests or detailed event annotation | Preserve the original recording outside Git; transcribe visible setup and timestamped actions, identify game patch and dummy, compare to ESO Logs; do not infer Yolnahkriin boss performance or formula constants from dummy footage |

## 2026-10-12 — Fail-closed combat intelligence dependency declarations

| Finding | Source / confidence | Existing implementation | Destination | Status | Test evidence | Limits / next action |
| --- | --- | --- | --- | --- | --- | --- |
| An empty declared mechanics dependency was silently filtered by the shared intelligence snapshot, potentially hiding a missing requirement from Comp/Optimization/Rotation decision checks. | Current `FoundryIntelligenceService.snapshot` compared with canonical `CanonicalMechanicsCoverageReport.dependency_gaps_for`; high confidence from source inspection | `services/canonical_mechanics_coverage_audit.py` already rejects blank declared keys | `services/foundry_intelligence_service.py` now rejects blank/non-string declarations and preserves valid deduplication | Source and regression tests committed; **execution pending** | `services/tests/test_foundry_intelligence_service.py` includes malformed and duplicate-key regression cases; not run in this chat | This is a fail-closed decision-boundary fix, not a new ESO combat formula. Run focused tests and UI/intelligence/integration tracks in local checkout before marking operational. |

## Maintenance contract

One finding should identify source/update/confidence, canonical owner, intended consumer, the changed decision, status, test witness, limits and next action. Update the same finding as evidence advances instead of appending a succession of “test added / CI pending” narratives. Keep historical validation reports linked, not copied. Do not upgrade a status merely because a test file exists.

The uploaded snapshot refers to an inventory JSON/regeneration tool that is absent in this checkout. Those references are historical dependencies, not working instructions. Do not invent a generator or create a competing inventory. If the designated environment actually supplies one, confirm its ownership before using it.

## Current reconciliation notes

- Coverage's new native interaction consumer is committed locally with 230 targeted UI/service checks passing and dependency audit passing. It is bounded synthetic/offscreen evidence; group geometry, actual execution, broad ingredient discovery and Windows appearance remain open.
- The uploaded encounter Readiness report has mixed wider results and missing corpus/strategy evidence. Keep those gaps visible; see [Milestone 2 report](PHASE155_INTELLIGENCE_MILESTONE2_VALIDATION.md).
- Cached Coverage-to-Comp and scoped support-set reviews in the uploaded inventory have CI-pending and synthetic-only witnesses. Reconcile their current implementation before promotion. They do not establish equipped thresholds or delivery.

## Integration inventory

| Finding | Source / confidence | Existing implementation | Destination | Status | Test evidence | Limits / next action |
| --- | --- | --- | --- | --- | --- | --- |
| U51 Sorcerer Exploitation contributes a unique 2,974 Offensive Penetration to the group; planned maximum passive assumptions are not observed delivery. | Official U51 notes and current calculator cross-check; high confidence for the U51 value/scope, no combat uptime evidence. | `RaidPlanOffensiveStatsService` adds one plan-inferred group penetration contribution only for a Sorcerer seat with `endgame_ready_assumed`; Raid Health and Readiness preserve the distinction between effective and support-ceiling totals. | Raid Plan offensive stats → Health and Readiness player decisions | Operational (synthetic plan scope) | Four affected test modules: 48 passed in 9.60s on local working tree based at `74b0141a94974a4238b76e440af3df3feeef3e4c`; includes the group-source, Health review and Readiness decision regressions. | Does not infer Force of Nature stacks or prove live application/uptime. Run packaged Windows acceptance; retain explicit patch/source version in future patch-intake work. |
| Raid Plan DD checks must keep personal Savagery separate from group buffs, while composing critical chance with exact build stats and saved group penetration/debuff evidence. | `NamedBuffResolutionService` / canonical effect targets and `GearStatInputResolver`; high confidence for the typed U51 effect scope, saved-plan evidence only. | `RaidPlanOffensiveStatsService` keeps Major/Minor Savagery by seat, shares Major Force/Brittle/Breach and penetration inputs, and emits per-DD provenance/unresolved evidence; Readiness opens the actual all-DD review. | Raid Plan Readiness → DD penetration and critical review | Operational (saved-plan projection) | `services/tests/test_raid_plan_offensive_stats_service.py`, `services/tests/test_raid_plan_context_offensive_stats_service.py`, `ui/tests/test_phase155_raid_plan_workspace.py`; 48 related tests passed on 2026-10-14. | Does not infer live buff delivery, uptime, or combat logs. Savagery on one support seat cannot raise every DD's result. Windows/package appearance remains unchecked. |
| Shared team interaction evidence must distinguish mechanical compatibility, routine planning, recipients and execution. Status consequences require a source/damage-type opportunity bound to the selected Build and stage; free-text conditions cannot establish a proc. | Existing named-effect owner, capability audits, reviewed support references, Orb registry and canonical status opportunity/consequence owners; bounded canonical-snapshot confidence, not fresh patch revalidation | NamedBuffResolutionService.reviewed_pair_can_coexist; strict InteractionAuditBinding/TeamInteractionEvidence/TeamInteractionReview | FoundryIntelligenceService.team_interactions; reusable by Coverage, Comp Engine, Optimization, Readiness and Rotations | Integrated | services/tests/test_team_interaction_evidence.py; validation checkpoint in docs/phase155_team_cross_reactivity_m1_validation.md | Native positive-interaction presentation is Milestone 2 and remains pending. No group access, numeric team gain or observed execution inferred; conditional status prerequisites and broad ingredient coverage remain unresolved. |
| Ordinary support-set triggers should count as planning support without masquerading as measured uptime. Explicit manual Coverage choices must not become generic conditional Optimization findings. Ozezan's Plating names an effect from Ozezan the Inferno. | Existing canonical equipment counts / support references; current ESO-Hub tooltips; high for trigger relationship, declared planning policy for routine use | RaidUniqueSupportSetCapabilityService; RaidPlanCoverageAssignmentService | shared RoutineSupportProcPlan; Coverage automatic/detail presentation; Optimization adviser | Operational | services/tests/test_routine_support_proc_planning.py plus existing assignment, support-set, adviser and Coverage checks: 46 passed in 4.41s | Four reviewed set families only; roles and qualifying-bar Ultimate slots must be recorded. Conditional mechanical evidence stays unchanged. No group availability, universal uptime or execution inference. |
| U45 converted nine Green stars to passives; old name lists and mixed discipline ID/index coordinates cannot determine current bar eligibility. | Official U45 v10.3.5 notes / Bethesda support; high confidence for the nine conversions. Local reference metadata provides exact numeric slottable types and discipline IDs. | minmax.champion_point_static_repository constants; ReferenceDataService reference rows | ReferenceDataService.list_slottable_champion_points; Builds baseline and stage _CPDialog | Operational | services/tests/test_reference_data_champion_point_choices.py; ui/tests/test_phase155_builds_champion_point_dialog.py; isolated actual-reference witness: 35 Blue / 28 Red / 10 Green choices, correct healer grouping, unchanged reference hash | Scope is current Builds slot selection, not purchased progression or a rewrite of every engine's historical CP semantics. Unknown saved choices need explicit review; no assumed points or game-math magnitudes. |
| Existing canonical Comp candidate benefits, sacrificed source effects, conditions and provenance now reach the native Comp Engine build browser. A bounded source-diverse pool keeps alternative source families discoverable without treating popularity as performance. | services/comp_candidate_adviser_service.py, comp.candidate.learning_explanation; high confidence for the typed presentation contract, no combat gains established. | explain_comp_candidate / CompCandidateLearningSummary | services/phase15_comp_engine_service.py; ui/phase15_comp_engine_page.py | Operational | services/tests/test_comp_candidate_learning_summary.py; services/tests/test_phase15_workbench_discovery.py; ui/tests/test_phase15_raid_lead_workbench.py; included in 351 passing related tests on 2026-10-09 | Existing Saved Build/reference/log candidates only. Review lenses do not compute a new objective. Independent-duty execution, numeric damage and uptime remain unproven. Optimization review prompts are generic questions, not a new encounter engine. This manual consumer audit supplements the existing document; its referenced inventory JSON/regenerator are absent in this checkout. |
| A saved support assignment is planning intent; Readiness must retain unsupported or duplicate provider warnings. Unresolved build placeholders remain gaps and never enter capability math. | services/raid_plan_coverage_assignment_service.py; services/tests/test_raid_plan_coverage_assignment_service.py; High for the planning/evidence contract; no new numeric ESO rule. | services/raid_plan_coverage_assignment_service.py; services/raid_readiness_evidence_service.py; ui/phase15_readiness_page.py | services/raid_readiness_evidence_service.py | Operational | services/tests/test_readiness_assignment_intelligence_integration.py; services/tests/test_raid_plan_coverage_assignment_service.py; services/tests/test_raid_readiness_evidence_service.py; services/tests/test_raid_plan_coverage_scope_service.py; pytest exit 0: ........................                                                 [100%] / 24 passed in 1.10s | Static/planned source evidence is not observed uptime. Conditional supported coverage still requires runtime validation. |
| Extreme runtime buffs and exact Rotation potion actions enter one ordered combat-state projection. | services/rotation_plan_runtime_combat_state_service.py; services/canonical_mechanics_coverage_inventory.py; High for shared orchestration; potion numbers retain canonical source/update restrictions. | services/rotation_plan_runtime_combat_state_service.py; services/rotation_plan_potion_combat_state_service.py | services/rotation_plan_runtime_combat_state_service.py | Operational | services/tests/test_rotation_plan_runtime_potion_bridge.py; services/tests/test_rotation_plan_potion_combat_state_service.py; pytest exit 0: .............                                                            [100%] / 13 passed in 0.61s | Focused synthetic boundary tests, not a live-player DPS witness. Unresolved scheduled state fails closed. |
| Rotations consume canonical progression and per-bar build contexts rather than private armor/passive formulas. | services/rotation_static_build_context_service.py; services/canonical_mechanics_coverage_inventory.py; High for context reuse; incomplete passive/runtime catalogs remain explicit. | services/rotation_static_build_context_service.py | services/rotation_static_build_context_service.py | Operational | services/tests/test_rotation_static_build_context_service.py; pytest exit 0: .........                                                                [100%] / 9 passed in 0.36s | Per-bar resource ceilings can differ; a single common ceiling is only returned when evidence permits it. |
| Canonical encounter roster/execution evaluators exist but this uploaded Readiness service evaluates only builds and named support coverage. | services/encounter_roster_evaluation.py; services/encounter_execution_evaluation.py; services/raid_readiness_evidence_service.py; High for inspected integration gap in uploaded snapshot; newer work from another chat is not present here. | services/encounter_roster_evaluation.py; services/encounter_execution_evaluation.py | services/raid_readiness_evidence_service.py | Validated | services/tests/test_encounter_roster_evaluation.py; services/tests/test_encounter_execution_evaluation.py; pytest exit 0: .........                                                                [100%] / 9 passed in 0.65s | Next roadmap integration: stage-effective builds, difficulty, assignments, actionable requirement evidence. Do not duplicate Milestone 2 work if a newer sandbox already connects these. All nine mapped encounter tests pass with the supplied eso.zip reference database; fallback corpus disagreements and empty-database errors were environment issues, not grounds to rewrite mechanics. |
| User reports Enlivening Overflow and Hope Infusion should not be assigned redundantly to both healers. | User report, 2026-10-08; source verification pending.; Unverified current-update mechanics; retain as a research question. | None | services/raid_plan_coverage_assignment_service.py | Documented | No test evidence yet; not run by this audit | Verify exact effect stacking, conditions and update before adding assignment constraints; not hardcoded. |
| Conditional healer candidates consume canonical runtime condition windows, including exact expiration, instead of standing bonuses. | services/extreme_runtime_snapshot_conditional_actual_heal_optimization_service.py; services/tests/test_extreme_runtime_snapshot_conditional_actual_heal_bridge.py; High for the bounded synthetic runtime contract; not proof of exhaustive actual-heal optimization. | services/extreme_runtime_snapshot_conditional_actual_heal_optimization_service.py | services/extreme_runtime_snapshot_conditional_actual_heal_optimization_service.py | Operational | services/tests/test_extreme_runtime_snapshot_conditional_actual_heal_bridge.py; pytest exit 0: .....                                                                    [100%] / 5 passed in 0.51s | Verified in the originating Extreme consumer; a shared downstream cross-engine witness remains to be mapped. |
| Damage components receive their own damage-category modifiers; unresolved or mismatched classification remains explicit. | minmax/skill_combat_damage.py; minmax/tests/test_classified_skill_combat_damage.py; High for executable classified-component math under fixture assumptions; coefficients need independent canonical data. | minmax/skill_combat_damage.py | minmax/skill_combat_damage.py | Validated | minmax/tests/test_classified_skill_combat_damage.py; pytest exit 0: ....                                                                     [100%] / 4 passed in 0.10s | This tests the canonical combat function. Map a current UI/rotation consumer witness before promoting this audit entry to Integrated or Operational. |

## Shared mechanics backlog

Imported directly from the existing canonical mechanics inventory. Coverage classifications describe bounded mechanical support, not end-to-end integration proof. These rows remain Documented in this audit until a consumer/test mapping is added above.

| Key | Known support | Source | Consumers | Missing evidence | Integration status |
| --- | --- | --- | --- | --- | --- |
| saved_build:canonical_structure | calculation_ready: Saved build class/role/race, exact six-slot bars, skill eligibility, weapon type, set identity, mythic identity, weapon enchantment identity, and Champion Point allocations can be adapted into CharacterBuild with unresolved identities failing closed. | minmax/character_build/saved_build_adapter.py | comp_maker, rotation_maker, optimizer | Consumer verification mapping needed | Documented |
| effect_duration:build_modifiers | partial: Build-effective duration resolution exists and currently supports the verified status_effect_duration_increase semantic used by Serpent's Disdain. | minmax/character_build/effect_duration_resolver.py | comp_maker, rotation_maker, optimizer | Catalog and verify every other class passive, armor/set, mythic, Champion Point, potion, or other mechanic that changes effect duration, including applicability, additive/multiplicative behavior, stacking order, caps, bar/slot requirements, and refresh interaction. | Documented |
| heavy_attack:restoration | partial: Scheduled heavy attacks can be mapped to active weapon/bar and converted to restoration events when completion, fully-charged state, successful-hit state, verified base restore, and modifiers are explicitly supplied. ESO Logs damage observations can promote reviewed completions to landed evidence one-to-one. | services/rotation_heavy_attack_restoration_evidence_service.py | rotation_maker, optimizer | Update 35 now supplies authoritative base restoration for standard weapon families. Complete the exact passive/set/CP/modifier catalog that alters heavy restore, including current ownership/values for historical Tenacity, Ulfnor's Favor, Off Balance, Rampaging Slash, Arch-Mage, and block-reduction axes; verify Werewolf separately, complete blocked/dodged/missed outcome semantics beyond the current positive landed observation, and preserve channel/completion timing evidence rather than inferring it. | Documented |
| assignment:rotation_fulfillment_catalog | partial: Provider ownership can be translated into exact runtime effect obligations, discrete taunt applications, continuous/symbolic taunt maintenance, or explicit non-effect dispositions. Reviewed policy is persisted in one strict, versioned production registry keyed by exact encounter + requirement identity; missing assignment semantics remain shared knowledge gaps rather than inferred strategy. | data/rotation_assignment_policy/reviewed.json; services/rotation_assignment_policy_registry_service.py; services/rotation_assignment_policy_resolver.py; services/rotation_assignment_canonical_evidence_service.py | comp_maker, rotation_maker, optimizer | Expand reviewed production rows beyond the currently sparse encounter coverage. For each real assigned requirement, retain provenance-backed exact effect/source/bar/uptime semantics when effect-based, explicit taunt/maintenance windows when target ownership is required, or the exact non-effect mechanic model responsible. Unreviewed encounter/requirement pairs must remain absent and fail closed. | Documented |
| passives:runtime_semantics | partial: PassiveGrant evidence participates in build effect availability and duration evaluation when supplied explicitly. Rotation static evaluation reuses the rank-aware Phase5BuildCalculationContextFactory, which applies racial passives and reviewed Warden, Dragonknight, Necromancer, Nightblade, Sorcerer, Templar, armor, One Hand and Shield, reviewed weapon standing-passive branches, Undaunted, guild, and Alliance Support passive resolvers. Generated sustained-DPS exact evaluation now preflights that static context and fails closed before simulation when the canonical context retains unresolved mechanics. | minmax/character_build/passive_grant.py; services/rotation_build_effect_duration_service.py; minmax/context_factory.py; minmax/phase5_context_factory.py; services/rotation_static_build_context_service.py; minmax/racial_passive_stat_repository.py; services/extreme_resource_racial_passive_ownership_service.py; services/extreme_passive_projection_service.py; services/extreme_sustained_dps_generated_runtime_evaluation_service.py | comp_maker, rotation_maker, optimizer | Expand the verified rotation-runtime passive catalog beyond the resolver families already owned by the Phase 5 context path. Racial passive ownership/stat parsing now reaches rotation static contexts. Reviewed Dual Wield sword Twin Blade and Blunt, Dual Wield Ambidextrous, Two Handed greatsword Heavy Weapons, and Bow Accuracy standing-sheet branches now flow through Phase 5; unreviewed weapon-subtype branches fail closed. Remaining weapon/world/vampire/werewolf and other passives still require runtime ownership. ExtremePassiveProjectionService now also rejects max-rank passive source disagreements carried by the canonical skill universe, so stale rank text cannot be projected merely because an ability tooltip is parseable. It otherwise classifies simple unconditional passive tooltip contributions and fails conditional/runtime clauses closed; those reviewed projections are not yet a shared rotation runtime source of truth. Remaining work includes rank, slot/bar/equipment prerequisites, trigger conditions, duration/resource/status/target effects, and stacking semantics. | Documented |
| armor:weight_passive_semantics | partial: Verified static armor math distinguishes exact Light/Medium/Heavy piece counts for armor-line effects and distinct equipped armor weights for Undaunted Mettle. Rotation static build evaluation already reuses BuildCalculationContextFactory, so verified armor and Undaunted passive ownership/ranks reach front/back rotation contexts instead of being recomputed by the optimizer. | minmax/armor_passive_input_resolver.py; minmax/undaunted_passive_input_resolver.py; minmax/context_factory.py; services/rotation_static_build_context_service.py | comp_maker, rotation_maker, optimizer | Expand the verified armor-passive catalog beyond the passives already owned by BuildCalculationContextFactory, preserve rank/prerequisite gates, and verify every Light/Medium/Heavy and composition-sensitive passive that can change resource costs/recovery, block behavior, damage/healing, penetration, critical stats, mitigation, movement, or other rotation-relevant state. | Documented |
| gear:conditional_topology | partial: Set and mythic identities are canonicalized and EffectVariant-capable gear effects can participate where verified, but identity alone is not treated as complete runtime proc semantics. | minmax/character_build/saved_build_adapter.py; minmax/character_build/effect_availability.py | comp_maker, rotation_maker, optimizer | For gear sets, arena weapons and mythics, verify trigger, prerequisites, proc chance, internal cooldown/lockout, duration/tick cadence, stacks, refresh rule, range, target cap/selection, bar state, resource thresholds, suppression/prevention and wearer/group/enemy tradeoffs. | Documented |
| skills:runtime_topology | partial: Exact saved abilities, class eligibility, skill bars and verified skill effects can be canonicalized for rotation/build evaluation. | minmax/character_build/saved_build_adapter.py; minmax/skill_effect_repository.py | comp_maker, rotation_maker, optimizer | Verify comprehensive per-skill cost, cast/channel time, GCD occupancy, duration/tick cadence, range, target cap, targeting rule, buff/debuff/status effects, execute scaling, LA/HA interaction, proc conditions, passive slot effects, scribing/subclass dependencies and interrupt/channel behavior. | Documented |
| procs:conditional_topology | partial: Some canonical effect variants and temporal services can model verified effects, durations and cooldown-like constraints, but there is not yet a single exhaustive proc-topology catalog. | minmax/character_build/effect_instance.py; services/rotation_candidate_temporal_effect_service.py | comp_maker, rotation_maker, optimizer | Normalize proc topology across skills/sets/mythics/enchants/CP: cause, prerequisites, deterministic vs stochastic trigger, proc chance, duration, ticks, ICD/target lockout, stacks, refresh, target selection, range, state thresholds, suppression and renewal action. | Documented |
| consumables:runtime_resource_and_buff_policy | partial: Saved builds retain potion identity; scheduled POTION actions are resolved through canonical potion evidence into ordered CombatState buff windows, and Medicinal Use rank extends those source-backed durations through PotionCadence. The same scheduled uses can now project source-backed instant Health/Magicka/Stamina restoration events. Rotation requests also carry potion selection/on-cooldown policy, but this is not yet exhaustive runtime potion/poison mechanics. Front/back poison identity and authoritative 20% / global-10-second trigger cadence are now available to runtime consumers. | minmax/character_build/saved_build_adapter.py; minmax/potion_cadence.py; minmax/potion_use_event.py; services/rotation_plan_potion_combat_state_service.py; services/rotation_candidate_canonical_plan_evidence_service.py; ui/rotation_generation_support.py | comp_maker, rotation_maker, optimizer | Scheduled potion instant-restoration events now feed canonical generated-candidate sustain evaluation, support-cadence sustain, recovery-heavy replay, and saved Extreme resource records through the fail-closed result contract. Complete remaining potion runtime effects beyond scheduled buff windows, plus poison effect magnitude/dilution/application, invisibility/detection/speed/Unstoppable effects, and any poison-specific target/effect stacking rules not yet represented. | Documented |
| consumables:potion_cooldown_effective | partial: Rotation Maker enforces one shared potion-cadence timeline when an effective cooldown is supplied. Saved-build jewelry Potion Speed reductions are resolved with CP160/Truly Superb and Infused provenance, canonical non-item potion_cooldown_reduction EffectVariants can be evaluated conservatively, and a dedicated aggregator emits a final effective cooldown only when the non-item effect inventory is explicitly complete. Objective #32 can now resolve that effective cooldown from each finalized canonical build and fails closed when canonical build adaptation, passive-grant inventory, dynamic cooldown topology, or external scenario inventory is unresolved. | minmax/jewelry_potion_cooldown_repository.py; services/rotation_saved_build_potion_cooldown_item_service.py; services/rotation_potion_cooldown_effect_variant_service.py; services/rotation_effective_potion_cooldown_service.py; services/extreme_sustained_dps_potion_cooldown_resolution_service.py; services/extreme_sustained_dps_potion_cooldown_passive_grant_service.py; services/extreme_sustained_dps_generated_axis_pipeline_service.py; minmax/rotation_potion_cadence.py | rotation_maker, optimizer | Generated progression now has an explicit completeness-bearing canonical PassiveGrant derivation seam for potion-cooldown effects; incomplete or competing passive authorities stop before cooldown math.  Prove the external scenario denominator and promote only reviewed passive cooldown mechanics. Conditional skill/passive/set cooldown modifiers discovered downstream of potion scheduling require a cadence-aware runtime model and must not be flattened into a permanent pre-rotation reduction. | Documented |
| weapon_enchantments:runtime_cadence | missing_critical: Canonical equipped weapon-enchantment sources can now preserve exact bar/slot provenance, classify cadence family from canonical consequences, materialize reviewed activation opportunities, and branch finite source/cooldown histories without guessing. ZOS-authoritative evidence covers landed Light/Heavy/qualifying weapon-ability activation, source-weapon persistence across bar swaps, poison suppression, one-hit exclusivity, and the normal 4-second direct-damage cooldown example. Selected CP160 Legendary Decrease Health procs can now resolve exact target-Max-Health Oblivion damage through the sequential target-Health ledger. Candidate-scoped cadence proof allows a single authoritative direct-damage identity to use its reviewed 4-second cadence without unrelated multi-identity topology; duplicate same-identity sources use the official shared timer. Distinct-identity topology, buff/debuff-family cadence, and ordinary non-Oblivion glyph damage policy remain separately fail-closed. | minmax/weapon_enchantment_repository.py; minmax/weapon_enchantment_effect_service.py; minmax/combat_cooldown_rules.py; minmax/weapon_enchantment_runtime_cadence.py; services/extreme_sustained_dps_weapon_enchantment_runtime_source_service.py; services/extreme_sustained_dps_weapon_enchantment_activation_event_service.py; services/extreme_sustained_dps_weapon_enchantment_sequence_frontier_service.py; services/extreme_sustained_dps_weapon_enchantment_cooldown_policy_resolver.py; services/extreme_sustained_dps_weapon_enchantment_oblivion_damage_service.py | rotation_maker, optimizer | Multi-identity exact cadence still needs an authoritative buff/debuff enchant base cooldown, authoritative proof that distinct enchant identities retain independent cooldowns, and the remaining ordinary elemental/absorb direct-damage consequence rules needed for exact damage application. Official ESO Support now establishes that duplicate enchant identities share one cooldown, so that specific topology field is authoritative. Decrease Health/Oblivion is exact for the reviewed CP160 Legendary path. Distinct-identity independence remains community-supported but provisional and must not be promoted into Objective #32 combat math. | Documented |
| weapons:bash_interrupt_poison_topology | partial: Weapon type, bar ownership, traits, set identity and weapon-enchantment identity are canonicalized from saved builds. Front/back poison ownership is now persisted separately, adapted into canonical Bar state, and suppresses only the enchantments on the poisoned weapon set. ZOS-backed poison cadence evidence now covers 20% proc chance, qualifying damaging Light/Heavy/weapon abilities, one global 10-second poison cooldown, and single-target DoT exclusion. Imported UESP Alchemy Poison tier evidence can also resolve one saved crafted poison item label to a source-backed possibility universe of effect identities while preserving base/triple duration alternatives. Explicit formula and dilution witnesses can separately close the selected effect set and exact duration. Reviewed U50 Breach and Protection target-side consequences then reuse canonical Minor Breach and Minor Vulnerability target combat math. Generated Objective #32 search now enumerates the canonical crafted-poison formula catalog independently on legal front/back bars, then intersects every selected formula trait over imported Poison solvent/level coordinates to search a finite source-backed tier denominator. Poison tiers are now a first-class canonical Objective #32 mutation axis, so theoretical closure cannot treat formula search alone as complete weapon-poison coverage. Front/back tier choices remain independent, are retained on the assembled candidate, and runtime consequence authority selects the tier belonging to the proc source bar. Literal per-trait '(triple)' source annotations are preserved and mixed per-effect dilution witnesses are supported, while unmarked or implicit source cells remain provenance rather than guessed base-duration mechanics. The saved label alone still proves neither formula nor dilution. Imported formula section headings are preserved as audit provenance but are not promoted to dilution authority. | minmax/character_build/saved_build_adapter.py; importers/import_uesp_alchemy_effects_db.py; minmax/alchemy_formula_catalog.py; services/extreme_sustained_dps_weapon_poison_frontier_service.py; services/extreme_sustained_dps_generated_weapon_poison_tier_frontier_service.py; services/extreme_sustained_dps_generated_weapon_poison_tier_loadout_frontier_service.py; services/extreme_sustained_dps_generated_weapon_poison_formula_authority_service.py; services/extreme_sustained_dps_generated_weapon_poison_dilution_authority_service.py; services/extreme_sustained_dps_generated_weapon_poison_consequence_authority_factory_service.py; services/extreme_sustained_dps_generated_late_axis_adapter_service.py; services/extreme_sustained_dps_weapon_poison_identity_service.py; services/extreme_sustained_dps_weapon_poison_formula_selection_service.py; services/extreme_sustained_dps_weapon_poison_dilution_selection_service.py; minmax/alchemy_poison_effect_semantics.py; services/extreme_sustained_dps_weapon_poison_named_effect_consequence_service.py; services/extreme_sustained_dps_weapon_poison_named_effect_authority_service.py; services/extreme_sustained_dps_weapon_poison_activation_event_service.py; services/extreme_sustained_dps_weapon_poison_sequence_frontier_service.py; services/extreme_sustained_dps_weapon_poison_consequence_frontier_service.py | comp_maker, rotation_maker, optimizer | Verify weapon-specific light/heavy timing, bash cost/damage modifiers, interrupt legality/timing, remaining enchant cooldown topology, authoritative per-effect ordinary/triple duration semantics for generated poison formulas when source cells are unmarked or implicit, remaining poison-trait relationships, Ravage Health/resource magnitudes and periodic application, dual-wield/two-hand legacy representation, arena weapon conditional rules and weapon/passive interactions. | Documented |
| encounter:target_range_movement_topology | partial: Reviewed encounter facts can project timed demand windows and rotation services can enforce explicit demand/bar/temporal obligations. | services/encounter_rotation_demand_service.py; services/rotation_plan_temporal_legality_service.py | comp_maker, rotation_maker, optimizer | Expand reviewed encounter evidence for target swaps, immunity/downtime, range/positioning, movement time, add waves, execute/burst windows, target counts/caps, incoming-damage/heal-pressure windows, interrupts, blocking, synergies and phase-specific legal-action constraints. | Documented |
| niche:stealth_thief_bash_objectives | niche: Stealth/thief, unusual movement, bash-focused and other niche mechanics should remain canonical evidence even when ordinary raid objectives assign them zero or negligible relevance. | shared optimization objective policy | comp_maker, rotation_maker, optimizer | Do not discard niche mechanics from canonical data merely because the standard trial candidate generator does not currently prefer them. | Documented |



## Historical audit trail

Full original evidence and wording: [dated source](docs/archive/governance_2026-10-10/INTELLIGENCE_INTEGRATION.md). Historical counts and completion claims apply only to their recorded checkpoint.

## Concurrent branch evidence retained

Newer shared-branch records were preserved during integration: [checkpoint f08ff6f15](docs/archive/governance_2026-10-10/concurrent_f08ff6f15/INTELLIGENCE_INTEGRATION.md). This evidence includes cached Coverage/Comp handoffs and plan/stage invalidation checks; its original confidence and CI status remain scoped to that checkpoint.

## Coverage consumer reconciliation — 2026-10-10 UTC

Preserved newer shared-branch cached Coverage/Comp and support-delivery contracts while integrating the visible native layout. Shared team interaction projection now includes reviewed Pillager equipped-threshold capability with explicit Ultimate/ally-range prerequisites and unknown delivery. The inspector retains all sources and delegates Rotations navigation. An initialized native page with actual temporary plan/build repositories and a real worker verifies review → selected-source/timing display → invalidation. Its capability audit is a declared synthetic fixture, not a real reference-dataset/raid execution witness. See docs/phase155_coverage_connections_validation.md for actual checks.

## Planned map reach foundation (2026-10-10)

- **Decision:** Warn when a planned recipient marker lies outside an assigned support Ultimate's evidence-backed range; do not infer a missed cast.
- **Evidence/confidence:** User-supplied two-point distance and provenance; only explicitly reviewed scale enables meter calculations. Ability range requires separate canonical source evidence.
- **Scope:** Exact Raid Plan and stage context; mismatches are explicit unresolved states.
- **Canonical implementation:** `services/support_event_link_review_service.py` (`calibration_from_reference_points`, `review_planned_map_reach`).
- **Consumers:** Not yet connected to Raid Map editor, persistent layout storage, Readiness, Coverage or Live Raid. The current contract is not an operational UI feature.
- **Tests:** `tests/test_support_map_planned_reach.py` committed for boundaries, missing evidence, cross-stage scope and invalid calibration input. Execution on current branch remains unverified.
- **Remaining limitations:** A drawing may be distorted or nonuniform; reference distance reliability, calibration persistence, stale edit rejection, conflicting range evidence, UI interaction, and observed delivery still require separate validation.

### Calibration persistence update (2026-10-10)

`EncounterRaidMapStore` now owns user-data persistence of `RaidMapReferenceCalibration` at exact plan and stage scope. A versioned strict payload, atomic write, read-back check and optimistic revision check protect saves. Regression coverage committed in `tests/test_raid_map_distance_reference_persistence.py`; tests have not been executed on the current GitHub branch. Editor inputs, scale suitability review, Live Raid/Coverage/Readiness consumption and real-build validation remain open. No protected databases are written by this path.

### Raid Map calibration/layout isolation regression (2026-10-10)

Saved plan layouts are enumerated from JSON files in the exact plan/stage folder. The new `distance_reference.json` calibration record shares that folder, so without filtering it could be returned as a diagram or selected by `latest_plan_layout`. Fixed in `EncounterRaidMapStore.list_plan_layouts` by excluding calibration metadata while continuing to find genuine diagram JSON. Regression added to `tests/test_raid_map_distance_reference_persistence.py`. Execution against the current repository remains unverified. This is a persistence/consumer interaction issue, not a new ESO mechanic.

### Calibration editor integration (2026-10-10)

`ui/phase15_strategy_page.py` now exposes a plan/stage-scoped calibration action in the existing Raid Map inspector using the canonical `EncounterRaidMapStore` and reference-to-scale contract. Source and map uniformity review remain explicit; an unreviewed scale is preserved but not admissible to support-reach verdicts. Current interaction requires manual drawing coordinates. Actual Qt save/reload tests and click-to-pick point workflow remain pending, as do Live Raid, Coverage and Readiness consumers. This is not proof of combat delivery.

### Live Raid map evidence storage alignment (2026-10-10)

Found an integration gap: Strategy/Raid Map saves through the canonical user-owned Raid Map store, whereas Live Raid initialized its reader with the reference data directory. Changed Live Raid to `EncounterRaidMapStore.for_application()` to use the same persistence owner and preserve additive legacy lookup behavior. Added AST wiring regression; running a real saved-map roundtrip and eventual planned-range UI evidence remains outstanding. This is a storage routing defect, not newly established ESO math.

### Live Raid calibrated scale consumption (2026-10-10)

Live Raid's existing support-chair cards now consume the exact-plan/boss saved calibration reference, compute its scale using `calibration_from_reference_points`, and label reviewed vs unreviewed evidence. Contradictory no-scale text was reconciled. The range evidence ladder is still incomplete: recipient positions and derived reach are not connected, and no observed delivery is inferred. Added `tests/test_live_raid_map_calibration_wiring.py` structural regression; current-branch execution remains unverified.

### Live Raid planned seat-distance integration (2026-10-10)

`ui/phase15_live_raid_page.py` now passes exact plan/boss coordinates, a reviewed reference scale, and nonconflicting build-backed radius to canonical `review_planned_map_reach`. Multiple markers for the same seat are deliberately excluded as ambiguous. Resulting labels distinguish within/outside planned radius and explicitly disclaim recipient eligibility and effect delivery. This is an initial consumer, not full effect-target modeling: different Ultimate mechanics can target enemies, allies, or areas; stage-specific eligibility, recipients without markers, and page-wide readiness integration remain unresolved. Structural regression added in `tests/test_live_raid_planned_reach_wiring.py`; execution and actual Qt validation are pending.

### Strict calibration point boundary (2026-10-10)

Hardened `RaidMapReferenceCalibration` so persisted/imported NaN and infinite coordinates and blank identity/evidence strings fail Pydantic validation at the boundary. Added regression cases to `tests/test_support_map_planned_reach.py`. This removes a gap where invalid data was rejected only by downstream computation; execution in current-branch pytest remains unverified. Recipient eligibility and real Qt interaction are still outstanding.

### Stage-match guard for Live Raid planned range (2026-10-10)

Live Raid now requires the selected assignment `context_key` to match the displayed guide's encounter id before obtaining marked seat positions or calibration scale. This closes a cross-stage evidence contamination path discovered during review. `tests/test_live_raid_planned_reach_wiring.py` includes structural checks. Earlier uploaded checkout smoke tests passed 3/3, but that older baseline does not validate the newer GitHub implementation; full current-branch testing remains pending.

### Generic ability range is not verified effect radius (2026-10-10)

`InteractionSource.range_meters` does not encode casting-range versus area-radius geometry or recipient eligibility. Live Raid previously called this numeric fact a `radius`, which overclaimed the evidence. Corrected the display to describe a comparison of planned seat separation against reported ability range, explicitly leaving targeting geometry and delivery unresolved. Exact assignment/guide stage matching now also guards presence-only marker evidence. Committed structural regression updates; execution on the current branch remains pending. Decision gate: do not use this geometric comparison as a support-coverage pass/fail until source-backed targeting semantics are modeled.

### Support range geometry gate (2026-10-10)

InteractionSource now distinguishes unknown, cast distance, and effect radius. Support constraints preserve that distinction. Live Raid withholds seat-radius conclusions unless current evidence explicitly identifies effect-radius geometry. No ability-specific geometry is presumed. Source contract tests committed; current-branch execution and Qt validation remain pending.

### Geometry-versus-recipient evidence wording (2026-10-10)

Live Raid's effect-radius guarded branch previously stated geometry was unverified after requiring explicit `effect_radius` geometry evidence. Corrected its explanation to acknowledge sourced effect-radius geometry while preserving uncertainty about eligible recipients, activation and actual delivery. Updated the existing Live Raid regression assertion. The underlying sources still require independent review and the current-branch tests and Qt flow remain unverified.

### Geometry measurements must accompany geometry classifications (2026-10-10)

Audit found `InteractionSource` allowed a specific `range_geometry` without `range_meters`. Added a Pydantic after-validator so a claimed cast distance or effect radius requires an explicit measured range. Unknown geometry remains backward compatible for absent range. Regression tests cover both rejection and legacy acceptance in `tests/test_support_map_range_geometry.py`. Current branch test execution and actual Live Raid consumer validation remain unverified.

### Active boss context versus encounter ID (2026-10-10)

Live Raid previously compared assignment `context_key` directly to `guide.encounter_id`, although the controller's canonical boss stage key uses `boss:<id>` while the guide holds `<id>`. This could reject valid same-stage map evidence. Replaced the comparison with a shared active-stage and plan identity check in `_support_map_matches_displayed_stage`, used for coordinate markers and scale display. Updated structural regression; running against current-branch pytest and interactive Qt remains outstanding. This is an identity integration correction, not an ESO mechanic discovery.

### Strict assignment persistence must accept JSON-shaped arrays (2026-10-10)

Reproduced a save failure in the uploaded checkout: `Phase15AssignmentState` uses strict tuple collections, while legitimate save payloads supply `jobs` as JSON lists. A `mode=before` validator now accepts only lists/tuples and converts them to tuple values before strict nested validation, preserving rejection of other types. Sandbox tests passed 3/3 in `test_phase15_support_ultimate_assignments.py`, plus manual invalid-input checks; new regression test was committed on phase15.5. The uploaded checkout differs from GitHub, so current-branch CI/Qt validation remains outstanding.

### Stale map layouts invalidate calibration reach (2026-10-10)

Found calibration provenance tied only to plan/stage, not the particular drawing. Replacing a map could silently reuse an obsolete meters-per-unit scale. The reference model now supports an optional saved-layout map ID; the Raid Map editor stamps new references with the current saved layout, and Live Raid refuses reviewed reach evidence from unbound or mismatched layout IDs. Legacy calibration JSON remains readable; it is not trusted for reach until resaved with a matching map. Structural and model regressions added but current-branch pytest and interactive Qt validation remain outstanding.


### Finch integration test reconciliation (2026-10-10)

Focused Finch CI at `76b3af0b` ran 70 tests: 66 passed, four failed. One Coverage sharing test double omitted the canonical `manual_for` method; updated the double to represent empty manual assignments. Three collaboration tests referenced deleted `ui/raid_engine_dashboard_support.py`; replaced their obsolete host assumptions with checks of the current standalone page's read-only and structured-signal contract. **Not proven:** native Phase 15.5 shell registration and successful dispatch of `workspaceRequested(route, context_key)`. This must be tested against an actual active host before the collaboration navigation workflow is marked integrated. Current-head CI results are pending.

### Finch native host handoff connected (2026-10-10)

Closed the previous unregistered-page gap: `Phase15RaidPlanWindow` now owns the existing read-only `FinchCollaborationPage`, exposes a research route, and connects page/workspace requests through native navigation. A shared snapshot context is never treated as a verified local saved plan: navigation changes the page only, retaining the locally selected plan and stage. Unsupported routes report no native workspace. Structural tests cover host registration and context non-adoption. Full Qt and Windows interactions remain to be demonstrated.


### Cross-plan persistence CI execution gate (2026-10-10)

Added `services/tests/test_raid_plan_stage_realistic_workflow.py::test_two_saved_plans_keep_stage_selection_and_coverage_isolated` to the Required Quality Baseline. It uses a disposable SQLite store and verifies independently saved plan/stage selection and stage-scoped Coverage overrides after fresh controller/repository construction. Do not report this test as passed until it actually executes at the current commit.

GitHub workflow run `38083389082` and its one-job retry both failed during runner startup: jobs completed with zero reported execution steps, no pytest output and no useful downloadable logs. The earlier validated commit `35307865` passed Required Quality and Planning Stability but predates this new regression. The uploaded September test ZIP is not a current checkout, and the local sandbox cannot run the Qt-dependent test because PySide6 is unavailable. **State: implemented / in required gate / execution unverified.** Do not weaken or remove the gate to force green. Once Actions is operational, run the current-head baseline and the full native Windows save/reopen acceptance.\n


### 2026-10-15 — Phase 1 read-only Support Windows

`FoundryIntelligenceService.support_windows` is the canonical public consumer of
the strict frozen `models/support_window.py` request/evidence/assessment contracts.
`services/support_window_evidence.py` is its pure interval projection helper, not
a new mechanics authority. Requests bind exact plan, stage, encounter, timeline,
recipient, target, semantic effect and caller-supplied snapshot fingerprint;
provider seat/build identity, owner, source revision and provenance remain attached.
The snapshot fingerprint must include selected builds/revisions, assignments and
relevant source revisions. Callers are responsible for producing it from current
canonical context; Phase 1 does not independently load or certify that context.

Decision: does explicit supplied evidence cover the requested half-open time
interval? Union/clipping reports covered intervals and gaps without summing buffs.
Scope/basis mismatches are excluded with structured reasons. Relevant unknown,
conflict, unsupported or limitation-bearing evidence cannot yield a supported
conclusion. Planned and observed timelines remain distinct. No equipment-based
recipient, range, condition, duration, stacking, magnitude, DPS or uptime inference.
Evidence remains caller-supplied, not independently patch revalidated; even an
observed-basis assessment does not independently certify execution.

Validation at phase15.5 checkpoint `8957a395113d8a9b0f4a216c3f16d46226b1a0b2`
(plus existing dirty work and this local increment): 60 focused support-window,
Foundry intelligence and registry tests passed; 169 adjacent team-interaction,
handoff and catalog tests passed. Synthetic evidence only. The new tests include
strict rejection, immutable snapshots, serialization roundtrip, context/evidence
exclusions, deterministic union, debt preservation and an I/O entry-point guard.
Commands used installed Python with `PYTHONDONTWRITEBYTECODE=1` and pytest
`-p no:cacheprovider`; repository .venv lacked pytest. Scoped `git diff --check`
passed. No protected database, UI or validation-runner change. Persistence/reopen
gates are not applicable to this pure read-only API. No active UI is wired yet;
canonical evidence adapters and UI adoption remain future work. This is bounded
Phase 1 operation, not a full phase closeout or real-build certification.
Local only; not committed, published or installed.

Phase 1 follow-up validation (2026-10-15): result contracts now independently
reject evidence misclassification, fabricated temporal coverage, hidden relevant
conflicts, incorrect exclusion reasons and contradictory assessment statuses.
This closes a reconstruction boundary gap; the evaluator remains the union
producer and no new mechanics or evidence source is introduced. Ten additional
regressions cover malformed assessments and observed-basis serialization without
execution certification. Revalidated on the same phase15.5 HEAD with current
concurrent dirty work: 70 focused tests passed in 7.43 seconds and 169 adjacent
regressions passed in 14.85 seconds, using installed Python, disabled bytecode and
disabled pytest cache as above. Scoped diff checks passed. Only the support-window
model, its tests and this receipt changed in this follow-up. UI, protected
databases, validation runner and unrelated concurrent work remain untouched.

### 2026-10-15 — Mechanic-linked support planning bridge

`FoundryIntelligenceService.support_window_plan` now consumes an explicit strict
`SupportWindowPlanningRequest`, existing `Phase15AssignmentState` event links,
an `EncounterBossGuide` snapshot and a fresh canonical team-interaction projection
over the effective Raid Plan context, selected Saved Builds and bound audits.
The canonical intelligence catalog registers this responsibility on the existing
Foundry owner. `services/support_window_planning.py` is its pure projection helper;
`models/support_window_planning.py` owns immutable planning assumptions/results.

Decision: retain an explicit proposed support interval associated with an assigned
provider, semantic effect, recipient/target and reviewed event identity, while
showing which facts still prevent evidence-supported coverage. The bridge checks
exact plan/stage/encounter/trial scope and the fresh interaction fingerprint.
Its output fingerprint also incorporates assignments, guide contents, difficulty,
timeline and strategy assumptions. Duplicate assumptions are rejected; missing,
unreviewed or duplicate event facts and absent/ambiguous provider effects remain
gaps. Unstructured support assignments are reported as lacking timing assumptions.

Trigger clock, activation offset and effect-specific duration must be explicit
strategy assumptions with provenance. No clock or duration is extracted from
mechanic descriptions, assignment notes, generic source duration or health
thresholds. No hardmode applicability is inferred. Proposed intervals remain
separate from assessed coverage: range/position, recipient eligibility, ultimate
availability, prerequisites and assumed timing/duration remain unresolved, and
the generated Phase 1 evidence remains unknown and planned, never observed.
This does not yet supply reviewed Dreadsail hardmode data or UI adoption.

Validation: at phase15.5 HEAD `8957a395113d8a9b0f4a216c3f16d46226b1a0b2`
plus current dirty work, 272 tests passed in 23.78 seconds across support-window
planning/intelligence, Foundry intelligence, registry integrity, support event-link
review, team interactions/acceptance, named-buff handoff and application/service
catalog suites. Tests include the real public-owner/canonical-team path, synthetic
fixtures, strict input rejection, serialization, stale audits, exact scope,
assumption changes, missing clocks/durations and an I/O entry-point guard.
Installed Python used `PYTHONDONTWRITEBYTECODE=1` and pytest `-p no:cacheprovider`.
Scoped diff checks passed. No protected database, persistence, UI or validation
runner changes; save/reopen gates do not apply to this read-only snapshot API.
Local only, not committed, published or installed; no full regression claim.

### 2026-10-15 — Assignments Support Windows read-only consumer

With explicit user approval to lift the earlier no-UI constraint, the existing
Assignments page now has a read-only Support Windows tab. Its review action
validates the current editor snapshot as `Phase15AssignmentState` and consumes
`FoundryIntelligenceService.support_window_readiness`, which returns strict frozen
`SupportWindowReadinessReview` / row contracts via the existing planning helper.
The projection reuses canonical `review_support_event_links` and never parses
timing notes, performs build audits, or writes/reads storage during review.
It deliberately reports all activation windows unresolved until structured
intervals and the remaining delivery evidence exist. The numeric planning bridge
remains separate; this view does not claim to invoke it or certify coverage.

The decision is whether each current support-chair assignment has an explicit
ultimate and an encounter-event link, and which inputs still prevent a support
window assessment. Cards retain manual call text as intent, distinguish checked
empty event evidence from unavailable evidence, and label draft/snapshot status.
Event evidence is explicitly from the last stage load. Its source lookup now uses
exact encounter ID and trial scope, excluding ambiguous keys and avoiding the
former display-name/catalog fallback. Plan/controller/editor mismatches reject
review. Assignment edits, successful saves and stage changes (including hidden
pages) immediately clear previous cards. Opening/reviewing this tab does not
construct a parked page or add data access to page startup.

Validation at phase15.5 HEAD `8957a395113d8a9b0f4a216c3f16d46226b1a0b2` plus
current dirty work: 336 scoped service/UI regressions passed in 84.39 seconds.
After the final card-height fix, all 9 new Qt UI tests passed again in 5.14 seconds;
the themed isolated preview also passed text-height checks. The checks cover real
review-button dispatch through the canonical owner, no database I/O/save during
review, dirty-draft preservation, exact scope, hidden-stage invalidation, temporary
database save/reload/reopen integrity, and one outer wheel-scroll at 1280×800 and
1000×650 without changing the outer window dimensions. The preview was inspected
under the existing Granite ThemeManager with explicit local font loading because
AppContainer Qt could not enumerate system fonts. No theme implementation changed.
Initial UI collection/setup attempts failed to create temporary directories;
reruns used a unique repository-local `work/` base directory and passed. Two UI
defects found by validation (card cleanup and wrapped-text clipping) were fixed.

Installed Python used `PYTHONDONTWRITEBYTECODE=1`, `QT_QPA_PLATFORM=offscreen`,
pytest `-p no:cacheprovider` and isolated per-run `--basetemp` folders. Protected
working databases and validation runner remain untouched. No live Dreadsail HM
or packaged/full-application certification is claimed. Local only, not committed,
published or installed; ready for the user's checkout-based visual testing.


## 2026-10-19 — Raid Plan endgame-default consumer integration

Raid-lead decision: assume a normal endgame baseline once, then enter exceptions
per assigned chair before saving. Existing owners: RaidPlanRepository and its
strict payload boundary; RaidPlanSavedBuildResolutionService for equipment;
raid_plan_endgame_baseline_service for temporary progression; canonical MinMax
passive/CP resolvers for eligibility and existing math. No new readiness or
mechanics engine was added. UI action is Phase15RaidPlanWorkspace through its
inherited Raid Plan persistence page and the compact individual editor.

Assumptions are plan-scoped policy, not verified ownership or uptime. Original
Saved Build and Character records remain authoritative facts. Plan/seat identity,
explicit gold override and member exceptions survive repository reopen. Sparse
boss choices resolve before final plan equipment projection in offensive/Health
consumers. Their result provenance distinguishes assumptions. The U51 Sorcerer
Exploitation contribution remains conditional, Plan Inferred and provider-scoped;
an individual passive exception disables its assumed contribution. Roster-ready
does not establish Coverage, assignment, build, or encounter evidence. Historical
Human Ready persistence is retained.

Consumer regressions: services/tests/test_raid_plan_endgame_defaults.py and
ui/tests/test_raid_plan_endgame_defaults_workflow.py. They exercise Cancel,
assigned-only draft changes, canonical readback/reopen, stale and failed saves,
global inheritance and explicit False, equipment and empty-slot preservation,
source-build immutability, sparse boss inheritance, progression-to-CP consumer,
Sorcerer conditional provenance and the actual active workspace action/dialog.
No new ESO mechanics or research claims were introduced, so field-note/source
updates are not applicable. Validation and Git closeout are recorded below.


### Endgame-defaults validation receipt (2026-10-19)

Base checkpoint: a305d35caa776d10550bb89e2890f78924dd7d50, requested
granite-fantasy-blend worktree. The feature was staged independently of its
pre-existing shared-database/UI changes. The staged tree
75c444ba724135bd2b244b3bf70e2af0a1a77f20 was archived to a disposable source
directory for validation: **203 passed, 2 explicitly deselected in 85.05s**.
After the final stable-character assignment guard, a further isolated run of
the new workflow/defaults and existing Readiness context/encounter tests passed:
**41 passed in 19.19s**. All changed Python files compiled; staged and working
git diff --check passed. Service-registry integrity was included.

The two deselected tests were first run and also reproduced with the captured
pre-change modules: test_unresolved_stage_snapshot_fails_closed attempts a
dataclasses.replace on the existing Pydantic offensive row, and
test_new_workspace_reads_saved_route_and_switches_shared_stage expects three
phase records absent from the reference corpus copy. They are baseline/test-data
limitations, not a green full-suite claim. An initial combined run also had a
Qt wrapped-card timing failure; it passed in both an isolated rerun and the
203-test staged-source run. Geometry cleanup is a separate subsequent increment.

Fixture scope: temporary SQLite user stores, synthetic plan/build identities,
and a consistent SQLite backup of the worktree reference database opened in
mode=ro. Actual shared WyrdworksData databases were not opened for mutation,
migrated or replaced. No full application startup or install was performed.
No original builds.json or canonical character/build records were written by
the feature. No schema migration was added. Full production/corpus and packaged
visual acceptance remain outside these bounded tests.

Tests in the 203-test staged-source run (pytest -q -p no:cacheprovider with
isolated --basetemp; -k excluded only the two baseline tests named above):
- `services/tests/test_raid_plan_endgame_defaults.py`
- `ui/tests/test_raid_plan_endgame_defaults_workflow.py`
- `services/tests/test_raid_plan_endgame_baseline.py`
- `services/tests/test_raid_plan_saved_build_resolution_service.py`
- `services/tests/test_raid_plan_offensive_stats_service.py`
- `services/tests/test_raid_plan_context_offensive_stats_service.py`
- `services/tests/test_raid_plan_offensive_run_audit_service.py`
- `services/tests/test_raid_plan_coverage_scope_service.py`
- `services/tests/test_raid_plan_repository.py`
- `services/tests/test_raid_plan_repository_revisions.py`
- `services/tests/test_raid_plan_stage_realistic_workflow.py`
- `services/tests/test_raid_plan_context_override.py`
- `services/tests/test_raid_readiness_evidence_service.py`
- `services/tests/test_service_catalog_registry_integrity.py`
- `services/tests/test_raid_health_result_contract.py`
- `models/tests/test_raid_plan.py`
- `minmax/tests/test_context_factory_passive_progression.py`
- `minmax/tests/test_champion_point_effect_variant_resolver.py`
- `ui/tests/test_phase155_raid_plan_workspace.py`
- `ui/tests/test_phase155_health_endgame_baseline.py`
- `ui/tests/test_phase15_readiness_effective_context.py`
- `ui/tests/test_phase15_readiness_encounter_handling.py`
- `ui/tests/test_contextual_build_editor.py`

Files in the focused feature commit:

- `FEATURES.md`
- `INTELLIGENCE_INTEGRATION.md`
- `SYSTEM_ARCHITECTURE_RULES.md`
- `models/raid_plan.py`
- `services/raid_health_check_service.py`
- `services/raid_plan_context_offensive_stats_service.py`
- `services/raid_plan_endgame_baseline_service.py`
- `services/raid_plan_offensive_stats_service.py`
- `services/raid_plan_pydantic_schema.py`
- `services/raid_plan_repository.py`
- `services/raid_plan_saved_build_resolution_service.py`
- `services/tests/test_raid_plan_endgame_defaults.py`
- `ui/components/raid_plan_endgame_dialog.py`
- `ui/phase15_raid_plan_page.py`
- `ui/phase15_raid_plan_workspace.py`
- `ui/phase15_readiness_page.py`
- `ui/tests/test_raid_plan_endgame_defaults_workflow.py`

Publication: committed on codex/raid-plan-endgame-defaults, then narrowly ported
onto current wyrdworks-dev for the user's subsequent geometry request. Commit
and push identities are supplied by Git, not an installation claim. Existing
worktree source changes are retained separately; data/eso.db is excluded from
all feature/WIP source commits and remains in place.


## 2026-10-23 — Authored Kill & Pull instructions and reference separation

- Canonical destination: Phase15AssignmentStateService, exact plan_id/context_key, stable pull_id and ordered target rows. These are raid-lead plans, not observed execution or verified mechanics.
- Reference source: existing encounter_enemy_candidate_projection, using structured add_group/explicit kill_order_target guide facts and the existing reconciliation owner. Conflicting guide facts and log-only facts do not produce suggestions. Phase context remains explanatory; it never becomes a trash pull identity.
- Consumers: Raid Plan selected-stage readiness preview (Unknown/Planned), explicit modal editor, and Live Raid Now saved-order display. Enemy key and map marker references remain authored opaque references; no automatic map resolution, intelligence ranking or combat behavior is claimed.
- Consumer evidence: ui/tests/test_kill_pull_order_editor.py tests the real checklist click, canonical save and refreshed summary, stage changes and compact geometry. ui/tests/test_phase15_live_raid_now_assignments.py tests saved pull sequence, focus order, seat labels, marker display and scope clearing. ui/tests/test_encounter_enemy_candidate_projection.py tests conflicting references and logs exclusion. The editor tests also establish that reference lookup is on demand and never saves by itself.
- Limits: synthetic disposable plans and Windows Qt offscreen execution; no new ESO mechanic, actual player execution, desktop installation or EXE acceptance. Existing corpus-dependent phase UI assertion is recorded in the issue receipt.

## Phase role teaching copies — 2026-10-26

Existing encounter_movement_route_preview now projects explicit phase/duty/actor requests into canonical designed MapAnnotationPayload copies, bound to exact replay fingerprints and calibrated image geometry. Consumer: Map Workshop Add Phase Role Path, phase filter and ordinary save/reopen/package owners. Separate tank/healer actors and cage rotation slots retain exact reusable seat IDs without guessing people. Raw observations are immutable; boss-flight windows do not imply player flight. Tests: services/tests/test_phase_role_routes.py, ui/tests/test_workshop_phase_role_routes.py, services/tests/test_workshop_map_package_service.py. Bounded operation only: historical tomb timing remains advisory, no cage/release event inference or live eligibility rule is wired.

## Per-dragon Sunspire reference additions — 2026-10-26

Three code65536 source-family evidence packets feed the existing EncounterGuideEvidenceProjectionService and encounter-reference consumers. Tests in services/tests/test_sunspire_guide_review_projection.py verify the correct dragon receives the added details and other dragons do not inherit Frozen Tomb. No database replacement or alternative research engine was introduced.

## Explicit small-waypoint teaching plans

The existing movement-route owner now accepts strict authored waypoint requests (maximum eight) separately from observed extraction. The Lokke recipe records user-supplied tactic provenance, second-flight exception, entrance-side cage identity and two four-DD house groups. Workshop reuses canonical annotation editing/persistence and explicit seat associations; it does not infer live cooldowns or overwrite Raid Plan house positions. Consumer evidence: services/tests/test_simple_teaching_routes.py and ui/tests/test_simple_route_contrast.py (actual light/dark painting, saved color/assignment and duplicate house-seat rejection).
