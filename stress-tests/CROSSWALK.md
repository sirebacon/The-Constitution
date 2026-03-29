# Stress-Test To Simulation Crosswalk

This table links the prose stress tests in `stress-tests/` to their simulator counterparts in `simulation/scenarios/`.

## Current Mapping

| Prose Stress Test | Simulator Status | Simulator Scenario |
| --- | --- | --- |
| [article-iii-executive/emergency-extension-without-real-review.md](/Users/chris/Documents/GitHub/The-Constitution/stress-tests/article-iii-executive/emergency-extension-without-real-review.md) | Converted | [simulation/scenarios/emergency-extension-without-real-review.json](/Users/chris/Documents/GitHub/The-Constitution/simulation/scenarios/emergency-extension-without-real-review.json) |
| [article-iii-executive/president-interferes-with-own-investigation.md](/Users/chris/Documents/GitHub/The-Constitution/stress-tests/article-iii-executive/president-interferes-with-own-investigation.md) | Converted | [simulation/scenarios/president-obstructs-investigation.json](/Users/chris/Documents/GitHub/The-Constitution/simulation/scenarios/president-obstructs-investigation.json) |
| [article-ii-legislature/member-bribery-shielded-by-chamber.md](/Users/chris/Documents/GitHub/The-Constitution/stress-tests/article-ii-legislature/member-bribery-shielded-by-chamber.md) | Converted | [simulation/scenarios/member-bribery-shielded-by-chamber.json](/Users/chris/Documents/GitHub/The-Constitution/simulation/scenarios/member-bribery-shielded-by-chamber.json) |
| [article-iv-judiciary/supreme-court-strategic-delay.md](/Users/chris/Documents/GitHub/The-Constitution/stress-tests/article-iv-judiciary/supreme-court-strategic-delay.md) | Converted | [simulation/scenarios/supreme-court-strategic-delay.json](/Users/chris/Documents/GitHub/The-Constitution/simulation/scenarios/supreme-court-strategic-delay.json) |
| [article-ix-citizenship/naturalization-path-closed.md](/Users/chris/Documents/GitHub/The-Constitution/stress-tests/article-ix-citizenship/naturalization-path-closed.md) | Prose only | None yet |
| [article-x-federalism/preemption-and-local-housing.md](/Users/chris/Documents/GitHub/The-Constitution/stress-tests/article-x-federalism/preemption-and-local-housing.md) | Prose only | None yet |
| [article-x-federalism/state-democratic-backsliding.md](/Users/chris/Documents/GitHub/The-Constitution/stress-tests/article-x-federalism/state-democratic-backsliding.md) | Converted | [simulation/scenarios/state-democratic-backsliding.json](/Users/chris/Documents/GitHub/The-Constitution/simulation/scenarios/state-democratic-backsliding.json) |
| [article-xvi-war-powers/domestic-deployment-against-protest.md](/Users/chris/Documents/GitHub/The-Constitution/stress-tests/article-xvi-war-powers/domestic-deployment-against-protest.md) | Converted | [simulation/scenarios/domestic-deployment-against-protest.json](/Users/chris/Documents/GitHub/The-Constitution/simulation/scenarios/domestic-deployment-against-protest.json) |
| [article-xvi-war-powers/first-use-nuclear-crisis.md](/Users/chris/Documents/GitHub/The-Constitution/stress-tests/article-xvi-war-powers/first-use-nuclear-crisis.md) | Prose only | None yet |
| [article-xvi-war-powers/unauthorized-sustained-cyber-campaign.md](/Users/chris/Documents/GitHub/The-Constitution/stress-tests/article-xvi-war-powers/unauthorized-sustained-cyber-campaign.md) | Converted | [simulation/scenarios/unauthorized-military-action.json](/Users/chris/Documents/GitHub/The-Constitution/simulation/scenarios/unauthorized-military-action.json) |
| [article-vii-campaign-finance/dark-money-layering.md](/Users/chris/Documents/GitHub/The-Constitution/stress-tests/article-vii-campaign-finance/dark-money-layering.md) | Planned later | None yet |
| [article-viii-ethics/president-family-trading.md](/Users/chris/Documents/GitHub/The-Constitution/stress-tests/article-viii-ethics/president-family-trading.md) | Planned later | None yet |
| [article-viii-ethics/regulator-revolving-door.md](/Users/chris/Documents/GitHub/The-Constitution/stress-tests/article-viii-ethics/regulator-revolving-door.md) | Planned later | None yet |
| [cross-article/constitutional-hardball-package.md](/Users/chris/Documents/GitHub/The-Constitution/stress-tests/cross-article/constitutional-hardball-package.md) | Planned later | None yet |
| [cross-article/foreign-cyber-election-crisis.md](/Users/chris/Documents/GitHub/The-Constitution/stress-tests/cross-article/foreign-cyber-election-crisis.md) | Converted | [simulation/scenarios/foreign-cyber-election-crisis.json](/Users/chris/Documents/GitHub/The-Constitution/simulation/scenarios/foreign-cyber-election-crisis.json) |

## Notes

- Some converted tests use a simulator scenario name that is shorter or slightly normalized relative to the prose title.
- A `Prose only` status means the test is currently better handled as legal interpretation rather than deterministic institutional flow.
- A `Planned later` status means the simulator likely can model it, but needs more event types or richer state first.
