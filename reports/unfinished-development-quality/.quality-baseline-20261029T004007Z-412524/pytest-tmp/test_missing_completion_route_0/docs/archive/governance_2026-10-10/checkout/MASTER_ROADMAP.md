# 🖤 Black Feather Foundry
## Updated Development Roadmap

## Roadmap authority / anti-regression rule

This roadmap is interpreted against the **current Phase 15.5 implementation and current architecture rules**, not as permission to restore older code paths.

- Current/new roadmap requirements and validated Phase 15.5 behavior are authoritative over superseded roadmap assumptions.
- Work performed from an older roadmap is reconciliation/additive work only. It may contribute missing engine intelligence, tests, evidence, or still-valid capability, but it must not roll the product back to older routing, persistence, service ownership, UI composition, or duplicate truth.
- Before shared architecture is changed, inspect the current branch implementation, `CLAUDE.md`, and `SYSTEM_ARCHITECTURE_RULES.md`.
- If an older roadmap item conflicts with newer working behavior, preserve the newer implementation and reinterpret/update the older item around the current contract.
- Passing Git merge mechanics do not prove semantic compatibility. A clean merge that restores a retired authority is still a regression.
- Never use broad checkout/revert/reset operations to make the old roadmap "match" the branch. Port narrowly, preserve concurrent work, and update stale tests rather than reviving retired behavior.

## North Star

BFF becomes a trustworthy, database-backed ESO combat, effects, encounter, and optimization engine that can explain not only **what** is optimal, but **why**.

```text
REAL ESO DATA
      ↓
CANONICAL BUILD
      ↓
RULES / EFFECT ENGINE
      ↓
STATIC COMBAT MATH
      ↓
COMBAT STATE
      ↓
ENCOUNTER ENGINE
      ↓
ROSTER / COVERAGE
      ↓
PROVIDER ASSIGNMENT
      ↓
BUILD OPTIMIZATION
      ↓
ENCOUNTER OPTIMIZATION
      ↓
EXPLANATION
      ↓
LOG VALIDATION
```

---

# Roadmap Completion Standard

This section is authoritative for **every phase**, including phases previously marked complete.

A phase is not complete merely because its architecture exists, representative tests pass, or one happy-path example works. Phase completion means the phase's stated scope is demonstrably usable against the real data and downstream path it claims to support.

## Mandatory closeout gates

Every phase marked **🟢 Complete** must satisfy all applicable gates below.

1. **Architecture gate**
   - one authoritative implementation path exists;
   - no competing legacy implementation silently remains authoritative;
   - ownership and boundaries with adjacent phases are explicit.

2. **Data / corpus gate**
   - the required real-data corpus for the phase has a declared scope and denominator;
   - parse/import failures, missing rows, unresolved rows, conflicts, and intentionally unsupported cases are counted;
   - low coverage may be accepted only when the phase scope explicitly says coverage enrichment is deferred and downstream correctness does not depend on the missing data;
   - absence of evidence is never treated as evidence of absence.

3. **Persistence gate**
   - if the phase creates canonical or durable data, a dry run must validate the exact write set first;
   - writes must preserve provenance and review state;
   - rejected, conflicting, unresolved, or unsupported rows must not leak into canonical truth;
   - write paths must be idempotent or have another explicit duplicate-prevention guarantee;
   - a post-write audit must verify the persisted rows, not merely trust the writer's success message.

4. **Real integration gate**
   - at least one representative real saved build, roster, encounter, or other real production path must traverse the phase end-to-end;
   - synthetic fixtures are necessary but are not sufficient by themselves.

5. **Regression gate**
   - focused tests for the phase must be green;
   - a full regression checkpoint must be recorded when the phase changes shared engine behavior or when its closeout depends on broad compatibility;
   - tests are only claimed green from actual reported output.

6. **Unresolved-boundary gate**
   - remaining unknowns must be explicit, countable, and assigned to a later phase or supported limitation;
   - a deferral may not contradict the phase's own promised outcome;
   - `UNKNOWN`, unsupported, and conflicting states may not be silently converted to zero, false, unavailable, or safe.

7. **Downstream dependency gate**
   - when later work materially changes canonical inputs owned by an earlier phase, dependent completed phases receive a retrospective impact review;
   - dependent phases do not automatically reopen, but representative integration must be rerun when the changed upstream data could alter their conclusions.

## Corpus-bearing phase rule

Phases that claim to model a real corpus, including encounter data, effect data, or optimization candidates, must distinguish these four states:

```text
SOURCE EXISTS
    ↓
PARSED / PROJECTED
    ↓
REVIEWED / RESOLVED
    ↓
CANONICALLY PERSISTED + AUDITED
```

Completing the first or second step does **not** imply the third or fourth.

## Status meanings

- **🟢 Complete**: all applicable completion gates are satisfied.
- **🟢 Engine complete / 🟡 retrospective validation**: the implementation is complete, but later upstream hardening requires a recorded revalidation.
- **🟡 Active**: work required for the phase's exit criteria remains.
- **🔴 Planned**: not yet active.

If a later audit discovers that a required closeout gate was never satisfied, the roadmap must say so. Historical completion dates remain useful history, but they do not overrule current evidence.

---

# PHASE 15.5 PRODUCT LINE · Clean Application Integration
**Status: 🟡 Active integration track**

Phase 15.5 is the clean product line for the current FoundryDock application. It is not a replacement for the engine roadmap below and it does not redefine engine-phase ownership. Its job is to make the existing canonical engines usable through one coherent, persistent, stage-aware application without reviving retired duplicate authorities.

The active product principle is:

```text
CANONICAL ENGINE TRUTH
        ↓
ONE SAVED RAID PLAN
        ↓
TEAM / STAGE / BUILD / ASSIGNMENT CONTEXT
        ↓
CLEAR NATIVE PHASE 15.5 SURFACES
        ↓
EXPLAINABLE PLANNING + EXECUTION + REVIEW
```

Current proven state:

- Phase 15.5 is the active clean product line; older Phase 15 / City / dashboard presentation paths are compatibility history, not the intended runtime authority.
- Native Phase 15.5 navigation, Roster, Raid Plan, Assignments, Comp, Builds, Coverage, Readiness, Rotations, Strategy/Raid Map, Live Raid, and related research surfaces own the routed application experience.
- duplicate legacy presentation authorities have been aggressively retired only after native replacement, persistence, downstream-consumer, and recovery checks;
- user-owned databases remain protected: schema evolution is additive and migrations/upgrades are preferred over reset or replacement;
- current Raid Plan / Stage context must remain explicit across every page that consumes encounter-specific state;
- canonical Character → Build → Team identity remains a cross-page requirement, not a page-local convenience;
- Extreme, Rotation, Comp Maker, Team Optimization, Coverage, Readiness, Raid Health, Raid Review, and Live Raid must reuse shared mechanic/evidence services rather than hard-code isolated conclusions;
- validated intelligence discovered while building Extreme and later combat/encounter engines should be surfaced wherever it improves decisions, while preserving provenance, confidence, UNKNOWN, unsupported, and conflicting evidence;
- UI work remains colorblind red/green accessible, seizure safe, and responsive enough to feel immediate rather than layered with avoidable blocking work.

### Phase 15.5 hardening status

Completed and retained as proven implementation history:

- clean-shell / duplicate-authority peel substantially completed;
- native navigation authority established;
- persistence and protected-database guards added around risky validation paths;
- Raid Health runtime redesign and observed-review contracts restored and focused regressions passed;
- Map Workshop / Library hardening completed on **2026-10-06** with reusable editable maps, thumbnail library, tags, portable validated `.fdmap` packages, explicit Workshop-vs-Strategy ownership, and guarded Windows checkpoint;
- authoritative A6 Windows checkpoint: **64 passed, 1 intentional ZIP-tamper warning**, with identical before/after hashes for `data/eso.db` and `user_data/foundrydock.db`.

Active integration priorities, subordinate to the engine roadmap rather than replacing it:

1. finish canonical Character → Build adoption through the full team workflow;
2. keep Raid Plan / Stage context consistent across planning, readiness, strategy, rotations, and live execution; new Comp drafts now begin stage-neutral and author only real Raid Stage keys while legacy fixed context keys remain readable;
3. close obvious Coverage/provider-source provenance gaps;
4. finish Readiness and Raid Health as trustworthy projections of canonical state;
5. wire encounter intelligence and exact saved builds into Rotation, Comp Maker, Optimization, and Live Raid without duplicate truth;
6. complete FD.my consumption of the modern saved-plan schema;
7. keep the application snappy by moving expensive analysis off avoidable UI-blocking paths while preserving deterministic results and visible save state.

### Team cross-reactivity and composition refinement — added 2026-10-09

**Status: Active — Milestone 1 shared evidence and the first native Milestone 2 Coverage inspector are implemented; broader interaction families and later milestones remain pending.** This is an additive Phase 15.5 intelligence integration track over the existing engine roadmap. Refine Coverage, Comp Engine, Optimization, Rotations and Readiness; do not create another encounter engine, optimizer or top-level page initially.

**Raid-lead outcome:** explain which combinations make the selected team stronger for the current encounter/stage, how to exploit them, which links are missing, who benefits, what a change sacrifices and what evidence remains unresolved. Highlight positive combinations as well as deficiencies, and refine advice as the Raid Plan progresses.

**Detailed implementation plan:** [Team cross-reactivity implementation plan](docs/phase155_team_cross_reactivity_plan.md). This contains exact service/function touchpoints, typed contracts, dependency order, behavioral tests, performance safeguards and a 12-seat Dreadsail Reef HM witness.

**Full scope:** all legal PvE armor-set families, monster sets, mythics, arena weapons, race/racial passives, class and configured subclass choices, combat/class/weapon/armor/guild/Alliance War/world skills and exact morphs, Ultimates, eligible passives, weapon topology, armor weights, traits, enchantments, poisons, attributes, CP, Scribing, Mundus, food/drink, potions and applicable transformations. Distinguish currently available ingredients from acquisition/build-swap/character-change opportunities and inaccessible choices. Preserve player locks and role/duty constraints; popularity does not establish mechanical value.

**Milestone 1 checkpoint:** strict shared contracts and FoundryIntelligenceService.team_interactions now project reviewed Major/Minor compatibility, source-preserving duplicate evidence, routine support families, Orb synergy capability and applicable canonical status consequences. This is bounded evidence integration, not complete ingredient discovery or new page behavior. See [validation and limitations](docs/phase155_team_cross_reactivity_m1_validation.md).

