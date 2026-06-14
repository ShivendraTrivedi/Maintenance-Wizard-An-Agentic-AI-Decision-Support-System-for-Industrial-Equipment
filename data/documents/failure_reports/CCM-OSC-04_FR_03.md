# Failure Analysis Report — CCM-OSC-04 — FR-20251028-003

**Asset:** CCM-OSC-04 (Continuous Casting Mould Oscillator)  
**Area:** Continuous Casting  
**Date of failure:** 2025-10-28  
**Downtime:** 36 hours  
**Fault mode:** Hydraulic pressure loss  

## Event Description
Operations reported an abnormal condition on CCM-OSC-04. Internal leakage reduces oscillation stroke, risking sticker breakouts. The parameter 'oscillation_frequency' deviated from its normal band (80–220 cpm) prior to the trip.

## Root Cause
Investigation concluded the primary root cause was **seal wear**, leading to hydraulic pressure loss.

## Corrective Action Taken
- Isolated the asset per LOTO SOP.
- Replaced affected component (Mould level sensor).
- Restored normal operating parameters and monitored for 24 hours.

## Preventive Recommendation
- Tighten inspection interval for the affected sub-assembly.
- Add 'oscillation_frequency' to the early-warning watch list with alert at 209 cpm.
- Ensure spare 'Hydraulic seal kit' is held in stock given lead time.