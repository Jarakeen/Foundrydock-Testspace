# For Next Time — Wyrdworks (formerly FoundryDock)

A private project notebook for lessons learned while building Wyrdworks. FoundryDock remains the repository and technical identifier.

This file is **for the repository only**. It is not application content, runtime data, user-facing documentation, or something that should be bundled into an EXE.

The point is simple: if I ever build another project like this, I should not have to relearn every lesson the expensive way.

---

## Things I Would Do Earlier

Use this section for decisions that would have saved time, rewrites, debugging, or emotional damage if they had happened sooner.

- Add **Pydantic, or an equivalent strict validation/model layer, early** instead of bolting it on after the app has already grown around loose dictionaries, implicit assumptions, and inconsistent payload shapes.
- **Build and test persistence through the authoritative owner as workflows grow.** For active workflow changes, prove relevant save, reload, identity, and handoff behavior through the canonical repository/service and affected active consumer. Parked interfaces do not each need a duplicate page-specific save/reopen certification; keep their regression coverage and verify their underlying data through authoritative owners. Do not wait until the workflow exists to discover that screens disagree about who owns the data.
- **Build the app in the order I would actually use it, not from a shiny mockup.** A mockup can help establish visual direction, but workflow, state ownership, persistence, and real user actions should drive implementation order. Pretty screens are much cheaper than untangling a beautiful workflow that does not match reality.
- **Walk through every active workflow using a complete real-world planning scenario before architecture settles.** For a raid-planning app, that means actually planning a core team from beginning to end and asking what changes at every encounter, transition, trash pack, boss, and pre-pull setup.
- Spend more time talking through the domain before building around simplified assumptions. The questions should be concrete: What does the raid lead need for trash? How many bosses are there? Which bosses need different builds? Are there multiple trash setups? Does a fight need a pre-pull or predot configuration? What must carry forward, and what must vary by encounter?
- **Start the domain-math/reference notebook early, even if it may never be “finished.”** The ESO Math Field Notes page is valuable because it gives mechanics, formulas, assumptions, edge cases, and discoveries a durable home while the app is still evolving. An incomplete knowledge base started early is more useful than a perfect one postponed until the end.
- **Put System Architecture Rules in place immediately.** Write down non-negotiable ownership, persistence, dependency, layering, database, migration, and cross-page state rules before feature work spreads. Architecture rules are cheaper when they prevent drift than when they are written later to explain why the drift happened.
- **Start a For Next Time notebook at the beginning of the project.** Capture lessons while the reason is still fresh instead of reconstructing them months later from bugs, commits, chats, and emotional scar tissue. Future-me should inherit the observations continuously, not receive a postmortem after the damage is done.
- **Start the project under a short path such as `C:\\Dev\\<Project>` from day one.** Avoid deeply nested folders and long repository names on Windows so build tools, packaging, caches, generated files, and dependencies do not eventually collide with path-length limits. Short roots are boring, which is precisely why they work.

---

## Architecture Lessons

Notes about project structure, boundaries, service layers, models, ownership, and anything that became painful because responsibilities were unclear.

- Design around the real workflow and the sequence a user actually follows. Let screens and services grow from that flow rather than forcing the workflow to fit an attractive early concept.
- Establish a **System Architecture Rules** document at project start and treat it as an active engineering constraint, not ceremonial documentation. Record authority boundaries, allowed dependency directions, persistence ownership, migration rules, shared state contracts, and things that must never be reset or silently replaced.
- In raid planning, **the plan is not one static team configuration**. The real planning unit is a sequence of encounter contexts.
- A useful mental model is closer to:
  - Trash setup A
  - Trash setup B, if needed
  - Boss 1
  - Boss 2
  - Boss 3
  - Boss 4 / Boss 5 when the trial has them
  - Optional pre-pull / predot state for encounters that need it
- Each context can change builds, gear, skills, assignments, coverage, positioning, notes, and pre-pull actions while still belonging to the same saved Raid Plan.
- Boss variants and trash variants should be first-class architecture, not special cases added later.
- A page that displays or edits raid-plan data should be designed with encounter context in mind from the beginning, even when the initial version only needs a subset of those contexts.

---

## Data & Persistence Lessons

Anything learned about databases, migrations, save/load behavior, backups, authority boundaries, synchronization, and protecting user-owned data.