**Native Coverage checkpoint:** the effect list now links to a Connections & timing inspector, with visible connection nodes and three delivery cards; existing provider overrides and Known Sources remain in a selectable drawer. Explicit background review exposes exact sources, compatible effects, prerequisites and per-source delivery values; stale completions are rejected. Canonical status-duration extension is kept separate from buffs/debuffs. Unknown group reach, radius origin and measured execution remain explicit. Full coordinated refinement and comprehensive interaction discovery are not complete. See [validation and limits](docs/phase155_coverage_connections_validation.md).

**Core interaction families:**

- named buff/debuff stacking, equivalent sources, recipient-specific duplication and useful backups;
- status-effect interactions, application opportunities, prerequisites and caster-versus-target consequences;
- damage-type overlap and component-specific amplification, without applying a narrow benefit to all team damage;
- player-activated **Synergy Mechanics as group cross-reactivity**, with supplier, eligible activator, recipients, consumption/cooldown evidence and activation-dependent benefits;
- duration extension, sustain, healing/overhealing, defense, control, Ultimate/action competition and provider displacement;
- coordinated two/three-player combinations that may be valuable only as a complete package.

**Ordered milestones:**

| Milestone | Concrete outcome | Dependencies / acceptance |
| --- | --- | --- |
| 1. Shared interaction evidence | Inventory reviewed relationships and expose strict typed evidence through existing canonical owners. | Reuse named-effect resolution, marginal value, build capability, effect variants and status consequences. Preserve provenance, unknowns and missing rule coverage; no self-proving prerequisite cycles. |
| 2. Coverage positive-combination presentation | Add an expandable **Team interactions** view: Works together, Opportunity, Conflict and Evidence needed. | Depends on 1. Keep the existing effect list and normal-proc/manual planning correction; each interaction names beneficiaries, required use, limits, sacrifices and next action. |
| 3. Encounter group availability and Readiness | Reevaluate relationships when providers/recipients split or leave for duties; report necessary broken connections. | Depends on 1–2. Use authoritative stage, exact Builds and explicit group/window evidence. Optional opportunities never become readiness blockers. |
| 4. Comp Engine packages and Optimization refinements | Offer conventional/off-meta build options and bounded coordinated alternatives, then targeted changes to the selected plan. | Depends on 1–3. Preserve lost coverage, assignments, tradeoffs and confidence through existing comparison/proposal handoffs; blocked candidates stay visible but cannot win/adopt unsafely. |
| 5. Rotation guidance and progressive refinement | Explain source-backed use/order/workload and refresh relevant suggestions after meaningful plan changes. | Depends on 1–4. Separate scheduled/model feasibility from observed execution; reject stale results/proposals; support honest manual validation when team logs are absent. |

**Evidence contract:** strict frozen Pydantic interaction/finding/opportunity records retain canonical semantic keys, exact source Build/seat/bar identity, prerequisites, recipients/targets, stage/group/window, expected benefit, sacrificed effects/output, provenance, confidence and unresolved facts. Keep planning, mechanical support, handling, availability and execution as separate axes. Do not collapse team power into one synthetic score; numerical gains require supported canonical evaluation.

**DSR HM acceptance:** validate Twins elemental groups, carrier/interrupt conflicts and provider availability; isolate Reef pair entry, returning player, solo second-Heart continuation and configurable three-person Heart strategies; compare Taleria two/three DD bridge teams and upstairs support displacement. Never infer solo Heart capability from pair evidence, recommend solo Taleria bridges against the raid lead's exclusion, or invent timings/DPS/survival thresholds.

**Safety/performance gates:** reuse service-catalog owners, preserve concurrent native-page improvements and stable workspace geometry; use accessible text/symbols without flashing. No new schema for initial read-only milestones; later persistence, if necessary, is additive through canonical user-data owners. Analysis performs no writes. Use isolated database copies for dependent tests. Keep full scans/network/deep package searches off navigation and saving; deeper analysis is bounded, explicit and cancellable, with complete fingerprint invalidation and measured cold/warm 12-seat performance.

**Regression gates:** exact stage/build identities; stacking and useful redundancy; trait/CP/enchant applicability; damage-component eligibility; status opportunity versus application; synergy supplier/activator and reviewed cooldown/consumption conflicts; missing effect-extension prerequisites; group displacement; coordinated-package sacrifices and hard duties; stale evidence/adoption rejection; optional-versus-required findings; no writes and stable accessible UI. Run focused and related provider/Readiness/Rotation/Comp/UI tests plus the Phase 15.5 dependency audit at each relevant milestone. Update FEATURES.md only when behavior ships, and maintain the existing mechanics/source/integration records with honest evidence status.

**Important:** the former A1–A7 cleanup checklist is implementation history, not the master sequencing authority. The engine phases below remain the development spine. Phase 15.5 work should unblock and expose those engines, not distract from them.

---

# PHASE 0 · Data Foundation
**Status: 🟢 Complete**

Database-backed ESO information exists for skills, morphs, skill ranks, coefficients, gear, set effects, encounter imports, UESP encounter data, repositories, and data services.

**Hardened exit criteria:** BFF has reliable database-backed sources for required ESO information, provenance is retained, canonical and raw/source data remain distinguishable, and missing or unsupported source coverage is explicit.

---

# PHASE 1 · Canonical Build System
**Status: 🟢 Backend foundation / 🟡 UI & downstream adoption**

A Build is the reusable canonical representation of one character configuration.

```text
Character
 ├── Identity
 ├── Character-owned progression
 │    ├── Owned skill lines
 │    └── Passive ranks
 └── Build(s)
      ├── Race / Class
      ├── Gear / Traits / Enchants
      ├── Skills / Morphs / Ultimates
      ├── CP
      ├── Mundus / Food / Potions
      └── Configuration
```

Completed canonical persistence foundation includes stable character/build identity, many builds per character, character-scoped progression, stable build IDs, passive-rank persistence, and canonical progression surviving legacy sync.

Remaining adoption work:

- expose all character-owned progression in the Builds/character UI;
- make passive ranks and owned skill lines editable without direct JSON work;
- make saved Character → Build selection authoritative across downstream pages;
- migrate remaining page-specific identity/build reconstruction onto the canonical catalog.

**Exit criteria:** a real character can have reusable database-backed builds and character-owned progression that downstream systems consume directly, without page-specific reconstruction becoming a competing identity model.

---

# PHASE 2 · Effect Architecture
**Status: 🟡 Advanced foundation**

The existing `EffectVariant` / effect-resolution architecture remains authoritative for effect identity, category, magnitude, duration, chance, cooldown, trigger, target, conditions, and stacking.

```text
ESO Database
     ↓
Skill / Morph / Gear / Consumable
     ↓
EffectVariant
     ↓
Effect Repository
     ↓
Build Effect Resolver
     ↓
Normalized Effects
```

**Rule:** do not create a second competing hard-coded effect dictionary.

A selected potion represents available capability, not standing uptime. Temporal activation is projected explicitly later.

**Exit criteria:** a real build exposes the effects it actually provides, unsupported or conditional behavior remains explicit, and downstream consumers use this architecture rather than parallel effect truth.

---

# PHASE 3 · Static Combat Rules Engine
**Status: 🟢 Complete**

Phase 3 established one explainable static combat calculation with separate modifier stages rather than one giant multiplier bucket.

Authoritative damage path:

```text
Database coefficient
      ↓
Raw component value
      ↓
Attacker Damage Done
      ↓
Critical eligibility / expected crit
      ↓
Target Critical Resistance
      ↓
Resistance / penetration mitigation
      ↓
Target Damage Taken
      ↓
Final damage
```

Closeout evidence:

- real `eso.db` classified component traversed the full static pipeline;
- type-8 coefficient formula unified as `A * MaxStat + B * Power + C`;
- modifier stages remain separate and explainable;
- unresolved evidence remains explicit;
- full suite at historical closeout: **1305 passed**;
- exit criteria met on **2026-08-31**.

Supported limitation: unresolved/ambiguous component semantics remain explicit rather than guessed and are not silently routed as zero-value mechanics.

---

# PHASE 4 · Resource & Sustain Engine
**Status: 🟢 Complete**

Phase 4 models resource state, verified ability costs, ordinary recovery timing, temporary recovery modifiers, explicit restoration events, deterministic resource timelines, and sustain failure/margin interpretation.

Closeout evidence:

- real **Magrat → DF Healer** saved build traversed the complete resource path;
- deterministic same-timestamp ordering is cost → recovery tick → restoration event;
- failure, shortfall, minimum-resource, ending-margin, cost, and wasted-restore diagnostics are explicit;
- unresolved mechanics remain explicit;
- full regression suite at historical closeout: **1,444 passed**;
- exit criteria met on **2026-08-31**.

Deferred runtime trigger scheduling remains owned by later temporal phases rather than being guessed in sustain math.

---

# PHASE 5 · Real Build Resolution
**Status: 🟢 Complete**

Phase 5 proves the actual ESO database → canonical character/build → resolver → `EffectVariant` / capability path across authoritative saved builds while keeping temporal and conditional mechanics explicit.

Historical closeout evidence:

- authoritative saved build **Magrat → DF Healer** resolved through production paths;
- Spaulder of Ruin, Serpent's Disdain, Master Architect, Combat Prayer, Expansive Frost Cloak, Overflowing Altar, Aggressive Horn, and selected potion capability resolved through the effect architecture;
- authoritative roster closeout reported **0 genuine unresolved** capability gaps;
- full regression suite: **1,619 passed** on **2026-09-01**;
- detailed closeout: `docs/phase5_real_build_resolution_closeout.md`.

**Exit criteria met on 2026-09-01.**

---

# PHASE 6 · Damage / Effect Components
**Status: 🟢 Complete**

Phase 6 makes coefficient-local ability semantics explicit without turning runtime combat state into static facts. It bridges per-component identity into the existing effect architecture and records static relationships that Phase 7 can execute over time.

Historical closeout evidence on **2026-09-02**:

- residual audit rows: **403**;
- needs Phase 6 review: **0**;
- parser-coverage rows: **0**;
- source-evidence blocked: **4**;
- unsupported source alignment: **4**;
- unresolved source blocks: **0**;
- classification cleanup: **356**;
- ownership negatives: **8**;
- Phase 7 boundaries: **35**;
- targeted final regression checkpoint: **14 passed**;
- **RESULT: PASS**.

Four Engulfing Dragonfire coefficient-3 rows remain explicit unsupported source-alignment cases rather than invented semantics.

**Exit criteria met on 2026-09-02.**

---

# PHASE 7 · Conditional Effects & Proc Engine
**Status: 🟢 Complete**

Phase 7 executes the static component/effect relationships established in Phase 6 over deterministic runtime state while preserving `EffectVariant` as authoritative.

Historical closeout evidence:

