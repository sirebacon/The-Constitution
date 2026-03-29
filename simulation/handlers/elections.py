from __future__ import annotations

from typing import Any

from sim_core import SimulationState


def handle_foreign_cyber_election_attack_detected(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    actor = event.get("actor", "Unknown actor")
    details = event.get("details", {})
    state.provisions.update(
        {
            "Article I election administration provisions",
            "Article V speech and press protections",
            "Article VI democratic integrity provisions",
            "Article X federalism provisions",
            "Article XVI war powers",
            "Article XVII foreign policy and national security",
        }
    )
    state.add_entry(
        day,
        "event",
        "A foreign adversary hacks voter systems, releases forged materials, and disrupts power near an election.",
    )
    state.add_obligation(
        "electoral_commission_protect_election",
        "Electoral Commission",
        "protect the election through constitutional disclosure, transparency, and emergency administration powers",
        "Article I and Article VI",
        day,
        day + 2,
        severity="high",
    )
    state.add_obligation(
        "court_review_speech_restriction",
        "Federal courts",
        "review any direct speech restriction imposed in response to the foreign attack",
        "Article V and Article XVII",
        day,
        day + 3,
        severity="high",
    )


def handle_president_attempts_direct_state_takeover(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    actor = event.get("actor", "Unknown actor")
    details = event.get("details", {})
    state.add_violation(
        "president_direct_state_takeover",
        "executive_defiance",
        "President",
        "President attempts direct federal control over state election administration outside the constitutional election framework.",
        "Article I and Article X",
        day,
    )


def handle_president_attempts_speech_restriction(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    actor = event.get("actor", "Unknown actor")
    details = event.get("details", {})
    state.add_violation(
        "president_speech_restriction_foreign_attack",
        "rights_suppression",
        "Executive branch",
        "Executive branch attempts to suppress suspected foreign propaganda directly rather than using disclosure and transparency tools.",
        "Article V and Article XVII",
        day,
    )


def handle_electoral_commission_acts(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    actor = event.get("actor", "Unknown actor")
    details = event.get("details", {})
    state.resolve_obligation(
        "electoral_commission_protect_election",
        day,
        "used constitutional disclosure and emergency administration powers to protect election administration without direct federal takeover",
    )


def handle_president_uses_article_xiv_tools(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    actor = event.get("actor", "Unknown actor")
    details = event.get("details", {})
    state.add_entry(
        day,
        "outcome",
        "The President uses Article XIV foreign-affairs tools short of war and without suppressing domestic political rights.",
        "Article XVII foreign policy and national security tools",
    )


def handle_courts_block_speech_restriction(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    actor = event.get("actor", "Unknown actor")
    details = event.get("details", {})
    state.resolve_obligation(
        "court_review_speech_restriction",
        day,
        "blocked the direct speech restriction and required the government to use disclosure-based measures instead",
    )


def handle_state_denies_overseas_citizen_assignment(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    actor = event.get("actor", "Unknown actor")
    details = event.get("details", {})
    state.provisions.update({"Article IX Section 3", "Article I election administration provisions"})
    state.add_violation(
        "overseas_citizen_assignment_denied",
        "membership_exclusion",
        "Election officials",
        "Election officials deny an overseas citizen any practical federal electoral home and reject registration on the theory that long residence abroad extinguished meaningful federal participation.",
        "Article IX Section 3 and Article I",
        day,
    )
    state.add_obligation(
        "court_restore_overseas_assignment",
        "Federal courts",
        "restore a lawful federal electoral home for the overseas citizen",
        "Article IX Section 3 and Article I",
        day,
        day + 7,
        severity="high",
    )


def handle_court_restores_overseas_assignment(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    actor = event.get("actor", "Unknown actor")
    details = event.get("details", {})
    state.resolve_obligation(
        "court_restore_overseas_assignment",
        day,
        "restored the overseas citizen's federal electoral assignment and registration rights",
    )


def handle_naturalized_candidate_excluded_by_statute(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    actor = event.get("actor", "Unknown actor")
    details = event.get("details", {})
    state.provisions.update({"Article IX Section 1", "Article III Section 2"})
    state.add_violation(
        "naturalized_candidate_exclusion",
        "caste_hierarchy",
        "Congress",
        "A federal statute bars naturalized citizens from holding a non-presidential federal office, creating a blanket civic disability based on the manner of citizenship.",
        "Article IX Section 1 and Article III Section 2",
        day,
    )
    state.add_obligation(
        "court_void_naturalized_exclusion",
        "Federal courts",
        "void the blanket exclusion of naturalized citizens from federal office",
        "Article IX Section 1 and Article III Section 2",
        day,
        day + 10,
        severity="high",
    )


def handle_court_voids_naturalized_candidate_exclusion(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    actor = event.get("actor", "Unknown actor")
    details = event.get("details", {})
    state.resolve_obligation(
        "court_void_naturalized_exclusion",
        day,
        "voided the blanket exclusion of naturalized citizens from non-presidential federal office",
    )


HANDLERS = {
    "foreign_cyber_election_attack_detected": handle_foreign_cyber_election_attack_detected,
    "president_attempts_direct_state_takeover": handle_president_attempts_direct_state_takeover,
    "president_attempts_speech_restriction": handle_president_attempts_speech_restriction,
    "electoral_commission_acts": handle_electoral_commission_acts,
    "president_uses_article_xiv_tools": handle_president_uses_article_xiv_tools,
    "courts_block_speech_restriction": handle_courts_block_speech_restriction,
    "state_denies_overseas_citizen_assignment": handle_state_denies_overseas_citizen_assignment,
    "court_restores_overseas_assignment": handle_court_restores_overseas_assignment,
    "naturalized_candidate_excluded_by_statute": handle_naturalized_candidate_excluded_by_statute,
    "court_voids_naturalized_candidate_exclusion": handle_court_voids_naturalized_candidate_exclusion,
}
