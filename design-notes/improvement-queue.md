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
| 1 | ~~Simulation coverage gaps~~ **DONE** | Articles V, IX, X, and XVIII now all have direct scenario coverage across their main live edge cases | Remaining validation work is now optional refinement rather than a meaningful coverage deficit | A draft whose remaining medium-risk articles are directly tested |
| 2 | ~~Article VIII / Article XIII boundary review~~ **DONE** | Ethics and agency architecture now state their boundary more cleanly: Article VIII owns substantive ethics and market-integrity duties, Article XIII owns general agency structure, and the stale Article XIII cross-reference to nonexistent Article VIII §2.10 is fixed | Remaining work is only light later compression of Article VIII §1.13 and some operational detail in Article XIII | No further action needed unless a later whole-draft pass surfaces new overlap |
| 3 | ~~Article XII / Article XIX continuity edge cases~~ **DONE** | The duplicate vacancy rule is now merged (§5.6), the internal-boycott scenario validates Article XII §5.5 under pressure, and the bridge-startup scenario now validates that Article XIX's temporary quorum becomes operational rather than merely formal | Remaining work is no longer a live continuity-design uncertainty; it is optional later sabotage/refusal refinement | Continuity backstops that hold under hostile conditions without adding new machinery |
| 4 | ~~Article IX citizenship scenarios~~ **DONE** | §5.2 loss-of-citizenship rule tightened with explicit procedural floor; overseas assignment, naturalized-candidate, sensitive-office, and proof-dispute scenarios now all exist | Only one optional later cleanup scenario remains for renunciation/statelessness/foreign-office incompatibility | No further action needed unless a later edge-case review surfaces a new exploit |
| 5 | ~~Article II draft-discipline cleanup~~ **DONE** | §16 compressed: drafting note deleted, auto-referral machinery removed, investigation-clock mechanics removed, §16.8 stated as principle; discipline 7.8 → 8.2 | §15A.4 remains dense but simulation-validated | No further action needed unless a later pass surfaces more compressible detail |
| 6 | ~~Private platform and infrastructure chokepoint power~~ **DONE** | Dominant-civic-intermediary scenarios are now built and Article VI §7.5A supplies a narrow constitutional continuity remedy | The remaining issue is later compression: keep the duty viewpoint-neutral and confined to indispensable civic intermediaries | No further action needed unless later scenarios show overbreadth or underreach |
| 7 | ~~Party-system degradation without formal dictatorship~~ **PARTIAL** | Overt ballot-access cartelization and soft cartelization scenarios are now built, and Article I §9.5 / §10.6 closes the core public-infrastructure exclusion gap | Quasi-private exclusion beyond public or publicly regulated election infrastructure still needs scenario pressure | Add one more scenario family for softer cartelization outside the new constitutional floor |

See also: [presidential-system-hardening.md](presidential-system-hardening.md)

---

## Current Weaknesses Snapshot

These are the main weaknesses of the draft in its current state. They are narrower than earlier structural gaps and should guide the next revision cycle.

1. Simulation coverage is now broad, with only optional cleanup scenarios left.
   Remaining validation work is mainly discretionary: one later Article IX nationality edge case, one later Article X cross-border variant, and any future “unknown gap” families the project decides are worth exploring.

2. Some core articles are still denser than ideal constitutional text.
   Article II remains the clearest draft-discipline outlier, and parts of Articles VIII, XIII, and XIX still risk reading more like advanced statutory design than near-final constitutional prose, even though the VIII/XIII boundary itself is now clearer.

3. Political nonperformance remains the dominant live stress pattern.
   The draft now usually supplies an automatic consequence, but the simulator still shows repeated missed deadlines, refusals to act, and delay chains under hostile conditions.

4. The new resilience clauses are good but may need later compression.
   The oligarchic-pressure hardening closed real gaps, but provisions such as contractor beneficial-ownership disclosure should eventually be checked for constitutional abstraction level.

5. Some resilience clauses are now stronger but may need later compression.
   Article VIII Section 1.13 is now doing more real work after the contractor-capture hardening, which increases the value of a later abstraction-level review.

