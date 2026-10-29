# Wyrdworks — Current delivery roadmap

**Active development branch:** `wyrdworks-dev` supersedes the `phase15.5` branch for ongoing development as of 2026-10-18. Phase 15.5 remains the product/architecture milestone identifier. The approved Granite/fantasy blend is the default style; preserve its shared palette, assets and active workflow updates. The old branch remains available as history.

Product: **Wyrdworks** (formerly FoundryDock). Repository and technical identifiers retain their existing names. Product line: **phase15.5**. This roadmap organizes work; [DEVELOPMENT_STANDARD.md](DEVELOPMENT_STANDARD.md) owns completion gates and [SYSTEM_ARCHITECTURE_RULES.md](SYSTEM_ARCHITECTURE_RULES.md) owns architecture. Preserve current working behavior over stale historical plans.

## Product outcome

A trustworthy, persistent, stage-aware raid assistant that combines existing mechanics, builds, encounter requirements and observations into explainable team decisions. Improve the existing pages and canonical engines; do not create another top-level engine/page for each intelligence increment.


## Standing delivery rule — make researched encounter intelligence usable

When encounter research, real-build validation or mechanic reconciliation uncovers useful information, trace it through its canonical owner into the active raid workflows. Every researched encounter should be audited for phase-specific enemy targets, killability/vulnerability, arena/portal location, required handling, timing, evidence and unknowns. Build generic projections and show source-backed suggestions without overwriting raid-lead decisions. Do not hardcode a per-boss UI workaround where a reusable evidence contract belongs. Completion means cross-trial coverage accounting and an actual saved-plan/Windows acceptance path, not merely data present in a research file. Current concrete backlog: [Encounter intelligence reconciliation](docs/product_todo.md#encounter-intelligence-research-to-workflow-coverage).

## Current Wyrdworks delivery scope (2026-10-26)

The **only active raid-planning UI is Raid Plan**, containing **Teams, Map, and Readiness** columns. Roster, Assignments, Builds, Map Workshop, and Finch / Collaboration are supporting capabilities only where required by Raid Plan. Prioritize complete data paths through canonical owners; do not create a separate planning-page acceptance requirement. The prior compact-workspace/Main Dock migration proposal is superseded as current direction.

The following interfaces are **parked**: Lantern, Comp Brainstorm, Coverage, Rotations, standalone Readiness, Health, Comp Engine, Optimization, Extreme Build, and **Live Raid**. Parked means retained in the codebase; preserve their existing behavior, records, business logic, integrations, shared-service usefulness, and regression coverage. Do not proactively redesign, expand, benchmark, or require their page construction/navigation/save-and-reopen for unrelated acceptance. A direct user request or a critical shared regression can bring a specific parked interface into scope. Underlying authoritative data and reusable service capabilities remain available to active workflows.

Data access is data-first: load the current Raid Plan, stage, seat identities, assignments, and necessary Saved Builds before optional reference-heavy data. Keep repositories/services widget-independent and reuse canonical owners. Examine repeated queries, Pydantic validation, capability audits, and recalculations before proposing optimization. Any scoped cache must state freshness and invalidation; plan/stage/build-revision/relevant-source changes invalidate dependent evidence. Never trade strict validation, provenance, stable identity, or user data for speed, and never present stale or incomplete evidence as current.

For active workflows, acceptance covers the relevant save/reload, identity, and handoff path through canonical data owners and affected active consumers. For parked interfaces, test underlying records/shared behavior through authoritative owners and retain regression coverage; page-specific persistence certification is not a blanket gate. Full phase closeout still follows [DEVELOPMENT_STANDARD.md](DEVELOPMENT_STANDARD.md).

## Active delivery queue

| Work | Current evidence / next acceptance |
| --- | --- |
| Raid Plan continuity | Prove current-plan/stage/seat identity, required build resolution, assignments, save/reload, and downstream active handoffs. Preserve dirty drafts and stale-write rejection. |
| Raid Plan Teams and supporting editors | Preserve exact team/player/character/build/seat/stage identity through canonical repositories and verify changed writes by readback. |
| Raid Plan Map and Map Workshop | Keep authored strategy, calibration, movement evidence, and map data bound to exact plan/stage/map identities; verify save/reload and consumption in Raid Plan. Preserve coordinate alignment. |
| Live Raid | **Parked by user on 2026-10-20.** Preserve existing code/data, but exclude Live Raid handoff and page acceptance from current P0–P7 acceptance. |
| Finch / Collaboration | Advance only where applicable to the active workflow, retaining explicit ownership, consent, and external-action boundaries. |
| Shared data and performance | Measure data access used by an active action; remove repeated work at canonical owners, use only explicit freshness-aware caches, and preserve strict validation/provenance. |
| Real-data / Windows closeout | Use isolated representative saved plans/builds, scoped corpus counts, active-consumer evidence and reopen where applicable. Packaging/install claims need their own evidence. |

Select the next unfulfilled acceptance outcome from the active queue. Deliver a small complete path rather than endlessly adding audit scaffolding. Record blockers and close independent wiring/testing work. The detailed phase exit criteria remain historical engineering scope; apply them only to the user-requested current work and do not let parked-page criteria silently reopen. Do not delete historical requirements or claims.

## P0–P7 acceptance for the current one-page scope

- P0: existing local quality runner and verified clean exact-HEAD receipt; historical passes do not certify a later revision.
- P1: broad regression with explicit discovery scope and separate product, fixture, environment, and missing-evidence failures.
- P2: Raid Plan save/reopen, exact team/stage/build/assignment identity, stale-write rejection, retained drafts.
- P3: Map Workshop calibration and Lokke movement/map continuity consumed by Raid Plan; observed movement is not an authored strategy or verified image calibration.
- P4: removed from this delivery by the user; this is a personal-use application and release/installer certification is not required. Existing packaging code and safety tests remain retained.
- P5: Kill & Pull Order in Raid Plan Readiness, using canonical stage assignment persistence; no separate Live Raid acceptance.
- P6: classify architecture warnings and fix actionable current-scope defects; retain tracked migration inventories.
- P7: dependency-aware inventory ranked by size and conservative cleanup recommendations; no bulk deletion or database replacement.

Completion evidence and remaining blockers: [2026-10-26 receipt](docs/validation/raid_plan_p0_p7_20261026.md). Unverified gates remain open.

Current follow-through: [2026-10-28 acceptance](docs/validation/raid_plan_followthrough_20261028.md). Lokke visual verification and fine tuning remain with the user; engineering checks must preserve that concurrent work. P1 remains open until unresolved broad regressions are reconciled; focused passes do not erase those failures.

## Historical checkpoint boundaries

Reported local Windows results: Phase 15.5 baseline **358 passed in 98.03 seconds**; focused reliability integration **72 passed in 12.69 seconds**; the previous 11 baseline failures later passed in focused local verification; startup to visible window approximately **9.0 seconds**; Builds refresh approximately **11.4 seconds**; Collectibles initial construction approximately **28.2 seconds**. These are historical, scope-specific reports, not certification of the current branch, package, or installation. The former 15-second Coverage refresh target is no longer an active optimization target because Coverage is parked. Do not replace newer authoritative evidence with these figures.

## Engine roadmap reference

Statuses below are **reported historical engine scope**, not fresh certification or current UI priorities. A parked page does not mean its underlying engine/data is deleted or unavailable to shared owners; an engine status of active does not reopen a parked interface. Revalidate affected downstream phases when canonical inputs change. Historical green counts do not prove current code/corpus coverage.

# PHASE 15.5 PRODUCT LINE · Clean Application Integration

**Status: 🟡 Active integration track**

Phase 15.5 is the clean product line for the current Wyrdworks application. It is not a replacement for the engine roadmap below and it does not redefine engine-phase ownership. Its job is to make the existing canonical engines usable through one coherent, persistent, stage-aware application without reviving retired duplicate authorities. The active product principle is: ```text CANONICAL ENGINE TRUTH ↓ ONE SAVED RAID PLAN ↓ TEAM / STAGE / BUILD / ASSIGNMENT CONTEXT ↓ CLEAR NATIVE PHASE 15.5 SURFACES ↓ EXPLAINABLE PLANNING + EXECUTION + REVIEW ``` Curr

Detailed requirements: [source](docs/archive/governance_2026-10-10/MASTER_ROADMAP.md).

# PHASE 0 · Data Foundation

**Status: 🟢 Complete**

Canonical data and provenance foundation. Revalidate required corpus coverage before making new downstream claims.

Detailed requirements: [source](docs/archive/governance_2026-10-10/MASTER_ROADMAP.md).

# PHASE 1 · Canonical Build System

**Status: 🟢 Backend foundation / 🟡 UI & downstream adoption**

Reusable character/build identity, progression and configuration. Backend foundation exists; complete current UI and downstream adoption.

Detailed requirements: [source](docs/archive/governance_2026-10-10/MASTER_ROADMAP.md).

# PHASE 2 · Effect Architecture

**Status: 🟡 Advanced foundation**

One EffectVariant/effect-resolution authority for identity, targeting, magnitude, timing, triggers and stacking. Expand reviewed coverage through this owner.

Detailed requirements: [source](docs/archive/governance_2026-10-10/MASTER_ROADMAP.md).

# PHASE 3 · Static Combat Rules Engine

**Status: 🟢 Complete**

Explainable static combat calculation with separate component/modifier stages. Runtime assumptions must not become standing bonuses.

Detailed requirements: [source](docs/archive/governance_2026-10-10/MASTER_ROADMAP.md).

# PHASE 4 · Resource & Sustain Engine

**Status: 🟢 Complete**

Resource state, ability costs, recovery and restoration timelines with explicit sustain failures and event ordering.

Detailed requirements: [source](docs/archive/governance_2026-10-10/MASTER_ROADMAP.md).

# PHASE 5 · Real Build Resolution

**Status: 🟢 Complete**

Real saved-build resolution through canonical data and capability services. Preserve temporal, conditional and unknown evidence.

Detailed requirements: [source](docs/archive/governance_2026-10-10/MASTER_ROADMAP.md).

# PHASE 6 · Damage / Effect Components

**Status: 🟢 Complete**

Coefficient-local damage/effect components and classification, shared with runtime execution. Detailed historical coverage remains in the source report.

Detailed requirements: [source](docs/archive/governance_2026-10-10/MASTER_ROADMAP.md).

# PHASE 7 · Conditional Effects & Proc Engine

**Status: 🟢 Complete**

Conditional/proc execution over deterministic runtime state, with timing, chance, cooldown, stacking and refresh evidence.

Detailed requirements: [source](docs/archive/governance_2026-10-10/MASTER_ROADMAP.md).

# PHASE 8 · Combat State

**Status: 🟢 Complete**

One CombatState snapshot built from canonical build and runtime history. It answers what is true at the requested time.

Detailed requirements: [source](docs/archive/governance_2026-10-10/MASTER_ROADMAP.md).

# PHASE 9 · Encounter Model

**Status: 🟢 Complete**

Source-backed encounter identities, mechanics, phases, requirements and evidence. Historical corpus completion does not prove the current database contains those facts.

Detailed requirements: [source](docs/archive/governance_2026-10-10/MASTER_ROADMAP.md).

# PHASE 10 · Encounter Evaluation

**Status: 🟢 Complete**

Combine encounter, requirements, roster and builds into capability/coverage/conflict/unknown outcomes without inventing provider execution.

Detailed requirements: [source](docs/archive/governance_2026-10-10/MASTER_ROADMAP.md).

# PHASE 11 · Provider Assignment

**Status: 🟢 Complete**

Assign exact providers while preserving capability, suitability, responsibility conflicts and uncertainty. Build optimization cannot silently transfer a duty.

Detailed requirements: [source](docs/archive/governance_2026-10-10/MASTER_ROADMAP.md).

# PHASE 12 · Build Optimization

**Status: 🟢 Complete**

Bounded build optimization through existing mechanics. Hard sustain, capability and provider constraints are ranking gates; unknown consequences cannot win.

Detailed requirements: [source](docs/archive/governance_2026-10-10/MASTER_ROADMAP.md).

# PHASE 12.5 · Team Workflow Integration

**Status: 🟡 Active**

Phase 12.5 is the product-integration bridge between the completed bounded build optimizer and the later temporal engines. It does **not** expand Phase 12's mathematical search scope and it does **not** substitute UI plumbing for Phase 13 Rotation Engine work. The authoritative user workflow is: ```text COMP MAKER ↓ NAMED TEAM + EXACT CHAIR / BUILD ASSIGNMENTS ↓ ROSTER ↓ LOAD TEAM IN OPTIMIZATION ↓ AUDIT / IMPROVE / COMPARE ↓ ROSTER ``` Active scope, in order: 1. **Canonical team identity** - a named team created in Comp Maker, displayed in Roster, and l

Detailed requirements: [source](docs/archive/governance_2026-10-10/MASTER_ROADMAP.md).

# PHASE 13 · Rotation Engine

**Status: 🟡 Active engine work**

Rotation planning and execution over canonical actions, timing, resources, duties and runtime state. Preserve exact build/context and explicit unsupported branches.

Detailed requirements: [source](docs/archive/governance_2026-10-10/MASTER_ROADMAP.md).

# PHASE 14 · Combat Simulation

**Status: 🟠 Active / validation-hardening**

Combat simulation with damage, targets, health, sustain, effects, fight termination and evidence. Real-build full DPS requires its own complete execution witness.

Detailed requirements: [source](docs/archive/governance_2026-10-10/MASTER_ROADMAP.md).

# PHASE 15 · Encounter-Aware Optimization

**Status: 🟠 Active / first vertical slice**

Encounter-aware optimization comparing whole candidates and team tradeoffs through guarded review, explicit approval and verified durable adoption. Current vertical slices do not establish a full raid optimizer.

Detailed requirements: [source](docs/archive/governance_2026-10-10/MASTER_ROADMAP.md).

# PHASE 16 · Explanation Engine

**Status: 🔴 Planned**

Explain recommendations with change, impact, reason, tradeoff, encounter effect, confidence and evidence. Never invent an explanation for unsupported outcomes.

Detailed requirements: [source](docs/archive/governance_2026-10-10/MASTER_ROADMAP.md).

# PHASE 17 · ESO Logs Validation

**Status: 🔴 Planned**

Compare modeled and observed ESO Logs outcomes with scoped provenance and discrepancy diagnosis. Observations validate models; they do not silently replace formulas.

Detailed requirements: [source](docs/archive/governance_2026-10-10/MASTER_ROADMAP.md).

# PHASE 18 · Strategy Engine

**Status: 🔴 Planned**

Compare safe, balanced, aggressive and experimental strategies with practical risk, execution and expected-outcome evidence.

**User-requested follow-up (2026-10-25): assignable role movement guides.**
Simplify reviewed movement into instructive, stage-aware DD, tank and healer
routes using the existing movement-route and Map Workshop owners. Use one DD
symbol where members genuinely share a route, and split symbols when mechanics
or duties diverge. Preserve separate tank/healer duties, timing, safe pauses,
teleports and floor changes; never average incompatible paths or bridge gaps.
Allow explicit assignment to exact team seats/people and normal route editing,
save and reopen. Keep original observations and provenance separate from the
authored teaching copy. First increment (2026-10-26): Workshop phase-filtered, source-bound teaching copies and independent Lokkestiiz cage rotation slots are implemented. Second increment: strict small-waypoint authored plans, user-corrected Lokke flow, saved path contrast and independently assignable house/cage diagram slots. Remaining: reviewed cage occurrence/release detection, eligibility checks, complete authored instructional animation and actual Raid Plan person-assignment handoff.

Detailed requirements: [source](docs/archive/governance_2026-10-10/MASTER_ROADMAP.md).

# PHASE 19 · Full Raid Optimizer

**Status: 🔴 Planned**

End-to-end optimization of an actual twelve-player roster against a reviewed encounter, with explicit assignments, candidates, simulation, strategy and explanation.

Detailed requirements: [source](docs/archive/governance_2026-10-10/MASTER_ROADMAP.md).

Full original evidence and wording: [dated source](docs/archive/governance_2026-10-10/MASTER_ROADMAP.md). Historical counts and completion claims apply only to their recorded checkpoint.

## Concurrent branch evidence retained

Newer shared-branch records were preserved during integration: [checkpoint f08ff6f15](docs/archive/governance_2026-10-10/concurrent_f08ff6f15/MASTER_ROADMAP.md). This evidence includes cached Coverage/Comp handoffs and plan/stage invalidation checks; its original confidence and CI status remain scoped to that checkpoint.
