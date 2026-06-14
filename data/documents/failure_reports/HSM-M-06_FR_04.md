# Failure Analysis Report — HSM-M-06 — FR-20250919-004

**Asset:** HSM-M-06 (Hot Strip Mill Main Drive Motor)  
**Area:** Hot Rolling  
**Date of failure:** 2025-09-19  
**Downtime:** 8 hours  
**Fault mode:** Coupling misalignment  

## Event Description
Operations reported an abnormal condition on HSM-M-06. High NDE vibration with characteristic 2x running frequency. The parameter 'vibration_nde' deviated from its normal band (1.0–4.5 mm/s) prior to the trip.

## Root Cause
Investigation concluded the primary root cause was **improper installation**, leading to coupling misalignment.

## Corrective Action Taken
- Isolated the asset per LOTO SOP.
- Replaced affected component (DE bearing (SKF 6324)).
- Restored normal operating parameters and monitored for 24 hours.

## Preventive Recommendation
- Tighten inspection interval for the affected sub-assembly.
- Add 'vibration_nde' to the early-warning watch list with alert at 4 mm/s.
- Ensure spare 'Flexible coupling element' is held in stock given lead time.