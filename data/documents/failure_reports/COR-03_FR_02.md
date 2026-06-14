# Failure Analysis Report — COR-03 — FR-20250525-002

**Asset:** COR-03 (Coke Oven Pushing Ram)  
**Area:** Coke Making  
**Date of failure:** 2025-05-25  
**Downtime:** 24 hours  
**Fault mode:** Drive gearbox wear  

## Event Description
Operations reported an abnormal condition on COR-03. Rising current and vibration signal gear tooth wear. The parameter 'drive_motor_current' deviated from its normal band (120–320 A) prior to the trip.

## Root Cause
Investigation concluded the primary root cause was **lubrication failure**, leading to drive gearbox wear.

## Corrective Action Taken
- Isolated the asset per LOTO SOP.
- Replaced affected component (Ram shoe).
- Restored normal operating parameters and monitored for 24 hours.

## Preventive Recommendation
- Tighten inspection interval for the affected sub-assembly.
- Add 'drive_motor_current' to the early-warning watch list with alert at 304 A.
- Ensure spare 'Ram chain link' is held in stock given lead time.