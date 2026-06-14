# Equipment Manual — Blast Furnace Stove (BFS-04)

**Asset ID:** BFS-04  
**Plant Area:** Iron Making  
**Criticality:** Critical  
**Manufacturer:** ABB  
**Installed:** 2011  

## 1. Overview
The Blast Furnace Stove (BFS-04) is a critical-criticality asset in the Iron Making area. This manual describes its monitored parameters, normal operating envelope, common fault modes, recommended maintenance schedule, troubleshooting guidance, and associated spare parts.

## 2. Monitored Parameters & Normal Operating Envelope
| Parameter | Unit | Normal Low | Normal High |
|---|---|---|---|
| dome_temperature | degC | 1100 | 1450 |
| waste_gas_temp | degC | 250 | 400 |
| combustion_air_flow | Nm3/h | 40000 | 60000 |
| shell_temperature | degC | 60 | 120 |

Operation outside these limits should trigger investigation. Sustained excursions indicate developing faults and should be escalated per the alerting matrix.

## 3. Common Fault Modes
### 3.1 Checker brick degradation
Thermal cycling fatigue and dust deposition reduce heat-transfer efficiency.

**Typical root causes:** Excessive thermal cycling, Poor gas cleaning upstream, Overdue checker inspection.

### 3.2 Hot blast valve leakage
Worn valve seat allows hot blast to bypass, lowering blast temperature.

**Typical root causes:** Seat erosion, Inadequate cooling water, Refractory spalling.

### 3.3 Shell hot-spot
Localised refractory loss raises shell temperature with risk of breakthrough.

**Typical root causes:** Refractory wear, Cooling stave blockage, Scaffold formation.

## 4. Recommended Maintenance Schedule
| Task | Interval |
|---|---|
| Visual inspection & cleaning | Weekly |
| Lubrication / fluid check | Monthly |
| Vibration & thermography survey | Quarterly |
| Condition-based overhaul | As indicated by trend / RUL |

## 5. Troubleshooting Guide
- **Symptom related to Checker brick degradation:** Check Excessive thermal cycling, Poor gas cleaning upstream. Verify readings against Section 2 limits, inspect affected sub-assembly, and replace worn spares from Section 6 if confirmed.
- **Symptom related to Hot blast valve leakage:** Check Seat erosion, Inadequate cooling water. Verify readings against Section 2 limits, inspect affected sub-assembly, and replace worn spares from Section 6 if confirmed.
- **Symptom related to Shell hot-spot:** Check Refractory wear, Cooling stave blockage. Verify readings against Section 2 limits, inspect affected sub-assembly, and replace worn spares from Section 6 if confirmed.

## 6. Associated Spare Parts
- Checker bricks (silica)
- Hot blast valve seat
- Cooling stave
- Burner nozzle

## 7. Safety Notes
Always apply Lockout-Tagout (LOTO) before intervention. Confirm zero energy state. Refer to the relevant SOP before performing any maintenance task on this asset.