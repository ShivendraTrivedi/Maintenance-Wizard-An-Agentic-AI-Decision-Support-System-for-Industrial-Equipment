"""Equipment knowledge base — single source of truth for asset types.

Sensor normal-bands and fault modes used by BOTH the data generator
(scripts/generate_corpus.py) and the live predictive engine
(src/core/predictive.py). Pure data, no dependencies.
"""

EQUIP_TYPES = {
    "Blast Furnace Stove": {
        "area": "Iron Making",
        "criticality": "Critical",
        "sensors": [
            ("dome_temperature", "degC", 1100, 1450),
            ("waste_gas_temp", "degC", 250, 400),
            ("combustion_air_flow", "Nm3/h", 40000, 60000),
            ("shell_temperature", "degC", 60, 120),
        ],
        "faults": [
            ("Checker brick degradation", "Thermal cycling fatigue and dust deposition reduce heat-transfer efficiency.",
             ["Excessive thermal cycling", "Poor gas cleaning upstream", "Overdue checker inspection"]),
            ("Hot blast valve leakage", "Worn valve seat allows hot blast to bypass, lowering blast temperature.",
             ["Seat erosion", "Inadequate cooling water", "Refractory spalling"]),
            ("Shell hot-spot", "Localised refractory loss raises shell temperature with risk of breakthrough.",
             ["Refractory wear", "Cooling stave blockage", "Scaffold formation"]),
        ],
        "spares": ["Checker bricks (silica)", "Hot blast valve seat", "Cooling stave", "Burner nozzle"],
    },
    "Hot Strip Mill Main Drive Motor": {
        "area": "Hot Rolling",
        "criticality": "Critical",
        "sensors": [
            ("winding_temperature", "degC", 60, 110),
            ("vibration_de", "mm/s", 1.0, 4.5),
            ("vibration_nde", "mm/s", 1.0, 4.5),
            ("bearing_temperature", "degC", 45, 85),
            ("motor_current", "A", 800, 1600),
        ],
        "faults": [
            ("Bearing wear / imbalance", "Rising vibration and bearing temperature indicate progressive bearing degradation.",
             ["Lubrication starvation", "Misalignment", "Contaminated grease", "Excess load cycling"]),
            ("Winding insulation breakdown", "Elevated winding temperature and current spikes precede insulation failure.",
             ["Overheating", "Moisture ingress", "Voltage transients", "Aged insulation"]),
            ("Coupling misalignment", "High NDE vibration with characteristic 2x running frequency.",
             ["Foundation settling", "Improper installation", "Thermal growth"]),
        ],
        "spares": ["DE bearing (SKF 6324)", "NDE bearing", "Stator winding kit", "Flexible coupling element"],
    },
    "Continuous Casting Mould Oscillator": {
        "area": "Continuous Casting",
        "criticality": "Critical",
        "sensors": [
            ("oscillation_frequency", "cpm", 80, 220),
            ("hydraulic_pressure", "bar", 90, 160),
            ("mould_level_dev", "mm", -5, 5),
            ("oil_temperature", "degC", 35, 55),
        ],
        "faults": [
            ("Hydraulic pressure loss", "Internal leakage reduces oscillation stroke, risking sticker breakouts.",
             ["Seal wear", "Contaminated oil", "Pump degradation", "Accumulator pre-charge loss"]),
            ("Mould level instability", "Level sensor drift or clogging causes oscillation control hunting.",
             ["Sensor fouling", "SEN clogging", "Argon flow imbalance"]),
            ("Servo valve sticking", "Valve hysteresis degrades oscillation waveform fidelity.",
             ["Oil contamination", "Wear", "Temperature drift"]),
        ],
        "spares": ["Servo valve", "Hydraulic seal kit", "Accumulator bladder", "Mould level sensor"],
    },
    "Coke Oven Pushing Ram": {
        "area": "Coke Making",
        "criticality": "High",
        "sensors": [
            ("ram_force", "kN", 100, 350),
            ("drive_motor_current", "A", 120, 320),
            ("rail_temperature", "degC", 40, 90),
            ("ram_speed", "m/min", 8, 18),
        ],
        "faults": [
            ("Hard pushing / sticky oven", "Abnormally high ram force indicates poor coke release.",
             ["Under-coking", "Wall carbon build-up", "Inadequate oven heating", "Coal blend issue"]),
            ("Drive gearbox wear", "Rising current and vibration signal gear tooth wear.",
             ["Lubrication failure", "Overload pushing", "Misalignment"]),
            ("Rail misalignment", "Uneven ram travel and rail heating.",
             ["Thermal distortion", "Foundation movement", "Debris on rail"]),
        ],
        "spares": ["Ram shoe", "Drive gearbox", "Rail clamp", "Ram chain link"],
    },
    "Sinter Plant ID Fan": {
        "area": "Sinter Making",
        "criticality": "High",
        "sensors": [
            ("vibration", "mm/s", 1.0, 6.0),
            ("bearing_temperature", "degC", 40, 80),
            ("motor_current", "A", 200, 480),
            ("inlet_pressure", "mmWC", -1200, -700),
        ],
        "faults": [
            ("Impeller dust build-up / imbalance", "Dust accretion on impeller raises vibration and unbalance.",
             ["Inadequate gas cleaning", "High dust load", "Missed cleaning cycle"]),
            ("Impeller erosion", "Abrasive dust thins blades, shifting balance over time.",
             ["High particulate", "Long service hours", "Wrong blade material"]),
            ("Bearing failure", "Bearing temperature and vibration rise sharply before seizure.",
             ["Lube starvation", "Water ingress", "Overheating"]),
        ],
        "spares": ["Fan impeller", "Plummer block bearing", "Wear liner", "Coupling"],
    },
    "BOF Lance Hoist": {
        "area": "Steel Making",
        "criticality": "Critical",
        "sensors": [
            ("hoist_motor_current", "A", 60, 200),
            ("rope_tension", "kN", 20, 80),
            ("brake_temperature", "degC", 30, 75),
            ("lance_cooling_flow", "m3/h", 120, 200),
        ],
        "faults": [
            ("Cooling water flow drop", "Reduced lance cooling risks lance burn-through during blow.",
             ["Pump cavitation", "Strainer blockage", "Valve fault", "Scale build-up"]),
            ("Wire rope degradation", "Broken wires and tension irregularity threaten lance drop.",
             ["Fatigue", "Corrosion", "Overload", "Sheave wear"]),
            ("Brake fade", "Rising brake temperature reduces holding capacity.",
             ["Worn brake pads", "Hydraulic leak", "Misadjustment"]),
        ],
        "spares": ["Wire rope", "Brake pad set", "Cooling water pump", "Sheave wheel"],
    },
    "Reheating Furnace Walking Beam Drive": {
        "area": "Hot Rolling",
        "criticality": "High",
        "sensors": [
            ("hydraulic_pressure", "bar", 120, 210),
            ("beam_position_error", "mm", -8, 8),
            ("oil_temperature", "degC", 35, 58),
            ("cylinder_drift", "mm/cycle", 0, 3),
        ],
        "faults": [
            ("Hydraulic cylinder drift", "Internal leakage causes beam position error and skid marks.",
             ["Piston seal wear", "Oil contamination", "Valve leakage"]),
            ("Skid button wear", "Worn skids cause non-uniform heating and slab marks.",
             ["Long service", "Overheating", "Abrasion"]),
            ("Oil overheating", "High oil temperature degrades viscosity and seals.",
             ["Cooler fouling", "Low oil level", "Continuous high load"]),
        ],
        "spares": ["Cylinder seal kit", "Skid button", "Hydraulic cooler", "Proportional valve"],
    },
    "Cooling Water Pump": {
        "area": "Utilities",
        "criticality": "Medium",
        "sensors": [
            ("discharge_pressure", "bar", 4, 9),
            ("flow_rate", "m3/h", 300, 700),
            ("bearing_temperature", "degC", 40, 80),
            ("vibration", "mm/s", 0.8, 4.5),
            ("motor_current", "A", 80, 220),
        ],
        "faults": [
            ("Cavitation", "Low suction head causes pressure pulsation and impeller pitting.",
             ["Clogged suction strainer", "Low sump level", "Air ingress"]),
            ("Mechanical seal leak", "Seal failure causes leakage and bearing contamination.",
             ["Seal face wear", "Dry running", "Misalignment"]),
            ("Impeller wear", "Reduced flow and pressure from worn impeller clearances.",
             ["Abrasive water", "Long service", "Erosion"]),
        ],
        "spares": ["Mechanical seal", "Pump impeller", "Bearing set", "Wear ring"],
    },
}
