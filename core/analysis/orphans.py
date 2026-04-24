"""
core/analysis/orphans.py
==========================
Tool: deterministic detection of orphan requirements and objectives.

An *orphan requirement* is an IRQ or NFR that is not associated with any
objective (OBJ-X).  An *orphan objective* is an OBJ that has no
requirements associated with it.

This module is **purely deterministic** – no LLM call is performed.  It
parses the structured Markdown produced by the extraction tools and
computes the orphan sets.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import Dict, List, Set, Tuple


# ---------------------------------------------------------------------------
# ID normalisation helpers
# ---------------------------------------------------------------------------

_OBJ_ID = re.compile(r"\b(OBJ-\d+(?:\.\d+)*)\b", re.IGNORECASE)
_IRQ_ID = re.compile(r"\b(IRQ-\d+)\b", re.IGNORECASE)
_NFR_ID = re.compile(r"\b(NFR-\d+)\b", re.IGNORECASE)

# Matches lines like:  - **Objetivos asociados:** OBJ-1, OBJ-2
_OBJ_ASSOC_LINE = re.compile(
    r"(?:Objetivos?\s+asociados?):\s*(.+)", re.IGNORECASE
)

# Matches a requirement header: ### IRQ-3: ... or ### NFR-1: ...
_REQ_HEADER = re.compile(r"^###\s+((?:IRQ|NFR)-\d+)", re.IGNORECASE | re.MULTILINE)


def _extract_ids(pattern: re.Pattern, text: str) -> Set[str]:
    return {m.group(1).upper() for m in pattern.finditer(text)}


def _parse_req_associations(requirements_md: str) -> Dict[str, List[str]]:
    """Return a mapping of each requirement ID → list of associated OBJ IDs.

    Parses lines like::

        - **Objetivos asociados:** OBJ-1, OBJ-2

    within each requirement block in *requirements_md*.
    """
    associations: Dict[str, List[str]] = {}

    # Split on requirement headers
    parts = _REQ_HEADER.split(requirements_md)
    # parts[0] = preamble, then alternating: req_id, block_text, req_id, block_text…
    i = 1
    while i < len(parts) - 1:
        req_id = parts[i].upper()
        block = parts[i + 1]
        assoc_match = _OBJ_ASSOC_LINE.search(block)
        if assoc_match:
            raw = assoc_match.group(1)
            objs = [o.strip().upper() for o in _OBJ_ID.findall(raw)]
            associations[req_id] = objs
        else:
            associations[req_id] = []
        i += 2

    return associations


# ---------------------------------------------------------------------------
# Public data classes
# ---------------------------------------------------------------------------

@dataclass
class OrphanReport:
    """Result of :func:`detect_orphans`.

    Attributes
    ----------
    orphan_requirements:
        IDs of IRQ/NFR items that have no associated objective.
    orphan_objectives:
        IDs of OBJ items that have no requirements associated with them.
    objective_ids:
        All objective IDs found in *objectives_md*.
    requirement_ids:
        All requirement IDs (IRQ + NFR) found in *requirements_md*.
    req_to_objs:
        Mapping of each requirement → list of associated objectives.
    obj_to_reqs:
        Mapping of each objective → list of associated requirements.
    """
    orphan_requirements: List[str] = field(default_factory=list)
    orphan_objectives: List[str] = field(default_factory=list)
    objective_ids: List[str] = field(default_factory=list)
    requirement_ids: List[str] = field(default_factory=list)
    req_to_objs: Dict[str, List[str]] = field(default_factory=dict)
    obj_to_reqs: Dict[str, List[str]] = field(default_factory=dict)

    def as_markdown(self) -> str:
        """Render the report as a Markdown string."""
        lines = ["# Orphan Detection Report\n"]

        lines.append(f"\n## Summary\n")
        lines.append(f"- **Total objectives:** {len(self.objective_ids)}\n")
        lines.append(f"- **Total requirements:** {len(self.requirement_ids)}\n")
        lines.append(f"- **Orphan requirements (no objective):** {len(self.orphan_requirements)}\n")
        lines.append(f"- **Orphan objectives (no requirements):** {len(self.orphan_objectives)}\n")

        if self.orphan_requirements:
            lines.append("\n## Orphan Requirements (not linked to any objective)\n")
            for rid in sorted(self.orphan_requirements):
                lines.append(f"- **{rid}**: no `OBJ-X` association found\n")
        else:
            lines.append("\n## Orphan Requirements\n\n✅ None found – all requirements link to at least one objective.\n")

        if self.orphan_objectives:
            lines.append("\n## Orphan Objectives (no requirements cover them)\n")
            for oid in sorted(self.orphan_objectives):
                lines.append(f"- **{oid}**: no IRQ or NFR is associated with this objective\n")
        else:
            lines.append("\n## Orphan Objectives\n\n✅ None found – all objectives are covered by at least one requirement.\n")

        lines.append("\n## Objective Coverage\n")
        for oid in sorted(self.objective_ids):
            reqs = self.obj_to_reqs.get(oid, [])
            status = "✅" if reqs else "❌"
            req_list = ", ".join(sorted(reqs)) if reqs else "–"
            lines.append(f"- {status} **{oid}**: {req_list}\n")

        return "".join(lines)


# ---------------------------------------------------------------------------
# Main public function
# ---------------------------------------------------------------------------

def detect_orphans(
    objectives_md: str,
    requirements_md: str,
) -> OrphanReport:
    """Detect orphan requirements and objectives deterministically.

    Parameters
    ----------
    objectives_md:
        Structured objectives produced by ``core/extraction/objectives.py``.
    requirements_md:
        Structured requirements produced by ``core/extraction/requirements.py``.

    Returns
    -------
    OrphanReport
        Dataclass with lists of orphan IDs plus full coverage mappings.
    """
    # Collect all objective IDs declared in the objectives block
    obj_ids: Set[str] = _extract_ids(_OBJ_ID, objectives_md)

    # Parse requirement→objective associations from the requirements block
    req_to_objs = _parse_req_associations(requirements_md)

    # Also catch any requirement IDs that might not appear in a proper block
    all_irqs = _extract_ids(_IRQ_ID, requirements_md)
    all_nfrs = _extract_ids(_NFR_ID, requirements_md)
    all_req_ids = all_irqs | all_nfrs
    for rid in all_req_ids:
        if rid not in req_to_objs:
            req_to_objs[rid] = []

    # Orphan requirements: those with empty (or absent) objective list
    orphan_reqs = sorted(rid for rid, objs in req_to_objs.items() if not objs)

    # Build reverse mapping: objective → requirements that reference it
    obj_to_reqs: Dict[str, List[str]] = {oid: [] for oid in obj_ids}
    for rid, objs in req_to_objs.items():
        for oid in objs:
            if oid in obj_to_reqs:
                obj_to_reqs[oid].append(rid)
            else:
                # Objective referenced by a requirement but not declared
                obj_to_reqs[oid] = [rid]
                obj_ids.add(oid)

    # Orphan objectives: those with no requirements referencing them
    orphan_objs = sorted(oid for oid, reqs in obj_to_reqs.items() if not reqs)

    return OrphanReport(
        orphan_requirements=orphan_reqs,
        orphan_objectives=orphan_objs,
        objective_ids=sorted(obj_ids),
        requirement_ids=sorted(all_req_ids),
        req_to_objs=req_to_objs,
        obj_to_reqs=obj_to_reqs,
    )
