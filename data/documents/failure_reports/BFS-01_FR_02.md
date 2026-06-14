# Failure Analysis Report — BFS-01 — FR-20240802-002

**Asset:** BFS-01 (Blast Furnace Stove)  
**Area:** Iron Making  
**Date of failure:** 2024-08-02  
**Downtime:** 4 hours  
**Fault mode:** Shell hot-spot  

## Event Description
Operations reported an abnormal condition on BFS-01. Localised refractory loss raises shell temperature with risk of breakthrough. The parameter 'waste_gas_temp' deviated from its normal band (250–400 degC) prior to the trip.

## Root Cause
Investigation concluded the primary root cause was **cooling stave blockage**, leading to shell hot-spot.

## Corrective Action Taken
- Isolated the asset per LOTO SOP.
- Replaced affected component (Hot blast valve seat).
- Restored normal operating parameters and monitored for 24 hours.

## Preventive Recommendation
- Tighten inspection interval for the affected sub-assembly.
- Add 'waste_gas_temp' to the early-warning watch list with alert at 380 degC.
- Ensure spare 'Hot blast valve seat' is held in stock given lead time.