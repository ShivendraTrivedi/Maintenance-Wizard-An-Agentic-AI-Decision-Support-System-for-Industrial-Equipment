# Failure Analysis Report — HSM-M-04 — FR-20250506-002

**Asset:** HSM-M-04 (Hot Strip Mill Main Drive Motor)  
**Area:** Hot Rolling  
**Date of failure:** 2025-05-06  
**Downtime:** 4 hours  
**Fault mode:** Bearing wear / imbalance  

## Event Description
Operations reported an abnormal condition on HSM-M-04. Rising vibration and bearing temperature indicate progressive bearing degradation. The parameter 'vibration_de' deviated from its normal band (1.0–4.5 mm/s) prior to the trip.

## Root Cause
Investigation concluded the primary root cause was **excess load cycling**, leading to bearing wear / imbalance.

## Corrective Action Taken
- Isolated the asset per LOTO SOP.
- Replaced affected component (Flexible coupling element).
- Restored normal operating parameters and monitored for 24 hours.

## Preventive Recommendation
- Tighten inspection interval for the affected sub-assembly.
- Add 'vibration_de' to the early-warning watch list with alert at 4 mm/s.
- Ensure spare 'Flexible coupling element' is held in stock given lead time.