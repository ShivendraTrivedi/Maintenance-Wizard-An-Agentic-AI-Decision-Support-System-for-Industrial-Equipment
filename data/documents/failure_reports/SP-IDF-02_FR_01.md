# Failure Analysis Report — SP-IDF-02 — FR-20250513-001

**Asset:** SP-IDF-02 (Sinter Plant ID Fan)  
**Area:** Sinter Making  
**Date of failure:** 2025-05-13  
**Downtime:** 2 hours  
**Fault mode:** Impeller erosion  

## Event Description
Operations reported an abnormal condition on SP-IDF-02. Abrasive dust thins blades, shifting balance over time. The parameter 'motor_current' deviated from its normal band (200–480 A) prior to the trip.

## Root Cause
Investigation concluded the primary root cause was **high particulate**, leading to impeller erosion.

## Corrective Action Taken
- Isolated the asset per LOTO SOP.
- Replaced affected component (Coupling).
- Restored normal operating parameters and monitored for 24 hours.

## Preventive Recommendation
- Tighten inspection interval for the affected sub-assembly.
- Add 'motor_current' to the early-warning watch list with alert at 456 A.
- Ensure spare 'Wear liner' is held in stock given lead time.