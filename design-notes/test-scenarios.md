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
| B2 | [x] Budget Deadlock — Automatic CR | `budget-deadlock-cr.json` | Art. XV §3.2, §3.3 | Congress misses Oct 1 deadline; executive attempts selective CR funding | CR self-executes; court blocks manipulation |
| B3 | [x] Single-Subject Challenge | `single-subject-challenge.json` | Art. II §10.7A | Omnibus bill with unrelated riders passes both chambers | Supreme Court voids bill; returned for redrafting |
| B4 | [x] Perjury Before Congress | `perjury-before-congress.json` | Art. II §16.4 | Senior official gives known false testimony; DOJ declines to prosecute | ACC jurisdiction; automatic removal on conviction |
| B5 | [x] Member Bribery Shielded by Chamber | `member-bribery-shielded-by-chamber.json` | Art. II §5.3, §14.2; Art. VIII §1.4, §1.7 | Chamber leadership refuses expulsion after bribery; ACC proceeds anyway | Conviction triggers automatic removal |

---

## Category C — Judicial Independence

| # | Scenario | File | Provision | Stress Path | Expected Outcome |
|---|----------|------|-----------|-------------|-----------------|
| C1 | [x] Court Order Defied by Executive | `court-order-defied.json` | Art. II §16.2(c) | Executive refuses to comply with federal court enforcement order | Marshals enforce; contempt proceedings |
| C2 | [x] Judicial Vacancy Exploitation | `judicial-vacancy-exploitation.json` | Art. IV §2.7 | Chief Justice incapacitated; President refuses to confirm successor | Judicial continuity rule designates substitute |
| C3 | [x] Supreme Court Strategic Delay | `supreme-court-strategic-delay.json` | Art. IV §10.1, §10.4, §8.2 | Court withholds required delay notice and uses repeated nondecision to shape political timing | Judicial Conduct Board finds strategic delay as conduct-based misconduct |
| C4 | [x] Shadow Docket — Emergency Stay Without Explanation | `shadow-docket-unexplained-order.json` | Art. IV §9.7 | Supreme Court issues emergency stay without the required explanation; party moves to void | Originating court voids unexplained stay |
| C5 | [x] Justice Refuses Valid Recusal Demand | `justice-refuses-recusal.json` | Art. IV §7.3 | Judicial Conduct Board directs recusal; justice refuses | Automatic referral; justice barred from the case; removal proceedings may follow |
| C6 | [x] Judicial Conduct Board Certification Deadlock | `judicial-conduct-board-certification-deadlock.json` | Art. IV §8.1, §8.2 | Board misses 60-day certification deadline on judicial impeachment articles | 2/3 chamber override allows impeachment path to continue |

---

## Category D — War Powers

| # | Scenario | File | Provision | Stress Path | Expected Outcome |
|---|----------|------|-----------|-------------|-----------------|
| D1 | [x] Nuclear First-Use Circumvention | `nuclear-first-use-circumvention.json` | Art. XVI §3.1 | SecDef refuses first-use order; President fires him to find compliant replacement | Violation; acting SecDef also refuses; launch blocked |
| D2 | [x] Covert Operation Against US Citizen Without Warrant | `covert-operation-against-citizen.json` | Art. XVI §5.2 | CIA orders lethal strike on citizen; warrant denied as capture is feasible | Operation blocked; ACC prosecution if proceeds anyway |
| D3 | [x] Unauthorized Military Action (existing) | `unauthorized-military-action.json` | Art. XVI §1 | Congress misses AUMF window; President ignores withdrawal order | House fallback; Regional Assembly trial |
| D4 | [x] PMC Substitution for Authorized Forces | `pmc-substitution.json` | Art. XVI §4.4 | Congress denies AUMF; President deploys PMCs as substitute | Violation; expedited impeachment chain |
| D5 | [x] Coordinated Absenteeism to Defeat Required Vote | `coordinated-absenteeism-required-vote.json` | Art. II §15A.4; Art. XVI §1; Art. III §10.2A | House bloc coordinates absence and refuses continuity procedures to defeat mandatory impeachment vote | Conduct treated as obstruction; default consequence still applies and Regional Assembly trial proceeds |

