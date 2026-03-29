# Constitution Improvement Queue

This document turns the scorecard into a working revision queue. Use it to decide what to fix next, why it matters, and what “done” should look like.

---

## Priority Rules

Use this order when deciding what to work on:

1. Fix contradictions, stale cross-references, and structural incoherence
2. Fix enforceability problems
3. Simplify over-detailed constitutional text
4. Tighten legitimacy and abuse-resistance where gaps remain
5. Polish prose and presentation

---

## Active Priorities

| Priority | Area | Why It Matters | Main Issue | Target Outcome |
|----------|------|----------------|------------|----------------|
| 1 | Simulation coverage gaps | The highest-leverage remaining work is direct validation of articles whose text is stronger than their scenario coverage | Articles V, X, and XVIII still lack the dedicated scenario pressure their enforceability scores imply they need | A draft whose medium-risk articles are directly tested rather than only textually improved |
| 2 | Article IV provision validation | Shadow-docket transparency, recusal enforcement, and Conduct Board deadlock rules were recently strengthened but not yet directly simulated | The score should rest on validated operation, not only doctrinal improvement | Dedicated scenarios that confirm the new Article IV provisions work under stress |
| 3 | Article VIII / Article XIII boundary review | Ethics and agency architecture are both stronger, but their overlap needs one clean final check | Article VIII still contains a specific market regulator while Article XIII governs agencies generally | A clean boundary between ethics enforcement and general agency design |
| 4 | Article XII / Article XIX continuity edge cases | The current fallback model works, but it still deserves adversarial pressure | Internal boycott, quorum sabotage, and organ-setup friction remain the most plausible continuity edge cases | Continuity backstops that hold under hostile conditions without adding new machinery |
| 5 | Article IX citizenship scenarios | The article is structurally improved but still under-validated | Loss-of-citizenship, overseas assignment, and sensitive-office restrictions remain lightly tested | Clear outcomes in hostile membership and eligibility cases |
| 6 | Article II draft-discipline cleanup | The legislature article still carries the lowest draft-discipline score among the core structural articles | Enforcement and continuity mechanics can still sprawl even when they are conceptually sound | A leaner legislature article that preserves the floor while moving more process detail to law |

See also: [presidential-system-hardening.md](presidential-system-hardening.md)

---

## Legislative Deadline Matrix

This matrix converts the current simulator bottlenecks into explicit keep/change decisions. The goal is to avoid repeatedly revisiting deadline failures that are already backed by an acceptable automatic constitutional consequence.

| Scenario | Deadline Failure | Current Consequence | Keep or Change | Reason |
|----------|------------------|---------------------|----------------|--------|
| Unauthorized military action | Congress misses day-30 force authorization | Article XVI already treats missed authorization as nonauthorization for all purposes, triggering withdrawal-order and fiscal-hold sequence | Keep | The constitutional consequence is already automatic; the bottleneck reflects political failure, not missing text |
| Unauthorized military action | House misses war-powers impeachment vote | Article III Section 10.2A already transmits the certified charge automatically to the Regional Assembly | Keep | The House miss is already bypassed by an operative fallback |
| Coordinated absenteeism required vote | Congress misses day-30 force authorization through organized obstruction | Default nonauthorization still applies, and Article II Section 15A.4 now classifies coordinated absentee obstruction as constitutional-process obstruction | Keep | This path is now covered both substantively and normatively |
| President obstructs investigation | House misses expedited impeachment vote | Article III Section 10.2A already supplies automatic transmission to the Regional Assembly after House nonperformance | Keep | Same logic as the war-powers impeachment path; additional hardening is not obviously worth the extra complexity |
| Emergency extension without real review | Regional Assembly misses day-30 emergency review vote | Article III Section 5.4 already causes automatic lapse and voids continued emergency measures | Keep | The current consequence is strong, immediate, and already one of the cleanest automatic defaults in the draft |
| Emergency near election | Regional Assembly misses day-30 emergency review vote | Same automatic lapse and voiding rule under Article III Section 5.4 | Keep | Same reason; this is a residual political-risk scenario, not a text gap |
| Contested incapacity declaration | Congress misses day-23 contest resolution vote | Article III Section 11.3 already returns presidential powers if Congress does not sustain the incapacity determination | Keep | The Constitution already provides a clear status-default, and forcing a harsher consequence would risk biasing a contested incapacity process |
| PMC substitution | House misses expedited impeachment vote | Article III Section 10.2A already supplies the same automatic transmission fallback | Keep | The impeachment fallback is already doing the work it was designed to do |
| State democratic backsliding | Congress misses day-180 remedial legislation deadline | Article X Section 1.6 already starts automatic federal election administration and later hard suspension timelines | Keep | This path already has a meaningful automatic consequence and was previously misread as a gap when it was not |

### Separate Non-Legislative Follow-Up

These still matter, but they are not legislative missed-vote problems and should be tracked separately:

- Accountability Commission certification delay in the presidential-obstruction path
- Constitutional Organs setup delay after ratification
- Supreme Court delay in expedited constitutional cases

