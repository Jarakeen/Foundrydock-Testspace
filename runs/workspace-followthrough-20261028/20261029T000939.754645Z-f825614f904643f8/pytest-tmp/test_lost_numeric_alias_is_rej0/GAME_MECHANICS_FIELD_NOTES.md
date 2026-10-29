## 2026-10-21 — Lokkestiiz flight entry and observed damage return are different signals

## 2026-10-25 — Banner Bearer and airborne NPC calibration references

The user identified the smoky blue circle in the recordings as **Banner Bearer**, with an **8 m radius**. Local ability 217699 also retains radius 800 separately from cast range. Its actor-centred aura is a more useful scale reference than assuming a Budding Seeds cast position is the ground-field centre.

Empirical fits to stable Banner buff state can suggest a per-map log-to-metre scale, but buff update timing, source replacement, missing positions and elevation prevent interpreting fit accuracy as surveyed distance precision. Keep those fits provisional and source-bound.

The user also confirmed that **Nahvi flies off to the side during Lokke**. Preserve that track, but exclude it from Lokke platform bounds and ground-marker placement. An enemy's recorded XY does not establish that it is on the arena floor.


## 2026-10-25 — Ground-targeted support radius versus caster position

Budding Seeds has an **8 m effect radius (16 m diameter)** and **28 m cast range**. These are different measurements. A visible, correctly identified circle can be a calibration reference after accounting for camera perspective.

The three downloaded reports contain 821 Budding Seeds cast events. Only 56 contain a target-resource snapshot, and a target snapshot is not itself proof of a ground-effect centre. Do not place an 8 m circle around the caster simply because the cast event includes the caster's XY. Healing recipients provide delivery observations, not the exact boundary or maximum reach. Original log XY and all uncertain samples remain preserved.


In ESO Logs export `v16hzgGWTV7BZ48f`, successful fights 22, 37 and 54 contain `cast` events with IDs `122820`, `122821`, `122822`. Existing `PerformanceRaidReviewLokkestiizBoundaryService` treats these as occurrence-specific flight-entry *signatures*, not immunity aura IDs. For fight 22, cast-relative beginnings are 20.000, 97.243 and 183.696 seconds. The first boss damage after each qualifying long gap resumes at 72.683, 161.703 and 247.165 seconds. This is a reproducible **combat-active boundary**, not a proof of the visual landing frame or exact immunity removal. The boss also flies beyond the observed player arena; dragon coordinates must not define ground-arena dimensions. Source is an offline user-provided report, not a live API witness.

## 2026-10-20 — Map stage identity and Windows paths

Raid Map stores must preserve the logical Plan and Raid Stage identity, but not use punctuation-bearing context strings such as `trash:after-lokke` directly as Windows directory names. Deterministically derive a safe map-storage key shared by editor, save/reopen and calibration consumers. Keep boss keys compatible with existing saved maps. Library sources remain immutable; map edits are plan-stage-owned copies. Live Raid is parked and not an acceptance consumer for this work.

## 2026-10-20 — Kill & Pull candidates vs authored strategy

The Kill & Pull suggestions are phase-aware *evidence candidates*, not a raid-lead-approved order. Their phase, required response, explanatory notes and source provenance must be readable individually. In particular, a named enemy fact never establishes killability or target priority without corroborating evidence. Saving is scoped to the exact plan and stage and must preserve independent Assignments fields; map persistence remains owned by the Raid Map services.

## 2026-10-20 — One-piece monster equipment is deliberate

ESO monster pieces do not require both head and shoulder to be equipped. A one-piece Slimecraw head can be an intentional setup. A metadata warning is legitimate only for an *actually occupied* slot with missing physical metadata, not for an imagined matching monster shoulder. A previously saved shoulder with the same set is distinguishable from an empty shoulder: Build editing must clear stale matching pieces when the user unchecks the two-piece option without silently clearing a different set.

## 2026-10-20 — Warning provenance, not invented readiness

Individual player warning pills must derive from existing Saved Build physical metadata, exact stage/seat Assignments and per-chair Coverage reviews. A missing source or unknown combat evidence is not proof that a buff or mechanic is absent. Coverage review is visually neutral, actionable gaps amber, and clicking a pill opens the canonical editor. Recalculate after the user saves; do not maintain an independent warning database or persist presentation statuses.

## 2026-10-20 — Copying a build must not silently switch the raid chair

Copying a saved character build creates an alternative package, not an instruction to change tonight's twelve-person plan. The selected chair can still be assigned to the original BuildId while the duplicate exists. Never let the editor visually jump to a different build without an explicit selection: this would make later edits appear attached to the wrong planned loadout. This is application assignment identity, not a combat mechanic.

## 2026-10-20 — Copied build is not a copied character

Wyrdworks must duplicate gear, bars and boss/stage overrides when a raid lead copies a build, while retaining the original character's canonical identity. A copied build requires a NEW BuildId and should not inherit Ready for Raid or source-plan/seat provenance. Otherwise a variant can silently masquerade as an already reviewed or assigned build. This is an application ownership rule, not ESO combat math.

## 2026-10-20 — Encounter target context must come from evidence, not boss switches

A creature's targetability and required response can change by phase. Generic Kill Order extraction uses reviewed structured enemy-group or explicit target facts, with phase, response, and missing/unknown evidence carried forward. Mechanic labels are frequently ability names, not monsters. Reusing narrative notes as an automatic kill list would create false targets. Nahviintaas portal Eternal Servant is a timed kill, while an upstairs survivor is immortal; preserve that distinction in structured evidence. Existing encounter research without target-shaped facts still needs evidence reconciliation, not boss-specific UI rules.

## 2026-10-20 — Nahviintaas target identity is phase-dependent

Eternal Servant is killable by the portal group in the time-shifted realm within about 90 seconds; if that mechanic fails, the upstairs threat is immortal and wipes the team. It must never appear as a generic main-arena focus target. Vigil Statue on HM is only vulnerable during the rock-casting window and requires off-tank control / interrupts. Flame Atronachs appear during execute and can be gathered for cleave. Kill-order suggestions need phase, location, response and explicit uncertainty, not just a creature name. Source-backed planning suggestions remain opt-in and must not overwrite the raid lead's saved priorities.

