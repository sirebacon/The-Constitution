#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

from event_handlers import handle_event
from sim_core import SimulationState, load_scenario, scenario_paths
from sim_reporting import (
    build_aggregate_json,
    ensure_output_dir,
    print_report,
    print_summary,
    write_outputs,
)


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
