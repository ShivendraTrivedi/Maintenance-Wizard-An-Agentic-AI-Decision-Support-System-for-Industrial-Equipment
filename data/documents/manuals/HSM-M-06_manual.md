# Equipment Manual — Hot Strip Mill Main Drive Motor (HSM-M-06)

**Asset ID:** HSM-M-06  
**Plant Area:** Hot Rolling  
**Criticality:** Critical  
**Manufacturer:** ABB  
**Installed:** 2009  

## 1. Overview
The Hot Strip Mill Main Drive Motor (HSM-M-06) is a critical-criticality asset in the Hot Rolling area. This manual describes its monitored parameters, normal operating envelope, common fault modes, recommended maintenance schedule, troubleshooting guidance, and associated spare parts.

## 2. Monitored Parameters & Normal Operating Envelope
| Parameter | Unit | Normal Low | Normal High |
|---|---|---|---|
| winding_temperature | degC | 60 | 110 |
| vibration_de | mm/s | 1.0 | 4.5 |
| vibration_nde | mm/s | 1.0 | 4.5 |
| bearing_temperature | degC | 45 | 85 |
| motor_current | A | 800 | 1600 |

Operation outside these limits should trigger investigation. Sustained excursions indicate developing faults and should be escalated per the alerting matrix.

## 3. Common Fault Modes
### 3.1 Bearing wear / imbalance
Rising vibration and bearing temperature indicate progressive bearing degradation.

**Typical root causes:** Lubrication starvation, Misalignment, Contaminated grease, Excess load cycling.

### 3.2 Winding insulation breakdown
Elevated winding temperature and current spikes precede insulation failure.

**Typical root causes:** Overheating, Moisture ingress, Voltage transients, Aged insulation.

### 3.3 Coupling misalignment
High NDE vibration with characteristic 2x running frequency.

**Typical root causes:** Foundation settling, Improper installation, Thermal growth.

## 4. Recommended Maintenance Schedule
| Task | Interval |
|---|---|
| Visual inspection & cleaning | Weekly |
| Lubrication / fluid check | Monthly |
| Vibration & thermography survey | Quarterly |
| Condition-based overhaul | As indicated by trend / RUL |

## 5. Troubleshooting Guide
- **Symptom related to Bearing wear / imbalance:** Check Lubrication starvation, Misalignment. Verify readings against Section 2 limits, inspect affected sub-assembly, and replace worn spares from Section 6 if confirmed.
- **Symptom related to Winding insulation breakdown:** Check Overheating, Moisture ingress. Verify readings against Section 2 limits, inspect affected sub-assembly, and replace worn spares from Section 6 if confirmed.
- **Symptom related to Coupling misalignment:** Check Foundation settling, Improper installation. Verify readings against Section 2 limits, inspect affected sub-assembly, and replace worn spares from Section 6 if confirmed.

## 6. Associated Spare Parts
- DE bearing (SKF 6324)
- NDE bearing
- Stator winding kit
- Flexible coupling element

## 7. Safety Notes
Always apply Lockout-Tagout (LOTO) before intervention. Confirm zero energy state. Refer to the relevant SOP before performing any maintenance task on this asset.