# ESO — Mechanics field notes

Keep the oddities. These notes are practical discoveries, not executable formulas. Follow provenance, scope and canonical owners before using them as math. New discoveries belong here in plain language; routine refactoring does not.

## Current highlights

### 2026-10-12 — Hard Mode incoming damage and defensive response exceptions (provisional)

- **DSR Twins:** The same heavy attack can have opposite undesirable consequences. A dodge triggers the boss's Seethe damage increase; a block exposes the tank to Hindered healing absorption plus Rattled. Neither `BLOCK` nor `NO ROLL` is universally correct without active debuffs and group mitigation. Source registry: `dsr_q_twins` and `dsr_nilandia` in `data/encounter_research/provisional_hm_mechanics_20261012.json`.
- **DSR Taleria:** Nilandia uses **Coral Slam** while Qcell calls the two-hit heavy **Coral Slash**. Nilandia's 30-34k blocked hit is a post-mitigation source observation with unknown tank parameters, not a universal base damage amount. Maelstrom frequency is disputed (20-second cooldown versus approximately 30-second recurrence). Keep names/values separate until ability-ID or combat-log evidence reconciles them.
- **Sanity's Edge Chimera:** Chain Lightning becomes conditionally lethal when a player receives subsequent Chain Circuit with Circuit Charge active. The guide reports more than 1.5 million damage under that condition; this is not the amount of an ordinary Chain Lightning hit. Keep the affected target, 30-second debuff and approximate 20-second repeat distinct.
- **Lucent Citadel Xoryn:** Directly checked ESO snapshot identity `encounter.id=xoryn`. Alcast documents a 60-second Fluctuating Current, required ~10-15-second handoffs, and a 90-second Overloaded Current restriction. This is a condition-specific lethal mechanic, not general Shock damage.
- **Source verification boundary:** Research packet contains 32 strictly provisional findings, now opt-in queryable through `EncounterService.provisional_research(...)`. Guide text and screenshots may support **attack naming** without validating exact attack-ID alias, timing, mitigation or current-patch damage. Negative action badges (`NO ROLL`, `NO BLOCK`, `HOLD`) need exact target and situation. Never push this provisional packet to reviewed canonical encounter facts or the Combat Engine based on text alone.


### 2026-10-11 — Video effect-timer lanes are measurable observations

In the user-provided Nightblade Yolna setup recording, the player identifies the timers **above the player's health bar** as effects on the player (such as Major Slayer), while the timers **beneath the dummy's health bar at the top of the screen** show effects on the target (such as Alkosh and Lucent Echoes). These are important visual time-series signals: later frame-level annotation can record an effect's appearance, displayed countdown, refresh, and disappearance; line these up with ability activations and damage events. Keep the two lanes distinct by **effect recipient/target**, and record timestamps and icon/label confidence. The precise positive/negative classification of an effect must come from its verified identity, not from the bar's screen position. A displayed timer is not, by itself, proof of target application, recipients, actual combat-log uptime, or damage contribution. The user's lane identification is firsthand UI context, while exact effect IDs and durations remain to be verified. Source: `USER_VIDEO_YOLNA_BLADE_20261011`.

### 2026-10-11 — A Yolna-labeled dummy demonstration is not a Yolna boss result

A user-provided Nightblade clip titled `Blade core set up - Yolna` contains dummy-combat footage and setup screens. This can help document a player's demonstrated setup, but a dummy is not the Yolnahkriin hard-mode fight: movement, target access, mechanics and support coverage can change results. Sampled video frames do not establish exact skill timing or DPS math. Source `USER_VIDEO_YOLNA_BLADE_20261011`; observational evidence only until timecoded and checked against logs.

### 2026-10-09 — Health CP, scribing, and item quality evidence

Breakfall, Fleet Phantom, and ten legacy Craft CP stars do not provide static Health-sheet stats; mapping them to their non-sheet owners prevents fake evidence gaps while retaining their mechanic-specific relevance. The Banner shorthand represents the Banner Bearer Scribing grimoire (Support), not a Bone Tyrant slot, so it must not inflate Health Avarice. Full context is retained in the discovery index.

### 2026-10-09 — Gear metadata is not combat evidence

A missing armor weight or weapon type is an actionable saved-build metadata gap and can be highlighted for bulk entry. An absent screenshot is optional evidence, not a gear defect; unknown damage math must be researched rather than guessed from an editor. Existing reviewed values must not be replaced by bulk completion.

### 2026-10-09 — Duration extension is not universal

Serpent's Disdain helps qualifying status effects applied by its wearer; it must not be treated as a generic extension to named group buffs such as Roaring Opportunist. For Brittle, check which status/application pathway actually produced the effect. Likewise, a Pillager or Nazaray set appearing on a build does not prove every teammate stood within the effect's reach at the right time. Full context is retained in the discovery index.

### 2026-10-09 — Status opportunities are not group-wide benefits

The reviewed reference snapshot separates a status effect’s target benefit from its caster benefit: Sundered’s enemy debuff and caster power are different recipients. A damage-type opportunity does not prove the status actually happened. Likewise, supplying Orb’s synergy does not prove another player accessed or activated it. Team interaction evidence keeps these separate, and an asserted condition is not execution proof. Full context is retained in the discovery index.

### 2026-10-09 — A normal support proc is not unfinished planning

Wearing Ozezan on a healer is a reasonable plan for its healing/overhealing support; using an Ultimate is an ordinary action for Nazaray, Master Architect and War Machine. The app should not turn those triggers into a repeated warning to the raid lead. It now separates expected planning support from measured execution. Full context is retained in the discovery index.

### 2026-10-09 — Green CP passives are not Champion Bar choices

Rationer and Liquid Efficiency no longer need slots: official Update 45 notes changed nine Craft stars to passives. The old Builds name list was therefore stale. Current reference data agrees. Its discipline IDs (Blue 1 / Red 2 / Green 3) differ from client UI indexes (Green 1 / Blue 2 / Red 3); treating those columns as interchangeable puts choices in the wrong group. Full context is retained in the discovery index.

