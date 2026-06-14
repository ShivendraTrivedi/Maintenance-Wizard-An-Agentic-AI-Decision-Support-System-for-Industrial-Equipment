# Failure Analysis Report — BFS-03 — FR-20250924-005

**Asset:** BFS-03 (Blast Furnace Stove)  
**Area:** Iron Making  
**Date of failure:** 2025-09-24  
**Downtime:** 8 hours  
**Fault mode:** Checker brick degradation  

## Event Description
Operations reported an abnormal condition on BFS-03. Thermal cycling fatigue and dust deposition reduce heat-transfer efficiency. The parameter 'dome_temperature' deviated from its normal band (1100–1450 degC) prior to the trip.

## Root Cause
Investigation concluded the primary root cause was **excessive thermal cycling**, leading to checker brick degradation.

## Corrective Action Taken
- Isolated the asset per LOTO SOP.
- Replaced affected component (Checker bricks (silica)).
- Restored normal operating parameters and monitored for 24 hours.

## Preventive Recommendation
- Tighten inspection interval for the affected sub-assembly.
- Add 'dome_temperature' to the early-warning watch list with alert at 1377 degC.
- Ensure spare 'Hot blast valve seat' is held in stock given lead time.