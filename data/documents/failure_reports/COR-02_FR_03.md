# Failure Analysis Report — COR-02 — FR-20240916-003

**Asset:** COR-02 (Coke Oven Pushing Ram)  
**Area:** Coke Making  
**Date of failure:** 2024-09-16  
**Downtime:** 24 hours  
**Fault mode:** Rail misalignment  

## Event Description
Operations reported an abnormal condition on COR-02. Uneven ram travel and rail heating. The parameter 'ram_speed' deviated from its normal band (8–18 m/min) prior to the trip.

## Root Cause
Investigation concluded the primary root cause was **debris on rail**, leading to rail misalignment.

## Corrective Action Taken
- Isolated the asset per LOTO SOP.
- Replaced affected component (Rail clamp).
- Restored normal operating parameters and monitored for 24 hours.

## Preventive Recommendation
- Tighten inspection interval for the affected sub-assembly.
- Add 'ram_speed' to the early-warning watch list with alert at 17 m/min.
- Ensure spare 'Drive gearbox' is held in stock given lead time.