- deterministic runtime event contract;
- canonical timing/state binding;
- explicit proc chance without hidden RNG;
- global/per-target cooldowns;
- active windows, stacking, refresh, status state, triggered restoration/healing, and target caps;
- closeout boundary rows: **24**;
- trigger-resolution gaps: **0**;
- timing unresolved: **0**;
- targeted checkpoint: **105 passed in 48.20s**;
- `python tools\check_phase7_closeout.py`: **RESULT: PASS**;
- detailed closeout: `docs/phase7_conditional_runtime_closeout.md`.

**Exit criteria met on 2026-09-02.**

---

# PHASE 8 · Combat State
**Status: 🟢 Complete**

Phase 8 answers: **what is true right now?** It projects canonical build state plus runtime history into an auditable `CombatState` snapshot without becoming the rotation or simulation engine.

```text
Canonical Build + Static Character State
                 ↓
       Runtime Event History
                 ↓
    Phase 7 Effect Runtime State
                 ↓
      CombatState Snapshot at t
                 ↓
Static Combat / Sustain / Encounter Consumers
```

**Exit criteria met on 2026-09-02.** Detailed closeout: `docs/phase8_combat_state_closeout.md`.

---

# PHASE 9 · Encounter Model
**Status: 🟢 Complete**

Phase 9 owns the deterministic, source-backed encounter model for boss identity, structural encounter data, mechanics, phases, requirements, positioning demands, timers, transitions, target-count constraints, add groups, damage windows, canonical facts, evidence, and unresolved/conflicting state.

## Historical Phase 9 closeout

The original closeout on **2026-09-02** proved the encounter architecture and projection/evidence boundaries:

- focused Phase 9 regression checkpoint: **23 passed in 3.94s**;
- encounter corpus audited: **490 encounters**;
- mechanics represented at that time: **35 encounters**;
- phases represented: **2 encounters**;
- requirements represented: **21 encounters**;
- positioning constraints represented: **12 encounters**;
- temporal evidence represented: **4 encounters**;
- transition evidence represented: **6 encounters**;
- target constraints represented: **3 encounters**;
- reconciled evidence represented: **8 encounters**;
- explicit add-group evidence represented: **1 encounter**;
- explicit damage-window evidence represented: **1 encounter**.

Detailed historical closeout: `docs/phase9_encounter_model_closeout.md`.

## Retrospective hardening closeout

The hardened corpus review and persistence gate completed on **2026-09-03**:

- boss source files: **490**;
- canonical boss encounter identities: **490 / 490**;
- inferred mechanic rows requiring semantic review: **109 across 35 bosses**;
- review decisions: **109 / 109**;
- accepted: **94**;
- rejected as currently inferred: **15**;
- pending: **0**;
- accepted rows persisted as `reviewed_single_source`: **94**;
- UESP evidence rows persisted: **94**;
- rejected rows persisted as canonical facts: **0**;
- first apply: **94 facts inserted / 94 evidence rows inserted**;
- second apply: **0 inserted / 94 facts existing / 94 evidence rows existing**, proving idempotency;
- post-persistence audit: **94 / 94 canonical facts matched**, **94 / 94 evidence rows matched**, **0 missing**, **0 conflicting**;
- focused persisted-mechanic audit tests: **3 passed in 0.22s**;
- structural source audit: **490 / 490 health**, **2070 / 2070 abilities**, **4 / 4 explicit phases**, **2274 / 2274 dialogue rows**, **2450 / 2450 section rows**, **0 problems**;
- structural dry run: **490 ready**, **0 blocked**;
- controlled structural apply created a SQLite backup before write and independently verified the same exact counts after commit.

The reviewed-single-source path remains deliberately separate from corroboration-based promotion. Human review does not impersonate a second source. Inferred mechanics remain outside the structural-import shortcut.

Detailed retrospective closeout: `docs/phase9_retrospective_hardening_closeout.md`.

**Hardened Phase 9 exit criteria met on 2026-09-03.**

---

# PHASE 10 · Encounter Evaluation
**Status: 🟢 Complete**

Phase 10 combines Encounter + Requirements + Roster + Builds and produces covered, redundant, insufficient, missing, conflict, and unknown outcomes while preserving the boundary between collective capability and provider assignment.

Historical closeout evidence:

- real saved builds: **2**;
- unique real characters: **2**;
- authoritative exit roster: **Magrat → DF Healer** and **Susan → Necro Tank**;
- both selected builds: **0 capability-resolution gaps**;
- Oaxiltso veteran: **fully evaluable = true**;
- Oaxiltso veteran: **capability-ready = true**;
- provider rows: **0**, as expected for that validation encounter;
- focused final checkpoint: **16 passed in 1.65s**;
- full suite after final historical Phase 10 changes: **2031 passed in 94.10s**;
- detailed historical closeout: `docs/phase10_encounter_evaluation_closeout.md`.

## Retrospective revalidation after Phase 9 hardening

The dependency-impact rerun completed on **2026-09-03** against the reviewed canonical mechanic corpus.

Canonical consumption boundary:

- raw inferred source mechanics: **109**;
- canonical mechanic facts: **94**;
- accepted inferred replacements: **94**;
- rejected/unpersisted inferred: **15**;
- canonical facts without raw inferred source rows: **0**;
- raw inferred downstream leaks: **0**;
- result: **PASS**.

Focused regression checkpoint:

- **38 passed in 3.34s**.

Current canonical-filtered execution corpus:

- encounters with requirements: **18**;
- fully evaluable encounters: **6**;
- fully ready encounters: **6**;
- covered requirements: **20**;
- unknown requirements: **24**;
- conflicting requirements: **0**.

Real roster revalidation used **Magrat → DF Healer** and **Susan → Necro Tank**, with **0 capability-resolution gaps** on both selected builds.

Oaxiltso veteran control result:

- fully evaluable: **true**;
- capability-ready: **true**;
- execution rows: **6**;
- provider rows: **0**;
- Phase 10 exit ready: **true**.

Hiath the Battlemaster veteran boundary result:

- execution rows: **5**;
- covered: Agony interrupt, Purifying Light cleanse, Solar Disturbance interrupt;
- unknown: Invisibility positioning because no source-backed execution-method fact is persisted;
- unknown: Roll Dodge movement because the source describes **Hiath's own roll dodge**, exposing an actor-semantics limitation in the current requirement contract rather than a player movement action;
- conflicting requirements: **0**;
- provider rows: **0**.

The Hiath result is an expected preserved-UNKNOWN boundary, not a reason to manufacture player execution semantics. Phase 10's promise is correct evaluation and explicit uncertainty, not universal encounter completeness.

Detailed retrospective closeout: `docs/phase10_retrospective_revalidation_closeout.md`.

**Hardened Phase 10 exit criteria met on 2026-09-03.**

---

# PHASE 11 · Provider Assignment
**Status: 🟢 Complete**

Phase 11 moved BFF from “does the roster have the required support capability?” to “who should provide it here?” while preserving the boundary between encounter facts, raid-support requirements, provider capability, suitability, responsibility conflicts, and later build optimization.

Historical closeout evidence:

- provider assignment preserves Phase 10 VIABLE / UNRESOLVED / CONFLICTING evidence;
- suitability is explicit and evidence-backed;
- deterministic assignment does not use roster order as a hidden tie-breaker;
- responsibility-conflict evidence is explicit;
- Oaxiltso veteran + default raid coverage + real roster produced a deterministic War Horn provider assignment;
- focused checkpoint: **39 passed in 0.69s**;
- full regression suite: **2031 passed in 73.87s**;
- real configured provider evaluation: **PASS**;
- detailed closeout: `docs/phase11_provider_assignment_closeout.md`.

Phase 11 does not automatically reopen for Phase 9 mechanic enrichment because provider requirements are a separate semantic layer. If Phase 10 retrospective validation changes requirement/capability conclusions used by provider assignment, Phase 11 receives its own dependency-impact rerun.

**Exit criteria met on 2026-09-03.**

---

# PHASE 12 · Build Optimization
**Status: 🟢 Complete**

Phase 12 established the authoritative bounded build-optimization path. The optimizer represents exact immutable candidate changes, delegates ESO math and capability evidence to existing engine services, keeps hard constraints separate from objective score, and ranks only candidates that have enough evidence to be rankable.

The closed real-data scope is deliberately bounded one-change optimization for Mundus, armor traits, armor enchants, and food/drink. The candidate/evaluator contracts are reusable for later gear-set, mythic, weapon, skill, morph, ultimate, CP, potion, and configuration expansion; Phase 12 closeout does not pretend those broader combinatorial dimensions are already exhaustively searched.

Closeout evidence on **2026-09-03**:

- one immutable `BuildCandidate` / `BuildChange` representation preserves canonical identity and exact before/after changes;
- deterministic candidate generation and ranking use explicit named objective metrics with no hidden fallback score;
- `WORSENED`, `UNSATISFIED`, and `UNKNOWN` hard-constraint states block ranking rather than becoming point penalties;
- candidate scoring delegates to existing static build/healing, sustain, capability, encounter-evaluation, and provider-assignment services;
- required capability coverage and baseline provider responsibility remain explicit gates;
- unsupported or unresolved evidence cannot win by being treated as zero;
- real saved build **Magrat → DF Healer** completed baseline → candidates → scoring → ranking → explanation with Oaxiltso provider context and **Necro Tank** roster support;
- winning recommendation: **Witchmother's Potent Brew → Ghastly Eye Bowl**;
- winning healing comparison delta: **+2150.139**;
- winning Magicka sustain: **repaired**, minimum **3573**, ending **6314**;
- capability coverage: **preserved**;
- provider responsibility: **preserved**;
- selected-candidate unresolved evidence: **none**;
- provisioning search hardening reduced the real audit from **121 discovered** to **73 evaluated** candidates without changing the winner or hard-constraint conclusions;
- focused optimizer/performance checkpoint: **117 passed in 8.94s**;
- final full regression checkpoint: **2232 passed in 87.58s**;
- detailed closeout: `docs/phase12_build_optimization_closeout.md`.

The healing value used by the closeout audit is a modeled comparison score, not HPS. The healer/DD role boundary remains explicit; diagnostic role mismatch does not become a valid healer recommendation.

**Hardened Phase 12 exit criteria met on 2026-09-03.**

---

# PHASE 12.5 · Team Workflow Integration
**Status: 🟡 Active**

Phase 12.5 is the product-integration bridge between the completed bounded build optimizer and the later temporal engines. It does **not** expand Phase 12's mathematical search scope and it does **not** substitute UI plumbing for Phase 13 Rotation Engine work.

The authoritative user workflow is:

```text
COMP MAKER
   ↓
NAMED TEAM + EXACT CHAIR / BUILD ASSIGNMENTS
   ↓
ROSTER
   ↓
LOAD TEAM IN OPTIMIZATION
   ↓
AUDIT / IMPROVE / COMPARE
   ↓
ROSTER
```

Active scope, in order:

1. **Canonical team identity**
   - a named team created in Comp Maker, displayed in Roster, and loaded in Optimization is the same user-facing team identity;
   - generated-plan persistence may remain an implementation detail, but it must not create a second competing team concept in the UI;
   - recruits remain assignment slots, never fabricated roster people.

2. **Structured assignment persistence**
   - preserve slot, player/recruit state, class, role, exact selected build, source identity, gear, skills/abilities, Mundus, candidate/template identity, and explicit unresolved fields where known;
   - do not reconstruct structured application state by scraping human-readable evidence text when a canonical field can be persisted instead;
   - native Comp Brainstorm writes only the Raid Plan-scoped draft authority; the old name-only draft is migration-read input only and is no longer dual-written.
   - native Optimization stages BuildId/name plus source kind/name and rejects stale proposals when either identity or provenance changed before Apply.

3. **Visible assigned state in Comp Maker**
   - each chair clearly shows the exact build/source currently assigned before transfer;
   - explicit manual choices remain authoritative and are never silently reranked during transfer;
   - Optimization now treats stable BuildId as authoritative and falls back to Build name only when no stable BuildId exists.

4. **Hard-constraint routing integrity**
   - class and required-gear constraints apply to every candidate source, including saved builds, reference templates, and ESO Logs snapshots;
   - native Comp Engine now reuses shared hard-ingredient semantics for locked class/gear: blocked evidence remains visible but cannot route as a replacement;
   - wrapper/install order may not bypass hard constraints.

5. **Static Optimization integration groundwork**
   - Optimization loads a named team from Roster and consumes existing canonical build, coverage, provider, sustain, and bounded optimization evidence;
   - native Phase 15.5 Optimization now consumes canonical static capability analysis directly for the exact Raid Plan-selected Saved Builds, with BuildId-first identity and fail-closed ambiguous name fallback;
   - legacy Optimization presentation monkey patches are retired; reusable analysis/comparison services and evidence-gap guidance remain service-owned;
   - placeholder recommendation surfaces are replaced only where existing engine evidence supports the claim;
   - temporal/rotation-dependent conclusions remain deferred to Phases 13–15.

6. **Team A / Team B bounded comparison groundwork**
   - compare only currently supported canonical/static metrics;
   - do not label modeled single-event or bounded objective values as parse DPS, raid ceiling, or simulated encounter outcome.

7. **Recruit → real player → reusable build workflow**
   - a prescribed recruit chair can later be assigned to a real roster player without rebuilding the team;
   - the player may keep an existing build or save the prescribed setup as a new reusable Build while preserving the original Build unchanged.

Current Phase 13.2 bridge work now also supplies reusable Comp Maker / Optimization provider contracts without weakening Phase 12.5 identity and persistence boundaries:

- source-neutral named-buff marginal value and duplicate suppression;
- recipient-capacity modeling, including repeated applications and concurrent coverage limits;
- sequential roster context so later chairs do not receive credit for already-covered effects;
- timed provider windows and intentional staggered multi-carrier strategies;
- scoped uptime targets with explicit provenance rather than universal hard-coded percentages;
- provider requirement compatibility remains backward compatible when coverage/timing policy is not supplied.

Verified focused checkpoints supplied by the user:

- Extreme / Comp optimization contract: **147 passed in 25.38s**;
- marginal provider bridge: **50 passed in 1.08s**;
- recipient-coverage bridge: **33 passed in 0.88s**.

The corrected expanded temporal/provider/workload suite was rerun on **2026-10-07** inside the durable Phase 15.5 Planning Stability gate after commit `72c25c0`; the expanded gate reported **321 passed in 37.29s**. The old pending-rerun boundary is therefore closed.

**Phase 12.5 exit criteria:** a representative real team can be created in Comp Maker, saved and inspected in Roster, loaded into Optimization, and transferred back without losing or silently changing team identity, exact assignment choice, source, gear/skill evidence, hard constraints, recruit state, or unresolved boundaries. Focused regression tests must pass, a real-data end-to-end workflow must be demonstrated, and an appropriate full regression checkpoint must be recorded before Phase 12.5 is closed.

**Real-data closeout gate on 2026-10-07:** the current native read-only Phase 12.5 Raid Plan audit was run against the protected **Half of Us Are Dead in Godslayer** plan using the uploaded canonical `foundrydock.db` plus the repaired canonical ESO reference copy. The audit reported **12/12 real chairs**, **12/12 exact selected Saved Builds**, **12/12 builds resolved identically by Optimization**, and **12/12 source-tagged/planned chairs**, with no identity/provenance problems. SHA-256 verification confirmed the protected user database and canonical ESO database were unchanged after the live audit. **RESULT: PASS.** The remaining closeout gate is the required full repository regression checkpoint.

---

# PHASE 13 · Rotation Engine
**Status: 🟡 Active engine work**

Phase 13 is active in controlled overlap with the still-open Phase 12.5 product-integration work. Phase 13 closeout remains gated on canonical Character → Build → Team identity integration; current engine development may proceed so long as it does not invent a competing identity or persistence model.

Start with semi-static rotations, then add dynamic priorities, duration/recast windows, resource awareness, proc alignment, execute, movement, interruptions, mechanic handling, and healing rotations.

## Current Phase 13 engine work

The active line now includes two mutually reinforcing tracks.

### A. Extreme build / class-route search

BFF can efficiently search the reviewed pure-class / Class Mastery and legal subclass structural universe without recomputing static route structure for every request.

Implemented and covered:

- precomputed Extreme Build Catalog with database fingerprint and subclass-rule version;
- **3,220** legal class configurations, **1,330** unique three-line sets, and **21** class skill lines in the generated catalog used by the current local database snapshot;
- independent front/back six-slot allocation search;
- active-bar versus either-bar standing-effect scope;
- reviewed passive formulas and standing-skill families;
- source-neutral named-buff stacking and external-context marginal value;
- stale or malformed catalog rejection with canonical live fallback;
- structural pruning and unique-line-set memoization instead of blind 28×28 repeated scoring;
- physical-resistance regression preserving the independent-bar **10,414** reviewed result rather than the older **9,174** compromised result;
- verified expanded Extreme / Comp contract checkpoint: **147 passed in 25.38s**.

The output remains a **best reviewed lower bound**, not an unsupported claim of a globally optimal ESO build. Broader class passive, gear, race, Mundus, CP, enchantment, proc, runtime, and encounter coverage must continue to expand before that boundary changes.

#### Extreme Builds role-complete completion roadmap

Extreme Builds is one shared legal-character optimization engine with role-specific objective packages for **Healer, Tank, and Damage Dealer**. It must not fork into separate competing build engines. All roles reuse the same canonical Character → Build identity, legal class/subclass search, static combat math, runtime/effect evidence, candidate pruning, unresolved-boundary handling, and search-space audit contracts.

Current engineering estimate toward a role-complete Extreme product is approximately **55–60% overall**. Architecture is farther along than exhaustive ESO mechanic/corpus coverage. Percentages below are planning estimates, not phase-closeout claims.

##### E1. Unified runtime snapshot — 🟢 Complete

E1 now replaces fragmented runtime scenario inputs with one deterministic runtime history plus one exact snapshot time:

```text
Runtime History
  ├── potion activations
  ├── cast buffs
  ├── triggered skills
  ├── gear procs
  ├── cooldown history
  ├── deterministic chance rolls
  ├── condition evidence
  ├── stacking / refresh
  ├── bar provenance / transitions
  ├── source-persistence semantics
  ├── explicit condition windows
  └── target applicability
          +
   exact snapshot time
          ↓
      CombatState
```

Closeout on **2026-09-15** proved one role-neutral runtime contract for named buffs, generic timed effects, potion windows, triggered skills, gear procs, `SELF_OR_ALLY`, explicit condition evidence, ordered event streams, cooldowns, stacking, exact active-window boundaries, bar-tagged activation, coherent bar-transition history, and reviewed source-persistence behavior. Restoration-heavy and Sacred Ground runtime windows now enter the production Extreme healer path through the same snapshot instead of parallel healer-only truth.

The closed Weapon Damage and Spell Damage records also expose machine-readable ownership and deterministic runtime witnesses. E1 owns only ordered player runtime history; target Health / Off Balance remain `target_state`, same-build higher resource remains `structural_state`, Font / Calculated Defense remain `class_runtime`, and Sorcerer slot legality remains `active_bar`.

Real integration used the canonical saved **Margrat → DF Healer** build and reported `snapshot_unresolved_count=0`, `e1_real_integration_ready=True`, `e1_healer_runtime_bridge_closed=True`, `e1_power_runtime_bridge_closed=True`, and `e1_closeout_audit_ready=True`. Focused E1 regression: **45 passed in 8.29s**. Full repository regression: **2970 passed in 198.10s**, failures **0**. Detailed closeout: `docs/extreme_e1_unified_runtime_closeout.md`.

The audit also exposed a separate canonical identity discrepancy: the live healer build is currently owned by `Margrat`, while a distinct `Magrat` character exists with zero builds. That issue belongs to Phase 1 / identity cleanup and does not reopen E1.

##### E2. Complete shared legal-character search — 🟡 partial

The universal candidate generator must eventually cover, search, safely prune, or explicitly block every relevant legal dimension:

- race;
- base class and legal subclass route;
- character progression and class passives;
- attributes;
- Mundus;
- food / drink;
- potion capability and explicit use state;
- armor weights and armor passives;
- gear sets, mythics, monster sets, arena weapons, and proc mechanics;
- armor, jewelry, and weapon traits;
- glyphs / enchantments;
- front/back weapon configuration and weapon passives;
- active skills, morphs, ultimates, and standing/slotted effects;
- Champion Points;
- Class Mastery where legally available;
- exact event/runtime state required by the selected objective.

The existing Extreme catalog already provides the legal class/subclass structural universe, independent bars, active-bar/either-bar scope, reviewed passive families, memoization, and structural pruning. Remaining work is primarily exhaustive dimension integration and mechanic coverage rather than a replacement combinatorial engine.

##### E3. Mechanic-coverage audit — 🟡 continuous requirement

For every candidate mechanic, Extreme must preserve one of four states:

```text
SUPPORTED
CONDITIONAL + PROVABLE
UNRESOLVED
UNSUPPORTED
```

Unknown mechanics never silently become zero. Exhaustive audits must cover class/racial/armor/weapon passives, sets and procs, mythics, arena weapons, skills/morphs/ultimates, CP, Mundus, consumables, traits/enchants, and Class Mastery. Inventory coverage is not mechanic coverage.

