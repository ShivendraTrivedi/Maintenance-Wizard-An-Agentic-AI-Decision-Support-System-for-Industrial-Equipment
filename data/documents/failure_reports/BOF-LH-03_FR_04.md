# Failure Analysis Report — BOF-LH-03 — FR-20250707-004

**Asset:** BOF-LH-03 (BOF Lance Hoist)  
**Area:** Steel Making  
**Date of failure:** 2025-07-07  
**Downtime:** 2 hours  
**Fault mode:** Brake fade  

## Event Description
Operations reported an abnormal condition on BOF-LH-03. Rising brake temperature reduces holding capacity. The parameter 'brake_temperature' deviated from its normal band (30–75 degC) prior to the trip.

## Root Cause
Investigation concluded the primary root cause was **worn brake pads**, leading to brake fade.

## Corrective Action Taken
- Isolated the asset per LOTO SOP.
- Replaced affected component (Brake pad set).
- Restored normal operating parameters and monitored for 24 hours.

## Preventive Recommendation
- Tighten inspection interval for the affected sub-assembly.
- Add 'brake_temperature' to the early-warning watch list with alert at 71 degC.
- Ensure spare 'Brake pad set' is held in stock given lead time.