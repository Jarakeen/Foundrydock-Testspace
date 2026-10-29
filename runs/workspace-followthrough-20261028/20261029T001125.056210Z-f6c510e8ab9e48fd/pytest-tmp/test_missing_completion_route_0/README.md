# Wyrdworks

Wyrdworks is a Windows desktop raid-planning companion for The Elder Scrolls Online.
It brings Raid Plans, roster and saved builds, assignments, and encounter strategy
maps together around shared game data and mechanics.

The active development branch is **wyrdworks-dev**. Phase 15.5 is the product and
architecture milestone; FoundryDock remains in technical names and local paths.
See the [current roadmap](MASTER_ROADMAP.md) for active and parked workflows.

## Start here

- [Features](FEATURES.md): capabilities and their recorded limits.
- [Current roadmap](MASTER_ROADMAP.md): priorities and workflow scope.
- [Workspace guide](docs/workspace.md): where files belong and how Explorer is simplified.
- [Contributor entry point](AGENTS.md): required reading and document ownership.
- [Development standard](DEVELOPMENT_STANDARD.md): validation and completion gates.
- [Release status](RELEASE_STATUS.md): historical packaging evidence and release gates.

## Run from an existing development checkout

The Windows CI baseline uses Python 3.12. In your chosen virtual environment,
install the runtime/build dependencies and test runner:

```powershell
python -m pip install -r requirements-build.txt pytest
python app.py
```

The existing reference database and user state are separate from the source code.
A fresh clone does not guarantee a provisioned game-data corpus. The existing
[database model notes](docs/DATABASE_REQUIREMENTS.md) describe data requirements,
not a provisioning procedure. Preserve working databases and saved records; do not
replace them with test data or use cleanup as a migration.

## Validate changes

```powershell
python tools/run_phase155_validation.py --suite quality
```

This runner isolates validation state under `validation_reports/`. Use the
[development standard](DEVELOPMENT_STANDARD.md) for additional checks appropriate
to the change. A source checkout or passing test run is not a packaged release.

## Repository layout

| Location | Purpose |
| --- | --- |
| `app.py`, `ui/`, `widgets/` | Desktop entry point and presentation |
| `services/`, `models/`, `engine/`, `minmax/` | Shared owners, contracts, and mechanics |
| `data/`, `database/`, `user_data/` | Reference data, persistence support, and local saved state |
| `assets/`, `resources/` | Artwork and application resources |
| `tools/`, `tests/`, package-local `tests/` | Development utilities and regression coverage |
| `docs/`, `research/`, `math/` | Documentation, research, and evidence |
| `packaging/`, `.github/` | Build tooling and automation |
| `deprecated/`, `legacy/`, `migration/`, `old_pages/` | Retained compatibility, transition, and historical material |

The [service catalog](services/service_catalog.py) identifies canonical service
owners. The [retirement policy](docs/CODE_RETIREMENT_AND_QUARANTINE.md) governs old
code; parked interfaces and apparently unused files are not automatic deletion candidates.
