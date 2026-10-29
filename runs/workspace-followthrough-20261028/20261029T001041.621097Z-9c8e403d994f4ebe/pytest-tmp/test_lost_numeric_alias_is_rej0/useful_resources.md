## 2026-10-21 — Offline Lokkestiiz reference movement evidence

## 2026-10-25 — Banner Bearer calibration reference

- https://www.btvtools.com/database/skills/alliance-war/support/banner-bearer — ability reference showing 8 m radius; corroborates the user's identification of the smoky blue ring.
- https://eso-hub.com/en/skills/alliance-war/support/banner-bearer — 8 m radius and scribing context. Useful corroboration, not an independent measurement of the supplied artwork or proof of recipient delivery.
- Local API map IDs 1502 (Cloudrest), 1649 (Sunspire), 2165 (Twins), 2183 (Reef), 2179/2180 (side bosses) are preserved in map metadata and empirical-fit receipts under `archives/eso_logs`. The Sunspire video matches the September 4 report segment despite its August 29 filename; health-based alignment evidence is retained locally.


## 2026-10-25 — User-supplied trial log/video calibration corpus

- Dreadsail Reef: https://www.esologs.com/reports/6h4DjY8zNAxKMb2W — 32 fights, 1,644,585 downloaded events.
- Sunspire: https://www.esologs.com/reports/v16hzgGWTV7BZ48f — 78 fights, 2,431,491 events; August 29 and September 4 sessions (Eastern) must remain distinct.
- Cloudrest: https://www.esologs.com/reports/4GfDcwZYAqbTNHx3 — 17 fights, 468,625 events; user identifies +3 and Z'maja arena scope.
- Budding Seeds reference: https://esoacademy.com/skills/budding-seeds/ — corroborates 8 m radius versus 28 m cast range; community reference, not patch-independent formula authority. User also confirmed 8 m radius; local ability data stores separate radius/max-range values.

Raw pages/player details/master actor and ability data, final-cursor receipts and page hashes are in the local `archives/eso_logs` evidence library, outside the committed source changes. User videos remain at their original Downloads locations. Logs do not guarantee complete original recording or exact ground-target centres. Sampled video frames have been inspected; exact cast/video alignment and new arena calibration remain pending. Do not upload raw player data or promote inferred mechanics automatically.


- **Source key:** `ESOLOGS_REFERENCE_LOKKE_V16HZG_20261021`; **report URL:** https://www.esologs.com/reports/v16hzgGWTV7BZ48f; **source:** user-provided offline `phase13_lokkestiiz_v16hzgGWTV7BZ48f.json`; **uses:** successful fight references (22, 37, 54), recorded player positions, flight-entry cast timestamps and boss-damage resumption. **Confidence:** high for exact supplied log contents, medium for generalized encounter timing and identity; source data is observed execution, not a reviewed game-mechanic formula. **Limitations:** public report/API accessibility unverified in this increment; damage-return is not necessarily visual landing or immunity expiry; coordinates uncalibrated and add identity provisional. Encounter ID 43 / difficulty 122 are exported report values.

## 2026-10-20 — Nahviintaas Kill & Pull research

- **Official ESO forums community Sunspire mechanics guide** — https://forums.elderscrollsonline.com/en/discussion/comment/7372044 — Useful for portal-team Eternal Servant timing, channel, interrupts and HM distinction. **Confidence: medium-high for documented encounter behavior, community-authored rather than game code; patch recheck required.**
- **Xynode Sunspire guide** — https://xynodegaming.com/eso-guides/allaboutmechanics/eso-trial-guides/sunspire/ — Useful for Eternal Servant portal kill and immortal upstairs failure. **Confidence: medium, narrative guide not canonical formula source.**
- **Alcast Sunspire guide** — https://alcasthq.com/eso-sunspire-trial-guide/ — Useful for HM Vigil Statue vulnerability and Flame Atronach execute behavior. **Confidence: medium, tactical descriptions require encounter-specific verification.**

- **ESO Logs v2 API / GraphQL** — https://www.esologs.com/v2-api-docs/eso/ — Primary source for report fight metadata, playerDetails, tables, graphs, and raw combat events used by FoundryDock performance review tooling. **Confidence: high for API field/schema contracts; observational log data still reflects the uploaded combat session and should not be treated as authoritative game-formula documentation.**

# Useful ESO Resources

## 2026-10-12 — Provisional trial Hard Mode encounter research

