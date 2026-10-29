# Phase 15.5 — Dependency census

This is a dated retirement/dependency evidence index, not a current measured module count. Architecture rules live in [SYSTEM_ARCHITECTURE_RULES.md](SYSTEM_ARCHITECTURE_RULES.md).

The original census reported native shell independence and documented 62 retirement slices. Retain shared engines/components; an older name alone is not a reason to remove code. Do not restore deleted/retired modules to satisfy archival tests.

For fresh evidence use existing `tools/audit_phase155_dependencies.py`, `tools/audit_system_architecture.py`, retirement audit/manifest and relevant tests. Static closure does not prove every dynamic runtime path or that a file is safe to delete. Deletion requires supported-caller, replacement, migration and regression evidence.

Remaining debt described historically included shared map installer composition, compatibility/migration boundaries and quarantined history. Recheck actual code before treating those as open or closed today.

Full original evidence and wording: [dated source](docs/archive/governance_2026-10-10/PHASE155_DEPENDENCY_CENSUS.md). Historical counts and completion claims apply only to their recorded checkpoint.
