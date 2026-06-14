# Equipment Manual — Cooling Water Pump (CWP-04)

**Asset ID:** CWP-04  
**Plant Area:** Utilities  
**Criticality:** Medium  
**Manufacturer:** ABB  
**Installed:** 2017  

## 1. Overview
The Cooling Water Pump (CWP-04) is a medium-criticality asset in the Utilities area. This manual describes its monitored parameters, normal operating envelope, common fault modes, recommended maintenance schedule, troubleshooting guidance, and associated spare parts.

## 2. Monitored Parameters & Normal Operating Envelope
| Parameter | Unit | Normal Low | Normal High |
|---|---|---|---|
| discharge_pressure | bar | 4 | 9 |
| flow_rate | m3/h | 300 | 700 |
| bearing_temperature | degC | 40 | 80 |
| vibration | mm/s | 0.8 | 4.5 |
| motor_current | A | 80 | 220 |

Operation outside these limits should trigger investigation. Sustained excursions indicate developing faults and should be escalated per the alerting matrix.

## 3. Common Fault Modes
### 3.1 Cavitation
Low suction head causes pressure pulsation and impeller pitting.

**Typical root causes:** Clogged suction strainer, Low sump level, Air ingress.

### 3.2 Mechanical seal leak
Seal failure causes leakage and bearing contamination.

**Typical root causes:** Seal face wear, Dry running, Misalignment.

### 3.3 Impeller wear
Reduced flow and pressure from worn impeller clearances.

**Typical root causes:** Abrasive water, Long service, Erosion.

## 4. Recommended Maintenance Schedule
| Task | Interval |
|---|---|
| Visual inspection & cleaning | Weekly |
| Lubrication / fluid check | Monthly |
| Vibration & thermography survey | Quarterly |
| Condition-based overhaul | As indicated by trend / RUL |

## 5. Troubleshooting Guide
- **Symptom related to Cavitation:** Check Clogged suction strainer, Low sump level. Verify readings against Section 2 limits, inspect affected sub-assembly, and replace worn spares from Section 6 if confirmed.
- **Symptom related to Mechanical seal leak:** Check Seal face wear, Dry running. Verify readings against Section 2 limits, inspect affected sub-assembly, and replace worn spares from Section 6 if confirmed.
- **Symptom related to Impeller wear:** Check Abrasive water, Long service. Verify readings against Section 2 limits, inspect affected sub-assembly, and replace worn spares from Section 6 if confirmed.

## 6. Associated Spare Parts
- Mechanical seal
- Pump impeller
- Bearing set
- Wear ring

## 7. Safety Notes
Always apply Lockout-Tagout (LOTO) before intervention. Confirm zero energy state. Refer to the relevant SOP before performing any maintenance task on this asset.