# Failure Analysis Report — RHF-WBD-02 — FR-20240717-003

**Asset:** RHF-WBD-02 (Reheating Furnace Walking Beam Drive)  
**Area:** Hot Rolling  
**Date of failure:** 2024-07-17  
**Downtime:** 36 hours  
**Fault mode:** Hydraulic cylinder drift  

## Event Description
Operations reported an abnormal condition on RHF-WBD-02. Internal leakage causes beam position error and skid marks. The parameter 'oil_temperature' deviated from its normal band (35–58 degC) prior to the trip.

## Root Cause
Investigation concluded the primary root cause was **valve leakage**, leading to hydraulic cylinder drift.

## Corrective Action Taken
- Isolated the asset per LOTO SOP.
- Replaced affected component (Hydraulic cooler).
- Restored normal operating parameters and monitored for 24 hours.

## Preventive Recommendation
- Tighten inspection interval for the affected sub-assembly.
- Add 'oil_temperature' to the early-warning watch list with alert at 55 degC.
- Ensure spare 'Hydraulic cooler' is held in stock given lead time.