# BFF System Architecture Rules

These rules apply across the whole BFF / FoundryDock system. They are not feature-specific notes.

## Roadmap authority and concurrent-work safety

The current Phase 15.5 implementation and the current/new roadmap define the active product authority. Older roadmaps remain useful historical requirements and evidence, but they are subordinate when they conflict with newer validated architecture or behavior.

Rules:
- Treat older-roadmap work as additive/reconciliation work, not permission to restore old architecture.
- Before modifying a shared authority boundary, inspect the current implementation and current architecture rules first.
- Preserve newer working behavior unless the requested work is an explicit, evidence-backed improvement to it.
- Never reintroduce retired persistence, routing, service, UI, or engine authorities merely because an older test or roadmap expected them.
- Git conflict detection is insufficient: semantically stale code can merge cleanly. Review for authority regression, duplicate truth, persistence drift, and retired-path resurrection.
- Broad checkout/revert/reset operations are prohibited as a shortcut for roadmap reconciliation. Port narrowly and deliberately.
- When a legacy test contradicts the current contract, repair the test or document the superseded requirement; do not regress production code to satisfy stale expectations.
- Parallel work on the same branch must re-read branch head/current file contents before writes and preserve unrelated newer work.


## Standing product priority: smart, snappy, explainable raid intelligence

**FoundryDock is a reasoning assistant for raid leads, not merely a roster editor, data browser, or meta-build catalogue.** Treat making the application more capable of coalescing the game's large body of mechanics, encounter, combat, roster, skill, set, log, and player evidence into useful team decisions as an ongoing architectural priority on every phase and roadmap. This priority is not deferred until a later feature or confined to one page.

- **Reason over what already exists first.** Inspect `data/eso.db`, the UESP encounter corpus, reviewed encounter facts, service registry, encounter requirement/roster evaluators, provider coverage, build capabilities, rotation evidence, and recommendation services before proposing new storage or engines. Audit missing data *separately* from missing relationships, evaluation, and UI wiring. Extend canonical authorities rather than building parallel sources of truth.
- **Solve the raid lead's actual question.** For the chosen trial, difficulty, stage, team, and roster, derive mechanically relevant requirements, compare viable complete compositions, identify capability/assignment/coverage gaps, recommend actionable alternatives, and explain WHY. Tie every recommendation to the mechanic, build/ability/set/source, provider, recipient, timing, relevant constraints, and evidence that caused it.
- **Encourage clever off-meta choices.** Explore underused armor sets, skills, classes, role configurations, and unusual synergies when they are *mechanically legal and encounter-suitable*. Compare against conventional choices on damage, survivability, sustain, buff/debuff coverage, provider workload, uptime, swapping cost, and reliability. Do not equate popularity or ESO Logs prevalence with optimality; equally, do not claim off-meta performance without proof. Show tradeoffs and confidence, including proposals worth testing.
- **Evidence and uncertainty are first-class.** Maintain source/version/provenance, distinguish canonical mechanics from community practice, observational logs, team strategy, and hypotheses. Unknown must remain unknown; incomplete build, execution, or encounter evidence must never masquerade as confirmed capability, coverage, or DPS. Prefer targeted validation and testable predictions over arbitrary scores and lore-like prose.
- **Close the loop.** Reuse findings across Comp Brainstorm/Comp Engine, Assignments, Coverage, Builds, Rotations, Readiness, Strategy/Raid Map, Live Raid, and post-raid review through typed canonical contracts. Use observed outcomes and raid-lead decisions to improve *evidence-backed recommendations* without silently rewriting official mechanics or another team's plan. Keep context- and team-specific overrides separate from shared encounter facts.
- **Snappy is part of smart.** Avoid full database sweeps, expensive optimization, and synchronous deep inference during page load, save, or navigation. Make deeper comparison on demand, reuse appropriately keyed/invalidation-safe read-only projections, preserve stable outer workspace geometry, and prove performance improvements without weakening correctness or persistence safeguards.
- **Development acceptance question:** For any new mechanic, source, parser, encounter fact, capability, or service, ask: *How will this improve a raid lead's decision, what downstream page/engine consumes it, can the result be explained and validated, and does it remain responsive?* Document and test at least the relevant consumer/handoff; do not count passive data accumulation alone as completed intelligence work.
- **Persistence safety:** Additive database schema/data improvements and safe non-destructive updates are permitted. Do not delete records, drop schema, discard user state, replace/reset either database, or perform destructive synchronization without explicit user approval. Use isolated copies for validation.

