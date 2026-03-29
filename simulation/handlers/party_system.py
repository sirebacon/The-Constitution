from __future__ import annotations

from typing import Any

from sim_core import SimulationState


def handle_cartelized_ballot_access_barriers_imposed(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    details = event.get("details", {})
    barrier = details.get("barrier", "extraordinary signature and filing barriers targeted at new parties")
    state.provisions.update({"Article I Section 9.1", "Article I Section 9.4", "Article V Section 2.5"})
    state.add_violation(
        "cartelized_ballot_access_barriers",
        "party_cartelization",
        "State election authorities and dominant parties",
        f"State election authorities, under pressure from the dominant parties, impose {barrier} in a manner designed to keep new parties and independent entrants off the ballot. Article I Section 9.1 creates a constitutional qualification floor for party ballot access, and Section 9.4 bars prohibiting party formation or operation on ideological or political grounds.",
        "Article I Section 9.1 and Section 9.4; Article V Section 2.5",
        day,
    )
    state.add_obligation(
        "court_void_cartelized_ballot_access_barriers",
        "Federal courts",
        "void ballot-access barriers that functionally defeat the constitutional party-qualification rules or discriminate against new entrants for partisan advantage",
        "Article I Section 9.1 and Section 9.4; Article V Section 2.5",
        day,
        day + 21,
        severity="high",
    )


def handle_court_voids_cartelized_ballot_access_barriers(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    state.resolve_obligation(
        "court_void_cartelized_ballot_access_barriers",
        day,
        "voided the cartelized ballot-access barriers and ordered ballot qualification under the constitutional party-qualification rules",
    )
    state.add_entry(
        day,
        "outcome",
        "The scenario validates that Article I already provides a meaningful constitutional foothold against overt ballot-access cartelization by dominant parties and cooperating state authorities.",
        "Article I Section 9.1 and Section 9.4; Article V Section 2.5",
    )


def handle_dominant_parties_collude_to_exclude_debates_and_infrastructure(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    details = event.get("details", {})
    exclusion = details.get("exclusion", "debates, data feeds, and routine election-information channels")
    state.provisions.update({"Article I Section 9.4", "Article V Section 2.5", "Article VII"})
    state.add_violation(
        "party_cartel_soft_exclusion",
        "structural_gap",
        "Dominant parties and affiliated intermediaries",
        f"Dominant parties and affiliated intermediaries coordinate to deny qualified new entrants access to {exclusion} while preserving formal ballot access. The current Constitution clearly protects party formation and ballot qualification, but it is less explicit about cartelized exclusion from the softer infrastructure of meaningful contestation once ballot access itself is achieved.",
        "Article I Section 9.4; Article V Section 2.5; Article VII",
        day,
    )
    state.add_obligation(
        "electoral_commission_review_party_cartel_soft_exclusion",
        "Electoral Commission",
        "determine whether existing constitutional and statutory authority is sufficient to remedy coordinated exclusion of qualified entrants from core campaign infrastructure short of ballot denial",
        "Article I Section 9.4; Article V Section 2.5; Article VII",
        day,
        day + 21,
        severity="high",
    )


def handle_electoral_commission_finds_no_clear_remedy_for_soft_party_cartelization(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    state.resolve_obligation(
        "electoral_commission_review_party_cartel_soft_exclusion",
        day,
        "found no clear direct constitutional remedy because the exclusion preserved formal ballot access and operated through party-controlled or quasi-private infrastructure rather than through explicit state ballot denial",
    )
    state.add_entry(
        day,
        "outcome",
        "This scenario exposes a quieter party-system gap. The draft is stronger against formal exclusion than against coordinated soft cartelization that preserves legal competition in form while degrading it in practice.",
        "Article I Section 9.4; Article V Section 2.5; Article VII",
    )


HANDLERS = {
    "cartelized_ballot_access_barriers_imposed": handle_cartelized_ballot_access_barriers_imposed,
    "court_voids_cartelized_ballot_access_barriers": handle_court_voids_cartelized_ballot_access_barriers,
    "dominant_parties_collude_to_exclude_debates_and_infrastructure": handle_dominant_parties_collude_to_exclude_debates_and_infrastructure,
    "electoral_commission_finds_no_clear_remedy_for_soft_party_cartelization": handle_electoral_commission_finds_no_clear_remedy_for_soft_party_cartelization,
}
