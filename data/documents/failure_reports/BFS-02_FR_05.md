# Failure Analysis Report — BFS-02 — FR-20250131-005

**Asset:** BFS-02 (Blast Furnace Stove)  
**Area:** Iron Making  
**Date of failure:** 2025-01-31  
**Downtime:** 12 hours  
**Fault mode:** Checker brick degradation  

## Event Description
Operations reported an abnormal condition on BFS-02. Thermal cycling fatigue and dust deposition reduce heat-transfer efficiency. The parameter 'waste_gas_temp' deviated from its normal band (250–400 degC) prior to the trip.

## Root Cause
Investigation concluded the primary root cause was **overdue checker inspection**, leading to checker brick degradation.

## Corrective Action Taken
- Isolated the asset per LOTO SOP.
- Replaced affected component (Hot blast valve seat).
- Restored normal operating parameters and monitored for 24 hours.

## Preventive Recommendation
- Tighten inspection interval for the affected sub-assembly.
- Add 'waste_gas_temp' to the early-warning watch list with alert at 380 degC.
- Ensure spare 'Cooling stave' is held in stock given lead time.