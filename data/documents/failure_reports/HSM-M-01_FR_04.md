# Failure Analysis Report — HSM-M-01 — FR-20251110-004

**Asset:** HSM-M-01 (Hot Strip Mill Main Drive Motor)  
**Area:** Hot Rolling  
**Date of failure:** 2025-11-10  
**Downtime:** 18 hours  
**Fault mode:** Winding insulation breakdown  

## Event Description
Operations reported an abnormal condition on HSM-M-01. Elevated winding temperature and current spikes precede insulation failure. The parameter 'winding_temperature' deviated from its normal band (60–110 degC) prior to the trip.

## Root Cause
Investigation concluded the primary root cause was **overheating**, leading to winding insulation breakdown.

## Corrective Action Taken
- Isolated the asset per LOTO SOP.
- Replaced affected component (NDE bearing).
- Restored normal operating parameters and monitored for 24 hours.

## Preventive Recommendation
- Tighten inspection interval for the affected sub-assembly.
- Add 'winding_temperature' to the early-warning watch list with alert at 104 degC.
- Ensure spare 'NDE bearing' is held in stock given lead time.