##### Healer objective package

**H1. MOST Actual Heal — ~80% engineering estimate.** This is the most mature role objective. Existing coverage includes legal heal discovery, HEAL-only component math, mixed damage/heal exclusion, Critical Healing and cap behavior, Healing Done and ability-family modifiers, conditional/passive modifiers, low-health scenarios, Major Mending, named buffs, potion/skill source discovery, triggered skills, gear procs, runtime conditions, self-or-ally targeting, ordered runtime history, and exact expiration. Remaining work is unified snapshot orchestration plus exhaustive race/attributes/gear/CP/traits/glyphs/weapon/skill/mechanic search and denominator proof.

**H2. MOST Emergency Heal — ~70%.** Reuse H1 with explicit low-health and emergency-state assumptions. Complete the same exhaustive character/mechanic dimensions before claiming a global maximum.

**H3. MOST Sustained Healer — ~30–35%.** Requires rotations, HoTs, burst healing, resources, cooldowns, proc windows, recipient/target-count policy, overheal interpretation, and fight duration. This depends materially on Phase 13 Rotation Engine and later Phase 14 Combat Simulation rather than static snapshot optimization alone.

**H4. MOST Raid-Support Healer — ~50%.** Multi-objective search across healing adequacy, buff/debuff coverage and uptime, provider workload, sustain, and survivability. Reuse Phase 11/12.5 provider evidence rather than inventing a healer-specific support score.

##### Tank objective package

**T1. MOST Raw Physical Resistance — ~65%.** Finish exhaustive race, attributes, armor, traits, enchants, Mundus, sets, skills/passives, CP, temporary buffs, and active-bar state. Keep raw stat maximum separate from effective mitigation/cap interpretation.

**T2. MOST Raw Spell Resistance — ~60%.** Reuse T1 architecture with spell-resistance-specific modifier coverage.

**T3. MOST Health — ~55%.** Exhaustively search race, attributes, food, enchants, gear, CP, passives, and temporary Max Health effects.

**T4. MOST Blocky — ~40%.** Treat largest block mitigation, lowest block cost, and longest sustainable block as distinct objectives. Model block mitigation, block cost, stamina state, recovery constraints, weapon legality, CP, sets, passives, and runtime buffs without collapsing them into one arbitrary tank score.

**T5. MOST Survivable Tank — ~25–30%.** Combine incoming-damage sequence, resistance/mitigation, block, shields, self-healing, health, recovery, and sustain. A true survivability maximum depends on Phase 14 temporal combat simulation.

**T6. MOST Support Tank — ~45%.** Optimize raid buffs/debuffs and provider coverage subject to tank legality, sustain, survivability, recipient reach, and uptime. Encounter-specific conclusions belong later to Phase 15.

##### Damage Dealer objective package

**D1. MOST Single Hit — ~55%.** DD snapshot counterpart to MOST Actual Heal. Search the complete legal character plus target state, buffs/debuffs, proc state, resistance/penetration, and exact damage-event semantics to find the largest legal single damage event.

**D2. MOST Critical Hit — ~50%.** Find the largest legally crittable event without multiplying by critical chance. Preserve crit eligibility and target Critical Resistance semantics.

**D3. MOST Execute Hit — ~40%.** Add explicit target-health state, execute scaling, execute passives/skills, target debuffs, and runtime conditions.

**D4. MOST AoE Event — ~35%.** Keep largest hit to one target separate from aggregate damage across an explicit target count. Never silently convert multi-target aggregation into a single-target objective.

**D5. MOST Bash Damage — 🟡 existing novelty lane.** Fold existing MOST Bashy infrastructure into the shared DD/tank objective framework rather than maintaining a separate build engine. Outstanding bash-channel and dual-bar One Hand + Shield legality/mechanic gaps remain explicit blockers.

**D6. MOST Sustained DPS — ~25–30%.** Requires build + deterministic rotation + DoT/proc/cooldown/resource/execute state + simulation duration. This is intentionally downstream of the snapshot Extreme core and depends on Phases 13–14.

##### E4. Search-space proof — 🔴 required before “global maximum”

Every definitive Extreme result must report the legal search denominator and disposition of candidates. At minimum expose counts for class routes, races, attribute configurations, Mundus choices, gear combinations discovered/pruned, CP configurations, skills, unsupported mechanics, and unresolved mechanics. The solver must demonstrate that every relevant legal category was searched, safely pruned, or explicitly unresolved before the UI may label a result a **global maximum**. Otherwise the result remains a **best reviewed lower bound**.

##### E5. Search-performance engineering — 🟡 partial

Continue objective-aware dominance pruning, safe upper-bound pruning, memoization, equivalent-state deduplication, branch-and-bound, and staged candidate expansion. Existing Extreme catalog memoization/structural pruning is the foundation; exhaustive gear/CP/skill search must not become a blind Cartesian product.

##### E6. Real-build validation — 🔴 required closeout gate

Validate at least one real saved character/build for each role through baseline → Extreme search → winning build → explanation → unresolved audit → comparison:

- Healer: **Magrat → DF Healer** is the primary real validation path;
- Tank: use a real canonical saved tank build;
- Damage Dealer: use a real canonical saved DD build.

Synthetic fixtures remain necessary but cannot satisfy the real-integration gate by themselves.

##### E7. Role-complete Extreme product surface — 🔴 planned

The final Extreme UI should select **role**, **objective**, **scenario**, target/runtime assumptions, and reviewed-vs-exhaustive search depth, then show the complete winning build, exact objective result, why it won, runtime/buff proof, search coverage, candidates eliminated, unresolved mechanics, and proof/confidence status. No unexplained maximum number may be presented as authoritative.

##### Cross-role constrained optimization

After single-objective role packages are trustworthy, add constrained multi-objective searches rather than arbitrary universal scores. Examples:

- healer: maximize healing subject to required support effects, minimum sustain, and survivability;
- tank: maximize survivability subject to taunt/support obligations and minimum sustain;
- DD: maximize damage subject to sustain, assigned raid support, and mechanic compliance.

These constrained builds are the bridge from laboratory Extreme objectives to raid-usable recommendations and ultimately Phase 15 encounter-aware optimization.

##### Planned completion order from current state

```text
1. Unified runtime snapshot orchestration
2. Finish Healer single-event snapshot objectives
3. Generalize exact-event optimizer to DD single-hit / crit / execute
4. Finish Tank static/snapshot objectives
5. Complete shared race / attributes / gear / CP / traits / glyphs / weapon search
6. Run exhaustive mechanic-corpus and search-space denominator audits
7. Validate one real saved build per role
8. Close snapshot Extreme Engine
9. Use Phase 13 rotations for sustained role objectives
10. Use Phase 14 simulation for sustained DPS / healing / survivability
11. Use Phase 15 encounter context for raid-usable Extreme recommendations
```

Planning snapshot from 2026-09-09:

| Extreme area | Approximate engineering progress |
| --- | ---: |
| Shared legal class/subclass architecture | 90% |
| Static character calculation infrastructure | 90% |
| Runtime/proc architecture | 85% |
| Unified runtime snapshot orchestration | 100% |
| Whole-character exhaustive candidate dimensions | 55% |
| Mechanic corpus coverage | 50% |
| Search-space proof / exhaustive audit | 30% |
| Healer snapshot Extreme | 80% |
| Tank snapshot Extreme | 55% |
| DD snapshot Extreme | 50% |
| Sustained/temporal Extreme | 25–30% |
| Encounter-aware Extreme | 20% |
| **Role-complete Extreme product** | **55–60%** |

These estimates track engineering readiness only. They do not supersede the roadmap completion standard, corpus audits, real-integration gates, or regression requirements above.

### B. Team provider orchestration for Comp Maker / Optimization

The team optimization bridge now distinguishes four questions that were previously easy to collapse into one misleading “provider exists” flag:

```text
DOES THE TEAM HAVE THE EFFECT?
          ↓
DOES THIS CANDIDATE ADD MARGINAL VALUE?
          ↓
CAN THE PROVIDER REACH THE REQUIRED RECIPIENTS?
          ↓
IS THE EFFECT ACTIVE AT THE RIGHT TIMES / UPTIME?
```

Implemented contracts include:

- duplicate named effects receive zero marginal tie-break credit when already supplied by a skill, potion, set, passive, or group provider;
- hard provider IDs and role constraints remain authoritative and cannot be weakened by marginal-value scoring;
- recipient coverage supports targets per application and maximum useful/concurrent applications per refresh cycle;
- six-target mechanics can require repeated applications to cover a 12-player group, while a one-instance six-target provider can remain explicitly partial;
- provider effects selected for one open chair are carried into the evolving team context for later chairs;
- timed applications can be staggered across multiple carriers rather than being incorrectly deleted as duplicates;
- strategy may explicitly require a minimum number of distinct carriers, such as tank + healer support-ultimate rotations;
- temporal evaluation reports covered time, uncovered gaps, overlap, active sources, and target-uptime attainment;
- target uptime is effect/encounter/phase policy, not a universal constant.

### C. BTVTools calibration evidence

User-supplied BTVTools screenshots from a Lokke hard-mode fight are now accepted as **benchmark/calibration evidence**, not canonical static ESO mechanics. They demonstrate why provider policy needs encounter/effect scope and provenance.

Visible examples include:

- Major Berserk: **27.9% observed / 96% BTV target**;
- Major Slayer: **56.0% observed / 90% BTV target**;
- Powerful Assault: **85% observed / 95% BTV target**;
- Minor Courage: **84% observed / 97% BTV target**;
- Major Vulnerability: **38.3% observed / 56% BTV target**;
- Off Balance: **6.6% observed**, with BTV showing a theoretical maximum around **31.8%** for its displayed **7s / 22s cycle**.

The screenshot corpus also includes buff pages and critical-damage timelines that can support later calibration of overlapping Major Force / Brittle / other support windows. Screenshot-derived benchmarks must retain provenance and fight scope and may not silently become universal game constants.

### D. Provider rotation-workload comparison

The first source-neutral provider-workload contract now sits on top of the existing
recipient and temporal coverage gates. It can aggregate one or more contributor
rotations and expose, without inventing a universal weighted score:

- provider applications and refreshes per minute;
- provider GCD occupancy;
- resource spend by resource type;
- Ultimate spend;
- occupied provider bar slots;
- whole-plan skill, Ultimate, heavy-attack, bar-swap, and other action counts;
- caller-evidenced primary-role displacement;
- unresolved cost, action binding, and bar ownership as comparison-blocking evidence.

Two plans may be compared only when both meet recipient coverage, meet temporal
coverage, and have resolved workload evidence. The comparison deliberately reports
independent deltas rather than declaring that one heavy attack, GCD, bar slot,
resource cost, or Ultimate point has a universal exchange rate.

