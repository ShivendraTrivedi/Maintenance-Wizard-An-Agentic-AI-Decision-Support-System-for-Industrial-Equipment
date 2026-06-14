# Failure Analysis Report — CWP-03 — FR-20241017-003

**Asset:** CWP-03 (Cooling Water Pump)  
**Area:** Utilities  
**Date of failure:** 2024-10-17  
**Downtime:** 24 hours  
**Fault mode:** Cavitation  

## Event Description
Operations reported an abnormal condition on CWP-03. Low suction head causes pressure pulsation and impeller pitting. The parameter 'bearing_temperature' deviated from its normal band (40–80 degC) prior to the trip.

## Root Cause
Investigation concluded the primary root cause was **low sump level**, leading to cavitation.

## Corrective Action Taken
- Isolated the asset per LOTO SOP.
- Replaced affected component (Mechanical seal).
- Restored normal operating parameters and monitored for 24 hours.

## Preventive Recommendation
- Tighten inspection interval for the affected sub-assembly.
- Add 'bearing_temperature' to the early-warning watch list with alert at 76 degC.
- Ensure spare 'Mechanical seal' is held in stock given lead time.