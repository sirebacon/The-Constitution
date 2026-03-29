# Constitutional Stress Tests

This directory treats the draft Constitution as a specification and tests it with concrete scenarios.

The goal is not automated execution in software. The goal is disciplined review:

- Can a reader identify the governing text quickly?
- Does the Constitution produce one clear answer?
- Does the answer hold under bad-faith pressure?
- Can the responsible institution actually apply the rule in time?
- Do multiple articles fit together cleanly in the same event?

## How To Use This Suite

1. Pick a scenario.
2. Read only the facts in the scenario first.
3. Answer the listed questions from the constitutional text.
4. Compare your answer against the expected outcome.
5. Score the scenario using the rubric in [rubric.md](rubric.md).
6. If the scenario fails, revise the text or record the ambiguity.

## Pass Standard

A scenario passes when:

- The governing articles and sections are identifiable without guesswork.
- The Constitution yields one dominant answer rather than two equally plausible answers.
- The remedy and responsible institution are clear.
- A bad-faith actor does not have an obvious loophole.
- The article interaction does not create contradiction or drift.

## Suite Layout

- `rubric.md`
  Common scoring guidance for all scenarios.
- `TEMPLATE.md`
  Template for adding more scenarios.
- `CROSSWALK.md`
  Mapping between prose stress tests and simulator scenarios.
- `article-iii-executive/`
  Executive abuse, accountability, emergency, and succession tests.
- `article-vii-federalism/`
  Federalism, democratic-floor, preemption, and local-control tests.
- `article-xi-war-powers/`
  War powers, cyber, nuclear, covert action, and domestic deployment tests.
- `article-xii-campaign-finance/`
  Political-money and election-integrity edge cases.
- `article-xv-ethics/`
  Corruption, conflicts, revolving door, and civil-service abuse tests.
- `cross-article/`
  Scenarios that hit multiple articles at once.

## Suggested Workflow

- Use single-article scenarios during drafting.
- Use cross-article scenarios after any major reorganization.
- Re-run the whole suite after large revisions to Articles III, VII, XI, XII, XIV, or XV.
- Record failures in `design-notes/improvement-queue.md` when they indicate a real drafting gap.
- Use [design-notes/stress-test-conversion-plan.md](/Users/chris/Documents/GitHub/The-Constitution/design-notes/stress-test-conversion-plan.md) to decide whether a prose stress test should also become a simulator scenario.