---

## Category E — Emergency Powers

| # | Scenario | File | Provision | Stress Path | Expected Outcome |
|---|----------|------|-----------|-------------|-----------------|
| E1 | [x] Emergency Near Election Day (existing) | `emergency-near-election.json` | Art. III §5.3(a), §5.4 | Emergency restricts polling access; RA misses review deadline | Court blocks restriction; emergency lapses |
| E2 | [x] Emergency Extension Without Real Review (existing) | `emergency-extension-without-real-review.json` | Art. III §5.4, Art. V §1.3 | President self-extends lapsed emergency by memo | Violation; measures void |
| E3 | [x] Section 15A Enforcement — RA Blocks Emergency Vote | `ra-blocks-emergency-vote.json` | Art. II §15A, Art. III §5.4 | RA leadership blocks scheduling; presiding officer ignores motion | Mandamus issued; vote held within 30 days |
| E6 | [x] Recess Evasion — RA Runs Out Emergency Clock | `ra-recess-evasion.json` | Art. II §15A.1(e)-(f), Art. III §5.4 | RA enters recess on day 10 to evade 30-day deadline; §15A motion ignored; mandamus filed | Recess bars voided; court-ordered vote held before day 30 |
| E4 | [x] Emergency Used to Suppress Rights | `emergency-rights-suppression.json` | Art. III §5.3(f), Art. V | Emergency invoked to restrict protected speech | Violation; courts void restriction immediately |
| E5 | [x] Habeas Corpus Suspension by President Alone | `habeas-corpus-president-suspends.json` | Art. III §5.7 | President suspends habeas corpus by executive order | Violation; courts void; only Congress may suspend |

---

## Category F — Elections and Democracy

| # | Scenario | File | Provision | Stress Path | Expected Outcome |
|---|----------|------|-----------|-------------|-----------------|
| F1 | [x] Foreign Cyber Election Crisis (existing) | `foreign-cyber-election-crisis.json` | Art. I, V, VII, XI, XIV | Foreign hack; President attempts direct state takeover and speech suppression | Violations; courts block; non-military response used |
| F2 | [x] Electoral Certification Obstruction | `electoral-certification-obstruction.json` | Art. VI §1, Art. III §13 | President-elect certified; outgoing president refuses transition cooperation | Anti-subversion prosecution; transition proceeds |
| F3 | [x] Domestic Deployment Against Protest (existing) | `domestic-deployment-against-protest.json` | Art. XVI §7, §8 | Protest misclassified as rebellion; troops deployed | Courts reject deployment; service members refuse |

---

## Category G — Federalism

| # | Scenario | File | Provision | Stress Path | Expected Outcome |
|---|----------|------|-----------|-------------|-----------------|
| G1 | [x] State Democratic Backsliding (existing) | `state-democratic-backsliding.json` | Art. X §1.5, §1.6 | State dismantles free elections; Congress misses remedy deadline | Federal election administration; representation suspension |
| G2 | [x] Federal Commandeering of State Officials | `federal-commandeering.json` | Art. X §1.2 | Congress statute requires state executives to implement federal program | Courts void the commandeering statute |

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
| K1 | [x] Warrantless Domestic Surveillance | `warrantless-surveillance.json` | Art. V §5, Art. XV §6.5, Art. XVII §4.7 | Intelligence agency conducts warrantless surveillance of domestic political groups | Violation; court orders halt; ACC prosecution |
| K2 | [x] Government Suppression of Political Speech | `political-speech-suppression.json` | Art. V §2.1, §2.6 | Executive branch restricts political expression by content or viewpoint | Courts void the restriction |
| K3 | [x] State Equal Protection Violation | `state-equal-protection-violation.json` | Art. V §6.2, §7.2 | State enacts discriminatory classification based on sexual orientation | Courts apply strict scrutiny and void the law |
| K4 | [x] Overbroad Rights Suspension | `overbroad-rights-suspension.json` | Art. V §1.3, §14.3 | Congress attempts nationwide rights suspension without the constitutionally required judicial finding and narrow tailoring | Suspension never takes effect |
| K5 | [x] Data Purchase Warrant Circumvention | `data-purchase-warrant-circumvention.json` | Art. V §10.3, §5.3 | Government buys personal data from a broker to avoid the warrant requirement | Courts treat data as government-obtained and suppress it |

