# Failure Analysis Report — CWP-01 — FR-20240807-004

**Asset:** CWP-01 (Cooling Water Pump)  
**Area:** Utilities  
**Date of failure:** 2024-08-07  
**Downtime:** 6 hours  
**Fault mode:** Cavitation  

## Event Description
Operations reported an abnormal condition on CWP-01. Low suction head causes pressure pulsation and impeller pitting. The parameter 'motor_current' deviated from its normal band (80–220 A) prior to the trip.

## Root Cause
Investigation concluded the primary root cause was **air ingress**, leading to cavitation.

## Corrective Action Taken
- Isolated the asset per LOTO SOP.
- Replaced affected component (Pump impeller).
- Restored normal operating parameters and monitored for 24 hours.

## Preventive Recommendation
- Tighten inspection interval for the affected sub-assembly.
- Add 'motor_current' to the early-warning watch list with alert at 209 A.
- Ensure spare 'Bearing set' is held in stock given lead time.