## One system, shared mechanics

Extreme Builder, Comp Maker, Team Optimization, Rotation Builder, Performance / Raid Review, roster and provider assignment, encounter logic, and future role-specific tools are different consumers of the same canonical ESO mechanics and runtime-state model.

Do not create parallel versions of the same ESO rule merely because a feature has a different UI or optimization objective.

The intended direction is:

`canonical ESO data -> shared mechanics / runtime contracts -> role- and feature-specific evaluation -> explanation / UI`

Role-specific logic belongs above shared mechanics. Healer, tank, and damage-dealer objectives may interpret or rank the same canonical state differently, but they should not fork the underlying truth.

## Canonical service registry

Before adding a new service, mechanic implementation, evaluator, resolver, repository, orchestration path, or other architectural responsibility, consult the canonical service registry in `services/service_catalog.py` first.

Use the registry to determine whether a canonical service already owns the responsibility, what inputs and outputs it declares, which dependencies it uses, its lifecycle and authority, and which implementation path is authoritative.

If a canonical service already owns the responsibility, reuse or extend that service rather than creating a parallel implementation.

If a genuinely new architectural responsibility is introduced, add an explicit descriptor to the appropriate registry family so it is discoverable through `SERVICE_CATALOG` and covered by registry-integrity tests.

The registry is discovery metadata, not a dynamic service locator. Application code should continue to use normal typed imports and explicit dependency wiring rather than instantiate or execute implementations by string identity.

Registry consultation is a required architectural discovery step, not an optional convenience. This applies across Extreme Builder, Rotation Builder, Comp Maker, Team Optimization, Performance / Raid Review, encounter/provider systems, and future engines.

## Project knowledge capture

BFF keeps durable project knowledge in shared indexes. Development work should update them when the corresponding kind of knowledge is discovered or created.

### Game mechanics field notes

Whenever development, testing, real-build validation, encounter research, or data reconciliation reveals something mechanically odd or noteworthy, add a short layman's note to `GAME_MECHANICS_FIELD_NOTES.md`.

Use this for ESO behavior that is easy to misunderstand, surprising in practice, version-sensitive, or likely to cause future implementation drift. Capture the practical rule and why it matters. Do not turn ordinary refactoring, architecture cleanup, or routine implementation details into game-mechanics field notes.

### Feature index

Whenever a new user-visible capability or feature is created, add or update its entry in `FEATURES.md` so the application has a durable index of what it can do.

Keep the index descriptive rather than sales-oriented. Internal correctness work, tests, caches, audits, and implementation plumbing do not need feature entries unless they create or materially change a user-visible capability.

### Useful source registry

Whenever research uncovers a useful external source for ESO mechanics, data, logs, calibration, validation, or implementation reference, add it to `useful_resources.md`.

`useful_resources.md` is a working source registry for BFF / FoundryDock research and combat-math validation. It is not merely a link collection. Each source entry should say what the source is useful for and how much confidence should be placed in it before turning information into hardcoded game math. Record version, date, provenance, or limitations when those materially affect interpretation.

### ESO numeric ID registry

Whenever development, log analysis, historical research, data reconciliation, or external-source review identifies a reusable ESO numeric ID, alias, display ID, effect ID, source ability ID, raw ESO Logs ID, or other numeric handle, consult and update `ESO_ID_REFERENCE.md`.

The registry is deliberately evidence-oriented. Stable BFF skill/effect identity remains semantic `lower_snake_case`; numeric ESO IDs are aliases, source handles, or observations and may vary by component, morph, caster, target, event type, bundle, update, or source system.

When adding an ID, preserve its exact role/context, provenance, confidence, and update/year when version-sensitive. If a second numeric ID appears for the same semantic identity, add it rather than silently replacing the earlier observation. Unknown or contradictory IDs stay explicit until reviewed.

