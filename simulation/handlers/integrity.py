from __future__ import annotations

from typing import Any

from sim_core import SimulationState

# Handlers for oligarchic-resilience scenarios: foreign influence, beneficial
# ownership, critical infrastructure coercion, and records continuity.
# These scenarios validate the targeted hardening added after
# design-notes/resilience-against-oligarchic-pressure.md.


def handle_foreign_shell_entity_funds_political_messaging(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    details = event.get("details", {})
    entity = details.get("entity", "A domestic shell entity")
    sponsor = details.get("sponsor", "a foreign government")
    state.provisions.update({"Article VI Section 5.1", "Article VI Section 5.3", "Article VI Section 5.5"})
    state.add_violation(
        "foreign_shell_political_messaging",
        "foreign_interference",
        entity,
        f"{entity}, covertly funded and directed by {sponsor}, runs mass political messaging designed to destabilize public confidence in democratic institutions. Article VI Section 5.5 now pierces domestic conduits used to route foreign political funding, direction, or sponsorship and extends disclosure beyond formal campaign spending to mass political communications directed at the domestic public on matters of governance, elections, or constitutional legitimacy.",
        "Article VI Section 5.1(d), Section 5.3, and Section 5.5",
        day,
    )
    state.add_obligation(
        "acc_investigate_foreign_shell_messaging",
        "Accountability Commission",
        "investigate whether the shell entity is acting as a conduit for prohibited foreign political funding or direction, order disclosure of the ultimate beneficial sponsor, and determine whether the messaging violates Article VI Section 5.1(d), Section 5.3, or Section 5.5",
        "Article VI Section 5.1, Section 5.3, and Section 5.5",
        day,
        day + 30,
        severity="high",
    )


def handle_acc_orders_foreign_shell_disclosure(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    state.resolve_obligation(
        "acc_investigate_foreign_shell_messaging",
        day,
        "investigated the shell entity, found it to be acting as a conduit for foreign political sponsorship under Article VI Section 5.5, and ordered public disclosure of the ultimate foreign sponsor",
    )
    state.add_entry(
        day,
        "outcome",
        "The ACC reached the covert messaging operation directly through Article VI Section 5.5 rather than relying only on the foreign-agent registration theory of Section 5.3. The Constitution now treats domestic shell routing as no defense when the underlying funding, direction, or sponsorship would be unlawful if done openly by a foreign source.",
        "Article VI Section 5.1, Section 5.3, and Section 5.5",
    )
    state.add_obligation(
        "acc_penalize_foreign_shell_sponsor",
        "Accountability Commission",
        "impose civil and criminal penalties on the foreign sponsor and the shell entity operators under Article VI Section 5.1, Section 5.3, and Section 5.5",
        "Article VI Section 5.1, Section 5.3, and Section 5.5",
        day,
        day + 14,
        severity="high",
    )


def handle_foreign_shell_entity_penalized(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    state.resolve_obligation(
        "acc_penalize_foreign_shell_sponsor",
        day,
        "imposed civil penalties and referred the foreign sponsor's domestic operators for criminal prosecution under Article VI Section 5.1 and Section 5.3",
    )
    state.add_entry(
        day,
        "outcome",
        "Foreign-sponsored shell-entity political messaging is now directly reachable under Article VI Section 5.5. The scenario validates that the Constitution can treat covert routing through a domestic intermediary as foreign political interference without restricting ordinary domestic speech.",
        "Article VI Section 5.1, Section 5.3, and Section 5.5",
    )


def handle_entity_with_foreign_beneficial_owner_wins_federal_contract(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    details = event.get("details", {})
    entity = details.get("entity", "A federal contractor")
    sector = details.get("sector", "telecommunications infrastructure")
    state.provisions.update({"Article VIII Section 1.13", "Article XIII Section 9.3"})
    state.add_entry(
        day,
        "event",
        f"{entity} seeks and wins a major federal contract for {sector}. Post-award investigation reveals that the entity concealed foreign beneficial owners with ties to a hostile foreign government. Article VIII Section 1.13 now requires traceable beneficial-ownership disclosure for major federal contractors and strategic-sector control.",
        "Article VIII Section 1.13 and Article XIII Section 9.3",
    )
    state.add_obligation(
        "acc_investigate_contractor_beneficial_ownership",
        "Accountability Commission",
        "investigate whether the contractor concealed beneficial ownership in violation of Article VIII Section 1.13 and determine whether any official also engaged in regulatory corruption under Article XIII Section 9.3",
        "Article VIII Section 1.13 and Article XIII Section 9.3",
        day,
        day + 45,
        severity="high",
    )


def handle_acc_finds_no_corrupt_official_but_foreign_ownership(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    details = event.get("details", {})
    entity = details.get("entity", "Federal contractor")
    state.resolve_obligation(
        "acc_investigate_contractor_beneficial_ownership",
        day,
        "completed the investigation, confirmed concealed foreign-government beneficial ownership, found no corrupt official, and referred the contract for invalidation based on Article VIII Section 1.13's disclosure requirement",
    )
    state.add_violation(
        "contractor_concealed_foreign_beneficial_ownership",
        "foreign_capture_risk",
        entity,
        "A major federal contractor concealed foreign-government beneficial ownership while seeking sensitive federal work. Article VIII Section 1.13 now makes that concealment itself constitutionally disqualifying even where no individual federal official took a bribe or committed a separate corruption offense.",
        "Article VIII Section 1.13",
        day,
    )
    state.add_entry(
        day,
        "outcome",
        "The scenario validates the new contractor-transparency rule: foreign-state-linked control can now be reached directly through nondisclosure and contract ineligibility rather than only through official-corruption theories.",
        "Article VIII Section 1.13",
    )


def handle_foreign_entity_gains_critical_sector_control(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    details = event.get("details", {})
    entity = details.get("entity", "A foreign-state-linked company")
    sector = details.get("sector", "a major domestic telecommunications carrier")
    state.provisions.update({"Article XIII Section 12", "Article XVI"})
    state.add_entry(
        day,
        "event",
        f"{entity} acquires controlling ownership of {sector}. The acquisition raises national security and constitutional continuity concerns because failure or hostile manipulation of the carrier could impair elections, official communications, and emergency response. Article XIII Section 12 now gives Congress explicit authority to establish continuity and integrity standards for critical infrastructure whose failure or hostile control would materially impair constitutional government.",
        "Article XIII Section 12 and Article XVI",
    )
    state.add_obligation(
        "congress_respond_to_critical_sector_foreign_acquisition",
        "Congress",
        "invoke statutory national security review authority and, if the review finds a threat to constitutional governance, direct divestiture or remedial measures",
        "Article XIII Section 12 and Article XVI",
        day,
        day + 90,
        severity="high",
    )


def handle_congress_orders_critical_sector_divestiture(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    state.resolve_obligation(
        "congress_respond_to_critical_sector_foreign_acquisition",
        day,
        "enacted legislation directing divestiture of the foreign-controlled carrier based on documented threat to critical infrastructure supporting constitutional government operations",
    )
    state.add_entry(
        day,
        "outcome",
        "Congress acted on an explicit constitutional anchor. Article XIII Section 12 supports continuity and integrity standards for critical civilian infrastructure while separately barring open-ended military control and tying emergency measures back to Article III limits and Article IV review.",
        "Article XIII Section 12",
    )
    state.add_obligation(
        "entity_completes_divestiture",
        "Acquiring entity",
        "complete the court-supervised divestiture of the critical infrastructure carrier within the period set by Congress",
        "Article XIII Section 12 and implementing law",
        day,
        day + 180,
        severity="high",
    )


def handle_divestiture_completed(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    state.resolve_obligation(
        "entity_completes_divestiture",
        day,
        "completed the court-supervised divestiture of the critical infrastructure carrier",
    )


def handle_official_destroys_nonelectoral_records_during_transition(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    details = event.get("details", {})
    actor = details.get("actor", "Outgoing administration officials")
    records = details.get("records", "diplomatic communications and agency decision records")
    state.provisions.update({"Article VI Section 1.1", "Article XIX Section 6.5"})
    state.add_entry(
        day,
        "event",
        f"{actor} destroy or conceal {records} during the transition period. Article XIX Section 6.5 now expressly prohibits deliberate destruction, concealment, or unlawful transfer of federal records during transition and treats deliberate destruction of public records during transition as anti-subversion conduct under Article VI Section 1.1.",
        "Article XIX Section 6.5 and Article VI Section 1.1",
    )
    state.add_violation(
        "nonelectoral_records_destruction_transition",
        "anti_subversion",
        actor,
        f"{actor} destroyed or concealed non-electoral federal records during transition. Article XIX Section 6.5 makes deliberate destruction or concealment of public records during transition anti-subversion conduct and independently preserves all federal records beyond the election-records-specific protection in Article VI Section 1.2(c).",
        "Article XIX Section 6.5 and Article VI Section 1.1",
        day,
    )
    state.add_obligation(
        "acc_investigate_records_destruction",
        "Accountability Commission",
        "investigate the records destruction, determine responsibility under Article XIX Section 6.5 and Article VI Section 1.1, and prosecute responsible officials",
        "Article XIX Section 6.5 and Article VI Section 1.6",
        day,
        day + 30,
        severity="high",
    )


def handle_acc_prosecutes_records_destruction(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    state.resolve_obligation(
        "acc_investigate_records_destruction",
        day,
        "investigated, determined that the records destruction violated Article XIX Section 6.5 as anti-subversion conduct, and filed charges under Article VI Section 1.6",
    )
    state.add_entry(
        day,
        "outcome",
        "The scenario validates the new transition-records rule: non-electoral record destruction is now directly reachable as constitutional misconduct during transition rather than only by stretched obstruction theories.",
        "Article XIX Section 6.5 and Article VI Section 1.1",
    )


HANDLERS = {
    "foreign_shell_entity_funds_political_messaging": handle_foreign_shell_entity_funds_political_messaging,
    "acc_orders_foreign_shell_disclosure": handle_acc_orders_foreign_shell_disclosure,
    "foreign_shell_entity_penalized": handle_foreign_shell_entity_penalized,
    "entity_with_foreign_beneficial_owner_wins_federal_contract": handle_entity_with_foreign_beneficial_owner_wins_federal_contract,
    "acc_finds_no_corrupt_official_but_foreign_ownership": handle_acc_finds_no_corrupt_official_but_foreign_ownership,
    "foreign_entity_gains_critical_sector_control": handle_foreign_entity_gains_critical_sector_control,
    "congress_orders_critical_sector_divestiture": handle_congress_orders_critical_sector_divestiture,
    "divestiture_completed": handle_divestiture_completed,
    "official_destroys_nonelectoral_records_during_transition": handle_official_destroys_nonelectoral_records_during_transition,
    "acc_prosecutes_records_destruction": handle_acc_prosecutes_records_destruction,
}
