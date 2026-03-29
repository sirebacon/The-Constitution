from __future__ import annotations

from typing import Any

from sim_core import SimulationState


def handle_national_emergency_declared(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    actor = event.get("actor", "Unknown actor")
    details = event.get("details", {})
    state.provisions.update({"Article III Section 5", "Article I Section 3", "Article V Section 14"})
    state.add_entry(day, "event", f"{actor} declares a national emergency.", "Article III Section 5.1")
    state.add_obligation(
        "emergency_submit_ra",
        "President",
        "submit the emergency declaration to the Regional Assembly",
        "Article III Section 5.4",
        day,
        day + 2,
        severity="high",
    )
    state.add_obligation(
        "emergency_approve_ra",
        "Regional Assembly",
        "approve or reject the emergency declaration",
        "Article III Section 5.4",
        day,
        day + 30,
        severity="high",
    )
    if details.get("near_election"):
        state.notes.append("Emergency occurs near a federal election, which raises election-access constraints.")


def handle_emergency_submitted_to_regional_assembly(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    actor = event.get("actor", "Unknown actor")
    details = event.get("details", {})
    state.resolve_obligation("emergency_submit_ra", day, "submitted the emergency declaration to the Regional Assembly")


def handle_regional_assembly_rejects_or_fails_emergency(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    actor = event.get("actor", "Unknown actor")
    details = event.get("details", {})
    state.fail_obligation(
        "emergency_approve_ra",
        day,
        "Regional Assembly failed to approve or reject the emergency declaration by day 30 under Article III Section 5.4.",
    )
    state.add_entry(
        day,
        "outcome",
        "The emergency declaration lapses automatically at the end of day 30, the Chief Justice must issue a public certificate of lapse, and all emergency-dependent measures become void unless separately authorized by ordinary law.",
        "Article III Section 5.4",
    )


def handle_president_attempts_emergency_self_extension(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    actor = event.get("actor", "Unknown actor")
    details = event.get("details", {})
    state.provisions.update({"Article III Section 5.4", "Article V Section 1.3"})
    message = "President attempts to continue emergency restrictions without the constitutionally required outside review."
    state.add_violation(
        "emergency_self_extension",
        "executive_defiance",
        "President",
        message,
        "Article III Section 5.4",
        day,
    )
    state.add_entry(
        day,
        "outcome",
        "Emergency restrictions lapse absent the required constitutional renewal and cannot rest on internal executive memoranda alone.",
        "Article III Section 5.4",
    )


def handle_election_access_restricted_by_emergency(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    actor = event.get("actor", "Unknown actor")
    details = event.get("details", {})
    state.provisions.update({"Article I Section 3", "Article V Section 14"})
    message = "Emergency measures restrict access to polling places, early voting, or certification."
    state.add_violation(
        "emergency_election_restriction",
        "election_restriction",
        "Executive branch",
        message,
        "Article I Section 3.4 and Article V Section 14.2",
        day,
    )
    state.add_obligation(
        "court_review_emergency_election_restriction",
        "Federal courts",
        "review the emergency-based election restriction on an expedited basis",
        "Article I Section 3.4 and Article V Section 14.2",
        day,
        day + 3,
        severity="high",
    )


def handle_court_blocks_election_restriction(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    actor = event.get("actor", "Unknown actor")
    details = event.get("details", {})
    state.resolve_obligation(
        "court_review_emergency_election_restriction",
        day,
        "blocked the emergency-based restriction on election access",
    )


def handle_accountability_commission_investigation_opened(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    actor = event.get("actor", "Unknown actor")
    details = event.get("details", {})
    state.provisions.update({"Article III Section 15", "Article III Section 10", "Article XII Section 3"})
    state.add_entry(day, "event", "Accountability Commission opens an investigation into presidential conduct.", "Article III Section 15.8")


def handle_president_interferes_with_investigation(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    actor = event.get("actor", "Unknown actor")
    details = event.get("details", {})
    message = "President interferes with an investigation into their own conduct."
    state.add_violation(
        "president_interference_acc",
        "executive_defiance",
        "President",
        message,
        "Article III Section 15.8",
        day,
    )
    state.add_obligation(
        "acc_certify_obstruction",
        "Accountability Commission",
        "certify the presidential obstruction violation and transmit the matter for expedited impeachment consideration",
        "Article III Section 15.8 and Section 10.2A",
        day,
        day + 7,
        severity="high",
    )


def handle_accountability_commission_acts(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    actor = event.get("actor", "Unknown actor")
    details = event.get("details", {})
    state.resolve_obligation(
        "acc_certify_obstruction",
        day,
        "certified the obstruction violation and transmitted the matter for expedited impeachment consideration",
    )
    existing = state.obligations.get("house_vote_impeachment_obstruction")
    if existing is None:
        state.add_obligation(
            "house_vote_impeachment_obstruction",
            "House of Representatives",
            "hold a recorded impeachment vote on the certified obstruction violation",
            "Article III Section 10.2A and Section 15.8",
            day,
            day + 21,
            severity="high",
        )


def handle_house_member_files_obstruction_certification_motion(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    actor = event.get("actor", "House member")
    state.add_entry(
        day,
        "event",
        f"{actor} files a privileged certification motion after the Accountability Commission missed the certification deadline.",
        "Article III Section 10.2A and Section 15.8",
    )
    state.add_entry(
        day,
        "outcome",
        "The certification motion is deemed filed and certified upon submission to the Clerk and starts the expedited impeachment timetable without need for recognition, committee referral, or preliminary vote.",
        "Article III Section 10.2A",
    )
    existing = state.obligations.get("house_vote_impeachment_obstruction")
    if existing is None:
        state.add_obligation(
            "house_vote_impeachment_obstruction",
            "House of Representatives",
            "hold a recorded impeachment vote on the certified obstruction violation",
            "Article III Section 10.2A and Section 15.8",
            day,
            day + 21,
            severity="high",
        )


def handle_electoral_commission_certifies_election(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    actor = event.get("actor", "Unknown actor")
    details = event.get("details", {})
    state.provisions.update({"Article VI Section 1", "Article III Section 13"})
    state.add_entry(
        day,
        "event",
        "Electoral Commission certifies the election result and the constitutional transition period begins.",
        "Article III Section 13",
    )
    state.add_obligation(
        "president_transition_cooperation",
        "President",
        "cooperate with the constitutionally required transition",
        "Article III Section 13.1",
        day,
        day + 7,
        severity="high",
    )


def handle_president_refuses_transition_cooperation(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    actor = event.get("actor", "Unknown actor")
    details = event.get("details", {})
    state.fail_obligation(
        "president_transition_cooperation",
        day,
        "President refused to cooperate with the constitutionally required transition under Article III Section 13.1.",
    )
    state.add_violation(
        "transition_obstruction",
        "executive_defiance",
        "President",
        "Outgoing President refuses to cooperate with the constitutionally required transition, denying the President-elect access to security briefings and agency records.",
        "Article III Section 13.1 and Article VI Section 1",
        day,
    )
    state.add_obligation(
        "acc_transition_obstruction_case",
        "Accountability Commission",
        "open an electoral-subversion or transition-obstruction case",
        "Article VI Section 1 and Article III Section 13.2",
        day,
        day + 7,
        severity="high",
    )


def handle_acc_opens_electoral_subversion_investigation(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    actor = event.get("actor", "Unknown actor")
    details = event.get("details", {})
    state.resolve_obligation(
        "acc_transition_obstruction_case",
        day,
        "opened an electoral-subversion and transition-obstruction investigation",
    )


def handle_transition_proceeds_under_constitutional_mandate(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    actor = event.get("actor", "Unknown actor")
    details = event.get("details", {})
    state.add_entry(
        day,
        "outcome",
        "The constitutional transition proceeds despite presidential obstruction. Certification and term commencement are not dependent on outgoing presidential cooperation.",
        "Article III Section 13",
    )


def handle_president_issues_overreaching_executive_order(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    actor = event.get("actor", "Unknown actor")
    details = event.get("details", {})
    state.provisions.update({"Article III Section 6.2", "Article II Section 10"})
    state.add_violation(
        "executive_order_overreach",
        "executive_defiance",
        "President",
        "President issues an executive order imposing new regulatory obligations on private businesses without any statutory authorization, in violation of Article III Section 6.2(a).",
        "Article III Section 6.2(a)",
        day,
    )
    state.add_obligation(
        "congress_or_court_block_eo",
        "Congress",
        "disapprove or otherwise block the unauthorized executive order",
        "Article III Section 6.2 and Article II Section 10",
        day,
        day + 30,
        severity="high",
    )


def handle_congress_disapproves_executive_order(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    actor = event.get("actor", "Unknown actor")
    details = event.get("details", {})
    state.resolve_obligation(
        "congress_or_court_block_eo",
        day,
        "disapproved the unauthorized executive order and prevented it from taking effect",
    )


def handle_vp_and_cabinet_declare_presidential_incapacity(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    actor = event.get("actor", "Unknown actor")
    details = event.get("details", {})
    state.provisions.update({"Article III Section 11.2", "Article III Section 11.3"})
    state.add_entry(
        day,
        "event",
        "Vice President and Cabinet transmit a written declaration of presidential incapacity under Article III Section 11.2. The Vice President becomes Acting President.",
        "Article III Section 11.2",
    )
    state.add_entry(
        day,
        "outcome",
        "The President may contest this determination within 4 days. If contested, Congress has 21 days from the contest to resolve the question by 2/3 vote. If Congress does not sustain the determination within 21 days, the President resumes the powers of office.",
        "Article III Section 11.3",
    )


def handle_president_contests_incapacity(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    actor = event.get("actor", "Unknown actor")
    details = event.get("details", {})
    state.add_entry(
        day,
        "event",
        "President transmits a written contest of the incapacity determination within the 4-day window. The 21-day congressional resolution period begins.",
        "Article III Section 11.3",
    )
    state.add_obligation(
        "congress_resolve_incapacity_contest",
        "Congress",
        "resolve the contested incapacity determination by 2/3 vote of both chambers",
        "Article III Section 11.3",
        day,
        day + 21,
        severity="high",
    )


def handle_congress_fails_incapacity_determination(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    actor = event.get("actor", "Unknown actor")
    details = event.get("details", {})
    state.fail_obligation(
        "congress_resolve_incapacity_contest",
        day,
        "Congress failed to resolve the contested incapacity determination by 2/3 vote of both chambers by day 23 under Article III Section 11.3.",
    )
    state.add_entry(
        day,
        "outcome",
        "Under Article III Section 11.3, when Congress does not sustain the incapacity determination within 21 days, the President automatically resumes the powers of office. No further action by any branch is required.",
        "Article III Section 11.3",
    )


def handle_president_incapacitated(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    actor = event.get("actor", "Unknown actor")
    details = event.get("details", {})
    state.provisions.update({"Article III Section 12.2", "Article III Section 12.4"})
    state.add_entry(
        day,
        "event",
        "President becomes incapacitated and cannot discharge the powers of office.",
        "Article III Section 12.2",
    )
    state.add_obligation(
        "vp_assume_acting_presidency",
        "Vice President",
        "assume the Acting Presidency upon presidential incapacity",
        "Article III Section 12.2",
        day,
        day + 1,
        severity="high",
    )


def handle_vp_also_incapacitated(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    actor = event.get("actor", "Unknown actor")
    details = event.get("details", {})
    state.fail_obligation(
        "vp_assume_acting_presidency",
        day,
        "Vice President is also incapacitated and cannot assume the Acting Presidency under Article III Section 12.2.",
    )
    state.add_entry(
        day,
        "event",
        "Vice President is also incapacitated, creating a simultaneous succession crisis.",
        "Article III Section 12.2",
    )
    state.add_obligation(
        "speaker_assume_acting_presidency",
        "Speaker of the House",
        "assume the Acting Presidency under the constitutional succession order",
        "Article III Section 12.2",
        day,
        day + 1,
        severity="high",
    )


def handle_speaker_assumes_acting_presidency(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    actor = event.get("actor", "Unknown actor")
    details = event.get("details", {})
    state.resolve_obligation(
        "speaker_assume_acting_presidency",
        day,
        "assumed the Acting Presidency subject to the succession limits of Article III Section 12.4",
    )


def handle_recall_petition_certified(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    actor = event.get("actor", "Unknown actor")
    details = event.get("details", {})
    state.provisions.update({"Article III Section 14.5", "Article III Section 14.7"})
    state.add_entry(
        day,
        "event",
        "A presidential recall petition is certified and the recall referendum must now be scheduled.",
        "Article III Section 14.5",
    )
    state.add_obligation(
        "ec_schedule_recall_referendum",
        "Electoral Commission",
        "schedule and administer the recall referendum within 90 days of certification",
        "Article III Section 14.5",
        day,
        day + 90,
        severity="high",
    )


def handle_president_declares_emergency_to_delay_recall(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    actor = event.get("actor", "Unknown actor")
    details = event.get("details", {})
    state.provisions.update({"Article III Section 14.11", "Article III Section 5"})
    message = "President declares a national emergency for the purpose of delaying a certified recall referendum."
    state.add_violation(
        "recall_delay_emergency",
        "executive_defiance",
        "President",
        message,
        "Article III Section 14.11(a)",
        day,
        severity="high",
    )
    state.add_obligation(
        "court_review_recall_emergency",
        "Federal courts",
        "review the emergency declaration's effect on the recall referendum schedule",
        "Article III Section 14.11(a)",
        day,
        day + 5,
        severity="high",
    )


def handle_court_voids_recall_delay_emergency(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    actor = event.get("actor", "Unknown actor")
    details = event.get("details", {})
    state.resolve_obligation(
        "court_review_recall_emergency",
        day,
        "voided the emergency declaration insofar as it was used to delay the certified recall referendum",
    )


def handle_recall_referendum_held(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    actor = event.get("actor", "Unknown actor")
    details = event.get("details", {})
    state.resolve_obligation(
        "ec_schedule_recall_referendum",
        day,
        "administered the recall referendum within the required 90-day window",
    )


def handle_recall_fails_participation_threshold(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    actor = event.get("actor", "Unknown actor")
    details = event.get("details", {})
    state.add_entry(
        day,
        "outcome",
        "Recall referendum result: participation fell below the 60% threshold required by Article III Section 14.7. The President is retained. No further recall petition may be filed for the remainder of this term.",
        "Article III Section 14.7 and Section 14.4",
    )


def handle_acc_indicts_president(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    actor = event.get("actor", "Unknown actor")
    details = event.get("details", {})
    state.provisions.update({"Article III Section 7.2", "Article III Section 15.3", "Article XII Section 3"})
    state.add_entry(
        day,
        "event",
        "Accountability Commission indicts the President for criminal conduct falling within a no-immunity category.",
        "Article III Section 15.3",
    )


def handle_president_issues_self_pardon(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    actor = event.get("actor", "Unknown actor")
    details = event.get("details", {})
    state.add_violation(
        "president_self_pardon",
        "executive_defiance",
        "President",
        "President issues a pardon for their own criminal conduct.",
        "Article III Section 7.2(a)",
        day,
    )
    state.add_obligation(
        "acc_continue_after_self_pardon",
        "Accountability Commission",
        "continue the prosecution notwithstanding the void self-pardon",
        "Article III Section 7.2(a) and Section 15.3",
        day,
        day + 3,
        severity="high",
    )


def handle_acc_proceeds_despite_pardon_claim(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    actor = event.get("actor", "Unknown actor")
    details = event.get("details", {})
    state.resolve_obligation(
        "acc_continue_after_self_pardon",
        day,
        "continued the prosecution despite the self-pardon claim",
    )
    state.add_entry(
        day,
        "outcome",
        "The self-pardon is void. Presidential self-pardons are absolutely prohibited under Article III Section 7.2(a) and constitute a no-immunity category under Section 15.3. The Accountability Commission's prosecution continues without interruption.",
        "Article III Section 7.2(a) and Section 15.3",
    )


def handle_acc_opens_former_president_investigation(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    actor = event.get("actor", "Unknown actor")
    details = event.get("details", {})
    state.provisions.update({"Article III Section 15.6", "Article III Section 15.7"})
    state.add_entry(
        day,
        "event",
        "Accountability Commission opens a criminal investigation of a former President.",
        "Article III Section 15.6 and Section 15.7",
    )


def handle_former_president_asserts_residual_immunity(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    actor = event.get("actor", "Unknown actor")
    details = event.get("details", {})
    state.add_obligation(
        "court_reject_former_president_immunity",
        "Federal courts",
        "reject the residual immunity claim asserted by the former President",
        "Article III Section 15.6",
        day,
        day + 30,
        severity="high",
    )
    state.add_entry(
        day,
        "event",
        "Former President asserts residual immunity from criminal process for official acts after leaving office.",
        "Article III Section 15.6",
    )


def handle_court_rejects_immunity_claim(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    actor = event.get("actor", "Unknown actor")
    details = event.get("details", {})
    state.resolve_obligation(
        "court_reject_former_president_immunity",
        day,
        "rejected the former President's residual immunity claim and allowed prosecution to proceed",
    )


HANDLERS = {
    "national_emergency_declared": handle_national_emergency_declared,
    "emergency_submitted_to_regional_assembly": handle_emergency_submitted_to_regional_assembly,
    "regional_assembly_rejects_or_fails_emergency": handle_regional_assembly_rejects_or_fails_emergency,
    "president_attempts_emergency_self_extension": handle_president_attempts_emergency_self_extension,
    "election_access_restricted_by_emergency": handle_election_access_restricted_by_emergency,
    "court_blocks_election_restriction": handle_court_blocks_election_restriction,
    "accountability_commission_investigation_opened": handle_accountability_commission_investigation_opened,
    "president_interferes_with_investigation": handle_president_interferes_with_investigation,
    "accountability_commission_acts": handle_accountability_commission_acts,
    "house_member_files_obstruction_certification_motion": handle_house_member_files_obstruction_certification_motion,
    "electoral_commission_certifies_election": handle_electoral_commission_certifies_election,
    "president_refuses_transition_cooperation": handle_president_refuses_transition_cooperation,
    "acc_opens_electoral_subversion_investigation": handle_acc_opens_electoral_subversion_investigation,
    "transition_proceeds_under_constitutional_mandate": handle_transition_proceeds_under_constitutional_mandate,
    "president_issues_overreaching_executive_order": handle_president_issues_overreaching_executive_order,
    "congress_disapproves_executive_order": handle_congress_disapproves_executive_order,
    "vp_and_cabinet_declare_presidential_incapacity": handle_vp_and_cabinet_declare_presidential_incapacity,
    "president_contests_incapacity": handle_president_contests_incapacity,
    "congress_fails_incapacity_determination": handle_congress_fails_incapacity_determination,
    "president_incapacitated": handle_president_incapacitated,
    "vp_also_incapacitated": handle_vp_also_incapacitated,
    "speaker_assumes_acting_presidency": handle_speaker_assumes_acting_presidency,
    "recall_petition_certified": handle_recall_petition_certified,
    "president_declares_emergency_to_delay_recall": handle_president_declares_emergency_to_delay_recall,
    "court_voids_recall_delay_emergency": handle_court_voids_recall_delay_emergency,
    "recall_referendum_held": handle_recall_referendum_held,
    "recall_fails_participation_threshold": handle_recall_fails_participation_threshold,
    "acc_indicts_president": handle_acc_indicts_president,
    "president_issues_self_pardon": handle_president_issues_self_pardon,
    "acc_proceeds_despite_pardon_claim": handle_acc_proceeds_despite_pardon_claim,
    "acc_opens_former_president_investigation": handle_acc_opens_former_president_investigation,
    "former_president_asserts_residual_immunity": handle_former_president_asserts_residual_immunity,
    "court_rejects_immunity_claim": handle_court_rejects_immunity_claim,
}
