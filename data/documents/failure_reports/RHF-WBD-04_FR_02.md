# Failure Analysis Report — RHF-WBD-04 — FR-20250925-002

**Asset:** RHF-WBD-04 (Reheating Furnace Walking Beam Drive)  
**Area:** Hot Rolling  
**Date of failure:** 2025-09-25  
**Downtime:** 2 hours  
**Fault mode:** Oil overheating  

## Event Description
Operations reported an abnormal condition on RHF-WBD-04. High oil temperature degrades viscosity and seals. The parameter 'cylinder_drift' deviated from its normal band (0–3 mm/cycle) prior to the trip.

## Root Cause
Investigation concluded the primary root cause was **low oil level**, leading to oil overheating.

## Corrective Action Taken
- Isolated the asset per LOTO SOP.
- Replaced affected component (Cylinder seal kit).
- Restored normal operating parameters and monitored for 24 hours.

## Preventive Recommendation
- Tighten inspection interval for the affected sub-assembly.
- Add 'cylinder_drift' to the early-warning watch list with alert at 2 mm/cycle.
- Ensure spare 'Hydraulic cooler' is held in stock given lead time.