# Failure Analysis Report — SP-IDF-01 — FR-20250217-003

**Asset:** SP-IDF-01 (Sinter Plant ID Fan)  
**Area:** Sinter Making  
**Date of failure:** 2025-02-17  
**Downtime:** 24 hours  
**Fault mode:** Bearing failure  

## Event Description
Operations reported an abnormal condition on SP-IDF-01. Bearing temperature and vibration rise sharply before seizure. The parameter 'motor_current' deviated from its normal band (200–480 A) prior to the trip.

## Root Cause
Investigation concluded the primary root cause was **overheating**, leading to bearing failure.

## Corrective Action Taken
- Isolated the asset per LOTO SOP.
- Replaced affected component (Plummer block bearing).
- Restored normal operating parameters and monitored for 24 hours.

## Preventive Recommendation
- Tighten inspection interval for the affected sub-assembly.
- Add 'motor_current' to the early-warning watch list with alert at 456 A.
- Ensure spare 'Coupling' is held in stock given lead time.