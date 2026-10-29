# Wyrdworks — Architecture and ownership (formerly FoundryDock)

Working/concurrency rules: [CLAUDE.md](CLAUDE.md). Validation, save reliability and completion: [DEVELOPMENT_STANDARD.md](DEVELOPMENT_STANDARD.md). Knowledge routing: [AGENTS.md](AGENTS.md). Do not repeat their requirements here.

## Current Wyrdworks workflow and data-first access

Wyrdworks is the product name; FoundryDock remains the repository and technical identifier. Raid Plan is the only active raid-planning UI, with Teams, Map, and Readiness columns; Roster, Assignments, Builds, Map Workshop, and Finch / Collaboration remain supporting capabilities where required by Raid Plan. Lantern, Comp Brainstorm, Coverage, Rotations, standalone Readiness, Health, Comp Engine, Optimization, Extreme Build, and Live Raid interfaces are parked. Preserve their code, behavior, records, integrations, shared-service access, and regression tests. Do not make their UI construction, navigation, redesign, benchmark, or page-specific save/reopen a gate for unrelated work. This status applies to interfaces, not to whether their canonical data or reusable service capabilities may support active workflows.

Performance work prioritizes fast access to authoritative data for the active workflow over isolated page micro-optimization:

- Load the current Raid Plan, stage, seat identities, assignments, and required Saved Builds before optional reference-heavy information. Load only the data needed for the current action.
- Keep repositories and services independent of widgets. Extend canonical owners from `services/service_catalog.py`; do not duplicate calculations or construct a parked page to reach its data.
- Identify repeated queries, repeated Pydantic validation, repeated capability audits, and unnecessary recalculations before proposing optimization. Do not add speculative caches as a default remedy.
- Any scoped cache must state its dependencies, freshness, and invalidation behavior. Plan, stage, Saved Build revision, and relevant source changes invalidate dependent evidence. Reject stale results and never present stale or incomplete evidence as current or verified.
- Preserve strict validation, provenance, exact identities, and user data; performance shortcuts cannot lower evidence quality.

Detailed page ownership contracts below remain an inventory of existing capabilities and boundaries. Where they describe parked page construction, UI acceptance, or future handoffs, this current scope policy controls prioritization; it does not authorize removing code, data, or tests.

## Shared system

Canonical ESO data → shared mechanics/runtime contracts → role/feature evaluation → explanation/UI. Extreme, Combat, Encounter, Rotation, Comp, Coverage, Optimization, Readiness and Live Raid consume the same mechanics; role objectives may differ but formulas must not fork. `data/eso.db`, `math/` evidence and `data/eso_info/` corpus have distinct roles; raw/imported rows are not reviewed truth merely because they are stored.

Consult `services/service_catalog.py` before adding a responsibility. Reuse/extend its owner. Register genuinely new owners with integrity tests. The registry is discovery metadata, not a dynamic service locator. `services/foundry_intelligence_service.py` is a read-only projection, not another math engine.

Make intelligence useful: identify a raid-lead decision, exact provider/recipient/target/time context, source and confidence, tradeoffs and consumer. Consider supported off-meta options without claiming popularity is optimality or unknown damage is proven. Keep deeper analysis explicit and off the UI thread.

## Identity and evidence

Stable skill/effect/mechanic identity is semantic `lower_snake_case`. Numeric IDs are contextual aliases and must resolve with provenance before downstream evaluation. Preserve player, Character, baseline/candidate Build, team, plan, seat, stage, encounter, source and rotation identities separately. Exact selected IDs win over display-name fallback.

One authoritative runtime snapshot owns events, attempts, buff windows, potion timing and proc state. Explanations are outputs; never parse prose back into application state. Keep unknown/conflict/partial/unsupported evidence through every handoff. Dependency-specific gaps block relevant decisions; unrelated global gaps remain advisory.

Mechanical legality precedes gameplay practice and encounter-specific exceptions. Practice policy remains in `data/gameplay_policy/` via `services/gameplay_policy_service.py`, explained in [ENDGAME_PLAY_PRACTICES.md](ENDGAME_PLAY_PRACTICES.md). Observed logs, hypotheses and team strategy remain separate from formulas.

