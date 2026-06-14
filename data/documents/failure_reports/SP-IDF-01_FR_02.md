# Failure Analysis Report — SP-IDF-01 — FR-20250227-002

**Asset:** SP-IDF-01 (Sinter Plant ID Fan)  
**Area:** Sinter Making  
**Date of failure:** 2025-02-27  
**Downtime:** 12 hours  
**Fault mode:** Bearing failure  

## Event Description
Operations reported an abnormal condition on SP-IDF-01. Bearing temperature and vibration rise sharply before seizure. The parameter 'inlet_pressure' deviated from its normal band (-1200–-700 mmWC) prior to the trip.

## Root Cause
Investigation concluded the primary root cause was **water ingress**, leading to bearing failure.

## Corrective Action Taken
- Isolated the asset per LOTO SOP.
- Replaced affected component (Fan impeller).
- Restored normal operating parameters and monitored for 24 hours.

## Preventive Recommendation
- Tighten inspection interval for the affected sub-assembly.
- Add 'inlet_pressure' to the early-warning watch list with alert at -665 mmWC.
- Ensure spare 'Plummer block bearing' is held in stock given lead time.