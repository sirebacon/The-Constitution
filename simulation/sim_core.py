from __future__ import annotations

import json
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


def categorize_failed_obligation(obligation: Obligation) -> str:
    if obligation.source.startswith("Article X Section 1.6"):
        return "state_backsliding"
    legislative_actors = {
        "Congress",
        "House of Representatives",
        "Regional Assembly",
        "Speaker of the House",
        "Regional Assembly presiding officer",
        "Congress and appointing authorities",
    }
    if obligation.actor in legislative_actors:
        return "legislative_deadline_failure"
    executive_markers = (
        "President",
        "Secretary",
        "Executive",
        "agency",
        "Marshal",
    )
    if any(marker in obligation.actor for marker in executive_markers):
        return "executive_defiance"
    if obligation.actor in {"Federal courts", "Chief Justice", "Supreme Court", "U.S. District Court for D.C."}:
        return "judicial_delay"
    if obligation.actor in {"Accountability Commission", "Electoral Commission"}:
        return "institutional_deadline_failure"
    return "missed_deadline"


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


def scenario_paths() -> list[Path]:
    return sorted(SCENARIOS_DIR.glob("*.json"))


def load_scenario(path: Path) -> dict[str, Any]:
    with path.open() as f:
        return json.load(f)