The bulk Major/Minor effect alias corpus remains in `docs/major_minor_effect_ids.md`, and detailed raw ESO Logs event-tag research remains in `ESO_LOGS_RAW_TAG_REFERENCE.md`; `ESO_ID_REFERENCE.md` is the shared cross-system index and rule-of-use document.

## Gameplay-practice policy is a separate layer

BFF must distinguish between **what ESO mechanically permits** and **how organized players normally choose to play**.

Canonical mechanics remain the authority for coefficients, costs, durations, targets, triggers, cooldowns, range, combat events, and other engine truth. Gameplay-practice policy may rank, discourage, prefer, require, or explain choices made from those mechanically legal options, but it must not rewrite the underlying mechanic.

The shared gameplay-practice registry lives in `data/gameplay_policy/` with human-readable rationale in `ENDGAME_PLAY_PRACTICES.md` and read-only access through `services/gameplay_policy_service.py`.

The intended decision order is:

`mechanical legality -> normal role/content practice -> encounter/assignment context -> explainable override`

Do not hardcode the same raid convention independently into Extreme Builder, Rotation Builder, Comp Maker, Team Optimization, or Performance. Consumers should query the shared policy layer and apply their own feature-specific objective above it.

Practice rules are contextual defaults, not universal laws. Encounter assignments may override them when the assignment materially changes support access, survival obligations, positioning, role responsibilities, or other conditions that made the default sensible.

## Testing rule: prove reusable contracts

When work in one engine exposes or verifies a reusable mechanic, state, timing rule, legality rule, candidate rule, or optimization invariant, tests should be written with downstream reuse in mind.

In particular, findings from Extreme Builder development should be usable to strengthen Comp Maker and Team Optimization rather than remaining trapped inside Extreme-specific assumptions.

For shared behavior, tests should answer both questions:

1. Does the originating feature behave correctly?
2. Is the underlying contract sufficiently role-neutral and deterministic that another BFF engine can safely consume it?

Prefer shared contract tests plus thin feature-specific tests over duplicating the same mechanic independently in Extreme, Comp Maker, Team Optimization, Rotation, or Performance.

## Runtime state

There must be one authoritative runtime truth for a given evaluation snapshot. Consumers should use canonical projection properties/services rather than maintaining feature-local copies of attempts, buff windows, potion timing, proc state, or encounter state.

Compatibility fields may exist during migrations, but they are bridges, not competing sources of truth.

## Optimization and composition

Extreme optimization is a useful proving ground for exhaustive candidate mechanics, but its findings are part of the larger system.

When an Extreme rule is validated and is not inherently role-specific, prefer making it reusable by:

- Comp Maker candidate construction and legality,
- Team Optimization candidate comparison and constraints,
- Rotation Builder timing/state evaluation,
- provider and coverage evaluation,
- Performance / Raid Review explanation and validation.

Do not copy the result into those engines as hard-coded conclusions. Reuse the canonical mechanic or shared service that produced the result.

## Shared candidate-plan boundary

Comp Maker, Team Optimization, Extreme Builder, and Rotation Builder must converge on one shared candidate-plan boundary rather than exchange feature-local conclusions.

The intended ownership is:

`canonical Character / Build -> Extreme candidate evidence -> Rotation execution evidence -> complete candidate plan -> Comp Maker selection -> Team Optimization improvement`

A **complete candidate plan** represents one exact proposed player/chair configuration and preserves the structured evidence needed by downstream consumers. At minimum, where applicable, that includes canonical character/build identity, exact build changes, candidate/source identity, role and class, gear and skills, runtime assumptions, rotation/execution evidence, support/provider effects, recipient and temporal coverage, sustain/resource evidence, encounter scope, unresolved/unsupported evidence, and provenance/confidence.

The boundary follows these rules:

1. **Upstream engines resolve mechanics once.** Extreme Builder and Rotation Builder may discover or evaluate mechanics through canonical shared services. Their downstream output must retain the evidence/result needed by consumers rather than requiring Comp Maker or Team Optimization to rediscover the mechanic independently.
2. **Comp Maker chooses complete plans.** Comp Maker may compare suitability, composition fit, role/assignment constraints, provider coverage, workload, and encounter relevance, but it must not rebuild Extreme math or Rotation mechanics from display text, heuristics, or duplicate formulas.
3. **Team Optimization improves the same plans.** Optimization starts from the exact selected candidate plan and proposes explicit changes while preserving its canonical identities and evidence boundaries. It may call the authoritative upstream/shared evaluator again for a changed candidate, but it must not substitute a local approximation for an already-owned mechanic.
4. **No prose reconstruction.** Human-readable explanations, score reasons, UI labels, and report text are presentation outputs. Application state must travel through structured typed fields/contracts, not by parsing those strings back into mechanics, gear, skills, assignments, or assumptions.
5. **No silent evidence loss.** Unknown, unsupported, conflicting, partial, or assumption-bound evidence remains attached when a candidate crosses Extreme -> Rotation -> Comp Maker -> Optimization -> Roster. A downstream consumer may reject or defer the candidate, but it may not erase the boundary and treat it as proven.
6. **Identity is stable across the round trip.** Character, baseline Build, candidate Build, team, chair/slot, source/template, rotation plan, and encounter identity must remain distinguishable. Generated-plan persistence may be an implementation detail, but it must not create a second competing user-facing team/build identity.
7. **Results are reusable, not frozen conclusions.** A downstream change to gear, skills, assignment, encounter, runtime assumptions, or rotation invalidates only the evidence that depends on that change. The appropriate authoritative service should recompute that evidence; unaffected canonical evidence should be preserved rather than rediscovered wholesale.
8. **Ranking is consumer-owned; mechanics are not.** Extreme Builder may optimize an Extreme objective, Rotation Builder may optimize execution, Comp Maker may optimize composition, and Team Optimization may optimize the assigned team. Those rankings can differ. They must still consume the same underlying mechanic/evidence truth.

Tests for this boundary should prove that an exact candidate can move between engines without silent identity mutation, evidence loss, favorable UNKNOWN coercion, or mechanics being reconstructed from presentation strings.

## Phase 15.5 page ownership and persistence contracts

The Phase 15.5 application is one workflow with shared repositories, not a collection of independent mini-apps. Every page must have an explicit authority boundary so navigation, autosave, engine handoffs, and future refactors cannot silently create competing truth.

General page rules:

- A page may present or edit only the state it explicitly owns or has been given authority to modify.
- A page that depends on a Raid Plan must fail closed when no saved/loaded Raid Plan is active. It must not invent a plan, silently fall back to an unscoped persistence identity, or report a successful save when nothing durable was written.
- User-authored mutable page state belongs in `user_data/foundrydock.db` unless a documented repository intentionally owns another user-data location. Canonical ESO/reference truth remains in `data/eso.db`.
- Page persistence inputs must cross the appropriate strict Pydantic boundary before durable write whenever a schema exists or can reasonably exist.
- A successful save means durable write plus read-back verification of the intended identity. Dirty state must not clear merely because an INSERT/UPDATE was attempted.
- Navigation, stage switching, plan switching, and application shutdown must honor the owning page's save/flush contract. Failure to persist keeps the user on the page rather than silently discarding work.
- Display strings are not application state. Handoffs use stable typed identities and structured payloads, never prose reconstruction.
- Pages may consume shared mechanics/services but must not become alternate mechanics authorities.
- Compatibility reads may remain during migration. New writes must use the current authority.
- No page may erase richer state owned by another page just because its local snapshot is stale or incomplete.
- Stage-aware pages use the shared `RaidStageController` and the active Raid Plan's persisted stage/context identities. They do not create private competing stage truth.

### Landing / Foundry

**Owns:** entry/navigation intent only: create a new Raid Plan request, load an existing plan, open Team/Roster, and display recent/Tonight summaries.

**Requires:** no active Raid Plan.

**Persistence:** the Landing page itself owns no raid-planning persistence. Creating a plan request is not the same as persisting a Raid Plan.

**Allowed handoffs:** Raid Plan creation dialog -> Raid Plan editor; recent plan identity -> exact Raid Plan load; Team/Roster navigation.

**Must not:** create hidden plans, mutate roster/build/assignment state, or infer a current plan from display text.

### Raid Plan