## Retained domain invariants

- Preserve healer/DD/tank boundaries and hard sustain/provider/capability constraints. Unknown consequences cannot win ranking. Provider obligations cannot be silently reassigned away to improve a candidate.
- Candidates are immutable; deterministic tie-breaks do not prove ESO superiority. Distinguish modeled potency, actual HPS, sheet maxima, runtime damage and measured DPS.
- Base ability families and selected morphs are distinct; resolve names from canonical data. Preserve scribing/subclass ingredients and source evidence instead of guessed names.
- Keep Health, Magicka, Stamina, highest-resource, highest-attribute and fixed scaling separate. Preserve PvE/PvP/campaign restrictions.
- CP progression and active slottables differ; four slots per discipline. Preserve rank, allocation, eligibility and current-update evidence; do not infer ownership or magnitudes.
- Sparse Context Variants resolve through the existing shared resolver; absent fields inherit rather than empty the build. See [BUILD_CONTEXT_VARIANT_BEHAVIOR.md](BUILD_CONTEXT_VARIANT_BEHAVIOR.md).

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

## Phase 15.5 performance, interaction and asset invariants

These are persistent product requirements, not optional cleanup tasks. Apply them when building or changing a page, shell, theme, image asset, importer or test. Preserve existing owner boundaries, data safety, user-selected outer-window geometry and the actual saved draft/plan state.

**Page lifecycle and data access**

- Construct only the minimum shell, landing surface and shared context/controllers at startup. Register other pages as factories and construct each on its first navigation. Reuse that instance on subsequent visits. A page must never need to be opened merely to initialize an unrelated page. Guard signal connections, saved drafts, exit checks and cross-page handoffs when a target page is not constructed yet.
- Reference databases are not page models: no full-database materialization on page creation, navigation, refresh or category selection. Fetch bounded records via the canonical service using stable IDs, active context, search/filter or pagination. Favor targeted SQL, indexes and projections over repeated broad queries; don't silently copy reference data into the user database.
- **Achievements and Collectibles are truly on demand:** do not construct/populate their browser trees, read every achievement/collectible or enumerate every category's items at app startup. The page may load a bounded category directory when first opened; only load records in a specific category/subcategory when selected, and fetch details only for the selected record. Search is scoped and bounded, with incremental results. Profile-specific completion remains separate from reference data and must be accurate for the active profile. Closing/reopening or navigating away must not lose state.
- Expensive calculations, reference queries and intelligence evidence are not automatically rerun on every navigation. Cache/reuse by explicit plan, stage, build, assignments, profile, reference revision and other actual dependencies. Invalidate only affected results when evidence changes. Preserve stale-result rejection, explicit refresh, draft visibility and canonical readback. Heavy inference must not block the UI thread; never trade away strict validation for speed.
- Measure cold startup to interactive window, first page/category opening, second opening, repeated navigation and refresh using realistic data. Initial latency must not simply move to the first click. Avoid blanket console dumps and repeated tooltip/style generation in hot paths.

**Interaction and layout**

- Use concise visible labels and a small number of meaningful help affordances. Tooltips/hover help are reserved for ambiguous icons, unfamiliar terminology and consequential controls; do not attach repetitive rollover explanations to every item, cell, card or widget. Keep accessible names, focus navigation and essential status/error text.
- Enforce the single-scroll page geometry rule below also in **Encounters**: one outer page scroll; no extra vertical scrollbars in its middle or right panels. Long encounter content must reflow, collapse or render incrementally without overlapping columns, hiding Save-to-Live-Raid actions or changing the outer-window size.
- Use one fixed Urban Wilderness visual theme with centralized palette, typography and accessible/seizure-safe tokens. Do not add selectable theme variants or a new theme-management service. Existing compatibility wrappers may remain until migrated safely; removing them must preserve settings compatibility, rendering, accessibility and tests. Profile the stylesheet/import costs rather than assuming a renamed class improves startup.

