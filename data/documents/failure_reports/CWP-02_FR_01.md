# Failure Analysis Report — CWP-02 — FR-20241020-001

**Asset:** CWP-02 (Cooling Water Pump)  
**Area:** Utilities  
**Date of failure:** 2024-10-20  
**Downtime:** 8 hours  
**Fault mode:** Impeller wear  

## Event Description
Operations reported an abnormal condition on CWP-02. Reduced flow and pressure from worn impeller clearances. The parameter 'motor_current' deviated from its normal band (80–220 A) prior to the trip.

## Root Cause
Investigation concluded the primary root cause was **erosion**, leading to impeller wear.

## Corrective Action Taken
- Isolated the asset per LOTO SOP.
- Replaced affected component (Wear ring).
- Restored normal operating parameters and monitored for 24 hours.

## Preventive Recommendation
- Tighten inspection interval for the affected sub-assembly.
- Add 'motor_current' to the early-warning watch list with alert at 209 A.
- Ensure spare 'Bearing set' is held in stock given lead time.