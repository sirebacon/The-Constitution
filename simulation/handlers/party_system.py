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
    state.provisions.update({"Article I Section 9.5", "Article I Section 10.6", "Article V Section 2.5"})
    state.add_violation(
        "party_cartel_soft_exclusion",
        "party_cartelization",
        "Dominant parties and affiliated intermediaries",
        f"Dominant parties and affiliated intermediaries coordinate to deny qualified new entrants access to {exclusion} while preserving formal ballot access. Article I Section 9.5 now protects nondiscriminatory access to core public or publicly regulated election infrastructure necessary for meaningful federal contestation.",
        "Article I Section 9.5 and Section 10.6; Article V Section 2.5",
        day,
    )
    state.add_obligation(
        "electoral_commission_review_party_cartel_soft_exclusion",
        "Electoral Commission",
        "determine whether the excluded entrants are lawfully qualified and order temporary nondiscriminatory access to core public or publicly regulated election infrastructure under Article I Section 9.5 and Section 10.6",
        "Article I Section 9.5 and Section 10.6; Article V Section 2.5",
        day,
        day + 10,
        severity="high",
    )


def handle_electoral_commission_orders_relief_for_soft_party_cartelization(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    state.resolve_obligation(
        "electoral_commission_review_party_cartel_soft_exclusion",
        day,
        "found that qualified entrants were being discriminatorily excluded from core public or publicly regulated election infrastructure, ordered temporary nondiscriminatory access, and required neutral participation criteria for the affected channels",
    )
    state.add_obligation(
        "court_review_soft_party_cartel_relief",
        "Federal courts",
        "review the temporary access order on an expedited basis and sustain it if it is limited to core public or publicly regulated election infrastructure necessary for meaningful federal contestation",
        "Article I Section 9.5 and Section 10.6; Article V Section 2.5",
        day,
        day + 7,
        severity="high",
    )


def handle_court_upholds_relief_for_soft_party_cartelization(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    state.resolve_obligation(
        "court_review_soft_party_cartel_relief",
        day,
        "upheld the temporary access order as a narrow remedy preserving meaningful electoral competition without compelling private ideological sponsorship beyond the constitutional floor",
    )
    state.add_entry(
        day,
        "outcome",
        "The scenario validates that Article I now reaches soft cartelization where qualified entrants are excluded from core public or publicly regulated election infrastructure even though formal ballot access remains intact.",
        "Article I Section 9.5 and Section 10.6; Article V Section 2.5",
    )


HANDLERS = {
    "cartelized_ballot_access_barriers_imposed": handle_cartelized_ballot_access_barriers_imposed,
    "court_voids_cartelized_ballot_access_barriers": handle_court_voids_cartelized_ballot_access_barriers,
    "dominant_parties_collude_to_exclude_debates_and_infrastructure": handle_dominant_parties_collude_to_exclude_debates_and_infrastructure,
    "electoral_commission_orders_relief_for_soft_party_cartelization": handle_electoral_commission_orders_relief_for_soft_party_cartelization,
    "court_upholds_relief_for_soft_party_cartelization": handle_court_upholds_relief_for_soft_party_cartelization,
}
