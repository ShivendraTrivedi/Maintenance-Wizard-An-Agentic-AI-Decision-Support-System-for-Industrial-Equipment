# Failure Analysis Report — CCM-OSC-03 — FR-20250319-001

**Asset:** CCM-OSC-03 (Continuous Casting Mould Oscillator)  
**Area:** Continuous Casting  
**Date of failure:** 2025-03-19  
**Downtime:** 6 hours  
**Fault mode:** Mould level instability  

## Event Description
Operations reported an abnormal condition on CCM-OSC-03. Level sensor drift or clogging causes oscillation control hunting. The parameter 'hydraulic_pressure' deviated from its normal band (90–160 bar) prior to the trip.

## Root Cause
Investigation concluded the primary root cause was **argon flow imbalance**, leading to mould level instability.

## Corrective Action Taken
- Isolated the asset per LOTO SOP.
- Replaced affected component (Servo valve).
- Restored normal operating parameters and monitored for 24 hours.

## Preventive Recommendation
- Tighten inspection interval for the affected sub-assembly.
- Add 'hydraulic_pressure' to the early-warning watch list with alert at 152 bar.
- Ensure spare 'Mould level sensor' is held in stock given lead time.