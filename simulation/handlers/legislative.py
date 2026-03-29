from __future__ import annotations

from typing import Any

from sim_core import SimulationState


def handle_regional_assembly_leadership_blocks_scheduling(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    actor = event.get("actor", "Unknown actor")
    details = event.get("details", {})
    state.provisions.update({"Article II Section 15A", "Article III Section 5.4"})
    state.add_entry(
        day,
        "event",
        "Regional Assembly leadership refuses to place the emergency declaration on the floor calendar within the required period.",
        "Article II Section 15A.1 and Article III Section 5.4",
    )
    state.add_violation(
        "ra_leadership_blocks_scheduling",
        "legislative_deadline_failure",
        "Regional Assembly leadership",
        "Regional Assembly leadership refuses to place the emergency declaration on the floor calendar within the required period.",
        "Article II Section 15A.1 and Article III Section 5.4",
        day,
    )
    state.add_entry(
        day,
        "outcome",
        "Any member of the Regional Assembly may now file a mandatory scheduling motion under Article II Section 15A.1(b).",
        "Article II Section 15A.1(b)",
    )


def handle_regional_assembly_enters_recess_to_avoid_vote(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    actor = event.get("actor", "Unknown actor")
    details = event.get("details", {})
    state.provisions.update({"Article II Section 15A", "Article III Section 5.4"})
    state.add_entry(
        day,
        "event",
        "Regional Assembly leadership attempts to run out the emergency-approval deadline by entering recess instead of holding the constitutionally required vote.",
        "Article II Section 15A.1(e)-(f) and Article III Section 5.4",
    )
    state.add_violation(
        "ra_recess_evasion",
        "legislative_deadline_failure",
        "Regional Assembly leadership",
        "Regional Assembly leadership attempts to run out the emergency-approval deadline by entering recess instead of holding the constitutionally required vote.",
        "Article II Section 15A.1(e)-(f) and Article III Section 5.4",
        day,
    )
    state.add_entry(
        day,
        "outcome",
        "Any member of the Regional Assembly may file a mandatory scheduling motion, and any affected party may seek mandamus in the U.S. District Court for the District of Columbia if recess is used to block the vote.",
        "Article II Section 15A.1(d)-(f)",
    )


def handle_section_15a_scheduling_motion_filed(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    actor = event.get("actor", "Unknown actor")
    details = event.get("details", {})
    state.add_entry(
        day,
        "event",
        f"{actor} files a mandatory scheduling motion under Article II Section 15A.1(b).",
        "Article II Section 15A.1(b)",
    )
    state.add_obligation(
        "presiding_officer_15a_motion",
        "Regional Assembly presiding officer",
        "bring the Section 15A mandatory scheduling motion to a floor vote",
        "Article II Section 15A.1(b)",
        day,
        day + 3,
        severity="high",
    )


def handle_presiding_officer_fails_15a_motion(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    actor = event.get("actor", "Unknown actor")
    details = event.get("details", {})
    state.fail_obligation(
        "presiding_officer_15a_motion",
        day,
        "Regional Assembly presiding officer failed to bring the mandatory scheduling motion to a floor vote under Article II Section 15A.1(b).",
    )
    state.add_obligation(
        "dc_district_court_mandamus",
        "U.S. District Court for D.C.",
        "rule on the mandamus petition and order scheduling of the required vote",
        "Article II Section 15A.1(d)",
        day,
        day + 5,
        severity="high",
    )


def handle_mandamus_filed_dc_district_court(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    actor = event.get("actor", "Unknown actor")
    details = event.get("details", {})
    state.add_entry(
        day,
        "event",
        "An affected party files for mandamus in the U.S. District Court for the District of Columbia to compel scheduling of the required vote.",
        "Article II Section 15A.1(d)",
    )


def handle_court_orders_emergency_scheduling(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    actor = event.get("actor", "Unknown actor")
    details = event.get("details", {})
    state.resolve_obligation(
        "dc_district_court_mandamus",
        day,
        "issued a writ of mandamus ordering the Regional Assembly to schedule and hold the emergency declaration vote",
    )
    state.add_obligation(
        "regional_assembly_hold_court_ordered_vote",
        "Regional Assembly",
        "hold the emergency declaration vote as ordered by the court",
        "Article II Section 15A.1(d) and Article III Section 5.4",
        day,
        day + 7,
        severity="high",
    )


def handle_regional_assembly_approves_emergency(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    actor = event.get("actor", "Unknown actor")
    details = event.get("details", {})
    state.resolve_obligation("emergency_approve_ra", day, "approved the emergency declaration following court-ordered scheduling")
    state.resolve_obligation("regional_assembly_hold_court_ordered_vote", day, "held the required emergency declaration vote in compliance with the court order")


def handle_congressional_subpoena_issued(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    actor = event.get("actor", "Unknown actor")
    details = event.get("details", {})
    state.provisions.update({"Article II Section 16.2", "Article II Section 16.3"})
    state.add_entry(
        day,
        "event",
        f"House Judiciary Committee issues a subpoena to {details.get('target', 'Secretary of Defense')} requiring compliance within 30 days.",
        "Article II Section 16.2",
    )
    state.add_obligation(
        "executive_comply_subpoena",
        details.get("target", "Secretary of Defense"),
        "comply with the congressional subpoena by testifying and producing required documents",
        "Article II Section 16.2 and Section 16.3",
        day,
        day + 30,
        severity="high",
    )


def handle_executive_officer_defies_subpoena(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    actor = event.get("actor", "Unknown actor")
    details = event.get("details", {})
    message = f"{actor} willfully refuses to comply with a valid congressional subpoena."
    state.fail_obligation(
        "executive_comply_subpoena",
        day,
        f"{actor} failed to comply with the congressional subpoena by testifying and producing required documents by day 30 under Article II Section 16.2 and Section 16.3.",
    )
    state.add_violation(
        "subpoena_defiance",
        "executive_defiance",
        actor,
        message,
        "Article II Section 16.2 and Section 16.5",
        day,
    )
    state.add_obligation(
        "committee_refer_contempt_acc",
        "House Judiciary Committee",
        "refer the contempt citation to the Accountability Commission for criminal prosecution",
        "Article II Section 16.5(a)",
        day,
        day + 7,
        severity="high",
    )


def handle_contempt_referred_to_acc(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    actor = event.get("actor", "Unknown actor")
    details = event.get("details", {})
    state.resolve_obligation(
        "committee_refer_contempt_acc",
        day,
        "referred the contempt citation to the Accountability Commission for criminal prosecution",
    )
    state.add_obligation(
        "acc_prosecute_contempt",
        "Accountability Commission",
        "prosecute criminal contempt within 90 days of referral or publish specific written findings for declining",
        "Article II Section 16.5(b)",
        day,
        day + 90,
        severity="high",
    )


def handle_acc_initiates_contempt_prosecution(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    actor = event.get("actor", "Unknown actor")
    details = event.get("details", {})
    state.resolve_obligation(
        "acc_prosecute_contempt",
        day,
        "initiated criminal contempt prosecution within the required 90-day window",
    )


def handle_member_of_congress_accepts_bribe(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    actor = event.get("actor", "Unknown actor")
    details = event.get("details", {})
    state.provisions.update({"Article II Section 14.2", "Article II Section 5.3", "Article VIII Section 1.4", "Article VIII Section 1.7"})
    state.add_violation(
        "member_of_congress_bribery",
        "corruption",
        actor,
        "Senior member of Congress accepts money and future consulting promises from a regulated industry in exchange for official action, constituting bribery and abuse of office.",
        "Article II Section 14.2 and Article VIII Section 1.4",
        day,
    )


def handle_chamber_leadership_refuses_member_expulsion(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    actor = event.get("actor", "Unknown actor")
    details = event.get("details", {})
    state.add_entry(
        day,
        "event",
        "Chamber leadership refuses to pursue expulsion, but internal nonaction does not displace the Accountability Commission's independent jurisdiction over criminal corruption.",
        "Article II Section 14.2 and Article VIII Section 5.1",
    )


def handle_acc_opens_member_corruption_case(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    actor = event.get("actor", "Unknown actor")
    details = event.get("details", {})
    state.add_obligation(
        "acc_member_corruption_case",
        "Accountability Commission",
        "investigate and prosecute the congressional bribery matter notwithstanding any chamber preference for internal handling",
        "Article II Section 14.2 and Article VIII Section 5.1",
        day,
        None,
        severity="high",
    )
    state.resolve_obligation(
        "acc_member_corruption_case",
        day,
        "opened a corruption case against the member of Congress despite chamber leadership's refusal to move on expulsion",
    )


def handle_member_of_congress_convicted_of_bribery(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    actor = event.get("actor", "Unknown actor")
    details = event.get("details", {})
    state.add_obligation(
        "automatic_member_removal_bribery",
        "Federal courts and relevant chamber officers",
        "give effect to automatic removal upon final bribery conviction",
        "Article II Section 5.5(a) and Article VIII Section 1.7",
        day,
        None,
        severity="high",
    )
    state.resolve_obligation(
        "automatic_member_removal_bribery",
        day,
        "gave effect to automatic removal of the member from office upon bribery conviction; no chamber vote was required",
    )


def handle_official_commits_perjury_before_congress(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    actor = event.get("actor", "Unknown actor")
    details = event.get("details", {})
    state.provisions.update({"Article II Section 16.4", "Article II Section 16.4(b)"})
    state.add_violation(
        "congressional_perjury",
        "executive_defiance",
        actor,
        "Secretary of State gives testimony before a congressional committee containing knowing false statements of material fact, constituting perjury before Congress under Article II Section 16.4.",
        "Article II Section 16.4",
        day,
    )
    state.add_entry(
        day,
        "outcome",
        "Congressional perjury is prosecuted exclusively by the Accountability Commission. "
        "The Department of Justice has no role.",
        "Article II Section 16.4(b)",
    )
    state.add_obligation(
        "committee_refer_perjury_acc",
        "Senate Foreign Relations Committee",
        "refer the perjury matter to the Accountability Commission",
        "Article II Section 16.4(b)",
        day,
        day + 7,
        severity="high",
    )


def handle_committee_refers_perjury_to_acc(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    actor = event.get("actor", "Unknown actor")
    details = event.get("details", {})
    state.resolve_obligation(
        "committee_refer_perjury_acc",
        day,
        "referred the congressional perjury matter to the Accountability Commission for exclusive prosecution",
    )
    state.add_obligation(
        "acc_indict_congressional_perjury",
        "Accountability Commission",
        "indict the witness for congressional perjury if supported by the evidence",
        "Article II Section 16.4(b)",
        day,
        day + 30,
        severity="high",
    )


def handle_acc_indicts_for_congressional_perjury(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    actor = event.get("actor", "Unknown actor")
    details = event.get("details", {})
    state.resolve_obligation(
        "acc_indict_congressional_perjury",
        day,
        "indicted the witness for congressional perjury",
    )


def handle_omnibus_bill_passes_both_chambers(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    actor = event.get("actor", "Unknown actor")
    details = event.get("details", {})
    state.provisions.update({"Article II Section 10.7", "Article II Section 10.7A"})
    state.add_violation(
        "single_subject_violation",
        "legislative_deadline_failure",
        "Congress",
        "Congress passes an omnibus bill bundling unrelated subjects — defense appropriations, immigration rules, and drug pricing — in a single bill, in violation of the single-subject rule of Article II Section 10.7.",
        "Article II Section 10.7",
        day,
    )
    state.add_obligation(
        "supreme_court_review_single_subject",
        "Supreme Court",
        "review the pre-enactment single-subject challenge",
        "Article II Section 10.7A",
        day,
        day + 20,
        severity="high",
    )


def handle_single_subject_challenge_filed(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    actor = event.get("actor", "Unknown actor")
    details = event.get("details", {})
    state.add_entry(
        day,
        "event",
        "A pre-enactment single-subject challenge is filed against the omnibus bill.",
        "Article II Section 10.7A",
    )


def handle_supreme_court_voids_omnibus_bill(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    actor = event.get("actor", "Unknown actor")
    details = event.get("details", {})
    state.resolve_obligation(
        "supreme_court_review_single_subject",
        day,
        "voided the omnibus bill and returned the matter for single-subject redrafting",
    )


HANDLERS = {
    "regional_assembly_leadership_blocks_scheduling": handle_regional_assembly_leadership_blocks_scheduling,
    "regional_assembly_enters_recess_to_avoid_vote": handle_regional_assembly_enters_recess_to_avoid_vote,
    "section_15a_scheduling_motion_filed": handle_section_15a_scheduling_motion_filed,
    "presiding_officer_fails_15a_motion": handle_presiding_officer_fails_15a_motion,
    "mandamus_filed_dc_district_court": handle_mandamus_filed_dc_district_court,
    "court_orders_emergency_scheduling": handle_court_orders_emergency_scheduling,
    "regional_assembly_approves_emergency": handle_regional_assembly_approves_emergency,
    "congressional_subpoena_issued": handle_congressional_subpoena_issued,
    "executive_officer_defies_subpoena": handle_executive_officer_defies_subpoena,
    "contempt_referred_to_acc": handle_contempt_referred_to_acc,
    "acc_initiates_contempt_prosecution": handle_acc_initiates_contempt_prosecution,
    "member_of_congress_accepts_bribe": handle_member_of_congress_accepts_bribe,
    "chamber_leadership_refuses_member_expulsion": handle_chamber_leadership_refuses_member_expulsion,
    "acc_opens_member_corruption_case": handle_acc_opens_member_corruption_case,
    "member_of_congress_convicted_of_bribery": handle_member_of_congress_convicted_of_bribery,
    "official_commits_perjury_before_congress": handle_official_commits_perjury_before_congress,
    "committee_refers_perjury_to_acc": handle_committee_refers_perjury_to_acc,
    "acc_indicts_for_congressional_perjury": handle_acc_indicts_for_congressional_perjury,
    "omnibus_bill_passes_both_chambers": handle_omnibus_bill_passes_both_chambers,
    "single_subject_challenge_filed": handle_single_subject_challenge_filed,
    "supreme_court_voids_omnibus_bill": handle_supreme_court_voids_omnibus_bill,
}
