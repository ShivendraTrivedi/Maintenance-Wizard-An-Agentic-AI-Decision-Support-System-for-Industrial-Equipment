# Failure Analysis Report — HSM-M-05 — FR-20260216-004

**Asset:** HSM-M-05 (Hot Strip Mill Main Drive Motor)  
**Area:** Hot Rolling  
**Date of failure:** 2026-02-16  
**Downtime:** 8 hours  
**Fault mode:** Bearing wear / imbalance  

## Event Description
Operations reported an abnormal condition on HSM-M-05. Rising vibration and bearing temperature indicate progressive bearing degradation. The parameter 'bearing_temperature' deviated from its normal band (45–85 degC) prior to the trip.

## Root Cause
Investigation concluded the primary root cause was **lubrication starvation**, leading to bearing wear / imbalance.

## Corrective Action Taken
- Isolated the asset per LOTO SOP.
- Replaced affected component (Flexible coupling element).
- Restored normal operating parameters and monitored for 24 hours.

## Preventive Recommendation
- Tighten inspection interval for the affected sub-assembly.
- Add 'bearing_temperature' to the early-warning watch list with alert at 80 degC.
- Ensure spare 'NDE bearing' is held in stock given lead time.