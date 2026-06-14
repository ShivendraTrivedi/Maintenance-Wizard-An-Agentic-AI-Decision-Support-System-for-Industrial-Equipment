# Failure Analysis Report — HSM-M-02 — FR-20251221-001

**Asset:** HSM-M-02 (Hot Strip Mill Main Drive Motor)  
**Area:** Hot Rolling  
**Date of failure:** 2025-12-21  
**Downtime:** 24 hours  
**Fault mode:** Bearing wear / imbalance  

## Event Description
Operations reported an abnormal condition on HSM-M-02. Rising vibration and bearing temperature indicate progressive bearing degradation. The parameter 'winding_temperature' deviated from its normal band (60–110 degC) prior to the trip.

## Root Cause
Investigation concluded the primary root cause was **misalignment**, leading to bearing wear / imbalance.

## Corrective Action Taken
- Isolated the asset per LOTO SOP.
- Replaced affected component (DE bearing (SKF 6324)).
- Restored normal operating parameters and monitored for 24 hours.

## Preventive Recommendation
- Tighten inspection interval for the affected sub-assembly.
- Add 'winding_temperature' to the early-warning watch list with alert at 104 degC.
- Ensure spare 'Flexible coupling element' is held in stock given lead time.