Those belong to Article XII / Article XIX / Article IV review, not to further broadening Article II default-vote machinery.

---

## Article-by-Article Queue

### Article I — Electoral System

| Task | Priority | Reason | Done When |
|------|----------|--------|-----------|
| Trim administrative detail | Medium | Some procedures may belong in statute or commission rules | Core electoral principles remain, implementation detail is reduced |
| Stress-test referendum and recall thresholds | Medium | Thresholds should be hard to game but not impossible to meet | Participation and signature rules feel realistic and defensible |

### Article II — Legislature

| Task | Priority | Reason | Done When |
|------|----------|--------|-----------|
| Map every remaining constitutionally required vote with a live missed-deadline bottleneck | High | Legislative deadline failure is now the dominant system weakness | Each recurring scenario has an explicit determination on whether the current default is sufficient or needs hardening |
| Review anti-obstruction consequences for coordinated nonperformance | High | The text now covers coordinated absenteeism, but not every missed-vote chain has been revisited in that light | The highest-risk paths have a clear answer on sabotage versus ordinary nonperformance |
| Reduce procedural code density | Medium | Legislature article is strong but detailed | Structural rules remain while legislative mechanics are simplified |
| Review deadlock and oversight timelines | Medium | Tight timelines can break in practice | Deadlines are realistic under actual institutional load |
| Re-check subpoena enforcement detail | Medium | Oversight enforcement still reads somewhat code-like | The article preserves strong oversight without over-specifying marshals, detention, or execution detail |

### Article III — Executive

| Task | Priority | Reason | Done When |
|------|----------|--------|-----------|
| Revisit emergency-review and impeachment bottlenecks with Article II continuity/default rules in mind | High | The text is structurally stronger, but Regional Assembly and House nonperformance still recur in the suite | The remaining missed-vote paths are either accepted as political-risk residuals or narrowed further by constitutional default rules |
| Review recall design for practicality | Medium | National recall is structurally unusual | Thresholds and timing feel constitutional, not aspirational only |
| Expand emergency-review simulation coverage | Medium | Emergency review is still the clearest recurring legislative bottleneck | Recess, leadership obstruction, nonapproval, and redeclaration scenarios all produce one clear answer |

### Article IV — Judiciary

| Task | Priority | Reason | Done When |
|------|----------|--------|-----------|
| Review whether the current anti-delay stack is sufficient | High | Notice duty, conduct review, temporary lower-court effect, and party-level finality now exist, but judicial-delay bottlenecks still appear | There is a clear decision to stop where the article is, or one narrowly justified further hardening step |
| Simplify appointment and governance machinery | High | The article is improved, but still denser than most of the draft | Appointment process and court governance can be summarized more cleanly without losing safeguards |
| Re-check lower court design and senior-justice fallback rules | Medium | The institutional model should remain coherent after the continuity revisions | Terms, senior status, and fallback duties fit the overall judicial philosophy |

### Article V — Civil and Political Rights

| Task | Priority | Reason | Done When |
|------|----------|--------|-----------|
| Distinguish constitutional principle from statutory implementation | High | Some rights clauses are too operational | Rights language becomes shorter and more durable |
| Review speech and religion carve-outs for narrowness | High | These areas are vulnerable to overreach or ambiguity | Exceptions are clearly bounded and easier to defend |
| Re-check digital rights for constitutional level of abstraction | Medium | Some protections may be too technology-specific | Text protects principles that survive tech change |

### Article VI — Democratic Integrity

| Task | Priority | Reason | Done When |
|------|----------|--------|-----------|
| Stress-test media-pluralism enforcement | Medium | Good principle, but implementation can be hard | Enforcement architecture is clean and speech-safe |
| Re-check anti-subversion boundary lines | Medium | Must punish coups without chilling lawful contestation | Protected challenge and prohibited subversion are sharply distinguished |

### Article X — Federalism and the States

| Task | Priority | Reason | Done When |
|------|----------|--------|-----------|
| Review preemption rules for administrability | Medium | Clear preemption is good, but edge cases matter | Courts could apply the rules without making new doctrine by guesswork |
| Stress-test the revised democratic-floor fallback | Medium | The election-administration snap-in is stronger, but still needs more scenario pressure | The Article VII pathway remains clear under sabotage, delay, and partial compliance scenarios |

### Article XI — Amendments

| Task | Priority | Reason | Done When |
|------|----------|--------|-----------|
| Reassess judicial pre-clearance scope | High | Too much pre-clearance can over-judicialize amendment politics | Review is narrow, legitimate, and not dominant over ratification |
| Re-test the unamendable core | High | Must protect democracy without freezing too much | The core feels principled and limited rather than expansive |

### Article XII — Constitutional Organs

