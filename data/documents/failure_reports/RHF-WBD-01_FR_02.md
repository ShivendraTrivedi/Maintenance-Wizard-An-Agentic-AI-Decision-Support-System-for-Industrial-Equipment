# Failure Analysis Report — RHF-WBD-01 — FR-20240419-002

**Asset:** RHF-WBD-01 (Reheating Furnace Walking Beam Drive)  
**Area:** Hot Rolling  
**Date of failure:** 2024-04-19  
**Downtime:** 24 hours  
**Fault mode:** Skid button wear  

## Event Description
Operations reported an abnormal condition on RHF-WBD-01. Worn skids cause non-uniform heating and slab marks. The parameter 'beam_position_error' deviated from its normal band (-8–8 mm) prior to the trip.

## Root Cause
Investigation concluded the primary root cause was **long service**, leading to skid button wear.

## Corrective Action Taken
- Isolated the asset per LOTO SOP.
- Replaced affected component (Hydraulic cooler).
- Restored normal operating parameters and monitored for 24 hours.

## Preventive Recommendation
- Tighten inspection interval for the affected sub-assembly.
- Add 'beam_position_error' to the early-warning watch list with alert at 7 mm.
- Ensure spare 'Cylinder seal kit' is held in stock given lead time.