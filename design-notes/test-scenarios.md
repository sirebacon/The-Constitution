# Constitutional Test Scenario Catalog

This document is the master catalog of simulation scenarios for the constitutional flow simulator.
Each scenario isolates one constitutional system, defines a stress path, and records the expected outcome.

Status markers: `[x]` implemented — `[ ]` planned.

---

## Category A — Executive Power Limits

| # | Scenario | File | Provision | Stress Path | Expected Outcome |
|---|----------|------|-----------|-------------|-----------------|
| A1 | [x] Self-Pardon Attempt | `self-pardon-attempt.json` | Art. III §7.2(a), §15.3 | President indicted by ACC, issues self-pardon | Pardon void; prosecution continues |
| A2 | [x] Executive Order Overreach | `executive-order-overreach.json` | Art. III §6.2 | President issues EO creating private-citizen obligations without statute | EO void; congressional disapproval or court strike |
| A3 | [x] Transition Obstruction | `electoral-certification-obstruction.json` | Art. III §13, Art. VI | Outgoing president refuses security briefings and transition cooperation | Anti-subversion referral; transition proceeds |

---

## Category B — Legislative Enforcement

| # | Scenario | File | Provision | Stress Path | Expected Outcome |
|---|----------|------|-----------|-------------|-----------------|
| B1 | [x] Congressional Subpoena Defiance | `congressional-subpoena-defiance.json` | Art. II §16.2, §16.5 | Senior official defies subpoena; contempt not referred promptly | Violation; ACC prosecution chain |
| B2 | [x] Budget Deadlock — Automatic CR | `budget-deadlock-cr.json` | Art. II §12.2, §12.3 | Congress misses Oct 1 deadline; executive attempts selective CR funding | CR self-executes; court blocks manipulation |
| B3 | [x] Single-Subject Challenge | `single-subject-challenge.json` | Art. II §10.7A | Omnibus bill with unrelated riders passes both chambers | Supreme Court voids bill; returned for redrafting |
| B4 | [x] Perjury Before Congress | `perjury-before-congress.json` | Art. II §16.4 | Senior official gives known false testimony; DOJ declines to prosecute | ACC jurisdiction; automatic removal on conviction |

---

## Category C — Judicial Independence

| # | Scenario | File | Provision | Stress Path | Expected Outcome |
|---|----------|------|-----------|-------------|-----------------|
| C1 | [x] Court Order Defied by Executive | `court-order-defied.json` | Art. II §16.2(c) | Executive refuses to comply with federal court enforcement order | Marshals enforce; contempt proceedings |
| C2 | [x] Judicial Vacancy Exploitation | `judicial-vacancy-exploitation.json` | Art. IV §2.7 | Chief Justice incapacitated; President refuses to confirm successor | Judicial continuity rule designates substitute |

---

## Category D — War Powers

| # | Scenario | File | Provision | Stress Path | Expected Outcome |
|---|----------|------|-----------|-------------|-----------------|
| D1 | [x] Nuclear First-Use Circumvention | `nuclear-first-use-circumvention.json` | Art. XI §3.1 | SecDef refuses first-use order; President fires him to find compliant replacement | Violation; acting SecDef also refuses; launch blocked |
| D2 | [x] Covert Operation Against US Citizen Without Warrant | `covert-operation-against-citizen.json` | Art. XI §5.2 | CIA orders lethal strike on citizen; warrant denied as capture is feasible | Operation blocked; ACC prosecution if proceeds anyway |
| D3 | [x] Unauthorized Military Action (existing) | `unauthorized-military-action.json` | Art. XI §1 | Congress misses AUMF window; President ignores withdrawal order | House fallback; Regional Assembly trial |
| D4 | [x] PMC Substitution for Authorized Forces | `pmc-substitution.json` | Art. XI §4.4 | Congress denies AUMF; President deploys PMCs as substitute | Violation; expedited impeachment chain |

---

## Category E — Emergency Powers

