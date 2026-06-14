# Equipment Manual — Continuous Casting Mould Oscillator (CCM-OSC-02)

**Asset ID:** CCM-OSC-02  
**Plant Area:** Continuous Casting  
**Criticality:** Critical  
**Manufacturer:** Siemens  
**Installed:** 2017  

## 1. Overview
The Continuous Casting Mould Oscillator (CCM-OSC-02) is a critical-criticality asset in the Continuous Casting area. This manual describes its monitored parameters, normal operating envelope, common fault modes, recommended maintenance schedule, troubleshooting guidance, and associated spare parts.

## 2. Monitored Parameters & Normal Operating Envelope
| Parameter | Unit | Normal Low | Normal High |
|---|---|---|---|
| oscillation_frequency | cpm | 80 | 220 |
| hydraulic_pressure | bar | 90 | 160 |
| mould_level_dev | mm | -5 | 5 |
| oil_temperature | degC | 35 | 55 |

Operation outside these limits should trigger investigation. Sustained excursions indicate developing faults and should be escalated per the alerting matrix.

## 3. Common Fault Modes
### 3.1 Hydraulic pressure loss
Internal leakage reduces oscillation stroke, risking sticker breakouts.

**Typical root causes:** Seal wear, Contaminated oil, Pump degradation, Accumulator pre-charge loss.

### 3.2 Mould level instability
Level sensor drift or clogging causes oscillation control hunting.

**Typical root causes:** Sensor fouling, SEN clogging, Argon flow imbalance.

### 3.3 Servo valve sticking
Valve hysteresis degrades oscillation waveform fidelity.

**Typical root causes:** Oil contamination, Wear, Temperature drift.

## 4. Recommended Maintenance Schedule
| Task | Interval |
|---|---|
| Visual inspection & cleaning | Weekly |
| Lubrication / fluid check | Monthly |
| Vibration & thermography survey | Quarterly |
| Condition-based overhaul | As indicated by trend / RUL |

## 5. Troubleshooting Guide
- **Symptom related to Hydraulic pressure loss:** Check Seal wear, Contaminated oil. Verify readings against Section 2 limits, inspect affected sub-assembly, and replace worn spares from Section 6 if confirmed.
- **Symptom related to Mould level instability:** Check Sensor fouling, SEN clogging. Verify readings against Section 2 limits, inspect affected sub-assembly, and replace worn spares from Section 6 if confirmed.
- **Symptom related to Servo valve sticking:** Check Oil contamination, Wear. Verify readings against Section 2 limits, inspect affected sub-assembly, and replace worn spares from Section 6 if confirmed.

## 6. Associated Spare Parts
- Servo valve
- Hydraulic seal kit
- Accumulator bladder
- Mould level sensor

## 7. Safety Notes
Always apply Lockout-Tagout (LOTO) before intervention. Confirm zero energy state. Refer to the relevant SOP before performing any maintenance task on this asset.