#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import io
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
SCENARIOS_DIR = ROOT / "scenarios"


@dataclass
class Obligation:
    key: str
    actor: str
    duty: str
    source: str
    created_day: int
    due_day: int | None = None
    status: str = "open"
    closed_day: int | None = None
    outcome: str | None = None
    severity: str = "medium"


@dataclass
class TimelineEntry:
    day: int
    kind: str
    message: str
    source: str | None = None


@dataclass
class Issue:
    id: str
    category: str
    actor: str
    summary: str
    source: str
    severity: str
    day: int
    deadline_day: int | None = None


@dataclass
class SimulationState:
    title: str
    provisions: set[str] = field(default_factory=set)
    obligations: dict[str, Obligation] = field(default_factory=dict)
    timeline: list[TimelineEntry] = field(default_factory=list)
    bottlenecks: list[Issue] = field(default_factory=list)
    violations: list[Issue] = field(default_factory=list)
    notes: list[str] = field(default_factory=list)

    def add_entry(self, day: int, kind: str, message: str, source: str | None = None) -> None:
        self.timeline.append(TimelineEntry(day=day, kind=kind, message=message, source=source))

    def add_obligation(
        self,
        key: str,
        actor: str,
        duty: str,
        source: str,
        created_day: int,
        due_day: int | None,
        severity: str = "medium",
    ) -> None:
        self.obligations[key] = Obligation(
            key=key,
            actor=actor,
            duty=duty,
            source=source,
            created_day=created_day,
            due_day=due_day,
            severity=severity,
        )
        due_text = f" by day {due_day}" if due_day is not None else ""
        self.add_entry(created_day, "obligation", f"{actor} must {duty}{due_text}.", source)

    def resolve_obligation(self, key: str, day: int, resolution: str, success: bool = True) -> None:
        obligation = self.obligations.get(key)
        if not obligation or obligation.status in {"satisfied", "failed"}:
            return
        obligation.status = "satisfied" if success else "failed"
        obligation.closed_day = day
        obligation.outcome = resolution
        kind = "resolution" if success else "failure"
        self.add_entry(day, kind, f"{obligation.actor} {resolution}.", obligation.source)

    def fail_obligation(self, key: str, day: int, summary: str) -> None:
        obligation = self.obligations.get(key)
        if not obligation or obligation.status == "failed":
            return
        obligation.status = "failed"
        obligation.closed_day = day
        obligation.outcome = summary
        self.bottlenecks.append(
            Issue(
                id=key,
                category=categorize_failed_obligation(obligation) if obligation.due_day is not None else "unperformed_duty",
                actor=obligation.actor,
                summary=summary,
                source=obligation.source,
                severity=obligation.severity,
                day=day,
                deadline_day=obligation.due_day,
            )
        )
        self.add_entry(day, "bottleneck", summary, obligation.source)
        if key == "house_vote_impeachment_obstruction":
            self.add_entry(
                day,
                "outcome",
                "The certified obstruction charge is automatically transmitted to the Regional Assembly as articles of impeachment limited to the certified violation.",
                "Article III Section 10.2A",
            )
            self.add_obligation(
                "regional_assembly_trial_obstruction",
                "Regional Assembly",
                "proceed to impeachment trial on the automatically transmitted obstruction articles",
                "Article III Section 10.2A and Section 10.3",
                day,
                day + 21,
                severity="high",
            )
        elif key == "house_vote_impeachment_war":
            self.add_entry(
                day,
                "outcome",
                "The certified war-powers charge is automatically transmitted to the Regional Assembly as articles of impeachment limited to the certified violation.",
                "Article III Section 10.2A",
            )
            self.add_obligation(
                "regional_assembly_trial_war",
                "Regional Assembly",
                "proceed to impeachment trial on the automatically transmitted war-powers articles",
                "Article III Section 10.2A and Section 10.3",
                day,
                day + 21,
                severity="high",
            )
        elif key == "house_vote_impeachment_pmc":
            self.add_entry(
                day,
                "outcome",
                "The certified PMC-substitution charge is automatically transmitted to the Regional Assembly as articles of impeachment limited to the certified violation.",
                "Article III Section 10.2A",
            )
            self.add_obligation(
                "regional_assembly_trial_pmc",
                "Regional Assembly",
                "proceed to impeachment trial on the automatically transmitted PMC-substitution articles",
                "Article III Section 10.2A and Section 10.3",
                day,
                day + 21,
                severity="high",
            )

    def add_violation(
        self,
        issue_id: str,
        category: str,
        actor: str,
        summary: str,
        source: str,
        day: int,
        severity: str = "high",
    ) -> None:
        self.violations.append(
            Issue(
                id=issue_id,
                category=category,
                actor=actor,
                summary=summary,
                source=source,
                severity=severity,
                day=day,
            )
        )
        self.add_entry(day, "violation", summary, source)

    def check_due_obligations(self, current_day: int) -> None:
        for obligation in list(self.obligations.values()):
            if obligation.status != "open" or obligation.due_day is None:
                continue
            if current_day > obligation.due_day:
                overdue_message = (
                    f"{obligation.actor} failed to {obligation.duty} by day {obligation.due_day} "
                    f"under {obligation.source}."
                )
                self.fail_obligation(obligation.key, current_day, overdue_message)


def derive_system_risk(summary_data: dict[str, Any]) -> str:
    categories = {issue["category"] for issue in summary_data["violations"] + summary_data["bottlenecks"]}
    if "executive_defiance" in categories:
        return "executive_defiance"
    if "state_backsliding" in categories:
        return "democratic_backsliding"
    if "legislative_deadline_failure" in categories:
        return "legislative_delay"
    if "election_restriction" in categories:
        return "election_stress"
    return "institutional_stress" if categories else "none"


def categorize_failed_obligation(obligation: Obligation) -> str:
    if obligation.source.startswith("Article X Section 1.6"):
        return "state_backsliding"
    if obligation.actor in {"Congress", "House of Representatives", "Regional Assembly", "Speaker of the House"}:
        return "legislative_deadline_failure"
    if obligation.actor in {"Federal courts", "Chief Justice", "Supreme Court", "U.S. District Court for D.C."}:
        return "judicial_delay"
    if obligation.actor in {"Accountability Commission", "Electoral Commission"}:
        return "institutional_deadline_failure"
    return "missed_deadline"


def scenario_paths() -> list[Path]:
    return sorted(SCENARIOS_DIR.glob("*.json"))


def load_scenario(path: Path) -> dict[str, Any]:
    with path.open() as f:
        return json.load(f)


