# Constitution Flow Simulator

This directory contains a CLI-first simulator for pressure-testing the constitutional draft as an institutional system rather than as prose alone.

The simulator is intentionally simple:

- It is deterministic, not AI-driven.
- It uses JSON scenario files.
- It emits a timeline of triggered duties, deadlines, compliance, violations, and bottlenecks.
- It is designed to find structural problems early: missing fallback rules, ambiguous authority, unrealistic deadlines, and deadlock points.

## Why This Exists

The constitution now has enough institutional detail that bottlenecks are easier to miss in prose than in execution. The simulator makes it possible to ask:

- Which institution must act first?
- What deadline governs that action?
- What happens if the actor refuses to act?
- Is there a fallback?
- Does the constitution route the issue to a court, commission, Congress, or the public?
- Can the system stall even if the text is formally clear?

## File Layout

```text
simulation/
  README.md
  run.py
  scenarios/
    emergency-near-election.json
    president-obstructs-investigation.json
    state-democratic-backsliding.json
    unauthorized-military-action.json
```

## Usage

List scenarios:

```bash
python3 simulation/run.py --list
```

Run one scenario:

```bash
python3 simulation/run.py simulation/scenarios/emergency-near-election.json
```

Run one scenario in condensed mode:

```bash
python3 simulation/run.py --summary simulation/scenarios/emergency-near-election.json
```

Run every scenario:

```bash
python3 simulation/run.py --all
```

Run every scenario with both report types:

```bash
python3 simulation/run.py --all --both
```

Save human and AI artifacts:

```bash
python3 simulation/run.py --all --both --out-dir simulation/reports --save-full --save-json --save-aggregate
```

## Output

Each run prints:

- Scenario metadata
- Timeline entries in day order
- Triggered constitutional provisions
- Open obligations and whether they were satisfied
- Bottlenecks and failure points
- A final assessment

The CLI supports three output styles:

- Full: the complete diagnostic report
- Summary: condensed reading version for discussion
- Both: summary first, then full report

## Structured Exports

The simulator can also write files for later review and AI processing.

Recommended flags:

- `--out-dir <dir>`: output directory
- `--save-full`: save full Markdown report
- `--save-json`: save normalized AI-oriented JSON summary
- `--save-aggregate`: when running `--all`, save a combined aggregate JSON report

Example:

```bash
python3 simulation/run.py --all --both --out-dir simulation/reports --save-full --save-json --save-aggregate
```

This produces artifacts like:

```text
simulation/reports/
  emergency-near-election.full.md
  emergency-near-election.summary.json
  president-obstructs-investigation.full.md
  president-obstructs-investigation.summary.json
  aggregate.json
```

## AI Consumption Model

The best workflow is:

1. Read the `.full.md` file as the human audit trail.
2. Feed the `.summary.json` file to AI for structured reasoning.
3. Feed `aggregate.json` to AI when comparing scenarios or identifying repeated bottlenecks.

Each JSON summary is intentionally normalized and compact so it is easy for AI to compare across runs.

## Scenario Model

Each scenario file includes:

- `id`
- `title`
- `description`
- `events`

Each event includes:

- `day`
- `type`
- `actor`
- optional `details`

The engine converts those events into:

- constitutional duties
- deadlines
- resolved obligations
- unresolved obligations
- bottlenecks

## Current Coverage

The seeded scenarios focus on the highest-value system tests:

- emergency powers near an election
- presidential interference with an investigation
- state democratic backsliding
- unauthorized sustained military action

## Limits

This is not yet a full legal model. It does not parse constitutional text automatically, reason about contested semantics, or model strategic multi-agent branching. It is a structured execution harness for known constitutional flows.

The next logical expansions would be:

1. more event types and scenario files
2. capacity assumptions for courts and commissions
3. branching actor-behavior modes
4. report generation to markdown or JSON
5. an eventual browser UI, if the CLI proves useful
