# Equipment Manual — Reheating Furnace Walking Beam Drive (RHF-WBD-04)

**Asset ID:** RHF-WBD-04  
**Plant Area:** Hot Rolling  
**Criticality:** High  
**Manufacturer:** SMS Group  
**Installed:** 2009  

## 1. Overview
The Reheating Furnace Walking Beam Drive (RHF-WBD-04) is a high-criticality asset in the Hot Rolling area. This manual describes its monitored parameters, normal operating envelope, common fault modes, recommended maintenance schedule, troubleshooting guidance, and associated spare parts.

## 2. Monitored Parameters & Normal Operating Envelope
| Parameter | Unit | Normal Low | Normal High |
|---|---|---|---|
| hydraulic_pressure | bar | 120 | 210 |
| beam_position_error | mm | -8 | 8 |
| oil_temperature | degC | 35 | 58 |
| cylinder_drift | mm/cycle | 0 | 3 |

Operation outside these limits should trigger investigation. Sustained excursions indicate developing faults and should be escalated per the alerting matrix.

## 3. Common Fault Modes
### 3.1 Hydraulic cylinder drift
Internal leakage causes beam position error and skid marks.

**Typical root causes:** Piston seal wear, Oil contamination, Valve leakage.

### 3.2 Skid button wear
Worn skids cause non-uniform heating and slab marks.

**Typical root causes:** Long service, Overheating, Abrasion.

### 3.3 Oil overheating
High oil temperature degrades viscosity and seals.

**Typical root causes:** Cooler fouling, Low oil level, Continuous high load.

## 4. Recommended Maintenance Schedule
| Task | Interval |
|---|---|
| Visual inspection & cleaning | Weekly |
| Lubrication / fluid check | Monthly |
| Vibration & thermography survey | Quarterly |
| Condition-based overhaul | As indicated by trend / RUL |

## 5. Troubleshooting Guide
- **Symptom related to Hydraulic cylinder drift:** Check Piston seal wear, Oil contamination. Verify readings against Section 2 limits, inspect affected sub-assembly, and replace worn spares from Section 6 if confirmed.
- **Symptom related to Skid button wear:** Check Long service, Overheating. Verify readings against Section 2 limits, inspect affected sub-assembly, and replace worn spares from Section 6 if confirmed.
- **Symptom related to Oil overheating:** Check Cooler fouling, Low oil level. Verify readings against Section 2 limits, inspect affected sub-assembly, and replace worn spares from Section 6 if confirmed.

## 6. Associated Spare Parts
- Cylinder seal kit
- Skid button
- Hydraulic cooler
- Proportional valve

## 7. Safety Notes
Always apply Lockout-Tagout (LOTO) before intervention. Confirm zero energy state. Refer to the relevant SOP before performing any maintenance task on this asset.