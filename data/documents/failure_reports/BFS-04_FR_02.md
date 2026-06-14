# Failure Analysis Report — BFS-04 — FR-20250221-002

**Asset:** BFS-04 (Blast Furnace Stove)  
**Area:** Iron Making  
**Date of failure:** 2025-02-21  
**Downtime:** 12 hours  
**Fault mode:** Checker brick degradation  

## Event Description
Operations reported an abnormal condition on BFS-04. Thermal cycling fatigue and dust deposition reduce heat-transfer efficiency. The parameter 'waste_gas_temp' deviated from its normal band (250–400 degC) prior to the trip.

## Root Cause
Investigation concluded the primary root cause was **overdue checker inspection**, leading to checker brick degradation.

## Corrective Action Taken
- Isolated the asset per LOTO SOP.
- Replaced affected component (Burner nozzle).
- Restored normal operating parameters and monitored for 24 hours.

## Preventive Recommendation
- Tighten inspection interval for the affected sub-assembly.
- Add 'waste_gas_temp' to the early-warning watch list with alert at 380 degC.
- Ensure spare 'Hot blast valve seat' is held in stock given lead time.