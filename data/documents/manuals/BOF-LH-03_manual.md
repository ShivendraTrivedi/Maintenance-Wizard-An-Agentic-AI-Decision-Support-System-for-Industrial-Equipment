# Equipment Manual — BOF Lance Hoist (BOF-LH-03)

**Asset ID:** BOF-LH-03  
**Plant Area:** Steel Making  
**Criticality:** Critical  
**Manufacturer:** Danieli  
**Installed:** 2013  

## 1. Overview
The BOF Lance Hoist (BOF-LH-03) is a critical-criticality asset in the Steel Making area. This manual describes its monitored parameters, normal operating envelope, common fault modes, recommended maintenance schedule, troubleshooting guidance, and associated spare parts.

## 2. Monitored Parameters & Normal Operating Envelope
| Parameter | Unit | Normal Low | Normal High |
|---|---|---|---|
| hoist_motor_current | A | 60 | 200 |
| rope_tension | kN | 20 | 80 |
| brake_temperature | degC | 30 | 75 |
| lance_cooling_flow | m3/h | 120 | 200 |

Operation outside these limits should trigger investigation. Sustained excursions indicate developing faults and should be escalated per the alerting matrix.

## 3. Common Fault Modes
### 3.1 Cooling water flow drop
Reduced lance cooling risks lance burn-through during blow.

**Typical root causes:** Pump cavitation, Strainer blockage, Valve fault, Scale build-up.

### 3.2 Wire rope degradation
Broken wires and tension irregularity threaten lance drop.

**Typical root causes:** Fatigue, Corrosion, Overload, Sheave wear.

### 3.3 Brake fade
Rising brake temperature reduces holding capacity.

**Typical root causes:** Worn brake pads, Hydraulic leak, Misadjustment.

## 4. Recommended Maintenance Schedule
| Task | Interval |
|---|---|
| Visual inspection & cleaning | Weekly |
| Lubrication / fluid check | Monthly |
| Vibration & thermography survey | Quarterly |
| Condition-based overhaul | As indicated by trend / RUL |

## 5. Troubleshooting Guide
- **Symptom related to Cooling water flow drop:** Check Pump cavitation, Strainer blockage. Verify readings against Section 2 limits, inspect affected sub-assembly, and replace worn spares from Section 6 if confirmed.
- **Symptom related to Wire rope degradation:** Check Fatigue, Corrosion. Verify readings against Section 2 limits, inspect affected sub-assembly, and replace worn spares from Section 6 if confirmed.
- **Symptom related to Brake fade:** Check Worn brake pads, Hydraulic leak. Verify readings against Section 2 limits, inspect affected sub-assembly, and replace worn spares from Section 6 if confirmed.

## 6. Associated Spare Parts
- Wire rope
- Brake pad set
- Cooling water pump
- Sheave wheel

## 7. Safety Notes
Always apply Lockout-Tagout (LOTO) before intervention. Confirm zero energy state. Refer to the relevant SOP before performing any maintenance task on this asset.