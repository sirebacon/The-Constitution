# Simulation Findings Log

This document records conclusions drawn from the constitutional flow simulator and its generated reports. Each entry should cite the relevant scenario outputs so recurring bottlenecks can be tracked over time.

## 2026-03-28 Rerun Review

### Inputs Reviewed

- [aggregate.json](/Users/chris/Documents/GitHub/The-Constitution/simulation/reports/aggregate.json)
- [emergency-near-election.summary.json](/Users/chris/Documents/GitHub/The-Constitution/simulation/reports/emergency-near-election.summary.json)
- [president-obstructs-investigation.summary.json](/Users/chris/Documents/GitHub/The-Constitution/simulation/reports/president-obstructs-investigation.summary.json)
- [state-democratic-backsliding.summary.json](/Users/chris/Documents/GitHub/The-Constitution/simulation/reports/state-democratic-backsliding.summary.json)
- [unauthorized-military-action.summary.json](/Users/chris/Documents/GitHub/The-Constitution/simulation/reports/unauthorized-military-action.summary.json)

### Aggregate Read

- All 4 scenarios were marked `stress_point_found`.
- Aggregate recurring risks were `executive_defiance` (2), `democratic_backsliding` (1), and `legislative_delay` (1).
- Aggregate recurring bottlenecks were `legislative_deadline_failure` (2) and `state_backsliding` (1).
- Open duties remain concentrated in the `House of Representatives` (2).

### Main Results

#### 1. War-powers enforcement still ends in a political open loop

Source: [unauthorized-military-action.summary.json](/Users/chris/Documents/GitHub/The-Constitution/simulation/reports/unauthorized-military-action.summary.json)

- Congress misses the day-30 force deadline.
- The Chief Justice issues the required withdrawal order.
- The President continues military operations anyway.
- The remaining constitutional consequence is only an open House duty to consider impeachment.

Assessment:
The draft identifies illegality clearly, but the simulator still shows no hard post-defiance timetable after a presidential refusal to comply with the withdrawal order.

#### 2. Emergency review still depends on legislative follow-through

Source: [emergency-near-election.summary.json](/Users/chris/Documents/GitHub/The-Constitution/simulation/reports/emergency-near-election.summary.json)

- Courts can block election-access restrictions quickly.
- The Regional Assembly still creates a high-severity bottleneck by failing to approve or reject the emergency by day 30.
- The simulation output records the missed deadline, but no further institutional consequence appears in the scenario.

Assessment:
Either the constitution needs a more explicit automatic lapse rule for unapproved emergencies, or the simulator needs to encode that consequence more clearly if it already exists in the text.

#### 3. Democratic-backsliding remedies remain slow before coercive relief arrives

Source: [state-democratic-backsliding.summary.json](/Users/chris/Documents/GitHub/The-Constitution/simulation/reports/state-democratic-backsliding.summary.json)

- Congress misses the remedial deadline at day 180.
- Representation suspension does not occur until day 760.

Assessment:
The Article VII pathway may still allow too much delay between confirmed violation and meaningful coercive response.

#### 4. Presidential obstruction still relies on discretionary impeachment uptake

Source: [president-obstructs-investigation.summary.json](/Users/chris/Documents/GitHub/The-Constitution/simulation/reports/president-obstructs-investigation.summary.json)

- The Accountability Commission acts on the obstruction matter.
- The President's interference is still logged as a high-severity violation.
- The remaining unresolved duty is only that the House consider impeachment.

Assessment:
The system can identify presidential self-protection but still depends on a later political choice rather than a tighter constitutional enforcement sequence.

### Structural Pattern

The rerun points to a repeated weakness rather than many unrelated ones:

- Violations are being identified.
- Missed deadlines are being identified.
- The remaining trouble is institutional closure after defiance or nonaction.

In short, the draft is comparatively stronger at declaring a breach than at forcing rapid constitutional resolution after the breach occurs.

### Best Revision Targets

1. [articles/XI-war-powers-national-security.md](/Users/chris/Documents/GitHub/The-Constitution/articles/XI-war-powers-national-security.md)
   Tighten the post-withdrawal enforcement sequence after presidential defiance.
