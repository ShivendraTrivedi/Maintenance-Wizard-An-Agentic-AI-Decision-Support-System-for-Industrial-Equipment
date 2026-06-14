# Failure Analysis Report — BOF-LH-02 — FR-20240128-004

**Asset:** BOF-LH-02 (BOF Lance Hoist)  
**Area:** Steel Making  
**Date of failure:** 2024-01-28  
**Downtime:** 8 hours  
**Fault mode:** Cooling water flow drop  

## Event Description
Operations reported an abnormal condition on BOF-LH-02. Reduced lance cooling risks lance burn-through during blow. The parameter 'brake_temperature' deviated from its normal band (30–75 degC) prior to the trip.

## Root Cause
Investigation concluded the primary root cause was **valve fault**, leading to cooling water flow drop.

## Corrective Action Taken
- Isolated the asset per LOTO SOP.
- Replaced affected component (Sheave wheel).
- Restored normal operating parameters and monitored for 24 hours.

## Preventive Recommendation
- Tighten inspection interval for the affected sub-assembly.
- Add 'brake_temperature' to the early-warning watch list with alert at 71 degC.
- Ensure spare 'Cooling water pump' is held in stock given lead time.