# Failure Analysis Report — HSM-M-01 — FR-20240709-001

**Asset:** HSM-M-01 (Hot Strip Mill Main Drive Motor)  
**Area:** Hot Rolling  
**Date of failure:** 2024-07-09  
**Downtime:** 24 hours  
**Fault mode:** Coupling misalignment  

## Event Description
Operations reported an abnormal condition on HSM-M-01. High NDE vibration with characteristic 2x running frequency. The parameter 'vibration_de' deviated from its normal band (1.0–4.5 mm/s) prior to the trip.

## Root Cause
Investigation concluded the primary root cause was **foundation settling**, leading to coupling misalignment.

## Corrective Action Taken
- Isolated the asset per LOTO SOP.
- Replaced affected component (Stator winding kit).
- Restored normal operating parameters and monitored for 24 hours.

## Preventive Recommendation
- Tighten inspection interval for the affected sub-assembly.
- Add 'vibration_de' to the early-warning watch list with alert at 4 mm/s.
- Ensure spare 'Stator winding kit' is held in stock given lead time.