2. [articles/III-executive.md](/Users/chris/Documents/GitHub/The-Constitution/articles/III-executive.md)
   Make the consequence of legislative nonapproval of an emergency explicit and automatic if that is the intended rule.
3. [articles/VII-federalism.md](/Users/chris/Documents/GitHub/The-Constitution/articles/VII-federalism.md)
   Shorten the path from missed congressional remedy to representation consequences.
4. [articles/III-executive.md](/Users/chris/Documents/GitHub/The-Constitution/articles/III-executive.md)
   Consider whether presidential obstruction should trigger a firmer constitutional timetable beyond a House duty to consider impeachment.

### Logging Guidance For Future Runs

For each new simulation batch, append:

- date of review
- scenarios reviewed
- recurring risk patterns
- recurring bottleneck categories
- any open duties that remain politically discretionary
- any text amendments made in response

## 2026-03-28 Expanded Scenario Review

### Inputs Reviewed

- [aggregate.json](/Users/chris/Documents/GitHub/The-Constitution/simulation/reports/aggregate.json)
- [domestic-deployment-against-protest.summary.json](/Users/chris/Documents/GitHub/The-Constitution/simulation/reports/domestic-deployment-against-protest.summary.json)
- [emergency-extension-without-real-review.summary.json](/Users/chris/Documents/GitHub/The-Constitution/simulation/reports/emergency-extension-without-real-review.summary.json)
- [emergency-near-election.summary.json](/Users/chris/Documents/GitHub/The-Constitution/simulation/reports/emergency-near-election.summary.json)
- [foreign-cyber-election-crisis.summary.json](/Users/chris/Documents/GitHub/The-Constitution/simulation/reports/foreign-cyber-election-crisis.summary.json)
- [president-obstructs-investigation.summary.json](/Users/chris/Documents/GitHub/The-Constitution/simulation/reports/president-obstructs-investigation.summary.json)
- [state-democratic-backsliding.summary.json](/Users/chris/Documents/GitHub/The-Constitution/simulation/reports/state-democratic-backsliding.summary.json)
- [unauthorized-military-action.summary.json](/Users/chris/Documents/GitHub/The-Constitution/simulation/reports/unauthorized-military-action.summary.json)

### Aggregate Read

- All 7 scenarios were marked `stress_point_found`.
- Aggregate recurring risks were `executive_defiance` (3), `institutional_stress` (2), `democratic_backsliding` (1), and `legislative_delay` (1).
- Aggregate recurring bottlenecks were `legislative_deadline_failure` (3) and `state_backsliding` (1).
- Open duties still remain concentrated in the `House of Representatives` (2).
- The expanded pool added more `rights_suppression` and `federalism_breach` coverage without changing the dominant overall pattern.

### Main Results

#### 1. The core closure problem remains unchanged

Source: [aggregate.json](/Users/chris/Documents/GitHub/The-Constitution/simulation/reports/aggregate.json)

- The simulator continues to identify violations and missed deadlines reliably.
- The recurring weakness is still what happens after defiance or nonaction is identified.
- The draft remains strongest at declaring a breach and weaker at forcing rapid institutional closure afterward.

Assessment:
The expanded scenario set increased confidence in the existing diagnosis rather than replacing it with a different one.

#### 2. War-powers enforcement still ends in a political open loop

Source: [unauthorized-military-action.summary.json](/Users/chris/Documents/GitHub/The-Constitution/simulation/reports/unauthorized-military-action.summary.json)

- Congress misses the day-30 authorization deadline.
- The Chief Justice issues the withdrawal order.
- The President ignores the withdrawal order.
- The remaining constitutional response is still only an open House duty to consider impeachment.

Assessment:
This remains the clearest unresolved enforcement gap in the draft.

#### 3. Emergency scenarios confirm both the lapse rule and the same legislative bottleneck

Sources:
- [emergency-near-election.summary.json](/Users/chris/Documents/GitHub/The-Constitution/simulation/reports/emergency-near-election.summary.json)
- [emergency-extension-without-real-review.summary.json](/Users/chris/Documents/GitHub/The-Constitution/simulation/reports/emergency-extension-without-real-review.summary.json)

- The new self-extension scenario confirms that the simulator now models emergency lapse after missed approval and rejects self-renewal by executive memorandum.
- The same Regional Assembly day-30 bottleneck still appears in both emergency scenarios.

