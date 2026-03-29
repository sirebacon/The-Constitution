from __future__ import annotations

import io
import json
from pathlib import Path
from typing import Any

from sim_core import ROOT, SimulationState, derive_system_risk


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
