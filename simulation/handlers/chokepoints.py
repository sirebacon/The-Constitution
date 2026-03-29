from __future__ import annotations

from typing import Any

from sim_core import SimulationState


def handle_executive_pressures_platforms_to_suppress_dissent(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    details = event.get("details", {})
    official = details.get("official", "Senior executive officials")
    targets = details.get("targets", "major digital platforms")
    speech = details.get("speech", "lawful political dissent")
    state.provisions.update({"Article V Section 2.1", "Article V Section 2.6", "Article XIII Section 2.0.5"})
    state.add_violation(
        "executive_coercive_platform_pressure",
        "executive_defiance",
        official,
        f"{official} pressure {targets} through threatened regulatory retaliation to suppress {speech} without issuing a formal order. The Constitution does not permit the executive to accomplish through coercive private pressure what Article V forbids it to do directly, and Article XIII Section 2.0.5 bars use of agency power for political retaliation.",
        "Article V Section 2.1 and Section 2.6; Article XIII Section 2.0.5",
        day,
    )
    state.add_obligation(
        "court_review_coercive_platform_pressure",
        "Federal courts",
        "determine on expedited review whether the state-coerced suppression is attributable to government action and enjoin any unconstitutional pressure",
        "Article V Section 2.1 and Section 2.6; Article XIII Section 2.0.5",
        day,
        day + 10,
        severity="high",
    )
    state.add_obligation(
        "acc_investigate_platform_weaponization",
        "Accountability Commission",
        "investigate whether executive officials used agency threats or regulatory leverage to induce viewpoint-based suppression",
        "Article XIII Section 2.0.5 and Article XII",
        day,
        day + 30,
        severity="high",
    )


def handle_court_enjoins_coercive_platform_pressure(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    state.resolve_obligation(
        "court_review_coercive_platform_pressure",
        day,
        "held that the pressure campaign constituted state action through coercive use of threatened agency power, enjoined further retaliation, and ordered restoration of access where the suppression resulted from that coercion",
    )
    state.add_entry(
        day,
        "outcome",
        "The scenario validates that the Constitution can reach indirect censorship when private suppression is driven by government coercion rather than ordinary platform discretion. Article V protects against state action in substance, not only formal edicts.",
        "Article V Section 2.1 and Section 2.6; Article XIII Section 2.0.5",
    )


def handle_acc_refers_platform_pressure_officials(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    state.resolve_obligation(
        "acc_investigate_platform_weaponization",
        day,
        "found that executive officials used threatened regulatory retaliation to induce viewpoint-based suppression and referred the responsible officials for prosecution or removal proceedings",
    )


def handle_private_infrastructure_firms_cut_off_opposition(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    details = event.get("details", {})
    firms = details.get("firms", "payment processors and hosting firms")
    organization = details.get("organization", "a lawful opposition organization")
    state.provisions.update({"Article V Section 2.6", "Article VII", "Article XIII"})
    state.add_violation(
        "private_chokepoint_election_cutoff",
        "structural_gap",
        "Private infrastructure chokepoints",
        f"{firms} jointly cut off service to {organization} during a federal election period. No formal government coercion is proved. The harm is politically severe, but the current Constitution has no clearly defined direct remedy for synchronized private exclusion by dominant civic infrastructure intermediaries absent state action, foreign control, or campaign-finance violation.",
        "Article V Section 2.6; Article VII; Article XIII",
        day,
    )
    state.add_obligation(
        "court_review_private_chokepoint_cutoff",
        "Federal courts",
        "determine whether existing constitutional provisions or implementing law provide a direct remedy for coordinated private exclusion of a lawful political organization during an election",
        "Article V Section 2.6; Article VII; Article XIII",
        day,
        day + 14,
        severity="high",
    )


def handle_court_finds_no_clear_constitutional_remedy_for_private_cutoff(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    state.resolve_obligation(
        "court_review_private_chokepoint_cutoff",
        day,
        "found no clear direct constitutional remedy because the exclusion was carried out by private firms without proven state coercion, foreign control, or a violation of an existing statutory duty",
    )
    state.add_entry(
        day,
        "outcome",
        "This scenario exposes a real under-tested gap. The draft is stronger against government censorship and foreign control than against purely private chokepoint exclusion of lawful political actors during an election.",
        "Article V Section 2.6; Article VII; Article XIII",
    )


HANDLERS = {
    "executive_pressures_platforms_to_suppress_dissent": handle_executive_pressures_platforms_to_suppress_dissent,
    "court_enjoins_coercive_platform_pressure": handle_court_enjoins_coercive_platform_pressure,
    "acc_refers_platform_pressure_officials": handle_acc_refers_platform_pressure_officials,
    "private_infrastructure_firms_cut_off_opposition": handle_private_infrastructure_firms_cut_off_opposition,
    "court_finds_no_clear_constitutional_remedy_for_private_cutoff": handle_court_finds_no_clear_constitutional_remedy_for_private_cutoff,
}