def handle_event(state: SimulationState, event: dict[str, Any]) -> None:
    event_type = event["type"]
    day = int(event["day"])
    actor = event.get("actor", "Unknown actor")
    details = event.get("details", {})

    if event_type == "national_emergency_declared":
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
            state.provisions.add("Article I Section 3.4")
            state.notes.append("Emergency occurs near a federal election, which raises election-access constraints.")

    elif event_type == "emergency_submitted_to_regional_assembly":
        state.resolve_obligation("emergency_submit_ra", day, "submitted the emergency declaration to the Regional Assembly")

    elif event_type == "regional_assembly_rejects_or_fails_emergency":
        state.resolve_obligation("emergency_approve_ra", day, "failed to approve the emergency declaration, causing it to lapse", success=False)
        state.add_entry(day, "outcome", "Emergency declaration lapses unless independently authorized ordinary law remains in effect.", "Article III Section 5.4")
        state.add_entry(
            day,
            "outcome",
            "The Chief Justice issues a public certificate of lapse, and any continued enforcement of emergency-dependent measures is constitutionally void unless separately authorized by ordinary law.",
            "Article III Section 5.4",
        )

    elif event_type == "president_attempts_emergency_self_extension":
        state.provisions.update({"Article III Section 5", "Article V Section 1.3", "Article V Section 14"})
        message = "President attempts to continue emergency restrictions without the constitutionally required outside review."
        state.add_violation(
            "president_attempts_emergency_self_extension",
            "executive_defiance",
            "President",
            message,
            "Article III Section 5.4 and Article V Section 1.3",
            day,
        )
        state.add_entry(
            day,
            "outcome",
            "Emergency restrictions lapse absent the required constitutional renewal and cannot rest on internal executive memoranda alone.",
            "Article III Section 5.4 and Article V Section 1.3",
        )

    elif event_type == "election_access_restricted_by_emergency":
        state.provisions.add("Article I Section 3.4")
        message = "Emergency measures restrict access to polling places, early voting, or certification."
        state.add_violation(
            "emergency_election_restriction",
            "election_restriction",
            "Executive branch",
            message,
            "Article I Section 3.4",
            day,
        )
        state.add_obligation(
            "court_review_emergency_election",
            "Federal courts",
            "resolve the election-access challenge",
            "Article I Section 3.4",
            day,
            day + 3,
            severity="high",
        )

    elif event_type == "court_blocks_election_restriction":
        state.resolve_obligation("court_review_emergency_election", day, "blocked the election restriction on strict-scrutiny review")

    elif event_type == "accountability_commission_investigation_opened":
        state.provisions.update({"Article III Section 15", "Article IX Section 3"})
        state.add_entry(day, "event", f"{actor} opens an investigation into presidential misconduct.", "Article III Section 15.7")

    elif event_type == "president_interferes_with_investigation":
        state.provisions.add("Article III Section 15.8")
        message = "President interferes with an investigation into their own conduct."
        state.add_violation(
            "president_interferes_with_investigation",
            "executive_defiance",
            "President",
            message,
            "Article III Section 15.8",
            day,
        )
        state.add_obligation(
            "acc_prosecute_obstruction",
            "Accountability Commission",
            "pursue obstruction-related enforcement",
            "Article III Section 15.8",
            day,
            day + 30,
            severity="high",
        )

    elif event_type == "accountability_commission_acts":
        state.resolve_obligation("acc_prosecute_obstruction", day, "acted on the obstruction matter and formally certified the violation")
        state.add_obligation(
            "house_vote_impeachment_obstruction",
            "House of Representatives",
            "hold a recorded impeachment vote on the certified obstruction violation",
            "Article III Section 10.2A and Section 15.8",
            day,
            day + 21,
            severity="high",
        )

    elif event_type == "supreme_court_finds_state_democratic_floor_violation":
        state.provisions.update({"Article X Section 1.5", "Article X Section 1.6"})
        state.add_entry(day, "event", "Supreme Court finds persistent and material violation of the democratic floor.", "Article X Section 1.6(a)")
        state.add_obligation(
            "congress_state_remedy",
            "Congress",
            "enact a remedial measure for the violating state",
            "Article X Section 1.6(b)",
            day,
            day + 180,
            severity="high",
        )

    elif event_type == "congress_fails_state_remedy":
        state.add_entry(day, "event", "Congress fails to enact a timely remedy for the state democratic-floor violation.", "Article X Section 1.6(b)")
        state.fail_obligation(
            "congress_state_remedy",
            day,
            "Congress failed to enact a remedial measure for the violating state by day 180 under Article X Section 1.6(b).",
        )
        state.add_entry(
            day,
            "outcome",
            "Federal elections in the state shift immediately to federally supervised administration through the Electoral Commission pending congressional action or Supreme Court certification of compliance.",
            "Article X Section 1.6(c)",
        )
        state.add_obligation(
            "congress_vote_suspend_representation",
            "Congress",
            "hold a recorded vote on suspension of the state's representation",
            "Article X Section 1.6(c)",
            day,
            day + 30,
            severity="high",
        )

    elif event_type == "state_violation_persists_one_year":
        state.add_entry(day, "event", "The state remains in material violation one year after the Supreme Court finding.", "Article X Section 1.6(d)")
        vote_obligation = state.obligations.get("congress_vote_suspend_representation")
        if not vote_obligation or vote_obligation.status != "satisfied":
            state.add_entry(
                day,
                "outcome",
                "The state's representation is suspended automatically until the Supreme Court certifies compliance.",
                "Article X Section 1.6(d)",
            )

    elif event_type == "congress_suspends_representation":
        state.resolve_obligation(
            "congress_vote_suspend_representation",
            day,
            "held the required vote and suspended the state's representation pending Supreme Court certification of compliance",
        )

    elif event_type == "regional_assembly_begins_trial_on_transmitted_articles":
        trial_type = details.get("trial_type", "certified")
        if trial_type == "obstruction":
            state.resolve_obligation(
                "regional_assembly_trial_obstruction",
                day,
                "began trial on automatically transmitted obstruction articles",
            )
        elif trial_type == "war":
            state.resolve_obligation(
                "regional_assembly_trial_war",
                day,
                "began trial on automatically transmitted war-powers articles",
            )

    elif event_type == "unauthorized_military_action_started":
        state.provisions.update({"Article XVI Section 1", "Article III Section 10"})
        state.add_entry(day, "event", f"{actor} initiates military action without prior authorization.", "Article XVI Section 1")
        state.add_obligation(
            "congress_authorize_force",
            "Congress",
            "grant authorization for continued military force or refuse it",
            "Article XVI Section 1",
            day,
            day + 30,
            severity="high",
        )

    elif event_type == "congress_fails_aumf":
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

    elif event_type == "chief_justice_issues_withdrawal_order":
        state.resolve_obligation("chief_justice_withdrawal_order", day, "issued a withdrawal order")

    elif event_type == "president_ignores_withdrawal_order":
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

    elif event_type == "president_declares_domestic_insurrection":
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

    elif event_type == "courts_reject_domestic_deployment":
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

    elif event_type == "service_members_refuse_unlawful_order":
        state.resolve_obligation(
            "service_members_assess_order",
            day,
            "refused the unconstitutional domestic deployment order",
        )

    elif event_type == "foreign_cyber_election_attack_detected":
        state.provisions.update(
            {
                "Article I election administration provisions",
                "Article V speech and press protections",
                "Article VI democratic integrity provisions",
                "Article X federalism provisions",
                "Article XVI war powers",
                "Article XVII foreign policy and national security",
            }
        )
        state.add_entry(
            day,
            "event",
            "A foreign adversary hacks voter systems, releases forged materials, and disrupts power near an election.",
        )
        state.add_obligation(
            "electoral_commission_protect_election",
            "Electoral Commission",
            "coordinate constitutional election-protection measures with the states",
            "Article I election administration provisions and Article IX electoral administration provisions",
            day,
            day + 3,
            severity="high",
        )
        state.add_obligation(
            "executive_choose_nonmilitary_response",
            "President",
            "confine immediate response measures to non-military Article XVII authorities unless Article XI is lawfully triggered",
            "Article XVI war powers and Article XVII foreign policy and national security",
            day,
            day + 1,
            severity="high",
        )
        state.add_obligation(
            "federal_courts_protect_speech",
            "Federal courts",
            "review any attempted suppression of protected expression",
            "Article V speech and press protections",
            day,
            day + 3,
            severity="high",
        )

    elif event_type == "president_attempts_direct_state_takeover":
        message = "President attempts direct federal control over state election administration outside the constitutional election framework."
        state.add_violation(
            "president_attempts_direct_state_takeover",
            "federalism_breach",
            "President",
            message,
            "Article I election administration provisions and Article X federalism provisions",
            day,
        )

    elif event_type == "president_attempts_speech_restriction":
        message = "Executive branch attempts to suppress suspected foreign propaganda directly rather than using disclosure and transparency tools."
        state.add_violation(
            "president_attempts_speech_restriction",
            "rights_suppression",
            "Executive branch",
            message,
            "Article V speech and press protections",
            day,
        )

    elif event_type == "electoral_commission_acts":
        state.resolve_obligation(
            "electoral_commission_protect_election",
            day,
            "implemented constitutional election-protection measures in coordination with affected states",
        )

    elif event_type == "president_uses_article_xiv_tools":
        state.resolve_obligation(
            "executive_choose_nonmilitary_response",
            day,
            "used attribution, sanctions, and other non-military countermeasures under Article XVII",
        )

    elif event_type == "courts_block_speech_restriction":
        state.resolve_obligation(
            "federal_courts_protect_speech",
            day,
            "blocked direct suppression of protected expression while allowing disclosure-based responses",
        )

    elif event_type == "regional_assembly_leadership_blocks_scheduling":
        state.provisions.add("Article II Section 15A")
        message = "Regional Assembly leadership refuses to place the emergency declaration on the floor calendar within the required period."
        state.add_violation(
            "ra_leadership_blocks_scheduling",
            "legislative_deadline_failure",
            "Regional Assembly leadership",
            message,
            "Article II Section 15A.1 and Article III Section 5.4",
            day,
            severity="high",
        )
        state.add_entry(
            day,
            "outcome",
            "Any member of the Regional Assembly may now file a mandatory scheduling motion under Article II Section 15A.1(b).",
            "Article II Section 15A.1(b)",
        )

    elif event_type == "regional_assembly_enters_recess_to_avoid_vote":
        state.provisions.update({"Article II Section 15A", "Article III Section 5.4"})
        message = (
            "Regional Assembly leadership attempts to run out the emergency-approval deadline by entering recess "
            "instead of holding the constitutionally required vote."
        )
        state.add_violation(
            "ra_recess_evasion",
            "legislative_deadline_failure",
            "Regional Assembly leadership",
            message,
            "Article II Section 15A.1(e)-(f) and Article III Section 5.4",
            day,
            severity="high",
        )
        state.add_entry(
            day,
            "outcome",
            "Recess does not suspend the day-30 emergency deadline. The Regional Assembly remains constitutionally obligated to reconvene under Article II Section 15A.1(f) and hold the vote.",
            "Article II Section 15A.1(e)-(f) and Article III Section 5.4",
        )
        state.add_entry(
            day,
            "outcome",
            "Any member of the Regional Assembly may file a mandatory scheduling motion, and any affected party may seek mandamus in the U.S. District Court for the District of Columbia if recess is used to block the vote.",
            "Article II Section 15A.1(b) and (d)",
        )

    elif event_type == "section_15a_scheduling_motion_filed":
        state.provisions.add("Article II Section 15A")
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

    elif event_type == "presiding_officer_fails_15a_motion":
        state.fail_obligation(
            "presiding_officer_15a_motion",
            day,
            "Regional Assembly presiding officer failed to bring the mandatory scheduling motion to a floor vote under Article II Section 15A.1(b).",
        )
        state.add_entry(
            day,
            "outcome",
            "The scheduling failure activates the Article II Section 15A.1(d) mandamus route: any affected party may petition the U.S. District Court for the District of Columbia to compel scheduling.",
            "Article II Section 15A.1(d)",
        )

    elif event_type == "mandamus_filed_dc_district_court":
        state.provisions.add("Article II Section 15A")
        state.add_entry(
            day,
            "event",
            f"{actor} files a mandamus petition in the U.S. District Court for the District of Columbia to compel scheduling of the emergency declaration vote.",
            "Article II Section 15A.1(d)",
        )
        state.add_obligation(
            "dc_court_mandamus_emergency",
            "U.S. District Court for D.C.",
            "rule on the mandamus petition and order scheduling of the required vote",
            "Article II Section 15A.1(d)",
            day,
            day + 5,
            severity="high",
        )

    elif event_type == "court_orders_emergency_scheduling":
        state.resolve_obligation(
            "dc_court_mandamus_emergency",
            day,
            "issued a writ of mandamus ordering the Regional Assembly to schedule and hold the emergency declaration vote",
        )
        state.add_obligation(
            "ra_comply_court_order_emergency",
            "Regional Assembly",
            "hold the emergency declaration vote as ordered by the court",
            "Article II Section 15A.1(d) and Article III Section 5.4",
            day,
            day + 7,
            severity="high",
        )

    elif event_type == "regional_assembly_approves_emergency":
        state.resolve_obligation(
            "emergency_approve_ra",
            day,
            "approved the emergency declaration following court-ordered scheduling",
        )
        state.resolve_obligation(
            "ra_comply_court_order_emergency",
            day,
            "held the required emergency declaration vote in compliance with the court order",
        )

    # --- Category A: Executive Power Limits ---

    elif event_type == "acc_indicts_president":
        state.provisions.add("Article III Section 15.5")
        state.add_entry(
            day,
            "event",
            f"{actor} indicts the sitting President. Trial is stayed until the President leaves office; pre-trial proceedings continue.",
            "Article III Section 15.5",
        )
        state.add_obligation(
            "acc_continue_pretrial",
            "Accountability Commission",
            "continue pre-trial proceedings while the President remains in office",
            "Article III Section 15.5",
            day,
            None,
            severity="medium",
        )

    elif event_type == "president_issues_self_pardon":
        state.provisions.update({"Article III Section 7.2", "Article III Section 15.3"})
        message = "President issues a pardon for their own criminal conduct."
        state.add_violation(
            "president_self_pardon",
            "executive_defiance",
            "President",
            message,
            "Article III Section 7.2(a) and Section 15.3",
            day,
            severity="high",
        )
        state.add_entry(
            day,
            "outcome",
            "The self-pardon is void. Presidential self-pardons are absolutely prohibited under Article III Section 7.2(a) and constitute a no-immunity category under Section 15.3. The Accountability Commission's prosecution continues without interruption.",
            "Article III Section 7.2(a) and Section 15.3",
        )

    elif event_type == "acc_proceeds_despite_pardon_claim":
        state.resolve_obligation(
            "acc_continue_pretrial",
            day,
            "proceeded with pre-trial proceedings notwithstanding the void self-pardon claim",
        )

    # --- Category B: Legislative Enforcement ---

    elif event_type == "congressional_subpoena_issued":
        state.provisions.update({"Article II Section 16.2", "Article II Section 16.3"})
        target = details.get("target", "Subpoenaed executive official")
        state.add_entry(
            day,
            "event",
            f"{actor} issues a subpoena to {target} requiring compliance within 30 days.",
            "Article II Section 16.2",
        )
        state.add_obligation(
            "executive_comply_subpoena",
            target,
            "comply with the congressional subpoena by testifying and producing required documents",
            "Article II Section 16.2 and Section 16.3",
            day,
            day + 30,
            severity="high",
        )

    elif event_type == "executive_officer_defies_subpoena":
        message = f"{actor} willfully refuses to comply with a valid congressional subpoena."
        state.add_violation(
            "subpoena_defiance",
            "executive_defiance",
            actor,
            message,
            "Article II Section 16.2 and Section 16.5",
            day,
            severity="high",
        )
        state.fail_obligation(
            "executive_comply_subpoena",
            day,
            f"{actor} failed to comply with the congressional subpoena by the required deadline under Article II Section 16.2.",
        )
        state.add_obligation(
            "contempt_referral_to_acc",
            "House Judiciary Committee",
            "refer the contempt citation to the Accountability Commission for criminal prosecution",
            "Article II Section 16.5(a)",
            day,
            day + 7,
            severity="medium",
        )

    elif event_type == "contempt_referred_to_acc":
        state.resolve_obligation(
            "contempt_referral_to_acc",
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

    elif event_type == "acc_initiates_contempt_prosecution":
        state.resolve_obligation(
            "acc_prosecute_contempt",
            day,
            "initiated criminal contempt prosecution within the required 90-day window",
        )

    elif event_type == "member_of_congress_accepts_bribe":
        state.provisions.update({"Article II Section 5.3", "Article II Section 14.2", "Article VIII Section 1.4", "Article VIII Section 1.7"})
        message = (
            f"{actor} accepts money and future consulting promises from a regulated industry in exchange for official action, "
            "constituting bribery and abuse of office."
        )
        state.add_violation(
            "member_of_congress_bribery",
            "corruption",
            actor,
            message,
            "Article II Section 14.2 and Article VIII Section 1.4",
            day,
            severity="high",
        )
        state.add_obligation(
            "acc_member_corruption_case",
            "Accountability Commission",
            "investigate and prosecute the congressional bribery matter notwithstanding any chamber preference for internal handling",
            "Article II Section 14.2 and Article VIII Section 5.1",
            day,
            None,
            severity="high",
        )

    elif event_type == "chamber_leadership_refuses_member_expulsion":
        state.add_entry(
            day,
            "outcome",
            "Chamber leadership refuses to pursue expulsion, but internal nonaction does not displace the Accountability Commission's independent jurisdiction over criminal corruption.",
            "Article II Section 5.3 and Section 14.2",
        )

    elif event_type == "acc_opens_member_corruption_case":
        state.resolve_obligation(
            "acc_member_corruption_case",
            day,
            "opened a corruption case against the member of Congress despite chamber leadership's refusal to move on expulsion",
        )
        state.add_obligation(
            "member_automatic_removal_on_bribery_conviction",
            "Federal courts and relevant chamber officers",
            "give effect to automatic removal upon final bribery conviction",
            "Article II Section 5.5(a) and Article VIII Section 1.7",
            day,
            None,
            severity="high",
        )

    elif event_type == "member_of_congress_convicted_of_bribery":
        state.resolve_obligation(
            "member_automatic_removal_on_bribery_conviction",
            day,
            "gave effect to automatic removal of the member from office upon bribery conviction; no chamber vote was required",
        )
        state.add_entry(
            day,
            "outcome",
            "The member is automatically removed from office upon conviction for bribery. Chamber leadership's refusal to expel did not prevent constitutional accountability.",
            "Article II Section 5.5(a) and Article VIII Section 1.7",
        )

    elif event_type == "budget_deadline_missed":
        state.provisions.update({"Article XV Section 3.2", "Article XV Section 3.3"})
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

    elif event_type == "executive_attempts_selective_cr_funding":
        state.provisions.add("Article XV Section 3.4")
        message = "Executive branch attempts to alter funding ratios, withhold appropriated funds, or selectively apply funding levels under the automatic continuing resolution."
        state.add_violation(
            "executive_cr_manipulation",
            "executive_defiance",
            "Executive branch",
            message,
            "Article XV Section 3.4",
            day,
            severity="high",
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

    elif event_type == "court_blocks_cr_manipulation":
        state.resolve_obligation(
            "court_review_cr_manipulation",
            day,
            "issued an expedited order blocking the executive branch's selective application of the automatic continuing resolution",
        )

    # --- Category D: War Powers ---

    elif event_type == "president_orders_nuclear_first_use":
        state.provisions.update({"Article XVI Section 3.1", "Article XVI Section 3.2"})
        state.add_entry(
            day,
            "event",
            f"{actor} orders first use of nuclear weapons without a prior nuclear attack on the United States.",
            "Article XVI Section 3.1",
        )
        state.add_obligation(
            "secdef_confirm_nuclear_order",
            "Secretary of Defense",
            "confirm or refuse the nuclear first-use order",
            "Article XVI Section 3.1",
            day,
            day + 1,
            severity="high",
        )
        state.add_obligation(
            "secstate_confirm_nuclear_order",
            "Secretary of State",
            "confirm or refuse the nuclear first-use order",
            "Article XVI Section 3.1",
            day,
            day + 1,
            severity="high",
        )

    elif event_type == "secretary_of_defense_refuses_nuclear_order":
        state.resolve_obligation(
            "secdef_confirm_nuclear_order",
            day,
            "refused to confirm the nuclear first-use order, blocking the launch under Article XVI Section 3.1",
        )
        state.add_entry(
            day,
            "outcome",
            "Nuclear first-use order cannot proceed. Under Article XVI Section 3.1, the order does not proceed if either Secretary declines to confirm it.",
            "Article XVI Section 3.1",
        )

    elif event_type == "secretary_of_state_refuses_nuclear_order":
        state.resolve_obligation(
            "secstate_confirm_nuclear_order",
            day,
            "refused to confirm the nuclear first-use order",
        )

    elif event_type == "president_fires_secretary_to_compel_nuclear_compliance":
        state.provisions.add("Article III Section 4.4")
        message = "President removes the Secretary of Defense to install a replacement willing to confirm a nuclear first-use order, using the removal power to circumvent a constitutional authorization safeguard."
        state.add_violation(
            "removal_to_circumvent_nuclear_safeguard",
            "executive_defiance",
            "President",
            message,
            "Article XVI Section 3.1 and Article III Section 4.4",
            day,
            severity="high",
        )
        state.add_obligation(
            "acting_secdef_confirm_nuclear_order",
            "Acting Secretary of Defense",
            "confirm or refuse the nuclear first-use order",
            "Article XVI Section 3.1",
            day,
            day + 1,
            severity="high",
        )

    elif event_type == "acting_secretary_also_refuses_nuclear_order":
        state.resolve_obligation(
            "acting_secdef_confirm_nuclear_order",
            day,
            "also refused to confirm the nuclear first-use order; the launch remains blocked",
        )
        state.resolve_obligation(
            "secstate_confirm_nuclear_order",
            day,
            "declined to confirm the nuclear first-use order",
        )
        state.add_entry(
            day,
            "outcome",
            "The nuclear first-use order remains blocked. The President's removal of the Secretary of Defense did not produce a compliant replacement. No authorized officer has confirmed the order.",
            "Article XVI Section 3.1",
        )

    # --- Category I: Presidential Recall ---

    elif event_type == "recall_petition_certified":
        state.provisions.add("Article III Section 14")
        state.add_entry(
            day,
            "event",
            f"{actor} certifies that the recall petition meets all requirements of Article III Section 14.3.",
            "Article III Section 14.3 and Section 14.5",
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

    elif event_type == "president_declares_emergency_to_delay_recall":
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

    elif event_type == "court_voids_recall_delay_emergency":
        state.resolve_obligation(
            "court_review_recall_emergency",
            day,
            "voided the emergency declaration insofar as it was used to delay the certified recall referendum",
        )

    elif event_type == "recall_referendum_held":
        state.resolve_obligation(
            "ec_schedule_recall_referendum",
            day,
            "administered the recall referendum within the required 90-day window",
        )

    elif event_type == "recall_fails_participation_threshold":
        state.add_entry(
            day,
            "outcome",
            "Recall referendum result: participation fell below the 60% threshold required by Article III Section 14.7. The President is retained. No further recall petition may be filed for the remainder of this term.",
            "Article III Section 14.7 and Section 14.4",
        )

    # --- Category C: Judicial Independence ---

    elif event_type == "court_issues_compliance_order":
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

    elif event_type == "executive_defies_court_order":
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
            f"{actor} failed to comply with the court enforcement order by the required deadline under Article II Section 16.2(c).",
        )
        state.add_entry(
            day,
            "outcome",
            "The respondent is in contempt of court. Civil detention and daily fines apply. Enforcement is by the United States Marshals Service without requiring action by the Department of Justice.",
            "Article II Section 16.2(c)",
        )
        state.add_obligation(
            "marshals_enforce_order",
            "U.S. Marshals Service",
            "enforce the court order through civil contempt mechanisms without requiring DOJ direction",
            "Article II Section 16.2(c)",
            day,
            day + 1,
            severity="high",
        )

    elif event_type == "marshals_enforce_court_order":
        state.resolve_obligation(
            "marshals_enforce_order",
            day,
            "enforced the court order through civil contempt mechanisms without DOJ involvement",
        )

    elif event_type == "chief_justice_vacancy_occurs":
        state.provisions.update({"Article IV Section 2.3", "Article IV Section 2.7"})
        state.add_entry(
            day,
            "event",
            "The Chief Justice seat becomes vacant before the end of its scheduled term.",
            "Article IV Section 2.3",
        )

    elif event_type == "judicial_continuity_activated":
        state.provisions.add("Article IV Section 2.7")
        state.add_entry(
            day,
            "event",
            "Judicial continuity rule activates: the most senior Associate Justice assumes Chief Justice duties; the most senior willing Senior Justice fills the vacant seat temporarily until the next scheduled appointment date.",
            "Article IV Section 2.3 and Section 2.7",
        )
        state.add_obligation(
            "president_nominate_justice",
            "President",
            "nominate a qualified candidate from the Judicial Nominations Commission certified pool to fill the scheduled vacancy",
            "Article IV Section 3.1",
            day,
            day + 90,
            severity="medium",
        )

    elif event_type == "president_refuses_to_nominate":
        message = "President refuses to submit a nomination from the Judicial Nominations Commission certified pool to fill a scheduled Supreme Court vacancy."
        state.add_violation(
            "president_refuses_nomination_duty",
            "executive_defiance",
            "President",
            message,
            "Article IV Section 3.1 and Article III Section 1.2(d)",
            day,
            severity="high",
        )
        state.fail_obligation(
            "president_nominate_justice",
            day,
            "President refused to submit a nomination within the required period, triggering the Judicial Nominations Commission backstop under Article IV Section 3.4.",
        )

    elif event_type == "judicial_nominations_commission_appoints_directly":
        state.provisions.add("Article IV Section 3.4")
        state.add_entry(
            day,
            "event",
            f"{actor} exercises its backstop appointment authority and appoints a justice from the certified pool directly. The appointment takes office without further confirmation.",
            "Article IV Section 3.4",
        )

    elif event_type == "supreme_court_hears_major_case":
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

    elif event_type == "supreme_court_fails_delay_notice":
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
        state.add_obligation(
            "judicial_conduct_board_delay_review",
            "Judicial Conduct Board",
            "review the pattern of judicial delay and determine whether it reflects strategic misconduct rather than genuine complexity or workload",
            "Article IV Section 10.1 and Section 10.4",
            day,
            None,
            severity="high",
        )

    elif event_type == "judicial_conduct_board_opens_delay_review":
        state.add_entry(
            day,
            "event",
            "Judicial Conduct Board opens review of the Court's delay pattern and the apparent failure to provide the required public notice.",
            "Article IV Section 10.1 and Section 10.4",
        )

    elif event_type == "judicial_conduct_board_finds_strategic_delay":
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

    # --- Category E continued: Emergency Rights ---

    elif event_type == "emergency_used_to_restrict_protected_speech":
        state.provisions.update({"Article III Section 5.3", "Article V"})
        message = "Executive branch uses an emergency declaration to restrict protected expression, in violation of the absolute bar on overriding Article V rights through emergency powers."
        state.add_violation(
            "emergency_rights_suppression",
            "rights_suppression",
            "Executive branch",
            message,
            "Article III Section 5.3(f)",
            day,
            severity="high",
        )
        state.add_obligation(
            "court_void_emergency_rights_violation",
            "Federal courts",
            "void the emergency-based speech restriction",
            "Article III Section 5.3(f) and Article V",
            day,
            day + 5,
            severity="high",
        )

    elif event_type == "court_voids_emergency_rights_restriction":
        state.resolve_obligation(
            "court_void_emergency_rights_violation",
            day,
            "voided the emergency-based restriction on protected expression; Article V rights may not be overridden by emergency declaration",
        )

    elif event_type == "president_suspends_habeas_corpus_by_executive_order":
        state.provisions.update({"Article III Section 5.7", "Article III Section 5"})
        message = "President suspends the privilege of the writ of habeas corpus by executive order. This power belongs exclusively to Congress under Article III Section 5.7 and may not be exercised by the President alone."
        state.add_violation(
            "president_suspends_habeas_corpus",
            "executive_defiance",
            "President",
            message,
            "Article III Section 5.7",
            day,
            severity="high",
        )
        state.add_obligation(
            "court_void_habeas_suspension",
            "Federal courts",
            "void the unlawful executive suspension of habeas corpus",
            "Article III Section 5.7",
            day,
            day + 5,
            severity="high",
        )

    elif event_type == "court_voids_habeas_suspension":
        state.resolve_obligation(
            "court_void_habeas_suspension",
            day,
            "voided the executive suspension of habeas corpus; only Congress may suspend the writ under Article III Section 5.7",
        )

    # --- Category F: Elections ---

    elif event_type == "electoral_commission_certifies_election":
        state.provisions.update({"Article I", "Article III Section 13", "Article VI Section 1"})
        state.add_entry(
            day,
            "event",
            f"{actor} certifies the election result and the President-elect. The constitutional transition period begins.",
            "Article III Section 13.1",
        )
        state.add_obligation(
            "president_cooperate_transition",
            "President",
            "cooperate fully with the President-elect's transition including security briefings, agency access, and office space",
            "Article III Section 13.1",
            day,
            day + 81,
            severity="high",
        )

    elif event_type == "president_refuses_transition_cooperation":
        message = "Outgoing President refuses to cooperate with the constitutionally required transition, denying the President-elect access to security briefings and agency records."
        state.add_violation(
            "transition_obstruction",
            "executive_defiance",
            "President",
            message,
            "Article III Section 13.5 and Article VI Section 1",
            day,
            severity="high",
        )
        state.fail_obligation(
            "president_cooperate_transition",
            day,
            "President refused to cooperate with the constitutionally required transition under Article III Section 13.1.",
        )

    elif event_type == "acc_opens_electoral_subversion_investigation":
        state.provisions.add("Article VI Section 1")
        state.add_entry(
            day,
            "event",
            f"{actor} opens an electoral subversion investigation into the outgoing President's transition obstruction.",
            "Article VI Section 1 and Article III Section 15.7",
        )
        state.add_obligation(
            "acc_pursue_subversion_case",
            "Accountability Commission",
            "pursue the electoral subversion case through investigation and prosecution",
            "Article VI Section 1",
            day,
            None,
            severity="high",
        )

    elif event_type == "transition_proceeds_under_constitutional_mandate":
        state.resolve_obligation(
            "acc_pursue_subversion_case",
            day,
            "continued pursuing the electoral subversion case while the transition proceeded under constitutional mandate",
        )
        state.add_entry(
            day,
            "outcome",
            "The constitutional transfer of power proceeds. Presidential obstruction does not prevent the transition — it only creates additional criminal exposure for the outgoing President.",
            "Article III Section 13 and Article VI Section 1",
        )

    elif event_type == "constitution_ratified":
        state.provisions.update({"Article XIX Section 4", "Article XIX Section 5"})
        state.add_entry(
            day,
            "event",
            "The Constitution is ratified and the first-cycle implementation period begins.",
            "Article XIX Section 1 and Section 4",
        )
        state.add_obligation(
            "congress_first_election_law",
            "Congress",
            "provide by law for the first federal elections and orderly commencement of terms under the new constitutional order",
            "Article XIX Section 4.1 and Section 4.2",
            day,
            day + 365,
            severity="high",
        )
        state.add_obligation(
            "constitute_constitutional_organs",
            "Congress and appointing authorities",
            "constitute the Constitutional Organs on the timeline required by the Constitution",
            "Article XIX Section 5.2",
            day,
            day + 365,
            severity="high",
        )

    elif event_type == "congress_fails_first_election_law":
        state.fail_obligation(
            "congress_first_election_law",
            day,
            "Congress failed to provide by law for the first federal election on the timetable required by Article XIX Section 4.1 and Section 4.2.",
        )
        state.add_entry(
            day,
            "outcome",
            "The Electoral Commission must administer the first federal election under interim rules consistent with the Constitution, subject to expedited judicial review.",
            "Article XIX Section 4.5",
        )
        state.add_obligation(
            "electoral_commission_interim_first_election",
            "Electoral Commission",
            "publish and administer interim rules for the first federal election",
            "Article XIX Section 4.5",
            day,
            day + 30,
            severity="high",
        )

    elif event_type == "congress_enacts_first_election_law":
        state.resolve_obligation(
            "congress_first_election_law",
            day,
            "provided by law for the first federal elections and orderly commencement of terms under the new constitutional order",
        )

    elif event_type == "electoral_commission_administers_interim_first_election":
        state.resolve_obligation(
            "electoral_commission_interim_first_election",
            day,
            "published interim first-election rules and administered the first federal election under constitutional supervision",
        )

    elif event_type == "constitutional_organs_constituted":
        state.resolve_obligation(
            "constitute_constitutional_organs",
            day,
            "constituted the Electoral Commission and Accountability Commission on the constitutional timetable",
        )

    elif event_type == "constitutional_organs_deadline_missed":
        state.fail_obligation(
            "constitute_constitutional_organs",
            day,
            "Congress and appointing authorities failed to constitute the Constitutional Organs by the one-year deadline and no impossibility finding has yet been identified publicly by the Supreme Court under Article XIX Section 5.2.",
        )
        state.add_obligation(
            "supreme_court_orders_constitutional_organs_completion",
            "Supreme Court",
            "order completion of the constitutional-organ appointment process",
            "Article XIX Section 5.2A",
            day,
            day + 30,
            severity="high",
        )
        state.add_entry(
            day,
            "outcome",
            "The missed deadline triggers a Supreme Court duty to order completion of the appointment process within 30 days.",
            "Article XIX Section 5.2A",
        )

    elif event_type == "supreme_court_orders_constitutional_organs_completion":
        state.resolve_obligation(
            "supreme_court_orders_constitutional_organs_completion",
            day,
            "ordered completion of the constitutional-organ appointment process within 30 days",
        )
        state.add_obligation(
            "complete_constitutional_organs_after_court_order",
            "Congress and appointing authorities",
            "complete the constitutional-organ appointment process after Supreme Court order",
            "Article XIX Section 5.2A",
            day,
            day + 30,
            severity="high",
        )

    elif event_type == "supreme_court_makes_temporary_constitutional_organ_appointments":
        state.fail_obligation(
            "complete_constitutional_organs_after_court_order",
            day,
            "Congress and appointing authorities failed to complete the constitutional-organ appointment process within 30 days after Supreme Court order under Article XIX Section 5.2A.",
        )
        state.add_entry(
            day,
            "outcome",
            "The Supreme Court appointed the minimum temporary Commissioners necessary to create lawful quorums and begin startup, continuity, and protective functions in the affected Constitutional Organs.",
            "Article XIX Section 5.2A",
        )

    elif event_type == "state_denies_overseas_citizen_assignment":
        state.provisions.update({"Article IX Section 2", "Article IX Section 3", "Article IX Section 6", "Article I Section 12"})
        message = "Election officials deny an overseas citizen any practical federal electoral home and reject registration on the theory that long residence abroad extinguished meaningful federal participation."
        state.add_violation(
            "overseas_assignment_denied",
            "membership_exclusion",
            "Election officials",
            message,
            "Article IX Section 2.3, Section 3.3, and Section 6.4",
            day,
            severity="high",
        )
        state.add_obligation(
            "court_review_overseas_assignment",
            "Federal courts",
            "resolve the overseas-citizen assignment dispute and restore a practical federal electoral home if the denial is unconstitutional",
            "Article IX Section 3.3 and Section 6.4",
            day,
            day + 7,
            severity="high",
        )

    elif event_type == "court_restores_overseas_assignment":
        state.resolve_obligation(
            "court_review_overseas_assignment",
            day,
            "held that residence abroad does not extinguish federal political membership and restored a practical federal electoral assignment",
        )

    elif event_type == "naturalized_candidate_excluded_by_statute":
        state.provisions.update({"Article IX Section 1", "Article IX Section 4"})
        message = "A federal statute bars naturalized citizens from holding a non-presidential federal office, creating a blanket civic disability based on the manner of citizenship."
        state.add_violation(
            "naturalized_candidate_excluded",
            "caste_hierarchy",
            "Congress",
            message,
            "Article IX Section 1.1 and Section 4.1 through Section 4.3",
            day,
            severity="high",
        )
        state.add_obligation(
            "court_review_naturalized_candidate_exclusion",
            "Federal courts",
            "resolve the challenge to the exclusion of naturalized citizens from federal office",
            "Article IX Section 4.1 through Section 4.3",
            day,
            day + 10,
            severity="high",
        )

    elif event_type == "court_voids_naturalized_candidate_exclusion":
        state.resolve_obligation(
            "court_review_naturalized_candidate_exclusion",
            day,
            "voided the blanket exclusion and restored equal eligibility for the federal office at issue",
        )

    # --- Category G: Federalism ---

    elif event_type == "congress_enacts_commandeering_statute":
        state.provisions.add("Article X Section 1.2")
        message = "Congress enacts a statute requiring state executive officials to implement and enforce a federal regulatory program, in violation of the anti-commandeering provision of Article X Section 1.2."
        state.add_violation(
            "federal_commandeering",
            "federalism_breach",
            "Congress",
            message,
            "Article X Section 1.2",
            day,
            severity="high",
        )
        state.add_obligation(
            "court_review_commandeering",
            "Federal courts",
            "review and void the commandeering statute",
            "Article X Section 1.2",
            day,
            day + 60,
            severity="medium",
        )

    elif event_type == "state_refuses_commandeering":
        state.add_entry(
            day,
            "event",
            f"{actor} refuses to implement the federal program, exercising its constitutional protection against commandeering under Article X Section 1.2.",
            "Article X Section 1.2",
        )

    elif event_type == "court_voids_commandeering_statute":
        state.resolve_obligation(
            "court_review_commandeering",
            day,
            "voided the commandeering statute; the federal government may not conscript state executive officials to implement federal programs",
        )

    # --- Category H: Presidential Accountability ---

    elif event_type == "acc_opens_former_president_investigation":
        state.provisions.update({"Article III Section 15.6", "Article III Section 15.7"})
        state.add_entry(
            day,
            "event",
            f"{actor} opens a criminal investigation of a former President for conduct during their term in office.",
            "Article III Section 15.6 and Section 15.7",
        )

    elif event_type == "former_president_asserts_residual_immunity":
        state.provisions.add("Article III Section 15.6")
        state.add_entry(
            day,
            "event",
            f"{actor} asserts residual post-presidential immunity and moves to dismiss the investigation.",
            "Article III Section 15.6",
        )
        state.add_entry(
            day,
            "outcome",
            "Post-presidential immunity is explicitly abolished by Article III Section 15.6. The immunity claim has no constitutional basis under this Constitution. A court ruling is required to formally reject it.",
            "Article III Section 15.6",
        )
        state.add_obligation(
            "court_rule_on_immunity_claim",
            "Federal courts",
            "rule on the former President's immunity claim",
            "Article III Section 15.6",
            day,
            day + 14,
            severity="medium",
        )

    elif event_type == "court_rejects_immunity_claim":
        state.resolve_obligation(
            "court_rule_on_immunity_claim",
            day,
            "rejected the post-presidential immunity claim; Article III Section 15.6 provides no such immunity and prosecution proceeds",
        )

    # --- Category J: Presidential Succession ---

    elif event_type == "president_incapacitated":
        state.provisions.update({"Article III Section 11", "Article III Section 12"})
        state.add_entry(
            day,
            "event",
            "President becomes incapacitated and unable to discharge presidential duties.",
            "Article III Section 11 and Section 12",
        )
        state.add_obligation(
            "vp_assume_presidential_duties",
            "Vice President",
            "assume the powers and duties of the President as Acting President",
            "Article III Section 11.2 and Section 12.1",
            day,
            day + 1,
            severity="high",
        )

    elif event_type == "vp_also_incapacitated":
        obligation = state.obligations.get("vp_assume_presidential_duties")
        if obligation and obligation.status == "open":
            obligation.status = "satisfied"
            obligation.closed_day = day
            obligation.outcome = "VP is also incapacitated and cannot assume duties; succession advances to Speaker of the House under Article III Section 12.2"
        state.add_entry(
            day,
            "event",
            "Vice President is also incapacitated and unable to assume presidential duties. Succession advances to the Speaker of the House under Article III Section 12.2.",
            "Article III Section 12.2",
        )
        state.add_obligation(
            "speaker_assume_presidential_duties",
            "Speaker of the House",
            "assume the office of Acting President with the limited powers of Article III Section 12.4",
            "Article III Section 12.2",
            day,
            day + 1,
            severity="high",
        )

    elif event_type == "speaker_assumes_acting_presidency":
        state.resolve_obligation(
            "speaker_assume_presidential_duties",
            day,
            "assumed the office of Acting President; Article III Section 12.4 limitations apply — no pardon power, no treaty withdrawal, no emergency declaration, no removal of confirmed officials without cause, no recess appointments without majority approval of both chambers",
        )

    elif event_type == "vp_and_cabinet_declare_presidential_incapacity":
        state.provisions.update({"Article III Section 11.2", "Article III Section 11.3"})
        state.add_entry(
            day,
            "event",
            f"{actor} transmit a written declaration of presidential incapacity under Article III Section 11.2. The Vice President becomes Acting President.",
            "Article III Section 11.2",
        )
        state.add_entry(
            day,
            "outcome",
            "The President may contest this determination within 4 days. If contested, Congress has 21 days from the contest to resolve the question by 2/3 vote. If Congress does not sustain the determination within 21 days, the President resumes the powers of office.",
            "Article III Section 11.3",
        )

    elif event_type == "president_contests_incapacity":
        state.add_entry(
            day,
            "event",
            f"{actor} transmits a written contest of the incapacity determination within the 4-day window. The 21-day congressional resolution period begins.",
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

    elif event_type == "congress_fails_incapacity_determination":
        state.fail_obligation(
            "congress_resolve_incapacity_contest",
            day,
            "Congress failed to sustain the incapacity determination within the 21-day period required by Article III Section 11.3.",
        )
        state.add_entry(
            day,
            "outcome",
            "Under Article III Section 11.3, when Congress does not sustain the incapacity determination within 21 days, the President automatically resumes the powers of office. No further action by any branch is required.",
            "Article III Section 11.3",
        )

    # --- Category K: Rights ---

    elif event_type == "warrantless_surveillance_conducted":
        state.provisions.update({"Article V Section 5.3", "Article XV Section 6.5", "Article XVII Section 4.7"})
        message = "Intelligence agency conducts warrantless surveillance targeting a domestic political organization, in violation of Article V Section 5.3, Article XVII Section 4.7, and the prohibition on using classified appropriations for domestic political surveillance under Article XV Section 6.5."
        state.add_violation(
            "warrantless_domestic_surveillance",
            "rights_suppression",
            "Intelligence agency",
            message,
            "Article V Section 5.3, Article XVII Section 4.7, and Article XV Section 6.5",
            day,
            severity="high",
        )
        state.add_obligation(
            "court_order_surveillance_halt",
            "Federal courts",
            "order an immediate halt to the warrantless domestic surveillance operation",
            "Article V Section 5.3 and Article XVII Section 4.7",
            day,
            day + 5,
            severity="high",
        )

    elif event_type == "court_orders_surveillance_halt":
        state.resolve_obligation(
            "court_order_surveillance_halt",
            day,
            "ordered an immediate halt to the warrantless domestic surveillance and referred the matter to the Accountability Commission",
        )
        state.add_obligation(
            "agency_halt_surveillance",
            "Intelligence agency",
            "cease the warrantless domestic surveillance operation in compliance with the court order",
            "Article V Section 5.3 and Article XVII Section 4.7",
            day,
            day + 2,
            severity="high",
        )

    elif event_type == "agency_complies_with_surveillance_halt":
        state.resolve_obligation(
            "agency_halt_surveillance",
            day,
            "ceased the warrantless domestic surveillance operation in compliance with the court order",
        )

    # --- Category A continued: Executive Order Overreach ---

    elif event_type == "president_issues_overreaching_executive_order":
        state.provisions.update({"Article III Section 6.2", "Article III Section 6.4"})
        message = (
            f"{actor} issues an executive order imposing new regulatory obligations on private businesses "
            "without any statutory authorization, in violation of Article III Section 6.2(a)."
        )
        state.add_violation(
            "executive_order_overreach",
            "executive_defiance",
            actor,
            message,
            "Article III Section 6.2(a)",
            day,
            severity="high",
        )
        state.add_entry(
            day,
            "outcome",
            "The order is presumptively void. Under Article III Section 6.2(a), executive orders may not create legal "
            "obligations on private citizens or entities without prior statutory authorization. Congress may formally "
            "void it by resolution of disapproval within 60 days under Article III Section 6.4.",
            "Article III Section 6.2(a) and Section 6.4",
        )
        state.add_obligation(
            "congress_disapprove_eo",
            "Congress",
            "pass a resolution of disapproval within 60 days to formally void the overreaching executive order",
            "Article III Section 6.4",
            day,
            day + 60,
            severity="medium",
        )

    elif event_type == "congress_disapproves_executive_order":
        state.resolve_obligation(
            "congress_disapprove_eo",
            day,
            "passed a resolution of disapproval; the executive order is void and may not be reissued in substantially the same form without statutory authorization",
        )

    # --- Category B continued: Single-Subject Challenge ---

    elif event_type == "omnibus_bill_passes_both_chambers":
        state.provisions.update({"Article II Section 10.7", "Article II Section 10.7A"})
        message = (
            "Congress passes an omnibus bill bundling unrelated subjects — defense appropriations, immigration rules, "
            "and drug pricing — in a single bill, in violation of the single-subject rule of Article II Section 10.7."
        )
        state.add_violation(
            "single_subject_violation",
            "legislative_deadline_failure",
            "Congress",
            message,
            "Article II Section 10.7",
            day,
            severity="medium",
        )
        state.add_entry(
            day,
            "outcome",
            "The bill is subject to pre-enactment single-subject challenge under Article II Section 10.7A. "
            "The 15-day presidential action clock is tolled pending any such ruling.",
            "Article II Section 10.7A",
        )

    elif event_type == "single_subject_challenge_filed":
        state.provisions.add("Article II Section 10.7A")
        state.add_entry(
            day,
            "event",
            f"{actor} invokes the pre-enactment single-subject challenge mechanism under Article II Section 10.7A.",
            "Article II Section 10.7A",
        )
        state.add_obligation(
            "supreme_court_rule_single_subject",
            "Supreme Court",
            "rule on the single-subject challenge within 15 days",
            "Article II Section 10.7A",
            day,
            day + 15,
            severity="high",
        )

    elif event_type == "supreme_court_voids_omnibus_bill":
        state.resolve_obligation(
            "supreme_court_rule_single_subject",
            day,
            "ruled within the 15-day window, found a single-subject violation, and returned the bill to the originating chamber for severance or redrafting",
        )
        state.add_entry(
            day,
            "outcome",
            "The omnibus bill is voided. The originating chamber must sever the bill into single-subject measures "
            "or redraft before further action. The presidential action clock remains tolled until a valid bill is presented.",
            "Article II Section 10.7A",
        )

    # --- Category B continued: Perjury Before Congress ---

    elif event_type == "official_commits_perjury_before_congress":
        state.provisions.update({"Article II Section 16.4", "Article II Section 16.4(b)"})
        message = (
            f"{actor} gives testimony before a congressional committee containing knowing false statements "
            "of material fact, constituting perjury before Congress under Article II Section 16.4."
        )
        state.add_violation(
            "perjury_before_congress",
            "executive_defiance",
            actor,
            message,
            "Article II Section 16.4",
            day,
            severity="high",
        )
        state.add_entry(
            day,
            "outcome",
            "Congressional perjury is prosecuted exclusively by the Accountability Commission. "
            "The Department of Justice has no jurisdiction over this offense under Article II Section 16.4. "
            "Upon conviction: automatic removal from office, permanent disqualification from federal office, "
            "and no possibility of pardon under Section 16.4(b).",
            "Article II Section 16.4",
        )
        state.add_obligation(
            "committee_refer_perjury",
            "Senate Foreign Relations Committee",
            "refer the perjury matter to the Accountability Commission",
            "Article II Section 16.4",
            day,
            day + 30,
            severity="medium",
        )

    elif event_type == "committee_refers_perjury_to_acc":
        state.resolve_obligation(
            "committee_refer_perjury",
            day,
            "referred the congressional perjury matter to the Accountability Commission for exclusive prosecution",
        )
        state.add_obligation(
            "acc_indict_perjury",
            "Accountability Commission",
            "indict on the congressional perjury charge within the required indictment window",
            "Article II Section 16.4",
            day,
            day + 90,
            severity="high",
        )

    elif event_type == "acc_indicts_for_congressional_perjury":
        state.resolve_obligation(
            "acc_indict_perjury",
            day,
            "indicted the official for congressional perjury within the required window; upon conviction the official faces automatic removal, permanent disqualification, and no possibility of pardon",
        )

    # --- Category D continued: Covert Operation Against Citizen ---

    elif event_type == "covert_operation_ordered_against_us_citizen":
        state.provisions.update({"Article XVI Section 5.2", "Article IV"})
        state.add_entry(
            day,
            "event",
            f"{actor} orders a covert lethal operation targeting a United States citizen abroad. "
            "Under Article XVI Section 5.2, a judicial warrant issued upon probable cause is required before any such operation may proceed.",
            "Article XVI Section 5.2",
        )
        state.add_obligation(
            "court_issue_citizen_warrant",
            "Federal courts",
            "adjudicate the warrant application, finding probable cause of imminent specific threat and that capture is not feasible",
            "Article XVI Section 5.2",
            day,
            day + 3,
            severity="high",
        )

    elif event_type == "court_denies_warrant_capture_feasible":
        state.resolve_obligation(
            "court_issue_citizen_warrant",
            day,
            "denied the warrant application, finding that capture remains feasible; the operation is constitutionally blocked pending a valid warrant",
        )
        state.add_entry(
            day,
            "outcome",
            "Without a judicial warrant under Article XVI Section 5.2, no lethal covert operation against a US citizen may lawfully proceed.",
            "Article XVI Section 5.2",
        )

    elif event_type == "operation_proceeds_despite_warrant_denial":
        state.provisions.add("Article XVI Section 5.2")
        message = (
            f"{actor} proceeds with a covert lethal operation against a US citizen after a court denied the required "
            "warrant, in direct violation of Article XVI Section 5.2."
        )
        state.add_violation(
            "unlawful_covert_operation_us_citizen",
            "executive_defiance",
            actor,
            message,
            "Article XVI Section 5.2",
            day,
            severity="high",
        )
        state.add_obligation(
            "acc_prosecute_covert_operation",
            "Accountability Commission",
            "open prosecution of responsible officers for the unlawful covert lethal operation against a US citizen",
            "Article XVI Section 5.2 and Article III Section 15.7",
            day,
            day + 30,
            severity="high",
        )

    elif event_type == "acc_opens_prosecution_for_unlawful_operation":
        state.resolve_obligation(
            "acc_prosecute_covert_operation",
            day,
            "opened prosecution of the responsible officers for conducting a covert lethal operation against a US citizen in violation of the judicial warrant requirement",
        )

    # --- Category D continued: PMC Substitution ---

    elif event_type == "congress_denies_force_authorization":
        state.provisions.update({"Article XVI Section 1", "Article XVI Section 4.4"})
        state.add_entry(
            day,
            "event",
            f"{actor} explicitly denies an Authorization for Use of Military Force. No armed operations may proceed under the denied authorization.",
            "Article XVI Section 1 and Section 4.4",
        )

    elif event_type == "president_deploys_pmcs_as_aumf_substitute":
        state.provisions.add("Article XVI Section 4.4")
        message = (
            f"{actor} deploys private military contractors in a combat role to conduct the operation Congress denied, "
            "in direct violation of Article XVI Section 4.4, which prohibits using PMCs to avoid authorization "
            "requirements or to conceal the scale of US military engagement."
        )
        state.add_violation(
            "pmc_substitution_for_aumf",
            "executive_defiance",
            actor,
            message,
            "Article XVI Section 4.4",
            day,
            severity="high",
        )
        state.add_entry(
            day,
            "outcome",
            "The PMC deployment triggers the expedited impeachment timetable of Article III Section 10.2A. "
            "The House must hold a recorded impeachment vote within 21 days.",
            "Article III Section 10.2A",
        )
        state.add_obligation(
            "house_vote_impeachment_pmc",
            "House of Representatives",
            "hold a recorded impeachment vote on the unlawful PMC deployment used to circumvent the denied AUMF",
            "Article III Section 10.2A and Article XVI Section 4.4",
            day,
            day + 21,
            severity="high",
        )

    elif event_type == "house_misses_pmc_impeachment_vote":
        state.fail_obligation(
            "house_vote_impeachment_pmc",
            day,
            "House of Representatives failed to hold the required impeachment vote on the PMC substitution violation by the required deadline under Article III Section 10.2A.",
        )

    elif event_type == "regional_assembly_begins_pmc_trial":
        state.resolve_obligation(
            "regional_assembly_trial_pmc",
            day,
            "began impeachment trial on the automatically transmitted PMC substitution articles",
        )

    else:
        state.add_entry(day, "note", f"Unhandled event type: {event_type} (actor: {actor})")


def run_scenario(path: Path) -> SimulationState:
    data = load_scenario(path)
    state = SimulationState(title=data["title"])
    state.add_entry(0, "scenario", data["description"])

    events = sorted(data["events"], key=lambda item: int(item["day"]))
    current_day = 0

    for event in events:
        event_day = int(event["day"])
        if event_day < current_day:
            raise ValueError(f"Scenario {path.name} has out-of-order events.")
        state.check_due_obligations(event_day)
        current_day = event_day
        handle_event(state, event)

    state.check_due_obligations(current_day + 365)
    return state


def print_report(path: Path, state: SimulationState) -> None:
    print(f"# {state.title}")
    print(f"Scenario: {path.name}")
    print()
    print("## Timeline")
    for entry in sorted(state.timeline, key=lambda item: (item.day, item.kind, item.message)):
        source = f" [{entry.source}]" if entry.source else ""
        print(f"- Day {entry.day}: {entry.kind.upper()} - {entry.message}{source}")
    print()

    if state.provisions:
        print("## Triggered Provisions")
        for provision in sorted(state.provisions):
            print(f"- {provision}")
        print()

    open_obligations = [o for o in state.obligations.values() if o.status == "open"]
    if open_obligations:
        print("## Unresolved Obligations")
        for obligation in sorted(open_obligations, key=lambda item: (item.due_day is None, item.due_day or 10**9, item.actor)):
            due_text = f"day {obligation.due_day}" if obligation.due_day is not None else "no fixed constitutional deadline"
            print(f"- {obligation.actor}: {obligation.duty} ({due_text}; {obligation.source})")
        print()

    if state.violations:
        print("## Violations")
        for violation in state.violations:
            print(f"- {violation.summary}")
        print()

    if state.bottlenecks:
        print("## Bottlenecks")
        for bottleneck in state.bottlenecks:
            print(f"- {bottleneck.summary}")
        print()

    if state.notes:
        print("## Notes")
        for note in state.notes:
            print(f"- {note}")
        print()

    if state.bottlenecks or state.violations or open_obligations:
        print("## Assessment")
        print("- The scenario exposes at least one live bottleneck, unresolved duty, or constitutional violation.")
    else:
        print("## Assessment")
        print("- The scenario resolves cleanly under the currently modeled rules.")
    print()


def print_summary(path: Path, state: SimulationState) -> None:
    open_obligations = [o for o in state.obligations.values() if o.status == "open"]
    resolved_count = sum(1 for o in state.obligations.values() if o.status == "satisfied")
    failed_count = sum(1 for o in state.obligations.values() if o.status == "failed")

    print(f"# {state.title}")
    print(f"Scenario: {path.name}")
    print()
    print("## Condensed View")
    print(f"- Triggered provisions: {len(state.provisions)}")
    print(f"- Satisfied obligations: {resolved_count}")
    print(f"- Failed obligations: {failed_count}")
    print(f"- Unresolved obligations: {len(open_obligations)}")
    print(f"- Violations: {len(state.violations)}")
    print(f"- Bottlenecks: {len(state.bottlenecks)}")
    print()

    if state.violations:
        print("## Key Violations")
        for violation in state.violations:
            print(f"- {violation.summary}")
        print()

    if state.bottlenecks:
        print("## Key Bottlenecks")
        for bottleneck in state.bottlenecks:
            print(f"- {bottleneck.summary}")
        print()

    if open_obligations:
        print("## Open Duties")
        for obligation in sorted(open_obligations, key=lambda item: (item.due_day is None, item.due_day or 10**9, item.actor)):
            due_text = f"day {obligation.due_day}" if obligation.due_day is not None else "no fixed deadline"
            print(f"- {obligation.actor}: {obligation.duty} ({due_text})")
        print()

    if state.notes:
        print("## Review Notes")
        for note in state.notes:
            print(f"- {note}")
        print()

    if state.bottlenecks or state.violations or open_obligations:
        print("## Bottom Line")
        print("- This scenario still exposes at least one meaningful system stress point.")
    else:
        print("## Bottom Line")
        print("- This scenario resolves cleanly under the current rules model.")
    print()


def render_with_capture(renderer: Any, path: Path, state: SimulationState) -> str:
    import contextlib

    buffer = io.StringIO()
    with contextlib.redirect_stdout(buffer):
        renderer(path, state)
    return buffer.getvalue()


def scenario_slug(path: Path, state: SimulationState) -> str:
    return path.stem


def build_summary_json(path: Path, state: SimulationState) -> dict[str, Any]:
    open_obligations = [o for o in state.obligations.values() if o.status == "open"]
    satisfied_obligations = [o for o in state.obligations.values() if o.status == "satisfied"]
    failed_obligations = [o for o in state.obligations.values() if o.status == "failed"]
    status = "clean"
    if state.violations or state.bottlenecks or open_obligations:
        status = "stress_point_found"

    summary_data = {
        "scenario_id": scenario_slug(path, state),
        "title": state.title,
        "source_file": str(path.relative_to(ROOT.parent)),
        "status": status,
        "triggered_provisions": sorted(state.provisions),
        "metrics": {
            "satisfied_obligations": len(satisfied_obligations),
            "failed_obligations": len(failed_obligations),
            "unresolved_obligations": len(open_obligations),
            "violations": len(state.violations),
            "bottlenecks": len(state.bottlenecks),
            "timeline_entries": len(state.timeline),
        },
        "violations": [
            {
                "id": violation.id or f"violation_{index + 1}",
                "category": violation.category,
                "actor": violation.actor,
                "source": violation.source,
                "severity": violation.severity,
                "day": violation.day,
                "summary": violation.summary,
            }
            for index, violation in enumerate(state.violations)
        ],
        "bottlenecks": [
            {
                "id": bottleneck.id or f"bottleneck_{index + 1}",
                "category": bottleneck.category,
                "actor": bottleneck.actor,
                "source": bottleneck.source,
                "severity": bottleneck.severity,
                "day": bottleneck.day,
                "deadline_day": bottleneck.deadline_day,
                "summary": bottleneck.summary,
            }
            for index, bottleneck in enumerate(state.bottlenecks)
        ],
        "open_duties": [
            {
                "actor": obligation.actor,
                "duty": obligation.duty,
                "deadline_day": obligation.due_day,
                "source": obligation.source,
                "severity": obligation.severity,
            }
            for obligation in sorted(
                open_obligations,
                key=lambda item: (item.due_day is None, item.due_day or 10**9, item.actor),
            )
        ],
        "satisfied_duties": [
            {
                "actor": obligation.actor,
                "duty": obligation.duty,
                "closed_day": obligation.closed_day,
                "outcome": obligation.outcome,
                "source": obligation.source,
            }
            for obligation in sorted(satisfied_obligations, key=lambda item: (item.closed_day or 10**9, item.actor))
        ],
        "failed_duties": [
            {
                "actor": obligation.actor,
                "duty": obligation.duty,
                "deadline_day": obligation.due_day,
                "closed_day": obligation.closed_day,
                "outcome": obligation.outcome,
                "source": obligation.source,
                "severity": obligation.severity,
            }
            for obligation in sorted(
                failed_obligations,
                key=lambda item: (item.deadline_day if hasattr(item, "deadline_day") else item.due_day or 10**9, item.actor),
            )
        ],
        "notes": list(state.notes),
        "ai_summary": {
            "primary_violation": state.violations[0].summary if state.violations else None,
            "primary_bottleneck": state.bottlenecks[0].summary if state.bottlenecks else None,
            "primary_open_duty": open_obligations[0].duty if open_obligations else None,
            "system_risk": "none",
            "recommended_focus": (
                "review bottlenecks, violations, and unresolved duties"
                if status != "clean"
                else "no immediate constitutional flow issue detected in this scenario"
            ),
        },
    }
    summary_data["ai_summary"]["system_risk"] = derive_system_risk(summary_data)
    return summary_data


def build_aggregate_json(results: list[tuple[Path, SimulationState]]) -> dict[str, Any]:
    scenario_summaries = [build_summary_json(path, state) for path, state in results]
    provision_counts: dict[str, int] = {}
    unresolved_by_actor: dict[str, int] = {}
    risk_counts: dict[str, int] = {}
    bottleneck_categories: dict[str, int] = {}
    violation_categories: dict[str, int] = {}

    for summary in scenario_summaries:
        for provision in summary["triggered_provisions"]:
            provision_counts[provision] = provision_counts.get(provision, 0) + 1
        for duty in summary["open_duties"]:
            actor = duty["actor"]
            unresolved_by_actor[actor] = unresolved_by_actor.get(actor, 0) + 1
        risk = summary["ai_summary"]["system_risk"]
        risk_counts[risk] = risk_counts.get(risk, 0) + 1
        for issue in summary["bottlenecks"]:
            category = issue["category"]
            bottleneck_categories[category] = bottleneck_categories.get(category, 0) + 1
        for issue in summary["violations"]:
            category = issue["category"]
            violation_categories[category] = violation_categories.get(category, 0) + 1

    return {
        "scenario_count": len(scenario_summaries),
        "stress_point_scenarios": sum(1 for summary in scenario_summaries if summary["status"] != "clean"),
        "totals": {
            "violations": sum(summary["metrics"]["violations"] for summary in scenario_summaries),
            "bottlenecks": sum(summary["metrics"]["bottlenecks"] for summary in scenario_summaries),
            "unresolved_obligations": sum(summary["metrics"]["unresolved_obligations"] for summary in scenario_summaries),
        },
        "risk_pattern_counts": [
            {"risk": risk, "count": count}
            for risk, count in sorted(risk_counts.items(), key=lambda item: (-item[1], item[0]))
        ],
        "bottleneck_categories": [
            {"category": category, "count": count}
            for category, count in sorted(bottleneck_categories.items(), key=lambda item: (-item[1], item[0]))
        ],
        "violation_categories": [
            {"category": category, "count": count}
            for category, count in sorted(violation_categories.items(), key=lambda item: (-item[1], item[0]))
        ],
        "top_triggered_provisions": [
            {"provision": provision, "count": count}
            for provision, count in sorted(provision_counts.items(), key=lambda item: (-item[1], item[0]))
        ],
        "open_duties_by_actor": [
            {"actor": actor, "count": count}
            for actor, count in sorted(unresolved_by_actor.items(), key=lambda item: (-item[1], item[0]))
        ],
        "scenarios": scenario_summaries,
    }


def ensure_output_dir(path: str | None) -> Path | None:
    if not path:
        return None
    out_dir = Path(path)
    out_dir.mkdir(parents=True, exist_ok=True)
    return out_dir


def write_outputs(
    out_dir: Path | None,
    path: Path,
    state: SimulationState,
    save_full: bool,
    save_json: bool,
) -> None:
    if out_dir is None:
        return
    slug = scenario_slug(path, state)
    if save_full:
        full_text = render_with_capture(print_report, path, state)
        (out_dir / f"{slug}.full.md").write_text(full_text)
    if save_json:
        summary_data = build_summary_json(path, state)
        (out_dir / f"{slug}.summary.json").write_text(json.dumps(summary_data, indent=2) + "\n")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run constitution flow simulations.")
    parser.add_argument("scenario", nargs="?", help="Path to a scenario JSON file")
    parser.add_argument("--all", action="store_true", help="Run all bundled scenarios")
    parser.add_argument("--list", action="store_true", help="List bundled scenarios")
    parser.add_argument("--summary", action="store_true", help="Print condensed summary output")
    parser.add_argument("--both", action="store_true", help="Print both condensed and full output")
    parser.add_argument("--out-dir", help="Directory to write report files")
    parser.add_argument("--save-full", action="store_true", help="Write full Markdown reports")
    parser.add_argument("--save-json", action="store_true", help="Write condensed JSON summaries for AI use")
    parser.add_argument("--save-aggregate", action="store_true", help="Write aggregate JSON when running multiple scenarios")
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    if args.list:
        for path in scenario_paths():
            data = load_scenario(path)
            print(f"{path.name}: {data['title']}")
        return 0

    if args.all:
        targets = scenario_paths()
    elif args.scenario:
        targets = [Path(args.scenario)]
    else:
        print("Provide a scenario path, or use --list or --all.")
        return 1

    out_dir = ensure_output_dir(args.out_dir)
    results: list[tuple[Path, SimulationState]] = []

    for index, path in enumerate(targets):
        state = run_scenario(path)
        results.append((path, state))
        if args.both:
            print_summary(path, state)
            print("## Full Report")
            print()
            print_report(path, state)
        elif args.summary:
            print_summary(path, state)
        else:
            print_report(path, state)
        write_outputs(out_dir, path, state, save_full=args.save_full, save_json=args.save_json)
        if index != len(targets) - 1:
            print("=" * 80)

    if args.save_aggregate and out_dir is not None and len(results) > 1:
        aggregate = build_aggregate_json(results)
        (out_dir / "aggregate.json").write_text(json.dumps(aggregate, indent=2) + "\n")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
