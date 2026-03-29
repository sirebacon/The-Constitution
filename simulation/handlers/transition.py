from __future__ import annotations

from typing import Any

from sim_core import SimulationState


def handle_constitution_ratified(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    actor = event.get("actor", "Unknown actor")
    details = event.get("details", {})
    state.provisions.update({"Article XIX Section 4", "Article XIX Section 5"})
    state.add_entry(
        day,
        "event",
        "The Constitution is ratified and the first-cycle implementation period begins.",
        "Article XIX Section 1 and Section 4",
    )
    state.add_obligation(
        "constitute_constitutional_organs",
        "Congress and appointing authorities",
        "constitute the Constitutional Organs on the timeline required by the Constitution",
        "Article XIX Section 5.2",
        day,
        day + 365,
        severity="high",
    )
    state.add_obligation(
        "first_election_law",
        "Congress",
        "provide by law for the first federal elections and orderly commencement of terms under the new constitutional order",
        "Article XIX Section 4.1 and Section 4.2",
        day,
        day + 365,
        severity="high",
    )


def handle_congress_fails_first_election_law(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    actor = event.get("actor", "Unknown actor")
    details = event.get("details", {})
    state.fail_obligation(
        "first_election_law",
        day,
        "Congress failed to provide by law for the first federal elections and orderly commencement of terms under the new constitutional order by day 365 under Article XIX Section 4.1 and Section 4.2.",
    )
    state.add_obligation(
        "electoral_commission_interim_first_election",
        "Electoral Commission",
        "administer the first federal election under interim constitutional rules",
        "Article XIX Section 4.5",
        day,
        day + 60,
        severity="high",
    )
    state.add_entry(
        day,
        "outcome",
        "The Electoral Commission must administer the first federal election under interim rules consistent with the Constitution, subject to expedited judicial review.",
        "Article XIX Section 4.5",
    )


def handle_congress_enacts_first_election_law(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    actor = event.get("actor", "Unknown actor")
    details = event.get("details", {})
    state.resolve_obligation(
        "first_election_law",
        day,
        "provided by law for the first federal elections and orderly commencement of terms under the new constitutional order",
    )


def handle_electoral_commission_administers_interim_first_election(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    actor = event.get("actor", "Unknown actor")
    details = event.get("details", {})
    state.resolve_obligation(
        "electoral_commission_interim_first_election",
        day,
        "administered the first federal election under interim constitutional rules",
    )


def handle_constitutional_organs_constituted(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    actor = event.get("actor", "Unknown actor")
    details = event.get("details", {})
    state.resolve_obligation(
        "constitute_constitutional_organs",
        day,
        "constituted the Electoral Commission and Accountability Commission on the constitutional timetable",
    )


def handle_constitutional_organs_deadline_missed(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    actor = event.get("actor", "Unknown actor")
    details = event.get("details", {})
    state.fail_obligation(
        "constitute_constitutional_organs",
        day,
        "Congress and appointing authorities failed to constitute the Constitutional Organs on the timeline required by the Constitution by day 365 under Article XIX Section 5.2.",
    )
    state.add_obligation(
        "supreme_court_order_constitutional_organs_completion",
        "Supreme Court",
        "order completion of the constitutional-organ appointment process",
        "Article XIX Section 5.2A",
        day,
        day + 30,
        severity="high",
    )
    state.add_entry(
        day,
        "outcome",
        "The missed deadline triggers a Supreme Court duty to order completion of the appointment process within 30 days.",
        "Article XIX Section 5.2A",
    )


def handle_supreme_court_orders_constitutional_organs_completion(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    actor = event.get("actor", "Unknown actor")
    details = event.get("details", {})
    state.resolve_obligation(
        "supreme_court_order_constitutional_organs_completion",
        day,
        "ordered completion of the constitutional-organ appointment process within 30 days",
    )
    state.add_obligation(
        "constitute_constitutional_organs_after_order",
        "Congress and appointing authorities",
        "complete the constitutional-organ appointment process after Supreme Court order",
        "Article XIX Section 5.2A",
        day,
        day + 30,
        severity="high",
    )


def handle_supreme_court_makes_temporary_constitutional_organ_appointments(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    actor = event.get("actor", "Unknown actor")
    details = event.get("details", {})
    state.fail_obligation(
        "constitute_constitutional_organs_after_order",
        day,
        "Congress and appointing authorities failed to complete the constitutional-organ appointment process after Supreme Court order by day 420 under Article XIX Section 5.2A.",
    )
    state.add_entry(
        day,
        "outcome",
        "The Supreme Court appointed the minimum temporary Commissioners necessary to create lawful quorums and begin startup, continuity, and protective functions in the affected Constitutional Organs.",
        "Article XIX Section 5.2A",
    )


HANDLERS = {
    "constitution_ratified": handle_constitution_ratified,
    "congress_fails_first_election_law": handle_congress_fails_first_election_law,
    "congress_enacts_first_election_law": handle_congress_enacts_first_election_law,
    "electoral_commission_administers_interim_first_election": handle_electoral_commission_administers_interim_first_election,
    "constitutional_organs_constituted": handle_constitutional_organs_constituted,
    "constitutional_organs_deadline_missed": handle_constitutional_organs_deadline_missed,
    "supreme_court_orders_constitutional_organs_completion": handle_supreme_court_orders_constitutional_organs_completion,
    "supreme_court_makes_temporary_constitutional_organ_appointments": handle_supreme_court_makes_temporary_constitutional_organ_appointments,
}
