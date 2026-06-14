# Failure Analysis Report — BFS-02 — FR-20241207-003

**Asset:** BFS-02 (Blast Furnace Stove)  
**Area:** Iron Making  
**Date of failure:** 2024-12-07  
**Downtime:** 6 hours  
**Fault mode:** Hot blast valve leakage  

## Event Description
Operations reported an abnormal condition on BFS-02. Worn valve seat allows hot blast to bypass, lowering blast temperature. The parameter 'dome_temperature' deviated from its normal band (1100–1450 degC) prior to the trip.

## Root Cause
Investigation concluded the primary root cause was **inadequate cooling water**, leading to hot blast valve leakage.

## Corrective Action Taken
- Isolated the asset per LOTO SOP.
- Replaced affected component (Cooling stave).
- Restored normal operating parameters and monitored for 24 hours.

## Preventive Recommendation
- Tighten inspection interval for the affected sub-assembly.
- Add 'dome_temperature' to the early-warning watch list with alert at 1377 degC.
- Ensure spare 'Cooling stave' is held in stock given lead time.