6. A final cross-article edge-case pass is still needed.
   The remaining risk is less contradiction than boundary drift: emergency overlap, ethics/agency overlap, continuity overlap, and enforcement-path complexity.

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

**Non-legislative bottleneck decisions (closed):**

- **ACC certification delay** (presidential-obstruction path): Article III §10.2A already has a 7-day ACC deadline with a House-member backup certification path. The delay bottleneck reflects political nonperformance against existing machinery, not a text gap. **Decision: keep as political-risk residual. No text change warranted.**

- **Constitutional Organs setup delay**: Article XIX §5.2A already supplies Supreme Court bridge appointments as a backstop when ordinary appointment fails. The repeated missed-deadline bottleneck in simulation is the bridge mechanism working as designed. **Decision: keep as political-risk residual. No text change warranted.**

- **Article XII vacancy duplication**: Merged §2.8 and §3.8 into shared §5.6. **Done.**

- **Article II §16 discipline**: Drafting note deleted, three statutory-grade subsections compressed. Draft discipline 7.8 → 8.2. **Done.**

- **Article IX §5.2**: Explicit procedural floor added. **Done.**

- **Article XVIII scenarios**: All four N-series scenarios built and validated. **Done.**

**Completed this sprint:**

- **Art VIII / Art XIII boundary check**: Boundary is clean. Art VIII §2 owns substantive market-integrity rules; Art XIII owns general agency structure; cross-references (Art VIII §2.2 → Art XIII; Art XIII §7.1 → Art VIII §2 as floor) are correct. **No text changes warranted.**

- **Art XII internal boycott scenario**: Already built and validated as L7 in catalog. §5.5 anti-sabotage rule confirmed enforceable under adversarial pressure. **Done.**

- **Art IX sensitive-office and proof-dispute scenarios**: L5 (sensitive-office restriction overreach) and L6 (citizenship proof dispute) both built, validated, and cataloged. **Done.**

- **Art X preemption edge-case**: G3 (implied field preemption) and G4 (state preempts local housing) both built, validated, and cataloged. **Done.**

- **Quasi-private soft-cartel decision**: The O11 scenario confirms the gap exists — purely private coordination by dominant debate/data consortia can still degrade political competition outside the constitutional floor for public or publicly regulated infrastructure. **Decision: leave as statutory problem and flagged residual risk.** The constitutional floor (Art I §9.5, §10.6) reaches public or publicly regulated infrastructure; Congress may extend further by statute. Constitutionalizing private market conduct for non-state-sponsored actors at this level risks over-entrenchment.

- **Draft discipline pass**: Art IV §4.7A, §4.9, §10.1, §10.4 compressed — statutory-grade procedure (3-deadline trigger, lower-court reassignment mechanics) moved to "law shall provide" or removed. Art XI Rationale paragraphs removed from both tracks, §3.3 explanatory commentary removed, §5.2 standing list consolidated. Draft discipline: Art IV 8.0 → 8.3, Art XI 7.8 → 8.3, overall 8.8 → 8.9.

**Next sprint:**

1. Art XIX operational density — transition article has the second-lowest discipline score (7.8); targeted compression pass to identify any remaining implementation-code detail
2. Art VI §7.5A — watch for overbreadth; keep tightly limited to indispensable civic intermediaries; one more boundary scenario if needed
3. Final cross-article consistency pass after all discipline changes are settled

---

## How To Use This Queue

- Move a task up when it blocks multiple articles.
- Mark a task complete only when the scorecard score can defensibly rise.
- If a revision lowers complexity without lowering abuse resistance, that is usually a good trade.
- Re-score the affected article after every substantial revision round.
### Article IX — Citizenship and National Membership

| Task | Priority | Reason | Done When |
|------|----------|--------|-----------|
| ~~Tighten loss-of-citizenship rule~~ **DONE** | High | §5.2 now requires notice, independent tribunal, counsel, and judicial review before revocation | Done |
| ~~Add citizenship and eligibility scenarios~~ **DONE** | High | L3 (overseas), L4 (naturalized candidate), L5 (sensitive-office), L6 (proof dispute) all validated | Done |

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
