# Failure Analysis Report — RHF-WBD-04 — FR-20251208-004

**Asset:** RHF-WBD-04 (Reheating Furnace Walking Beam Drive)  
**Area:** Hot Rolling  
**Date of failure:** 2025-12-08  
**Downtime:** 18 hours  
**Fault mode:** Skid button wear  

## Event Description
Operations reported an abnormal condition on RHF-WBD-04. Worn skids cause non-uniform heating and slab marks. The parameter 'beam_position_error' deviated from its normal band (-8–8 mm) prior to the trip.

## Root Cause
Investigation concluded the primary root cause was **abrasion**, leading to skid button wear.

## Corrective Action Taken
- Isolated the asset per LOTO SOP.
- Replaced affected component (Cylinder seal kit).
- Restored normal operating parameters and monitored for 24 hours.

## Preventive Recommendation
- Tighten inspection interval for the affected sub-assembly.
- Add 'beam_position_error' to the early-warning watch list with alert at 7 mm.
- Ensure spare 'Hydraulic cooler' is held in stock given lead time.