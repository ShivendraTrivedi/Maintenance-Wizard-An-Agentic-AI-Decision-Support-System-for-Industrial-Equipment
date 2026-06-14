# Failure Analysis Report — BFS-03 — FR-20240312-002

**Asset:** BFS-03 (Blast Furnace Stove)  
**Area:** Iron Making  
**Date of failure:** 2024-03-12  
**Downtime:** 24 hours  
**Fault mode:** Hot blast valve leakage  

## Event Description
Operations reported an abnormal condition on BFS-03. Worn valve seat allows hot blast to bypass, lowering blast temperature. The parameter 'combustion_air_flow' deviated from its normal band (40000–60000 Nm3/h) prior to the trip.

## Root Cause
Investigation concluded the primary root cause was **seat erosion**, leading to hot blast valve leakage.

## Corrective Action Taken
- Isolated the asset per LOTO SOP.
- Replaced affected component (Cooling stave).
- Restored normal operating parameters and monitored for 24 hours.

## Preventive Recommendation
- Tighten inspection interval for the affected sub-assembly.
- Add 'combustion_air_flow' to the early-warning watch list with alert at 57000 Nm3/h.
- Ensure spare 'Cooling stave' is held in stock given lead time.