---

## Category L — Citizenship and Transition

| # | Scenario | File | Provision | Stress Path | Expected Outcome |
|---|----------|------|-----------|-------------|-----------------|
| L1 | [x] First Election Law Missed | `first-election-law-missed.json` | Art. XIX §4.1, §4.5 | Congress misses the first-election implementation deadline | Electoral Commission administers the first election under interim constitutional rules |
| L2 | [x] Constitutional Organs Delay | `constitutional-organs-delay.json` | Art. XIX §5.2, §5.2A | Congress and appointing authorities miss organ-constitution deadlines | Supreme Court bridge appointments create lawful temporary quorum and startup continuity |
| L3 | [x] Overseas Assignment Denied | `overseas-assignment-denied.json` | Art. IX; Art. I electoral application rules | Overseas citizen is wrongly denied political assignment and participation | Judicial correction restores assignment and participation rights |
| L4 | [x] Naturalized Candidate Excluded | `naturalized-candidate-excluded.json` | Art. IX; officeholding equality rules | Naturalized citizen is excluded from office without a constitutionally valid exception | Court rejects exclusion and restores eligibility |

---

## Category M — Amendments

| # | Scenario | File | Provision | Stress Path | Expected Outcome |
|---|----------|------|-----------|-------------|-----------------|
| M1 | [x] Unamendable Core Evasion | `unamendable-core-evasion.json` | Art. XI §3.1, §3.2, §4 | Congress proposes an authoritarian amendment that functionally narrows the electorate and weakens binding election results while pretending not to amend the core directly | Supreme Court rejects the amendment at pre-clearance under the unamendable core and principled backstop |
| M2 | [x] Rights Amendment Pre-Clearance Timeout | `rights-amendment-preclearance-timeout.json` | Art. XI §2, §4.3 | Rights-expanding amendment is submitted, but the Supreme Court misses the Track 2 pre-clearance deadline | Pre-clearance is deemed granted; ratification and national referendum proceed |

---

## Category N — Social, Economic, and Affirmative Rights

| # | Scenario | File | Provision | Stress Path | Expected Outcome |
|---|----------|------|-----------|-------------|-----------------|
| N1 | [x] Climate Backsliding Without Replacement | `climate-backsliding-without-replacement.json` | Art. XVIII §1.2, §1.4 | Government dismantles major climate protections without constitutionally sufficient replacement | Court declares violation and requires a remedial plan without prescribing policy instruments |
| N2 | [x] Education Floor Inequality | `education-floor-inequality.json` | Art. XVIII §2.2 | State leaves students in low-income districts with substantially inferior education | Court requires a lawful remedy sufficient to restore the constitutional floor |
| N3 | [x] Shelter Floor Failure — Withdrawal Without Replacement | `housing-floor-failure.json` | Art. XVIII §2.3, §2.4 | Government eliminates shelter programs without replacement, leaving a class without basic shelter | Court preserves against backsliding and requires constitutionally sufficient replacement |
| N4 | [x] Child Welfare Proceeding Without Independent Representation | `child-welfare-no-independent-representation.json` | Art. XVIII §4.5, §4.6 | State court terminates parental rights without independent representation for the child or stated reasons for departing from child's preference | Appellate court vacates and remands for constitutionally sufficient process |

## Category O — Oligarchic Pressure and Strategic Resilience

