# Failure Analysis Report — CWP-08 — FR-20240726-001

**Asset:** CWP-08 (Cooling Water Pump)  
**Area:** Utilities  
**Date of failure:** 2024-07-26  
**Downtime:** 8 hours  
**Fault mode:** Cavitation  

## Event Description
Operations reported an abnormal condition on CWP-08. Low suction head causes pressure pulsation and impeller pitting. The parameter 'motor_current' deviated from its normal band (80–220 A) prior to the trip.

## Root Cause
Investigation concluded the primary root cause was **low sump level**, leading to cavitation.

## Corrective Action Taken
- Isolated the asset per LOTO SOP.
- Replaced affected component (Bearing set).
- Restored normal operating parameters and monitored for 24 hours.

## Preventive Recommendation
- Tighten inspection interval for the affected sub-assembly.
- Add 'motor_current' to the early-warning watch list with alert at 209 A.
- Ensure spare 'Pump impeller' is held in stock given lead time.