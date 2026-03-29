from __future__ import annotations

from typing import Any

from sim_core import SimulationState

# Handlers for Article XVIII social, economic, and affirmative rights scenarios.


def handle_government_dismantles_climate_protections_without_replacement(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    details = event.get("details", {})
    action = details.get("action", "administrative rollback of major climate regulations")
    state.provisions.update({"Article XVIII Section 1.2", "Article XVIII Section 1.4"})
    state.add_violation(
        "climate_backsliding_without_replacement",
        "constitutional_floor_breach",
        "Executive branch",
        f"Government carries out {action} without simultaneously replacing those protections with measures constitutionally sufficient in aggregate. Article XVIII Section 1.2 prohibits knowingly and materially dismantling existing climate protections without constitutionally sufficient replacement.",
        "Article XVIII Section 1.2 and Section 1.4",
        day,
    )
    state.add_obligation(
        "court_declare_climate_violation_order_plan",
        "Federal courts",
        "declare the climate-protection backsliding a constitutional violation and require the government to submit a constitutionally sufficient remedial plan within a defined period",
        "Article XVIII Section 1.2 and Section 1.4",
        day,
        day + 60,
        severity="high",
    )


def handle_court_declares_climate_violation_orders_plan(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    state.resolve_obligation(
        "court_declare_climate_violation_order_plan",
        day,
        "declared a constitutional violation and ordered the government to submit a constitutionally sufficient remedial climate plan within 180 days; retained jurisdiction to review the plan's adequacy",
    )
    state.add_entry(
        day,
        "outcome",
        "Courts may declare a climate-floor violation and require a remedial plan, but may not prescribe emissions targets, technology choices, tax measures, or line-item appropriations. The political branches choose among materially sufficient policy alternatives.",
        "Article XVIII Section 1.2 and Section 1.4",
    )
    state.add_obligation(
        "government_submit_climate_remedial_plan",
        "Congress and Executive branch",
        "adopt and submit a constitutionally sufficient remedial climate plan within the court's deadline",
        "Article XVIII Section 1.2 and Section 1.4",
        day,
        day + 180,
        severity="high",
    )


def handle_government_submits_sufficient_climate_plan(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    state.resolve_obligation(
        "government_submit_climate_remedial_plan",
        day,
        "adopted and submitted a remedial climate plan that the court found constitutionally sufficient in aggregate",
    )
    state.add_entry(
        day,
        "outcome",
        "The constitutional floor is restored. Article XVIII Section 1.2 enforcement produced a remedial plan through the political branches without judicial prescription of specific policy instruments.",
        "Article XVIII Section 1.2 and Section 1.4",
    )


def handle_state_leaves_students_inferior_education(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    details = event.get("details", {})
    group = details.get("group", "students in low-income districts")
    basis = details.get("basis", "geographic location and income")
    state.provisions.add("Article XVIII Section 2.2")
    state.add_violation(
        "education_floor_inequality",
        "constitutional_floor_breach",
        "State government",
        f"State's education funding and resource allocation leaves {group} with substantially inferior education on the basis of {basis}, in violation of Article XVIII Section 2.2.",
        "Article XVIII Section 2.2",
        day,
    )
    state.add_obligation(
        "court_require_education_remedy",
        "Federal courts",
        "require the state to adopt a lawful remedy within a defined period sufficient to restore the constitutional education floor for the affected students",
        "Article XVIII Section 2.2",
        day,
        day + 90,
        severity="high",
    )


def handle_court_requires_education_remedy(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    state.resolve_obligation(
        "court_require_education_remedy",
        day,
        "required the state to adopt a constitutionally sufficient remedy for the education floor violation within one year and retained jurisdiction to review adequacy",
    )
    state.add_entry(
        day,
        "outcome",
        "Article XVIII Section 2.2 imposes a judicially enforceable floor: public education must be of sufficient quality to enable meaningful participation in civic and economic life, and no group may receive substantially inferior education on a prohibited basis. Courts determine whether the floor is met; the state chooses how to meet it.",
        "Article XVIII Section 2.2",
    )


def handle_government_withdraws_shelter_protections(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    details = event.get("details", {})
    action = details.get("action", "elimination of emergency shelter programs without replacement")
    state.provisions.update({"Article XVIII Section 2.3", "Article XVIII Section 2.4"})
    state.add_violation(
        "housing_floor_backsliding",
        "constitutional_floor_breach",
        "Government",
        f"Government carries out {action}, leaving a class of persons without basic shelter protection through circumstances beyond their control, in violation of Article XVIII Section 2.3's requirement to maintain measures sufficient to prevent destitution.",
        "Article XVIII Section 2.3 and Section 2.4",
        day,
    )
    state.add_obligation(
        "court_preserve_shelter_floor",
        "Federal courts",
        "preserve existing shelter protections against backsliding and require the government to adopt a constitutionally sufficient replacement or maintain existing protections pending adoption of an adequate alternative",
        "Article XVIII Section 2.3 and Section 2.4",
        day,
        day + 30,
        severity="high",
    )


def handle_court_preserves_shelter_floor_against_backsliding(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    state.resolve_obligation(
        "court_preserve_shelter_floor",
        day,
        "preserved existing shelter protections against backsliding and required the government to adopt constitutionally sufficient replacement measures within 120 days; interim executive use of existing lawful authority ordered",
    )
    state.add_entry(
        day,
        "outcome",
        "Government may not deliberately dismantle an existing system of protection below the constitutional floor unless it simultaneously replaces it with materially equal or greater protection. Article XVIII Section 2.4 allows courts to preserve against backsliding and enforce compliance while the political branches adopt an adequate replacement.",
        "Article XVIII Section 2.3 and Section 2.4",
    )


def handle_child_welfare_proceeding_without_independent_representation(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    details = event.get("details", {})
    proceeding = details.get("proceeding", "termination of parental rights")
    state.provisions.update({"Article XVIII Section 4.5", "Article XVIII Section 4.6"})
    state.add_violation(
        "child_welfare_no_independent_representation",
        "constitutional_floor_breach",
        "State court",
        f"A state court conducts a {proceeding} proceeding affecting a child's fundamental interests without providing independent representation for the child and without stating reasons on the record for departing from the child's expressed preference, in violation of Article XVIII Section 4.5.",
        "Article XVIII Section 4.5 and Section 4.6",
        day,
    )
    state.add_obligation(
        "appellate_court_vacate_or_remand_child_proceeding",
        "Appellate court",
        "vacate or remand the proceeding for constitutionally sufficient process including independent representation and, where the court departs materially from the child's preference, specific stated reasons grounded in the child's welfare",
        "Article XVIII Section 4.5 and Section 4.6",
        day,
        day + 30,
        severity="high",
    )


def handle_court_vacates_child_welfare_proceeding_for_constitutional_defect(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    state.resolve_obligation(
        "appellate_court_vacate_or_remand_child_proceeding",
        day,
        "vacated the proceeding and remanded for constitutionally sufficient process with independent representation for the child and an on-record explanation if the court departs from the child's expressed preference",
    )
    state.add_entry(
        day,
        "outcome",
        "Article XVIII Section 4.5 requires independent representation for children in proceedings affecting custody, placement, or comparable fundamental interests, and requires stated reasons grounded in the child's welfare if the court departs materially from a mature child's preference. Administrative convenience and blanket assumptions do not satisfy the best-interests standard of Section 4.6.",
        "Article XVIII Section 4.5 and Section 4.6",
    )


HANDLERS = {
    "government_dismantles_climate_protections_without_replacement": handle_government_dismantles_climate_protections_without_replacement,
    "court_declares_climate_violation_orders_plan": handle_court_declares_climate_violation_orders_plan,
    "government_submits_sufficient_climate_plan": handle_government_submits_sufficient_climate_plan,
    "state_leaves_students_inferior_education": handle_state_leaves_students_inferior_education,
    "court_requires_education_remedy": handle_court_requires_education_remedy,
    "government_withdraws_shelter_protections": handle_government_withdraws_shelter_protections,
    "court_preserves_shelter_floor_against_backsliding": handle_court_preserves_shelter_floor_against_backsliding,
    "child_welfare_proceeding_without_independent_representation": handle_child_welfare_proceeding_without_independent_representation,
    "court_vacates_child_welfare_proceeding_for_constitutional_defect": handle_court_vacates_child_welfare_proceeding_for_constitutional_defect,
}