Persistence belongs first to canonical repositories and services. The current active workflow is Raid Plan, Roster, Assignments, Builds, Strategy / Raid Map, Live Raid, and Finch / Collaboration where applicable. Lantern, Comp Brainstorm, Coverage, Rotations, Readiness, Health, Comp Engine, Optimization, and Extreme Build interfaces are parked. For active changes, test the relevant consumer handoff and exact identity; for parked interfaces, retain code/data/regression coverage and verify affected records through their authoritative owner without reopening every UI. Never weaken persistence safeguards to avoid a needed check.

- Treat persistence as part of each feature, not as a later integration task.
- When a page enters the active workflow, prove the relevant **save → reload → identity/handoff** path through its canonical owner before considering that workflow increment finished. A parked interface does not require duplicate page-specific certification.
- Test handoffs between adjacent pages as they are built. A page working alone does not prove the workflow persists correctly.
- Persistence models should reflect the domain's real hierarchy. For raid planning, do not assume one build or one assignment state per player per Raid Plan if the real plan needs variants by trash pull, boss, or pre-pull phase.
- Decide early which values are global to the Raid Plan and which are scoped to an encounter context. Making that distinction late causes duplication, accidental overwrites, and pages that silently show the wrong variant.
- Variant data must persist independently. Editing Boss 2 should not overwrite Trash or Boss 1 merely because all three happen to involve the same player.

---

## Validation & Pydantic Lessons

Patterns that made data safer, bugs that validation prevented, places where strict contracts mattered, and things worth standardizing from the beginning next time.

- Add Pydantic, or a comparable typed validation boundary, near the beginning of the project.
- Define canonical models for important persisted and cross-page data before many callers begin inventing their own payload shapes.
- Validate at boundaries: UI → service, service → persistence, persisted data → runtime model, import/export, and any place external or loosely structured data enters the application.
- Strict validation is much cheaper when introduced early. Retrofitting it later means discovering years of tiny assumptions that have quietly become API contracts.
- Model encounter identity and variant scope explicitly. A payload that contains a build or assignment should make it unambiguous whether it belongs to the whole plan, trash, a specific boss, a specific trash pull, or a pre-pull/predot state.

---

## Testing Lessons

Useful testing patterns, tests that caught surprisingly important failures, places that needed stronger coverage, and tests I wish I had written sooner.

- Build persistence tests alongside each page instead of doing one giant persistence audit after many interconnected screens exist.
- For stateful workflows, test realistic navigation sequences, not only isolated service methods.
- Include reopen/reload tests. A successful Save button click is not proof that the data actually survived.
- Test an entire realistic raid-plan journey, not just isolated screens.
- Use at least one deliberately complicated fixture: multiple trash variants, 3–5 bosses, boss-specific builds, and an encounter with a pre-pull/predot configuration.
- Verify that changing one encounter context does not mutate another.
- Verify that switching contexts and returning restores the exact correct builds, assignments, coverage, notes, and pre-pull data.
- Give chat a local test environment inside chat.
---

## UI / UX Lessons

Things learned about workflow, navigation, state, drafts, saves, destructive actions, visual hierarchy, and what humans apparently do when presented with buttons.

- Start from the workflow I actually want to perform repeatedly.
- Use mockups for visual language, not as the authority on application architecture.
- Before polishing a screen, make sure its place in the workflow, state ownership, navigation, and persistence behavior make sense.
- A less glamorous working workflow is a better foundation than a polished mockup whose assumptions later require the application to be rebuilt underneath it.
- Walk every active workflow page while pretending to prepare an actual raid night. Ask, on this exact page, which encounter am I planning and what information must differ from the previous or next encounter?
- Avoid solving encounter context by filling the top bar with permanent selectors. The UI needs a simple, compact way to carry context across pages without making every screen feel like an airplane cockpit.
- The user should always be able to tell whether they are editing the overall Raid Plan, Trash, a specific boss, a specific trash variant, or a pre-pull/predot setup.

---

## Domain Discovery Before Building

Before designing pages or persistence for a domain-heavy app, model one complete real task with all the annoying exceptions included.

For a core-team raid plan, explicitly walk through:

- Team and roster selection.
- Role and seat assignments.
- Overall raid-wide assumptions.
- Trash builds.
- More than one trash build when different pulls require different setups.
- Each boss in order. Expect roughly 3–5 bosses depending on the trial rather than assuming one generic boss state.
- Boss-specific gear and skill changes.
- Boss-specific assignments and coverage changes.
- Pre-pull or predot configurations where players need a setup that exists before combat begins and may differ from their sustained combat state.
- Transitions between encounters.
- What must be visible on every planning page versus what can stay tucked behind the current encounter context.
- What is inherited from a default/global setup and what is explicitly overridden.
- What exports, raid-lead views, calculators, warnings, and live tools need to know about the active variant.

