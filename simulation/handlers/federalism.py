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


HANDLERS = {
    "supreme_court_finds_state_democratic_floor_violation": handle_supreme_court_finds_state_democratic_floor_violation,
    "congress_fails_state_remedy": handle_congress_fails_state_remedy,
    "state_violation_persists_one_year": handle_state_violation_persists_one_year,
    "congress_suspends_representation": handle_congress_suspends_representation,
    "congress_enacts_commandeering_statute": handle_congress_enacts_commandeering_statute,
    "state_refuses_commandeering": handle_state_refuses_commandeering,
    "court_voids_commandeering_statute": handle_court_voids_commandeering_statute,
}
