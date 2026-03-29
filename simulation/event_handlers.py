from __future__ import annotations

from typing import Any

from sim_core import SimulationState
from handlers import HANDLERS


def handle_event(state: SimulationState, event: dict[str, Any]) -> None:
    event_type = event["type"]
    handler = HANDLERS.get(event_type)
    if handler is None:
        day = int(event["day"])
        actor = event.get("actor", "Unknown actor")
        state.add_entry(day, "note", f"Unhandled event type: {event_type} (actor: {actor})")
        return
    handler(state, event)
