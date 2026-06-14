# Failure Analysis Report — CWP-04 — FR-20240830-004

**Asset:** CWP-04 (Cooling Water Pump)  
**Area:** Utilities  
**Date of failure:** 2024-08-30  
**Downtime:** 4 hours  
**Fault mode:** Cavitation  

## Event Description
Operations reported an abnormal condition on CWP-04. Low suction head causes pressure pulsation and impeller pitting. The parameter 'bearing_temperature' deviated from its normal band (40–80 degC) prior to the trip.

## Root Cause
Investigation concluded the primary root cause was **clogged suction strainer**, leading to cavitation.

## Corrective Action Taken
- Isolated the asset per LOTO SOP.
- Replaced affected component (Bearing set).
- Restored normal operating parameters and monitored for 24 hours.

## Preventive Recommendation
- Tighten inspection interval for the affected sub-assembly.
- Add 'bearing_temperature' to the early-warning watch list with alert at 76 degC.
- Ensure spare 'Bearing set' is held in stock given lead time.