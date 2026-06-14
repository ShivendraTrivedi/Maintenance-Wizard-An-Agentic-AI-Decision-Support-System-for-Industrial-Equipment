# Failure Analysis Report — HSM-M-06 — FR-20240313-002

**Asset:** HSM-M-06 (Hot Strip Mill Main Drive Motor)  
**Area:** Hot Rolling  
**Date of failure:** 2024-03-13  
**Downtime:** 6 hours  
**Fault mode:** Coupling misalignment  

## Event Description
Operations reported an abnormal condition on HSM-M-06. High NDE vibration with characteristic 2x running frequency. The parameter 'bearing_temperature' deviated from its normal band (45–85 degC) prior to the trip.

## Root Cause
Investigation concluded the primary root cause was **thermal growth**, leading to coupling misalignment.

## Corrective Action Taken
- Isolated the asset per LOTO SOP.
- Replaced affected component (Stator winding kit).
- Restored normal operating parameters and monitored for 24 hours.

## Preventive Recommendation
- Tighten inspection interval for the affected sub-assembly.
- Add 'bearing_temperature' to the early-warning watch list with alert at 80 degC.
- Ensure spare 'NDE bearing' is held in stock given lead time.