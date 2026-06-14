# Failure Analysis Report — CWP-04 — FR-20240416-005

**Asset:** CWP-04 (Cooling Water Pump)  
**Area:** Utilities  
**Date of failure:** 2024-04-16  
**Downtime:** 24 hours  
**Fault mode:** Mechanical seal leak  

## Event Description
Operations reported an abnormal condition on CWP-04. Seal failure causes leakage and bearing contamination. The parameter 'bearing_temperature' deviated from its normal band (40–80 degC) prior to the trip.

## Root Cause
Investigation concluded the primary root cause was **misalignment**, leading to mechanical seal leak.

## Corrective Action Taken
- Isolated the asset per LOTO SOP.
- Replaced affected component (Bearing set).
- Restored normal operating parameters and monitored for 24 hours.

## Preventive Recommendation
- Tighten inspection interval for the affected sub-assembly.
- Add 'bearing_temperature' to the early-warning watch list with alert at 76 degC.
- Ensure spare 'Pump impeller' is held in stock given lead time.