| Task | Priority | Reason | Done When |
|------|----------|--------|-----------|
| Reduce cross-reference dependence | High | This article is central and should stand on its own | Core powers are understandable without constant external lookup |
| Simplify commission detail | High | Dense institutional design can still create fragility | Organ design stays narrow but reads more clearly |
| Reconcile organ-delay fallback with the permanent article text | Medium | Article XIX now supplies a validated bridge, but the permanent organ article should read cleanly alongside it | The transition fallback and permanent commission architecture feel integrated rather than patched together |

### Article XIII — Federal Agencies

| Task | Priority | Reason | Done When |
|------|----------|--------|-----------|
| Separate constitutional rules from administrative-code detail | High | This article most often drifts into statutory granularity | Only truly constitutional constraints remain in-text |
| Review revolving-door framework for generality | Medium | The principle is strong, but some specifics may be too narrow | The article sets a durable constitutional floor |

### Article XVI — War Powers and National Security

| Task | Priority | Reason | Done When |
|------|----------|--------|-----------|
| Stress-test enforcement against real command conditions | High | Crisis rules must work under actual pressure | Enforcement is tough but still operationally plausible |
| Re-check automatic withdrawal and compliance mechanics | Medium | Strong safeguards can become unworkable if too rigid | The remedy is both credible and administrable |

### Article VII — Campaign Finance and Political Money

| Task | Priority | Reason | Done When |
|------|----------|--------|-----------|
| Compress detailed compliance mechanics | High | This article is strong but very code-like | Constitutional principles remain while implementation is pushed downward |
| Review state-floor interaction | Medium | Federal and state campaign-finance interaction can get complex | Floor rules and state discretion are cleanly separated |

### Article XVIII — Social, Economic, and Affirmative Rights

| Task | Priority | Reason | Done When |
|------|----------|--------|-----------|
| Simplify positive-rights language | High | Some provisions risk sounding programmatic rather than constitutional | Core guarantees read as durable constitutional commitments |

### Article XVII — Foreign Policy and National Security

| Task | Priority | Reason | Done When |
|------|----------|--------|-----------|
| Keep boundary with Article XI sharp | High | Overlap between war and non-war powers creates confusion | A reader can tell immediately which article governs which action |
| Review gray-zone response authority | Medium | It is useful but susceptible to executive stretch | The authority is narrow, attributable, and reviewable |

### Article VIII — Government Ethics

| Task | Priority | Reason | Done When |
|------|----------|--------|-----------|
| Review investment and regulator rules for abstraction level | Medium | Some specifics may age poorly | The rule remains strong even if markets or instruments change |

### Cross-References and Draft Integration

| Task | Priority | Reason | Done When |
|------|----------|--------|-----------|
| Run consistency audit after every structural reorganization | Critical | This is the main source of drift | No stale article or section references remain after changes |
| Review drafting log for outdated summaries | Low | Historical notes can confuse current readers | Logs remain useful without contradicting current text |
| Keep simulator scenarios aligned with text revisions | High | Text-to-simulation drift is now a real maintenance risk | New constitutional fixes are exercised by at least one scenario and reflected in the reports |

---

## Current Sprint

Recommended next drafting sprint:

1. Review the non-legislative deadline bottlenecks: Accountability Commission certification delay, Constitutional Organs setup delay, and any remaining judicial-delay edge cases
2. Simplify Article XII
3. Review whether Article IV delay containment is now complete
4. Add or refresh targeted Article IX and fiscal edge-case scenarios

---

## How To Use This Queue

- Move a task up when it blocks multiple articles.
- Mark a task complete only when the scorecard score can defensibly rise.
- If a revision lowers complexity without lowering abuse resistance, that is usually a good trade.
- Re-score the affected article after every substantial revision round.
### Article IX — Citizenship and National Membership

| Task | Priority | Reason | Done When |
|------|----------|--------|-----------|
| Tighten loss-of-citizenship rule | High | Section 5.2 still leaves more discretion to future law than ideal | Involuntary loss standards are narrowly bounded and due-process protected |
| Add citizenship and eligibility scenarios | High | The de-duplicated structure has not yet been tested under hostile edge cases | Overseas assignment, proof disputes, and sensitive-office restrictions all produce clear outcomes |

### Article XIV and Article XV — Public Finance

| Task | Priority | Reason | Done When |
|------|----------|--------|-----------|
| Stress-test fiscal safeguards | Medium | The fiscal architecture is cleaner, but the moved rules need scenario pressure | Budget deadlock, CR manipulation, and classified-spending enforcement all point to the new article homes |
| Compress residual operational detail | Medium | Stronger fiscal safeguards can drift back toward code-like text | The articles keep constitutional principle while leaving implementation to law |

### Article XIX — Ratification and Transition

| Task | Priority | Reason | Done When |
|------|----------|--------|-----------|
| Stress-test first-cycle failure modes | High | Transition law is stronger, but not yet tested against non-cooperation and setup delay | Missed first-election law, organ-constitution delay, and outgoing obstruction scenarios all produce clear outcomes |
| Compress transition implementation detail | Medium | Some provisions still read like implementation code | First-cycle rules remain durable while operational detail is pushed down |