### 2026-10-09 — DSR staffing evidence must stay scoped

A successful paired Reef Heart entry does not demonstrate one player completing the second Heart alone. Returning upstairs and continuing downstairs are different responsibilities, and an upstairs buff provider's availability cannot be inferred from a build or roster presence. Two- or three-player Taleria bridge staffing is the raid lead's recommendation policy, not a claim that ESO mechanically forbids solo bridges. Full context is retained in the discovery index.

### 2026-10-09 — Reef Guardian trial identity needs content scope

The imported Reef Guardian page includes overland locations even though the reviewed raid registry and persisted encounter row place `reef_guardian` in `dreadsail_reef`. Use the content-scoped trial identity and reviewed DSR evidence; do not interpret the page's mixed location text as trial positioning or merge overland health/mechanics into the trial. Full context is retained in the discovery index.

## Coverage delivery and status-only extension — 2026-10-09
Two sources of the same buff can have different reach and duration. Coverage must keep those details attached to each source rather than give the combined buff one misleading radius or timer. Serpent's Disdain's canonical status-duration modifier extends eligible statuses; Major Slayer does not inherit it. The existing EffectDurationResolver remains the authority, and related Brittle duration is not inferred. Missing radius origin, recipient access and refresh rules remain evidence gaps.

## Full discovery index

Search these retained entries for older knowledge; dates do not imply a fresh validation.