**RAVEN / FORGE asset policy (canonical)**

- **Theme asset scope:** RAVEN/FORGE covers the canonical `assets/themes/Bff/urban_wilderness` directory and the explicitly approved Wyrdworks Granite directory `assets/themes/granite`. Granite's stone surface and collectible badge atlas are referenced and packaged from the Granite directory; do not duplicate them under Urban Wilderness. Exclude the entire `assets/themes/Bff/urban_wilderness/notes` subtree from inventory, hashing, duplicate analysis, size totals, candidate classification and conversion. Ignore all other theme directories. Independent non-theme game/raid asset directories may still be inventoried and reviewed separately.
- **SVG** remains the runtime format for scalable UI icons, symbols and simple vector embellishments. Never rasterize efficient SVGs merely to meet a conversion target.
- **Transparent PNG sprite sheets** and small transparent PNG UI assets may remain PNG when suitably sized and efficient. Preserve transparency, sprite-cell coordinates, icon indices, bounds and Qt rendering behavior. Do not broadly replace sprites or assume a smaller file is faster.
- **WebP** is the preferred runtime format for photographic/illustrated banners, headers, boss-box/boss portrait art, trial/encounter/map imagery and large background illustrations. New assets in these categories should be WebP; migrate existing assets in reviewed batches with references verified. Preserve exact image dimensions/aspect ratio and map marker coordinate alignment.
- **ICO** remains supported for Windows integration. Keep original/editable source artwork where necessary; no mass deletion of PNG, SVG or source masters.
- **RAVEN inventories, classifies and flags assets**: duplicates, large files, stale paths, transparency, dimensions, format suitability, reference owners, and conversion benefit. **FORGE converts eligible raster art to WebP**, lossless where pixel-exact rendering matters and quality-controlled lossy for illustration. Conversion requires a dry run, source fingerprints/idempotence, a size comparison, a manifest, decoded-image validation, safe path/reference updates, and a reversible rollback. Skip files that gain nothing from conversion.
- An asset conversion is incomplete until real Qt image loading, responsive layout, transparent sprite integrity and encounter-map coordinate/marker alignment are tested. Do not break packaged-resource resolution.

## Phase 15.5 page ownership and persistence contracts

The Phase 15.5 application is one workflow with shared repositories, not a collection of independent mini-apps. Every page must have an explicit authority boundary so navigation, autosave, engine handoffs, and future refactors cannot silently create competing truth.

General page rules:

**Single-scroll page geometry:** Every Phase 15.5 workspace page has **one primary vertical scrollbar, on the far-right outer edge**. Keep that scrollbar **thin and visually quiet** (target a roughly 8 px track at normal desktop scaling), styled in the Urban Wilderness slate palette with a subtly contrasting thumb; ensure a usable mouse hit area and keyboard/wheel access, and respect system accessibility and DPI scaling. Avoid thick default widget scrollbars or decorative high-contrast rails. The entire page content scrolls together. Do not add nested vertical scroll areas, independently scrolling center/right columns, scrollable inspector tabs, or secondary visible scrollbars in lists, tables, text panes, and cards. Preserve the user's outer-window dimensions; wrap and reflow long content within available width. For large searchable collections, use filtering, collapsing, or incremental rendering rather than a second scrolling viewport. Keyboard and wheel scrolling must target the same page-level scroll, and source links/buttons remain usable. Any widget with built-in scrolling must disable that internal scrolling and be sized/replaced appropriately. Enforce with a real Qt geometry and wheel-interaction test at representative window sizes; static-source tests alone do not prove compliance.

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

Full original evidence and wording: [dated source](docs/archive/governance_2026-10-10/SYSTEM_ARCHITECTURE_RULES.md). Historical counts and completion claims apply only to their recorded checkpoint.

### 2026-10-15 — Explicit additive Granite theme exception

