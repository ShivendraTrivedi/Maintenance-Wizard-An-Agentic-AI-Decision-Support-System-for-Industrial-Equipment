# Failure Analysis Report — CCM-OSC-02 — FR-20250130-002

**Asset:** CCM-OSC-02 (Continuous Casting Mould Oscillator)  
**Area:** Continuous Casting  
**Date of failure:** 2025-01-30  
**Downtime:** 12 hours  
**Fault mode:** Servo valve sticking  

## Event Description
Operations reported an abnormal condition on CCM-OSC-02. Valve hysteresis degrades oscillation waveform fidelity. The parameter 'mould_level_dev' deviated from its normal band (-5–5 mm) prior to the trip.

## Root Cause
Investigation concluded the primary root cause was **wear**, leading to servo valve sticking.

## Corrective Action Taken
- Isolated the asset per LOTO SOP.
- Replaced affected component (Accumulator bladder).
- Restored normal operating parameters and monitored for 24 hours.

## Preventive Recommendation
- Tighten inspection interval for the affected sub-assembly.
- Add 'mould_level_dev' to the early-warning watch list with alert at 4 mm.
- Ensure spare 'Mould level sensor' is held in stock given lead time.