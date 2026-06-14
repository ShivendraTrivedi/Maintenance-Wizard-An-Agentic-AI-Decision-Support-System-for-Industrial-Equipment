#!/usr/bin/env python3
"""
Sample Input / Output demonstration (no UI required).

Runs the full agentic pipeline on three representative scenarios and prints
the structured, cited outputs. Useful for judges and for the screen recording.

Usage:  python3 scripts/demo.py
"""
import os
import sys
import json
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.agents import orchestrator  # noqa: E402


def ts():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def show(title, query, **kw):
    print("\n" + "=" * 78)
    print(title)
    print("=" * 78)
    print(f"INPUT  : {query}")
    if kw.get("role"):
        print(f"ROLE   : {kw['role']}")
    b = orchestrator.run(query, ts(), **kw)
    print(f"\nRESOLVED ASSET : {b.get('asset_id')}")
    print(f"DETECTED INTENTS: {b.get('intents')}")
    print("\nOUTPUT :\n")
    print(b["answer"])
    if b.get("citations"):
        print("\nEXPLAINABILITY — sources used:")
        for c in b["citations"]:
            print(f"  • [{c['doc_type']}] {c.get('asset_id')} — {c['source']}")
    if b.get("risk_priority"):
        rp = b["risk_priority"]
        print(f"\nPRIORITY: {rp['priority_band']} ({rp['urgency']}) score={rp['priority_score']} | {rp['rationale']}")


def main():
    show("SCENARIO 1 — Reactive troubleshooting (degraded asset)",
         "HSM-M-02 has high vibration and the bearing is running hot. "
         "Diagnose, find the root cause, assess the risk and tell me what to do.",
         role="engineer")

    show("SCENARIO 2 — Predictive / RUL question",
         "CCM-OSC-02 oscillation frequency looks unstable and it has caused production delays. "
         "What is the remaining useful life and how urgent is it?",
         role="engineer")

    show("SCENARIO 3 — Plant-level prioritisation (supervisor)",
         "Which equipment across the plant should we prioritise this week? Show the bottlenecks.",
         role="supervisor")

    print("\n" + "=" * 78)
    print("Demo complete. A digital logbook entry was written for each interaction:")
    print("  data/logbook/logbook.jsonl")
    print("=" * 78)


if __name__ == "__main__":
    main()
