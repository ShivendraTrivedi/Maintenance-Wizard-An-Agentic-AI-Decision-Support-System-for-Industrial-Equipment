# Failure Analysis Report — HSM-M-04 — FR-20250222-001

**Asset:** HSM-M-04 (Hot Strip Mill Main Drive Motor)  
**Area:** Hot Rolling  
**Date of failure:** 2025-02-22  
**Downtime:** 36 hours  
**Fault mode:** Coupling misalignment  

## Event Description
Operations reported an abnormal condition on HSM-M-04. High NDE vibration with characteristic 2x running frequency. The parameter 'bearing_temperature' deviated from its normal band (45–85 degC) prior to the trip.

## Root Cause
Investigation concluded the primary root cause was **improper installation**, leading to coupling misalignment.

## Corrective Action Taken
- Isolated the asset per LOTO SOP.
- Replaced affected component (Stator winding kit).
- Restored normal operating parameters and monitored for 24 hours.

## Preventive Recommendation
- Tighten inspection interval for the affected sub-assembly.
- Add 'bearing_temperature' to the early-warning watch list with alert at 80 degC.
- Ensure spare 'NDE bearing' is held in stock given lead time.