At the user’s explicit request, the existing ThemeManager and AccessibilityPreferences now register Wyrdworks Granite alongside Urban Wilderness. The earlier single-theme restriction is relaxed only for these two static accessible profiles; no new manager/service, page construction, geometry or database owner is introduced. Granite uses palette/QSS and existing local page style roots. Text/symbol status cues, locked colorblind semantics and reduced-motion behavior remain required. No new theme-image directory is introduced.

### 2026-10-15 — Granite default supersedes the additive-theme exception

The user explicitly removed Urban Wilderness as a selectable visual theme. Granite is now the sole default through the existing ThemeManager and AccessibilityPreferences; legacy keys resolve to Granite without requiring a manual settings change. Existing Urban Wilderness-named asset paths and compatibility constants remain resource/backward-compatibility identifiers, not active appearance options. One small static neutral stone tile and a transparent 37-badge atlas live in the existing approved asset subtree. Granite normalizes legacy teal QSS, owns reversible rounded card masks, and reuses the existing lazy SpriteSheet cache. No timer, new service, startup page construction, database write or outer-window geometry responsibility is added.

### 2026-10-15 — Granite assets use their dedicated theme folder

At the user's explicit request, the Granite stone texture and collectible atlas now live at `assets/themes/granite` and `assets/themes/granite/collectibles`; Granite loaders and the curated release manifest reference those paths directly. This supersedes the preceding note about keeping Granite images in the Urban Wilderness subtree. Urban Wilderness remains excluded as a selectable appearance, and its unrelated assets and compatibility identifiers are unchanged.


### Raid Plan inline map consumer

The user-authorized inline editing rail mounts only in Raid Plan's map box. InlineRaidMap delegates board construction/context/save/projection to existing Phase15RaidMapWorkspace, EncounterBoard and EncounterRaidMapStore owners; it does not introduce a second map repository, assignment owner or mechanics engine. EncounterBoardStatePayload additively accepts vector annotations with normalized-scene coordinates, finite geometry, stable annotation ids and designed-route provenance; existing version-1/2 layouts remain loadable. Board token/zone metadata gains compatible defaulted identity/lock/visibility/phase fields. Calibration remains in the existing map-reference owner; map-relative units never imply meters. Collapse/layer visibility are presentation state and no heatmap computation or live targeting is performed. Source images remain unchanged. Deferred fitting/checkpoint callbacks are bound to Qt object lifetimes. Empty new plan-scoped layouts are legal; raster markings are not reverse-engineered into player positions.

### 2026-10-16 — Compact Raid Plan stage dialogs and authored route notes
The Fight consumer groups existing encounter records into downtime and other mechanics for presentation, with missing thresholds explicit; it does not write inferred mechanics facts. StageAssignmentsDialog delegates persistence to Phase15AssignmentStateService, preserving the full original snapshot and using its optional expected-snapshot transaction guard. RouteNotesDialog delegates to the existing inline board and stage map save owner. Compatible optional map fields route_note and route_annotation_id remain stage-layout metadata, not a second notes database. Hidden unused assignment rows stay in the existing state. Existing Assignments/Coverage pages and data remain intact. Default inline map cover fitting changes only the view transform, not artwork or stored coordinates.

### 2026-10-17 — User-directed dark fantasy replacement
On codex/dark-fantasy-ui, the supplied graphite/silver/ivory/amethyst references supersede the previous Granite visual experiments. Existing theme IDs remain compatibility keys in the single ThemeManager. Artwork lives in the existing granite resource subtree; semantic icon lookup remains in phase15_sprite_assets. Experimental material frames are disabled. No new persistence, page lifecycle or service owner is introduced.

The detailed reference implementation remains in ui/granite_theme.py. Local control projection prevents page QSS from overriding the single skin. Modal backdrop capture is static, parent-owned, bounded to 1100px width, and released on hide/close/theme teardown; no graphics effect is installed on the live workspace. The shell footer reads existing context and changes only existing map view transforms. Texture swatches live in assets/themes/granite/dark_fantasy_surfaces and are bundled through the current release manifest. No page factory, storage owner or mechanics calculation changes.

