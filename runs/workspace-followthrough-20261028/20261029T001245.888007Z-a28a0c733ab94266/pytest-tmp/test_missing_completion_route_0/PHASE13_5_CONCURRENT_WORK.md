# Phase 13.5 — Historical coordination

**Historical reference, not an active work order.** Current branch authority and concurrency rules are in [CLAUDE.md](CLAUDE.md); owners are in [SYSTEM_ARCHITECTURE_RULES.md](SYSTEM_ARCHITECTURE_RULES.md).

The original report described the Raid Plan persistence → Assignments → Coverage → Rotation → read-only Optimizer Adviser chain, its scoped responsibility boundaries and dated validation. It does not authorize restoring retired pages or old persistence shapes. Before reusing an old test/tool, verify its current replacement in `services/service_catalog.py` and the active checkout.

Rotation remains a consumer, not a new Raid Plan owner. User identities/builds are reusable; Raid Plan owns raid selections; Coverage consumes evidence; recommendations require explicit adoption. No log/runtime/optimizer state should become a hidden prerequisite for saving a plan.

Full original evidence and wording: [dated source](docs/archive/governance_2026-10-10/PHASE13_5_CONCURRENT_WORK.md). Historical counts and completion claims apply only to their recorded checkpoint.
