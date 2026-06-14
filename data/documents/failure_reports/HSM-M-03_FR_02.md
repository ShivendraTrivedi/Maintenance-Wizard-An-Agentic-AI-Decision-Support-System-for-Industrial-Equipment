# Failure Analysis Report — HSM-M-03 — FR-20250925-002

**Asset:** HSM-M-03 (Hot Strip Mill Main Drive Motor)  
**Area:** Hot Rolling  
**Date of failure:** 2025-09-25  
**Downtime:** 12 hours  
**Fault mode:** Bearing wear / imbalance  

## Event Description
Operations reported an abnormal condition on HSM-M-03. Rising vibration and bearing temperature indicate progressive bearing degradation. The parameter 'motor_current' deviated from its normal band (800–1600 A) prior to the trip.

## Root Cause
Investigation concluded the primary root cause was **lubrication starvation**, leading to bearing wear / imbalance.

## Corrective Action Taken
- Isolated the asset per LOTO SOP.
- Replaced affected component (DE bearing (SKF 6324)).
- Restored normal operating parameters and monitored for 24 hours.

## Preventive Recommendation
- Tighten inspection interval for the affected sub-assembly.
- Add 'motor_current' to the early-warning watch list with alert at 1520 A.
- Ensure spare 'DE bearing (SKF 6324)' is held in stock given lead time.