2026-10-17 user direction supersedes bitmap surface swatches: image-based stone UI backgrounds are disabled throughout the active theme and excluded from its curated release resources. Shared palette, code-drawn gradients/shadows, artwork, icon and map owners remain. Legacy local stone URLs are stripped by the existing projection; uploaded theme copies receive the same scoped removal without adopting their unrelated edits.

2026-10-17 compact-map refinement: the shell reparents its existing Raid Plan ribbon above the scroll and exposes no footer map zoom control. Existing mouse transforms remain. Quick notes are existing text annotations in the validated board payload, saved through Phase15RaidMapWorkspace's current layout/image/link owner after captured plan/stage revalidation; failed saves retain the note draft. Advanced toolbar presentation reuses original actions and preserves lazy editor creation. No alternate note store, engine, context controller, page factory or eager Live Raid construction.

2026-10-17 contextual-panel refinement supersedes the ribbon reparenting above: the ribbon remains in Raid Plan's center Fight column above the map. Roster constructs no stage bar. The four Fight views share the selected plan/stage; Assignments and Route Notes are lazy read-only projections of existing owners. The 2026-10-19 cleanup supersedes the fixed-height information scroll exception: the selected pane uses native height-for-width with a content-derived height, no nested primary scroll, and no hidden-page size reservation. The map canvas keeps its independent square constraint. Compact mechanic cards contain name and description; recorded thresholds and assignments retain their canonical owners and existing views. ContextualBuildEditor hosts the existing Builds page; its local presentation selector snapshots the shared stage identities but never persists or broadcasts changes to the shared raid selection. The existing build variant resolver and save owners retain all equipment, inheritance and persistence responsibilities. No mechanic-phase gear contexts or new serialized boundary/store are introduced.

Granite scrollbar metrics now belong to ui/theme/scrollbars.py: 9px in both directions, graphite track/handle, rounded handle, champagne hover and no arrows. Both Granite entry points reuse it; local QSS normalization removes scrollbar selectors without removing unrelated selectors in the same rule.

The explicitly requested header-logo drop shadow is a bounded, static effect on the logo label only, configured by the existing Granite theme. The workspace, map and header container have no graphics effect; their geometry and paint ownership remain unchanged.

The user's later stone-tablet preview explicitly permits the supplied stone_tablet.png on large outer panels only, superseding the earlier blanket image-surface removal for that limited scope. The existing Granite owner projects a paint-only, mouse-transparent child surface on outer panel frames at least 250x220 logical pixels in active workflow roots. The image decodes once; fixed 18px corners/edges and one aspect-preserving center crop avoid tiling. Existing layout border width and content margins stay intact, and the overlay takes no layout or input ownership. Nested cards, inputs, buttons, map scenes, sidebar and Collectibles room artwork remain unchanged. The original transparent PNG is preserved as nine-slice UI artwork; rounded 18px clipping is a runtime treatment. The preview is a source-level flag in the presentation component, not a selectable second theme, stored preference, new service or persisted data.

The later map-menu refinement parents the compact tools to the active map viewport and masks the container to its five button bounds, avoiding reserved side-strip space and allowing map input through the gaps. The existing board, scene, normalized coordinates and save owner remain authoritative. Object properties use the existing inspector through More. The existing square-canvas cap increases to 760px to use available center-column width; no top-level window resizing is introduced. The spearhead is a supplied transparent icon, trimmed only in the cached display projection, not rewritten as an asset. Timeline bands/cards remain read-only projections of recorded thresholds, with the latest requested 0%-to-100% orientation.


### Granite / fantasy blend preview (2026-10-18)
The current blend uses Granite charcoal palette and raised grey inner surfaces with the supplied `assets/themes/granite/panel_bg.png` on large outer workflow panels. Dark-fantasy navigation, champagne icons, branding, splash, Windows icon, footer, modals and contextual Fight/map behavior remain. The boss ribbon now spans above all three Team/Fight/Readiness columns on its own matching backing, superseding the center-only placement above. Granite segment painting retains the portrait on the left and names over the dark right half. Stage identity/order/selection remain owned by the existing Raid Plan; backing and painting own no saved data. The short ribbon backing explicitly qualifies for the same cached paint-only surface; nested cards remain raised grey.


