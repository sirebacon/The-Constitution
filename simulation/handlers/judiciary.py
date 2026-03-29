from __future__ import annotations

from typing import Any

from sim_core import SimulationState


def handle_court_issues_compliance_order(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    actor = event.get("actor", "Unknown actor")
    details = event.get("details", {})
    state.provisions.add("Article II Section 16.2")
    respondent = details.get("respondent", "Executive agency")
    state.add_entry(
        day,
        "event",
        f"Federal court issues a compliance order to {respondent}. Compliance is required within 15 days under Article II Section 16.2(c).",
        "Article II Section 16.2(c)",
    )
    state.add_obligation(
        "executive_comply_court_order",
        respondent,
        "comply with the federal court enforcement order",
        "Article II Section 16.2(c)",
        day,
        day + 15,
        severity="high",
    )


def handle_executive_defies_court_order(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    actor = event.get("actor", "Unknown actor")
    details = event.get("details", {})
    message = f"{actor} fails to comply with a federal court enforcement order within the required 15-day period."
    state.add_violation(
        "executive_defies_court_order",
        "executive_defiance",
        actor,
        message,
        "Article II Section 16.2(c)",
        day,
        severity="high",
    )
    state.fail_obligation(
        "executive_comply_court_order",
        day,
        f"{actor} failed to comply with the federal court enforcement order by day 15 under Article II Section 16.2(c).",
    )
    state.add_obligation(
        "marshals_enforce_court_order",
        "U.S. Marshals Service",
        "enforce the federal court order without further executive approval",
        "Article II Section 16.2(c)",
        day,
        day + 5,
        severity="high",
    )


def handle_marshals_enforce_court_order(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    actor = event.get("actor", "Unknown actor")
    details = event.get("details", {})
    state.resolve_obligation(
        "marshals_enforce_court_order",
        day,
        "enforced the court order notwithstanding executive resistance",
    )


def handle_chief_justice_vacancy_occurs(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    actor = event.get("actor", "Unknown actor")
    details = event.get("details", {})
    state.provisions.update({"Article IV Section 2.7", "Article IV Section 3.1"})
    state.add_entry(day, "event", "Chief Justice becomes unavailable and a constitutional duty must still be performed.", "Article IV Section 2.7")


def handle_judicial_continuity_activated(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    actor = event.get("actor", "Unknown actor")
    details = event.get("details", {})
    state.add_entry(
        day,
        "outcome",
        "The most senior available Associate Justice performs the designated constitutional duty under the judicial continuity rule.",
        "Article IV Section 2.7",
    )


def handle_president_refuses_to_nominate(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    actor = event.get("actor", "Unknown actor")
    details = event.get("details", {})
    state.provisions.update({"Article IV Section 3.4", "Article IV Section 3.1", "Article XII Section 2"})
    state.add_obligation(
        "president_nominate_justice",
        "President",
        "submit a Supreme Court nomination from the certified pool",
        "Article IV Section 3.4",
        day,
        day + 30,
        severity="high",
    )
    state.fail_obligation(
        "president_nominate_justice",
        day,
        "President refused to submit a nomination within the required period, triggering the Judicial Nominations Commission backstop under Article IV Section 3.4.",
    )


def handle_judicial_nominations_commission_appoints_directly(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    actor = event.get("actor", "Unknown actor")
    details = event.get("details", {})
    state.provisions.add("Article IV Section 3.4")
    state.add_entry(
        day,
        "event",
        f"{actor} exercises its backstop appointment authority and appoints a justice from the certified pool directly. The appointment takes office without further confirmation.",
        "Article IV Section 3.4",
    )


def handle_supreme_court_hears_major_case(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    actor = event.get("actor", "Unknown actor")
    details = event.get("details", {})
    state.provisions.update({"Article IV Section 10.1", "Article IV Section 10.4"})
    state.add_entry(
        day,
        "event",
        "The Supreme Court hears a major constitutional case with obvious national political consequences.",
        "Article IV Section 10.1",
    )
    state.add_obligation(
        "supreme_court_delay_notice",
        "Supreme Court",
        "publish a public notice identifying the case and the reason for delay if no decision has issued within six months of argument",
        "Article IV Section 10.1",
        day,
        day + 180,
        severity="high",
    )
    state.add_obligation(
        "supreme_court_decide_expedited_case",
        "Supreme Court",
        "issue a written decision in the constitutionally expedited case",
        "Article IV Section 10.1",
        day,
        day + 365,
        severity="high",
    )


def handle_supreme_court_fails_delay_notice(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    actor = event.get("actor", "Unknown actor")
    details = event.get("details", {})
    state.fail_obligation(
        "supreme_court_delay_notice",
        day,
        "Supreme Court failed to publish the required public notice after six months without decision in a major constitutional case under Article IV Section 10.1.",
    )
    state.add_violation(
        "supreme_court_strategic_delay_pattern",
        "institutional_stress",
        "Supreme Court",
        "The Court appears to be using delay itself to affect the political timing of a major constitutional dispute.",
        "Article IV Section 10.1",
        day,
        severity="high",
    )
    state.add_entry(
        day,
        "outcome",
        "Because the case involves constitutionally expedited election administration review, the last operative lower-court judgment remains temporarily in force until the Supreme Court acts or publicly enters a narrower interim order supported by written findings of genuine necessity.",
        "Article IV Section 10.1 and Section 10.4",
    )
    state.add_obligation(
        "judicial_conduct_board_delay_review",
        "Judicial Conduct Board",
        "review the pattern of judicial delay and determine whether it reflects strategic misconduct rather than genuine complexity or workload",
        "Article IV Section 10.1 and Section 10.4",
        day,
        None,
        severity="high",
    )


def handle_judicial_conduct_board_opens_delay_review(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    actor = event.get("actor", "Unknown actor")
    details = event.get("details", {})
    state.add_entry(
        day,
        "event",
        "Judicial Conduct Board opens review of the Court's delay pattern and the apparent failure to provide the required public notice.",
        "Article IV Section 10.1 and Section 10.4",
    )


def handle_judicial_conduct_board_finds_strategic_delay(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    actor = event.get("actor", "Unknown actor")
    details = event.get("details", {})
    state.resolve_obligation(
        "judicial_conduct_board_delay_review",
        day,
        "found that the delay pattern was strategic and intended to achieve political effect rather than attributable to genuine complexity or workload",
    )
    state.add_entry(
        day,
        "outcome",
        "The finding constitutes conduct-based grounds for judicial removal and does not rest on the substance of any judicial opinion.",
        "Article IV Section 8.1, Section 8.2, and Section 10.1",
    )


def handle_supreme_court_misses_expedited_decision_deadline(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    actor = event.get("actor", "Unknown actor")
    details = event.get("details", {})
    state.fail_obligation(
        "supreme_court_decide_expedited_case",
        day,
        "Supreme Court failed to issue a written decision within twelve months of argument in a constitutionally expedited case under Article IV Section 10.1.",
    )
    state.add_entry(
        day,
        "outcome",
        "The last operative lower-court judgment becomes final and binding on the parties to the case and is no longer subject to Supreme Court review.",
        "Article IV Section 10.1 and Section 10.4",
    )


def handle_amendment_submitted_for_preclearance(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    details = event.get("details", {})
    track = details.get("track", "track_1")
    title = details.get("title", "proposed constitutional amendment")
    source = "Article XI Section 2 and Section 4"
    state.provisions.update({"Article XI Section 2", "Article XI Section 3", "Article XI Section 4"})
    state.add_entry(
        day,
        "event",
        f"{title} is submitted to the Supreme Court for mandatory pre-clearance review before ratification may begin.",
        source,
    )
    deadline = day + (60 if track == "track_2" else 90)
    duty = "issue a pre-clearance ruling on the proposed amendment"
    state.add_obligation(
        "supreme_court_preclear_amendment",
        "Supreme Court",
        duty,
        "Article XI Section 4.1, Section 4.3, and Section 4.4",
        day,
        deadline,
        severity="high",
    )


def handle_supreme_court_rejects_amendment_preclearance(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    details = event.get("details", {})
    title = details.get("title", "The proposed amendment")
    reason = details.get(
        "reason",
        "would materially impair the capacity of citizens to alter their government through free and regular elections",
    )
    state.resolve_obligation(
        "supreme_court_preclear_amendment",
        day,
        f"rejected the proposed amendment at pre-clearance and published a written opinion stating that it {reason}",
    )
    state.add_violation(
        "authoritarian_amendment_attempt",
        "institutional_stress",
        "Congress",
        f"{title} attempts to evade the unamendable core or principled backstop by structurally entrenching political power.",
        "Article XI Section 3.1 and Section 3.2",
        day,
        severity="high",
    )


def handle_supreme_court_misses_preclearance_deadline(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    details = event.get("details", {})
    track = details.get("track", "track_1")
    state.fail_obligation(
        "supreme_court_preclear_amendment",
        day,
        f"Supreme Court failed to issue the required pre-clearance ruling within the {'60-day' if track == 'track_2' else '90-day'} deadline under Article XI Section 4.3.",
    )
    state.add_entry(
        day,
        "outcome",
        "Pre-clearance is deemed granted by operation of Article XI Section 4.3 and the amendment may proceed to ratification.",
        "Article XI Section 4.3",
    )


def handle_states_ratify_amendment(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    details = event.get("details", {})
    title = details.get("title", "The proposed amendment")
    state.add_entry(
        day,
        "event",
        f"{title} receives the required state ratifications under the applicable amendment track.",
        "Article XI Section 2",
    )
    if details.get("track", "track_1") == "track_2":
        state.add_obligation(
            "national_referendum_confirm_rights_amendment",
            "Electoral Commission",
            "administer and certify the national referendum confirming the rights amendment",
            "Article XI Section 2",
            day,
            day + 30,
            severity="high",
        )


def handle_national_referendum_confirms_rights_amendment(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    details = event.get("details", {})
    title = details.get("title", "The rights amendment")
    state.resolve_obligation(
        "national_referendum_confirm_rights_amendment",
        day,
        "administered and certified the national referendum confirming the rights amendment",
    )
    state.add_entry(
        day,
        "outcome",
        f"{title} is constitutionally ratified and takes effect on the timeline specified by Article XI.",
        "Article XI Section 2",
    )


def handle_supreme_court_issues_emergency_stay_without_explanation(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    details = event.get("details", {})
    case = details.get("case", "a pending case")
    state.provisions.add("Article IV Section 9.7")
    state.add_entry(
        day,
        "event",
        f"Supreme Court issues an emergency stay or injunction in {case} without a written explanation. Under Article IV Section 9.7, an explanation is required within 48 hours.",
        "Article IV Section 9.7",
    )
    state.add_obligation(
        "supreme_court_explain_emergency_stay",
        "Supreme Court",
        "publish a written explanation identifying the legal basis and the justices joining the emergency order",
        "Article IV Section 9.7",
        day,
        day + 2,
        severity="high",
    )


def handle_supreme_court_explains_emergency_stay(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    state.resolve_obligation(
        "supreme_court_explain_emergency_stay",
        day,
        "published a written explanation of the emergency stay identifying the legal basis and the joining justices",
    )
    state.add_entry(
        day,
        "outcome",
        "The emergency stay is procedurally valid under Article IV Section 9.7. The explanation is public and the joining justices are identified.",
        "Article IV Section 9.7",
    )


def handle_party_moves_to_void_unexplained_order(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    state.provisions.add("Article IV Section 9.7")
    state.fail_obligation(
        "supreme_court_explain_emergency_stay",
        day,
        "Supreme Court failed to provide a written explanation within 48 hours; a party has moved to void the unexplained emergency order under Article IV Section 9.7.",
    )
    state.add_obligation(
        "originating_court_void_unexplained_stay",
        "Originating court",
        "void the unexplained emergency stay pursuant to Article IV Section 9.7",
        "Article IV Section 9.7",
        day,
        day + 5,
        severity="high",
    )


def handle_originating_court_voids_unexplained_emergency_stay(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    state.resolve_obligation(
        "originating_court_void_unexplained_stay",
        day,
        "voided the unexplained emergency stay for failure to comply with the Article IV Section 9.7 explanation requirement",
    )
    state.add_entry(
        day,
        "outcome",
        "Emergency orders that lack a written explanation within 48 hours are voidable on motion under Article IV Section 9.7. The underlying proceeding resumes on the pre-stay schedule.",
        "Article IV Section 9.7",
    )


def handle_party_demands_justice_recusal(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    details = event.get("details", {})
    justice = details.get("justice", "A justice")
    ground = details.get("ground", "financial conflict of interest")
    state.provisions.add("Article IV Section 7.3")
    state.add_entry(
        day,
        "event",
        f"A party petitions the Judicial Conduct Board for recusal of {justice} on the ground of {ground}, pursuant to Article IV Section 7.3.",
        "Article IV Section 7.3",
    )
    state.add_obligation(
        "conduct_board_rule_on_recusal",
        "Judicial Conduct Board",
        "rule on the recusal petition and direct the justice to recuse if the petition meets the standard",
        "Article IV Section 7.3",
        day,
        day + 14,
        severity="high",
    )


def handle_justice_refuses_valid_recusal_demand(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    details = event.get("details", {})
    justice = details.get("justice", "The justice")
    state.provisions.add("Article IV Section 7.3")
    state.add_violation(
        "justice_refuses_recusal",
        "institutional_stress",
        justice,
        f"{justice} refuses to recuse despite a valid Judicial Conduct Board direction under Article IV Section 7.3. The refusal triggers an automatic referral and the justice is barred from the case.",
        "Article IV Section 7.3",
        day,
        severity="high",
    )
    state.resolve_obligation(
        "conduct_board_rule_on_recusal",
        day,
        "directed recusal; the justice refused, triggering automatic referral and case bar under Article IV Section 7.3",
    )
    state.add_obligation(
        "conduct_board_process_recusal_referral",
        "Judicial Conduct Board",
        "process the automatic recusal-refusal referral and determine whether removal proceedings are warranted",
        "Article IV Section 7.3",
        day,
        day + 30,
        severity="high",
    )


def handle_judicial_conduct_board_processes_recusal_referral(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    details = event.get("details", {})
    outcome = details.get("outcome", "referred the matter for impeachment proceedings")
    state.resolve_obligation(
        "conduct_board_process_recusal_referral",
        day,
        f"processed the recusal-refusal referral and {outcome}",
    )
    state.add_entry(
        day,
        "outcome",
        "Refusal to comply with a valid recusal direction is independently reviewable conduct under Article IV Section 7.3. The justice is barred from the case regardless of the removal outcome.",
        "Article IV Section 7.3 and Section 8.1",
    )


def handle_house_proposes_judge_impeachment_articles(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    details = event.get("details", {})
    judge = details.get("judge", "A federal judge")
    state.provisions.update({"Article IV Section 8.1", "Article IV Section 8.2"})
    state.add_entry(
        day,
        "event",
        f"House Judiciary Committee proposes articles of impeachment against {judge}. Under Article IV Section 8.1, the Judicial Conduct Board must certify within 60 days whether the articles are conduct-based.",
        "Article IV Section 8.1",
    )
    state.add_obligation(
        "conduct_board_certify_articles_conduct_based",
        "Judicial Conduct Board",
        "certify whether the proposed impeachment articles are conduct-based and not based on the substance of judicial opinions",
        "Article IV Section 8.1",
        day,
        day + 60,
        severity="high",
    )


def handle_conduct_board_certifies_articles_conduct_based(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    state.resolve_obligation(
        "conduct_board_certify_articles_conduct_based",
        day,
        "certified that the proposed impeachment articles are conduct-based and do not rest on the substance of any judicial opinion",
    )
    state.add_entry(
        day,
        "outcome",
        "Certification satisfied. The House may proceed to a full impeachment vote under Article IV Section 8.1.",
        "Article IV Section 8.1",
    )


def handle_house_invokes_conduct_board_certification_override(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    state.provisions.add("Article IV Section 8.1")
    state.fail_obligation(
        "conduct_board_certify_articles_conduct_based",
        day,
        "Judicial Conduct Board failed to certify within 60 days; House invokes the certification override by 2/3 vote under Article IV Section 8.1.",
    )
    state.add_entry(
        day,
        "event",
        "The House votes by 2/3 majority to declare the articles conduct-based under the Article IV Section 8.1 certification override. The 2/3 vote constitutes the required finding and the House may proceed to a full impeachment vote.",
        "Article IV Section 8.1",
    )
    state.add_obligation(
        "house_full_impeachment_vote_after_override",
        "House of Representatives",
        "hold a full impeachment vote on the articles following the certification override",
        "Article IV Section 8.1",
        day,
        day + 30,
        severity="high",
    )


def handle_house_votes_impeach_after_override(state: SimulationState, event: dict[str, Any]) -> None:
    day = int(event["day"])
    details = event.get("details", {})
    result = details.get("result", "passed")
    state.resolve_obligation(
        "house_full_impeachment_vote_after_override",
        day,
        f"voted on the impeachment articles following the certification override; vote {result}",
    )
    if result == "passed":
        state.add_entry(
            day,
            "outcome",
            "Impeachment articles adopted. The matter proceeds to the Regional Assembly for trial under Article IV Section 8.2.",
            "Article IV Section 8.1 and Section 8.2",
        )


HANDLERS = {
    "court_issues_compliance_order": handle_court_issues_compliance_order,
    "executive_defies_court_order": handle_executive_defies_court_order,
    "marshals_enforce_court_order": handle_marshals_enforce_court_order,
    "chief_justice_vacancy_occurs": handle_chief_justice_vacancy_occurs,
    "judicial_continuity_activated": handle_judicial_continuity_activated,
    "president_refuses_to_nominate": handle_president_refuses_to_nominate,
    "judicial_nominations_commission_appoints_directly": handle_judicial_nominations_commission_appoints_directly,
    "supreme_court_hears_major_case": handle_supreme_court_hears_major_case,
    "supreme_court_fails_delay_notice": handle_supreme_court_fails_delay_notice,
    "judicial_conduct_board_opens_delay_review": handle_judicial_conduct_board_opens_delay_review,
    "judicial_conduct_board_finds_strategic_delay": handle_judicial_conduct_board_finds_strategic_delay,
    "supreme_court_misses_expedited_decision_deadline": handle_supreme_court_misses_expedited_decision_deadline,
    "amendment_submitted_for_preclearance": handle_amendment_submitted_for_preclearance,
    "supreme_court_rejects_amendment_preclearance": handle_supreme_court_rejects_amendment_preclearance,
    "supreme_court_misses_preclearance_deadline": handle_supreme_court_misses_preclearance_deadline,
    "states_ratify_amendment": handle_states_ratify_amendment,
    "national_referendum_confirms_rights_amendment": handle_national_referendum_confirms_rights_amendment,
    "supreme_court_issues_emergency_stay_without_explanation": handle_supreme_court_issues_emergency_stay_without_explanation,
    "supreme_court_explains_emergency_stay": handle_supreme_court_explains_emergency_stay,
    "party_moves_to_void_unexplained_order": handle_party_moves_to_void_unexplained_order,
    "originating_court_voids_unexplained_emergency_stay": handle_originating_court_voids_unexplained_emergency_stay,
    "party_demands_justice_recusal": handle_party_demands_justice_recusal,
    "justice_refuses_valid_recusal_demand": handle_justice_refuses_valid_recusal_demand,
    "judicial_conduct_board_processes_recusal_referral": handle_judicial_conduct_board_processes_recusal_referral,
    "house_proposes_judge_impeachment_articles": handle_house_proposes_judge_impeachment_articles,
    "conduct_board_certifies_articles_conduct_based": handle_conduct_board_certifies_articles_conduct_based,
    "house_invokes_conduct_board_certification_override": handle_house_invokes_conduct_board_certification_override,
    "house_votes_impeach_after_override": handle_house_votes_impeach_after_override,
}
