#!/usr/bin/env python3
"""
Generate a large, realistic synthetic document corpus for the Maintenance Wizard.

Outputs (under data/):
  documents/manuals/*.md          - one equipment manual per asset
  documents/sops/*.md             - standard operating procedures
  documents/failure_reports/*.md  - historical failure analysis reports
  documents/maintenance_logs/*.md - narrative maintenance log records
  spares/spares_catalogue.csv     - spare parts: stock + procurement lead time
  sensors/<asset_id>.csv          - sensor time-series with injected anomalies
  manifest.json                   - index of everything generated

Deterministic (seeded) so the corpus is reproducible.
"""
import os
import csv
import json
import math
import random
from datetime import datetime, timedelta

random.seed(42)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data")
D_MAN = os.path.join(DATA, "documents", "manuals")
D_SOP = os.path.join(DATA, "documents", "sops")
D_FR = os.path.join(DATA, "documents", "failure_reports")
D_ML = os.path.join(DATA, "documents", "maintenance_logs")
D_DL = os.path.join(DATA, "documents", "delay_logs")
D_SP = os.path.join(DATA, "spares")
D_SE = os.path.join(DATA, "sensors")
D_DELAY = os.path.join(DATA, "delays")
for d in (D_MAN, D_SOP, D_FR, D_ML, D_DL, D_SP, D_SE, D_DELAY):
    os.makedirs(d, exist_ok=True)

# --------------------------------------------------------------------------
# Equipment-type knowledge base (realistic steel-plant assets)
# Each type defines: sensors (name, unit, normal range), common fault modes,
# typical root causes, and characteristic spare parts.
# --------------------------------------------------------------------------
# Equipment knowledge base lives in the runtime package (single source of truth).
import sys as _sys
_sys.path.insert(0, ROOT)
from src.core.equipment_kb import EQUIP_TYPES

ROMAN = ["A", "B", "C", "D", "E", "F", "G", "H"]


def make_assets():
    """Create concrete asset instances of each type."""
    assets = []
    counts = {  # how many instances of each type
        "Blast Furnace Stove": 4,
        "Hot Strip Mill Main Drive Motor": 6,
        "Continuous Casting Mould Oscillator": 5,
        "Coke Oven Pushing Ram": 3,
        "Sinter Plant ID Fan": 4,
        "BOF Lance Hoist": 3,
        "Reheating Furnace Walking Beam Drive": 4,
        "Cooling Water Pump": 8,
    }
    prefix = {
        "Blast Furnace Stove": "BFS",
        "Hot Strip Mill Main Drive Motor": "HSM-M",
        "Continuous Casting Mould Oscillator": "CCM-OSC",
        "Coke Oven Pushing Ram": "COR",
        "Sinter Plant ID Fan": "SP-IDF",
        "BOF Lance Hoist": "BOF-LH",
        "Reheating Furnace Walking Beam Drive": "RHF-WBD",
        "Cooling Water Pump": "CWP",
    }
    for etype, n in counts.items():
        for i in range(1, n + 1):
            aid = f"{prefix[etype]}-{i:02d}"
            assets.append({
                "asset_id": aid,
                "type": etype,
                "area": EQUIP_TYPES[etype]["area"],
                "criticality": EQUIP_TYPES[etype]["criticality"],
                "install_year": random.choice([2009, 2011, 2013, 2015, 2017, 2019]),
                "manufacturer": random.choice(["Siemens", "ABB", "Danieli", "SMS Group", "Primetals", "TMEIC"]),
            })
    return assets


