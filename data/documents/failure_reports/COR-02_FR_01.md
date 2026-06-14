# Failure Analysis Report — COR-02 — FR-20240731-001

**Asset:** COR-02 (Coke Oven Pushing Ram)  
**Area:** Coke Making  
**Date of failure:** 2024-07-31  
**Downtime:** 36 hours  
**Fault mode:** Drive gearbox wear  

## Event Description
Operations reported an abnormal condition on COR-02. Rising current and vibration signal gear tooth wear. The parameter 'rail_temperature' deviated from its normal band (40–90 degC) prior to the trip.

## Root Cause
Investigation concluded the primary root cause was **misalignment**, leading to drive gearbox wear.

## Corrective Action Taken
- Isolated the asset per LOTO SOP.
- Replaced affected component (Rail clamp).
- Restored normal operating parameters and monitored for 24 hours.

## Preventive Recommendation
- Tighten inspection interval for the affected sub-assembly.
- Add 'rail_temperature' to the early-warning watch list with alert at 85 degC.
- Ensure spare 'Ram shoe' is held in stock given lead time.