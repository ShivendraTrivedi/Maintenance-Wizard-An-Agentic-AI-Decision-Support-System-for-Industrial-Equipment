# Failure Analysis Report — CCM-OSC-01 — FR-20240202-004

**Asset:** CCM-OSC-01 (Continuous Casting Mould Oscillator)  
**Area:** Continuous Casting  
**Date of failure:** 2024-02-02  
**Downtime:** 12 hours  
**Fault mode:** Hydraulic pressure loss  

## Event Description
Operations reported an abnormal condition on CCM-OSC-01. Internal leakage reduces oscillation stroke, risking sticker breakouts. The parameter 'mould_level_dev' deviated from its normal band (-5–5 mm) prior to the trip.

## Root Cause
Investigation concluded the primary root cause was **accumulator pre-charge loss**, leading to hydraulic pressure loss.

## Corrective Action Taken
- Isolated the asset per LOTO SOP.
- Replaced affected component (Servo valve).
- Restored normal operating parameters and monitored for 24 hours.

## Preventive Recommendation
- Tighten inspection interval for the affected sub-assembly.
- Add 'mould_level_dev' to the early-warning watch list with alert at 4 mm.
- Ensure spare 'Hydraulic seal kit' is held in stock given lead time.