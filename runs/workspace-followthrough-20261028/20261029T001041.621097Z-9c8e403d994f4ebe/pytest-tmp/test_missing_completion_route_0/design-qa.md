# Raid Lead Workbench design QA

> Historical preview notice (2026-10-22): the user removed the old preview PNGs.
> Screenshot names below describe historical validation; they are no longer live
> attachments. See the [asset parking and preview removal record](docs/asset-parking-20261022.md) for the
> exact removal list and the Git revision retaining the originals. Test results
> below remain historical claims for their stated checkpoints.

**Source visual truth:** third displayed revised generated image, Raid Lead Workbench, `/workspace/scratch/19f31120ab7e/generated_images/exec-6db2ea9c-181b-4e07-a225-b4cf09fd44f6.png`.

**Implementation captures:** `docs/design/comp_engine_workbench.png` and `docs/design/optimization_workbench.png`. Combined comparison: `docs/design/workbench_reference_comparison.png` contains the source pair above the native pair. Captures were opened and inspected after each material visual fix. Individual captures were also inspected at their original size for text and clipping.

**Viewport / density:** native pages 1440×1024, density 1, Qt offscreen. Source pair 1984×793; paired native images are proportionally reduced to the source width for the full-view comparison. The source is a presentation board with simulated outer chrome; the implementation captures page content within the retained native application. This is an adaptation, not a pixel-identical browser clone. No browser CSS viewport exists.

**State:** illustrative candidate selected with support review lens; Optimization timing review with unknown execution. The native captures use controlled fixtures and empty team evidence; they are not a real DSR team evaluation. Actual stage bars and outer navigation remain owned by the current application shell.

## Findings and comparison history

- [P2, corrected] White scroll backgrounds and dark inherited text reduced contrast. Local widget background/foreground tokens now cover scroll contents; full-view recapture shows dark slate backgrounds and cream/muted text.
- [P2, corrected] Comp action captions clipped in the center column. Candidate navigation and persistent handoffs are separated; final capture shows the primary review actions outside the scrolling workspace.
- [P2, corrected] The footer minimum width grew a 1000-pixel window to 1005. Shorter labels corrected the minimum; the unchanged behavioral assertion passes at 1000×700 and 1200×800.
- [P2, corrected] Default views emphasized the existing comparison/table rather than the selected design's two tasks. Comp now shows a candidate first and reveals baseline on demand; Optimization now shows its typed review approach first and reveals team findings on demand. Final combined capture shows the two distinct main tasks.
- [P3] Native controls and exact-build inspection panels are denser than the generated concept. Existing editors, stage ownership and the outer shell were retained deliberately. No synthetic performance cards or invented set recommendations were substituted to make the image look complete.
- [P3] Linux offscreen uses a font fallback; Montserrat is requested by the native stylesheet. Windows font rendering requires a native check.

## Required fidelity surfaces

- Typography: readable 14px body, existing 30px title and text statuses; headers shortened to avoid clipping. Native font fallback is explicit.
- Spacing/layout: left roster, player build discovery, separate encounter review and persistent bottom actions. Overflow stays inside scroll areas; no shell resize was introduced.
- Color/tokens: existing charcoal/slate/brass/cream palette. Meaning is also conveyed through text. No new red/green distinction or motion.
- Assets: existing semantic Phase 15 sprite icons reused, no handcrafted placeholder drawings or new stock artwork. Generated presentation chrome is not installed as app navigation.
- Copy: exact-source uncertainty and unverified execution remain visible. The review is a question, not a diagnosed pacing problem. Temporary selection is not labelled a durable save.

## Interaction evidence

21 new behavioral tests passed in the final checkpoint, including candidate selection/filtering and exact identities, blocked adoption, compare toggle, evidence toggle, plan-scoped read-only review, missing-plan refusal, canonical explanation, review-basket invalidation and window size. Related checkpoint: 351 passed. No browser console exists for this desktop implementation.

## Remaining gate

Product Design Work Mode's browser-rendered verification requirement cannot be satisfied by these native Qt screenshots. No browser prototype was created because this work targets the existing desktop application. Native functionality is implemented and tested; a browser-preview handoff and a full Windows visual check are not claimed.

**Implementation checklist:** source/evidence/interaction checks complete; native visual fixes above complete; Windows native rendering and any separately requested browser prototype remain unverified.

final result: blocked