**Owns:** one raid-specific planning identity: plan id/name, trial, difficulty, ordered stages/contexts, plan members/chairs, plan-owned notes, selected character/build references, and other explicitly Raid-Plan-owned decisions.

**Requires:** nothing to begin a new draft; persistence requires a valid Raid Plan identity.

**Persistence:** `RaidPlanRepository` in `foundrydock.db`, with exact read-back. Stage order/selection remains in the canonical Raid Plan stage repository/controller path.

**Allowed handoffs:** seeds context for Roster, Comp Brainstorm, Assignments, Builds, Coverage, Rotations, Readiness, Strategy, Live Raid, and engine pages.

**Must not:** own reusable Personnel, Character, Saved Build, Team, or canonical ESO mechanic truth. A plan references those identities; it does not duplicate them.

### Roster

**Owns:** Team membership/availability presentation and raid-chair assignment workflows that explicitly belong to roster/team planning.

**Requires:** may be opened without a Raid Plan for Team/Character management; plan-specific chair work requires the active Raid Plan.

**Persistence:** reusable Personnel/Character/Team data remains in their canonical user-data repositories. Raid-specific chair selections write through the Raid Plan authority, not a parallel roster-plan store.

**Allowed handoffs:** selected people/characters into Raid Plan chairs; exact canonical identities downstream.

**Must not:** create duplicate Character or Build identity, overwrite Saved Builds, or silently mutate raid-specific assignments owned by other pages.

### Comp Brainstorm / Comp Maker

**Owns:** low-authority, raid-lead composition brainstorming for one exact Raid Plan, including seat-level draft choices, per-stage planned gear/build references, Mundus, blue/red CP choices, scribing notes, and freeform raid-lead notes.

**Requires:** a saved/loaded active Raid Plan. Normal Phase 15.5 Comp Brainstorm is never plan-less. The page must verify that its cached Raid Plan id and the shared stage controller plan id agree before editing or saving.

**Persistence:** exclusively plan-scoped Comp Brainstorm persistence in `foundrydock.db` for current writes. The scope identity (`plan_id + draft_name`) and the draft payload must cross strict Pydantic validation. Save succeeds only after exact read-back verification. Dirty state persists on page leave, stage change, plan change, and shutdown through the page flush contract.

**Compatibility:** old name-only drafts may remain readable/adoptable as migration input so prior work is recoverable. Native Phase 15.5 writes must not continue updating that retired unscoped identity.

**Allowed handoffs:** Save persists Brainstorm only. **Save to Draft Build** is the explicit promotion path into Saved Build work; promotion must preserve Character/Player/Raid Plan identity and stage context. Comp Maker may consume shared offensive-stat/mechanics services but does not own their formulas.

**Must not:** create a Raid Plan, create a Saved Build on ordinary Save, silently succeed without a plan, clear dirty state without verified persistence, parse freeform notes into mechanics, or write competing unscoped Brainstorm state.

### Assignments

**Owns:** raid-specific responsibility decisions: mechanics jobs, utility jobs, buff/debuff providers, house-stack/portal/group choices, and explicit raid-lead assignment overrides.

**Requires:** an active Raid Plan for writes.

**Persistence:** assignments are Raid-Plan-owned or assignment-repository-owned according to the current canonical assignment service. Writes must retain stable seat/provider/encounter identities and read back before leaving dirty state.

**Allowed handoffs:** exact provider/responsibility identities to Coverage, Rotations, Strategy/Raid Map, and Live Raid Now/call surfaces.

**Must not:** invent mechanics, infer provider uptime from capability presence, change reusable Saved Builds merely to satisfy an assignment, or replace Strategy/Raid Map manual overrides with hidden assignment heuristics.

### Builds

**Owns:** reusable Saved Build editing and raid-stage build selection/projection where explicitly supported. Exact gear pieces, traits, enchants, bars, skills, attributes, progression references, and stage variants belong to structured Build contracts.

**Requires:** reusable Build editing may exist independently; raid-stage application requires the active Raid Plan/chair identity.

**Persistence:** Saved Builds use the canonical Character -> Build persistence path in `foundrydock.db`. Stage selections remain plan references/overlays rather than duplicate Builds unless the user explicitly saves/promotes a new Build.

