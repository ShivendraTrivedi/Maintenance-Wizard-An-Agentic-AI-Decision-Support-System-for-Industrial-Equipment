# Failure Analysis Report — HSM-M-02 — FR-20251215-003

**Asset:** HSM-M-02 (Hot Strip Mill Main Drive Motor)  
**Area:** Hot Rolling  
**Date of failure:** 2025-12-15  
**Downtime:** 2 hours  
**Fault mode:** Winding insulation breakdown  

## Event Description
Operations reported an abnormal condition on HSM-M-02. Elevated winding temperature and current spikes precede insulation failure. The parameter 'vibration_nde' deviated from its normal band (1.0–4.5 mm/s) prior to the trip.

## Root Cause
Investigation concluded the primary root cause was **aged insulation**, leading to winding insulation breakdown.

## Corrective Action Taken
- Isolated the asset per LOTO SOP.
- Replaced affected component (NDE bearing).
- Restored normal operating parameters and monitored for 24 hours.

## Preventive Recommendation
- Tighten inspection interval for the affected sub-assembly.
- Add 'vibration_nde' to the early-warning watch list with alert at 4 mm/s.
- Ensure spare 'DE bearing (SKF 6324)' is held in stock given lead time.