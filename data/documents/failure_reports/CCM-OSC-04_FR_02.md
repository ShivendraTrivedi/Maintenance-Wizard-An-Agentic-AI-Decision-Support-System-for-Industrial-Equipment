# Failure Analysis Report — CCM-OSC-04 — FR-20260211-002

**Asset:** CCM-OSC-04 (Continuous Casting Mould Oscillator)  
**Area:** Continuous Casting  
**Date of failure:** 2026-02-11  
**Downtime:** 24 hours  
**Fault mode:** Mould level instability  

## Event Description
Operations reported an abnormal condition on CCM-OSC-04. Level sensor drift or clogging causes oscillation control hunting. The parameter 'oscillation_frequency' deviated from its normal band (80–220 cpm) prior to the trip.

## Root Cause
Investigation concluded the primary root cause was **sensor fouling**, leading to mould level instability.

## Corrective Action Taken
- Isolated the asset per LOTO SOP.
- Replaced affected component (Hydraulic seal kit).
- Restored normal operating parameters and monitored for 24 hours.

## Preventive Recommendation
- Tighten inspection interval for the affected sub-assembly.
- Add 'oscillation_frequency' to the early-warning watch list with alert at 209 cpm.
- Ensure spare 'Servo valve' is held in stock given lead time.