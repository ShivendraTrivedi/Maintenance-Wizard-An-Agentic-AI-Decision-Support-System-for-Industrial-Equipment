# Failure Analysis Report — BFS-03 — FR-20241018-001

**Asset:** BFS-03 (Blast Furnace Stove)  
**Area:** Iron Making  
**Date of failure:** 2024-10-18  
**Downtime:** 2 hours  
**Fault mode:** Checker brick degradation  

## Event Description
Operations reported an abnormal condition on BFS-03. Thermal cycling fatigue and dust deposition reduce heat-transfer efficiency. The parameter 'dome_temperature' deviated from its normal band (1100–1450 degC) prior to the trip.

## Root Cause
Investigation concluded the primary root cause was **poor gas cleaning upstream**, leading to checker brick degradation.

## Corrective Action Taken
- Isolated the asset per LOTO SOP.
- Replaced affected component (Cooling stave).
- Restored normal operating parameters and monitored for 24 hours.

## Preventive Recommendation
- Tighten inspection interval for the affected sub-assembly.
- Add 'dome_temperature' to the early-warning watch list with alert at 1377 degC.
- Ensure spare 'Checker bricks (silica)' is held in stock given lead time.