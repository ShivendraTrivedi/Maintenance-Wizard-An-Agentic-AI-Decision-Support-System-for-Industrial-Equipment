# Failure Analysis Report — SP-IDF-04 — FR-20240412-002

**Asset:** SP-IDF-04 (Sinter Plant ID Fan)  
**Area:** Sinter Making  
**Date of failure:** 2024-04-12  
**Downtime:** 4 hours  
**Fault mode:** Impeller erosion  

## Event Description
Operations reported an abnormal condition on SP-IDF-04. Abrasive dust thins blades, shifting balance over time. The parameter 'inlet_pressure' deviated from its normal band (-1200–-700 mmWC) prior to the trip.

## Root Cause
Investigation concluded the primary root cause was **wrong blade material**, leading to impeller erosion.

## Corrective Action Taken
- Isolated the asset per LOTO SOP.
- Replaced affected component (Plummer block bearing).
- Restored normal operating parameters and monitored for 24 hours.

## Preventive Recommendation
- Tighten inspection interval for the affected sub-assembly.
- Add 'inlet_pressure' to the early-warning watch list with alert at -665 mmWC.
- Ensure spare 'Plummer block bearing' is held in stock given lead time.