# Failure Analysis Report — CCM-OSC-04 — FR-20250205-004

**Asset:** CCM-OSC-04 (Continuous Casting Mould Oscillator)  
**Area:** Continuous Casting  
**Date of failure:** 2025-02-05  
**Downtime:** 36 hours  
**Fault mode:** Mould level instability  

## Event Description
Operations reported an abnormal condition on CCM-OSC-04. Level sensor drift or clogging causes oscillation control hunting. The parameter 'mould_level_dev' deviated from its normal band (-5–5 mm) prior to the trip.

## Root Cause
Investigation concluded the primary root cause was **sen clogging**, leading to mould level instability.

## Corrective Action Taken
- Isolated the asset per LOTO SOP.
- Replaced affected component (Hydraulic seal kit).
- Restored normal operating parameters and monitored for 24 hours.

## Preventive Recommendation
- Tighten inspection interval for the affected sub-assembly.
- Add 'mould_level_dev' to the early-warning watch list with alert at 4 mm.
- Ensure spare 'Hydraulic seal kit' is held in stock given lead time.