def manual_md(asset):
    t = EQUIP_TYPES[asset["type"]]
    lines = []
    lines.append(f"# Equipment Manual — {asset['type']} ({asset['asset_id']})")
    lines.append("")
    lines.append(f"**Asset ID:** {asset['asset_id']}  ")
    lines.append(f"**Plant Area:** {asset['area']}  ")
    lines.append(f"**Criticality:** {asset['criticality']}  ")
    lines.append(f"**Manufacturer:** {asset['manufacturer']}  ")
    lines.append(f"**Installed:** {asset['install_year']}  ")
    lines.append("")
    lines.append("## 1. Overview")
    lines.append(f"The {asset['type']} ({asset['asset_id']}) is a {asset['criticality'].lower()}-criticality asset "
                 f"in the {asset['area']} area. This manual describes its monitored parameters, normal operating "
                 f"envelope, common fault modes, recommended maintenance schedule, troubleshooting guidance, and "
                 f"associated spare parts.")
    lines.append("")
    lines.append("## 2. Monitored Parameters & Normal Operating Envelope")
    lines.append("| Parameter | Unit | Normal Low | Normal High |")
    lines.append("|---|---|---|---|")
    for name, unit, lo, hi in t["sensors"]:
        lines.append(f"| {name} | {unit} | {lo} | {hi} |")
    lines.append("")
    lines.append("Operation outside these limits should trigger investigation. Sustained excursions indicate "
                 "developing faults and should be escalated per the alerting matrix.")
    lines.append("")
    lines.append("## 3. Common Fault Modes")
    for j, (fault, desc, causes) in enumerate(t["faults"], 1):
        lines.append(f"### 3.{j} {fault}")
        lines.append(f"{desc}")
        lines.append("")
        lines.append(f"**Typical root causes:** {', '.join(causes)}.")
        lines.append("")
    lines.append("## 4. Recommended Maintenance Schedule")
    lines.append("| Task | Interval |")
    lines.append("|---|---|")
    lines.append("| Visual inspection & cleaning | Weekly |")
    lines.append("| Lubrication / fluid check | Monthly |")
    lines.append("| Vibration & thermography survey | Quarterly |")
    lines.append("| Condition-based overhaul | As indicated by trend / RUL |")
    lines.append("")
    lines.append("## 5. Troubleshooting Guide")
    for fault, desc, causes in t["faults"]:
        lines.append(f"- **Symptom related to {fault}:** Check {', '.join(causes[:2])}. "
                     f"Verify readings against Section 2 limits, inspect affected sub-assembly, and replace worn "
                     f"spares from Section 6 if confirmed.")
    lines.append("")
    lines.append("## 6. Associated Spare Parts")
    for sp in t["spares"]:
        lines.append(f"- {sp}")
    lines.append("")
    lines.append("## 7. Safety Notes")
    lines.append("Always apply Lockout-Tagout (LOTO) before intervention. Confirm zero energy state. "
                 "Refer to the relevant SOP before performing any maintenance task on this asset.")
    return "\n".join(lines)


def sop_md(asset, kind):
    t = EQUIP_TYPES[asset["type"]]
    title = {
        "startup": "Safe Start-up Procedure",
        "shutdown": "Controlled Shutdown Procedure",
        "loto": "Lockout-Tagout (LOTO) Procedure",
        "fault": "Fault Response Procedure",
    }[kind]
    lines = [f"# SOP — {title}: {asset['type']} ({asset['asset_id']})", ""]
    lines.append(f"**Applies to:** {asset['asset_id']} | **Area:** {asset['area']} | "
                 f"**Criticality:** {asset['criticality']}")
    lines.append("")
    lines.append("## Purpose")
    lines.append(f"This SOP defines the approved steps for the {title.lower()} of the {asset['type']} to ensure "
                 f"personnel safety, equipment integrity, and process continuity.")
    lines.append("")
    lines.append("## Pre-requisites")
    lines.append("- Valid work permit and PPE (helmet, gloves, safety shoes, hearing protection).")
    lines.append("- Communication established with control room.")
    lines.append("- Relevant isolation points identified.")
    lines.append("")
    lines.append("## Procedure")
    if kind == "loto":
        steps = [
            "Notify control room and obtain permit-to-work.",
            "Identify all energy sources (electrical, hydraulic, pneumatic, thermal).",
            "Switch off and isolate the main drive at the local isolator.",
            "Apply personal locks and tags at each isolation point.",
            "Dissipate stored energy (bleed hydraulic/pneumatic pressure, allow thermal cool-down).",
            "Verify zero-energy state using approved test method.",
            "Proceed with maintenance only after verification.",
        ]
    elif kind == "fault":
        f0 = t["faults"][0][0]
        steps = [
            f"On alarm, record the active parameter excursion against Section 2 limits.",
            f"Reduce load / transfer duty to standby unit if available.",
            f"Inspect for the most probable fault mode (e.g., {f0}).",
            "Isolate per the LOTO SOP before any physical intervention.",
            "Diagnose using the troubleshooting guide in the equipment manual.",
            "Replace confirmed worn spares; record part numbers consumed.",
            "Re-commission per the start-up SOP and monitor trend for 24 h.",
        ]
    elif kind == "startup":
        steps = [
            "Confirm all maintenance locks/tags removed and area clear.",
            "Verify lubrication levels and cooling media availability.",
            "Energise auxiliaries (lube, cooling) and confirm healthy readings.",
            "Start main drive at minimum load.",
            "Ramp to operating point while watching Section 2 parameters.",
            "Hand over to operations once stable.",
        ]
    else:  # shutdown
        steps = [
            "Obtain control-room clearance to stop.",
            "Reduce load progressively to minimum.",
            "Stop the main drive.",
            "Keep auxiliaries running for cool-down as specified.",
            "Isolate if maintenance is to follow (see LOTO SOP).",
        ]
    for i, s in enumerate(steps, 1):
        lines.append(f"{i}. {s}")
    lines.append("")
    lines.append("## Records")
    lines.append("Log all actions, readings, and consumed spares in the digital maintenance logbook.")
    return "\n".join(lines)


