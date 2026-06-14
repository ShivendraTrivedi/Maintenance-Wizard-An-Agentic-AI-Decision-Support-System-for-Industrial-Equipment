# Failure Analysis Report — COR-01 — FR-20240328-004

**Asset:** COR-01 (Coke Oven Pushing Ram)  
**Area:** Coke Making  
**Date of failure:** 2024-03-28  
**Downtime:** 4 hours  
**Fault mode:** Hard pushing / sticky oven  

## Event Description
Operations reported an abnormal condition on COR-01. Abnormally high ram force indicates poor coke release. The parameter 'drive_motor_current' deviated from its normal band (120–320 A) prior to the trip.

## Root Cause
Investigation concluded the primary root cause was **coal blend issue**, leading to hard pushing / sticky oven.

## Corrective Action Taken
- Isolated the asset per LOTO SOP.
- Replaced affected component (Ram chain link).
- Restored normal operating parameters and monitored for 24 hours.

## Preventive Recommendation
- Tighten inspection interval for the affected sub-assembly.
- Add 'drive_motor_current' to the early-warning watch list with alert at 304 A.
- Ensure spare 'Drive gearbox' is held in stock given lead time.