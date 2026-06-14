# Failure Analysis Report — HSM-M-04 — FR-20250324-004

**Asset:** HSM-M-04 (Hot Strip Mill Main Drive Motor)  
**Area:** Hot Rolling  
**Date of failure:** 2025-03-24  
**Downtime:** 6 hours  
**Fault mode:** Bearing wear / imbalance  

## Event Description
Operations reported an abnormal condition on HSM-M-04. Rising vibration and bearing temperature indicate progressive bearing degradation. The parameter 'winding_temperature' deviated from its normal band (60–110 degC) prior to the trip.

## Root Cause
Investigation concluded the primary root cause was **lubrication starvation**, leading to bearing wear / imbalance.

## Corrective Action Taken
- Isolated the asset per LOTO SOP.
- Replaced affected component (NDE bearing).
- Restored normal operating parameters and monitored for 24 hours.

## Preventive Recommendation
- Tighten inspection interval for the affected sub-assembly.
- Add 'winding_temperature' to the early-warning watch list with alert at 104 degC.
- Ensure spare 'NDE bearing' is held in stock given lead time.