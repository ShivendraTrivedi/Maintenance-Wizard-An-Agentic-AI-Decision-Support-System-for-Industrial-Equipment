# Failure Analysis Report — HSM-M-01 — FR-20251111-003

**Asset:** HSM-M-01 (Hot Strip Mill Main Drive Motor)  
**Area:** Hot Rolling  
**Date of failure:** 2025-11-11  
**Downtime:** 24 hours  
**Fault mode:** Bearing wear / imbalance  

## Event Description
Operations reported an abnormal condition on HSM-M-01. Rising vibration and bearing temperature indicate progressive bearing degradation. The parameter 'bearing_temperature' deviated from its normal band (45–85 degC) prior to the trip.

## Root Cause
Investigation concluded the primary root cause was **lubrication starvation**, leading to bearing wear / imbalance.

## Corrective Action Taken
- Isolated the asset per LOTO SOP.
- Replaced affected component (DE bearing (SKF 6324)).
- Restored normal operating parameters and monitored for 24 hours.

## Preventive Recommendation
- Tighten inspection interval for the affected sub-assembly.
- Add 'bearing_temperature' to the early-warning watch list with alert at 80 degC.
- Ensure spare 'Stator winding kit' is held in stock given lead time.