| # | Scenario | File | Provision | Stress Path | Expected Outcome |
|---|----------|------|-----------|-------------|-----------------|
| E1 | [x] Emergency Near Election Day (existing) | `emergency-near-election.json` | Art. III §5.3(a), §5.4 | Emergency restricts polling access; RA misses review deadline | Court blocks restriction; emergency lapses |
| E2 | [x] Emergency Extension Without Real Review (existing) | `emergency-extension-without-real-review.json` | Art. III §5.4, Art. V §1.3 | President self-extends lapsed emergency by memo | Violation; measures void |
| E3 | [x] Section 15A Enforcement — RA Blocks Emergency Vote | `ra-blocks-emergency-vote.json` | Art. II §15A, Art. III §5.4 | RA leadership blocks scheduling; presiding officer ignores motion | Mandamus issued; vote held within 30 days |
| E4 | [x] Emergency Used to Suppress Rights | `emergency-rights-suppression.json` | Art. III §5.3(f), Art. V | Emergency invoked to restrict protected speech | Violation; courts void restriction immediately |
| E5 | [x] Habeas Corpus Suspension by President Alone | `habeas-corpus-president-suspends.json` | Art. III §5.7 | President suspends habeas corpus by executive order | Violation; courts void; only Congress may suspend |

---

## Category F — Elections and Democracy

| # | Scenario | File | Provision | Stress Path | Expected Outcome |
|---|----------|------|-----------|-------------|-----------------|
| F1 | [x] Foreign Cyber Election Crisis (existing) | `foreign-cyber-election-crisis.json` | Art. I, V, VII, XI, XIV | Foreign hack; President attempts direct state takeover and speech suppression | Violations; courts block; non-military response used |
| F2 | [x] Electoral Certification Obstruction | `electoral-certification-obstruction.json` | Art. VI §1, Art. III §13 | President-elect certified; outgoing president refuses transition cooperation | Anti-subversion prosecution; transition proceeds |
| F3 | [x] Domestic Deployment Against Protest (existing) | `domestic-deployment-against-protest.json` | Art. XI §7, §8 | Protest misclassified as rebellion; troops deployed | Courts reject deployment; service members refuse |

---

## Category G — Federalism

| # | Scenario | File | Provision | Stress Path | Expected Outcome |
|---|----------|------|-----------|-------------|-----------------|
| G1 | [x] State Democratic Backsliding (existing) | `state-democratic-backsliding.json` | Art. VII §1.5, §1.6 | State dismantles free elections; Congress misses remedy deadline | Federal election administration; representation suspension |
| G2 | [x] Federal Commandeering of State Officials | `federal-commandeering.json` | Art. VII §1.2 | Congress statute requires state executives to implement federal program | Courts void the commandeering statute |

---

## Category H — Presidential Accountability

| # | Scenario | File | Provision | Stress Path | Expected Outcome |
|---|----------|------|-----------|-------------|-----------------|
| H1 | [x] President Obstructs Investigation (existing) | `president-obstructs-investigation.json` | Art. III §15.8, §10.2A | President interferes with ACC investigation | Certification; House fallback; RA trial |
| H2 | [x] Post-Presidential Prosecution | `post-presidential-prosecution.json` | Art. III §15.6 | Former president claims residual immunity after leaving office | No post-presidential immunity; prosecution proceeds |

---

## Category I — Presidential Recall

| # | Scenario | File | Provision | Stress Path | Expected Outcome |
|---|----------|------|-----------|-------------|-----------------|
| I1 | [x] Presidential Recall Interference | `presidential-recall-interference.json` | Art. III §14.5, §14.11 | President declares emergency to delay certified recall referendum | Violation; court voids delay; referendum held on schedule |

---

## Category J — Presidential Succession

| # | Scenario | File | Provision | Stress Path | Expected Outcome |
|---|----------|------|-----------|-------------|-----------------|
| J1 | [x] President and VP Both Incapacitated | `presidential-succession-gap.json` | Art. III §12.2 | Simultaneous incapacity; Speaker assumes acting presidency with limited powers | Clean succession; §12.4 limits apply |
| J2 | [x] Contested Incapacity Declaration | `contested-incapacity-declaration.json` | Art. III §11.3 | VP and Cabinet declare incapacity; President contests; Congress must resolve | 21-day resolution period; possible medical panel |

---

## Category K — Rights

| # | Scenario | File | Provision | Stress Path | Expected Outcome |
|---|----------|------|-----------|-------------|-----------------|
| K1 | [x] Warrantless Domestic Surveillance | `warrantless-surveillance.json` | Art. V §4, Art. XI §8 | Intelligence agency conducts warrantless surveillance of domestic political groups | Violation; court orders halt; ACC prosecution |

---

## Implementation Notes

When adding a new scenario:
1. Create a JSON file in `simulation/scenarios/`
2. Add event handlers to `simulation/run.py` for any new event types
3. Run `python3 simulation/run.py --all --out-dir simulation/reports --save-full --save-json --save-aggregate`
4. Log findings in `design-notes/simulation-findings.md`

Each scenario should isolate one system, test both the stress path and the constitutional response, and produce a deterministic output that can be compared across drafting iterations.
