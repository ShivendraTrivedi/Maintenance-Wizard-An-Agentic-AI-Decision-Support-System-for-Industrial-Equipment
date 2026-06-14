# Failure Analysis Report — HSM-M-04 — FR-20250729-003

**Asset:** HSM-M-04 (Hot Strip Mill Main Drive Motor)  
**Area:** Hot Rolling  
**Date of failure:** 2025-07-29  
**Downtime:** 24 hours  
**Fault mode:** Winding insulation breakdown  

## Event Description
Operations reported an abnormal condition on HSM-M-04. Elevated winding temperature and current spikes precede insulation failure. The parameter 'winding_temperature' deviated from its normal band (60–110 degC) prior to the trip.

## Root Cause
Investigation concluded the primary root cause was **moisture ingress**, leading to winding insulation breakdown.

## Corrective Action Taken
- Isolated the asset per LOTO SOP.
- Replaced affected component (Flexible coupling element).
- Restored normal operating parameters and monitored for 24 hours.

## Preventive Recommendation
- Tighten inspection interval for the affected sub-assembly.
- Add 'winding_temperature' to the early-warning watch list with alert at 104 degC.
- Ensure spare 'DE bearing (SKF 6324)' is held in stock given lead time.