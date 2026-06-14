# Failure Analysis Report — BFS-04 — FR-20251007-001

**Asset:** BFS-04 (Blast Furnace Stove)  
**Area:** Iron Making  
**Date of failure:** 2025-10-07  
**Downtime:** 8 hours  
**Fault mode:** Checker brick degradation  

## Event Description
Operations reported an abnormal condition on BFS-04. Thermal cycling fatigue and dust deposition reduce heat-transfer efficiency. The parameter 'waste_gas_temp' deviated from its normal band (250–400 degC) prior to the trip.

## Root Cause
Investigation concluded the primary root cause was **poor gas cleaning upstream**, leading to checker brick degradation.

## Corrective Action Taken
- Isolated the asset per LOTO SOP.
- Replaced affected component (Hot blast valve seat).
- Restored normal operating parameters and monitored for 24 hours.

## Preventive Recommendation
- Tighten inspection interval for the affected sub-assembly.
- Add 'waste_gas_temp' to the early-warning watch list with alert at 380 degC.
- Ensure spare 'Hot blast valve seat' is held in stock given lead time.