| # | Scenario | File | Provision | Stress Path | Expected Outcome |
|---|----------|------|-----------|-------------|-----------------|
| O1 | [x] Foreign Influence via Shell Entity Political Messaging | `foreign-influence-shell-funding.json` | Art. VI §5.1, §5.3, §5.5 | Foreign government routes destabilizing political messaging through a domestic shell entity | ACC pierces the conduit, orders sponsor disclosure, and penalizes the operation |
| O2 | [x] Federal Contractor with Concealed Foreign Beneficial Ownership | `contractor-foreign-beneficial-ownership.json` | Art. VIII §1.13; Art. XIII §9.3 | Foreign-state-linked entity conceals beneficial ownership while seeking sensitive federal contract | Concealed ownership itself becomes disqualifying even without separate bribery proof |
| O3 | [x] Foreign Acquisition of Critical Infrastructure | `critical-infrastructure-coercion.json` | Art. XIII §12 | Foreign-state-linked company acquires major telecom carrier | Congress orders divestiture under explicit critical-infrastructure continuity authority |
| O4 | [x] Deliberate Destruction of Public Records During Transition | `records-destruction-transition.json` | Art. XIX §6.5; Art. VI §1.1 | Outgoing officials destroy or conceal non-electoral federal records during transition | ACC prosecutes the destruction directly as anti-subversion conduct |
| O5 | [x] Executive Coercion of Platforms to Suppress Lawful Political Dissent | `executive-coerces-platform-suppression.json` | Art. V §2.1, §2.6; Art. XIII §2.0.5 | Executive officials pressure major platforms with threatened regulatory retaliation to suppress lawful dissent | Courts treat coercive suppression as state action and enjoin it; ACC investigates weaponization |
| O6 | [x] Coordinated Private Infrastructure Cutoff of Lawful Opposition Organization | `private-chokepoint-election-cutoff.json` | Art. V §2.6; Art. VII; Art. XIII | Dominant payment processors and hosting firms jointly cut off a lawful opposition organization during an election without proven state coercion | Scenario exposes a real under-tested gap: no clear direct constitutional remedy absent state action or foreign control |
| O7 | [x] Platform Denies Equal Candidate Access to Political Distribution Tools | `platform-denies-candidate-ad-tools.json` | Art. VI §7.5; Art. XII | Major platform denies a lawful federal candidate equal access to political advertising/distribution tools available to rivals | Electoral Commission orders nondiscriminatory access and opens audit |
| O8 | [x] Platform Manipulates Emergency and Election Information Visibility | `platform-manipulates-emergency-information-visibility.json` | Art. VI §7.5; Art. I; Art. V | Dominant platform materially downranks lawful emergency and election-administration information during a live crisis | Scenario exposes a narrower gap: transparency and audit exist, but no clear rapid corrective visibility remedy |
| O9 | [x] Dominant Parties Impose Cartelized Ballot-Access Barriers | `cartelized-ballot-access-barriers.json` | Art. I §9.1, §9.4; Art. V §2.5 | Dominant parties and cooperating state authorities impose extraordinary ballot-access barriers targeted at new entrants | Courts void the barriers under the constitutional party-qualification and association rules |
| O10 | [x] Dominant Parties Coordinate Soft Cartelization Without Formal Ballot Exclusion | `soft-party-cartelization.json` | Art. I §9.4; Art. V §2.5; Art. VII | Dominant parties preserve formal ballot access but exclude qualified entrants from debates and campaign-information infrastructure | Scenario exposes a quieter gap: soft cartelization remains harder to reach than overt ballot denial |

---

## Implementation Notes

When adding a new scenario:
1. Create a JSON file in `simulation/scenarios/`
2. Add any new event handlers under `simulation/handlers/` and ensure they are registered through the dispatcher
3. Run `python3 simulation/run.py --all --out-dir simulation/reports --save-full --save-json --save-aggregate`
4. Log findings in `design-notes/simulation-findings.md`

Each scenario should isolate one system, test both the stress path and the constitutional response, and produce a deterministic output that can be compared across drafting iterations.
