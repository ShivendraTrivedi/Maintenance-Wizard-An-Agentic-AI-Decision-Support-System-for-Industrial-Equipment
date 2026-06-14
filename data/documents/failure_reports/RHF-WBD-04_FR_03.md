# Failure Analysis Report — RHF-WBD-04 — FR-20240428-003

**Asset:** RHF-WBD-04 (Reheating Furnace Walking Beam Drive)  
**Area:** Hot Rolling  
**Date of failure:** 2024-04-28  
**Downtime:** 6 hours  
**Fault mode:** Hydraulic cylinder drift  

## Event Description
Operations reported an abnormal condition on RHF-WBD-04. Internal leakage causes beam position error and skid marks. The parameter 'hydraulic_pressure' deviated from its normal band (120–210 bar) prior to the trip.

## Root Cause
Investigation concluded the primary root cause was **valve leakage**, leading to hydraulic cylinder drift.

## Corrective Action Taken
- Isolated the asset per LOTO SOP.
- Replaced affected component (Skid button).
- Restored normal operating parameters and monitored for 24 hours.

## Preventive Recommendation
- Tighten inspection interval for the affected sub-assembly.
- Add 'hydraulic_pressure' to the early-warning watch list with alert at 199 bar.
- Ensure spare 'Proportional valve' is held in stock given lead time.