# Failure Analysis Report — HSM-M-02 — FR-20240826-002

**Asset:** HSM-M-02 (Hot Strip Mill Main Drive Motor)  
**Area:** Hot Rolling  
**Date of failure:** 2024-08-26  
**Downtime:** 12 hours  
**Fault mode:** Coupling misalignment  

## Event Description
Operations reported an abnormal condition on HSM-M-02. High NDE vibration with characteristic 2x running frequency. The parameter 'vibration_nde' deviated from its normal band (1.0–4.5 mm/s) prior to the trip.

## Root Cause
Investigation concluded the primary root cause was **thermal growth**, leading to coupling misalignment.

## Corrective Action Taken
- Isolated the asset per LOTO SOP.
- Replaced affected component (Stator winding kit).
- Restored normal operating parameters and monitored for 24 hours.

## Preventive Recommendation
- Tighten inspection interval for the affected sub-assembly.
- Add 'vibration_nde' to the early-warning watch list with alert at 4 mm/s.
- Ensure spare 'DE bearing (SKF 6324)' is held in stock given lead time.