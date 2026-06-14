# Failure Analysis Report — SP-IDF-03 — FR-20250221-003

**Asset:** SP-IDF-03 (Sinter Plant ID Fan)  
**Area:** Sinter Making  
**Date of failure:** 2025-02-21  
**Downtime:** 6 hours  
**Fault mode:** Impeller dust build-up / imbalance  

## Event Description
Operations reported an abnormal condition on SP-IDF-03. Dust accretion on impeller raises vibration and unbalance. The parameter 'bearing_temperature' deviated from its normal band (40–80 degC) prior to the trip.

## Root Cause
Investigation concluded the primary root cause was **missed cleaning cycle**, leading to impeller dust build-up / imbalance.

## Corrective Action Taken
- Isolated the asset per LOTO SOP.
- Replaced affected component (Plummer block bearing).
- Restored normal operating parameters and monitored for 24 hours.

## Preventive Recommendation
- Tighten inspection interval for the affected sub-assembly.
- Add 'bearing_temperature' to the early-warning watch list with alert at 76 degC.
- Ensure spare 'Plummer block bearing' is held in stock given lead time.