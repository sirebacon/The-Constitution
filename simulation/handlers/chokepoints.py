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
    state.provisions.update({"Article VI Section 7.5A", "Article XII", "Article V Section 2.6"})
    state.add_violation(
        "private_chokepoint_election_cutoff",
        "institutional_stress",
        "Private infrastructure chokepoints",
        f"{firms} jointly cut off service to {organization} during a federal election period. Article VI Section 7.5A permits neutral continuity and nondiscrimination duties for dominant civic intermediaries where coordinated denial would materially impair lawful political competition.",
        "Article VI Section 7.5A; Article XII; Article V Section 2.6",
        day,
    )
    state.add_obligation(
        "electoral_commission_review_private_chokepoint_cutoff",
        "Electoral Commission",
        "determine whether the excluded organization is a lawful qualified political actor and order temporary nondiscriminatory restoration of essential service if Article VI Section 7.5A is triggered",
        "Article VI Section 7.5A; Article XII",
        day,
        day + 7,
        severity="high",
    )


def handle_electoral_commission_orders_temporary_restoration_for_private_cutoff(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    state.resolve_obligation(
        "electoral_commission_review_private_chokepoint_cutoff",
        day,
        "found that the coordinated cutoff threatened meaningful federal political competition, ordered temporary restoration of nondiscriminatory payment and hosting access under Article VI Section 7.5A, and directed expedited judicial review of the order",
    )
    state.add_obligation(
        "court_review_private_chokepoint_restoration_order",
        "Federal courts",
        "review the temporary restoration order on an expedited basis and sustain it if the targeted firms are dominant civic intermediaries whose coordinated denial materially impairs lawful federal political competition",
        "Article VI Section 7.5A; Article V Section 2.6",
        day,
        day + 7,
        severity="high",
    )


def handle_court_upholds_private_chokepoint_restoration_order(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    state.resolve_obligation(
        "court_review_private_chokepoint_restoration_order",
        day,
        "upheld the temporary restoration order as a narrowly tailored, viewpoint-neutral continuity measure against coordinated exclusion by dominant civic intermediaries during a federal election period",
    )
    state.add_entry(
        day,
        "outcome",
        "The scenario validates the new Article VI Section 7.5A backstop. The Constitution now permits a narrow, reviewable remedy against coordinated private chokepoint exclusion of lawful political actors during a federal election without creating a general power to control private speech or editorial judgment.",
        "Article VI Section 7.5A; Article XII; Article V Section 2.6",
    )


def handle_platform_denies_equal_candidate_tools(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    details = event.get("details", {})
    platform = details.get("platform", "A major digital platform")
    candidate = details.get("candidate", "a lawfully registered federal candidate")
    state.provisions.update({"Article VI Section 7.5", "Article XII"})
    state.add_violation(
        "platform_denies_equal_candidate_tools",
        "election_fairness_breach",
        platform,
        f"{platform} denies {candidate} equal access to political advertising and distribution tools available to competing candidates. Article VI Section 7.5(c) requires major digital platforms to provide equal access to such tools for all lawfully registered political candidates and parties.",
        "Article VI Section 7.5(c)",
        day,
    )
    state.add_obligation(
        "electoral_commission_review_candidate_tool_denial",
        "Electoral Commission",
        "review the unequal platform access, order immediate nondiscriminatory access if a violation is found, and require an independent audit of the platform's political-content distribution tools",
        "Article VI Section 7.5 and Article XII",
        day,
        day + 14,
        severity="high",
    )


def handle_electoral_commission_orders_equal_candidate_access(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    state.resolve_obligation(
        "electoral_commission_review_candidate_tool_denial",
        day,
        "found a violation of Article VI Section 7.5(c), ordered immediate equal access to the platform's political advertising and distribution tools, and opened an independent audit of the platform's political-content systems",
    )
    state.add_entry(
        day,
        "outcome",
        "The scenario validates that Article VI Section 7.5 already provides a meaningful constitutional foothold against discriminatory denial of candidate platform tools, at least where the platform is providing structured political advertising or distribution services rather than merely ranking organic content.",
        "Article VI Section 7.5(c)",
    )


def handle_platform_manipulates_emergency_information_visibility(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    details = event.get("details", {})
    platform = details.get("platform", "A dominant digital platform")
    information = details.get("information", "lawful emergency and election-administration information")
    state.provisions.update({"Article VI Section 7.5", "Article VI Section 7.5A", "Article I"})
    state.add_violation(
        "platform_emergency_visibility_manipulation",
        "institutional_stress",
        platform,
        f"{platform} materially downranks or obscures {information} during a live constitutional emergency or election-administration disruption. Article VI Section 7.5A permits temporary corrective relief where manipulative visibility practices by a dominant platform materially impair access to official emergency or election-administration information.",
        "Article VI Section 7.5 and Section 7.5A; Article I",
        day,
    )
    state.add_obligation(
        "electoral_commission_review_emergency_visibility_manipulation",
        "Electoral Commission",
        "review the manipulation claim, compel disclosure of relevant ranking criteria, and order temporary neutral restoration of access to official emergency or election-administration information if Article VI Section 7.5A is triggered",
        "Article VI Section 7.5 and Section 7.5A; Article XII",
        day,
        day + 10,
        severity="high",
    )


def handle_electoral_commission_orders_visibility_restoration(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    state.resolve_obligation(
        "electoral_commission_review_emergency_visibility_manipulation",
        day,
        "compelled disclosure of ranking criteria and audit information, found manipulative suppression of official emergency or election-administration information, and ordered temporary neutral restoration of visibility under Article VI Section 7.5A",
    )
    state.add_obligation(
        "court_review_visibility_restoration_order",
        "Federal courts",
        "review the temporary visibility-restoration order on an expedited basis and sustain it if it is narrowly limited to preserving access to official emergency or election-administration information",
        "Article VI Section 7.5A; Article I",
        day,
        day + 5,
        severity="high",
    )


def handle_court_upholds_visibility_restoration_order(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    state.resolve_obligation(
        "court_review_visibility_restoration_order",
        day,
        "upheld the temporary restoration order as a narrow election-and-emergency continuity measure rather than a general power to control private editorial rankings",
    )
    state.add_entry(
        day,
        "outcome",
        "The scenario validates that Article VI now supplies a narrow rapid corrective remedy for manipulative visibility practices affecting official emergency or election-administration information on dominant platforms.",
        "Article VI Section 7.5 and Section 7.5A; Article I",
    )


HANDLERS = {
    "executive_pressures_platforms_to_suppress_dissent": handle_executive_pressures_platforms_to_suppress_dissent,
    "court_enjoins_coercive_platform_pressure": handle_court_enjoins_coercive_platform_pressure,
    "acc_refers_platform_pressure_officials": handle_acc_refers_platform_pressure_officials,
    "private_infrastructure_firms_cut_off_opposition": handle_private_infrastructure_firms_cut_off_opposition,
    "electoral_commission_orders_temporary_restoration_for_private_cutoff": handle_electoral_commission_orders_temporary_restoration_for_private_cutoff,
    "court_upholds_private_chokepoint_restoration_order": handle_court_upholds_private_chokepoint_restoration_order,
    "platform_denies_equal_candidate_tools": handle_platform_denies_equal_candidate_tools,
    "electoral_commission_orders_equal_candidate_access": handle_electoral_commission_orders_equal_candidate_access,
    "platform_manipulates_emergency_information_visibility": handle_platform_manipulates_emergency_information_visibility,
    "electoral_commission_orders_visibility_restoration": handle_electoral_commission_orders_visibility_restoration,
    "court_upholds_visibility_restoration_order": handle_court_upholds_visibility_restoration_order,
}