### Raid Plan stone layers (2026-10-18)
The stone slab preview is now restricted to Raid Plan, superseding its earlier use on other workflows. Roster, Builds, Assignments, Strategy and Map Workshop retain smooth code-painted surfaces. Raid Plan retains `panel_bg.png` on its three large columns. Its map uses `granite_top_panel_smooth.png` behind the map with a 2px visible rim, fixed vertical sizing and no surplus vertical padding. Only the full-width boss ribbon backing uses `granite_top_panel_rough.png`; rough texture is not spread across inner cards. Raid Plan action buttons use `granite_button_grey.png`, with muted-purple checked states, pressed/focus/disabled treatments and unchanged border metrics. Titles use champagne serif lettering with a restrained shadow, ivory for the readiness summary title, and champagne atlas icons on the contextual map tabs. Original PNGs remain unchanged, decoded/cropped at runtime or sliced by native Qt; no additional theme, preference, data or save owner is introduced.


### Smooth ribbon bevel and standalone-button preview (2026-10-18)
Raid Plan's full-width boss ribbon now uses the smooth panel material with an 8px rounded bevel and neutral cool shadow instead of rough stone. The stage cards have rounded artwork clipping, cool dark label backing, restrained raised edges and 6px separation; existing plan stage order, identity, selection and horizontal reveal remain authoritative. The supplied wide/square nine-slice button images preview only on ungrouped Raid Plan controls, including its separately hosted header. Icon-only controls use square artwork and text controls use wide artwork. Grouped tabs/filters, phase buttons and map tools retain prior styling, and other pages are excluded. Native QSS uses fixed 5px borders and authored transparent corners (no additional radius clipping), with cached prebuilt hover/pressed/selected/disabled variants. Original PNGs are preserved; compact transparent UI derivatives and crop/source hashes are recorded in the asset receipt. No new theme selector or persisted setting is added.


### App-wide stone-derived palette (2026-10-18)
The user's new palette now replaces the earlier neutral/cool palette throughout the existing Granite theme: background #101112, panel #1C1D1F, card #242527, button #303134, hover #3B3D40, selected #44474B, divider #484B50, control border #85898E, selection outline #C8CDD2, text #F0EDE6, secondary text #B9B8B3, gold heading #D8C39F. Status colors are covered #9FC4DD, review #E2BE77, unknown #B9B8B3 and blocked/conflict #E6A477. Existing readiness key Planned remains Planned; color changes do not equate it with observed blockage or alter saved statuses. Shared palette/QSS normalization, native roster/ribbon painters and readiness badges use the same tokens. Role identity colors, supplied stone/icon artwork, scoped Raid Plan button geometry and existing status symbols remain. The button preview stays Raid-Plan-only; only its selected derivative tint changes from purple to neutral grey. No theme selector, new state owner, migration or data interpretation is introduced.


### Raid Plan endgame defaults (2026-10-19)
RaidPlanRepository remains the sole endgame-default write owner. The existing
RaidPlan payload adds an optional strict gold_gear_override; absence inherits
the global Hardmode default. Member payloads retain endgame_ready_assumed and
add optional passive/CP exceptions and immutable sparse equipment metadata.
No database schema migration is required. Confirmation and individual adjustment
dialogs edit only a Raid Plan draft; normal Save/CAS/readback owns persistence.
Explicit plan False wins over the global default and legacy member flags.
Legacy member assumptions remain seat-scoped. Defaults do not equip empty slots
or choose glyph identities, skills, or slottable CP. An explicit bulk reapply may
replace equipment exceptions; Clear preserves authored equipment exceptions.
Canonical saved-build resolution owns plan equipment projection. Offensive and
Health consumers apply it after sparse encounter inheritance and use the existing
endgame-baseline service to project calculation-only progression through canonical
MinMax eligibility/CP owners. Assumption provenance travels with their results;
factual Coverage continues opting out. The explicit individual editor reads the
canonical build catalog through SQLite mode=ro and its existing validated pure
roster projection, without bootstrapping schemas or running migrations. Existing
global Settings and saved player/build records are never written by this workflow.


