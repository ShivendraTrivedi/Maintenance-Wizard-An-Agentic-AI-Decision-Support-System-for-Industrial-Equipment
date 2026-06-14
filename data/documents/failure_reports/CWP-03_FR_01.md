# Failure Analysis Report — CWP-03 — FR-20241002-001

**Asset:** CWP-03 (Cooling Water Pump)  
**Area:** Utilities  
**Date of failure:** 2024-10-02  
**Downtime:** 4 hours  
**Fault mode:** Cavitation  

## Event Description
Operations reported an abnormal condition on CWP-03. Low suction head causes pressure pulsation and impeller pitting. The parameter 'discharge_pressure' deviated from its normal band (4–9 bar) prior to the trip.

## Root Cause
Investigation concluded the primary root cause was **low sump level**, leading to cavitation.

## Corrective Action Taken
- Isolated the asset per LOTO SOP.
- Replaced affected component (Pump impeller).
- Restored normal operating parameters and monitored for 24 hours.

## Preventive Recommendation
- Tighten inspection interval for the affected sub-assembly.
- Add 'discharge_pressure' to the early-warning watch list with alert at 8 bar.
- Ensure spare 'Bearing set' is held in stock given lead time.