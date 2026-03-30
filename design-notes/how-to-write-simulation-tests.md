# How To Write Simulation Tests

This guide explains how to add new simulation tests to the constitutional flow simulator so other contributors can create scenarios consistently.

The simulator is not a fuzzy AI reasoning system. It is a deterministic scenario runner.

Each test usually has four parts:

1. a scenario JSON file
2. one or more event handlers
3. generated report outputs
4. follow-up documentation updates

---

## 1. Start With A Real Constitutional Stress Path

Do not start by inventing a random event type.

Start with a concrete question such as:

- What happens if a president continues an expired emergency tariff by decree?
- What happens if a state denies parental recognition to a same-sex family?
- What happens if a constitutional organ misses a startup deadline?
- What happens if a dominant platform cuts off a lawful political actor during an election?

Then define:

- the constitutional provisions being tested
- the institution expected to act
- the expected constitutional consequence
- whether any bottleneck should remain

The best scenarios test a known failure mode, not just a bad outcome in the abstract.

---

## 2. Decide Whether This Is A New Scenario Or A New Scenario Family

If the scenario fits an existing area, extend the existing handler module.

Common handler areas are:

- [executive.py](/Users/chris/Documents/GitHub/The-Constitution/simulation/handlers/executive.py)
- [legislative.py](/Users/chris/Documents/GitHub/The-Constitution/simulation/handlers/legislative.py)
- [judiciary.py](/Users/chris/Documents/GitHub/The-Constitution/simulation/handlers/judiciary.py)
- [rights.py](/Users/chris/Documents/GitHub/The-Constitution/simulation/handlers/rights.py)
- [federalism.py](/Users/chris/Documents/GitHub/The-Constitution/simulation/handlers/federalism.py)
- [integrity.py](/Users/chris/Documents/GitHub/The-Constitution/simulation/handlers/integrity.py)
- [transition.py](/Users/chris/Documents/GitHub/The-Constitution/simulation/handlers/transition.py)
- [social_rights.py](/Users/chris/Documents/GitHub/The-Constitution/simulation/handlers/social_rights.py)
- [fiscal.py](/Users/chris/Documents/GitHub/The-Constitution/simulation/handlers/fiscal.py)

If the scenario introduces a genuinely new domain, add a new handler module and register it in [dispatcher.py](/Users/chris/Documents/GitHub/The-Constitution/simulation/handlers/dispatcher.py).

---

## 3. Create The Scenario JSON

Scenario files live in [simulation/scenarios](/Users/chris/Documents/GitHub/The-Constitution/simulation/scenarios).

Use an existing file as the model.

Good reference examples:

- [emergency-revenue-measure-unilateral-extension.json](/Users/chris/Documents/GitHub/The-Constitution/simulation/scenarios/emergency-revenue-measure-unilateral-extension.json)
- [family-status-discrimination-parental-recognition.json](/Users/chris/Documents/GitHub/The-Constitution/simulation/scenarios/family-status-discrimination-parental-recognition.json)
- [constitutional-organ-bridge-startup.json](/Users/chris/Documents/GitHub/The-Constitution/simulation/scenarios/constitutional-organ-bridge-startup.json)

A scenario file should include:

- `id`
- `title`
- `description`
- `articles_tested`
- `provisions_tested`
- `events`

Typical structure:

```json
{
  "id": "example-scenario",
  "title": "Short Human Title",
  "description": "One paragraph explaining the stress path and what the scenario is testing.",
  "articles_tested": ["Article V"],
  "provisions_tested": ["Article V Section 2.1", "Article V Section 2.6"],
  "events": [
    {
      "day": 0,
      "type": "some_event_type",
      "actor": "President",
      "details": {
        "key": "value"
      }
    },
    {
      "day": 3,
      "type": "some_followup_event",
      "actor": "Federal courts"
    }
  ]
}
```

Guidelines:

- keep event order chronological
- keep titles short and readable
- keep descriptions explicit about what constitutional question is being tested
- list the real provisions that should control the scenario

---

## 4. Choose Good Event Types

Event types should describe meaningful constitutional actions or failures, not vague moods.

Good:

- `president_orders_emergency_revenue_measure_continued`
- `court_voids_unilateral_emergency_revenue_extension`
- `state_denies_parental_recognition`

Bad:

- `government_does_bad_thing`
- `court_acts`
- `problem_happens`

If a new event type is too broad, future scenarios become hard to reason about and the handler logic gets muddy.

---

