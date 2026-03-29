from __future__ import annotations

from typing import Any

from sim_core import SimulationState


def handle_warrantless_surveillance_conducted(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    actor = event.get("actor", "Unknown actor")
    details = event.get("details", {})
    state.provisions.update({"Article V Section 5.3", "Article XVII Section 4.7", "Article XV Section 6.5"})
    state.add_violation(
        "warrantless_domestic_surveillance",
        "rights_suppression",
        "Intelligence agency",
        "Intelligence agency conducts warrantless surveillance targeting a domestic political organization, in violation of Article V Section 5.3, Article XVII Section 4.7, and the prohibition on using classified appropriations for domestic political surveillance under Article XV Section 6.5.",
        "Article V Section 5.3, Article XVII Section 4.7, and Article XV Section 6.5",
        day,
    )
    state.add_obligation(
        "court_halt_surveillance",
        "Federal courts",
        "order an immediate halt to the warrantless domestic surveillance operation",
        "Article V Section 5.3 and Article XVII Section 4.7",
        day,
        day + 5,
        severity="high",
    )


def handle_court_orders_surveillance_halt(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    actor = event.get("actor", "Unknown actor")
    details = event.get("details", {})
    state.resolve_obligation(
        "court_halt_surveillance",
        day,
        "ordered an immediate halt to the warrantless domestic surveillance and referred the matter to the Accountability Commission",
    )
    state.add_obligation(
        "agency_comply_surveillance_halt",
        "Intelligence agency",
        "cease the warrantless domestic surveillance operation in compliance with the court order",
        "Article V Section 5.3 and Article XVII Section 4.7",
        day,
        day + 2,
        severity="high",
    )


def handle_agency_complies_with_surveillance_halt(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    actor = event.get("actor", "Unknown actor")
    details = event.get("details", {})
    state.resolve_obligation(
        "agency_comply_surveillance_halt",
        day,
        "ceased the warrantless domestic surveillance operation in compliance with the court order",
    )


def handle_emergency_used_to_restrict_protected_speech(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    actor = event.get("actor", "Unknown actor")
    details = event.get("details", {})
    state.provisions.update({"Article III Section 5.3", "Article V"})
    message = "Executive branch uses an emergency declaration to restrict protected expression, in violation of the absolute bar on overriding Article V rights through emergency powers."
    state.add_violation(
        "emergency_rights_suppression",
        "rights_suppression",
        "Executive branch",
        message,
        "Article III Section 5.3(f) and Article V",
        day,
    )
    state.add_obligation(
        "court_void_emergency_rights_restriction",
        "Federal courts",
        "void the emergency-based restriction on protected expression",
        "Article III Section 5.3(f) and Article V",
        day,
        day + 2,
        severity="high",
    )


def handle_court_voids_emergency_rights_restriction(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    actor = event.get("actor", "Unknown actor")
    details = event.get("details", {})
    state.resolve_obligation(
        "court_void_emergency_rights_restriction",
        day,
        "voided the emergency-based restriction on protected expression",
    )


def handle_president_suspends_habeas_corpus_by_executive_order(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    actor = event.get("actor", "Unknown actor")
    details = event.get("details", {})
    state.provisions.update({"Article III Section 5.7", "Article V Section 1"})
    state.add_violation(
        "executive_habeas_suspension",
        "rights_suppression",
        "President",
        "President suspends the privilege of the writ of habeas corpus by executive order. This power belongs exclusively to Congress under Article III Section 5.7 and may not be exercised by the President alone.",
        "Article III Section 5.7",
        day,
    )
    state.add_obligation(
        "court_void_habeas_suspension",
        "Federal courts",
        "void the executive habeas suspension immediately",
        "Article III Section 5.7 and Article V Section 1",
        day,
        day + 2,
        severity="high",
    )


def handle_court_voids_habeas_suspension(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    actor = event.get("actor", "Unknown actor")
    details = event.get("details", {})
    state.resolve_obligation(
        "court_void_habeas_suspension",
        day,
        "voided the executive habeas suspension and restored access to the writ",
    )


def handle_budget_deadline_missed(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    actor = event.get("actor", "Unknown actor")
    details = event.get("details", {})
    state.provisions.update({"Article XV Section 3.2", "Article XV Section 3.3", "Article XV Section 3.4"})
    state.add_entry(
        day,
        "event",
        "Congress has not enacted appropriations legislation by October 1. The automatic continuing resolution takes effect at 98% of prior-year enacted levels.",
        "Article XV Section 3.2",
    )
    state.add_entry(
        day,
        "outcome",
        "The government may not shut down for lack of appropriations. The automatic continuing resolution is self-executing and requires no further legislative or executive action to take effect.",
        "Article XV Section 3.2 and Section 3.3",
    )


def handle_executive_attempts_selective_cr_funding(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    actor = event.get("actor", "Unknown actor")
    details = event.get("details", {})
    state.add_violation(
        "executive_selective_cr_funding",
        "executive_defiance",
        "Executive branch",
        "Executive branch attempts to alter funding ratios, withhold appropriated funds, or selectively apply funding levels under the automatic continuing resolution.",
        "Article XV Section 3.4",
        day,
    )
    state.add_obligation(
        "court_review_cr_manipulation",
        "Federal courts",
        "review the executive branch's selective CR funding manipulation on an expedited basis",
        "Article XV Section 3.4",
        day,
        day + 5,
        severity="high",
    )


def handle_court_blocks_cr_manipulation(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    actor = event.get("actor", "Unknown actor")
    details = event.get("details", {})
    state.resolve_obligation(
        "court_review_cr_manipulation",
        day,
        "issued an expedited order blocking the executive branch's selective application of the automatic continuing resolution",
    )


HANDLERS = {
    "warrantless_surveillance_conducted": handle_warrantless_surveillance_conducted,
    "court_orders_surveillance_halt": handle_court_orders_surveillance_halt,
    "agency_complies_with_surveillance_halt": handle_agency_complies_with_surveillance_halt,
    "emergency_used_to_restrict_protected_speech": handle_emergency_used_to_restrict_protected_speech,
    "court_voids_emergency_rights_restriction": handle_court_voids_emergency_rights_restriction,
    "president_suspends_habeas_corpus_by_executive_order": handle_president_suspends_habeas_corpus_by_executive_order,
    "court_voids_habeas_suspension": handle_court_voids_habeas_suspension,
    "budget_deadline_missed": handle_budget_deadline_missed,
    "executive_attempts_selective_cr_funding": handle_executive_attempts_selective_cr_funding,
    "court_blocks_cr_manipulation": handle_court_blocks_cr_manipulation,
}
