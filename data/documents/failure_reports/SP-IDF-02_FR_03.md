# Failure Analysis Report — SP-IDF-02 — FR-20241017-003

**Asset:** SP-IDF-02 (Sinter Plant ID Fan)  
**Area:** Sinter Making  
**Date of failure:** 2024-10-17  
**Downtime:** 36 hours  
**Fault mode:** Bearing failure  

## Event Description
Operations reported an abnormal condition on SP-IDF-02. Bearing temperature and vibration rise sharply before seizure. The parameter 'bearing_temperature' deviated from its normal band (40–80 degC) prior to the trip.

## Root Cause
Investigation concluded the primary root cause was **water ingress**, leading to bearing failure.

## Corrective Action Taken
- Isolated the asset per LOTO SOP.
- Replaced affected component (Coupling).
- Restored normal operating parameters and monitored for 24 hours.

## Preventive Recommendation
- Tighten inspection interval for the affected sub-assembly.
- Add 'bearing_temperature' to the early-warning watch list with alert at 76 degC.
- Ensure spare 'Coupling' is held in stock given lead time.