- [2026-10-09 — Health CP, scribing, and item quality evidence](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-10-09 — Gear metadata is not combat evidence](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-10-09 — Duration extension is not universal](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-10-09 — Status opportunities are not group-wide benefits](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-10-09 — A normal support proc is not unfinished planning](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-10-09 — Green CP passives are not Champion Bar choices](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-10-09 — DSR staffing evidence must stay scoped](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-10-09 — Reef Guardian trial identity needs content scope](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-27 — Crusher can be exact from a Build; Alkosh cannot be treated as one fixed number](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-27 — Minor Force is personal; Boneyard is not Minor Breach](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-26 — Runtime-state closure evidence now stays typed through the final proof gates](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-26 — Proc-history identities, cooldown state, and timed enchantment windows now fail closed](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-26 — Generated search coordinates and ceilings are typed evidence too](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-26 — Potion, Heavy Attack, and delayed-Ultimate frontiers require typed proof inputs](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-26 — Generated CP, jewelry, and passive frontiers reject coercion](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [A higher recovery threshold does not necessarily leave you with more Magicka](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-06 — Falling below a threshold does not automatically mean "heavy now"](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-06 — Ending Magicka can hide a dangerous mid-rotation dip](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-06 — Locally sensible heavy attacks can become unnecessary after replay](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-06 — Two bars can restore the same resource but offer very different heavy opportunities](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-06 — Cycle of Life is a bonus, not the reason staff heavies restore Magicka](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-06 — The best healer rotation probably should not maximize ending Magicka](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-06 — Recovery-heavy scheduling behaves like a small feedback system](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-07 — Health-triggered mechanics do not live at one fixed clock time](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-07 — Some mechanic timing belongs to the group, not just the boss](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-07 — Preparing a heal earlier can improve sustain, not just readiness](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-07 — More raid DPS can move a mechanic out of a useful prep opportunity](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-07 — Healer opportunity bands can be helpful, neutral, or actively harmful](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-07 — A complete character can have 64 attribute points that do not change the stat being maximized](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-07 — Both skill bars belong to the build, but only the active bar gets active-bar-only standing bonuses](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-07 — "Resting maximum" and "potion-active maximum" are different honest answers](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-07 — Mechanic-entry Magicka is not monotonic with raid DPS](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-07 — A cast moved inside the mechanic window cannot repair a reserve deficit that already existed before the window](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-07 — Preserving the number of casts does not preserve uptime](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-08 — A class-line slot passive can boost heals from a completely different skill line](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-08 — Two low-health healing passives can care about completely different things](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-08 — "Current tooltip" can accidentally mean next patch](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-08 — A damage-stat buff can improve healing without being a healing buff](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-09 — The same buff coverage can have very different raid costs](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-09 — An instant skill is not proof of a free rotation slot](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-09 — The skill's base price is not always what the build pays](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-09 — A zero-cost Ultimate can still spend Ultimate after it is summoned](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-09 — A blocked provider plan is not the same thing as an expensive one](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-09 — Critical Healing can exist in data and still vanish before calculation](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-09 — Supported named buffs still need optimizer scenario plumbing](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-09 — A selected potion is availability, not an active combat buff](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-09 — Extreme may discover potion families only inside an explicit potion-use scenario](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-09 — Skill-buff discovery requires an explicit pre-cast snapshot](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-09 — Triggered skill buffs require observed runtime-event proof](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-09 — Gear-proc self application must be explicit, not inferred from ally/group targeting](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-09 — Self-or-ally targeting is distinct from ally-only targeting](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-09 — Runtime condition names require explicit evidence, not interpretation](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-09 — Maximum-heal snapshots need ordered runtime history, not isolated proc events](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-09 — Extreme snapshot optimization needs one runtime-history contract](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-09 — Extreme runtime snapshots need one role-neutral CombatState projector](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-11 — An unresolved effect still has a time window](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-11 — “Every one second” may be a limit, not a timer](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-11 — A triggered heal can be credited to someone other than its trigger](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-11 — A weapon trait can matter to the rotation without changing its healing number](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-11 — A rotation snapshot must carry the transient state it is claiming to evaluate](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-12 — A buff is not proof of the specific skill that supplied it](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-13 — A Champion Point formula can still have a simple hard ceiling](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-13 — Champion Point slots are four per discipline, not four total](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-13 — Maximum stored Ultimate and maximum Ultimate-spend recovery pull in opposite directions](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-13 — “Ultimate generation” is not one interchangeable bucket](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-13 — Ultimate recipient and cast clauses outrank headline generation](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-13 — A source ceiling is not a free build bonus](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-13 — Mutually exclusive source ceilings must not be summed](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-13 — Filling Strategic Reserve can still lower Health Recovery](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-13 — `5+5+2` arithmetic does not prove a real equipment loadout](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-13 — A provider skill name is not enough when the assignment is bar-specific](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-15 — Weapon/Spell Damage scaling is not sheet power](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-15 — A parsed set line does not bound an unmapped proc](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-16 — A proc can consume a skill slot even when it is not the scored action](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-16 — “You and nearby group members” includes the set wearer](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [Basalt-Blooded Warrior bar identity matters for healing](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [Class route IDs and skill-line display names are the same identity](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [Armor Master needs the Armor ability on the scored bar](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [Beacon of Oblivion is a chosen pet state, not a bar-slot rule](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [Jorvuld's Guidance is provider-local](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [Phase 14 Comp/Raid Plan provenance](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-20 — Execute damage depends on the Health created by earlier simulated actions](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-20 — A DoT's total damage cannot be dropped onto the target at cast time](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [Follow-up — periodic damage now lands on its reviewed occurrence timestamps](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-20 — Same-timestamp DoT ticks and actions need an explicit ordering rule](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-20 — Same-instant Health changes need recipient-specific ordering evidence](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-20 — A simulator event stream needs cause before state change](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-20 — Simultaneous components from one hit should not invent component order](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-20 — Death at one action sequence ends later actions at the same timestamp](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-20 — Periodic damage stops at the requested simulation horizon](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-20 — Attempted damage is not the same thing as proven applied damage](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-20 — A DD fight simulation must start with a living target](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-20 — Ambiguous outgoing damage ordering also makes DPS incomplete](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-21 — Same-timestamp resource ordering must preserve one Health-independent sustain truth](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-21 — Sustained DPS comparisons need the same execution horizon](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-21 — Sixty-four attribute points create 2,145 legal splits before the build even starts](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-21 — A tie-capable upper bound cannot be safely pruned](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-21 — Static character-sheet maxima are not sustained-DPS ceilings](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-21 — A direct-hit ceiling is not a rotation ceiling](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-21 — Exact damage is not automatically an optimistic ceiling](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-21 — Mundus and food cannot be safely optimized for DPS in isolation](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-21 — Max-resource armor reductions are not automatically DPS-safe](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-21 — Weapon enchant identity is static; weapon enchant DPS is runtime](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-21 — Champion Point legality and Champion Point damage are separate proofs](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-21 — A legal set-count partition is not yet a legal equipped build](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-21 — An active-bar gear witness is not a complete two-bar build](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-21 — Knowing a set proc exists is not the same as proving it happened](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-21 — Named buffs fit CombatState; generic timed gear stats need another bridge](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-21 — A timed proc belongs in the exact stat snapshot, not the standing sheet](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-21 — Potion recipes can differ while the combat effect family is identical](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-21 — Passive rank search must not invent skill-line ownership](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-21 — A skill family is unique per bar; a bar position is not a DPS mechanic](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-21 — An empty skill slot is legal until dominance proves it unnecessary](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-21 — Equipped, owned, and native skill lines are different facts](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-21 — Cross-axis optimization must assemble state, not swap whole candidate snapshots](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-21 — The same skill bar can produce different finite-horizon rotations](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-21 — Light-Attack weaving is a rotation choice, not a bar-legality fact](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-21 — Potion cooldown does not uniquely determine first-use timing](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-21 — “Ultimate is affordable” and “cast Ultimate now” are different policies](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-21 — Generic DD projection and dedicated Heavy Attack damage are different authorities](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-21 — A Heavy Attack action is not proof of a fully charged Heavy Attack](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-21 — A proven maximum does not require a unique winning build](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-21 — Missing upper bounds make search slower, not permission to guess](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-21 — Independent upper bounds intersect; they do not add](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-21 — Action count can bound DPS without pretending to know the winning build](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-21 — Missing pruning evidence is not missing damage evidence](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-21 — Skill order can change damage without changing the semi-static action count](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-21 — Ultimate affordability count is a capacity bound, not a cast schedule](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-21 — A local action maximum is only a ceiling for the denominator that proved it](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-21 — Lazy frontier traversal does not shrink the build denominator](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-21 — Dominating an axis and bounding its damage are different proofs](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-21 — Late search axes must meet before they alter one build](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-21 — A coupled dominance proof should stay coupled when promoted](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-21 — Trait search starts after the physical two-bar build exists](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-21 — Wiring a finite policy family does not widen its proof](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-21 — Enumerating every legal state does not tell us how much damage that axis can add](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-21 — A downstream policy denominator can depend on the upstream mutation](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-21 — Axis lists compose only when their state transitions compose](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-21 — Exact evaluation must use the last policy-mutated plan](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-21 — Rematerializing set identity must not erase later weapon choices](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-21 — Finite-axis dominance only works when the compared action stays the same action](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-21 — A finite proof denominator does not have to be materialized all at once](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-21 — Generated choices can reuse saved-build damage authority without becoming saved builds](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-21 — A convenience search should not become a second mechanics authority](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-21 — A finite policy family can be closed while the timing continuum remains open](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-21 — When the action changes, compare the whole plan instead of pretending the action did not change](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-21 — Dynamic plan comparisons should vary the plan, not quietly vary the build underneath it](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-21 — A dynamic family adapter must carry its omissions with it](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-21 — A closed runtime family is local proof, not proof that every runtime timeline has been imagined](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-21 — A local ceiling is only a branch ceiling when the branch really is that local family](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-21 — Major Slayer support has two different raid-coverage patterns](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [Potion restore timing and Phase 4 event priority](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [Heavy Attack channel reservation discovery](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [Runtime proc chance equivalence classes](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [Expected-value critical damage is not a critical-hit event stream](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-22 — Weapon bars can contribute two set pieces in two different ways](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-22 — Champion Points can be runtime procs, not just passive numbers](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-22 — A real proc does not automatically belong in a DPS search](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-22 — Vulnerability belongs to the target, not the attacker](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-22 — Breach belongs in resistance, not Damage Taken](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-22 — Brittle joins Critical Damage before the cap](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-22 — Fixed target reductions and scaling target reductions are different evidence classes](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-22 — Unique Damage Taken can share the bucket without sharing the name](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-22 — Crusher magnitude and Crusher uptime are separate proofs](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-22 — Cooldown modifiers do not prove a base cooldown](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-22 — Missing evidence and missing math are different blockers](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-22 — A complete search tree is not a complete combat model](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-22 — Master Architect duration belongs to the Ultimate spend](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-22 — Weapon enchantments remember identity across bars](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-22 — Update 35 standardized heavy-attack resource returns](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-22 — Heavy completion and landed-hit evidence are separate facts](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-22 — Heavy Attack modifiers need patch-era provenance](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-22 — Restoration Staff base versus observed 4247 return](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-22 — Historical heavy-restoration formula exposes unresolved runtime axes](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-23 — Shared Heavy Attack uncertainty is still uncertainty](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-23 — Weapon passive ownership is not enough; subtype matters](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-23 — Ambidextrous uses the off-hand weapon's own damage](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-23 — Bow Accuracy is active-bar Critical Chance rating](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-23 — Max rank can be mislabeled when rank evidence is stale](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-23 — Two rank tooltips are not one proof](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-23 — Shared missing action costs are not neutral](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-23 — Axe passive history is contradictory enough to fail closed](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-23 — Alkosh cares about Weapon Damage when the synergy fires](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-23 — Weapon enchantments care about damage events, not merely button presses](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-23 — Weapon enchant evidence is not one all-or-nothing rule](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-23 — One hit cannot fire two weapon enchantments](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-23 — Weapon enchantments remember which weapon launched the ability](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-23 — Weapon-skill DoTs split into two enchantment behaviors](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-23 — “No proc” is a real resolved outcome](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-23 — Source ownership and cooldown readiness are separate facts](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-23 — Knowing an enchant cooldown number is not enough to simulate its timer](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-23 — One enchant proc can have more than one consequence](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-23 — One proc family can have several consequences](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-23 — Ambidextrous can contribute a decimal internally even though Weapon Damage finishes as an integer](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-23 — Oblivion weapon-enchant damage is a documented crit exception](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-23 — “Same glyphs share” and “different glyphs are independent” are different facts](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-23 — A weapon glyph is not automatically a normal skill for critical-hit rules](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-23 — Infused has two different enchantment jobs](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-23 — A glyph firing is not the same as its consequence being scored](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-23 — Trait math must not erase enchant scaling metadata](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-23 — Selected Crusher now changes exact-time target resistance](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-23 — Weapon Damage glyphs are timed stat state, not bonus damage events](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-23 — Gold weapon quality is not proof of a Gold glyph](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-23 — Infused should not inflate Decrease Health's Oblivion damage](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-23 — Proc damage has to enter the Health timeline before execute math](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-23 — Poisons suppress a weapon set, not a whole character](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-23 — Poisons use one global 10-second clock](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-24 — A class passive is not coverage unless its trigger is actually on the bar](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-24 — ESO Logs can expose the same named Brittle effect under multiple IDs](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-24 — A poison proc gets one chance roll, not one roll per consequence](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-24 — A crafted poison bottle name is not its recipe](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-24 — A poison relationship source is not automatically the numeric authority for the named effect](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-24 — The thing a poison hit is not necessarily the recipient of every poison consequence](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-24 — Modeling an equipped poison is not the same as searching poison choices](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-24 — A finite poison proc history still does not prove what the poison did](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-24 — Poison selection has to happen before enchantment runtime](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-25 — A recipe-table heading is provenance, not automatically a dilution rule](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-25 — A generated poison formula ID is not a Poison IX item label](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-25 — Poison triple duration is an effect-level fact, not safely a whole-bottle switch](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-25 — A missing “triple” marker is not proof of normal poison duration](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-25 — Assigned skills can supply conditional group coverage](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-25 — Combat Prayer and Ozezan have different coverage gates](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-25 — An unanswered two-enchant rule should not block a one-enchant build](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-25 — Thief critical rating is a flat input, not a percent](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-25 — Build baseline must reach the Crit/Pen calculator](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-25 — An unreadable poison tier row is not evidence that the tier does not exist](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-26 — A capped Crit Damage value can hide wasted Crit Damage](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-26 — Generated search proof evidence must not be repaired by coercion](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-27 — Unknown passive domains are not proof of zero DPS impact](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-27 — U50 Warden mastery effects can use new ESO Logs numeric aliases](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-27 — Passive rank selections must match the candidate being tested](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [Extreme named gear physical witness counting](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-09-28 — A good match is not a measured upgrade](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-10-01 - Rotation comparisons need matching clocks](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-10-02 — A weapon bar is not always one item](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-10-03 — A self buff is not team coverage](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-10-03 — Update 51 consolidates offensive named buffs](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-10-03 — Set-bonus coverage belongs to the piece count, not merely the set name](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-10-04 — Raid Stage changes should not wake every hidden workspace](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-10-04 — Coverage should resolve one stage plan, not 74 copies of it](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-10-04 — Planned class passives need trigger-line evidence](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [U51 Coverage denominator: Sorcery/Prophecy retired, Mending/Vexation represented](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-10-05 — Build context variants belong to the Team, not the Raid Plan title](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-10-05 — A ranked ESO Logs setup is evidence, not a complete Extreme build](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-10-05 — Support-role gear evidence can transfer across classes; class skills cannot](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-10-06 — A working engine can outlive the UI bridge that once exposed it](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-10-06 — Migration storage should be read-once, not written forever](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-10-06 — Lokkestiiz flight is boss downtime, not raid downtime](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-10-06 — Empty raid-planning state should not invent encounters](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-10-06 — Same Build name is not the same Build identity](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-10-06 — A staged Build change also needs a source snapshot](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-10-06 — Useful evidence is not automatically an eligible replacement](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-10-06 — Static capability belongs in native Optimization, not in a patch stack](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-10-06 — Aggressive Horn is Major Force, not Major Slayer](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-10-07 — Imported CP names must not be guessed into current ESO data](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-10-07 — Saved-build weapon identity was coarser than combat math](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-10-07 — Phase 14 audit split build identity from progression authority](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-10-07 — Armor weight is slot-specific combat data, not just a build-wide label](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [Phase 14 DD relevance integration — progression diagnostics must be filtered at merge time](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-10-07 - Standard DD simulation must ignore non-DD CP and environmental mitigation](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-10-07 — Mighty / War Mage are scoped power, not sheet Weapon/Spell Damage](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-10-07 — Saved-build physical metadata gaps are roster-wide, not Aces-only](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-10-07 — Set identity can prove some armor weights, but not all](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-10-07 — Exact weapon subtype remains a real DD prerequisite](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-10-07 — Scheduled potion restores are distinct from potion buff uptime](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-10-07 — Phase 14 runtime authority and reviewed Templar damage boundary](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-10-07 — Direct-damage identity does not prove damage timestamp](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-10-07 — Phase 14 DD closeout false blockers from generic simulator placeholders](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-10-07 — Missing canonical skill descriptions must remain representable](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-10-07 — Extreme shape-only feasibility must still use legal canonical identities](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-10-07 — Encounter-aware comparisons must bind the evidence to the encounter and stage](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [Phase 15 candidate-family ranking must not promote deterministic tie order into game advice](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [Encounter boss-guide timeline queries must scale with canonical timeline kinds](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-10-07 — Encounter recommendation must not confuse ranking order with permission to mutate](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-10-07 — Local optimization wins can conflict at team level](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-10-07 — Plan-level optimization totals must be complete per dimension](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-10-07 — Raid-plan optimization verdicts must not hide tradeoffs inside one score](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-10-07 — Optimization decisions need frozen provenance, not later recomputation](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-10-07 — Human approval must bind to the exact optimizer evidence reviewed](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-10-07 — Approval is not enough unless apply proves it is the same proposal](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-10-07 — Phase 15 approval must bind to the reviewed Raid Plan state, not merely the reviewed swap tuple](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-10-07 — Manual build edits and optimizer decisions are different evidence classes](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [Review-session provenance binding](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-10-07 — Review history should show frozen provenance, not reconstruct optimizer reasoning](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-10-07 — Extreme Phase 15 result wrappers must use hardened Pydantic construction](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-10-06 — A Champion Point can be fully understood without being a character-sheet stat](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-10-06 — Player Armor and monster Armor use different resistance conversion](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [Roll Dodge fatigue is proven qualitatively, not numerically](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-10-06 — U51 typed DD Champion Point evidence](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-10-07 — U51 status-effect interaction consequence boundary](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-10-07 — U51 damaging status coefficients are a separate authority from status duration](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-10-07 — U51 status damage ordinary critical-strike routing](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-10-07 — Same-instant derived damage needs parent-hit causality](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-10-07 — Status damage must replay through the same Health ledger](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-10-07 — Set name is not enough to prove armor weight or weapon type](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-10-07 — A weapon skill line can prove a family without proving the weapon](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-10-07 — Poisoned must read Health before each individual tick](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-10-07 — A status debuff starts after the hit that caused it](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-10-07 — Sundered has two different post-hit consequences](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-10-07 — Set-piece topology must include weapons, not only armor](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-10-07 — Arena-weapon prose needs a closed reviewed denominator](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-10-07 — Dreadsail Reef mechanics must stay difficulty-scoped](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-10-07 — Class identity alone is not enough to prove passive raid coverage](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-10-07 — Phase 15 candidate scope must be proven before expensive evaluation](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-10-07 — Name-only build resolution is compatibility, not Phase 15 proof](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-10-07 — Real-data identity audits should mutate only disposable copies](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-10-07 — Rotation candidate evidence providers are build-bound](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-10-07 — Predot identity is not the same thing as active stage membership](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-10-07 — Real HOUAD Phase 15 identity proof is complete; mechanics proof is not](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-10-07 — Exact hand occupancy is part of weapon identity](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-10-07 — HOUAD DD front-bar weapon convention is reviewed user evidence](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-10-07 — Saved short weapon-enchant labels need semantic damage-type resolution](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-10-07 — Item quality and glyph quality are separate HOUAD evidence](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-10-07 — Scoped DD CP power must retire its own legacy static warning](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [2026-10-08 — Nightblade dummy footage is not Clus's saved raid build](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)
- [Coverage provider identity ambiguity - 2026-10-09](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md)

Full original evidence and wording: [dated source](docs/archive/governance_2026-10-10/GAME_MECHANICS_FIELD_NOTES.md). Historical counts and completion claims apply only to their recorded checkpoint.

## Concurrent branch evidence retained

Newer shared-branch records were preserved during integration: [checkpoint f08ff6f15](docs/archive/governance_2026-10-10/concurrent_f08ff6f15/GAME_MECHANICS_FIELD_NOTES.md). This evidence includes cached Coverage/Comp handoffs and plan/stage invalidation checks; its original confidence and CI status remain scoped to that checkpoint.

## Planned support radius is not recipient eligibility (2026-10-10)

**Planning caution, not a newly established ESO mechanic:** A measured distance between Raid Map seat markers can show geometric proximity to a support ability's sourced radius. It does **not** establish that the seat is a legal target, receives the effect, is positioned there during combat, or benefits during its activation window. Preserve the separate gates for recipient eligibility, applied effect, timing, and delivery. Source: FoundryDock Support Ultimate planned-reach integration audit; confidence high for the software-evidence distinction, not independent proof of any particular ESO Ultimate behavior.

## Generic range is not necessarily an effect radius (2026-10-10)

**FoundryDock evidence limitation, not an established ability-specific ESO rule:** `InteractionSource.range_meters` currently contains a numeric range but not the targeting geometry. A distance can be a cast limit, aura radius, or another requirement depending on the mechanic. Live Raid must not label that field as an area radius without reviewed ability semantics. Confidence: high for current data-contract limitation; no specific Ultimate geometry inferred. Reference: `services/team_interaction_evidence.py` and `ui/phase15_live_raid_page.py` current branch.

## U51 Sorcerer Exploitation is group offensive penetration (2026-10-13)

Update 51 Sorcerer Exploitation grants a unique 2,974 Offensive Penetration group effect. Model it as attacker-side group penetration, separate from target-side armor reduction such as Breach, Crusher, and Alkosh. Raid-plan projections may include it only when a Sorcerer seat explicitly assumes endgame-ready passive skills; preserve that assumption as conditional plan evidence and do not stack multiple Sorcerers. Source: [official U51 patch notes](https://forums.elderscrollsonline.com/en-gb/discussion/comment/8514837), corroborated by the [current penetration calculator](https://hyperioxes.com/eso/tools/penetration-calculator). This is planned capability, not proof of in-combat application or uptime.

## Critical chance buffs stay with their personal recipient (2026-10-14)

Major and Minor Savagery are modeled as personal critical-rating buffs in the Raid Plan DD check. A Coverage assignment identifies the player expected to bring that effect; it does not make the effect group-wide. The source is retained with that player's evidence, and other DDs' critical chance is unchanged. Major Force remains a group critical-damage effect, while Brittle remains target-side critical damage taken. These projections describe the saved plan and build evidence, not live application or uptime.

### Raid Plan Publishing: authored priorities are not encounter truth (2026-10-20)
Kill & Pull Order records are saved per plan and stage in Phase15AssignmentState and are explicitly Raid Lead instructions. Encounter enemy candidates offered in the editor do not become approved enemies or verified kill sequence until manually added; the exporter must preserve that distinction. Coverage records in RaidPlan are also author assertions, not proof of actual buff/debuff uptime. Avoid exporting either as validated game mechanics.


### 2026-10-20 — Saved scribing changes must not inherit an old formula
A boss setup can name a different scribed skill without saving its full recipe. Keeping the baseline recipe beside that new name would make the build look more complete than it is. The shared resolver now retains only recipes whose saved result names match the newly selected scribing names. Missing recipe parts stay unknown. Synthetic publishing tests cover the old-recipe mismatch; this is a saved-data consistency finding, not a new claim about ESO combat math.

The reference database included in the uploaded worktree also has no exact skill-choice row named “Ice Pulsar.” Publishing therefore keeps that saved name and marks its artwork unresolved instead of borrowing a similar skill's icon. This only describes this reference snapshot; it does not establish whether the ability exists or how ice-staff effects behave in game.



### 2026-10-20 — A gold Raid Plan can differ from the reusable saved build
Auto-endgame is a plan instruction. The export previously read the reusable build without that instruction, so its gear metadata could disagree with the plan. Publishing now applies the existing plan equipment owner after boss changes: populated gear is CP160 Gold and recorded glyphs are Gold Truly Superb unless an individual exception says otherwise. It does not choose missing traits or glyph identities, or alter reusable builds. These are planned equipment values, not proof of what a player currently wears.


## Lokkestiiz Frozen Tomb role rotation — 2026-10-26

The user reports DDs temporarily leaving the stack for cages, being healed out, and returning; slower groups rotate participants. Keep the main DD route separate from temporary cage duties. The user-provided 2019 code65536 forum guide states: ground-phase tombs; 23±1s cadence (user initially estimated ~25s); 60s lockout after release, not reset by a non-wipe death; one tomb in veteran non-HM versus two in HM. It describes 2.6s activation, a 10s entry deadline, and an 8s Frozen Prison heal-to-full check; initial health loss is 70%, differing from the user-provided 75%/8–10s estimate. Preserve that discrepancy rather than promoting either into current-patch numeric mechanics. The guide recommends staggered occupancy.

Planning inference: three pairs (1a/1b → 2a/2b → 3a/3b) provide six independent HM duty seats before reusing a pair; actual eligibility must account for release times and phase duration. This is historical community guidance, not current-patch or log-event verification. Movement alone cannot prove a cage, healing release, floor, cooldown or safe path. Source: https://forums.elderscrollsonline.com/en/discussion/474066/sunspire-mechanics-guide .

## Sunspire guide acceptance — 2026-10-26

At the raid lead's request, source-backed details are now attached to each dragon through existing reviewed evidence packets. The raid lead reports no trial changes since the guide era; age alone is not an exclusion. Publication/revision dates are provenance. The Yolnahkriin packet retains the disagreement over Focused Fire blocking. Nahviintaas meteor onset and the existing execute label remain distinct source claims. Automatic eligibility and event detection remain separate implementation work.

## Raid-lead Lokke route conventions

User-confirmed teaching sequence: ground DD stack stays on Lokke while 1–2 cage DDs leave, heal out and rejoin. Cage A is the entrance-side cage (bottom walkway on the dragon-right artwork), B the farther cage. For flights 1/3 the DD group can begin at either entrance/exit, cleave atronachs while moving to the opposite end (including the opposite cliff edge), stack near middle, then spread to house stacks. Flight 2 instead stacks middle for Barrier and goes directly to houses. Houses are two squares of four DDs between two west/left-side healers and Lokke on the right; healers face toward him. These are the raid lead's tactics and orientation, not inferred event timestamps or newly surveyed marker coordinates. Diagram A1–A4/B1–B4 are independent teaching slots, not a remapping of CrutchAlerts IDs.


## Lokkestiiz ice cage role eligibility and off-tank convention — 2026-10-27

Raid-lead observation: **any of the 12 players can take an ice cage**, including either tank, either healer, and all eight damage dealers. The off-tank (OT) often has no competing task during cages, so assigning the OT is a normal practical strategy, not an exceptional workaround or a mandatory encounter rule. The previous shorthand saying only cage DDs leave the stack describes one draft route plan, **not a mechanical eligibility restriction**.

Implementation guidance: treat `ice_cage_1a`, `ice_cage_1b`, `ice_cage_2a`, `ice_cage_2b`, `ice_cage_3a`, and `ice_cage_3b` as role-agnostic, independently assignable encounter duties; `role: "dd"` on older Workshop annotations is historical presentation metadata, not an eligibility filter. Raid Plan should bind each duty to a roster seat or player without rewriting the packaged source geometry. Recommend the available OT where appropriate; warn, but do not hard-block, when the selected player has a simultaneous boss-tanking, healing, or other critical obligation. Check known ice-cage lockout and rotation constraints separately from basic role eligibility. The historical guide's numerical timing remains advisory until corroborated with current evidence.

**Provenance/confidence:** direct raid-lead experience, high confidence as a team-planning convention; not independently verified as a universal mechanical rule in current-patch telemetry. Retain conflicting historical strategies and distinguish assignment recommendation from validated game mechanics.

## 2026-10-27 — Lokkestiiz variable spawns and flight-specific strategy

Raid-lead correction: ice cage and atronach spawn positions vary. A schematic path is a generalized response to actual enemy positions, not a fixed route or predicted spawn location. Cage markers express independent duties. Any role may take a cage; the off-tank often takes one when available. Eligibility/lockout still needs encounter evidence, not role-based assumptions.

The raid lead describes these distinct strategies: Flight 1 crosses entrance-to-exit or reverse, kills Storm Atronachs, then the tank pulls Ice Atronachs into the lightning circles left behind; gather at one chosen location for Barrier, then house stacks. Flight 2 has an earlier breath: Barrier gather, house stacks, then clear atronachs as above. Flight 3’s breath is intermediate: clear some atronachs, Barrier gather, house stacks, then clear the rest. Gathering need not be a universal fixed middle point. These are user-confirmed strategy instructions, not proof of every pull’s execution or exact current-patch timings.

Raw ESO Logs report v16hzgGWTV7BZ48f contains timestamped actor-39 hitPoints/maxHitPoints samples for pulls 22/37/54; movement-only bundles omit health. First sampled crossings of 80/50/20 percent are correlation anchors, not exact cast/flight start times. Different atronach event positions support adaptive-route teaching; movement alone cannot confirm target, intent, cage occupation or successful healing/release. See docs/validation/LOKKE_PACKAGE_20261027.md.

2026-10-27 clarification for map navigation: Lokkestiiz’s 20% takeoff is Flight 3. Ground 4 follows that flight; do not map the 20% flight selection directly to Ground 4. These package labels describe the established encounter sequence, not automatic detection of observed movement.

2026-10-27 raid-lead clarification: outside ice cage duties, damage dealers are intended to move as a group. Present one generalized DD route per main phase; individual recorded deviations are observed execution, not separate planned strategies. Cage departures remain independent role-agnostic duties. Bundled timeline Barrier and Storm Fury cast/begincast timestamps are observed events. Teaching focus changes around those anchors are authored guidance and do not prove Barrier recipients, actual house occupancy or exact movement intent.

## 2026-10-27 — Nahvi portal duty correction

Raid lead reports that an Eternal Servant appearing upstairs means the portal group has failed and the team is about to die; they describe him as unkillable in that situation. Do not offer a planned upstairs Eternal Servant kill/handling assignment. Portal participants vary by team; do not infer the current plan's three volunteers or reference pull portal identities from player movement alone. Keep three independent portal duties unassigned until the raid lead binds them. This correction concerns the upstairs failure state and does not automatically rewrite historical guide claims about enemies fought in the portal.

Nahvi reference kill 44 has sampled HP anchors at 90/80/70/60/50/40/33/31 percent. They anchor health-band playback, not confirmed portal entry, takeoff, landing, success or specific intent. Reviewed 33% meteor onset and 31% execute labels remain separate; other ability descriptions may use 30%. The first schematic does not reconcile those claims into one universal rule or infer lower-floor geometry.

## 2026-10-27 — Nahvi statue blasts, portal reference team and orientation

Raid lead confirms that reference actors 154, 156 and 8 are the portal DDs in the current Nahvi playback. This identification is scoped to report v16hzgGWTV7BZ48f, fight 44; it does not assign the current Raid Plan roster or identify their exact entry/exit times. Main-group route medians exclude those actors; their original samples remain visible in playback.

Raid lead identifies the room-wide blast at about 1:42 and says upstairs players must hide behind a statue beforehand on all three add flights. Corresponding observed Fire Storm casts in the selected pull are 102276, 194580 and 288448 ms; their begin-casts are 88499, 180830 and 274622 ms. These anchor advance statue-cover guidance. The earlier opening Fire Storm at 32337 ms is retained separately rather than counted as one of these three add-cycle blasts. A cast timestamp alone does not prove cover, survival or safe recovery.

Raid lead chooses Nahvi-at-top orientation to match the strategy map and describes his grounded visual body as occupying almost half the arena. The teaching overlay uses an approximate upper-arena body reference; it is not a measured collision/hitbox/breath boundary. Original Workshop art is preserved. Alignment, statue occlusion geometry and separate portal-floor projection remain unverified.

## 2026-10-28 — Raid Plan map geometry observation (UI, not encounter math)

Sidebar expansion/collapse changes the map column width while the QGraphicsView uses square height-for-width sizing; its previous `KeepAspectRatioByExpanding` fit mode could crop edges when the view rectangle and image differed. The Obsidian preview showed the image and playback controls not fitting together in the visible viewport when the rail collapsed. Switched to `KeepAspectRatio` for full artwork containment, but viewport-height/responsive layout behavior still requires native Windows screenshot validation. Do not treat this as a combat or boss-position calibration change.

2026-10-28 native follow-up to the map geometry observation: image containment alone did not solve the viewport problem. At Windows scaling, the original Obsidian canvas grew from 548px to 627px when the sidebar collapsed in a 752px-high viewport, while playback controls were omitted from the inline height-for-width report. The experiment now holds a 467px square in both states, including playback below it, by budgeting visible controls and using expanded-sidebar width as the stable ceiling. Full mechanics descriptions remain content-sized below the map and scroll normally; screenshots use synthetic description text solely for layout validation. These are UI measurements, not encounter units, observed player positions or revised calibration. No combat rule, coordinate payload, spawn/route evidence or source artwork was changed.
