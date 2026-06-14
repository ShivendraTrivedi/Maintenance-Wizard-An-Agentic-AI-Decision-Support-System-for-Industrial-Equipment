# Failure Analysis Report — HSM-M-05 — FR-20260221-005

**Asset:** HSM-M-05 (Hot Strip Mill Main Drive Motor)  
**Area:** Hot Rolling  
**Date of failure:** 2026-02-21  
**Downtime:** 2 hours  
**Fault mode:** Bearing wear / imbalance  

## Event Description
Operations reported an abnormal condition on HSM-M-05. Rising vibration and bearing temperature indicate progressive bearing degradation. The parameter 'vibration_de' deviated from its normal band (1.0–4.5 mm/s) prior to the trip.

## Root Cause
Investigation concluded the primary root cause was **contaminated grease**, leading to bearing wear / imbalance.

## Corrective Action Taken
- Isolated the asset per LOTO SOP.
- Replaced affected component (DE bearing (SKF 6324)).
- Restored normal operating parameters and monitored for 24 hours.

## Preventive Recommendation
- Tighten inspection interval for the affected sub-assembly.
- Add 'vibration_de' to the early-warning watch list with alert at 4 mm/s.
- Ensure spare 'Stator winding kit' is held in stock given lead time.