**Allowed handoffs:** canonical Build identity and structured build evidence to Comp, Coverage, Rotations, Readiness, Extreme Builder, Optimization, and exports.

**Must not:** silently fork Characters, flatten stage variants into one ambiguous build, infer missing equipment facts as known, or overwrite a Saved Build merely because a Raid Plan selected a different stage setup.

### Coverage

**Owns:** evaluation and raid-lead assertions of required buffs/debuffs/utility coverage for the active Raid Plan/stage.

**Requires:** active Raid Plan for plan-specific evaluation and edits.

**Persistence:** explicit raid-lead provider overrides/coverage choices are Raid-Plan-owned overlays. Canonical source/mechanic evidence remains read-only shared mechanics truth.

**Allowed handoffs:** structured covered/missing/needs-review evidence to Rotations, Readiness, Optimization, Live Raid, and explanations.

**Must not:** treat capability presence as proven uptime, erase explicit provider assignments, invent unknown mechanics, or create a second buff/debuff catalog.

### Raid Health / Performance Review

**Owns:** analysis of observed or simulated raid/player performance and actionable review findings. It is an evaluator/reporting surface, not a canonical mechanics store.

**Requires:** an active Raid Plan or explicit analysis context when reviewing team/raid state.

**Persistence:** user-authored review state may persist through its canonical review repository; observed evidence remains linked to provenance/log/run identity.

**Allowed handoffs:** selected findings/candidate concerns to Builds, Coverage, Rotations, Extreme Builder, Optimization, and Readiness.

**Must not:** rewrite source logs, mutate Builds from a finding without explicit user action, or turn heuristic observations into canonical game mechanics.

### Rotations

**Owns:** executable/scheduled player action plans, timing/cadence decisions, resource/ultimate feasibility projections, and rotation-specific evidence.

**Requires:** exact player/chair + canonical Build/candidate + encounter/stage context for plan-specific generation.

**Persistence:** authored/generated rotation plans use the canonical rotation persistence path and retain source Build/candidate/encounter identities and unresolved evidence.

**Allowed handoffs:** execution evidence into candidate plans, Coverage, Readiness, Extreme Builder, Optimization, and Live Raid call planning.

**Must not:** invent mechanic durations/costs/cooldowns, reconstruct Builds from prose, or silently convert unsupported timing into executable certainty.

### Readiness

**Owns:** readiness evaluation and explicit human ready/confirmed state for the active Raid Plan. It aggregates; it does not duplicate source truth.

**Requires:** active Raid Plan for team readiness.

**Persistence:** human confirmation/readiness state uses its documented plan/user-data authority. Derived readiness findings are recomputed from canonical plan/build/assignment/coverage state rather than copied into competing stores.

**Allowed handoffs:** navigation to Comp Engine, Optimization, Extreme Builder, Builds, Coverage, Rotations, and Strategy for fixing deficiencies.

**Must not:** mutate Builds/Assignments automatically, treat missing evidence as ready, or replace canonical source state with a readiness cache.

### Strategy / Raid Map

**Owns:** raid-lead strategy presentation and authored spatial/visual encounter overlays: markers, shapes, labels, paths, formations, map assets, and explicit manual placement overrides.

**Requires:** active Raid Plan for plan-owned strategy/maps; standalone workshop assets may have their own explicit draft contract.

**Persistence:** plan strategy/map state uses the canonical raid-map/strategy repository with exact plan/context identity. Custom uploads/assets remain references, not hidden mechanics truth.

**Allowed handoffs:** exact current-stage strategy/positions/assignments to Live Raid.

**Must not:** silently rewrite Assignments when the user manually repositions a marker unless an explicit documented command does so; must not derive canonical mechanics from drawing geometry.

### Live Raid

**Owns:** runtime presentation of already-authored plan truth: current stage/phase, key mechanics, Now assignments, raid calls, support ultimates, and map/strategy display.

**Requires:** active Raid Plan and stage/context.

**Persistence:** Live Raid should normally be presentation/runtime-state oriented. Any user-owned runtime annotations must use an explicit runtime repository; they must not mutate planning state merely by being displayed.

