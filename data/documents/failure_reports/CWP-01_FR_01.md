# Failure Analysis Report — CWP-01 — FR-20240824-001

**Asset:** CWP-01 (Cooling Water Pump)  
**Area:** Utilities  
**Date of failure:** 2024-08-24  
**Downtime:** 18 hours  
**Fault mode:** Impeller wear  

## Event Description
Operations reported an abnormal condition on CWP-01. Reduced flow and pressure from worn impeller clearances. The parameter 'flow_rate' deviated from its normal band (300–700 m3/h) prior to the trip.

## Root Cause
Investigation concluded the primary root cause was **abrasive water**, leading to impeller wear.

## Corrective Action Taken
- Isolated the asset per LOTO SOP.
- Replaced affected component (Mechanical seal).
- Restored normal operating parameters and monitored for 24 hours.

## Preventive Recommendation
- Tighten inspection interval for the affected sub-assembly.
- Add 'flow_rate' to the early-warning watch list with alert at 665 m3/h.
- Ensure spare 'Mechanical seal' is held in stock given lead time.