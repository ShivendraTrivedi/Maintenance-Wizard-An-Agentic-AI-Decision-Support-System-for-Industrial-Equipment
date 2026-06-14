# Failure Analysis Report — BFS-01 — FR-20250124-001

**Asset:** BFS-01 (Blast Furnace Stove)  
**Area:** Iron Making  
**Date of failure:** 2025-01-24  
**Downtime:** 18 hours  
**Fault mode:** Hot blast valve leakage  

## Event Description
Operations reported an abnormal condition on BFS-01. Worn valve seat allows hot blast to bypass, lowering blast temperature. The parameter 'waste_gas_temp' deviated from its normal band (250–400 degC) prior to the trip.

## Root Cause
Investigation concluded the primary root cause was **inadequate cooling water**, leading to hot blast valve leakage.

## Corrective Action Taken
- Isolated the asset per LOTO SOP.
- Replaced affected component (Cooling stave).
- Restored normal operating parameters and monitored for 24 hours.

## Preventive Recommendation
- Tighten inspection interval for the affected sub-assembly.
- Add 'waste_gas_temp' to the early-warning watch list with alert at 380 degC.
- Ensure spare 'Cooling stave' is held in stock given lead time.