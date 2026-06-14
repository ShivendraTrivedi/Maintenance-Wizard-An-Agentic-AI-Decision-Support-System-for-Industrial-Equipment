# Failure Analysis Report — COR-01 — FR-20250120-002

**Asset:** COR-01 (Coke Oven Pushing Ram)  
**Area:** Coke Making  
**Date of failure:** 2025-01-20  
**Downtime:** 2 hours  
**Fault mode:** Drive gearbox wear  

## Event Description
Operations reported an abnormal condition on COR-01. Rising current and vibration signal gear tooth wear. The parameter 'drive_motor_current' deviated from its normal band (120–320 A) prior to the trip.

## Root Cause
Investigation concluded the primary root cause was **misalignment**, leading to drive gearbox wear.

## Corrective Action Taken
- Isolated the asset per LOTO SOP.
- Replaced affected component (Ram shoe).
- Restored normal operating parameters and monitored for 24 hours.

## Preventive Recommendation
- Tighten inspection interval for the affected sub-assembly.
- Add 'drive_motor_current' to the early-warning watch list with alert at 304 A.
- Ensure spare 'Rail clamp' is held in stock given lead time.