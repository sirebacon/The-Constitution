from __future__ import annotations

from typing import Any

from sim_core import SimulationState


def handle_congress_enacts_temporary_emergency_revenue_measure(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    details = event.get("details", {})
    measure = details.get("measure", "a temporary emergency revenue surcharge")
    purpose = details.get("purpose", "a publicly stated emergency purpose")
    duration_days = int(details.get("duration_days", 30))
    state.provisions.update({"Article XIV Section 2.1", "Article XIV Section 2.2", "Article XIV Section 4.5"})
    state.add_entry(
        day,
        "event",
        f"Congress enacts {measure} for {purpose}, with a publicly stated statutory duration of {duration_days} days.",
        "Article XIV Section 2.1, Section 2.2, and Section 4.5",
    )
    state.add_entry(
        day,
        "outcome",
        "The Constitution permits temporary emergency revenue measures only by law, for publicly stated purposes, and for limited duration.",
        "Article XIV Section 4.5",
    )


def handle_president_orders_emergency_revenue_measure_continued(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    details = event.get("details", {})
    measure = details.get("measure", "the expired emergency revenue measure")
    state.provisions.update({"Article XIV Section 2.2", "Article XIV Section 3.2", "Article XIV Section 4.5", "Article XIV Section 5.2"})
    state.add_violation(
        "executive_continues_emergency_revenue_measure",
        "executive_defiance",
        "President",
        f"President orders continued collection of {measure} after its lawful expiration, without new legislation. Article XIV forbids executive creation or material alteration of revenue measures and bars indefinite continuation of emergency revenue measures by executive action alone.",
        "Article XIV Section 2.2, Section 3.2, Section 4.5, and Section 5.2",
        day,
    )
    state.add_obligation(
        "court_void_unilateral_emergency_revenue_extension",
        "Federal courts",
        "void the unilateral continuation of the expired emergency revenue measure",
        "Article XIV Section 2.2, Section 4.5, and Section 5.2",
        day,
        day + 7,
        severity="high",
    )


def handle_court_voids_unilateral_emergency_revenue_extension(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    state.resolve_obligation(
        "court_void_unilateral_emergency_revenue_extension",
        day,
        "voided the unilateral continuation of the expired emergency revenue measure and ordered ordinary collection to revert to the last valid statutory baseline",
    )
    state.add_entry(
        day,
        "outcome",
        "Article XIV's emergency-revenue rule has real bite: temporary revenue measures may expire, and the President cannot keep collecting them by proclamation once statutory authority ends.",
        "Article XIV Section 2.2, Section 4.5, and Section 5.2",
    )


def handle_treasury_grants_selective_customs_waiver_without_law(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    details = event.get("details", {})
    beneficiary = details.get("beneficiary", "a politically favored importer")
    state.provisions.update({"Article XIV Section 2.1", "Article XIV Section 3.2", "Article XIV Section 4.4", "Article XIV Section 5.1"})
    state.add_violation(
        "selective_customs_waiver_without_law",
        "executive_defiance",
        "Treasury Department",
        f"Treasury grants {beneficiary} a selective customs-duty waiver without lawful authorization. Article XIV forbids officers from collecting, waiving, redirecting, or selectively withholding taxes except as authorized by law, and bars revenue administration that creates arbitrary favoritism.",
        "Article XIV Section 3.2, Section 4.4, and Section 5.1",
        day,
    )
    state.add_obligation(
        "court_void_selective_customs_waiver",
        "Federal courts",
        "void the unlawful selective customs-duty waiver and require lawful, nondiscriminatory collection",
        "Article XIV Section 3.2, Section 4.4, and Section 5.1",
        day,
        day + 21,
        severity="high",
    )


def handle_court_voids_selective_customs_waiver(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    state.resolve_obligation(
        "court_void_selective_customs_waiver",
        day,
        "voided the selective customs-duty waiver and required Treasury to administer the duty law on equal terms",
    )
    state.add_entry(
        day,
        "outcome",
        "The scenario validates that Article XIV reaches selective revenue favoritism directly. Officers may not waive or selectively withhold taxes for preferred parties without statutory authority.",
        "Article XIV Section 3.2, Section 4.4, and Section 5.1",
    )


HANDLERS = {
    "congress_enacts_temporary_emergency_revenue_measure": handle_congress_enacts_temporary_emergency_revenue_measure,
    "president_orders_emergency_revenue_measure_continued": handle_president_orders_emergency_revenue_measure_continued,
    "court_voids_unilateral_emergency_revenue_extension": handle_court_voids_unilateral_emergency_revenue_extension,
    "treasury_grants_selective_customs_waiver_without_law": handle_treasury_grants_selective_customs_waiver_without_law,
    "court_voids_selective_customs_waiver": handle_court_voids_selective_customs_waiver,
}
