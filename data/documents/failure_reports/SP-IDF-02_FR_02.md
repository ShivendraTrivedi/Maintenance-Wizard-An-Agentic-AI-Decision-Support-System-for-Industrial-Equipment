# Failure Analysis Report — SP-IDF-02 — FR-20251027-002

**Asset:** SP-IDF-02 (Sinter Plant ID Fan)  
**Area:** Sinter Making  
**Date of failure:** 2025-10-27  
**Downtime:** 12 hours  
**Fault mode:** Bearing failure  

## Event Description
Operations reported an abnormal condition on SP-IDF-02. Bearing temperature and vibration rise sharply before seizure. The parameter 'bearing_temperature' deviated from its normal band (40–80 degC) prior to the trip.

## Root Cause
Investigation concluded the primary root cause was **overheating**, leading to bearing failure.

## Corrective Action Taken
- Isolated the asset per LOTO SOP.
- Replaced affected component (Wear liner).
- Restored normal operating parameters and monitored for 24 hours.

## Preventive Recommendation
- Tighten inspection interval for the affected sub-assembly.
- Add 'bearing_temperature' to the early-warning watch list with alert at 76 degC.
- Ensure spare 'Plummer block bearing' is held in stock given lead time.