# Failure Analysis Report — HSM-M-05 — FR-20250505-003

**Asset:** HSM-M-05 (Hot Strip Mill Main Drive Motor)  
**Area:** Hot Rolling  
**Date of failure:** 2025-05-05  
**Downtime:** 18 hours  
**Fault mode:** Coupling misalignment  

## Event Description
Operations reported an abnormal condition on HSM-M-05. High NDE vibration with characteristic 2x running frequency. The parameter 'motor_current' deviated from its normal band (800–1600 A) prior to the trip.

## Root Cause
Investigation concluded the primary root cause was **foundation settling**, leading to coupling misalignment.

## Corrective Action Taken
- Isolated the asset per LOTO SOP.
- Replaced affected component (DE bearing (SKF 6324)).
- Restored normal operating parameters and monitored for 24 hours.

## Preventive Recommendation
- Tighten inspection interval for the affected sub-assembly.
- Add 'motor_current' to the early-warning watch list with alert at 1520 A.
- Ensure spare 'Flexible coupling element' is held in stock given lead time.