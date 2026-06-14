# Failure Analysis Report — COR-03 — FR-20240820-003

**Asset:** COR-03 (Coke Oven Pushing Ram)  
**Area:** Coke Making  
**Date of failure:** 2024-08-20  
**Downtime:** 18 hours  
**Fault mode:** Drive gearbox wear  

## Event Description
Operations reported an abnormal condition on COR-03. Rising current and vibration signal gear tooth wear. The parameter 'rail_temperature' deviated from its normal band (40–90 degC) prior to the trip.

## Root Cause
Investigation concluded the primary root cause was **overload pushing**, leading to drive gearbox wear.

## Corrective Action Taken
- Isolated the asset per LOTO SOP.
- Replaced affected component (Rail clamp).
- Restored normal operating parameters and monitored for 24 hours.

## Preventive Recommendation
- Tighten inspection interval for the affected sub-assembly.
- Add 'rail_temperature' to the early-warning watch list with alert at 85 degC.
- Ensure spare 'Ram chain link' is held in stock given lead time.