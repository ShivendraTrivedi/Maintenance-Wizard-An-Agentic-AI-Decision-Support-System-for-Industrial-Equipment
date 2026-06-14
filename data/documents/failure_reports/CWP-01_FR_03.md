# Failure Analysis Report — CWP-01 — FR-20250804-003

**Asset:** CWP-01 (Cooling Water Pump)  
**Area:** Utilities  
**Date of failure:** 2025-08-04  
**Downtime:** 2 hours  
**Fault mode:** Mechanical seal leak  

## Event Description
Operations reported an abnormal condition on CWP-01. Seal failure causes leakage and bearing contamination. The parameter 'discharge_pressure' deviated from its normal band (4–9 bar) prior to the trip.

## Root Cause
Investigation concluded the primary root cause was **dry running**, leading to mechanical seal leak.

## Corrective Action Taken
- Isolated the asset per LOTO SOP.
- Replaced affected component (Wear ring).
- Restored normal operating parameters and monitored for 24 hours.

## Preventive Recommendation
- Tighten inspection interval for the affected sub-assembly.
- Add 'discharge_pressure' to the early-warning watch list with alert at 8 bar.
- Ensure spare 'Wear ring' is held in stock given lead time.