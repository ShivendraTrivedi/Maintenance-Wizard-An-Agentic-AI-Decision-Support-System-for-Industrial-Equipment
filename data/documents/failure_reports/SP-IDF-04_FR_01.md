# Failure Analysis Report — SP-IDF-04 — FR-20251009-001

**Asset:** SP-IDF-04 (Sinter Plant ID Fan)  
**Area:** Sinter Making  
**Date of failure:** 2025-10-09  
**Downtime:** 8 hours  
**Fault mode:** Impeller dust build-up / imbalance  

## Event Description
Operations reported an abnormal condition on SP-IDF-04. Dust accretion on impeller raises vibration and unbalance. The parameter 'motor_current' deviated from its normal band (200–480 A) prior to the trip.

## Root Cause
Investigation concluded the primary root cause was **high dust load**, leading to impeller dust build-up / imbalance.

## Corrective Action Taken
- Isolated the asset per LOTO SOP.
- Replaced affected component (Coupling).
- Restored normal operating parameters and monitored for 24 hours.

## Preventive Recommendation
- Tighten inspection interval for the affected sub-assembly.
- Add 'motor_current' to the early-warning watch list with alert at 456 A.
- Ensure spare 'Fan impeller' is held in stock given lead time.