**Allowed handoffs:** consumes Raid Plan, Assignments, Rotations, Strategy/Raid Map, Coverage, and readiness/runtime evidence.

**Must not:** become a second Assignments editor, invent a provider/call because upstream state is missing, or persist transient display state as canonical planning truth.

### Comp Engine

**Owns:** composition recommendation/evaluation of candidates for raid chairs using canonical mechanics, assignments, coverage, and candidate-plan evidence.

**Requires:** active Raid Plan/chair context for actionable recommendations.

**Persistence:** recommendation results are evidence/candidates until explicitly adopted. Adoption must use structured candidate-plan handoffs.

**Allowed handoffs:** candidate -> Optimization review, Extreme Builder test, or explicit plan/build adoption path.

**Must not:** directly rewrite canonical Builds/Characters, rediscover Extreme/Rotation mechanics locally, or treat recommendation prose as state.

### Team Optimization

**Owns:** team-wide comparison and explicit proposed improvements across the already-selected candidate plans/chairs.

**Requires:** active Raid Plan plus exact candidate/build identities and relevant assignment/encounter context.

**Persistence:** optimization output is proposal/evidence until the user explicitly applies it through the owning Build/Raid Plan/Assignment path.

**Allowed handoffs:** changed candidate back through canonical evaluators, Builds, Coverage, Comp Engine, Extreme Builder, and Raid Plan application.

**Must not:** mutate multiple user-owned identities merely to improve a score, substitute local approximations for shared mechanics, or discard unresolved evidence.

### Extreme Builder

**Owns:** deep single-player exhaustive candidate exploration and mechanical evidence generation.

**Requires:** exact Character/Build or explicit candidate input for actionable evaluation.

**Persistence:** candidate work/results use the documented candidate/build path; baseline Saved Builds stay untouched until explicit promotion/adoption.

**Allowed handoffs:** structured candidate evidence to Rotation, Comp Maker, Team Optimization, Raid Health, and Build adoption workflows.

**Must not:** become a second Character/Build database, hardcode mechanics already owned by shared services, or silently convert an experimental candidate into the user's Saved Build.

### Map Workshop

**Owns:** explicit map/diagram authoring drafts and reusable map assets independent of a Raid Plan when the workshop contract allows it.

**Requires:** no Raid Plan for standalone workshop drafting; attaching/applying a map to a Raid Plan requires explicit plan/context identity.

**Persistence:** workshop drafts/assets use the canonical map-workshop repository and must honor unsaved-change navigation guards.

**Allowed handoffs:** explicit apply/attach into Strategy/Raid Map.

**Must not:** silently attach drafts to a Raid Plan, discard dirty work on navigation, or convert visual geometry into game-mechanic truth.

### Gear

**Owns:** read/search/explain canonical gear/reference information.

**Requires:** no active Raid Plan.

**Persistence:** normally read-only against canonical ESO/reference data; any user favorites/notes require a separate documented user-data contract.

**Allowed handoffs:** exact canonical gear identity into editors/selectors where explicitly invoked.

**Must not:** mutate `eso.db` through browsing, infer build ownership, or create Saved Builds from viewing an item.

### Collectibles

**Owns:** presentation and user-owned progress/import state for collectibles, antiquities, motifs, recipes, lorebooks, and related catalog surfaces.

**Requires:** no Raid Plan.

**Persistence:** canonical collectible definitions remain in `eso.db`; user progress/learned state belongs in user-owned persistence.

**Allowed handoffs:** collection/progress evidence to relevant readiness or utility surfaces only when explicitly modeled.

**Must not:** store user progress in canonical reference rows or let collection state alter combat mechanics without an explicit canonical dependency.

### Achievements

**Owns:** canonical achievement browsing plus user-owned completion/progress/import state.

**Requires:** no Raid Plan.

**Persistence:** achievement definitions remain canonical ESO data; personal progress remains user-owned.

**Allowed handoffs:** achievement evidence to profile/readiness/history features where explicitly modeled.

**Must not:** mutate canonical achievement definitions or infer raid readiness solely from an achievement badge.

### Top Gear

**Owns:** observed/researched gear usage trends and snapshots by trial/role, with provenance and timestamp.

**Requires:** no active Raid Plan to browse; plan context may filter/recommend when explicitly requested.

