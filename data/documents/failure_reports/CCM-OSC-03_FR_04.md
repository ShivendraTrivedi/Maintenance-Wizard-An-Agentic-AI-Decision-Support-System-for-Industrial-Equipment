# Failure Analysis Report — CCM-OSC-03 — FR-20250727-004

**Asset:** CCM-OSC-03 (Continuous Casting Mould Oscillator)  
**Area:** Continuous Casting  
**Date of failure:** 2025-07-27  
**Downtime:** 36 hours  
**Fault mode:** Hydraulic pressure loss  

## Event Description
Operations reported an abnormal condition on CCM-OSC-03. Internal leakage reduces oscillation stroke, risking sticker breakouts. The parameter 'oil_temperature' deviated from its normal band (35–55 degC) prior to the trip.

## Root Cause
Investigation concluded the primary root cause was **accumulator pre-charge loss**, leading to hydraulic pressure loss.

## Corrective Action Taken
- Isolated the asset per LOTO SOP.
- Replaced affected component (Accumulator bladder).
- Restored normal operating parameters and monitored for 24 hours.

## Preventive Recommendation
- Tighten inspection interval for the affected sub-assembly.
- Add 'oil_temperature' to the early-warning watch list with alert at 52 degC.
- Ensure spare 'Accumulator bladder' is held in stock given lead time.