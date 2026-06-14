# Failure Analysis Report — RHF-WBD-01 — FR-20250218-001

**Asset:** RHF-WBD-01 (Reheating Furnace Walking Beam Drive)  
**Area:** Hot Rolling  
**Date of failure:** 2025-02-18  
**Downtime:** 8 hours  
**Fault mode:** Hydraulic cylinder drift  

## Event Description
Operations reported an abnormal condition on RHF-WBD-01. Internal leakage causes beam position error and skid marks. The parameter 'cylinder_drift' deviated from its normal band (0–3 mm/cycle) prior to the trip.

## Root Cause
Investigation concluded the primary root cause was **piston seal wear**, leading to hydraulic cylinder drift.

## Corrective Action Taken
- Isolated the asset per LOTO SOP.
- Replaced affected component (Hydraulic cooler).
- Restored normal operating parameters and monitored for 24 hours.

## Preventive Recommendation
- Tighten inspection interval for the affected sub-assembly.
- Add 'cylinder_drift' to the early-warning watch list with alert at 2 mm/cycle.
- Ensure spare 'Cylinder seal kit' is held in stock given lead time.