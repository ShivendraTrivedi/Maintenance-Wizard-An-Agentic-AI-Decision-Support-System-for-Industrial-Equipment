# Equipment Manual — Coke Oven Pushing Ram (COR-02)

**Asset ID:** COR-02  
**Plant Area:** Coke Making  
**Criticality:** High  
**Manufacturer:** Primetals  
**Installed:** 2015  

## 1. Overview
The Coke Oven Pushing Ram (COR-02) is a high-criticality asset in the Coke Making area. This manual describes its monitored parameters, normal operating envelope, common fault modes, recommended maintenance schedule, troubleshooting guidance, and associated spare parts.

## 2. Monitored Parameters & Normal Operating Envelope
| Parameter | Unit | Normal Low | Normal High |
|---|---|---|---|
| ram_force | kN | 100 | 350 |
| drive_motor_current | A | 120 | 320 |
| rail_temperature | degC | 40 | 90 |
| ram_speed | m/min | 8 | 18 |

Operation outside these limits should trigger investigation. Sustained excursions indicate developing faults and should be escalated per the alerting matrix.

## 3. Common Fault Modes
### 3.1 Hard pushing / sticky oven
Abnormally high ram force indicates poor coke release.

**Typical root causes:** Under-coking, Wall carbon build-up, Inadequate oven heating, Coal blend issue.

### 3.2 Drive gearbox wear
Rising current and vibration signal gear tooth wear.

**Typical root causes:** Lubrication failure, Overload pushing, Misalignment.

### 3.3 Rail misalignment
Uneven ram travel and rail heating.

**Typical root causes:** Thermal distortion, Foundation movement, Debris on rail.

## 4. Recommended Maintenance Schedule
| Task | Interval |
|---|---|
| Visual inspection & cleaning | Weekly |
| Lubrication / fluid check | Monthly |
| Vibration & thermography survey | Quarterly |
| Condition-based overhaul | As indicated by trend / RUL |

## 5. Troubleshooting Guide
- **Symptom related to Hard pushing / sticky oven:** Check Under-coking, Wall carbon build-up. Verify readings against Section 2 limits, inspect affected sub-assembly, and replace worn spares from Section 6 if confirmed.
- **Symptom related to Drive gearbox wear:** Check Lubrication failure, Overload pushing. Verify readings against Section 2 limits, inspect affected sub-assembly, and replace worn spares from Section 6 if confirmed.
- **Symptom related to Rail misalignment:** Check Thermal distortion, Foundation movement. Verify readings against Section 2 limits, inspect affected sub-assembly, and replace worn spares from Section 6 if confirmed.

## 6. Associated Spare Parts
- Ram shoe
- Drive gearbox
- Rail clamp
- Ram chain link

## 7. Safety Notes
Always apply Lockout-Tagout (LOTO) before intervention. Confirm zero energy state. Refer to the relevant SOP before performing any maintenance task on this asset.