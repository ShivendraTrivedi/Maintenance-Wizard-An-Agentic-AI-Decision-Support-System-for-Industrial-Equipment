# Failure Analysis Report — BOF-LH-01 — FR-20240607-001

**Asset:** BOF-LH-01 (BOF Lance Hoist)  
**Area:** Steel Making  
**Date of failure:** 2024-06-07  
**Downtime:** 36 hours  
**Fault mode:** Wire rope degradation  

## Event Description
Operations reported an abnormal condition on BOF-LH-01. Broken wires and tension irregularity threaten lance drop. The parameter 'hoist_motor_current' deviated from its normal band (60–200 A) prior to the trip.

## Root Cause
Investigation concluded the primary root cause was **overload**, leading to wire rope degradation.

## Corrective Action Taken
- Isolated the asset per LOTO SOP.
- Replaced affected component (Cooling water pump).
- Restored normal operating parameters and monitored for 24 hours.

## Preventive Recommendation
- Tighten inspection interval for the affected sub-assembly.
- Add 'hoist_motor_current' to the early-warning watch list with alert at 190 A.
- Ensure spare 'Sheave wheel' is held in stock given lead time.