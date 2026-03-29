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
    if obligation.source.startswith("Article VII Section 1.6"):
        return "state_backsliding"
    if obligation.actor in {"Congress", "House of Representatives", "Regional Assembly"}:
        return "legislative_deadline_failure"
    if obligation.actor in {"Federal courts", "Chief Justice", "Supreme Court"}:
        return "judicial_delay"
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
        state.provisions.update({"Article VII Section 1.5", "Article VII Section 1.6"})
        state.add_entry(day, "event", "Supreme Court finds persistent and material violation of the democratic floor.", "Article VII Section 1.6(a)")
        state.add_obligation(
            "congress_state_remedy",
            "Congress",
            "enact a remedial measure for the violating state",
            "Article VII Section 1.6(b)",
            day,
            day + 180,
            severity="high",
        )

    elif event_type == "congress_fails_state_remedy":
        state.add_entry(day, "event", "Congress fails to enact a timely remedy for the state democratic-floor violation.", "Article VII Section 1.6(b)")
        state.fail_obligation(
            "congress_state_remedy",
            day,
            "Congress failed to enact a remedial measure for the violating state by day 180 under Article VII Section 1.6(b).",
        )
        state.add_obligation(
            "congress_vote_suspend_representation",
            "Congress",
            "hold a recorded vote on suspension of the state's representation",
            "Article VII Section 1.6(c)",
            day,
            day + 30,
            severity="high",
        )

    elif event_type == "state_violation_persists_one_year":
        state.add_entry(day, "event", "The state remains in material violation one year after the Supreme Court finding.", "Article VII Section 1.6(d)")
        vote_obligation = state.obligations.get("congress_vote_suspend_representation")
        if not vote_obligation or vote_obligation.status != "satisfied":
            state.add_entry(
                day,
                "outcome",
                "The state's representation is suspended automatically until the Supreme Court certifies compliance.",
                "Article VII Section 1.6(d)",
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
        state.provisions.update({"Article XI Section 1", "Article III Section 10"})
        state.add_entry(day, "event", f"{actor} initiates military action without prior authorization.", "Article XI Section 1")
        state.add_obligation(
            "congress_authorize_force",
            "Congress",
            "grant authorization for continued military force or refuse it",
            "Article XI Section 1",
            day,
            day + 30,
            severity="high",
        )

    elif event_type == "congress_fails_aumf":
        state.add_entry(day, "event", "Congress does not provide timely authorization for the military action.", "Article XI Section 1")
        state.fail_obligation(
            "congress_authorize_force",
            day,
            "Congress failed to grant authorization for continued military force or refuse it by day 30 under Article XI Section 1.",
        )
        state.add_obligation(
            "chief_justice_withdrawal_order",
            "Chief Justice",
            "issue the required withdrawal order for unauthorized continued operations",
            "Article XI Section 1.5(c)",
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
            "Article XI Section 8(e)",
            day,
        )
        state.add_obligation(
            "house_vote_impeachment_war",
            "House of Representatives",
            "hold a recorded impeachment vote on the unlawful continued military operation",
            "Article XI Section 1.5(e) and Article III Section 10.2A",
            day,
            day + 21,
            severity="high",
        )

    elif event_type == "president_declares_domestic_insurrection":
        state.provisions.update({"Article XI Section 7", "Article XI Section 8", "Article V Section 1"})
        state.add_entry(day, "event", f"{actor} declares an insurrection and orders domestic military deployment.", "Article XI Section 7")
        state.add_obligation(
            "court_review_domestic_deployment",
            "Federal courts",
            "review the constitutional basis for the domestic deployment",
            "Article XI Section 7 and Section 8",
            day,
            day + 3,
            severity="high",
        )
        state.add_obligation(
            "service_members_assess_order",
            "Service members",
            "refuse compliance with an unconstitutional domestic deployment order",
            "Article XI Section 8",
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
            "Article XI Section 7 and Article V Section 1",
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
                "Article VII federalism provisions",
                "Article XI war powers",
                "Article XIV foreign policy and national security",
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
            "confine immediate response measures to non-military Article XIV authorities unless Article XI is lawfully triggered",
            "Article XI war powers and Article XIV foreign policy and national security",
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
            "Article I election administration provisions and Article VII federalism provisions",
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
            "used attribution, sanctions, and other non-military countermeasures under Article XIV",
        )

    elif event_type == "courts_block_speech_restriction":
        state.resolve_obligation(
            "federal_courts_protect_speech",
            day,
            "blocked direct suppression of protected expression while allowing disclosure-based responses",
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
