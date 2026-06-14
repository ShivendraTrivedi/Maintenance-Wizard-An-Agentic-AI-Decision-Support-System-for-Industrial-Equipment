# Failure Analysis Report — BOF-LH-03 — FR-20250210-002

**Asset:** BOF-LH-03 (BOF Lance Hoist)  
**Area:** Steel Making  
**Date of failure:** 2025-02-10  
**Downtime:** 36 hours  
**Fault mode:** Wire rope degradation  

## Event Description
Operations reported an abnormal condition on BOF-LH-03. Broken wires and tension irregularity threaten lance drop. The parameter 'lance_cooling_flow' deviated from its normal band (120–200 m3/h) prior to the trip.

## Root Cause
Investigation concluded the primary root cause was **overload**, leading to wire rope degradation.

## Corrective Action Taken
- Isolated the asset per LOTO SOP.
- Replaced affected component (Sheave wheel).
- Restored normal operating parameters and monitored for 24 hours.

## Preventive Recommendation
- Tighten inspection interval for the affected sub-assembly.
- Add 'lance_cooling_flow' to the early-warning watch list with alert at 190 m3/h.
- Ensure spare 'Cooling water pump' is held in stock given lead time.