# Failure Analysis Report — HSM-M-05 — FR-20240705-002

**Asset:** HSM-M-05 (Hot Strip Mill Main Drive Motor)  
**Area:** Hot Rolling  
**Date of failure:** 2024-07-05  
**Downtime:** 36 hours  
**Fault mode:** Winding insulation breakdown  

## Event Description
Operations reported an abnormal condition on HSM-M-05. Elevated winding temperature and current spikes precede insulation failure. The parameter 'winding_temperature' deviated from its normal band (60–110 degC) prior to the trip.

## Root Cause
Investigation concluded the primary root cause was **aged insulation**, leading to winding insulation breakdown.

## Corrective Action Taken
- Isolated the asset per LOTO SOP.
- Replaced affected component (NDE bearing).
- Restored normal operating parameters and monitored for 24 hours.

## Preventive Recommendation
- Tighten inspection interval for the affected sub-assembly.
- Add 'winding_temperature' to the early-warning watch list with alert at 104 degC.
- Ensure spare 'DE bearing (SKF 6324)' is held in stock given lead time.