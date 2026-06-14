# Failure Analysis Report — SP-IDF-01 — FR-20240623-001

**Asset:** SP-IDF-01 (Sinter Plant ID Fan)  
**Area:** Sinter Making  
**Date of failure:** 2024-06-23  
**Downtime:** 6 hours  
**Fault mode:** Impeller dust build-up / imbalance  

## Event Description
Operations reported an abnormal condition on SP-IDF-01. Dust accretion on impeller raises vibration and unbalance. The parameter 'motor_current' deviated from its normal band (200–480 A) prior to the trip.

## Root Cause
Investigation concluded the primary root cause was **missed cleaning cycle**, leading to impeller dust build-up / imbalance.

## Corrective Action Taken
- Isolated the asset per LOTO SOP.
- Replaced affected component (Fan impeller).
- Restored normal operating parameters and monitored for 24 hours.

## Preventive Recommendation
- Tighten inspection interval for the affected sub-assembly.
- Add 'motor_current' to the early-warning watch list with alert at 456 A.
- Ensure spare 'Wear liner' is held in stock given lead time.