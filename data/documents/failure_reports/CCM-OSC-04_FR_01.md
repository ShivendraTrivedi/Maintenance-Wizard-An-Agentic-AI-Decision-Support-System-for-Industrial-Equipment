# Failure Analysis Report — CCM-OSC-04 — FR-20250121-001

**Asset:** CCM-OSC-04 (Continuous Casting Mould Oscillator)  
**Area:** Continuous Casting  
**Date of failure:** 2025-01-21  
**Downtime:** 2 hours  
**Fault mode:** Mould level instability  

## Event Description
Operations reported an abnormal condition on CCM-OSC-04. Level sensor drift or clogging causes oscillation control hunting. The parameter 'oil_temperature' deviated from its normal band (35–55 degC) prior to the trip.

## Root Cause
Investigation concluded the primary root cause was **argon flow imbalance**, leading to mould level instability.

## Corrective Action Taken
- Isolated the asset per LOTO SOP.
- Replaced affected component (Accumulator bladder).
- Restored normal operating parameters and monitored for 24 hours.

## Preventive Recommendation
- Tighten inspection interval for the affected sub-assembly.
- Add 'oil_temperature' to the early-warning watch list with alert at 52 degC.
- Ensure spare 'Servo valve' is held in stock given lead time.