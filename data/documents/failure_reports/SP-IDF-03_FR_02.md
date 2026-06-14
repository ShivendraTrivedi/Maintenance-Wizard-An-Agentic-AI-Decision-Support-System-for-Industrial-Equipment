# Failure Analysis Report — SP-IDF-03 — FR-20241210-002

**Asset:** SP-IDF-03 (Sinter Plant ID Fan)  
**Area:** Sinter Making  
**Date of failure:** 2024-12-10  
**Downtime:** 2 hours  
**Fault mode:** Impeller erosion  

## Event Description
Operations reported an abnormal condition on SP-IDF-03. Abrasive dust thins blades, shifting balance over time. The parameter 'motor_current' deviated from its normal band (200–480 A) prior to the trip.

## Root Cause
Investigation concluded the primary root cause was **long service hours**, leading to impeller erosion.

## Corrective Action Taken
- Isolated the asset per LOTO SOP.
- Replaced affected component (Fan impeller).
- Restored normal operating parameters and monitored for 24 hours.

## Preventive Recommendation
- Tighten inspection interval for the affected sub-assembly.
- Add 'motor_current' to the early-warning watch list with alert at 456 A.
- Ensure spare 'Fan impeller' is held in stock given lead time.