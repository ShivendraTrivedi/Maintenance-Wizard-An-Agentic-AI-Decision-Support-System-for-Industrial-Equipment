# Failure Analysis Report — CWP-02 — FR-20250724-003

**Asset:** CWP-02 (Cooling Water Pump)  
**Area:** Utilities  
**Date of failure:** 2025-07-24  
**Downtime:** 8 hours  
**Fault mode:** Cavitation  

## Event Description
Operations reported an abnormal condition on CWP-02. Low suction head causes pressure pulsation and impeller pitting. The parameter 'bearing_temperature' deviated from its normal band (40–80 degC) prior to the trip.

## Root Cause
Investigation concluded the primary root cause was **low sump level**, leading to cavitation.

## Corrective Action Taken
- Isolated the asset per LOTO SOP.
- Replaced affected component (Pump impeller).
- Restored normal operating parameters and monitored for 24 hours.

## Preventive Recommendation
- Tighten inspection interval for the affected sub-assembly.
- Add 'bearing_temperature' to the early-warning watch list with alert at 76 degC.
- Ensure spare 'Wear ring' is held in stock given lead time.