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


def handle_sensitive_office_rule_overreaches(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    details = event.get("details", {})
    office = details.get("office", "a sensitive federal office")
    restriction = details.get("restriction", "a blanket exclusion of all dual citizens")
    state.provisions.update({"Article IX Section 4.2", "Article IX Section 4.5", "Article IX Section 5.3"})
    state.add_violation(
        "sensitive_office_overreach",
        "membership_exclusion",
        "Congress",
        f"Congress imposes {restriction} on eligibility for {office} without showing that the rule is narrowly tailored to an office involving exceptional national-security responsibility. Article IX permits targeted nationality, loyalty, or disclosure rules for especially sensitive offices, but not overbroad civic hierarchy by implication.",
        "Article IX Section 4.2, Section 4.5, and Section 5.3",
        day,
    )
    state.add_obligation(
        "court_narrow_sensitive_office_rule",
        "Federal courts",
        "invalidate or narrowly construe the overbroad sensitive-office restriction so that it does not create a general hierarchy of citizenship or nationality",
        "Article IX Section 4.2, Section 4.5, and Section 5.3",
        day,
        day + 14,
        severity="high",
    )


def handle_court_narrows_sensitive_office_rule(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    state.resolve_obligation(
        "court_narrow_sensitive_office_rule",
        day,
        "held that the restriction was overbroad, limited any valid nationality safeguards to genuinely exceptional national-security offices, and barred use of the rule as a general civic disability",
    )


def handle_agency_wrongly_rejects_citizenship_proof(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    details = event.get("details", {})
    context = details.get("context", "a federal election registration dispute")
    burden = details.get("burden", "an excessive documentary burden")
    state.provisions.update({"Article IX Section 2.2", "Article IX Section 6.1", "Article IX Section 6.2", "Article IX Section 6.3", "Article IX Section 6.4"})
    state.add_violation(
        "citizenship_proof_dispute",
        "membership_exclusion",
        "Election officials",
        f"Election officials deny recognition of citizenship in {context} based on {burden}, making citizenship practically impossible to prove for an otherwise eligible person and threatening time-sensitive political rights.",
        "Article IX Section 2.2 and Section 6.1 through Section 6.4",
        day,
    )
    state.add_obligation(
        "court_restore_citizenship_status",
        "Federal courts",
        "provide prompt review, reject the unlawful proof burden, and restore the citizen's political status before the time-sensitive right is lost",
        "Article IX Section 6.1 through Section 6.4",
        day,
        day + 5,
        severity="high",
    )


def handle_court_restores_citizenship_status(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    state.resolve_obligation(
        "court_restore_citizenship_status",
        day,
        "found the proof regime unlawfully burdensome, restored the citizen's political status, and ordered use of fair and reviewable procedures consistent with Article IX",
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
    "sensitive_office_rule_overreaches": handle_sensitive_office_rule_overreaches,
    "court_narrows_sensitive_office_rule": handle_court_narrows_sensitive_office_rule,
    "agency_wrongly_rejects_citizenship_proof": handle_agency_wrongly_rejects_citizenship_proof,
    "court_restores_citizenship_status": handle_court_restores_citizenship_status,
}
