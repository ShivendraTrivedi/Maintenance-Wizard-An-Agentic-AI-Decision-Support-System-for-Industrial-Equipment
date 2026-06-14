# Failure Analysis Report — CWP-04 — FR-20241001-002

**Asset:** CWP-04 (Cooling Water Pump)  
**Area:** Utilities  
**Date of failure:** 2024-10-01  
**Downtime:** 18 hours  
**Fault mode:** Cavitation  

## Event Description
Operations reported an abnormal condition on CWP-04. Low suction head causes pressure pulsation and impeller pitting. The parameter 'motor_current' deviated from its normal band (80–220 A) prior to the trip.

## Root Cause
Investigation concluded the primary root cause was **air ingress**, leading to cavitation.

## Corrective Action Taken
- Isolated the asset per LOTO SOP.
- Replaced affected component (Wear ring).
- Restored normal operating parameters and monitored for 24 hours.

## Preventive Recommendation
- Tighten inspection interval for the affected sub-assembly.
- Add 'motor_current' to the early-warning watch list with alert at 209 A.
- Ensure spare 'Wear ring' is held in stock given lead time.