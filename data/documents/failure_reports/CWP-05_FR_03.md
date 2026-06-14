# Failure Analysis Report — CWP-05 — FR-20241125-003

**Asset:** CWP-05 (Cooling Water Pump)  
**Area:** Utilities  
**Date of failure:** 2024-11-25  
**Downtime:** 4 hours  
**Fault mode:** Mechanical seal leak  

## Event Description
Operations reported an abnormal condition on CWP-05. Seal failure causes leakage and bearing contamination. The parameter 'flow_rate' deviated from its normal band (300–700 m3/h) prior to the trip.

## Root Cause
Investigation concluded the primary root cause was **dry running**, leading to mechanical seal leak.

## Corrective Action Taken
- Isolated the asset per LOTO SOP.
- Replaced affected component (Mechanical seal).
- Restored normal operating parameters and monitored for 24 hours.

## Preventive Recommendation
- Tighten inspection interval for the affected sub-assembly.
- Add 'flow_rate' to the early-warning watch list with alert at 665 m3/h.
- Ensure spare 'Bearing set' is held in stock given lead time.