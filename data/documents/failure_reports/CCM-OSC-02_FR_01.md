# Failure Analysis Report — CCM-OSC-02 — FR-20250605-001

**Asset:** CCM-OSC-02 (Continuous Casting Mould Oscillator)  
**Area:** Continuous Casting  
**Date of failure:** 2025-06-05  
**Downtime:** 18 hours  
**Fault mode:** Servo valve sticking  

## Event Description
Operations reported an abnormal condition on CCM-OSC-02. Valve hysteresis degrades oscillation waveform fidelity. The parameter 'oil_temperature' deviated from its normal band (35–55 degC) prior to the trip.

## Root Cause
Investigation concluded the primary root cause was **wear**, leading to servo valve sticking.

## Corrective Action Taken
- Isolated the asset per LOTO SOP.
- Replaced affected component (Servo valve).
- Restored normal operating parameters and monitored for 24 hours.

## Preventive Recommendation
- Tighten inspection interval for the affected sub-assembly.
- Add 'oil_temperature' to the early-warning watch list with alert at 52 degC.
- Ensure spare 'Accumulator bladder' is held in stock given lead time.