The canonical workload bridge now derives provider-action evidence from the exact
saved Character → Build identity and scheduled action. It reuses authoritative
ability-cost, saved-build slot, and imported cast/channel-timing services to resolve:

- final Magicka, Stamina, or Health skill cost after currently verified racial,
  armor, and jewelry cost modifiers;
- final ordinary canonical Ultimate cost after currently verified build modifiers;
- independent cost accounting for supported compound-resource skills;
- exact scheduled-bar legality and occupied provider slot;
- cast/channel occupancy for each provider application;
- only action-relevant unresolved evidence, without allowing an unrelated unused
  skill gap elsewhere on the build to poison the comparison.

General GCD duration and primary-role displacement remain explicit caller policy or
evidence. They are not inferred from zero cast/channel time.

Provider workload can now retain the canonical recipient-capacity and temporal-
coverage result objects that authorized the comparison. Their actual conclusions
override stale copied booleans, and UI-ready explanation evidence exposes recipient
counts, covered time, targets, gaps, distinct-carrier failures, casts, resources,
Ultimate, bar space, and role displacement without inventing a universal winner.

Comp Maker and Team Optimization now share a theme-native Provider Rotation Workload
card and typed presentation path for those exact workload/comparison objects. Until
a canonical rotation result is attached, the visible card explicitly distinguishes
static capability availability from recipient coverage, uptime, sustain, and role
disruption. Editing the composition or optimization selection clears attached
workload evidence so a result from an older team cannot remain on screen as if it
still applied.

The shared team surfaces can now generate candidate workload projections from their
currently selected exact saved builds when supplied explicit provider strategy,
coverage, rotation-plan, progression, GCD, and role-displacement evidence. The
orchestrator binds contributors by exact Character → Build identity, matches only
explicit action names, retains every scheduled matching cast, and renders missing
plans, progression, contributors, or actions as candidate blockers. Reference and
ESO Logs candidates do not silently become saved-build rotation evidence.

Persistent/summoned Ultimates with an explicit secondary activation contract now
reuse the existing canonical ability-description resolver. For example, a zero-base-
cost Eternal Guardian can contribute the evidenced 75-Ultimate Guardian's Wrath
activation cost; unsupported zero-cost Ultimates remain unresolved.

Expanded canonical provider-workload, coverage, explanation, presentation, final-
cost, saved-slot, timing, and Ultimate checkpoint: **122 passed, 1 skipped in 1.07s**.
The single local skip is the real PySide widget check because PySide6 is unavailable
in the Linux scratch runtime; the source-level dual-surface/install checks passed and
the widget test remains included for the user's Windows environment.
Latest user-reported full-suite checkpoint after the canonical workload slice:
**2,626 passed in 73.30s** on Windows / Python 3.12.4.
Candidate-generation focused checkpoint: **98 passed, 1 skipped in 0.69s**. The
skip remains the PySide6 widget check in the Linux scratch runtime.

Active next work:

1. convert the user-supplied BTV screenshot corpus into structured benchmark fixtures with provenance, encounter scope, observed uptime, target/reference uptime where visible, theoretical maximum where visible, and explicit unknown fields rather than guessed values;
2. test policy selection, target-vs-theoretical-max validation, temporal window scoring, overlap/gap explanation, and BTV-style feedback against those fixtures;
3. connect those benchmark fixtures to Comp Maker / Optimization explanation paths without treating them as canonical ESO mechanics;
4. feed encounter/provider assignment policies and the growing set of saved team rotation plans into the new Comp Maker / Optimization candidate-generation seam;
5. continue thorough healer, tank, and DD rotation coverage with class passives, armor/set duration modifiers, runtime proc conditions, and encounter-specific timing.

Fight-horizon policy: most raid fights are expected to finish within roughly six minutes in the user's working context, so **360 seconds may be used only as an overrideable fallback planning ceiling when encounter-specific timing is unavailable**. It is not a canonical encounter duration. Optimization should prioritize important burn/mechanic windows over meaningless attempts to force every support effect to 100% global uptime.

### Phase 13 / current Phase 13.5 closeout structural audit

**Closeout result (2026-09-17): COMPLETE.** The detailed ledger and architecture
audit have dispositions for every material finding, the architecture closeout gate has
zero blockers, and the full repository checkpoint is **3026 passed in 46.93s**. The
remaining UI class-patch and service-catalog candidate lists are explicit migration
inventories, not undispositioned correctness findings.

Before the current Phase 13 line is considered ready to close, and before Phase 14 begins building on top of it, perform a deliberate repository-wide structural audit. This is a stabilization gate, not a feature-expansion pass.

The audit must cover:

- **dead and obsolete code:** identify unreachable services, unused helpers, stale imports, abandoned flags, superseded adapters, and compatibility paths that no longer have a supported caller;
- **duplicate or competing authority:** find multiple services, repositories, factories, registries, dictionaries, or UI paths that claim ownership of the same concept and resolve them to one authoritative implementation where appropriate;
- **semantic conflicts:** trace important ESO concepts across the codebase to catch two active implementations that encode different rules even when both are individually tested. Priority examples include penetration, buff/debuff duration, periodic classification, execute scaling, potion effects, resource costs, proc timing, bar ownership, healing modifiers, and target/recipient semantics;
- **architecture drift:** identify code that works but bypasses canonical Character → Build → Team identity, canonical effect/runtime services, repositories, source/provenance boundaries, or other rules defined by the architecture documents;
- **stale tests and shims:** remove or rewrite tests that protect obsolete behavior, and review temporary wrappers, feature flags, migration shims, compatibility aliases, and fallback paths to determine whether they are still intentionally required;
- **dependency and configuration cruft:** review unused dependencies, duplicated configuration, stale data files, logging/debug leftovers, exception-swallowing fallbacks, and documentation that no longer describes the actual authoritative path;
- **recorded disposition:** every material finding must be fixed, explicitly retained with a reason, or recorded as a countable deferred item with an owner/phase boundary. Unknown or conflicting behavior may not be cleaned up by silently choosing whichever implementation is convenient;
- **post-cleanup validation:** rerun the affected focused suites and an appropriate full regression checkpoint after removals or consolidations so cleanup cannot become an untested behavior change.

The purpose is not to minimize line count. The purpose is to prove that the architecture BFF intends to carry into simulation has one coherent set of authorities and that historical implementation layers are not quietly contradicting the canonical engine.

**Prerequisite / integration gate:** Phase 12.5 must be green before Phase 13 is closed. Rotation evaluation must consume the canonical Character → Build → Team assignment path rather than introducing another page-specific build/team identity model.

**Hardened exit criteria:** BFF can produce and evaluate a realistic damage, support, or healing rotation from verified skill behavior and resource constraints; action timing is deterministic from identical inputs; class passives and build-derived effect-duration modifiers are respected; provider recipient and temporal obligations can be represented where relevant; unsupported mechanics remain explicit; at least one real build is validated end-to-end; the Phase 13 structural audit above is completed with findings dispositioned; focused and appropriate regression gates pass.

---

# PHASE 14 · Combat Simulation
**Status: 🟠 Active / validation-hardening**

Combat Simulation is implemented on the current Phase 15.5 line and is now in
validation-hardening rather than initial construction. The canonical runtime includes
deterministic event ordering/replay, resource and health state transitions, target
binding, outgoing damage/healing projection, fight termination, snapshots, and
fail-closed unresolved evidence. A dedicated Phase 14 regression gate is green in the
current validation checkout.

Phase 14 is not marked complete yet because the final real Saved Build end-to-end proof
remains blocked by player-specific physical gear metadata omitted by the historical HOUAD
import (exact armor weights on multi-weight sets and exact front-bar weapon subtype).
Canonical ESO evidence is backfilled where unambiguous; ambiguous facts remain explicit
and must be supplied through Builds rather than guessed.

- deterministic simulation event queue and replay signature;
- canonical `EffectiveBuildSnapshot + RotationPlan` kernel;
- resource-timeline projection through existing sustain authority;
- healing, Health-state, skill-effect, outgoing-damage, target-binding, and fight-termination services;
- exact-time Combat Simulation snapshots;
- saved-build DD damage/provider integration;
- planning-workflow round-trip coverage;
- causal same-instant derived-damage ordering with explicit parent-occurrence provenance;
- ordinary U51 status-damage finalization through canonical DD critical/Damage Done/mitigation/Damage Taken stages;
- chronological saved-build DD replay through a fresh target-Health ledger so resolved status damage affects later execute calculations and fight termination;
- exact-Health Poisoned status replay: each tick reads the chronological pre-tick target Health, including prior status damage, and bounded deterministic replay continues until the status-damage timeline converges;
- chronological status-interaction replay: enemy-target Vulnerability/Breach windows enter canonical target CombatState/resistance only after the parent hit, while reviewed caster-side Weapon/Spell Damage windows rebuild later DD contexts through the shared timed EffectVariant projection;
- status interaction windows are preserved in ordinary Combat Simulation runtime-window output for snapshot/audit visibility;
- explicit fail-closed boundary when caster-side status effects overlap an external caller-owned runtime build-context authority that cannot yet be composed without dropping unrelated timed state;
- expanded Phase 14 Combat Simulation CI checkpoint on **2026-10-07: 285 passed in 6.32s**, including Saved Build topology evidence, Poisoned exact-Health replay, target/caster status interaction replay, the UESP -> canonical gear-piece topology repair contract, formal audit wiring, and Combat Simulation service-catalog integrity;
- Phase 15.5 Planning Stability gate is green at **325 passed in 92.22s** after exact two-handed Saved Build topology, PM Greatsword template preservation, real-workbook import preservation, and the explicit armor-pattern repair workflow were included in the current gate.

