# Failure Analysis Report — BOF-LH-02 — FR-20250523-002

**Asset:** BOF-LH-02 (BOF Lance Hoist)  
**Area:** Steel Making  
**Date of failure:** 2025-05-23  
**Downtime:** 6 hours  
**Fault mode:** Cooling water flow drop  

## Event Description
Operations reported an abnormal condition on BOF-LH-02. Reduced lance cooling risks lance burn-through during blow. The parameter 'lance_cooling_flow' deviated from its normal band (120–200 m3/h) prior to the trip.

## Root Cause
Investigation concluded the primary root cause was **strainer blockage**, leading to cooling water flow drop.

## Corrective Action Taken
- Isolated the asset per LOTO SOP.
- Replaced affected component (Cooling water pump).
- Restored normal operating parameters and monitored for 24 hours.

## Preventive Recommendation
- Tighten inspection interval for the affected sub-assembly.
- Add 'lance_cooling_flow' to the early-warning watch list with alert at 190 m3/h.
- Ensure spare 'Wire rope' is held in stock given lead time.