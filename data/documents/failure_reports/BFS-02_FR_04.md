# Failure Analysis Report — BFS-02 — FR-20241229-004

**Asset:** BFS-02 (Blast Furnace Stove)  
**Area:** Iron Making  
**Date of failure:** 2024-12-29  
**Downtime:** 8 hours  
**Fault mode:** Shell hot-spot  

## Event Description
Operations reported an abnormal condition on BFS-02. Localised refractory loss raises shell temperature with risk of breakthrough. The parameter 'combustion_air_flow' deviated from its normal band (40000–60000 Nm3/h) prior to the trip.

## Root Cause
Investigation concluded the primary root cause was **cooling stave blockage**, leading to shell hot-spot.

## Corrective Action Taken
- Isolated the asset per LOTO SOP.
- Replaced affected component (Checker bricks (silica)).
- Restored normal operating parameters and monitored for 24 hours.

## Preventive Recommendation
- Tighten inspection interval for the affected sub-assembly.
- Add 'combustion_air_flow' to the early-warning watch list with alert at 57000 Nm3/h.
- Ensure spare 'Cooling stave' is held in stock given lead time.