# Constitution Finalization Plan

This plan is for the current stage of the project: the architecture is largely settled, the simulator is broad, and the remaining work is mainly validation, compression, and presentation.

Current baseline:

- `73` scenarios
- `71` stress-point scenarios
- `63` violations
- `33` bottlenecks
- `0` unresolved obligations
- overall draft score: about `9.0`

The goal now is not to keep inventing new machinery. It is to finish the draft cleanly without reopening solved systems.

---

## Final Objective

Reach a stable near-final draft that is:

- constitutionally disciplined rather than code-like
- well validated against realistic edge cases
- internally consistent across articles
- easy to publish, explain, and defend

---

## Guardrails

Use these rules during finalization:

1. Do not add new constitutional machinery unless a scenario exposes a real gap that existing text cannot plausibly cover.
2. Prefer scenario-building before text expansion.
3. Prefer narrowing and compression over adding new subsections.
4. Treat purely statutory or policy problems as statutory or policy problems.
5. Protect already-validated systems from unnecessary churn.

---

## Phase 1 — Finish Remaining Validation

### Purpose

Close the remaining meaningful testing gaps without broadening the Constitution unnecessarily.

### Main work

1. Add one more small wave of Article V edge-case scenarios.
   Target:
   - family autonomy
   - one digital-rights edge case
   Done when:
   - Article V no longer feels under-tested relative to its scope

2. Add one later Article X edge-case scenario.
   Target:
   - interstate digital conduct or cross-border harm
   Done when:
   - federalism no longer has an obvious untested modern edge case

3. Add one optional Article IX cleanup scenario only if it tests a real boundary.
   Target:
   - renunciation / statelessness avoidance / foreign-office incompatibility
   Done when:
   - Article IX feels fully validated rather than merely improved

4. Decide which “unknown gaps” should stay in simulation only.
   Priority examples:
   - quasi-private soft-cartelization
   - AI / synthetic media crisis
   - local democratic erosion below the state level
   Done when:
   - each remaining unknown-gap item is classified as:
     - constitutional target
     - statutory problem
     - monitor-only residual risk

### Deliverables

- new scenario files
- updated reports
- updated `test-scenarios.md`
- updated `simulation-findings.md`

---

## Phase 2 — Draft Discipline Pass

### Purpose

Make the Constitution read more like constitutional law and less like advanced statutory design.

### Main work

1. Compress Article IV.
   Focus:
   - procedural triggers
   - governance mechanics
   - anything that can safely move to “law shall provide”

2. Compress Article XI.
   Focus:
   - explanatory or rationale-style text
   - over-detailed standing or review mechanics

3. Compress Article VIII and Article XIII lightly.
   Focus:
   - Article VIII §1.13 abstraction level
   - any remaining agency-administration detail in Article XIII

4. Compress Article XIX where possible.
   Focus:
   - implementation-code feel
   - transition-specific operational detail that no longer needs to remain in constitutional text

5. Do one later cleanup pass on Article II.
   Focus:
   - residual density rather than structural repair

### Done when

- no article still reads like a mini-code unless the detail is truly indispensable
- high-value protections remain intact after compression
- scorecard draft-discipline scores can rise without forcing new architecture

---

## Phase 3 — Cross-Article Consistency Sweep

### Purpose

Catch final drift, overlaps, and boundary confusion before publication framing hardens.

### Main work

1. Review the Article VIII / XIII boundary one last time.
   Goal:
   - confirm it is still clean after later compression

2. Review the Article XII / XIX continuity boundary.
   Goal:
   - make sure temporary bridges and permanent organ rules read as one coherent design

3. Review emergency overlaps.
   Articles:
   - III
   - IV
   - V
   - XVI
   - XVII
   Goal:
   - make sure no fast-track, emergency, or anti-delay rule silently conflicts with another

4. Run a stale-reference and terminology audit.
   Goal:
   - no old section numbers
   - no duplicate institutional labels
   - no residual scaffolding text

### Deliverables

- updated articles if needed
- updated scorecard
- clean cross-reference state

---

## Phase 4 — Final Scorecard and Freeze Review

### Purpose

Decide what is truly finished and what should remain intentionally open.

### Main work

1. Re-score every article once after the compression and consistency passes.
2. Separate:
   - genuine remaining weaknesses
   - acceptable political-risk residuals
   - statutory-policy questions outside the Constitution
3. Create a short “freeze list” of articles or systems that should not be revised again unless a new concrete exploit appears.

### Freeze candidates

- Article III impeachment fallback structure
- Article IV anti-delay core
- Article VI anti-subversion core
- Article VIII / XIII basic anti-capture structure
- Article XVI war-powers default chain
- Article XII / XIX continuity backstops

### Done when

- the scorecard reflects the real current state rather than open brainstorming
- the project has a clear answer to “what is finished?”

---

## Phase 5 — Publication and Reader-Facing Work

### Purpose

Make the project readable and legible to non-drafters.

### Main work

1. Improve the website reader where useful.
   Possible targets:
   - better article summaries
   - easier navigation between article text and explainers
   - clearer simulator/results access

2. Expand public-facing explainers.
   High-value explainers:
   - unamendable core
   - why this is still presidential rather than parliamentary
   - how emergency powers work
   - how this differs from the current U.S. Constitution

3. Prepare translation workflow if desired.
   Goal:
   - translation system with glossary and review structure
   - not raw machine translation only

### Done when

- the project can be read by someone new without repo archaeology
- the main constitutional choices are easy to explain in plain language

---

## What Not To Chase

Do not spend finalization time on these unless a scenario proves they are real constitutional failures:

- purely private civic coordination that is better handled by statute
- ordinary attendance discipline inside chambers
- full criminal-code treatment of organized crime
- broad new emergency powers
- broad new constitutional duties for all private platforms
- redesigning the regime type

---

## Recommended Next Sequence

1. Finish the remaining Article V / X / optional IX scenario work.
2. Do the Article IV / XI draft-discipline compression pass.
3. Do the Article VIII / XIII / XIX light compression pass.
4. Run the cross-article consistency sweep.
5. Re-score and freeze.
6. Shift focus to publication and explainers.

---

## Success Standard

The Constitution is ready for near-final status when:

- simulator coverage feels broad rather than selective
- unresolved obligations remain at `0`
- remaining bottlenecks are mostly accepted political-risk residuals
- most article scores are in the `8.8+` range
- remaining edits are mostly prose polish, not system repair
