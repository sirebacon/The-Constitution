from __future__ import annotations

from typing import Any

from sim_core import SimulationState


def handle_regional_assembly_begins_trial_on_transmitted_articles(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    actor = event.get("actor", "Unknown actor")
    details = event.get("details", {})
    trial_type = details.get("trial_type", "obstruction")
    if trial_type == "war":
        key = "regional_assembly_trial_war"
        resolution = "began trial on automatically transmitted war-powers articles"
    else:
        key = "regional_assembly_trial_obstruction"
        resolution = "began trial on automatically transmitted obstruction articles"
    state.resolve_obligation(key, day, resolution)


def handle_unauthorized_military_action_started(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    actor = event.get("actor", "Unknown actor")
    details = event.get("details", {})
    state.provisions.update({"Article XVI Section 1", "Article III Section 10"})
    state.add_entry(day, "event", "President initiates military action without prior authorization.", "Article XVI Section 1")
    state.add_obligation(
        "congress_authorize_force",
        "Congress",
        "grant authorization for continued military force or refuse it",
        "Article XVI Section 1",
        day,
        day + 30,
        severity="high",
    )


def handle_congress_fails_aumf(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    actor = event.get("actor", "Unknown actor")
    details = event.get("details", {})
    state.add_entry(day, "event", "Congress does not provide timely authorization for the military action.", "Article XVI Section 1")
    state.fail_obligation(
        "congress_authorize_force",
        day,
        "Congress failed to grant authorization for continued military force or refuse it by day 30 under Article XVI Section 1.",
    )
    state.add_obligation(
        "chief_justice_withdrawal_order",
        "Chief Justice",
        "issue the required withdrawal order for unauthorized continued operations",
        "Article XVI Section 1.5(c)",
        day,
        day + 5,
        severity="high",
    )


def handle_chief_justice_issues_withdrawal_order(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    actor = event.get("actor", "Unknown actor")
    details = event.get("details", {})
    state.resolve_obligation("chief_justice_withdrawal_order", day, "issued a withdrawal order")


def handle_president_ignores_withdrawal_order(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    actor = event.get("actor", "Unknown actor")
    details = event.get("details", {})
    message = "President continues military operations in violation of a withdrawal order."
    state.add_violation(
        "president_ignores_withdrawal_order",
        "executive_defiance",
        "President",
        message,
        "Article XVI Section 8(e)",
        day,
    )
    state.add_obligation(
        "house_vote_impeachment_war",
        "House of Representatives",
        "hold a recorded impeachment vote on the unlawful continued military operation",
        "Article XVI Section 1.5(e) and Article III Section 10.2A",
        day,
        day + 21,
        severity="high",
    )
    state.add_obligation(
        "acc_issue_fiscal_hold",
        "Accountability Commission",
        "issue a self-executing fiscal hold on appropriated funds for the unlawful operation",
        "Article XVI Section 1.5(d)",
        day,
        day + 1,
        severity="high",
    )


def handle_acc_issues_fiscal_hold(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    state.resolve_obligation(
        "acc_issue_fiscal_hold",
        day,
        "issued a self-executing fiscal hold on appropriated funds for the unlawful operation",
    )
    state.add_obligation(
        "treasury_implement_fiscal_hold",
        "Secretary of the Treasury",
        "implement the ACC fiscal hold within 24 hours",
        "Article XVI Section 1.5(d)",
        day,
        day + 1,
        severity="high",
    )


def handle_treasury_implements_fiscal_hold(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    state.resolve_obligation(
        "treasury_implement_fiscal_hold",
        day,
        "implemented the ACC fiscal hold, cutting off appropriated funds for the unlawful operation",
    )


def handle_treasury_refuses_fiscal_hold(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    state.add_violation(
        "treasury_refuses_fiscal_hold",
        "executive_defiance",
        "Secretary of the Treasury",
        "Secretary of the Treasury refuses to implement a lawful ACC fiscal hold within the required 24-hour period, in violation of Article XVI Section 1.5(d).",
        "Article XVI Section 1.5(d)",
        day,
    )
    state.add_entry(
        day,
        "outcome",
        "The Secretary of the Treasury is subject to immediate removal from office and referral for prosecution by the Accountability Commission.",
        "Article XVI Section 1.5(d)",
    )
    state.add_obligation(
        "acc_remove_and_refer_treasury_officer",
        "Accountability Commission",
        "remove the non-compliant Treasury officer from office and refer for prosecution",
        "Article XVI Section 1.5(d)",
        day,
        day + 3,
        severity="high",
    )


def handle_house_members_coordinate_absence_to_block_required_vote(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    actor = event.get("actor", "Unknown actor")
    details = event.get("details", {})
    state.provisions.add("Article II Section 15A")
    state.add_entry(
        day,
        "event",
        "A bloc of House members coordinates absence and refuses available continuity procedures in order to defeat a constitutionally required impeachment vote.",
        "Article II Section 15A.4",
    )
    state.add_violation(
        "coordinated_absenteeism_required_vote",
        "institutional_stress",
        "Bloc of House members",
        "House members coordinate absence and refuse available continuity procedures in order to defeat a constitutionally required vote, constituting obstruction of a constitutional process.",
        "Article II Section 15A.4",
        day,
    )
    state.add_entry(
        day,
        "outcome",
        "Nominal reliance on travel, hardship, or ordinary chamber custom does not excuse coordinated absentee obstruction under Article II Section 15A.4.",
        "Article II Section 15A.4",
    )


def handle_president_declares_domestic_insurrection(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    actor = event.get("actor", "Unknown actor")
    details = event.get("details", {})
    state.provisions.update({"Article XVI Section 7", "Article XVI Section 8", "Article V Section 1"})
    state.add_entry(day, "event", f"{actor} declares an insurrection and orders domestic military deployment.", "Article XVI Section 7")
    state.add_obligation(
        "court_review_domestic_deployment",
        "Federal courts",
        "review the constitutional basis for the domestic deployment",
        "Article XVI Section 7 and Section 8",
        day,
        day + 3,
        severity="high",
    )
    state.add_obligation(
        "service_members_assess_order",
        "Service members",
        "refuse compliance with an unconstitutional domestic deployment order",
        "Article XVI Section 8",
        day,
        None,
        severity="high",
    )


def handle_courts_reject_domestic_deployment(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    actor = event.get("actor", "Unknown actor")
    details = event.get("details", {})
    message = "Executive branch treats protest unrest as armed rebellion and orders domestic military deployment without the required constitutional basis."
    state.add_violation(
        "domestic_deployment_unlawful",
        "rights_suppression",
        "Executive branch",
        message,
        "Article XVI Section 7 and Article V Section 1",
        day,
    )
    state.resolve_obligation(
        "court_review_domestic_deployment",
        day,
        "held that the domestic deployment lacked a constitutional basis and must cease",
    )


def handle_service_members_refuse_unlawful_order(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    actor = event.get("actor", "Unknown actor")
    details = event.get("details", {})
    state.resolve_obligation(
        "service_members_assess_order",
        day,
        "refused the unconstitutional domestic deployment order",
    )


def handle_president_orders_nuclear_first_use(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    actor = event.get("actor", "Unknown actor")
    details = event.get("details", {})
    state.provisions.update({"Article XVI Section 3.1", "Article XVI Section 3.2", "Article XVI Section 3.3"})
    state.add_entry(
        day,
        "event",
        "President orders nuclear first use without the constitutionally required authorization.",
        "Article XVI Section 3.1",
    )
    state.add_obligation(
        "secdef_refuse_nuclear_order",
        "Secretary of Defense",
        "refuse to confirm an unconstitutional nuclear first-use order",
        "Article XVI Section 3.2",
        day,
        None,
        severity="high",
    )
    state.add_obligation(
        "secstate_refuse_nuclear_order",
        "Secretary of State",
        "refuse to countersign or support an unconstitutional nuclear first-use order",
        "Article XVI Section 3.3",
        day,
        None,
        severity="high",
    )


def handle_secretary_of_defense_refuses_nuclear_order(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    actor = event.get("actor", "Unknown actor")
    details = event.get("details", {})
    state.resolve_obligation(
        "secdef_refuse_nuclear_order",
        day,
        "refused to confirm the unconstitutional nuclear first-use order",
    )


def handle_secretary_of_state_refuses_nuclear_order(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    actor = event.get("actor", "Unknown actor")
    details = event.get("details", {})
    state.resolve_obligation(
        "secstate_refuse_nuclear_order",
        day,
        "refused to support the unconstitutional nuclear first-use order",
    )


def handle_president_fires_secretary_to_compel_nuclear_compliance(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    actor = event.get("actor", "Unknown actor")
    details = event.get("details", {})
    state.add_violation(
        "president_fires_to_circumvent_nuclear_guardrail",
        "executive_defiance",
        "President",
        "President removes the Secretary of Defense to install a replacement willing to confirm a nuclear first-use order, using the removal power to circumvent a constitutional authorization safeguard.",
        "Article XVI Section 3.1 and Section 3.2",
        day,
    )
    state.add_obligation(
        "acting_secdef_refuse_nuclear_order",
        "Acting Secretary of Defense",
        "refuse to validate the unconstitutional nuclear first-use order notwithstanding the replacement pressure",
        "Article XVI Section 3.2",
        day,
        None,
        severity="high",
    )


def handle_acting_secretary_also_refuses_nuclear_order(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    actor = event.get("actor", "Unknown actor")
    details = event.get("details", {})
    state.resolve_obligation(
        "acting_secdef_refuse_nuclear_order",
        day,
        "also refused to validate the unconstitutional nuclear first-use order",
    )
    state.add_entry(
        day,
        "outcome",
        "The constitutional authorization safeguard holds. Nuclear first use is blocked absent the required approval.",
        "Article XVI Section 3.1 through Section 3.3",
    )


def handle_covert_operation_ordered_against_us_citizen(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    actor = event.get("actor", "Unknown actor")
    details = event.get("details", {})
    state.provisions.update({"Article XVI Section 5.2", "Article V Section 5"})
    state.add_entry(
        day,
        "event",
        "CIA orders a covert lethal operation against a US citizen and seeks the required warrant.",
        "Article XVI Section 5.2",
    )
    state.add_obligation(
        "court_review_citizen_targeting_warrant",
        "Federal courts",
        "review the warrant request for the lethal operation against the citizen",
        "Article XVI Section 5.2",
        day,
        day + 3,
        severity="high",
    )


def handle_court_denies_warrant_capture_feasible(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    actor = event.get("actor", "Unknown actor")
    details = event.get("details", {})
    state.resolve_obligation(
        "court_review_citizen_targeting_warrant",
        day,
        "denied the warrant because capture was feasible and the constitutional standard for lethal action was not met",
    )


def handle_operation_proceeds_despite_warrant_denial(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    actor = event.get("actor", "Unknown actor")
    details = event.get("details", {})
    state.add_violation(
        "citizen_targeting_after_warrant_denial",
        "executive_defiance",
        "CIA",
        "CIA proceeds with a covert lethal operation against a US citizen after a court denied the required warrant, in direct violation of Article XVI Section 5.2.",
        "Article XVI Section 5.2",
        day,
    )
    state.add_obligation(
        "acc_prosecute_unlawful_covert_op",
        "Accountability Commission",
        "open a prosecution for the unlawful covert operation against the citizen",
        "Article XVI Section 5.2 and Article XII Section 3",
        day,
        day + 14,
        severity="high",
    )


def handle_acc_opens_prosecution_for_unlawful_operation(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    actor = event.get("actor", "Unknown actor")
    details = event.get("details", {})
    state.resolve_obligation(
        "acc_prosecute_unlawful_covert_op",
        day,
        "opened a prosecution for the unlawful covert operation against the citizen",
    )


def handle_congress_denies_force_authorization(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    actor = event.get("actor", "Unknown actor")
    details = event.get("details", {})
    state.provisions.update({"Article XVI Section 4.4", "Article III Section 10.2A"})
    state.add_entry(
        day,
        "event",
        "Congress denies authorization for a military operation.",
        "Article XVI Section 4.4",
    )


def handle_president_deploys_pmcs_as_aumf_substitute(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    actor = event.get("actor", "Unknown actor")
    details = event.get("details", {})
    state.add_violation(
        "pmc_substitution_after_aumf_denial",
        "executive_defiance",
        "President",
        "President deploys private military contractors in a combat role to conduct the operation Congress denied, in direct violation of Article XVI Section 4.4, which prohibits using PMCs to avoid authorization requirements or to conceal the scale of US military engagement.",
        "Article XVI Section 4.4",
        day,
    )
    state.add_obligation(
        "house_vote_impeachment_pmc",
        "House of Representatives",
        "hold the required impeachment vote on the PMC substitution violation",
        "Article III Section 10.2A and Article XVI Section 4.4",
        day,
        day + 21,
        severity="high",
    )


def handle_house_misses_pmc_impeachment_vote(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    actor = event.get("actor", "Unknown actor")
    details = event.get("details", {})
    state.fail_obligation(
        "house_vote_impeachment_pmc",
        day,
        "House of Representatives failed to hold the required impeachment vote on the PMC substitution violation by the required deadline under Article III Section 10.2A.",
    )


def handle_regional_assembly_begins_pmc_trial(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    actor = event.get("actor", "Unknown actor")
    details = event.get("details", {})
    state.resolve_obligation(
        "regional_assembly_trial_pmc",
        day,
        "began impeachment trial on the automatically transmitted PMC substitution articles",
    )

HANDLERS = {
    "regional_assembly_begins_trial_on_transmitted_articles": handle_regional_assembly_begins_trial_on_transmitted_articles,
    "unauthorized_military_action_started": handle_unauthorized_military_action_started,
    "congress_fails_aumf": handle_congress_fails_aumf,
    "chief_justice_issues_withdrawal_order": handle_chief_justice_issues_withdrawal_order,
    "president_ignores_withdrawal_order": handle_president_ignores_withdrawal_order,
    "acc_issues_fiscal_hold": handle_acc_issues_fiscal_hold,
    "treasury_implements_fiscal_hold": handle_treasury_implements_fiscal_hold,
    "treasury_refuses_fiscal_hold": handle_treasury_refuses_fiscal_hold,
    "house_members_coordinate_absence_to_block_required_vote": handle_house_members_coordinate_absence_to_block_required_vote,
    "president_declares_domestic_insurrection": handle_president_declares_domestic_insurrection,
    "courts_reject_domestic_deployment": handle_courts_reject_domestic_deployment,
    "service_members_refuse_unlawful_order": handle_service_members_refuse_unlawful_order,
    "president_orders_nuclear_first_use": handle_president_orders_nuclear_first_use,
    "secretary_of_defense_refuses_nuclear_order": handle_secretary_of_defense_refuses_nuclear_order,
    "secretary_of_state_refuses_nuclear_order": handle_secretary_of_state_refuses_nuclear_order,
    "president_fires_secretary_to_compel_nuclear_compliance": handle_president_fires_secretary_to_compel_nuclear_compliance,
    "acting_secretary_also_refuses_nuclear_order": handle_acting_secretary_also_refuses_nuclear_order,
    "covert_operation_ordered_against_us_citizen": handle_covert_operation_ordered_against_us_citizen,
    "court_denies_warrant_capture_feasible": handle_court_denies_warrant_capture_feasible,
    "operation_proceeds_despite_warrant_denial": handle_operation_proceeds_despite_warrant_denial,
    "acc_opens_prosecution_for_unlawful_operation": handle_acc_opens_prosecution_for_unlawful_operation,
    "congress_denies_force_authorization": handle_congress_denies_force_authorization,
    "president_deploys_pmcs_as_aumf_substitute": handle_president_deploys_pmcs_as_aumf_substitute,
    "house_misses_pmc_impeachment_vote": handle_house_misses_pmc_impeachment_vote,
    "regional_assembly_begins_pmc_trial": handle_regional_assembly_begins_pmc_trial,
}