Real-build audit hardening on **2026-10-06** found that the audit entrypoint was still
loading the legacy `data/builds.json` mirror. The normal audit path now loads and
Pydantic-validates canonical `build_catalog` state from `user_data/foundrydock.db`
through SQLite read-only mode, verifies the database SHA-256 is unchanged, and uses
the shared canonical Build projection. Legacy JSON input remains available only via
an explicit compatibility flag. The mandatory real saved-build execution gate was exercised on **2026-10-07**
against the protected canonical `foundrydock.db` in SQLite read-only mode, with SHA-256
verified unchanged before and after every attempt. The gate did not pass because the
canonical saved DD catalog is missing combat-relevant gear topology: all eight saved DD
builds currently record **0 armor weights**, and their front/back weapon records have
blank **WeaponType** fields. Aces therefore correctly fails closed on armor-base and
weapon-base prerequisites rather than inventing those facts from set names. Phase 14
remains active until canonical Saved Build metadata can provide or safely derive the
required armor-weight and weapon-type identities and one real saved DD build completes
the simulation gate. The current implementation now includes a read-only,
Pydantic-hardened Saved Build gear-topology evidence service plus a Builds **Review Gear
Topology** workflow. It pre-fills only uniquely proven values, narrows ambiguous choices
from canonical set/skill evidence, and keeps the remaining choice user-owned. The Phase
14 saved-build audit consumes the same service through a temporary projection and never
mutates the protected user database.
The normal Saved Build model and Builds weapon pickers now also preserve exact two-handed
subtypes (**Greatsword / Battleaxe / Maul**) as first-class values while retaining legacy
`Two-Handed` for compatibility reads. Roster imports preserve exact subtype evidence
instead of collapsing it back to the aggregate family, and the six PM U50 DD templates
now persist their already-documented Perfected Merciless Charge **Greatsword** explicitly.
This closes the application-side recording gap; the remaining Aces closeout boundary is
the build's current player-owned slot topology, not an inability of FoundryDock to store it.
Screenshot evidence can now be staged from Builds against the selected Build and Character
identities. The intake remains observational, does not change Saved Build fields automatically,
and routes the user back through Gear Topology Review for explicit confirmation.
The Builds **Review Gear Topology** dialog now also offers an explicit bulk armor-pattern
helper: the player chooses a common weight and, optionally, one named exception slot/weight.
It only fills the equipped armor selectors shown for review, does not infer which slot is
exceptional, and still persists solely through the normal reviewed Save Build path.

A same-day reference-corpus audit also found a broader canonical projection defect:
`uesp_reference_item` contained direct U51 physical set-piece evidence that had never
been projected into `gear_set_piece`. The audit denominator was **13,918** directly
evidenced physical topology tuples; **7,160** were missing from the canonical piece
table across **605** sets (**7,148 weapon tuples**, **12 armor tuples**, **0 set-name
identity conflicts**). A dry-run-first additive repair inserted all 7,160 rows on a
database copy, post-write audit found **0 missing**, and a second run remained at **0**,
proving idempotency. Perfected Slivers of the Null Arca now correctly exposes its
weapon legality instead of appearing armor/jewelry-only. The normal U51 reference
importer now projects each directly evidenced physical item tuple into
`gear_set_piece` during import so future data refreshes do not recreate the defect.

The original connected Google Sheet **Performance Mode • Sunspire HM Comp** was also
checked directly for **AAA Aces**. It confirms the current planned sets, skills, Mundus,
Champion Points, and stage swap, but it does not record an exact front-weapon subtype
or slot-by-slot armor weights. Historical PM material preserves the aggregate
**1 Light / 6 Medium** rule, medium Slimecraw intent, and a Merciless Charge Greatsword
back bar, but it does not identify which current Aetheric Lancer body slot is Light.
Those remaining values therefore stay explicit player-owned unknowns rather than being
promoted from raid convention into canonical build truth.

The **2026-10-07** status-runtime work intentionally does not manufacture hidden RNG or
claim unsupported state ordering. Successful status applications still require explicit
deterministic proc evidence. Poisoned execute scaling reads exact chronological pre-tick
target Health from the same replay ledger as ordinary/status damage; later ticks therefore
observe Health lost to earlier ticks, and the bounded replay must converge deterministically
or fail closed. Enemy-target status consequences such as Vulnerability and Breach now enter
sequence-aware target windows only after the parent hit, and reviewed caster-side
`weapon_spell_damage` consequences such as Sundered's power buff rebuild later saved-build
DD contexts through the shared timed EffectVariant projection. Those windows are also
emitted through the normal simulation runtime-window surface. The remaining status
composition boundary is limited to caller-supplied external runtime build-context authority:
FoundryDock refuses to rebuild over that authority when doing so could erase unrelated timed
state.

**Comp Maker / Optimizer ownership update (2026-09-19):** Assignments owns WHO
is responsible for required buffs/debuffs. Comp Maker owns roster construction plus HOW
those assigned chairs will supply their jobs: compatible class/build/gear/skill/provider
choices, missing-provider detection, duplicate-provider visibility, and preservation of
fixed player/class/role/gear decisions. Comp Maker must not invent new responsibility
ownership from generic coverage gaps. Optimizer starts from the completed saved Raid Plan
and proposes better provider arrangements, opportunity-cost reductions, and coverage
improvements without silently rebuilding the roster or transferring responsibility.

```text
CombatState
      ↓
Action
      ↓
Effect / Damage
      ↓
Resource Change
      ↓
State Change
      ↓
Next Action
```

**Hardened exit criteria:** BFF can model combat over time with explicit event ordering, resource/state changes, supported target behavior, deterministic replay from identical deterministic inputs, and auditable unresolved boundaries.

### Parked Live Raid integration — encounter intelligence

Route the canonical **boss encounter information and encounter timelines** into the
**Live Raid** workspace wherever that information is useful during an active run.

Target behavior:

- Live Raid consumes the active Raid Plan's selected trial / encounter context rather
  than maintaining a separate boss-data selection or duplicate encounter model.
- Surface concise boss/phase information, mechanic timing, phase transitions, add or
  priority windows, and other reviewed encounter timeline facts on the Live Raid page
  where they help raid-leading decisions.
- Reuse the existing canonical encounter/timeline services and any reviewed
  position/timeline data rather than copying encounter prose into Live Raid.
- Keep the display contextual: show information appropriate to the selected boss and,
  when an explicit current phase is available, the relevant phase/window rather than
  dumping an entire guide into the run surface.
- Live Raid remains a **consumer**, not an encounter editor. Strategy/mechanic edits
  continue to belong to their owning planning/reference surfaces.
- Do not infer live telemetry, boss health, elapsed phase, or current mechanic from the
  mere existence of a timeline. Automatic "what is happening now" behavior requires a
  real/manual runtime clock or another explicit live-state source.
- Preserve unresolved/conflicting encounter evidence as unresolved rather than turning
  it into a confident live callout.
- Prefer compact, raid-lead-readable presentation with the detailed boss/encounter
  pages remaining available for deeper reference.

**Status:** PARKED / TODO. This is a Live Raid product integration item, not a reason to
duplicate encounter truth or reopen canonical encounter ownership.

Here is the agreed division of responsibility for buffs and debuffs:

**Assignments page — WHO owns the job**

* Assign each required buff/debuff to a raid seat or player.
* Store the primary responsibility and any backup in one assignment field.
* Preserve encounter-specific responsibilities.
* Do not choose the player’s complete build or calculate whether another configuration is better.

**Comp Maker — HOW the planned team will provide it**

* Read the responsibilities from Assignments.
* Choose the classes, gear sets, skills, or other provider sources needed to satisfy them.
* Detect missing and duplicate raid-wide providers while constructing the composition.
* Respect fixed player, class, role, and gear choices.
* Attach an existing compatible build or create an explicitly unfinished draft build.
* Send planned gear and provider choices into Builds; never silently overwrite an existing build.

**Builds — exact player configuration**

* Store the authoritative gear, weapons, traits, enchants, skills, CP, food, potions, Mundus, scribing, and other loadout details.
* Record the exact source through which that build provides an assigned buff/debuff.
* Builds describe what the player is actually configured to wear and use; they do not decide the raid-wide assignment.

**Coverage — verification**

* Read the selected saved Raid Plan, its Assignments, planned gear, and exact Builds.
* Report each required effect as Covered, Conditional, Missing, Unverified, or Conflicting.
* Planned gear counts as a planned provider. If its proc or rotation condition has not been proven, show it as Conditional—not Missing.
* Show the exact provider/source in tooltips.
* Coverage is read-only and must never inject a Roster team, change an assignment, or rewrite a build.

**Team Optimization — improve an already valid plan**

* Load the completed saved Raid Plan; it does not assemble the roster again.
* Find redundant providers, weak provider placement, excessive opportunity cost, unresolved coverage, and better provider arrangements.
* Evaluate proposed changes against the entire team through the authoritative shared services.
* Every recommendation must show the current state, proposed state, expected benefit, tradeoff, affected players, confidence, assumptions, and unresolved evidence.
* It must not silently transfer an assigned responsibility or invent uptime/DPS.
* Approved recommendations create new build variants and update the Raid Plan only after explicit review.

**Rotation Builder — prove execution**

* Determine whether conditional buffs/debuffs can actually be maintained by the selected skills, triggers, bars, and rotation.
* Feed supported uptime/execution evidence back into Coverage and Optimization.
* It does not choose who owns the responsibility.

**Raid Plan — source of truth tying everything together**

The saved Raid Plan connects the encounter, seats, players, assignments, selected builds/build variants, and planned provider sources. Other pages should consume that same plan rather than constructing their own parallel team state.

In short:

**Assignments says who owns it.
Comp Maker chooses how the composition supplies it.
Builds stores the exact source.
Coverage verifies it.
Rotation tests whether it can be executed.
Optimization proposes better arrangements.
Raid Plan preserves the approved truth.**



---

# PHASE 15 · Encounter-Aware Optimization
**Status: 🟠 Active / first vertical slice**

Compare builds across DPS, burst, sustained damage, execute, uptime, sustain, survivability, positioning, mechanic compliance, support contribution, phase compression, and execution complexity.

**Prerequisite gate:** Phases 9 and 10 must be green under the hardened completion standard. Encounter-aware optimization may not consume partially reviewed encounter truth as if it were complete. Phase 12.5 may expose bounded static comparison groundwork, but temporal or encounter-outcome claims require the later rotation/simulation dependencies they actually use.

**First vertical slice (2026-10-07):** A read-only encounter outcome comparison bridge now joins explicit canonical encounter/stage scope to already-evaluated whole-plan candidate evidence. It reuses the authoritative role-aware hard gates/ranker, exposes role-output/support/sustain/displacement tradeoffs, preserves unresolved evidence/confidence, rejects cross-encounter or cross-stage comparisons, and refuses to turn deterministic candidate-id tie-breaking into a gameplay recommendation. Candidate-family ranking and recommendation staging now feed a read-only team-plan aggregator, impact summary, verdict, immutable decision record, and explicit human approval packet. The team boundary suppresses apply bundles when staged swaps collide on seat/player/exclusive-resource identity or unresolved review state; approval is cryptographically bound to the exact frozen decision evidence reviewed. A guarded Phase 15 apply bridge can now produce a revised immutable Raid Plan snapshot only when that ready packet and explicit approval still match exactly. A separate approved-persistence boundary now requires the exact reviewed source Raid Plan, creates and verifies a full user-database safety snapshot, then delegates to RaidPlanRepository optimistic-concurrency save/read-back validation. UI wiring remains separate. This does not yet constitute full build search or raid-wide optimization.