**Persistence:** trend snapshots/research data remain observational evidence, separate from canonical mechanic truth and user Saved Builds.

**Allowed handoffs:** evidence/recommendation context into Comp, Builds, Extreme, or Optimization.

**Must not:** auto-rewrite user Builds, equate popularity with mechanical optimality, or hardcode a trend as a canonical ESO rule.

### Settings

**Owns:** application/user preferences, connector/configuration values, safe UI/accessibility preferences, and documented optional-module configuration.

**Requires:** no Raid Plan.

**Persistence:** settings use the canonical settings/credential paths; secrets belong in the approved credential store rather than ordinary JSON when supported.

**Allowed handoffs:** configuration only.

**Must not:** become a hidden mechanics override store, reset user databases, or silently change persistence authorities.

### Cross-page promotion rule

Moving data between pages is not ordinary copying. Every promotion must name the owning identities on both sides and preserve provenance.

Examples:

- Comp Brainstorm -> Draft Build is an explicit promotion; ordinary Comp Save is not.
- Extreme/Comp Engine/Optimization recommendation -> Saved Build requires explicit adoption.
- Assignment -> Live Raid is presentation of the same responsibility identity, not a new assignment.
- Strategy/Raid Map manual placement may override visual position without silently rewriting upstream assignment ownership.
- Coverage evidence may inform Readiness/Optimization without becoming a duplicate buff/debuff mechanic store.
- Roster/Team identity may seed a Raid Plan chair, but the Raid Plan remains owner of raid-specific selections.

If a page handoff cannot identify the source owner, destination owner, stable identity, persistence result, and rollback/recovery behavior, the handoff is not yet architecturally safe.

## Code retirement and quarantine

BFF preserves old code deliberately when it may still matter for compatibility, migration, forensic comparison, or historical reference. Do not treat a quick unreferenced search as proof that a file is safe to delete.

Use the retirement path:

`live runtime -> deprecated -> legacy or migration -> delete only after proof`

The directory meanings and proof checklist are defined in `docs/CODE_RETIREMENT_AND_QUARANTINE.md`.

Normal runtime code under `engine/`, `minmax/`, `models/`, `services/`, and `ui/` must not import from `legacy/`, `deprecated/`, `old_pages/`, or `migration/`.

- `deprecated/` contains still-callable code being phased out. It must not gain new production consumers.
- `legacy/` contains compatibility/history preserved after normal production callers have migrated away.
- `migration/` contains explicit old-data/schema/identity transition code. It may be invoked deliberately by migration/bootstrap tooling, but it is not a normal runtime authority.
- `old_pages/` is archival UI/reference material only. Runtime imports from it are forbidden.

Before moving a file into quarantine, prove its callers, canonical replacement, focused tests, service/architecture ownership, and persisted-data implications. Broad or cross-domain moves should also receive an appropriate full regression run.

Deletion is the final cleanup step. Keep a quarantined implementation until no supported migration or compatibility path needs it and tests prove removal safe.

## Fail closed

Unknown, unsupported, or mechanically ambiguous ESO behavior stays explicit. No BFF engine may turn missing evidence into a favorable optimization assumption.

This rule is system-wide.

## Practical development rule

Be exhaustive about mechanical coverage, but do not spend development time polishing already-sufficient infrastructure merely because it can be made prettier. Prioritize closing real coverage gaps, proving shared contracts, and moving executable behavior toward completion.

### User-owned workspace dimensions

The Phase 15.5 desktop shell owns the outer workspace dimensions. Individual pages, tables, dialogs embedded as pages, save handlers, refresh handlers, stage changes, and analysis results must adapt inside the current shell rather than resizing the top-level window.

- restore the user's last normal Phase 15.5 window size at startup;
- persist only user-driven normal-window resizes;
- child page size hints must not enlarge the shell during navigation, load, save, refresh, filtering, or analysis;
- overflow belongs in fluid layouts, splitters, and scroll areas rather than top-level window growth;
- fixed dimensions remain acceptable for deliberate small UI elements, but not as a mechanism for forcing the application window larger.

**Contract:** outer workspace dimensions do not change unless the user resizes the window or explicitly changes window state.

