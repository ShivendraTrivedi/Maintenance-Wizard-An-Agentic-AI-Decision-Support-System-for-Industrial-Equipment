# Failure Analysis Report — BOF-LH-02 — FR-20250703-003

**Asset:** BOF-LH-02 (BOF Lance Hoist)  
**Area:** Steel Making  
**Date of failure:** 2025-07-03  
**Downtime:** 8 hours  
**Fault mode:** Brake fade  

## Event Description
Operations reported an abnormal condition on BOF-LH-02. Rising brake temperature reduces holding capacity. The parameter 'brake_temperature' deviated from its normal band (30–75 degC) prior to the trip.

## Root Cause
Investigation concluded the primary root cause was **worn brake pads**, leading to brake fade.

## Corrective Action Taken
- Isolated the asset per LOTO SOP.
- Replaced affected component (Sheave wheel).
- Restored normal operating parameters and monitored for 24 hours.

## Preventive Recommendation
- Tighten inspection interval for the affected sub-assembly.
- Add 'brake_temperature' to the early-warning watch list with alert at 71 degC.
- Ensure spare 'Wire rope' is held in stock given lead time.