Assessment:
The draft is clearer than before on unlawful self-extension, but the institutional stress still centers on missed legislative review.

#### 4. Democratic-backsliding remedies still tolerate long delay before coercive consequence

Source: [state-democratic-backsliding.summary.json](/Users/chris/Documents/GitHub/The-Constitution/simulation/reports/state-democratic-backsliding.summary.json)

- Congress still misses the remedial deadline at day 180.
- Representation suspension still arrives much later.

Assessment:
The Article VII mechanism remains coherent but slow.

#### 5. The new cross-article scenarios are useful and comparatively clean

Sources:
- [domestic-deployment-against-protest.summary.json](/Users/chris/Documents/GitHub/The-Constitution/simulation/reports/domestic-deployment-against-protest.summary.json)
- [foreign-cyber-election-crisis.summary.json](/Users/chris/Documents/GitHub/The-Constitution/simulation/reports/foreign-cyber-election-crisis.summary.json)

- The domestic deployment scenario cleanly distinguishes protest unrest from armed rebellion and routes response through courts and service-member obligations.
- The foreign cyber election scenario catches direct federal takeover and speech-suppression attempts while also showing that non-military Article XIV tools can be used in a constitutional way.

Assessment:
These scenarios do not reveal new deadline bottlenecks, but they do strengthen confidence that the simulator can now test multi-article rights and federalism conflicts without collapsing into ambiguity.

### Structural Pattern

The expanded run reinforces a stable pattern:

- constitutional violations are detectable
- institutional duties are usually identifiable
- the recurring weaknesses are deadline misses by political bodies and discretionary follow-through after executive defiance

The system is therefore maturing in diagnostic clarity, but its strongest remaining design problem is still enforcement closure.

### Best Revision Targets

1. [articles/XI-war-powers-national-security.md](/Users/chris/Documents/GitHub/The-Constitution/articles/XI-war-powers-national-security.md)
   Tighten the post-withdrawal enforcement sequence after presidential defiance.
2. [articles/III-executive.md](/Users/chris/Documents/GitHub/The-Constitution/articles/III-executive.md)
   Make emergency nonapproval consequences even more automatic and operational if the draft intends immediate lapse.
3. [articles/VII-federalism.md](/Users/chris/Documents/GitHub/The-Constitution/articles/VII-federalism.md)
   Shorten the path from missed congressional remedy to representation consequences.
4. [articles/III-executive.md](/Users/chris/Documents/GitHub/The-Constitution/articles/III-executive.md)
   Consider whether presidential obstruction should trigger something firmer than a House duty to consider impeachment.

## 2026-03-28 House Fallback Review

### Inputs Reviewed

- [aggregate.json](/Users/chris/Documents/GitHub/The-Constitution/simulation/reports/aggregate.json)
- [emergency-extension-without-real-review.summary.json](/Users/chris/Documents/GitHub/The-Constitution/simulation/reports/emergency-extension-without-real-review.summary.json)
- [emergency-near-election.summary.json](/Users/chris/Documents/GitHub/The-Constitution/simulation/reports/emergency-near-election.summary.json)
- [president-obstructs-investigation.summary.json](/Users/chris/Documents/GitHub/The-Constitution/simulation/reports/president-obstructs-investigation.summary.json)
- [state-democratic-backsliding.summary.json](/Users/chris/Documents/GitHub/The-Constitution/simulation/reports/state-democratic-backsliding.summary.json)
- [unauthorized-military-action.summary.json](/Users/chris/Documents/GitHub/The-Constitution/simulation/reports/unauthorized-military-action.summary.json)

### Aggregate Read

- All 7 scenarios remain `stress_point_found`.
- `unresolved_obligations` fell to `0`.
- Total bottlenecks rose to `6`, because prior open loops are now recorded as timed institutional failures.
- `open_duties_by_actor` is now empty.
- The dominant bottleneck category is now `legislative_deadline_failure` (5).

### Main Results

#### 1. The draft is materially better on enforcement closure

Source: [aggregate.json](/Users/chris/Documents/GitHub/The-Constitution/simulation/reports/aggregate.json)