## 5. Implement Or Extend The Handler Logic

The simulator processes events through handler registries.

The dispatcher registry is in [dispatcher.py](/Users/chris/Documents/GitHub/The-Constitution/simulation/handlers/dispatcher.py).

Each handler module exports a `HANDLERS` map keyed by event type.

Typical pattern:

```python
HANDLERS = {
    "some_event_type": handle_some_event,
}
```

Inside a handler, the code usually does some combination of:

- add a timeline entry
- trigger a constitutional provision
- create an obligation with a deadline
- resolve or violate an obligation
- record a bottleneck
- record a violation category or risk pattern

When adding handler logic:

- keep it deterministic
- name triggered provisions explicitly
- keep the result tied to the actual constitutional design
- do not silently smuggle in policy assumptions not grounded in the draft

If you need a new module:

1. add the file under [simulation/handlers](/Users/chris/Documents/GitHub/The-Constitution/simulation/handlers)
2. export a `HANDLERS` mapping
3. register that mapping in [dispatcher.py](/Users/chris/Documents/GitHub/The-Constitution/simulation/handlers/dispatcher.py)

---

## 6. Run The Scenario

List scenarios:

```bash
python3 simulation/run.py --list
```

Run one scenario:

```bash
python3 simulation/run.py --summary simulation/scenarios/example-scenario.json
```

Run all scenarios and save outputs:

```bash
python3 simulation/run.py --all --out-dir simulation/reports --save-full --save-json --save-aggregate
```

Useful outputs:

- `.full.md` for human review
- `.summary.json` for structured results
- `aggregate.json` for the full-suite baseline

The runner is in [run.py](/Users/chris/Documents/GitHub/The-Constitution/simulation/run.py).

---

## 7. Read The Result Correctly

A scenario should tell you:

- which provisions triggered
- what obligations were created
- which obligations were satisfied
- whether any violations occurred
- whether any bottlenecks remain
- whether any obligations stayed unresolved

Important distinction:

- a `violation` often means the scenario successfully modeled bad conduct
- an `unresolved_obligation` is a more serious design problem because the Constitution failed to complete a required consequence path

The design goal is not zero violations across scenarios. Many scenarios intentionally begin with unlawful behavior.

The real goal is:

- clear constitutional routing
- enforceable duties
- clean closure of the consequence chain
- `0` unresolved obligations

---

## 8. Update The Scenario Catalog

After adding a test, update [test-scenarios.md](/Users/chris/Documents/GitHub/The-Constitution/design-notes/test-scenarios.md).

Add:

- category
- scenario name
- file name
- provision
- stress path
- expected outcome

The catalog is the public inventory of what has and has not been tested.

---

## 9. Update Findings If The Scenario Teaches You Something

If the new scenario:

- validates a previously uncertain provision
- exposes a real gap
- changes how an article should be scored
- clarifies that a bottleneck is acceptable or unacceptable

then update:

- [simulation-findings.md](/Users/chris/Documents/GitHub/The-Constitution/design-notes/simulation-findings.md)
- and sometimes [scorecard.md](/Users/chris/Documents/GitHub/The-Constitution/design-notes/scorecard.md)

Do not update the scorecard mechanically just because a new test exists.
Update it when the test materially changes confidence in the article.

---

## 10. What Makes A Good Scenario

A strong scenario:

- tests one constitutional system clearly
- uses a realistic stress path
- names the actual controlling provisions
- produces a readable expected outcome
- isolates whether the problem is:
  - violation
  - bottleneck
  - structural gap
  - acceptable political-risk residual

A weak scenario:

- tries to test too many systems at once
- uses vague event names
- assumes outcomes without handler support
- treats all bad facts as constitutional failure

---

## 11. Recommended Workflow

The safest workflow is:

1. pick a real constitutional question
2. find the closest existing scenario
3. create the new scenario JSON
4. extend or add the handler logic
5. run the single scenario first
6. inspect the summary and full report
7. run the full suite
8. update catalog and findings

This keeps the scenario understandable and reduces the chance of adding a test that looks good but is not actually wired into the system.

---

## 12. Quick Contributor Checklist

- Did I define a real constitutional stress path?
- Did I name the actual provisions being tested?
- Did I use clear event types?
- Did I add or update handler logic?
- Did the scenario run without unresolved obligations unless it is intentionally exposing a gap?
- Did I update `test-scenarios.md`?
- Did I update findings or scorecard if the result changed project confidence?

If the answer is yes to those, the scenario is probably ready.