### Crit / Pen source calculator consumer (2026-10-20)
The existing stage offensive-stats service remains the calculation authority.
`raid_offensive_calculator` is a pure, Pydantic-validated additive scenario adapter
for that immutable result, not a second build engine or persistence owner. The
Coverage-styled `RaidCritPenDialog` is shared by Raid Plan and Builds and retains
seat and captured stage identities. Personal/group provenance and unknown values
survive projection. Discovery-only variable options require explicit manual values;
non-additive traces cannot be toggled as flat bonuses. Scenario drafts are dialog-local
and never promote into saved records. Worker operations capture the input scope;
application-owned tasks can finish safely after a dialog closes. No new database,
page factory, theme, navigation owner or top-level workspace resize is introduced.


### Map toolbar anchor correction (2026-10-20)
The compact rail is now a child of the active QGraphicsView frame, positioned
relative to its viewport origin on show/move/resize. This supersedes viewport
parenting in the earlier map-menu refinement: Qt's preview scroll path can move
viewport children with the image. The rail remains a masked overlay with the same
five controls, no reserved layout strip, no scene item or graphics transform, and
no additional timer, data owner, saved coordinates or workspace resize behavior.
Preview/editor switching reparents this same rail to the active view.

### Raid Plan module save continuity (2026-10-22)
RaidPlanRepository owns exact-scope build drafts and compound build/plan commits;
BuildCatalogService and RaidPlanContextOverrideRepository still own their respective
validated writes within that transaction. Assignment drafts remain with
Phase15AssignmentStateService, Coverage owner drafts with the existing context
Coverage repository. Additive draft tables use repeatable CREATE IF NOT EXISTS;
existing payloads remain supported. Version-1 calculator states extend RaidPlan
through its existing Pydantic boundary with an empty legacy default.

Context tokens conservatively cover the plan, its stage/assignment/coverage records
and the canonical build catalog. Changes in an unrelated stage/build can therefore
require reopening; this is intentional rejection rather than an automatic merge.
The explicit existing-build apply updates a reusable build and the exact plan seat
selection atomically; it does not fork build identity or change character progression.
Unknown imported build fields survive the complete known-field editor projection.
Calculator apply persists a planning scenario, not build-engine inputs. Legacy
TeamName/BossName build-variant resolution retains its existing semantics; exact
draft/selection IDs do not redefine that compatibility inheritance system.
No protected database replacement, new engine, eager page, polling timer or theme
owner is introduced. Game formulas and mechanics field notes are unchanged.


### Stage-authored Kill & Pull Order (2026-10-23)
Phase15AssignmentStateService remains the structured instruction owner within its existing per-plan/per-context JSON payload. Stable pull_id and contiguous ordered target rows separate pull sequence from target priority; labels can change without changing identity. The compatibility adapter assigns deterministic identities to legacy flat rows and groups their repeated labels in first-seen order without rewriting stored data. No table or schema migration is required. Exact Trash instructions do not inherit from shared Trash; other assignment inheritance is retained and guarded by an expected shared snapshot when creating an exact record. The dialog retains its full baseline and calls the existing transaction/CAS/readback save. Suggestions remain an on-demand guide-evidence projection with reconciliation; no observed logs, phase-to-pull inference or automatic approval is introduced. Live Raid Now is a saved-instruction consumer, not a mechanics authority. Marker references are opaque stage-map annotations for manual use. The existing Fight segmented tools ignore horizontal text size hints so their parent does not force horizontal overflow; one outer page scrollbar and the separate modal scrollbar remain.

Workshop movement recipes remain embedded in canonical EncounterBoard layouts. Their named places, phases and generated-object baselines are distinct from boss-package presentation state and observed replay/calibration. Copies to another encounter or artwork require location placement; regeneration may replace only its owned objects and must preserve unrelated annotations and recover editor state if checkpointing fails.