- The earlier open-ended impeachment duties are gone.
- The simulator now produces fixed constitutional consequences after House nonaction.
- The cost is that the simulator records more bottlenecks, but those bottlenecks are more specific and actionable.

Assessment:
This is a genuine improvement. The Constitution is no longer failing because key duties remain indefinite. It is now failing in the narrower way that a chamber misses a constitutionally required vote.

#### 2. House noncompliance no longer kills the process

Sources:
- [president-obstructs-investigation.summary.json](/Users/chris/Documents/GitHub/The-Constitution/simulation/reports/president-obstructs-investigation.summary.json)
- [unauthorized-military-action.summary.json](/Users/chris/Documents/GitHub/The-Constitution/simulation/reports/unauthorized-military-action.summary.json)

- In both scenarios, the House fails to hold the required impeachment vote on time.
- In both scenarios, the certified charge is automatically transmitted to the Regional Assembly.
- The Regional Assembly then proceeds to trial on the transmitted articles.

Assessment:
The constitutional system no longer stops at House refusal. This is the clearest single improvement produced by the revision.

#### 3. War-powers enforcement is tighter, but still not clean

Source: [unauthorized-military-action.summary.json](/Users/chris/Documents/GitHub/The-Constitution/simulation/reports/unauthorized-military-action.summary.json)

- Congress still misses the initial authorization deadline.
- The President still violates the withdrawal order.
- The House still misses the mandatory impeachment vote.
- The difference is that the Regional Assembly trial now begins automatically after House failure.

Assessment:
The war-powers sequence is substantially stronger than before. The remaining stress point is legislative noncompliance, not collapse of the enforcement chain.

#### 4. Presidential obstruction is now routed forward instead of stalling

Source: [president-obstructs-investigation.summary.json](/Users/chris/Documents/GitHub/The-Constitution/simulation/reports/president-obstructs-investigation.summary.json)

- The Accountability Commission certifies the violation.
- The House misses the vote deadline.
- The Regional Assembly begins trial on automatically transmitted articles.

Assessment:
This is a better constitutional response than the earlier model, which merely left an unresolved House duty.

#### 5. The remaining bottlenecks are now more clearly sorted by type

Sources:
- [emergency-extension-without-real-review.summary.json](/Users/chris/Documents/GitHub/The-Constitution/simulation/reports/emergency-extension-without-real-review.summary.json)
- [emergency-near-election.summary.json](/Users/chris/Documents/GitHub/The-Constitution/simulation/reports/emergency-near-election.summary.json)
- [state-democratic-backsliding.summary.json](/Users/chris/Documents/GitHub/The-Constitution/simulation/reports/state-democratic-backsliding.summary.json)

- Emergency scenarios still point to the Regional Assembly approval bottleneck.
- The democratic-floor scenario still points to missed congressional remedy.
- The impeachment scenarios now point to House vote failure rather than indefinite open duty.

Assessment:
The stress map is cleaner now. Each remaining problem is attached to a specific institution and deadline rather than a vague failure of follow-through.

### Structural Pattern

The revised system now looks stronger on closure but still vulnerable to chamber-level refusal:

- violations are identified
- deadlines are identified
- fallback routing now exists where it did not before
- the main remaining weakness is that some political institutions can still miss required deadlines even after the fallback design is improved

This is a better failure mode than the earlier one because it is narrower and easier to design against.

### Best Revision Targets

1. [articles/III-executive.md](/Users/chris/Documents/GitHub/The-Constitution/articles/III-executive.md)
   The House fallback now works better; further changes should be cautious and avoid overcorrecting into automatic removal.
2. [articles/III-executive.md](/Users/chris/Documents/GitHub/The-Constitution/articles/III-executive.md)
   Emergency review remains the clearest unresolved legislative bottleneck.
3. [articles/XI-war-powers-national-security.md](/Users/chris/Documents/GitHub/The-Constitution/articles/XI-war-powers-national-security.md)
   War-powers closure is materially improved and may now be good enough for a holding position pending more scenarios.
4. [articles/VII-federalism.md](/Users/chris/Documents/GitHub/The-Constitution/articles/VII-federalism.md)
   The Article VII revision is working better; remaining work is now more about remedy speed than structural collapse.
