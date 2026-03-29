from __future__ import annotations

from .executive import HANDLERS as EXECUTIVE_HANDLERS
from .federalism import HANDLERS as FEDERALISM_HANDLERS
from .war_powers import HANDLERS as WAR_POWERS_HANDLERS
from .elections import HANDLERS as ELECTIONS_HANDLERS
from .legislative import HANDLERS as LEGISLATIVE_HANDLERS
from .judiciary import HANDLERS as JUDICIARY_HANDLERS
from .transition import HANDLERS as TRANSITION_HANDLERS
from .rights import HANDLERS as RIGHTS_HANDLERS
from .integrity import HANDLERS as INTEGRITY_HANDLERS

HANDLERS = {}
for registry in [EXECUTIVE_HANDLERS, FEDERALISM_HANDLERS, WAR_POWERS_HANDLERS, ELECTIONS_HANDLERS, LEGISLATIVE_HANDLERS, JUDICIARY_HANDLERS, TRANSITION_HANDLERS, RIGHTS_HANDLERS, INTEGRITY_HANDLERS]:
    overlap = set(HANDLERS) & set(registry)
    if overlap:
        raise RuntimeError(f"Duplicate event handlers registered: {sorted(overlap)}")
    HANDLERS.update(registry)
