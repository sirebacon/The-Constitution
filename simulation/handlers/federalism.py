from __future__ import annotations

from typing import Any

from sim_core import SimulationState


def handle_supreme_court_finds_state_democratic_floor_violation(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    actor = event.get("actor", "Unknown actor")
    details = event.get("details", {})
    state.provisions.update({"Article X Section 1.5", "Article X Section 1.6"})
    state.add_entry(day, "event", "Supreme Court finds persistent and material violation of the democratic floor.", "Article X Section 1.6(a)")
    state.add_obligation(
        "congress_state_remedy",
        "Congress",
        "enact a remedial measure for the violating state",
        "Article X Section 1.6(b)",
        day,
        day + 180,
        severity="high",
    )


def handle_congress_fails_state_remedy(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    actor = event.get("actor", "Unknown actor")
    details = event.get("details", {})
    state.fail_obligation(
        "congress_state_remedy",
        day,
        "Congress failed to enact a remedial measure for the violating state by day 180 under Article X Section 1.6(b).",
    )
    state.add_entry(day, "event", "Congress fails to enact a timely remedy for the state democratic-floor violation.", "Article X Section 1.6(b)")
    state.add_obligation(
        "congress_vote_state_suspension",
        "Congress",
        "hold a recorded vote on suspension of the state's representation",
        "Article X Section 1.6(c)",
        day,
        day + 30,
        severity="high",
    )
    state.add_entry(
        day,
        "outcome",
        "Federal elections in the state shift immediately to federally supervised administration through the Electoral Commission pending congressional action or Supreme Court certification of compliance.",
        "Article X Section 1.6(c)",
    )


def handle_state_violation_persists_one_year(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    actor = event.get("actor", "Unknown actor")
    details = event.get("details", {})
    state.add_entry(day, "event", "The state remains in material violation one year after the Supreme Court finding.", "Article X Section 1.6(d)")
    state.add_entry(
        day,
        "outcome",
        "If suspension has not already taken effect, it becomes automatic at the one-year mark under the constitutional backstop.",
        "Article X Section 1.6(d)",
    )


def handle_congress_suspends_representation(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    actor = event.get("actor", "Unknown actor")
    details = event.get("details", {})
    state.resolve_obligation(
        "congress_vote_state_suspension",
        day,
        "held the required vote and suspended the state's representation pending Supreme Court certification of compliance",
    )


def handle_congress_enacts_commandeering_statute(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    actor = event.get("actor", "Unknown actor")
    details = event.get("details", {})
    state.provisions.add("Article X Section 1.2")
    state.add_violation(
        "federal_commandeering",
        "federalism_breach",
        "Congress",
        "Congress enacts a statute requiring state executive officials to implement and enforce a federal regulatory program, in violation of the anti-commandeering provision of Article X Section 1.2.",
        "Article X Section 1.2",
        day,
    )
    state.add_obligation(
        "court_void_commandeering",
        "Federal courts",
        "void the federal commandeering statute",
        "Article X Section 1.2",
        day,
        day + 15,
        severity="high",
    )


def handle_state_refuses_commandeering(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    actor = event.get("actor", "Unknown actor")
    details = event.get("details", {})
    state.add_entry(
        day,
        "event",
        "State officials refuse to execute the commandeering statute and seek judicial relief.",
        "Article X Section 1.2",
    )


def handle_court_voids_commandeering_statute(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    actor = event.get("actor", "Unknown actor")
    details = event.get("details", {})
    state.resolve_obligation(
        "court_void_commandeering",
        day,
        "voided the federal commandeering statute",
    )


def handle_federal_government_asserts_implied_field_preemption(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    details = event.get("details", {})
    subject = details.get("subject", "environmental regulation")
    stricter_rule = details.get("stricter_rule", "a stricter state protection")
    state.provisions.update({"Article X Section 4.1", "Article X Section 4.3", "Article X Section 4.4"})
    state.add_violation(
        "implied_field_preemption_overreach",
        "federalism_breach",
        "Federal government",
        f"Federal officials assert that federal regulation of {subject} automatically occupies the field and displaces {stricter_rule} even though Congress did not expressly preempt the state rule and the subject is outside the narrow domains of implied field preemption preserved by Article X Section 4.3.",
        "Article X Section 4.1, Section 4.3, and Section 4.4",
        day,
    )
    state.add_obligation(
        "court_reject_implied_field_preemption_overreach",
        "Federal courts",
        "reject the implied field preemption claim and preserve stricter concurrent state regulation where Congress has not expressly preempted the field",
        "Article X Section 4.1, Section 4.3, and Section 4.4",
        day,
        day + 20,
        severity="high",
    )


def handle_court_rejects_implied_field_preemption_overreach(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    state.resolve_obligation(
        "court_reject_implied_field_preemption_overreach",
        day,
        "held that implied field preemption is abolished in the regulated domain, found no express preemption, and preserved the stricter state rule as valid concurrent regulation",
    )
    state.add_entry(
        day,
        "outcome",
        "The scenario validates that Article X sharply limits implied field preemption and preserves concurrent state regulation outside the few constitutionally uniform national domains.",
        "Article X Section 4.1, Section 4.3, and Section 4.4",
    )


def handle_state_preempts_local_housing_rule_without_showing_statewide_interest(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    details = event.get("details", {})
    ordinance = details.get("ordinance", "a local housing ordinance")
    state.provisions.update({"Article X Section 8.1", "Article X Section 8.2", "Article X Section 8.3"})
    state.add_violation(
        "state_local_preemption_overreach",
        "federalism_breach",
        "State government",
        f"State officials nullify {ordinance} with only generalized claims of statewide uniformity and no specific, compelling statewide interest shown by clear and convincing evidence, despite Article X's protection for local self-government on matters of local concern.",
        "Article X Section 8.1, Section 8.2, and Section 8.3",
        day,
    )
    state.add_obligation(
        "court_review_local_preemption_overreach",
        "State or federal courts",
        "review the state override under heightened scrutiny and enjoin it unless the state demonstrates a specific compelling statewide interest that cannot be served by less intrusive means",
        "Article X Section 8.2 and Section 8.3",
        day,
        day + 21,
        severity="high",
    )


def handle_court_blocks_local_preemption_overreach(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    state.resolve_obligation(
        "court_review_local_preemption_overreach",
        day,
        "blocked the state override after finding that the asserted statewide interests were generalized and that the state had not shown by clear and convincing evidence that preemption was necessary",
    )
    state.add_entry(
        day,
        "outcome",
        "The scenario validates that Article X gives local self-government meaningful protection against broad state nullification of local housing, labor, and environmental ordinances without disabling genuine statewide minimum standards.",
        "Article X Section 8.1, Section 8.2, and Section 8.3",
    )


def handle_state_asserts_extraterritorial_jurisdiction_over_digital_conduct(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    details = event.get("details", {})
    actor = details.get("actor", "an out-of-state speaker")
    conduct = details.get("conduct", "lawful digital publication")
    state.provisions.update({"Article X Section 5.5", "Article X Section 9.2"})
    state.add_violation(
        "extraterritorial_digital_jurisdiction",
        "federalism_breach",
        "State government",
        f"State officials attempt to apply their law to {actor} for {conduct} that occurred entirely outside the state, relying only on the fact that the digital content reached an in-state audience. Article X bars a state from asserting jurisdiction over out-of-state digital conduct based solely on audience reach or downstream effects.",
        "Article X Section 5.5 and Section 9.2",
        day,
    )
    state.add_obligation(
        "court_block_extraterritorial_digital_jurisdiction",
        "State or federal courts",
        "block the state's attempt to apply its law extraterritorially to out-of-state digital conduct absent a constitutionally sufficient nexus",
        "Article X Section 5.5 and Section 9.2",
        day,
        day + 21,
        severity="high",
    )


def handle_court_blocks_extraterritorial_digital_jurisdiction(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    state.resolve_obligation(
        "court_block_extraterritorial_digital_jurisdiction",
        day,
        "blocked the state's extraterritorial assertion of jurisdiction after finding that the conduct occurred outside the state and that audience reach alone did not supply the required nexus",
    )
    state.add_entry(
        day,
        "outcome",
        "The scenario validates Article X's modern territorial rule for digital conduct: a state may not project its law across borders merely because online activity was visible or had downstream effects within the state.",
        "Article X Section 5.5 and Section 9.2",
    )


def handle_state_asserts_jurisdiction_over_tribal_lands(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    details = event.get("details", {})
    tribe = details.get("tribe", "a recognized tribal nation")
    conduct = details.get("conduct", "a criminal prosecution against a tribal member for conduct occurring on tribal land")
    state.provisions.update(
        {
            "Article X Section 10.1",
            "Article X Section 10.4",
            "Article X Section 10.5",
            "Article X Section 10.7",
        }
    )
    state.add_violation(
        "state_tribal_jurisdiction_overreach",
        "federalism_breach",
        "State government",
        f"State officials attempt to exercise civil or criminal jurisdiction over {tribe} through {conduct} without tribal consent or express congressional authorization, despite Article X's tribal-sovereignty protections and recognition of tribal courts.",
        "Article X Section 10.1, Section 10.4, Section 10.5, and Section 10.7",
        day,
    )
    state.add_obligation(
        "court_block_state_tribal_jurisdiction_overreach",
        "Federal courts",
        "block the state's assertion of jurisdiction and recognize the tribal court as the competent first-instance forum within its proper domain",
        "Article X Section 10.4, Section 10.5, and Section 10.7",
        day,
        day + 21,
        severity="high",
    )


def handle_court_blocks_state_tribal_jurisdiction_overreach(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    state.resolve_obligation(
        "court_block_state_tribal_jurisdiction_overreach",
        day,
        "blocked the state's assertion of jurisdiction and required deference to the tribal court within its proper domain",
    )
    state.add_entry(
        day,
        "outcome",
        "The scenario validates that Article X now supplies a real tribal-sovereignty framework rather than a bare commerce-clause reference: tribal courts are recognized, and states may not unilaterally extend jurisdiction onto tribal lands.",
        "Article X Section 10.1, Section 10.4, Section 10.5, and Section 10.7",
    )


def handle_state_dismantles_judicial_independence(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    details = event.get("details", {})
    changes = details.get(
        "changes",
        "two-year judicial terms, salary reductions during active service, and elimination of an independent judicial conduct body",
    )
    state.provisions.update({"Article X Section 1.5", "Article X Section 1.5A"})
    state.add_violation(
        "state_judicial_independence_breach",
        "constitutional_floor_breach",
        "State government",
        f"State officials restructure the judiciary through {changes}, undermining the minimum judicial-independence standards that Article X makes part of the democratic floor.",
        "Article X Section 1.5 and Section 1.5A",
        day,
    )
    state.add_obligation(
        "court_block_state_judicial_independence_breach",
        "Federal courts",
        "hold that the state's judicial restructuring violates the democratic floor and enjoin the noncompliant measures",
        "Article X Section 1.5 and Section 1.5A",
        day,
        day + 30,
        severity="high",
    )


def handle_court_blocks_state_judicial_independence_breach(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    state.resolve_obligation(
        "court_block_state_judicial_independence_breach",
        day,
        "held that the state judicial changes violated the democratic-floor minimum standards for terms, compensation, removal protections, and judicial discipline",
    )
    state.add_entry(
        day,
        "outcome",
        "The scenario validates that Article X's democratic-floor language no longer leaves state judicial independence to implication alone; it now supplies concrete minimum standards that courts can enforce directly.",
        "Article X Section 1.5 and Section 1.5A",
    )


def handle_state_restricts_voting_access_below_floor(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    details = event.get("details", {})
    measures = details.get(
        "measures",
        "ending automatic registration, eliminating early voting, and limiting absentee voting to narrow excuse categories",
    )
    state.provisions.update({"Article X Section 1.5", "Article X Section 1.7A"})
    state.add_violation(
        "state_voting_access_floor_breach",
        "election_restriction",
        "State government",
        f"State officials attempt to run state elections under rules that reduce access below the constitutional floor by {measures}.",
        "Article X Section 1.5 and Section 1.7A",
        day,
    )
    state.add_obligation(
        "court_restore_state_voting_access_floor",
        "Federal courts",
        "block the restrictive state-election rules and restore the voting-access floor required by Article X",
        "Article X Section 1.5 and Section 1.7A",
        day,
        day + 21,
        severity="high",
    )


def handle_court_restores_state_voting_access_floor(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    state.resolve_obligation(
        "court_restore_state_voting_access_floor",
        day,
        "blocked the restrictive state-election rules and ordered restoration of automatic registration, early voting, and no-excuse absentee access consistent with the constitutional floor",
    )
    state.add_entry(
        day,
        "outcome",
        "The scenario validates that Article X now protects state-election access directly rather than relying only on federal-election rules or campaign-finance floors.",
        "Article X Section 1.5 and Section 1.7A",
    )


HANDLERS = {
    "supreme_court_finds_state_democratic_floor_violation": handle_supreme_court_finds_state_democratic_floor_violation,
    "congress_fails_state_remedy": handle_congress_fails_state_remedy,
    "state_violation_persists_one_year": handle_state_violation_persists_one_year,
    "congress_suspends_representation": handle_congress_suspends_representation,
    "congress_enacts_commandeering_statute": handle_congress_enacts_commandeering_statute,
    "state_refuses_commandeering": handle_state_refuses_commandeering,
    "court_voids_commandeering_statute": handle_court_voids_commandeering_statute,
    "federal_government_asserts_implied_field_preemption": handle_federal_government_asserts_implied_field_preemption,
    "court_rejects_implied_field_preemption_overreach": handle_court_rejects_implied_field_preemption_overreach,
    "state_preempts_local_housing_rule_without_showing_statewide_interest": handle_state_preempts_local_housing_rule_without_showing_statewide_interest,
    "court_blocks_local_preemption_overreach": handle_court_blocks_local_preemption_overreach,
    "state_asserts_extraterritorial_jurisdiction_over_digital_conduct": handle_state_asserts_extraterritorial_jurisdiction_over_digital_conduct,
    "court_blocks_extraterritorial_digital_jurisdiction": handle_court_blocks_extraterritorial_digital_jurisdiction,
    "state_asserts_jurisdiction_over_tribal_lands": handle_state_asserts_jurisdiction_over_tribal_lands,
    "court_blocks_state_tribal_jurisdiction_overreach": handle_court_blocks_state_tribal_jurisdiction_overreach,
    "state_dismantles_judicial_independence": handle_state_dismantles_judicial_independence,
    "court_blocks_state_judicial_independence_breach": handle_court_blocks_state_judicial_independence_breach,
    "state_restricts_voting_access_below_floor": handle_state_restricts_voting_access_below_floor,
    "court_restores_state_voting_access_floor": handle_court_restores_state_voting_access_floor,
}
