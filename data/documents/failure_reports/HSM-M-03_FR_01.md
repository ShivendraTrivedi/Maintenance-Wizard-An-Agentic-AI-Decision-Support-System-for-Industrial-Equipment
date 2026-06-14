# Failure Analysis Report — HSM-M-03 — FR-20241111-001

**Asset:** HSM-M-03 (Hot Strip Mill Main Drive Motor)  
**Area:** Hot Rolling  
**Date of failure:** 2024-11-11  
**Downtime:** 8 hours  
**Fault mode:** Winding insulation breakdown  

## Event Description
Operations reported an abnormal condition on HSM-M-03. Elevated winding temperature and current spikes precede insulation failure. The parameter 'bearing_temperature' deviated from its normal band (45–85 degC) prior to the trip.

## Root Cause
Investigation concluded the primary root cause was **moisture ingress**, leading to winding insulation breakdown.

## Corrective Action Taken
- Isolated the asset per LOTO SOP.
- Replaced affected component (Stator winding kit).
- Restored normal operating parameters and monitored for 24 hours.

## Preventive Recommendation
- Tighten inspection interval for the affected sub-assembly.
- Add 'bearing_temperature' to the early-warning watch list with alert at 80 degC.
- Ensure spare 'Flexible coupling element' is held in stock given lead time.