Do this before finalizing database shape or navigation. The boring walkthrough is cheaper than discovering halfway through development that “a build” actually means six related builds wearing a trench coat.

---

## Working With Coding AIs

AI assistants are useful, but they are also perfectly capable of turning a small practical request into an elaborate framework nobody asked for.

- **Keep the requested scope sacred.** If I ask for a small helper file, checklist, note, rule sheet, or utility, make the small thing first. Do not automatically expand it into a grand architecture, policy system, abstraction layer, or repo-wide redesign.
- **Do not confuse completeness with usefulness.** More sections, more rules, more abstractions, and more ceremony do not automatically make the result better.
- **Prefer the smallest artifact that solves the actual problem.** A concise working note is better than a majestic document I will never reread.
- If a request could reasonably mean either “tiny practical thing” or “large formal system,” default to the tiny practical thing unless I clearly ask for the larger version.
- Before adding project-wide process, ask whether it is actually necessary for the task or merely attractive to the AI because structure is catnip.
- Do not turn a five-minute aid into a constitutional convention.

---

## Packaging & Release Lessons

PyInstaller, EXE distribution, signing, bundled resources, update strategy, crash logging, versioning, friend builds, and all the other machinery nobody thinks about while happily writing the first feature.

- 
- 
- 

---

## Source Data & Game-Data Lessons

Lessons about external sources, confidence levels, patch changes, hardcoded mechanics, reconciliation, provenance, and separating observed game behavior from assumptions.

- 
- 
- 

---

## Things That Looked Small but Were Not

For features or changes that appeared harmless and then unfolded into a small civilization of dependencies.

- Persistence across multiple pages.
- Retrofitting validation after many services and UI pages already depended on informal payload shapes.
- Changing workflow after screens had already been designed around the mockup rather than actual use.
- Adding boss variants after pages had already been designed around one build/state per Raid Plan.
- Supporting multiple trash builds and pre-pull/predot states after encounter context was treated as optional UI metadata instead of a core data dimension.
- Asking an AI for a small helper and accidentally receiving the beginnings of a governance framework.

---

## Things That Worked Really Well

Keep the good decisions too. Future projects deserve inherited wisdom, not merely inherited trauma.

- **Starting the ESO Math Field Notes page.** Even if I never finish every section, it was still worth creating because it turns scattered mechanics knowledge into something inspectable, correctable, and reusable. I should have started it sooner.
- A living technical notebook does not need to be complete to be successful. Its value begins as soon as it starts capturing what would otherwise stay scattered across chats, code, memory, and one-off investigations.
- 

---

## Rules I Would Carry Into Another Project

Short principles worth treating as defaults next time.

- Protect user data before adding convenience.
- Make ownership of persisted data explicit.
- **Add typed validation early.**
- **Prove persistence one page at a time.**
- **Build in real-use order, not mockup order.**
- **Walk one complete real workflow before freezing architecture.**
- **Model variants that exist in the real world as first-class data, not later exceptions.**
- **Keep AI assistance proportional to the request.**
- **Start the mechanics/math field notebook early; do not wait until the knowledge is complete.**
- **Write System Architecture Rules before the project gets large enough to need rescue from itself.**
- **Create the For Next Time notebook on day one and keep feeding it as the project evolves.**
- **Use a short Windows project root such as `C:\\Dev\\<Project>` to avoid path-length problems before they exist.**
- Validate boundaries, not just happy paths.
- Prefer migrations over replacement.
- Make save state visible and predictable.
- Build diagnostics before they become urgently necessary.
- Keep source confidence separate from calculated certainty.
- Do not call a stateful page finished until its data survives leaving it and coming back.
- Let mockups describe appearance; let real workflow define architecture.
- Separate global/default state from encounter-specific overrides deliberately.
- If the workflow includes Trash, multiple Bosses, special Trash pulls, or pre-pull states, design that context system before building pages that depend on it.
- When asking an AI for a small artifact, get the small artifact first. Expansion is optional, not the default.

---

## Repository Planning, PR Hygiene & Workspace Cleanliness

