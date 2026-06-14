# Failure Analysis Report — CCM-OSC-05 — FR-20250413-002

**Asset:** CCM-OSC-05 (Continuous Casting Mould Oscillator)  
**Area:** Continuous Casting  
**Date of failure:** 2025-04-13  
**Downtime:** 4 hours  
**Fault mode:** Mould level instability  

## Event Description
Operations reported an abnormal condition on CCM-OSC-05. Level sensor drift or clogging causes oscillation control hunting. The parameter 'hydraulic_pressure' deviated from its normal band (90–160 bar) prior to the trip.

## Root Cause
Investigation concluded the primary root cause was **sensor fouling**, leading to mould level instability.

## Corrective Action Taken
- Isolated the asset per LOTO SOP.
- Replaced affected component (Hydraulic seal kit).
- Restored normal operating parameters and monitored for 24 hours.

## Preventive Recommendation
- Tighten inspection interval for the affected sub-assembly.
- Add 'hydraulic_pressure' to the early-warning watch list with alert at 152 bar.
- Ensure spare 'Accumulator bladder' is held in stock given lead time.