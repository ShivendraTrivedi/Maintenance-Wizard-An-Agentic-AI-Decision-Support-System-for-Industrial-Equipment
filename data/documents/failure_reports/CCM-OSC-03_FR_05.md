# Failure Analysis Report — CCM-OSC-03 — FR-20250517-005

**Asset:** CCM-OSC-03 (Continuous Casting Mould Oscillator)  
**Area:** Continuous Casting  
**Date of failure:** 2025-05-17  
**Downtime:** 12 hours  
**Fault mode:** Hydraulic pressure loss  

## Event Description
Operations reported an abnormal condition on CCM-OSC-03. Internal leakage reduces oscillation stroke, risking sticker breakouts. The parameter 'mould_level_dev' deviated from its normal band (-5–5 mm) prior to the trip.

## Root Cause
Investigation concluded the primary root cause was **contaminated oil**, leading to hydraulic pressure loss.

## Corrective Action Taken
- Isolated the asset per LOTO SOP.
- Replaced affected component (Mould level sensor).
- Restored normal operating parameters and monitored for 24 hours.

## Preventive Recommendation
- Tighten inspection interval for the affected sub-assembly.
- Add 'mould_level_dev' to the early-warning watch list with alert at 4 mm.
- Ensure spare 'Servo valve' is held in stock given lead time.