- **Plan repository boundaries at the beginning.** Decide what belongs in the application repository, a separate research/evidence repository, and protected local/cloud archives. Keep executable code, tests, runtime contracts, and essential governance with the app; keep exploratory ESO findings and provenance in research; keep large raw logs, backups, and historical binaries in appropriately protected storage.
- **Define where generated material goes before tools start producing it.** Test reports, validation snapshots, temporary SQLite copies, logs, build outputs, and release packages need named owners, retention rules, expiration/review criteria, and locations outside the active source tree when practical.
- **Close the PR loop.** Every PR needs an owner, purpose, target branch, validation evidence, and a final disposition: merged, closed as superseded, or explicitly retained with a reason. Review open PRs regularly; never leave report-only or abandoned PRs lingering without an intentional decision.
- **Treat branches and worktrees as temporary workspaces with a lifecycle.** Create focused branches, push completed work, reconcile dirty/untracked files and unique commits, then safely retire obsolete branches and registered worktrees. Never infer deletion safety from age, zero ahead commits, or a clean remote comparison alone.
- **Make integration follow-through part of 'done'.** A feature is not finished when a branch exists or tests pass in isolation: verify the intended consumer, documentation, PR status, merge target, and subsequent cleanup. Do not merge unrelated research or validation branches into the active app by accident.
- **Keep the main application checkout lean but recoverable.** Regularly inspect root-folder sprawl, duplicated checkouts, temporary test databases, caches, artifacts, and old environments. Preserve canonical ESO/user databases, saved Raid Plans, raw evidence, backup coverage, and unique local work before any move or deletion.
- **Automate reporting before automating deletion.** Use periodic inventories of open PRs, branch age and divergence, dirty worktrees, disk usage, and evidence retention. Require explicit approval and exact paths for destructive cleanup; maintain a rollback record.
- **Keep GitHub for versioned text, source, tests, and small research records, not as the sole large-file backup system.** Separate Git repository history from actual disaster recovery. Verify backups independently and document restoration.
- **Review project organization at milestones.** A quick monthly repository/PR/worktree hygiene pass is cheaper than a 50 GiB archaeology expedition later.

---

## Notes to Future Me

Free-form notes that do not belong anywhere else.

- A shiny mockup is a hypothesis, not a specification.
- If the application owns important user data, persistence is a feature, not plumbing.
- Future-me would rather write ten small persistence tests now than perform another forensic investigation later.
- “One build per player” was never really the domain. It was an early simplification.
- Before coding another domain-heavy tool, sit down and narrate one full real use case out loud, including every awkward exception. Those exceptions are usually the architecture trying to introduce itself.
- When I ask an AI for a rules sheet, clarify whether I mean “a few practical rules” before permitting the machine to found a republic.
- The most obvious FNT lesson is recursive: start FNT at the start.

---

## Styling & Visual Ownership Lessons

- **Centralize styling from day one.** One canonical theme owner should define palette tokens, typography, spacing, borders, focus states, card surfaces, background textures and accessibility behavior. Page files should not invent their own colors or miniature themes.
- **No scattered visual snippets in page code.** Avoid ad hoc `setStyleSheet()` strings, page-local `STYLE` blocks, and hard-coded hex values for ordinary buttons, cards, labels and backgrounds. Use shared semantic widget properties/components and theme tokens instead. Exception: genuinely unique visualizations, image rendering and temporary diagnostic styling, with a documented owner.
- **One clear application order.** Apply the selected theme once at startup; do not silently concatenate multiple legacy themes or install widget event filters that repeatedly rewrite local styles. Compatibility adapters must have explicit, testable boundaries.
- **Keep layout ownership separate from appearance ownership.** Pages own content, widget composition and necessary geometry. The shared theme owns their visual treatment. Do not let a page-level `QWidget` or `QFrame` selector repaint every descendant and hide its parent's textured surface.
- **Make texture and asset selection explicit.** Use one reusable texture/surface renderer, verify it paints each full widget on resize, and keep map background defaults in map initialization rather than theme code. Saved/custom map choices must always win over defaults.
- **Audit the effective result, not just source text.** Record theme startup calls, page-level styles, palette changes, resource paths and Qt widget properties; flag conflicts with file/line evidence and validate actual screenshots on representative pages.
- **Enforce this in development reviews and tests.** New page-local visual overrides require a justified exception. A small CI/static audit should flag new hard-coded styles before another fifty pages independently pick their favorite shade of charcoal.