**Exact weapon-hand topology hardening (2026-10-07):** Saved Builds already persist front/back main and off hand separately, so Phase 15 required no user-database migration. A shared strict topology resolver now separates one-handed pairs, Sword + Shield, and whole-bar weapons; physical-metadata readiness requires the second hand when one-handed main identity is known; topology review can represent main/off hand separately; and metadata completion rejects hand-illegal subtypes and legacy aggregate family labels. Skill-line evidence may prove occupancy without inventing exact subtype, so Dual Wield evidence creates two explicit subtype questions rather than one vague front-weapon question.

**Real HOUAD persisted-identity witness (2026-10-07):** the uploaded canonical `foundrydock.db` was inspected read-only with SHA-256 unchanged before/after. All **36 boss-seat combinations** (3 Sunspire boss contexts × 12 seats) resolve through stable selected BuildId to exactly one reusable Saved Build with stable CharacterId and role; **0 identity problems** were found. The same database exposed an active-stage persistence defect: `predot:lokkestiiz` and `predot:yolnahkriin` were still present in `raid_plan_shared_stage_sequence` after the user had attempted to remove those phases. Predot active membership is now separated from reusable context identity and the fix was exercised against a disposable copy of the real HOUAD database: disabling both removed them from the active sequence while preserving both context rows, re-enabling Lokke restored it immediately before Lokke, and the original database hash remained unchanged.

**Current real mechanics blocker (2026-10-07):** persisted identity and the HOUAD DD weapon package are no longer the Phase 15 blocker. Read-only validation of the uploaded HOUAD database plus the reviewed team convention reduces DD physical-metadata gaps from **30 to 22**, and all remaining gaps are armor-weight questions. **Cobble, Jaded, and Pippin now have zero physical-topology gaps**: their front bars resolve to CP160 Gold dual daggers from each build's weapon/jewelry set (Nirnhoned + Flame main hand, Charged + Poison off hand), Bloodthirsty + Weapon Damage jewelry, and an Infused + Weapon Damage Greatsword back bar, with Truly Superb Gold enchant state recorded separately from item quality. Canonical Flame/Poison short labels now resolve by damage-type evidence, Ambidextrous has verified off-hand item power, and resolved Mighty/War Mage scoped DD power retires only its duplicate legacy static warnings. The next closeout gate is therefore real rotation/runtime combat evidence for one of those physically complete DDs, not weapon identity. Rik's tank Saved Build remains physically complete but still lacks an authoritative scalar tank survivability/ranking objective. Phase 15 remains Active until one real persisted encounter candidate family produces authoritative role-output mechanics.

**Cross-build canonical evidence routing (2026-10-07):** the canonical Rotation plan-evidence service is intentionally bound to one Saved Build at construction time. Phase 15 now has a read-only BuildId dispatcher that routes each candidate in a cross-build family to its own build-bound evidence provider before the shared recommendation/ranking pipeline runs. Missing provider bindings, blank BuildIds, duplicate candidate identities, and out-of-family candidates fail closed. This prevents one Saved Build's calculation context from leaking into another candidate's mechanics evidence.

**Protected real-data witness audit (2026-10-07):** a dedicated CLI now runs the persisted encounter witness against a temporary copy of `foundrydock.db`, while SHA-256 checking proves the original user database is unchanged. The audit loads only reusable Saved Builds from the strict canonical Build catalog, resolves one persisted Raid Plan encounter context/seat, and reports exact identity blockers without mutating the real database. This is an identity/provenance gate only; it deliberately does not claim the Phase 15 mechanics comparison exit criterion has passed.

**Persisted encounter identity witness (2026-10-07):** Phase 15 now has a strict read-only provenance gate for one effective Raid Plan seat. It requires an encounter-bound Raid Stage plus an explicitly persisted stable selected BuildId, resolves that Build through the canonical Saved Build authority, and verifies matching BuildId, CharacterId, Build name, and role before the seat is considered closeout-ready. Name-only build selection remains readable for compatibility but is not promoted into Phase 15 proof. This moves the remaining exit work to actual generated/evaluated mechanics evidence rather than identity plumbing.

**Generated-candidate evaluation bridge (2026-10-07):** Phase 15 can now accept a real generated whole-plan Rotation candidate family rather than requiring callers to preassemble Phase 15 evidence manually. The bridge validates stable BuildId plus encounter/Raid Stage scope before evaluation, evaluates every candidate against one explicit baseline through the canonical Rotation recommendation-evidence provider, rejects candidate/evidence identity drift, and then delegates unchanged evidence to the existing Phase 15 ranking service. It owns no new ESO mechanics and performs no mutation. The remaining closeout gate is still a real persisted Saved Build + canonical encounter execution, not synthetic family plumbing.

**Hardened exit criteria:** BFF answers which build produces the better outcome in a real canonically persisted encounter, explains why, preserves unknown/conflicting mechanics, and demonstrates the result against at least one real saved build and encounter.

---

# PHASE 16 · Explanation Engine
**Status: 🔴 Planned**

Every recommendation should expose change, expected impact, reason, tradeoff, encounter effect, confidence, and evidence.

**Hardened exit criteria:** recommendations are inspectable and defensible, distinguish modeled fact from assumption, expose provenance/confidence, and never fabricate explanations for unsupported outcomes.

---

# PHASE 17 · ESO Logs Validation
**Status: 🔴 Planned**

Use logs as a later validation feedback loop:

```text
MODEL
  ↓
Expected Result
  ↓
Observed Log Result
  ↓
Difference
  ↓
Diagnosis
  ↓
Model Refinement
```

Logs are validation/corroboration, not a substitute for authoritative static rules when those rules can be sourced directly.

**Hardened exit criteria:** log-derived observations remain attributable to specific logs/patch context, discrepancies are measured rather than patched with unexplained fudge factors, and model changes preserve canonical-source precedence.

---

# PHASE 18 · Strategy Engine
**Status: 🔴 Planned**

Evaluate safe, balanced, aggressive, and experimental strategies against roster capability, encounter risk, execution difficulty, confidence, expected gain, and failure cost.

**Hardened exit criteria:** BFF can compare practical strategies for an actual roster and encounter, explain risk/reward and uncertainty, and prefer a lower theoretical ceiling when evidence indicates a better expected real outcome.

---

# PHASE 19 · Full Raid Optimizer
**Status: 🔴 Planned**

```text
12 CHARACTERS
       ↓
12 BUILDS
       ↓
ENCOUNTER / REQUIREMENTS
       ↓
CAPABILITY ANALYSIS
       ↓
PROVIDER ASSIGNMENT
       ↓
BUILD CANDIDATES
       ↓
COMBAT SIMULATION
       ↓
EXPECTED OUTCOME
       ↓
STRATEGY OPTIONS
       ↓
RECOMMENDATION + EXPLANATION
```

**Hardened exit criteria:** a real 12-player roster can be optimized end-to-end against a canonically persisted encounter; assignments, candidate changes, simulation assumptions, strategy tradeoffs, and explanations remain auditable; unsupported data cannot silently improve the score; rerunning identical deterministic inputs yields the same recommendation; appropriate full regression and real-world validation gates pass.

### Phase 15 validation-hardening note — recommendation staging
Candidate-family ranking now feeds a read-only recommendation boundary. The recommendation carries encounter/Raid Stage provenance, expected role-output/support/sustain/displacement deltas, reasons, tradeoffs, unresolved evidence, and confidence. It may stage the existing Optimization build-swap proposal only when the canonical ranking has a safe, non-equivalent winner; it never applies or persists the change itself.

### Phase 15 validation-hardening note — candidate-family ranking
The first encounter-outcome comparison slice now extends to a read-only candidate-family ranking service. It ranks multiple already-evaluated whole-plan candidates within one encounter/Raid Stage using the existing role-aware hard gates and ordering, preserves provenance, and refuses to manufacture a winner when the top candidates are substantively equivalent. This is still not the full raid-wide optimizer; proposal/application mutation remains out of scope for this slice.


### Phase 15 validation note — 2026-10-07
Encounter-aware optimization now includes pairwise comparison, candidate-family ranking, staged per-seat recommendations, team-level conflict aggregation, read-only plan-level impact summaries, and an explicit team verdict. Plan totals are fail-closed per dimension when any staged seat lacks that evidence, and the verdict refuses a weighted magic score: tradeoffs remain `mixed`, while incomplete/conflicting/unresolved evidence becomes `insufficient_evidence`. Explicit proposal application remains the only mutation boundary.


### Phase 15 validation-hardening note — 2026-10-07
- Encounter-aware optimization now has a complete read-only decision chain: compare candidates → rank family → stage per-seat recommendation → conflict-check team plan → aggregate impact → classify verdict → freeze immutable decision record.
- The decision record embeds already-evaluated artifacts rather than recomputing them, and rejects cross-encounter/cross-stage provenance.
- Mutation remains outside this chain; existing explicit Optimization proposal/application ownership is unchanged.


### Phase 15 validation-hardening note — approved durable persistence — 2026-10-07
The reviewed decision chain now has a durable write boundary. Persistence requires the exact Raid Plan snapshot that was present during review; any intervening plan change blocks the write before mutation. Before saving, FoundryDock creates a full SQLite user-data safety snapshot and reopens it to prove the exact reviewed Raid Plan is recoverable. The canonical RaidPlanRepository then performs its existing optimistic-concurrency writer lock, revision capture, Pydantic serialization, and exact read-back validation. No Saved Build or canonical ESO reference data is mutated.

### Phase 15 validation-hardening note — Optimization UI approval boundary — 2026-10-07
The native Phase 15 Optimization page now has a dedicated encounter-decision review surface over the frozen decision/approval/persistence chain. Encounter-derived recommendations expose their verdict, confidence, reasons/blockers, and encounter/stage provenance; Approve and Persist are separate actions; stale reviewed Raid Plans disable persistence; and durable writes go only through the guarded Phase 15 persistence service with a verified `foundrydock.db` safety snapshot. Manual user-selected build swaps remain a separate explicit-edit lane rather than being mislabeled as optimizer evidence.

- Phase 15 validation-hardening: Optimization UI review now uses immutable review-session provenance, binding the exact reviewed Raid Plan digest to the frozen encounter decision through approve/reject/persist transitions.

### Phase 15 validation-hardening note — review receipt visibility — 2026-10-07
Optimization now exposes a deterministic, read-only review receipt derived from the immutable Phase 15 review session. The UI can show the exact reviewed Raid Plan fingerprint, frozen decision digest, encounter/stage scope, affected seats, human action, and verified persistence snapshot path without recomputing optimizer evidence or creating a second persistence authority.
