# Failure Analysis Report — CWP-08 — FR-20240827-004

**Asset:** CWP-08 (Cooling Water Pump)  
**Area:** Utilities  
**Date of failure:** 2024-08-27  
**Downtime:** 24 hours  
**Fault mode:** Cavitation  

## Event Description
Operations reported an abnormal condition on CWP-08. Low suction head causes pressure pulsation and impeller pitting. The parameter 'discharge_pressure' deviated from its normal band (4–9 bar) prior to the trip.

## Root Cause
Investigation concluded the primary root cause was **clogged suction strainer**, leading to cavitation.

## Corrective Action Taken
- Isolated the asset per LOTO SOP.
- Replaced affected component (Wear ring).
- Restored normal operating parameters and monitored for 24 hours.

## Preventive Recommendation
- Tighten inspection interval for the affected sub-assembly.
- Add 'discharge_pressure' to the early-warning watch list with alert at 8 bar.
- Ensure spare 'Mechanical seal' is held in stock given lead time.