def failure_report_md(asset, idx, date):
    t = EQUIP_TYPES[asset["type"]]
    fault, desc, causes = random.choice(t["faults"])
    rc = random.choice(causes)
    downtime = random.choice([2, 4, 6, 8, 12, 18, 24, 36])
    sensor = random.choice(t["sensors"])
    lines = [f"# Failure Analysis Report — {asset['asset_id']} — FR-{date:%Y%m%d}-{idx:03d}", ""]
    lines.append(f"**Asset:** {asset['asset_id']} ({asset['type']})  ")
    lines.append(f"**Area:** {asset['area']}  ")
    lines.append(f"**Date of failure:** {date:%Y-%m-%d}  ")
    lines.append(f"**Downtime:** {downtime} hours  ")
    lines.append(f"**Fault mode:** {fault}  ")
    lines.append("")
    lines.append("## Event Description")
    lines.append(f"Operations reported an abnormal condition on {asset['asset_id']}. {desc} "
                 f"The parameter '{sensor[0]}' deviated from its normal band ({sensor[2]}–{sensor[3]} {sensor[1]}) "
                 f"prior to the trip.")
    lines.append("")
    lines.append("## Root Cause")
    lines.append(f"Investigation concluded the primary root cause was **{rc.lower()}**, leading to {fault.lower()}.")
    lines.append("")
    lines.append("## Corrective Action Taken")
    lines.append(f"- Isolated the asset per LOTO SOP.")
    lines.append(f"- Replaced affected component ({random.choice(t['spares'])}).")
    lines.append(f"- Restored normal operating parameters and monitored for 24 hours.")
    lines.append("")
    lines.append("## Preventive Recommendation")
    lines.append(f"- Tighten inspection interval for the affected sub-assembly.")
    lines.append(f"- Add '{sensor[0]}' to the early-warning watch list with alert at "
                 f"{int(sensor[3]*0.95)} {sensor[1]}.")
    lines.append(f"- Ensure spare '{random.choice(t['spares'])}' is held in stock given lead time.")
    return "\n".join(lines), {"fault": fault, "root_cause": rc, "downtime": downtime}


def maint_log_md(asset, idx, date):
    t = EQUIP_TYPES[asset["type"]]
    action = random.choice([
        "Routine quarterly vibration survey performed; readings within limits.",
        "Lubrication topped up and grease lines flushed.",
        f"Replaced {random.choice(t['spares'])} as part of condition-based maintenance.",
        "Thermography survey conducted; minor hot-spot noted and trended.",
        "Cleaned and inspected; no abnormality found.",
        f"Investigated minor alarm on '{random.choice(t['sensors'])[0]}'; recalibrated sensor.",
    ])
    eng = random.choice(["A. Mahato", "S. Iyer", "R. Banerjee", "P. Kulkarni", "M. Khan", "D. Rao"])
    lines = [f"# Maintenance Log — {asset['asset_id']} — ML-{date:%Y%m%d}-{idx:03d}", ""]
    lines.append(f"**Asset:** {asset['asset_id']} ({asset['type']})  ")
    lines.append(f"**Date:** {date:%Y-%m-%d}  ")
    lines.append(f"**Engineer:** {eng}  ")
    lines.append(f"**Work type:** {'Preventive' if 'Routine' in action or 'Lubric' in action else 'Corrective'}  ")
    lines.append("")
    lines.append("## Work Performed")
    lines.append(action)
    lines.append("")
    lines.append("## Outcome")
    lines.append(random.choice([
        "Asset returned to service in healthy condition.",
        "Parameters normalised post-intervention.",
        "Recommend follow-up at next scheduled window.",
    ]))
    return "\n".join(lines)


