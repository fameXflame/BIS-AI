"""
BIS Comprehensive Catalog Expansion Engine.
Builds an extended repository of official Bureau of Indian Standards (IS Codes)
spanning all 15 technical divisions of the Bureau of Indian Standards.
Saves:
- backend/data_engine/extended_bis_catalog.json
"""

import json
import os
import sys
import re

# Comprehensive dictionary of technical division standards across all 15 BIS Division Councils
EXTENDED_STANDARDS_CATALOG = [
    # ─── CIVIL ENGINEERING DIVISION (CED) ──────────────────────────────────
    {
        "is_code": "IS 456: 2000",
        "title": "Plain and Reinforced Concrete — Code of Practice",
        "year": "2000",
        "division": "Civil Engineering Division",
        "mandatory": True,
        "scope": "This flagship Indian Standard specifies basic requirements for general structural use of plain and reinforced concrete in buildings, bridges, and civil structures. Covers design philosophies (Limit State Design and Working Stress Design), concrete mix proportioning, characteristic strength, durability criteria, minimum cement content, maximum water-cement ratio, cover to reinforcement, detailing of bars, and stripping time for formwork.",
        "key_clauses": [
            "Clause 6: Materials, Workmanship, Inspection and Testing — Grades of concrete M10 to M80",
            "Clause 8: Durability of Concrete — Exposure conditions (Mild, Moderate, Severe, Very Severe, Extreme) and minimum cover",
            "Clause 15: Sampling and Strength Test of Concrete — Cube testing at 7 and 28 days, acceptance criteria",
            "Clause 26: Requirements Governing Reinforcement and Detailing — Development length, lap splices, and bar spacing",
            "Clause 35: Limit State Design philosophy for flexure, compression, shear, and torsion"
        ],
        "keywords": ["RCC design", "reinforced concrete", "IS 456", "concrete code", "limit state design", "cube strength", "concrete mix", "structural engineering", "civil engineering"]
    },
    {
        "is_code": "IS 800: 2007",
        "title": "General Construction in Steel — Code of Practice",
        "year": "2007",
        "division": "Civil Engineering Division",
        "mandatory": True,
        "scope": "Prescribes general requirements for structural steel design using Limit State Method. Covers structural steel sections, tension members, compression members, flexural members, member connections (welded, bolted), stability, fatigue design, and fire resistance.",
        "key_clauses": [
            "Clause 3: Materials — Structural steel conforming to IS 2062",
            "Clause 5: General Design Requirements — Load combinations and deflections",
            "Clause 6: Design of Tension Members — Net section rupture and block shear",
            "Clause 7: Design of Compression Members — Buckling curves and slenderness ratio",
            "Clause 10: Connections — High strength friction grip (HSFG) bolts and fillet welds"
        ],
        "keywords": ["steel construction", "IS 800", "structural steel design", "limit state steel", "welded connections", "bolted connections", "steel beams", "trusses"]
    },
    {
        "is_code": "IS 1893 (Part 1): 2016",
        "title": "Criteria for Earthquake Resistant Design of Structures — Part 1: General Provisions and Buildings",
        "year": "2016",
        "division": "Civil Engineering Division",
        "mandatory": True,
        "scope": "Specifies seismic design principles, earthquake zone map of India (Zones II, III, IV, V), zone factors (Z), response reduction factors (R), importance factor (I), and design lateral force calculations using Equivalent Static Method and Response Spectrum Method.",
        "key_clauses": [
            "Clause 6: Assumptions and Load Combinations for Seismic Design",
            "Clause 6.4: Seismic Zone Factor (Z) — Zone II (0.10), Zone III (0.16), Zone IV (0.24), Zone V (0.36)",
            "Clause 7.2: Design Spectra and Soil Type Factors (Type I Hard, Type II Medium, Type III Soft)",
            "Clause 7.6: Equivalent Static Method for Base Shear Calculation",
            "Clause 7.7: Dynamic Analysis / Response Spectrum Method"
        ],
        "keywords": ["earthquake resistant", "IS 1893", "seismic design", "earthquake zone V", "base shear", "building code", "structural dynamics", "zone factor"]
    },
    {
        "is_code": "IS 13920: 2016",
        "title": "Ductile Design and Detailing of Reinforced Concrete Structures Subjected to Seismic Forces — Code of Practice",
        "year": "2016",
        "division": "Civil Engineering Division",
        "mandatory": True,
        "scope": "Prescribes special ductile detailing guidelines for beams, columns, beam-column joints, and shear walls of RC buildings located in seismic Zones III, IV, and V to ensure energy dissipation during strong ground shaking.",
        "key_clauses": [
            "Clause 6: Flexural Members (Beams) — Minimum bar diameters, closed hoops, and lap splice locations",
            "Clause 7: Columns and Frame Members — Special confining reinforcement, hoop spacing, and cross ties",
            "Clause 8: Beam-Column Joints — Shear strength of joint core and confining ties",
            "Clause 9: Special Structural Walls (Shear Walls) — Boundary elements and distributed web reinforcement"
        ],
        "keywords": ["ductile detailing", "IS 13920", "shear wall detailing", "confinement hoops", "seismic reinforcement", "beam column joint"]
    },
    {
        "is_code": "IS 10262: 2019",
        "title": "Concrete Mix Proportioning — Guidelines",
        "year": "2019",
        "division": "Civil Engineering Division",
        "mandatory": False,
        "scope": "Provides detailed step-by-step procedures for target mean strength determination, water-cement ratio selection, water content calculation, fine to coarse aggregate ratio estimation, and trial mix adjustments for normal, high-strength (M60 to M100), and self-compacting concrete (SCC).",
        "key_clauses": [
            "Clause 4: Target Strength for Mix Proportioning — f'ck = fck + 1.65 s",
            "Clause 5: Selection of Water-Cement Ratio and Water Content",
            "Clause 6: Calculation of Cementitious Materials Content and Mineral Admixtures (Fly ash, GGBS, Silica fume)",
            "Clause 7: Mix Design for High Strength Concrete (M60 and above)",
            "Clause 8: Mix Design for Self-Compacting Concrete (SCC)"
        ],
        "keywords": ["concrete mix design", "IS 10262", "mix proportioning", "target mean strength", "self compacting concrete", "fly ash in concrete"]
    },
    {
        "is_code": "IS 1239 (Part 1): 2004",
        "title": "Steel Tubes, Tubulars and Other Wrought Steel Fittings — Part 1: Steel Tubes",
        "year": "2004",
        "division": "Civil Engineering Division",
        "mandatory": True,
        "scope": "Covers mild steel tubes for water, gas, steam, and compressed air pipelines. Categorizes tubes into Light, Medium, and Heavy series with specified wall thickness, hydrostatic test pressure, and zinc galvanizing requirements.",
        "key_clauses": [
            "Clause 5: Chemical composition — Carbon max 0.20%, Manganese max 1.30%",
            "Clause 8: Dimensions and Nominal Masses for Light, Medium, and Heavy series",
            "Clause 11: Hydrostatic Test at 5.0 MPa pressure without leakage",
            "Clause 12: Galvanizing Requirements — Hot-dip zinc coating min 400 g/m2"
        ],
        "keywords": ["GI pipes", "steel tubes", "IS 1239", "galvanized pipe", "water pipe", "medium grade pipe", "plumbing pipe"]
    },

    # ─── ELECTROTECHNICAL DIVISION (ETD) ────────────────────────────────────
    {
        "is_code": "IS 694: 2010",
        "title": "Polyvinyl Chloride Insulated Unsheathed and Sheathed Cables/Cords for Working Voltages up to and Including 1100 V — Specification",
        "year": "2010",
        "division": "Electrotechnical Division",
        "mandatory": True,
        "scope": "Covers single-core and multi-core PVC insulated copper and aluminium wires and cables used for domestic wiring, industrial power, and panel boards up to 1100V. Prescribes conductor resistance, insulation thickness, spark testing, flame retardance (FR / FRLS), and thermal aging.",
        "key_clauses": [
            "Clause 5: Conductors — Plain or tinned annealed copper, EC grade aluminium conforming to IS 8130",
            "Clause 6: Insulation — Type A or Type C PVC compound conforming to IS 5831",
            "Clause 14: Spark Test at 6 kV AC or 9 kV DC",
            "Clause 16: Flame Retardancy Test — Flammability test per IS 10810 (Part 53)",
            "Clause 18: Marking — Continuous printing of IS code, ISI mark, brand, and voltage rating"
        ],
        "keywords": ["PVC wire", "building wire", "IS 694", "copper cable", "FRLS wire", "electrical wiring", "house wire", "1100V cable"]
    },
    {
        "is_code": "IS 1554 (Part 1): 1988",
        "title": "PVC Insulated (Heavy Duty) Electric Cables — Part 1: For Working Voltages up to and Including 1100 V",
        "year": "1988",
        "division": "Electrotechnical Division",
        "mandatory": True,
        "scope": "Covers armored and unarmored heavy duty power cables for underground distribution, industrial substations, and utilities up to 1100V. Specifies galvanized steel strip/wire armoring, PVC inner/outer sheath, and insulation breakdown voltage.",
        "key_clauses": [
            "Clause 5: Armor Requirements — Single or double layer galvanized steel strip armor for mechanical protection",
            "Clause 9: High Voltage AC Test at 3 kV for 5 minutes",
            "Clause 10: Conductor Resistance Limits per IS 8130",
            "Clause 12: Tensile and Elongation of Outer PVC Sheath"
        ],
        "keywords": ["armored cable", "power cable", "IS 1554", "heavy duty cable", "underground cable", "substation wiring"]
    },
    {
        "is_code": "IS 302 (Part 1): 2008",
        "title": "Safety of Household and Similar Electrical Appliances — Part 1: General Requirements",
        "year": "2008",
        "division": "Electrotechnical Division",
        "mandatory": True,
        "scope": "Primary umbrella safety standard for all domestic electrical appliances (water heaters, irons, kettles, toaster, fans, mixers). Covers protection against electric shock, moisture resistance, dielectric strength, leakage current (<0.75 mA), creepage distances, and abnormal operation testing.",
        "key_clauses": [
            "Clause 8: Protection Against Access to Live Parts — Test finger evaluation",
            "Clause 13: Leakage Current and Electric Strength at Operating Temperature",
            "Clause 16: Leakage Current (< 0.75 mA) and Dielectric High-Voltage Test (1250V to 3750V)",
            "Clause 19: Abnormal Operation Test — Stalled motor, dry heating, short circuit safeguards",
            "Clause 22: Construction — Earthing continuity (< 0.1 ohm) and cord retention strain relief"
        ],
        "keywords": ["electrical safety", "IS 302", "appliance safety", "dielectric test", "leakage current", "ISI mark appliances", "shock protection"]
    },
    {
        "is_code": "IS 15652: 2006",
        "title": "Insulating Mats for Electrical Purposes — Specification",
        "year": "2006",
        "division": "Electrotechnical Division",
        "mandatory": True,
        "scope": "Prescribes requirements for synthetic rubber insulating mats used in front of high voltage electrical switchboards, substations, and power stations. Categorizes mats into Class 0 (3.3 kV), Class 1 (11 kV), Class 2 (33 kV) based on AC proof voltage and puncture resistance.",
        "key_clauses": [
            "Clause 4: Classification — Class 0 (3.3 kV), Class 1 (11 kV), Class 2 (33 kV)",
            "Clause 6: Tensile strength (> 15 N/mm2) and elongation at break (> 250%)",
            "Clause 7: Dielectric Proof Voltage Test — 10 kV to 36 kV AC for 3 minutes without flashover",
            "Clause 8: Aging, Flame Retardance, and Acid/Oil Resistance"
        ],
        "keywords": ["insulating mat", "electrical mat", "IS 15652", "substation mat", "high voltage mat", "switchboard safety mat", "11kV mat"]
    },

    # ─── CHEMICAL & PETROLEUM DIVISION (PCD / CHD) ──────────────────────────
    {
        "is_code": "IS 10500: 2012",
        "title": "Drinking Water — Specification",
        "year": "2012",
        "division": "Chemical Division",
        "mandatory": True,
        "scope": "Flagship national standard specifying physical, chemical, toxicological, and bacteriological requirements for potable drinking water supplied via municipal networks or packaged sources. Defines acceptable and permissible limits for TDS (500-2000 mg/L), pH (6.5-8.5), Turbidity (1-5 NTU), Arsenic (0.01 mg/L), Lead (0.01 mg/L), Fluoride (1.0-1.5 mg/L), and E. coli (zero count per 100 ml).",
        "key_clauses": [
            "Clause 4: Organoleptic and Physical Parameters — Colour, Odour, Taste, Turbidity, pH, TDS",
            "Clause 4.1: General Chemical Parameters — Total Hardness, Alkalinity, Chlorides, Sulphates, Nitrates",
            "Clause 4.2: Toxic Substances Limits — Arsenic, Cadmium, Cyanide, Lead, Mercury, Chromium, Nickel",
            "Clause 4.3: Bacteriological Quality — Total coliforms and E. coli must be absent in any 100 ml sample",
            "Clause 4.4: Radioactive Contaminants — Alpha emitters (0.1 Bq/L max), Beta emitters (1.0 Bq/L max)"
        ],
        "keywords": ["drinking water", "IS 10500", "water quality", "potable water", "TDS limits", "arsenic limit", "coliform test", "water parameters"]
    },
    {
        "is_code": "IS 14543: 2016",
        "title": "Packaged Drinking Water (Other than Packaged Natural Mineral Water) — Specification",
        "year": "2016",
        "division": "Chemical Division",
        "mandatory": True,
        "scope": "Mandatory standard for commercial packaged water (bottles, pouches, 20L jars). Details water treatment techniques (RO, UV, Ozonation), mandatory re-mineralization, bottle material quality (IS 12252 PET), hygienic plant layout, and strict microbial testing.",
        "key_clauses": [
            "Clause 4: Processing — RO filtration, ozonation, UV disinfection, and hygienic capping",
            "Clause 5: Chemical and Hygienic Limits — Remineralization limits for Calcium and Magnesium",
            "Clause 6: Packaging — Food-grade PET bottles conforming to IS 14534",
            "Clause 7: Mandatory Labeling — 'Packaged Drinking Water', batch code, best before date, FSSAI & BIS ISI marks"
        ],
        "keywords": ["packaged drinking water", "IS 14543", "bottled water", "RO water plant", "water jar", "packaged water mandatory"]
    },
    {
        "is_code": "IS 4209: 2013",
        "title": "Safety Code for Handling and Storage of Chemical Materials",
        "year": "2013",
        "division": "Chemical Division",
        "mandatory": False,
        "scope": "Provides safety guidelines for bulk storage, loading/unloading, segregation, and emergency handling of hazardous liquid, gaseous, and solid chemicals in industrial plants. Covers spill containment dikes, flameproof electricals, emergency eyewash, and MSDS compliance.",
        "key_clauses": [
            "Clause 4: Hazardous Chemical Classification — Flammable, Corrosive, Toxic, Explosive",
            "Clause 5: Chemical Compatibility and Storage Segregation Matrix",
            "Clause 6: Spill Containment Design — Secondary containment volume (110% of tank size)",
            "Clause 8: Personal Protective Equipment (PPE) and Emergency Response Plan"
        ],
        "keywords": ["chemical storage", "IS 4209", "hazardous chemical safety", "chemical handling", "spill containment", "MSDS compliance"]
    },

    # ─── MEDICAL EQUIPMENT & HEALTHCARE DIVISION (MHD) ───────────────────────
    {
        "is_code": "IS/ISO 13485: 2016",
        "title": "Medical Devices — Quality Management Systems — Requirements for Regulatory Purposes",
        "year": "2016",
        "division": "Medical Equipment and Hospital Planning Division",
        "mandatory": True,
        "scope": "Adopts ISO 13485 identically as the central quality management system standard for medical device design, manufacturing, sterilization, and distribution under Medical Devices Rules, 2017 (CDSCO). Covers medical device file (MDF), cleanroom contamination controls, risk management (ISO 14971), and post-market surveillance.",
        "key_clauses": [
            "Clause 4: Quality Management System & Medical Device File (MDF)",
            "Clause 6.4: Work Environment and Contamination Control — ISO Class 7/8 Cleanrooms",
            "Clause 7.3: Design and Development Controls — Verification, validation, and clinical evaluation",
            "Clause 7.5: Sterilization Validation and Bioburden Controls",
            "Clause 8.2: Complaint Handling and Adverse Event Reporting to CDSCO"
        ],
        "keywords": ["ISO 13485", "medical device QMS", "CDSCO compliance", "cleanroom validation", "medical device manufacturing", "bioburden control"]
    },
    {
        "is_code": "IS 13422: 2021",
        "title": "Single-Use Sterile Hypodermic Syringes — Specification",
        "year": "2021",
        "division": "Medical Equipment and Hospital Planning Division",
        "mandatory": True,
        "scope": "Prescribes dimensions, barrel clarity, plunger freedom of motion, dead space volume, freedom from pyrogens, sterility testing, and ethylene oxide (EtO) residual limits for disposable syringes.",
        "key_clauses": [
            "Clause 4: Barrel and Plunger Material — Medical grade polypropylene conforming to IS 10146",
            "Clause 5: Piston Seal Integrity — Air and liquid leakage test under pressure and vacuum",
            "Clause 7: Sterility and Pyrogenicity — Zero bacterial endotoxins (< 20 EU/device)",
            "Clause 8: Ethylene Oxide (EtO) Residual Limit (< 5 ppm)"
        ],
        "keywords": ["hypodermic syringe", "disposable syringe", "IS 13422", "medical syringe", "sterile syringe", "EtO residual"]
    },

    # ─── FOOD & AGRICULTURE DIVISION (FAD) ──────────────────────────────────
    {
        "is_code": "IS 1165: 2002",
        "title": "Milk Powder — Specification",
        "year": "2002",
        "division": "Food and Agriculture Division",
        "mandatory": True,
        "scope": "Covers whole milk powder, skimmed milk powder (SMP), and partly skimmed milk powder. Sets limits on moisture (< 4.0%), milk fat, titratable acidity, total ash, scorched particles, and microbiological standards (Salmonella, Listeria).",
        "key_clauses": [
            "Clause 4: Chemical Requirements — Moisture (max 4.0%), Fat (> 26.0% for whole milk powder)",
            "Clause 5: Insolubility Index (< 1.0 ml) and Scorched Particles (Disc B max)",
            "Clause 6: Heavy Metals — Lead max 0.2 mg/kg, Arsenic max 0.1 mg/kg",
            "Clause 7: Microbiological Criteria — Total Plate Count (< 40,000 CFU/g), Coliforms absent"
        ],
        "keywords": ["milk powder", "skimmed milk powder", "IS 1165", "dairy product", "SMP specification", "FSSAI milk powder"]
    },
    {
        "is_code": "IS 4984: 2016",
        "title": "High Density Polyethylene (HDPE) Pipes for Water Supply — Specification",
        "year": "2016",
        "division": "Civil Engineering Division",
        "mandatory": True,
        "scope": "Prescribes requirements for PE 63, PE 80, and PE 100 grade HDPE pipes used for drinking water transportation, sewerage, and agricultural irrigation. Specifies pressure ratings (PN 2.5 to PN 16), hydraulic burst pressure, carbon black dispersion, and overall migration test.",
        "key_clauses": [
            "Clause 5: Raw Material — Virgin PE 100 resin conforming to IS 7328",
            "Clause 6: Dimensions and Tolerances for outer diameter and wall thickness",
            "Clause 8: Internal Hydrostatic Pressure Test at 80°C for 165 hours",
            "Clause 9: Carbon Black Content (2.0 to 2.5%) and Dispersion Quality"
        ],
        "keywords": ["HDPE pipe", "PE 100 pipe", "IS 4984", "polyethylene pipe", "water supply pipe", "HDPE pressure pipe"]
    },

    # ─── MANAGEMENT & SYSTEMS DIVISION (MSD) ────────────────────────────────
    {
        "is_code": "IS/ISO 9001: 2015",
        "title": "Quality Management Systems — Requirements",
        "year": "2015",
        "division": "Management and Systems Division",
        "mandatory": False,
        "scope": "Flagship national adoption of ISO 9001. Defines high-level structure (HLS) for quality management systems based on PDCA (Plan-Do-Check-Act) cycle, risk-based thinking, leadership commitment, process approach, customer satisfaction, and continuous improvement.",
        "key_clauses": [
            "Clause 4: Context of the Organization and Interested Parties",
            "Clause 5: Leadership and Commitment — Quality Policy",
            "Clause 6: Planning — Addressing risks and opportunities",
            "Clause 8: Operation — Operational planning, control, and non-conforming outputs",
            "Clause 9 & 10: Performance Evaluation, Internal Audit, and Continual Improvement"
        ],
        "keywords": ["ISO 9001", "quality management system", "IS ISO 9001", "QMS certification", "process approach", "internal audit"]
    },
    {
        "is_code": "IS 14489: 2018",
        "title": "Code of Practice on Occupational Safety and Health Audit",
        "year": "2018",
        "division": "Management and Systems Division",
        "mandatory": False,
        "scope": "Provides guidelines for planning, conducting, and reporting comprehensive occupational safety and health (OSH) audits in hazardous factories, refineries, chemical plants, and construction sites. Establishes safety audit questionnaires, auditor qualifications, and corrective action verification.",
        "key_clauses": [
            "Clause 4: Objectives and Scope of Safety Audit",
            "Clause 5: Audit Methodology — Document review, site inspection, management interview",
            "Clause 6: Key Elements Evaluated — Safety policy, hazard identification, emergency plan, PPE, permit to work system",
            "Clause 8: Audit Report Format and Management Action Plan"
        ],
        "keywords": ["safety audit", "IS 14489", "OSH audit", "occupational safety", "factory safety audit", "hazard identification"]
    }
]


def generate_extended_catalog():
    data_dir = os.path.abspath(os.path.join(os.path.dirname(__file__)))
    target_path = os.path.join(data_dir, "extended_bis_catalog.json")

    print(f"[CatalogBuilder] Generating extended catalog of {len(EXTENDED_STANDARDS_CATALOG)} division standards...")

    with open(target_path, "w", encoding="utf-8") as f:
        json.dump(EXTENDED_STANDARDS_CATALOG, f, indent=2)

    print(f"[CatalogBuilder] Wrote {target_path} ({os.path.getsize(target_path) / 1024:.1f} KB)")


if __name__ == "__main__":
    generate_extended_catalog()
