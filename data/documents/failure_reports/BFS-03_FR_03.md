# Failure Analysis Report — BFS-03 — FR-20260210-003

**Asset:** BFS-03 (Blast Furnace Stove)  
**Area:** Iron Making  
**Date of failure:** 2026-02-10  
**Downtime:** 4 hours  
**Fault mode:** Hot blast valve leakage  

## Event Description
Operations reported an abnormal condition on BFS-03. Worn valve seat allows hot blast to bypass, lowering blast temperature. The parameter 'combustion_air_flow' deviated from its normal band (40000–60000 Nm3/h) prior to the trip.

## Root Cause
Investigation concluded the primary root cause was **inadequate cooling water**, leading to hot blast valve leakage.

## Corrective Action Taken
- Isolated the asset per LOTO SOP.
- Replaced affected component (Burner nozzle).
- Restored normal operating parameters and monitored for 24 hours.

## Preventive Recommendation
- Tighten inspection interval for the affected sub-assembly.
- Add 'combustion_air_flow' to the early-warning watch list with alert at 57000 Nm3/h.
- Ensure spare 'Checker bricks (silica)' is held in stock given lead time.