def gen_sensor_csv(asset, days=45, freq_min=60):
    """Generate a sensor time-series with a baseline + an injected degradation/anomaly window."""
    t = EQUIP_TYPES[asset["type"]]
    start = datetime(2026, 4, 1)
    n = int(days * 24 * 60 / freq_min)
    rows = []
    # choose one sensor to degrade for ~40% of assets
    degrade = random.random() < 0.45
    deg_sensor = random.randrange(len(t["sensors"])) if degrade else -1
    deg_start = int(n * random.uniform(0.55, 0.75))
    header = ["timestamp", "asset_id"] + [s[0] for s in t["sensors"]]
    for i in range(n):
        ts = start + timedelta(minutes=i * freq_min)
        row = [ts.strftime("%Y-%m-%d %H:%M"), asset["asset_id"]]
        for si, (name, unit, lo, hi) in enumerate(t["sensors"]):
            mid = (lo + hi) / 2.0
            span = (hi - lo) / 2.0
            # daily cycle + noise
            val = mid + 0.25 * span * math.sin(2 * math.pi * (i % 24) / 24.0)
            val += random.gauss(0, span * 0.10)
            # injected progressive degradation (trend up beyond hi)
            if si == deg_sensor and i >= deg_start:
                prog = (i - deg_start) / max(1, (n - deg_start))
                val += span * (0.6 + 1.4 * prog)  # drifts above the normal band
                if random.random() < 0.05:  # occasional spike
                    val += span * 1.2
            row.append(round(val, 2))
        rows.append(row)
    path = os.path.join(D_SE, f"{asset['asset_id']}.csv")
    with open(path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(header)
        w.writerows(rows)
    return {
        "path": os.path.relpath(path, ROOT),
        "degraded_sensor": t["sensors"][deg_sensor][0] if degrade else None,
        "rows": n,
    }


def gen_spares_catalogue(assets):
    path = os.path.join(D_SP, "spares_catalogue.csv")
    seen = {}
    rows = []
    for a in assets:
        for sp in EQUIP_TYPES[a["type"]]["spares"]:
            key = (a["type"], sp)
            if key in seen:
                continue
            seen[key] = True
            lead = random.choice([2, 3, 5, 7, 10, 14, 21, 30, 45, 60])
            stock = random.choice([0, 0, 1, 1, 2, 3, 4, 6])
            cost = random.choice([1500, 4200, 8500, 15000, 32000, 75000, 120000])
            rows.append({
                "part_name": sp,
                "equipment_type": a["type"],
                "stock_qty": stock,
                "procurement_lead_time_days": lead,
                "unit_cost_inr": cost,
                "criticality": a["criticality"],
                "preferred_vendor": random.choice(["OEM", "Local Vendor A", "Local Vendor B", "Imported"]),
            })
    with open(path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    return os.path.relpath(path, ROOT), len(rows)


DELAY_REF = datetime(2026, 5, 16)  # "today" for recent delay events (aligns with sensor window)


def gen_delay_events(asset, degraded):
    """Generate recent equipment delay events for an asset.

    Degraded assets accumulate more frequent and longer production delays, so
    delay severity correlates with equipment health (realistic + demonstrable).
    Returns (events:list[dict], delay_log_markdown:str).
    """
    t = EQUIP_TYPES[asset["type"]]
    n_events = random.randint(4, 7) if degraded else random.randint(0, 2)
    events = []
    for _ in range(n_events):
        days_ago = random.randint(0, 30)
        date = DELAY_REF - timedelta(days=days_ago)
        if degraded:
            mins = random.choice([20, 35, 50, 75, 120, 180, 240])
        else:
            mins = random.choice([5, 10, 15, 20, 30])
        fault = random.choice(t["faults"])[0]
        reason = random.choice([
            f"Production held due to {fault.lower()}",
            f"Unplanned stoppage — {fault.lower()}",
            "Process interruption pending inspection",
            "Slow-down to protect equipment after alarm",
        ])
        sev = "Critical" if mins >= 180 else "High" if mins >= 75 else "Medium" if mins >= 30 else "Low"
        events.append({
            "asset_id": asset["asset_id"], "equipment_type": asset["type"],
            "date": date.strftime("%Y-%m-%d"), "delay_minutes": mins,
            "reason": reason, "severity": sev,
        })
    events.sort(key=lambda e: e["date"])
    total = sum(e["delay_minutes"] for e in events)

    # narrative delay-log document for RAG
    lines = [f"# Equipment Delay Log — {asset['asset_id']} ({asset['type']})", ""]
    lines.append(f"**Asset:** {asset['asset_id']} | **Area:** {asset['area']} | "
                 f"**Window:** last 30 days (to {DELAY_REF:%Y-%m-%d})")
    lines.append(f"**Total recorded delay:** {total} minutes across {len(events)} event(s)")
    lines.append("")
    if events:
        lines.append("| Date | Delay (min) | Severity | Reason |")
        lines.append("|---|---|---|---|")
        for e in events:
            lines.append(f"| {e['date']} | {e['delay_minutes']} | {e['severity']} | {e['reason']} |")
    else:
        lines.append("No production delays recorded in the last 30 days for this asset.")
    return events, "\n".join(lines)


def main():
    assets = make_assets()
    manifest = {"assets": [], "counts": {}}
    n_man = n_sop = n_fr = n_ml = n_dl = 0
    all_delays = []

    base_date = datetime(2024, 1, 1)
    for a in assets:
        # manual
        with open(os.path.join(D_MAN, f"{a['asset_id']}_manual.md"), "w") as f:
            f.write(manual_md(a))
        n_man += 1
        # SOPs
        for kind in ("startup", "shutdown", "loto", "fault"):
            with open(os.path.join(D_SOP, f"{a['asset_id']}_{kind}_sop.md"), "w") as f:
                f.write(sop_md(a, kind))
            n_sop += 1
        # failure reports (history)
        for k in range(random.randint(2, 5)):
            d = base_date + timedelta(days=random.randint(0, 800))
            txt, meta = failure_report_md(a, k + 1, d)
            with open(os.path.join(D_FR, f"{a['asset_id']}_FR_{k+1:02d}.md"), "w") as f:
                f.write(txt)
            n_fr += 1
        # maintenance logs
        for k in range(random.randint(3, 7)):
            d = base_date + timedelta(days=random.randint(0, 850))
            with open(os.path.join(D_ML, f"{a['asset_id']}_ML_{k+1:02d}.md"), "w") as f:
                f.write(maint_log_md(a, k + 1, d))
            n_ml += 1
        # sensors
        sinfo = gen_sensor_csv(a)
        # delay logs (degraded assets cause more delays)
        events, dl_md = gen_delay_events(a, degraded=bool(sinfo["degraded_sensor"]))
        with open(os.path.join(D_DL, f"{a['asset_id']}_delay_log.md"), "w") as f:
            f.write(dl_md)
        n_dl += 1
        all_delays.extend(events)
        manifest["assets"].append({**a, "sensor": sinfo,
                                   "delay_minutes_30d": sum(e["delay_minutes"] for e in events)})

    # structured delay events (single source for delay-severity scoring)
    delay_csv = os.path.join(D_DELAY, "delay_events.csv")
    fields = ["asset_id", "equipment_type", "date", "delay_minutes", "reason", "severity"]
    with open(delay_csv, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(all_delays)

    sp_path, sp_n = gen_spares_catalogue(assets)

    manifest["counts"] = {
        "assets": len(assets),
        "manuals": n_man,
        "sops": n_sop,
        "failure_reports": n_fr,
        "maintenance_logs": n_ml,
        "delay_logs": n_dl,
        "delay_events": len(all_delays),
        "spare_parts": sp_n,
        "sensor_files": len(assets),
        "total_documents": n_man + n_sop + n_fr + n_ml + n_dl,
    }
    with open(os.path.join(DATA, "manifest.json"), "w") as f:
        json.dump(manifest, f, indent=2)

    c = manifest["counts"]
    print("Corpus generated:")
    print(f"  Assets ............. {c['assets']}")
    print(f"  Manuals ............ {c['manuals']}")
    print(f"  SOPs ............... {c['sops']}")
    print(f"  Failure reports .... {c['failure_reports']}")
    print(f"  Maintenance logs ... {c['maintenance_logs']}")
    print(f"  Delay logs ......... {c['delay_logs']} ({c['delay_events']} events)")
    print(f"  Spare parts ........ {c['spare_parts']}")
    print(f"  Sensor files ....... {c['sensor_files']}")
    print(f"  TOTAL documents .... {c['total_documents']}")


if __name__ == "__main__":
    main()