- **Source key:** `HM_RESEARCH_PACKET_20261012`; **checked:** 2026-10-12; **local inventory:** `data/encounter_research/provisional_hm_mechanics_20261012.json`. Thirty-two source-backed *provisional* encounter observations, with named attacks, difficulty, thresholds, defensive responses, conditionally lethal mechanics, and unresolved conflicts. Not promoted to the Encounter Engine or production ESO database.
- **Source keys `DSR_QCELL_TWINS`, `DSR_QCELL_REEF`, `DSR_QCELL_TALERIA`:** [ESO-Hub Twins HM](https://eso-hub.com/en/guides/Dreadsail-Reef-Guide/boss-1-lylanar-and-turlassil), [Reef Guardian HM](https://eso-hub.com/en/guides/Dreadsail-Reef-Guide/boss-2-reef-guardian), [Taleria HM](https://eso-hub.com/en/guides/Dreadsail-Reef-Guide/boss-3-tideborn-taleria). **Use:** published HM mechanics and response candidates. **Confidence:** medium for guide-described behavior; no direct current-patch log witness. Preserve contradictions with Nilandia's saved veteran guide.
- **Source keys `SE_ALCAST`, `LC_ALCAST`, `LC_DODOS`:** [Sanity's Edge](https://alcasthq.com/eso-sanitys-edge-trial-guide/), [Lucent Citadel](https://alcasthq.com/eso-lucent-citadel-trial-guide/), [Lucent Citadel HM strategy](https://dodos.fun/lucent-citadel/). **Use:** difficulty-scoped thresholds, kill conditions, debuffs and timing candidates. **Confidence:** medium; game-update applicability requires review.
- **Source keys `OSSEIN_WONDERNUTS`, `OSSEIN_COMMUNITY`:** [Jynorah/Skorkhif HM video description](https://www.youtube.com/watch?v=8kMBYYHHc8I), [Shapers of Flesh HM video](https://www.youtube.com/watch?v=TsN8N2yiiJI), [Ossein Cage time-trial community research discussion](https://www.reddit.com/r/elderscrollsonline/comments/1l77d2l). **Use:** further audiovisual and numerical-damage research. **Confidence:** medium for explicitly stated video-description warnings; unverified for unseen video frames and uninspected spreadsheet data. Never mark a named attack screenshot-verified until the actual screenshot has been examined.
- **User-owned source archive:** `data/encounter_research/strategy_archive_20260903_manifest.json` references Nilandia's vDSR and vSE guides by SHA-256. **Use:** veteran encounter details and HM differences for vSE. **Limit:** the vDSR guide explicitly excludes HM mechanics. Source archive not re-imported.

Source registry: retain every distinct URL, use, confidence and version/context. A repeated URL with different claims is one source supporting multiple findings, not grounds to discard evidence. New entries need a stable source key, URL, use, source kind, confidence, checked date/update, limits and linked finding/ID/tag where applicable.


A working source registry for BFF / FoundryDock research and combat-math validation.

The purpose of this file is not merely to collect links. Each source should say what it is useful for and how much confidence we should place in it before turning information into hardcoded game math.

## 2026-10-11 — User-supplied Yolna Nightblade video observation

- **Source key:** `USER_VIDEO_YOLNA_BLADE_20261011`
- **Source:** [Twitch VOD 2898449631 at 00:17](https://www.twitch.tv/videos/2898449631?t=0h0m17s); user-provided offline file `Highlight_ Blade core set up - Yolna.mp4` (214.932 seconds; SHA-256 `c60916ae02caf1e56eeec4872e550949f73816f0d3f71909be012f77f74a4a58`).
- **Useful for:** visual review of Nightblade action bars, dummy-combat sequence and visible setup screens in the context labeled Yolna; comparison with subsequent ESO Logs and exact saved-build data.
- **Confidence:** high that this particular recording exists and has the stated file identity/duration; **low for any quantitative combat mechanics, exact ability identity, rotation timing, DPS, boss-specific encounter effectiveness, or patch-version claim** without detailed video annotation and corroborating telemetry.
- **Limitations:** the clip was initially reviewed through sampled frames, not a complete frame-by-frame annotation. Dummy combat is not observed Yolnahkriin boss combat. No combat-math constant, skill coefficient, or optimizer recommendation may be changed on the basis of this clip alone.
- **Intended owner:** existing Combat/Rotation evidence research, reviewed through `services/foundry_intelligence_service.py` before any engine consumer uses a finding. **Status: observational intake; not mechanically validated.**

## 2026-10-09 — Normal support-proc planning references

[Ozezan the Inferno](https://eso-hub.com/en/sets/ozezan-the-inferno), [Nazaray](https://eso-hub.com/en/sets/nazaray), [Master Architect](https://eso-hub.com/en/sets/master-architect), [War Machine](https://eso-hub.com/en/sets/war-machine). Checked 2026-10-09 against the existing reference set identities and piece thresholds. Useful for trigger relationships: healing/overhealing support, Ultimate-based debuff extension and Ultimate-based Major Slayer. Confidence: high for current tooltip descriptions as corroboration of reference data; not official patch notes or observed team performance. The live pages list U51 content but do not independently establish a historical U51 change. No tooltip values were hardcoded. Covered-for-planning expectations must not imply guaranteed recipients, proximity, uptime or execution.

## 2026-10-09 — Craft Champion Point slot eligibility

- [Official PC/Mac U45 v10.3.5 patch notes](https://forums.elderscrollsonline.com/en/discussion/674341/pc-mac-patch-notes-v10-3-5-fallen-banners-dlc-update-45) and [Bethesda support explanation](https://help.bethesda.net/app/answers/detail/a_id/69237): primary, high confidence for the nine Craft stars converted to passives, including Rationer and Liquid Efficiency. Useful for rejecting stale pre-U45 slot choices in Builds. Does not establish purchased points, effect magnitude, or a complete future-patch catalog. Current numeric slot eligibility remains reference-data-owned; no database rewrite was performed.

## Source confidence guide

- **Primary / reference-grade** — suitable for establishing raw IDs, client/API behavior, canonical exported data, or other facts that can anchor implementation.
- **Validation / corroboration** — useful for independently checking an interpretation or finding mechanics/data, but should normally be confirmed against a primary source or in-game observation before hardcoding.
- **Historical / contextual** — useful for understanding mechanics and formulas, but patch age must be checked before using numerical values.

---

## Primary / reference-grade

### ESOUI source mirror
https://github.com/esoui/esoui

**Use for:** ESO client UI source, Lua/API usage, events, constants/enums, skill-bar behavior, crafted/scribed ability handling, equipment state, character-stat presentation, and other client-facing behavior.

**Notes:** Default branch is `live`. Prefer this when the question is "how does the ESO client/UI expose or represent this?"

### ESOUI API / developer discussions
https://www.esoui.com/forums/

**Use for:** Client API behavior that is not obvious from signatures alone, especially `GetUnitBuffInfo`, `EVENT_EFFECT_CHANGED`, effect type, status-effect type, ability IDs, stack counts, timing, and known API naming quirks.

**Confidence:** Primary / reference-grade when the explanation comes from ZOS staff; otherwise validation / corroboration.

**Notes:** `GetUnitBuffInfo` / `EVENT_EFFECT_CHANGED` expose timing, stacks, effect type, ability type, status-effect type, and ability ID. Do not assume the legacy `buffType` string is a real `BuffType` enum; ZOS staff documented that it is a poorly named legacy/debug value. Use the actual typed returns and live source definitions instead.

### Official ESO patch notes archive
https://forums.elderscrollsonline.com/en/categories/patch-notes

**Use for:** Versioned skill/passive changes, named-buff changes, rank-dependent durations, developer-stated mechanic changes, and establishing when a rule entered or left the live game.

**Confidence:** Primary / reference-grade for the documented change history. Pair with current live data or in-game validation when proving that an old rule still survives unchanged in the active update.

**Notes:** Especially useful when a current third-party tooltip has already moved to PTS/future-patch data. Record the exact patch/update being cited instead of treating the newest visible wording as timeless truth. Update 51 is a critical version boundary for named effects and Alchemy: Brutality absorbs Sorcery, Savagery absorbs Prophecy, and Vexation is introduced as Mending's healing-done reduction counterpart.

### UESP ESO Log Collector source repository
https://github.com/uesp/uesp-esolog

**Use for:** Auditing how UESP derives and exports ESO Log Collector tables, including `minedItemSummary` field selection, version suffixes, raw-data provenance, and whether a field exists upstream before FoundryDock imports it.

**Confidence:** Primary / reference-grade for UESP's own export implementation; it is evidence about the UESP data pipeline, not direct proof of an ESO combat mechanic.

**Notes:** The current `createMinedItemSummary.php` implementation includes enchant name/description among summary fields and does not expose a weapon-enchantment cooldown field. Treat imported item/enchant identifiers as provenance/lookup data unless their game-mechanic meaning is separately proven; do not infer an internal cooldown from an item-link or default-enchant identifier.

### UESP ESO Log Collector
https://esoitem.uesp.net/viewlog.php

**Use for:** UESP datamined / ESO Log Collector data exploration, IDs, game-data records, and provenance checks.

**Notes:** Prefer exported/raw records over manually transcribed values when available. Record game update/API version/retrieval date whenever the export provides them.

### UESP skill coefficient export
https://esolog.uesp.net/exportJson.php?table=skillCoef

**Use for:** Canonical raw skill coefficient records used by the Phase 3 tooltip/effect pipeline.

**Notes:** Coefficients are raw inputs, not complete tooltip formulas. Preserve coefficient provenance and do not treat regression metadata as a gameplay multiplier.

### UESP Scribing
https://en.uesp.net/wiki/Online:Scribing

**Use for:** Grimoires, Focus/Signature/Affix script catalogues, Grimoire compatibility, scribing-system rules, resulting-skill naming behavior, and character/archive behavior.

**Notes:** Particularly useful for the Scribed Skills builder. Compatibility between a script and a Grimoire does not by itself prove every three-script combination is legal; some combinations have additional exclusions.

---

## Runtime / combat-event validation

### LibCombat API
https://github.com/Solinur/LibCombat/blob/master/docs/API.md

**Use for:** Runtime combat-event semantics, damage/healing events, buffs/effects, resources, combat state, weapon swaps, skill timing, and ability IDs exposed during combat.

**Confidence:** Validation / corroboration.

**Notes:** Excellent for checking whether BFF's combat-state/proc/uptime model corresponds to observable game events. It is an addon library built on ESO APIs, so use ESOUI/client APIs as the more foundational source when the two layers need to be distinguished.

### ESO Logs
https://www.esologs.com/

**Use for:** Real-run encounter timelines, cast/event ordering, target patterns, mechanic cadence, add timing, role behavior, and checking whether a proposed strategy description matches what successful groups actually do.

**Confidence:** Validation / runtime corroboration.

**Notes:** Excellent for filling or validating Encounter-page timelines after mechanic identity is known. Logs show what happened in a run, not necessarily the complete game rule. Use multiple representative logs before treating cadence or target patterns as general, and reconcile patch/version differences.

### BTV Tools
https://www.btvtools.com/

**Use for:** ESO Logs analysis, buff/debuff uptime, crit and penetration analysis, Z'en/Heat Shock stack tracking, roster planning, top-log player-meta comparisons, calculators, and searchable ESO skills/sets/buff data.

**Confidence:** Validation / runtime and build-practice corroboration.

**Notes:** Particularly useful for comparing FoundryDock's Performance, Comp Maker, Rotation, and support-coverage outputs against an independent player-facing implementation. BTV Tools can import specific ESO Logs fights, exclude boss downtime, inspect group coverage over time, and build trial rosters from logged clears. Treat its derived calculations and provider relationships as corroboration rather than shared canonical truth until reconciled against primary data, official patch history, or FoundryDock's reviewed mechanics layer.

---

## Calculators / independent cross-checks

### ESO Decoded tools
https://esodecoded.com/tools

**Use for:** Independent cross-checks of traits, glyphs, Mundus values, stats, foods, sets, Champion Points, arena sets, and other build/math references.

**Notes:** Useful for finding discrepancies and sanity-checking results. Check the tool/data date before using numerical values as current-game truth.

### ESO-Hub skill pages
https://eso-hub.com/en/skills

**Use for:** Current readable skill-line rosters and tooltip wording when reviewing class, weapon, guild, and world skill/passive families.

**Notes:** Useful for confirming the visible passive roster and effect wording, but the site may expose PTS/future-update values before that update is live. On 2026-09-23, Update 51 was still scheduled for September 28 while current ESO-Hub weapon pages already reflected the U51-facing tooltip set. Always reconcile patch-sensitive values against the live update boundary and official notes before hardcoding combat math.

### UESP raw ESO Character Build Data
https://chat.uesp.net/esobuilddata/

**Use for:** Raw character-build snapshots containing skill/passive names, ranks, ability IDs, and rendered tooltip values that can corroborate current passive wording and rank-specific magnitudes.

**Notes:** Useful for cross-checking a passive against FoundryDock's imported canonical data. Individual build records may be old, so compare multiple records and a current source before promoting patch-sensitive values. For Bow Accuracy, multiple UESP records show Rank 2 at 1314 Critical Chance rating and Rank 1 at 657; ESO-Hub currently reports the same values.

### UESP Lifesteal mechanics page
https://en.uesp.net/wiki/Online:Lifesteal

**Use for:** Readable Minor Lifesteal provider history, tooltip wording, affected-target semantics, and candidate cadence/ownership claims that can be tested against ESO Logs or live combat events.

**Confidence:** Validation / historical corroboration.

**Notes:** The page currently describes attackers receiving 600 Health every 1 second while damaging an affected enemy, but its revision and provider history cross multiple game updates. Use it to frame runtime-evidence questions, not to promote a cooldown, event owner, or numeric heal rule without current-version log/client validation.

### ESO-Hub Buffs & Debuffs
https://eso-hub.com/en/buffs-debuffs

**Use for:** Enumerating current named-effect providers across skills and sets, checking readable Major/Minor effect values, durations, targets, and provider relationships.

**Notes:** Particularly useful for discovering missing provider relationships for Combat Reference. Treat provider enumeration as research candidates until reconciled against official patch history, canonical game data, or reviewed BFF relationships. Do not copy current provider lists directly into canonical registries without review.

### ESO-Hub Status Effects
https://eso-hub.com/en/status-effects

**Use for:** Status-effect families, associated damage types, proc-chance categories, readable status-effect behavior, and candidate values/durations that need canonical review.

**Notes:** Useful for driving the `Not modeled` gap queue. Current page lists Burning, Chilled, Concussed, Diseased, Hemorrhaging, Overcharged, Poisoned, and Sundered with their associated damage types and proc-chance categories. Cross-check numerical/status behavior against patch notes, client data, or combat evidence before promoting it to canonical truth.

### ESO-Hub set pages
https://eso-hub.com/en/sets

**Use for:** Current readable gear-set tooltip wording, including set-trigger conditions, cooldown/lockout wording, target descriptions, and duration modifiers such as Jorvuld's Guidance.

**Notes:** For U50 Jorvuld's Guidance, the five-piece tooltip was rechecked 2026-09-10 and states a 40% duration increase to Major buffs, Minor buffs, and damage shields applied by the wearer to self/allies while in combat. Preserve patch/version provenance and reconcile against primary game data before broadening hardcoded semantics.

### ESO-Hub trial guides
https://eso-hub.com/en/guides

**Use for:** Boss-by-boss trial strategy, health-percentage transitions, hardmode differences, target counts, common handling, role responsibilities, add priority, portal/side-team mechanics, and raid-lead callouts for Encounter-page strategy/timeline backfill.

**Confidence:** Validation / gameplay-practice corroboration.

**Notes:** Prefer authored long-form trial guides over generic zone pages. These are particularly useful for filling reviewed Encounter-page strategy when canonical structural data is sparse. Do not treat every numerical statement as immutable game truth: reconcile defensive properties, exact target counts, and patch-sensitive timings against official patch notes, UESP/client data, Combat Alerts, or logs. Dreadsail Reef already demonstrates why: current guide prose and official patch history disagree on Rapid Deluge blockability.

### ESO-Hub Scribing Simulator
https://eso-hub.com/en/scribing-simulator

**Use for:** Scribing combination exploration and a practical UX/reference model for Grimoire + Focus + Signature + Affix selection.

**Notes:** Useful for checking names and combinations against the UESP compatibility catalogue. Do not make it the sole source for hardcoded combat math.

---

## Gameplay / raid-practice references

### Xynode Gaming
https://xynodegaming.com/

**Use for:** Gameplay explanations, encounter handling, role expectations, build context, and organized-player practice that can help distinguish game-engine possibility from how experienced groups actually play.

**Confidence:** Validation / gameplay-practice context.

**Notes:** Useful for Encounter-page strategy, Field Notes, and practice corroboration, not as sole authority for canonical combat math. Search results may be less indexable than ESO-Hub or official sources, so use targeted page retrieval when a specific mechanic or encounter is under review.

### The Tank Club
https://thetankclub.com/game/the-elder-scrolls-online/

**Use for:** Tank-specific trial and dungeon strategy, main-tank/off-tank role division, boss positioning and facing, add ownership, taunt swaps, mitigation choices, survivability, support-set context, and practical organized-group tank play.

**Notes:** Particularly useful when Encounter-page research needs to answer who tanks what, where an enemy should be positioned, when tanks swap, or how experienced tanks handle a mechanic in Veteran/Hard Mode. The site is actively maintained and includes current 2026 tank builds plus dedicated trial tank guides. Treat tank strategy and role practice as corroboration rather than canonical mechanic math; reconcile exact timings, target counts, damage types, and patch-sensitive mechanic properties against official notes, UESP/client data, or logs before promoting them to shared mechanics truth.

### Ninja Pulls
https://www.youtube.com/@NinjaPulls

**Use for:** Current ESO trial guides, boss/mechanic breakdowns, trial preparation, DPS and support practice, class/system explanations, and organized-group gameplay examples.

**Notes:** Especially useful for newer encounter guides and for comparing FoundryDock's raid-lead explanations against concise player-facing mechanic breakdowns. Recent material includes dedicated trial-guide, trial-prep, and mechanic-focused videos. Video publication date and game update matter; corroborate exact numerical properties against official notes, UESP/client data, or logs.

### SeaUnicorn
https://www.youtube.com/@SeaUnicorn

**Use for:** ESO gameplay footage, raid/trial demonstrations, positioning examples, mechanic execution, and player-practice corroboration when a visual example is more useful than written prose.

**Notes:** Use encounter-specific videos as visual evidence of how groups execute mechanics, not as sole authority for exact combat rules or patch-sensitive numbers. Record the video date/update when using it as encounter evidence.

### FaceheadMcGee
https://www.youtube.com/@FaceheadMcGee

**Use for:** ESO raid/trial gameplay, mechanic demonstrations, positioning and role execution, and visual cross-checks for Encounter-page strategy and Raid Map research.

**Notes:** Treat footage as observed player practice. It is particularly useful for checking what a mechanic looks like and how a successful group handles space, movement, stack positions, and role assignments. Pair exact mechanic claims with primary or reviewed textual evidence.

### Temfoolery
https://www.youtube.com/@Temfoolery

**Use for:** ESO dungeon and trial strategy videos, mechanic demonstrations, positioning, role execution, and organized-group gameplay examples that can help corroborate Encounter-page strategy research.

**Notes:** Use encounter-specific videos as observed player practice, especially when researching Veteran/Hard Mode execution and spatial handling. Record the video date/update and corroborate exact timings, target counts, damage properties, and other patch-sensitive mechanics against official notes, UESP/client data, or logs before promoting them to shared mechanics truth.

### Game-Maps.com ESO maps and walkthroughs
https://game-maps.com/ESO/The-Elder-Scrolls-Online.asp

**Use for:** Zone and dungeon geography, entrances, landmarks, boss-room context, route planning, and visual positioning references that can help build or validate Encounters-page Raid Maps.

**Confidence:** Validation / positioning corroboration.

**Notes:** Use this for spatial context, map labels, and route/layout research rather than combat-math authority. Pair encounter-specific positioning claims with reviewed strategy sources or in-game/log evidence before treating them as required raid handling. The site maintains broad ESO map coverage and links current and legacy content maps.

---

## Visual / UI asset references

### Game-icons.net
https://game-icons.net/

**Use for:** Generic game/UI iconography and visual-reference ideas for non-proprietary FoundryDock interface symbols, mechanic categories, status markers, and prototype/mockup concepts.

**Confidence:** Visual-reference source only; not a gameplay or mechanic authority.

**Notes:** Check the license/attribution requirements for any individual icon before shipping it. Do not treat icon names or categories as ESO terminology or mechanics data.

---

## Historical / mechanics references

These can be extremely useful for deriving or understanding ESO formulas, but numerical claims must be reconciled against the current patch before implementation.

### UESP ESO Build Editor
https://en.uesp.net/wiki/Special:EsoBuildData

**Use for:** Formula archaeology, build-stat relationships, and comparison against UESP's implementation.

**Confidence:** Historical / contextual unless independently verified for the current update.

---

## BFF source-use rule

Before a mechanic enters the shared stat/combat pipeline:

1. Establish the formula or raw data source.
2. Verify its activation/eligibility rule.
3. Add a deterministic test.
4. Route it through the correct standing, active-bar, combat-state, target, or attack-family layer.
5. Validate against a live character sheet, tooltip, combat log, or another appropriate observable result.

A convenient calculator matching our expected number is evidence, not proof. ESO already provides enough opportunities for accidental folklore without us manufacturing more.

## Hyperioxes — ESO Ultimate Generation Calculator (U50 snapshot)

- **Location:** `math/ESO Ultimate Generation Calculator _ U50 _ Hyperioxes.htm`
- **Useful for:** Discovering the candidate universe for Ultimate generation, including Class Masteries, passives, skills, gear, base combat generation, Heroism, and Decisive.
- **Confidence:** **Medium for source discovery; low for hardcoded combat math without corroboration.** Labels and displayed rates still require canonical tooltip, trigger, cooldown, recipient, proc-chance, and build-legality verification.
- **Version/provenance:** Saved U50 page snapshot reviewed 2026-09-13. Treat it as version-sensitive observational tooling rather than a replacement for canonical ESO mechanics data.

### ESO-Hub set tooltips
https://eso-hub.com/en/sets/

**Use for:** Current live-facing set tooltip wording, set locations, piece bonuses, proc triggers, duration/cooldown wording, and quickly identifying mechanics that need deeper canonical validation.

**Notes:** Useful for spotting runtime-scaling obligations before hardcoding them. Example: the current Roar of Alkosh tooltip states that its resistance reduction equals the user's Weapon Damage at activation, capped at 6000. Treat ESO-Hub as corroboration rather than the sole authority for formulas; confirm critical math against primary data, official patch notes, or in-game/runtime evidence before promoting it to canonical engine math.

### ZOS Horns of the Reach v3.1.5 weapon-enchantment trait and Oblivion notes
https://forums.elderscrollsonline.com/en/discussion/365904

**Use for:** Primary historical ZOS evidence that Infused reduces weapon-enchantment cooldown, Torug's Pact modifies weapon-enchantment cooldown multiplicatively with Infused, and Damage Health (Oblivion) weapon-enchantment damage cannot critically strike. Also useful for the documented Oblivion/Prismatic Infused cooldown bug fixes in that patch.

**Confidence:** Primary / reference-grade for the explicitly documented mechanics in v3.1.5. Treat it as historical evidence; current exact numeric trait values or broader ordinary-enchantment critical rules still require current corroboration before hardcoding.

**Notes:** The developer comment specifically identifies Oblivion damage as non-critical. It does not establish that every other weapon-enchantment damage family can critically strike, nor which critical-stat family an ordinary glyph would use.

### ZOS Update 20 weapon-enchantment activation rules
https://forums.elderscrollsonline.com/en/discussion/435633/pts-patch-notes-v4-2-0

**Use for:** Authoritative weapon-enchantment activation topology. ZOS states that weapon enchantments proc 100% of the time when not on cooldown when a Light Attack, Heavy Attack, or weapon ability deals damage; Dual Wield weapon abilities may proc either weapon and favor an enchantment that is not on cooldown.

**Confidence:** Primary / reference-grade for the documented activation rule.

**Notes:** This closes activation-cause evidence, not the exact current base cooldown values, off-bar source persistence, poison replacement, or same-identity cooldown sharing. Those remain separately gated until current-version authoritative evidence is available.

### ZOS Update 21 weapon-enchantment cooldown example
https://forums.elderscrollsonline.com/en/discussion/463161/playstation-4-patch-notes-v1-45-wrathstone-update-21

**Use for:** Primary-source evidence that a normal direct-damage weapon enchantment uses a 4-second cooldown. ZOS's one-handed enchantment balance example explicitly preserves a 4-second cooldown while halving enchantment potency.

**Confidence:** Primary / reference-grade for the documented direct-damage cooldown example.

**Notes:** Do not generalize the 4-second value to Crusher, Weakening, Hardening, or other buff/debuff enchantments. Their family cooldown still needs its own authoritative evidence.

### ZOS Dark Brotherhood poison/enchantment suppression rule
https://forums.elderscrollsonline.com/en/discussion/261799/pts-patch-notes-v2-4-0

**Use for:** Primary-source topology for poison-equipped weapon sets. ZOS states that while a weapon set has a poison equipped, weapon enchantments on that set are temporarily suppressed.

**Confidence:** Primary / reference-grade for the documented suppression rule.

**Notes:** This establishes replacement/suppression topology, not poison proc cadence or current enchantment cooldown values.

### ZOS v4.2.6 one-damage-instance weapon-enchantment rule
https://forums.elderscrollsonline.com/en/discussion/443312/pc-mac-patch-notes-v4-2-6

**Use for:** Authoritative per-damage-instance weapon-enchantment exclusivity. ZOS fixed Dual Wield weapon enchantments both proccing from one isolated damage instance and clarified that separate hits from a multi-hit ability can proc separate enchantments.

**Confidence:** Primary / reference-grade for the documented exclusivity rule.

**Notes:** This proves that one isolated damage occurrence cannot activate two weapon enchantments simultaneously. It does not by itself establish same-identity shared cooldown behavior or the exact source-selection algorithm beyond the separately documented Update 20 off-cooldown preference.

### ZOS Update 19 weapon-source persistence rule
https://forums.elderscrollsonline.com/en/discussion/428092/pts-patch-notes-v4-1-3

**Use for:** Primary-source weapon-enchantment source ownership across weapon swaps. ZOS clarified that enchantments remember the weapon from which an ability was fired; if the ability deals damage after a bar swap, the enchantment on that original weapon fires.

**Confidence:** Primary / reference-grade for source-weapon ownership across a swap.

**Notes:** This promotes off-bar/source-weapon persistence independently from cooldown-sharing rules. It does not prove that duplicate enchantment identities share one cooldown or establish the buff/debuff-family base cooldown.

### ZOS Combat Team: single-target DoTs do not trigger weapon enchants
https://forums.elderscrollsonline.com/en/discussion/443598/adjustments-to-how-weapon-enchants-and-poisons-trigger

**Use for:** Primary-source weapon-enchantment occurrence eligibility. ZOS Combat Team staff explicitly narrowed the Update 20 trigger model so single-target Damage over Time abilities, and abilities that apply a single-target DoT, do not repeatedly fire weapon enchantments; direct damage and ground-targeted/AoE effects remain outside that exclusion.

**Confidence:** Primary / reference-grade for the documented trigger-family exception.

**Notes:** This is the authority for classifying exact weapon-skill damage occurrences by component shape instead of treating every tick owned by a weapon ability as enchant-eligible. It does not establish current cooldown duration or duplicate-enchantment cooldown scope.

### ESO forum community testing: duplicate weapon-enchantment cooldown sharing
https://forums.elderscrollsonline.com/en/discussion/460533/clarification-on-enchants-unnecessarily-over-complicated

**Use for:** Corroborative community evidence that identical weapon enchantments share a cooldown across weapon sources/bars. The thread also points back to the ZOS Wolfhunter activation-rule patch notes.

**Confidence:** Community / corroborative only. Useful for shaping the research hypothesis, not sufficient to promote exact combat math.

**Notes:** Historical corroboration only. The same-enchantment shared-cooldown rule is now closed by the first-party **ESO Support — Do weapon enchantments share cooldowns?** entry later in this registry. Keep this thread as supporting history; it does not close distinct-enchantment independence or buff/debuff-family base cooldowns.

### ESO forum community testing: distinct enchant identities use independent cooldowns
https://forums.elderscrollsonline.com/en/discussion/363984/glyphs-cooldown-sharing

**Use for:** Corroborative community evidence that different enchant identities can proc on their own cooldown timers while identical glyph identities share one timer.

**Confidence:** Community / corroborative only. Useful for distinguishing duplicate-identity sharing from distinct-identity independence, but not sufficient for Objective #32 theoretical closure.

**Notes:** This source supports keeping a separate provisional `distinct_effect_identities_have_independent_cooldowns` proof field rather than hiding both topology claims behind one generic cooldown-scope label.

### ESO Forums — “Clarification on enchants: Unnecessarily over-complicated?”
https://forums.elderscrollsonline.com/en/discussion/460533/clarification-on-enchants-unnecessarily-over-complicated

**Use for:** Community corroboration of weapon-enchantment cooldown topology after the Wolfhunter/Update 20 trigger changes. The thread explicitly distinguishes identical enchant identities sharing a cooldown from different enchant identities retaining separate cooldowns, and ties the discussion back to ZOS Update 20 plus Gilliam’s trigger clarification.

**Confidence:** Community / corroborating only. Useful for narrowing the research target and validating long-running player observations. Same-identity sharing is now independently authoritative through the first-party ESO Support article; this community thread still does **not** promote distinct-identity independence into authoritative Objective #32 combat math.

### ESO-Hub — Infused Weapon Trait
https://eso-hub.com/en/traits/weapon/infused

**Use for:** Current-live corroboration of the weapon Infused trait split: enchantment effect strength scales by item quality while enchantment cooldown reduction remains 50%. Useful for checking the imported trait semantics and the Gold/Legendary quality path used by saved builds.

**Confidence:** Current community/reference-grade, not primary ZOS mechanics proof. Use to corroborate the canonical imported trait description and detect data-routing mistakes; prefer primary/client-derived evidence before introducing new hardcoded combat constants.

### ZOS Update 23 PC/Mac Patch Notes v5.1.5 — Oblivion Damage / Decrease Health
https://forums.elderscrollsonline.com/en/discussion/491043/pc-mac-patch-notes-v5-1-5-scalebreaker-update-23

**Use for:** Primary ZOS evidence for the Update 23 player-sourced Oblivion Damage model and Decrease Health weapon enchantment: target-Max-Health scaling, quality-scaled percentage with the documented Legendary CP160 ceiling, maximum damage cap, and the special bypass/non-critical behavior described for player-sourced Oblivion Damage.

**Confidence:** Primary / reference-grade for the documented Update 23 mechanic. Current imported enchant descriptions should still be checked for present-version scaling metadata before exact U50 damage is applied; do not infer glyph quality from weapon quality.

### ESO Support — What is poison-making in The Elder Scrolls Online?
https://help.elderscrollsonline.com/app/answers/detail/a_id/34326/

**Use for:** Current first-party support evidence that poisons are equipped alongside wielded weapon sets and that a poison suppresses the weapon enchantments on that specific weapon set.

**Confidence:** Primary / reference-grade for poison-to-weapon-set ownership and enchantment suppression. This source does not establish current poison proc chance, cooldown, effect duration, or the complete poison formula catalog.

### ZOS PC/Mac Patch Notes v4.2.5 — poison 20% activation
https://forums.elderscrollsonline.com/en/discussion/comment/5552032

**Use for:** Primary ZOS live Update 20 evidence that all poisons proc 20% of the time when a Light Attack, Heavy Attack, or weapon ability deals damage.

**Confidence:** Primary / reference-grade for poison proc chance and qualifying damaging attack families.

### ZOS PC/Mac Patch Notes v4.2.7 — poison single-target DoT exclusion
https://forums.elderscrollsonline.com/en/discussion/444322/pc-mac-patch-notes-v4-2-7

**Use for:** Primary ZOS evidence that weapon enchantments and poisons no longer proc from single-target weapon-ability Damage over Time effects, with specific excluded examples.

**Confidence:** Primary / reference-grade for the single-target DoT exclusion.

### ZOS Update 13 Sneak Peek — global poison cooldown
https://forums.elderscrollsonline.com/en/discussion/310623/update-13-sneak-peak-notes

**Use for:** Primary developer evidence from ESO Creative Director Rich Lambert that all poisons share one global cooldown, no longer have individual cooldowns, and cannot proc more than once every 10 seconds.

**Confidence:** Primary / reference-grade for the introduced global 10-second poison cooldown rule. Later poison fixes found during review do not document a replacement cadence; future contrary ZOS evidence should supersede this field rather than being blended with it.

### ESO Forums — Official Feedback Thread for Poison-Making (ZOS Systems Team)
https://forums.elderscrollsonline.com/en/discussion/261818/official-feedback-thread-for-poison-making/p5

**Use for:** Primary-source design intent for crafted poison cadence and consequence shape. ZOS Systems Team staff explicitly described the move to a 10-second poison cooldown, converting instant poison effects into over-time effects, and drain poisons carrying paired positive/negative effects.

**Confidence:** High for the documented mechanic shape and historical design change because the relevant post is from ZOS staff. Do **not** use the 2016-era numeric tooltip values as current hardcoded magnitudes without a modern canonical data source or current in-game/log validation.

**BFF rule:** Safe evidence for poison runtime topology and consequence structure. Not sufficient by itself for 2026 poison damage/healing/resource magnitudes, dilution, tick interval, or current named-effect values.

### ESO-PvP Alchemy Guide — Update 50 poison relationship cross-check
https://eso-pvp.com/alchemy/

**Use for:** Current U50 crafted potion/poison recipe and relationship cross-checks, especially which poison-side Alchemy traits produce named effects on the target or wielder. The page was checked in September 2026 and explicitly labels itself Update 50.

**Confidence:** Medium for trait -> named-effect relationships and recipe/item cross-checking. Do not treat its displayed named-effect percentages as BFF's numeric authority when they conflict with FoundryDock's separately reviewed canonical named-effect semantics.

**BFF rule:** Safe corroboration for relationships such as Breach -> Minor Breach, Protection poison -> target Minor Vulnerability + self Minor Protection, Increase Weapon Power poison -> target Minor Maim + self Minor Brutality, and Increase Spell Power poison -> target Minor Cowardice + self Minor Sorcery under U50. Keep U51 semantics separately versioned; Update 51 lands September 28, 2026.

### ZOS PTS Patch Notes v8.3.2 — Ozezan buff duration
https://forums.elderscrollsonline.com/en/discussion/627533/pts-patch-notes-v8-3-2

**Use for:** First-party confirmation that Ozezan the Inferno's repeatedly applied buffs were set to 1.1 seconds to avoid flicker. Cross-check this historical change against the current imported two-piece bonus before using the duration.

**Confidence:** Primary for the documented 2023 change; current `data/eso.db` two-piece tooltip is the local authority for the exact Minor Vitality relationship and current displayed duration. This patch note alone does not prove present-day uptime or the separate Armor trigger.

### ESO-Hub — Camouflaged Hunter
https://eso-hub.com/en/skills/guild/fighters-guild/camouflaged-hunter

**Use for:** Current post-U51 cross-check that Camouflaged Hunter grants Major Savagery while slotted.

**Confidence:** High secondary/reference cross-check. Prefer first-party patch notes for system-wide named-buff changes; use current in-game/canonical skill data when hardcoding exact skill relationships.

### ZOS PC/Mac Patch Notes v11.1.5 — Grim Focus family
https://forums.elderscrollsonline.com/en/discussion/681998/pc-mac-patch-notes-v11-1-5-update-47

**Use for:** First-party evidence that Grim Focus and its morphs, including Relentless Focus, grant Major Prophecy and Major Savagery while slotted on either bar as of Update 47.

**Confidence:** Primary / reference-grade for the introduced skill relationship. Update 51 later consolidated Prophecy into Savagery, so the personal-coverage identity should now be Major Savagery.

### ESO Forums — Update 51 Major/Minor consolidation
https://forums.elderscrollsonline.com/en/discussion/694084/with-the-update-51-combat-rework

**Use for:** Current first-party explanation that Update 51 consolidates Weapon/Spell critical named effects into Savagery and removes Prophecy as a separate named effect.

**Confidence:** Primary for the Update 51 system-level consolidation. Individual skills should still be validated against current skill data when building exact provider registries.

### ZOS Update 51 Launch Day Patch Notes
https://www.elderscrollsonline.com/en-us/news/post/70379

**Use for:** Current first-party Update 51 combat-system context, including hybridized Weapon/Spell Damage and Critical named effects plus the Sorcerer Exploitation 2974 Offensive Penetration and Templar Illuminate 2974 Armor changes.

**Confidence:** Primary / current reference-grade for the explicitly documented Update 51 changes.

**BFF rule:** Use this source to version Health/Extreme named-effect and role-diagnostic assumptions for U51. Do not infer unrelated caps or recommended role thresholds from silence in these notes.

### ZOS PTS v6.3.3 — player resistance cap tooltip
https://forums.elderscrollsonline.com/en/discussion/561927/pts-patch-notes-v6-3-3/p1

**Use for:** First-party documentation that the Advanced Stats resistance tooltip describes the player resistance cap as 50% / 33,000 rating.

**Confidence:** Primary for the documented cap relationship; historical unless superseded by newer first-party evidence.

**BFF rule:** Treat 33,000 as a mechanical cap/reference, not a claim that every Tank build must show 33,000 in static build state. Role review floors remain advisory and encounter-dependent.

### ESO Support — Do weapon enchantments share cooldowns?
https://help.elderscrollsonline.com/app/answers/detail/a_id/23047/

**Use for:** Primary ZOS support evidence for duplicate weapon-enchantment cooldown topology. The support answer states that when dual-wield weapons carry the same enchantment, the enchantments share one cooldown.

**Confidence:** Primary / reference-grade for same-enchantment cooldown sharing.

**Notes:** This closes only the duplicate/same-enchantment identity rule. It does not prove that different enchantment identities always have independent timers, nor does it establish the exact current base cooldown for every buff/debuff/damage enchantment family. Keep those separate runtime-cadence questions fail-closed.

### Hyperioxes — ESO Status Effects Guide (Update 51)
https://hyperioxes.com/eso/guides/status-effects

**Use for:** Current Update 51 cross-check of the eight damaging status effects: Martial/Magical families, proc-source base chances, exact current damage coefficients, 0/2/4-second periodic schedules, Poisoned execute scaling, Hemorrhaging stack scaling, Diseased secondary AoE, Concussion recent-status bonus, Overcharged resource restore, and status-effect scaling from the higher Max resource and higher Weapon/Spell Damage.

**Confidence:** High current secondary/reference evidence. The page explicitly identifies itself as updated for Update 51 on September 29, 2026. ZOS Update 41 patch notes independently corroborate the major behavior changes, but the exact current coefficients are sourced here rather than from the local combat-effect rows.

**BFF rule:** Safe as the versioned U51 coefficient/profile source when paired with primary ZOS behavior corroboration. Keep critical-strike behavior and any mechanic not explicitly documented here fail-closed rather than inheriting it from older UESP/forum formula evidence.

## ZOS — PC/Mac Patch Notes v5.0.5 (Elsweyr / Update 22)

**URL:** https://forums.elderscrollsonline.com/en/discussion/comment/6062157/

**Use for:** Primary ZOS evidence that Poisoned, like the other status effects, derives from the caster's highest Weapon/Spell Damage, Max Stamina/Magicka, and Weapon/Spell Critical Strike Chance. Use as historical mechanic provenance and corroborate patch-sensitive behavior against current notes.

## ZOS — PTS Patch Notes v12.1.0 (Update 51)

**URL:** https://forums.elderscrollsonline.com/en-gb/discussion/697154/pts-patch-notes-v12-1-0

**Use for:** Current Update 51 primary evidence that status effects are proc-based attacks and that proc attacks no longer inherit Sneak or Shadowy Disguise guaranteed Critical Strike. Combined with prior ZOS status-critical scaling evidence, this supports ordinary crit eligibility while excluding those guaranteed-crit sources.

### ESO-Hub — Complete Dreadsail Reef Guide
https://eso-hub.com/en/guides/Dreadsail-Reef-Guide/dreadsail-reef-boss-list

**Use for:** Dreadsail Reef boss-by-boss Veteran/Hard Mode differences, boss/add health, Twins dome/interrupt rules, Reef Guardian heart/parasite handling, Tideborn Taleria portal thresholds, Rapid Deluge target counts, Sea Behemoth cadence, and raid-lead strategy context.

**Confidence:** Validation / gameplay-practice corroboration. Strong for encounter planning because the guide explicitly separates Hard Mode behavior, but exact numeric timings and patch-sensitive values should still be reconciled against Combat Alerts/Qcell helper, official notes, logs, or live observation before becoming canonical combat math.

**BFF rule:** Preserve Veteran and Hard Mode values as separate scoped facts. Do not flatten difficulty-specific target counts, cooldowns, add cadence, or mechanic responses into one encounter-wide value.

### Qcell's Dreadsail Reef Helper
https://www.esoui.com/downloads/info3354-QcellsDreadsailReefHelper.html

**Use for:** Dreadsail Reef-specific runtime mechanic identities, role-facing alerts, tank fragility swaps, dome cooldowns, Hard Mode teleport positions, execute rescue mechanics, Reef Guardian status/heart tracking, Taleria Deluge/Behemoth/Winter Storm/bridge timers, and historical Swashbuckler Supreme execution evidence.

**Confidence:** High validation / runtime-practice corroboration. It is an encounter-specific addon maintained by the guide author and directly tracks live mechanic events, but addon timing/IDs still need version-aware review before becoming timeless canonical facts.

**BFF rule:** Excellent corroboration for which mechanics need explicit assignments or backups in Comp/Assignments/Live Raid. Treat addon version history as evidence that several DSR mechanics differ by difficulty and changed during early patches.

### The Tank Club — Dreadsail Reef Trial Tank Guide
https://thetankclub.com/eso-dreadsail-reef-trial-tank-guide/

**Use for:** Main-tank/off-tank ownership, Twins fragility swaps, add control, Reef Guardian boss routing and Acid Reflux handling, Taleria positioning, Sea Behemoth ownership, resource pressure, and practical HM tank burden.

**BFF rule:** Use to inform role-pressure and assignment suggestions, not exact game formulas. Cross-check mechanic values against reviewed encounter evidence before hardcoding.

### User-supplied Nightblade dummy-parse video (2026-10-08)
**Source:** Video shared in the FoundryDock project conversation (MP4 attachment; not stored in the Git repository). User explicitly identifies it as an exemplary Nightblade parse reference, **not** Clus's saved Necromancer trial build.

**Use for:** Observational comparison of Nightblade dummy rotation sequencing, approximate bar changes and timing, and visual character-sheet context. Transcribe only actions that can be independently identified from readable frames. Keep a separate identity from any saved HOUAD raid character/build.

**Confidence:** Medium for clearly visible on-screen actions and the user's class classification; low for precise timing, enchant/proc behavior, damage coefficients, and exact DPS without combat-event logs and verified contemporaneous build/buffs.

**BFF rule:** Calibration/rotation reference only. Do not hardcode formulas, modify Clus's canonical equipment, or claim a validated Nightblade DPS number based solely on this footage.


## Stable source URL index

These keys identify documents/URLs, not game entities or numeric ability IDs. Confidence and allowed use remain in the source entries above. Multiple findings may cite one source key; a new patch-specific URL gets its own key. No fresh external verification was performed during consolidation.

| Source key | URL |
| --- | --- |
| `src-05db2adfff13` | https://www.esologs.com/v2-api-docs/eso/ |
| `src-4cbab2242d6e` | https://eso-hub.com/en/sets/ozezan-the-inferno |
| `src-ea10c035cfdf` | https://eso-hub.com/en/sets/nazaray |
| `src-f513f427bcac` | https://eso-hub.com/en/sets/master-architect |
| `src-61c097acc89b` | https://eso-hub.com/en/sets/war-machine |
| `src-38dc7fc23e93` | https://forums.elderscrollsonline.com/en/discussion/674341/pc-mac-patch-notes-v10-3-5-fallen-banners-dlc-update-45 |
| `src-774605b7efef` | https://help.bethesda.net/app/answers/detail/a_id/69237 |
| `src-522b542f9400` | https://github.com/esoui/esoui |
| `src-6fc59317dc47` | https://www.esoui.com/forums/ |
| `src-2163f49f2d1f` | https://forums.elderscrollsonline.com/en/categories/patch-notes |
| `src-3d57f9fe66ab` | https://github.com/uesp/uesp-esolog |
| `src-db99155e72eb` | https://esoitem.uesp.net/viewlog.php |
| `src-24d587d009be` | https://esolog.uesp.net/exportJson.php?table=skillCoef |
| `src-b6fc0b386d8c` | https://en.uesp.net/wiki/Online:Scribing |
| `src-9d4e1e3be97e` | https://github.com/Solinur/LibCombat/blob/master/docs/API.md |
| `src-52adf7c6824f` | https://www.esologs.com/ |
| `src-85959cfd2adc` | https://www.btvtools.com/ |
| `src-6feb55830728` | https://esodecoded.com/tools |
| `src-062ac46489bc` | https://eso-hub.com/en/skills |
| `src-e5f32e284fae` | https://chat.uesp.net/esobuilddata/ |
| `src-ab8c209ee4a6` | https://en.uesp.net/wiki/Online:Lifesteal |
| `src-0baa1cc6d925` | https://eso-hub.com/en/buffs-debuffs |
| `src-fa7fff7f3bdd` | https://eso-hub.com/en/status-effects |
| `src-00d9c8064093` | https://eso-hub.com/en/sets |
| `src-04caf83d4d46` | https://eso-hub.com/en/guides |
| `src-7a370ea0c538` | https://eso-hub.com/en/scribing-simulator |
| `src-e3113731bb33` | https://xynodegaming.com/ |
| `src-4df4f8b71f43` | https://thetankclub.com/game/the-elder-scrolls-online/ |
| `src-b719178ad1da` | https://www.youtube.com/@NinjaPulls |
| `src-2e6eac46c600` | https://www.youtube.com/@SeaUnicorn |
| `src-2993b5314a8c` | https://www.youtube.com/@FaceheadMcGee |
| `src-8dcb58dcdabe` | https://www.youtube.com/@Temfoolery |
| `src-0e56bb84b514` | https://game-maps.com/ESO/The-Elder-Scrolls-Online.asp |
| `src-bfdc0d5cf976` | https://game-icons.net/ |
| `src-2b9d5d869087` | https://en.uesp.net/wiki/Special:EsoBuildData |
| `src-b6314cbbfeae` | https://eso-hub.com/en/sets/ |
| `src-ed58ccb79cae` | https://forums.elderscrollsonline.com/en/discussion/365904 |
| `src-7eec395572f9` | https://forums.elderscrollsonline.com/en/discussion/435633/pts-patch-notes-v4-2-0 |
| `src-6821e6694e16` | https://forums.elderscrollsonline.com/en/discussion/463161/playstation-4-patch-notes-v1-45-wrathstone-update-21 |
| `src-9e94a7ed07f4` | https://forums.elderscrollsonline.com/en/discussion/261799/pts-patch-notes-v2-4-0 |
| `src-ecdbb8b39d0a` | https://forums.elderscrollsonline.com/en/discussion/443312/pc-mac-patch-notes-v4-2-6 |
| `src-e6d1321bb680` | https://forums.elderscrollsonline.com/en/discussion/428092/pts-patch-notes-v4-1-3 |
| `src-09d7ef3c2fa1` | https://forums.elderscrollsonline.com/en/discussion/443598/adjustments-to-how-weapon-enchants-and-poisons-trigger |
| `src-8a6bbb07ed35` | https://forums.elderscrollsonline.com/en/discussion/460533/clarification-on-enchants-unnecessarily-over-complicated |
| `src-f990300e244c` | https://forums.elderscrollsonline.com/en/discussion/363984/glyphs-cooldown-sharing |
| `src-ec39c5d3d658` | https://eso-hub.com/en/traits/weapon/infused |
| `src-d87d909ab5ff` | https://forums.elderscrollsonline.com/en/discussion/491043/pc-mac-patch-notes-v5-1-5-scalebreaker-update-23 |
| `src-a990bbbe201b` | https://help.elderscrollsonline.com/app/answers/detail/a_id/34326/ |
| `src-5ef436c026c7` | https://forums.elderscrollsonline.com/en/discussion/comment/5552032 |
| `src-2abdff20d9ff` | https://forums.elderscrollsonline.com/en/discussion/444322/pc-mac-patch-notes-v4-2-7 |
| `src-97539995178d` | https://forums.elderscrollsonline.com/en/discussion/310623/update-13-sneak-peak-notes |
| `src-c36cf69ebda8` | https://forums.elderscrollsonline.com/en/discussion/261818/official-feedback-thread-for-poison-making/p5 |
| `src-90bbc874c30e` | https://eso-pvp.com/alchemy/ |
| `src-e8a9fb5411b5` | https://forums.elderscrollsonline.com/en/discussion/627533/pts-patch-notes-v8-3-2 |
| `src-5d463648312f` | https://eso-hub.com/en/skills/guild/fighters-guild/camouflaged-hunter |
| `src-477e95e0ada0` | https://forums.elderscrollsonline.com/en/discussion/681998/pc-mac-patch-notes-v11-1-5-update-47 |
| `src-e1c7431150ce` | https://forums.elderscrollsonline.com/en/discussion/694084/with-the-update-51-combat-rework |
| `src-aa0d88383aa9` | https://www.elderscrollsonline.com/en-us/news/post/70379 |
| `src-ea0e89fea425` | https://forums.elderscrollsonline.com/en/discussion/561927/pts-patch-notes-v6-3-3/p1 |
| `src-424a61c9be60` | https://help.elderscrollsonline.com/app/answers/detail/a_id/23047/ |
| `src-2ad3e3e16f87` | https://hyperioxes.com/eso/guides/status-effects |
| `src-aa7a58d6ae8c` | https://forums.elderscrollsonline.com/en/discussion/comment/6062157/ |
| `src-7cb13317d94c` | https://forums.elderscrollsonline.com/en-gb/discussion/697154/pts-patch-notes-v12-1-0 |
| `src-69dad4f52f44` | https://eso-hub.com/en/guides/Dreadsail-Reef-Guide/dreadsail-reef-boss-list |
| `src-48991681e58e` | https://www.esoui.com/downloads/info3354-QcellsDreadsailReefHelper.html |
| `src-dd76bfc4d3da` | https://thetankclub.com/eso-dreadsail-reef-trial-tank-guide/ |



### UESP ability artwork mirror — publishing artwork (2026-10-20)
- Source: https://esoicons.uesp.net/esoui/art/icons/
- Useful for: optional ability-icon packs, using the exact texture basename already attached to a uniquely resolved skill/morph in Wyrdworks reference data. Existing runtime pack location: assets/AbilityIcons/icons/128; publishing also reads user-data/artwork/skills.
- Confidence and limits: artwork reference only; not evidence for mechanics, coefficients, morph equivalence or current-patch behavior. A similar name or filename is not an acceptable identity match.
- Availability witness: the web lookup was unavailable and a direct selected PNG request returned HTTP 403 in this environment on 2026-10-20. No images were acquired or bundled. Export remains offline and uses a neutral placeholder when the exact local image is absent.

### Lokkestiiz role-guide planning source (reviewed 2026-10-26)

https://forums.elderscrollsonline.com/en/discussion/474066/sunspire-mechanics-guide — code65536, 2019 community first-hand mechanics guide. Useful for ground/flight sequencing, staggered HM tomb duties and distinguishing spawn cadence from player lockout. Historical evidence only; numerical rules are not promoted into current-patch eligibility. User-linked YouTube videos gZRkDe4ltks and S6ZWlUKdras were unavailable to the web reader; no transcript verification claimed.

Sunspire code65536 guide reviewed for all three dragons on 2026-10-26 at user request: https://forums.elderscrollsonline.com/en/discussion/474066/sunspire-mechanics-guide . The raid lead accepts continued trial applicability. Preserve source revision and disagreements; publication age alone is not grounds for excluding mechanics.

## 2026-10-27 — Lokkestiiz package evidence

https://forums.elderscrollsonline.com/en/discussion/474066/sunspire-mechanics-guide — code65536 first-hand guide, re-read for phase thresholds and distinguishing Storm/Frost atronachs and Frozen Tomb. Community evidence with historical provenance; user strategy clarifications control the authored teaching sequence. Guide flow supports 80/50/20 flight threshold context, not precise per-pull takeoff times.

https://www.esologs.com/reports/v16hzgGWTV7BZ48f — locally downloaded event pages, master actor identities and fight start timestamps establish observed boss health samples for fights 22/37/54. Do not infer health from damage totals or reuse one fight’s timing across pulls. Raw player data stays local. API documentation request returned HTTP 403; no API availability claim is based on that page.

The bundled package timeline retains separate per-pull sampled health crossings, recorded flight endpoints, Reviving Barrier casts and Storm Fury begin/cast events. These local report observations anchor playback; authored teaching cues remain explicitly distinct from confirmed player activity. No guide-specific timestamp is substituted for recorded evidence.

Nahviintaas package evidence: https://www.esologs.com/reports/v16hzgGWTV7BZ48f — locally downloaded successful fight 44 provides boss actor 133 HP samples, named casts and 12-player observations. Attempts 30/62 are comparison evidence, not complete successful reference timelines. Schematic orientation is log-coordinate based; no surveyed floor, compass, portal identity or artwork fit is established. Reviewed code65536 portal/add-flight thresholds are reused from existing evidence packets; upstairs Eternal Servant failure handling follows the raid lead's 2026-10-27 correction.

Nahvi report v16hzgGWTV7BZ48f/fight 44: Fire Storm begin/cast anchors 88499/102276, 180830/194580, 274622/288448 ms are correlated with raid-lead-confirmed upstairs statue-cover guidance. The raw cast names/IDs remain provenance; player survival and statue occlusion are not inferred. Portal actors 154/156/8 and boss-at-top orientation are direct raid-lead confirmations for this pull.
