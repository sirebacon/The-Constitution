# Stress-Test Conversion Plan

This document maps the prose stress-test suite to the simulator. The goal is not to replace `stress-tests/` with `simulation/scenarios/`, but to decide which tests should become executable scenarios now and which should remain human-review prompts until the simulator can model them well.

## Decision Rule

Convert a stress test into a simulator scenario when it can be expressed primarily as:

- event
- institutional duty
- deadline or trigger
- action or inaction
- constitutional consequence

Keep a test in prose when it depends mainly on:

- open-textured interpretation
- balancing tests
- strategic ambiguity
- fact sensitivity that the current simulator cannot encode without becoming misleading

## Current Classification

### Convert Now

These tests already fit the simulator's current strengths: deadlines, institutional handoffs, missed duties, and enforcement flow.

1. [stress-tests/article-iii-executive/emergency-extension-without-real-review.md](/Users/chris/Documents/GitHub/The-Constitution/stress-tests/article-iii-executive/emergency-extension-without-real-review.md)
   Why:
   This is a clean executive-emergency sequence with renewal, review, lapse, and rights-floor consequences.
2. [stress-tests/article-iii-executive/president-interferes-with-own-investigation.md](/Users/chris/Documents/GitHub/The-Constitution/stress-tests/article-iii-executive/president-interferes-with-own-investigation.md)
   Why:
   This already exists in the simulator's coverage model and is strongly rule-driven.
3. [stress-tests/article-vii-federalism/state-democratic-backsliding.md](/Users/chris/Documents/GitHub/The-Constitution/stress-tests/article-vii-federalism/state-democratic-backsliding.md)
   Why:
   The enforcement chain is sequential and deadline-based.
4. [stress-tests/article-xi-war-powers/unauthorized-sustained-cyber-campaign.md](/Users/chris/Documents/GitHub/The-Constitution/stress-tests/article-xi-war-powers/unauthorized-sustained-cyber-campaign.md)
   Why:
   It maps directly to a war-powers authorization window and withdrawal sequence.
5. [stress-tests/article-xi-war-powers/domestic-deployment-against-protest.md](/Users/chris/Documents/GitHub/The-Constitution/stress-tests/article-xi-war-powers/domestic-deployment-against-protest.md)
   Why:
   It can be modeled as declaration, review, unlawful order, and response obligations.
6. [stress-tests/cross-article/foreign-cyber-election-crisis.md](/Users/chris/Documents/GitHub/The-Constitution/stress-tests/cross-article/foreign-cyber-election-crisis.md)
   Why:
   It is cross-article, but still event-driven enough to test handoffs among elections, foreign-response, and speech protections.

### Convert Later

These tests are good simulation candidates, but the current engine would need more event types, actor choices, or output categories first.

1. [stress-tests/article-xii-campaign-finance/dark-money-layering.md](/Users/chris/Documents/GitHub/The-Constitution/stress-tests/article-xii-campaign-finance/dark-money-layering.md)
   Why:
   This needs pre-election timing, tracing logic, and shell-entity handling that the current engine does not yet model.
2. [stress-tests/article-xv-ethics/president-family-trading.md](/Users/chris/Documents/GitHub/The-Constitution/stress-tests/article-xv-ethics/president-family-trading.md)
   Why:
   The simulator would need conflict-coverage logic, family-member attribution, and remedy branching.
3. [stress-tests/article-xv-ethics/regulator-revolving-door.md](/Users/chris/Documents/GitHub/The-Constitution/stress-tests/article-xv-ethics/regulator-revolving-door.md)
   Why:
   This needs better handling of functional equivalents such as consulting versus lobbying.
4. [stress-tests/cross-article/constitutional-hardball-package.md](/Users/chris/Documents/GitHub/The-Constitution/stress-tests/cross-article/constitutional-hardball-package.md)
   Why:
   It is a strong eventual simulator target, but it combines too many simultaneous channels for the current deterministic model.

### Keep Prose

These should remain primarily in `stress-tests/` for now because reducing them to current simulator primitives would strip out too much of the real constitutional question.

1. [stress-tests/article-vii-federalism/preemption-and-local-housing.md](/Users/chris/Documents/GitHub/The-Constitution/stress-tests/article-vii-federalism/preemption-and-local-housing.md)
   Why:
   This is mainly an interpretation and judicial-standard test, not a deadline-flow test.
2. [stress-tests/article-xi-war-powers/first-use-nuclear-crisis.md](/Users/chris/Documents/GitHub/The-Constitution/stress-tests/article-xi-war-powers/first-use-nuclear-crisis.md)
   Why:
   The legal issue is compressed, extreme-time-pressure decision design rather than an institutional queue.

## Mapping To Existing Simulator Coverage

Some prose tests already correspond to simulator scenarios, but with different names:

- `president-interferes-with-own-investigation.md`
  maps to [simulation/scenarios/president-obstructs-investigation.json](/Users/chris/Documents/GitHub/The-Constitution/simulation/scenarios/president-obstructs-investigation.json)
- `state-democratic-backsliding.md`
  maps to [simulation/scenarios/state-democratic-backsliding.json](/Users/chris/Documents/GitHub/The-Constitution/simulation/scenarios/state-democratic-backsliding.json)
- `unauthorized-sustained-cyber-campaign.md`
  maps to [simulation/scenarios/unauthorized-military-action.json](/Users/chris/Documents/GitHub/The-Constitution/simulation/scenarios/unauthorized-military-action.json)

This is close enough for now, but future work should either align names or add a small crosswalk table in the simulator metadata.

## Recommended Conversion Order

1. `emergency-extension-without-real-review.md`
   This is the cleanest next Article III scenario and should help resolve the emergency-lapse issue already surfaced in simulation output.
2. `domestic-deployment-against-protest.md`
   This expands Article XI coverage beyond foreign force and tests abuse resistance against internal repression.
3. `foreign-cyber-election-crisis.md`
   This is the best next cross-article scenario because it exercises Article I, V, VI, VII, XI, and XIV together.
4. `dark-money-layering.md`
   Start only after the simulator has better campaign-finance and tracing primitives.

## Recommended Process

When converting a prose stress test:

1. Keep the original Markdown file in `stress-tests/`.
2. Add a JSON scenario in `simulation/scenarios/`.
3. Use the same underlying factual setup, but simplify only where needed to make duties and deadlines explicit.
4. Record any lost nuance in the scenario's notes or in `design-notes/simulation-findings.md`.
5. If the conversion cannot preserve the real constitutional issue, stop and keep it prose-only.

## Immediate Next Batch

The strongest next simulator additions are:

- [stress-tests/article-iii-executive/emergency-extension-without-real-review.md](/Users/chris/Documents/GitHub/The-Constitution/stress-tests/article-iii-executive/emergency-extension-without-real-review.md)
- [stress-tests/article-xi-war-powers/domestic-deployment-against-protest.md](/Users/chris/Documents/GitHub/The-Constitution/stress-tests/article-xi-war-powers/domestic-deployment-against-protest.md)
- [stress-tests/cross-article/foreign-cyber-election-crisis.md](/Users/chris/Documents/GitHub/The-Constitution/stress-tests/cross-article/foreign-cyber-election-crisis.md)
