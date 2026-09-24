import type { SearchResult } from './types';

export interface TopicData {
  id: string;
  category: string;
  keywords: string[];
  sampleQueries: string[];
  data: SearchResult;
}

export const BIS_TOPIC_DATASETS: Record<string, TopicData> = {
  // =========================================================================
  // TOPIC 1: ELECTRIC KETTLE & HOUSEHOLD ELECTRICAL APPLIANCES
  // =========================================================================
  electric_kettle: {
    id: 'electric_kettle',
    category: 'Electrotechnical',
    keywords: [
      'kettle', 'electric kettle', 'heating liquid', 'appliance', 'is 302',
      'is 4250', 'is 13252', 'is 1293', 'crs', 'isi mark', 'certification',
      'boil dry', 'thermal cutoff', 'emc', 'plugs', 'household electrical', 'tea maker'
    ],
    sampleQueries: [
      'Electric kettle manufacturing standards',
      'I want to manufacture an electric kettle in India. Which BIS standards apply to it, what tests are required, and how do I get certification?',
      'electric kettle bis standard',
      'heating liquids appliance safety',
      'IS 302 electric kettle'
    ],
    data: {
      summary:
        "Manufacturing an electric kettle in India requires compliance with mandatory safety standards under the BIS Compulsory Registration Scheme (CRS) and ISI mark scheme. The primary standard IS 302-2-15 regulates appliances heating liquids, mandating boil-dry protection, thermal endurance, and insulation tests before market clearance.",
      query_magnified:
        'electric kettle manufacturing, IS 302 safety, household electrical appliances, heating liquids, BIS certification, ISI mark, EMC compliance, compulsory registration scheme, type testing, boil-dry protection',
      standards: [
        {
          is_code: 'IS 302 (Part 2/Sec 15) : 2009',
          title: 'Safety of Household and Similar Electrical Appliances — Particular Requirements for Appliances for Heating Liquids',
          confidence: 98,
          confidence_tier: 'high',
          highlight_reason:
            'PRIMARY MANDATORY STANDARD: Specifically written for electric kettles, coffee makers, and liquid heaters. Mandates automatic boil-dry cutouts, thermal fuses, spill resistance, and maximum temperature limits on touchable handles.',
          key_clauses: [
            'Clause 15.101: Boil-dry Protection & Abnormal Heating',
            'Clause 19: Abnormal Operation & Fault Conditions',
            'Clause 22: Mechanical Construction & Cord Anchorage',
            'Clause 30: Resistance to Heat and Fire'
          ],
          division: 'Electrotechnical',
          year: 2009,
          abstract_scope:
            'This standard specifies safety requirements for electric appliances intended for heating liquids for domestic and similar purposes with rated voltage not exceeding 250V. Tests include thermal endurance, leakage current under humid conditions, mechanical strength of spouts and lids, and fire resistance of polymeric enclosures.',
          url: 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/knowyourstandards/indian_standards/isdetails/3364'
        },
        {
          is_code: 'IS 302 (Part 1) : 2008',
          title: 'Safety of Household and Similar Electrical Appliances — General Requirements',
          confidence: 95,
          confidence_tier: 'high',
          highlight_reason:
            'Foundational parent standard for all home appliances. Covers fundamental electrical safety, grounding continuity (<0.1 ohm), high-voltage dielectric strength (1250V AC), and marking tolerances.',
          key_clauses: [
            'Clause 8: Protection Against Electric Shock',
            'Clause 10: Power Input & Rated Current Tolerances',
            'Clause 13: Leakage Current at Operating Temperature',
            'Clause 25: Supply Connection & External Flexible Cords'
          ],
          division: 'Electrotechnical',
          year: 2008,
          abstract_scope:
            'Specifies baseline safety principles for household and commercial electrical appliances. Addresses hazards from electrical shock, excessive heat, fire, mechanical instability, and toxic radiation.',
          url: 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/knowyourstandards/indian_standards/isdetails/3349'
        },
        {
          is_code: 'IS 4250 : 1980',
          title: 'Specification for Electric Kettles',
          confidence: 92,
          confidence_tier: 'high',
          highlight_reason:
            'Product specification standard defining physical parameters: maximum water level indicators, food-grade grade 304 stainless steel or safe polypropylene bodies, wattage ratings, and minimum heating speed efficiency.',
          key_clauses: [
            'Clause 4: Capacity and Rating (up to 3 Litres)',
            'Clause 5: Materials in Contact with Potable Water',
            'Clause 6: Construction and Thermal Efficiency',
            'Clause 8: Mandatory Markings and Rating Plate'
          ],
          division: 'Electrotechnical',
          year: 1980,
          abstract_scope:
            'Covers domestic electric kettles with immersed or concealed heating elements up to 3000 watts. Sets criteria for element corrosion resistance, lid hinge durability, and water boil performance.',
          url: 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/knowyourstandards/indian_standards/isdetails/4490'
        },
        {
          is_code: 'IS 13252 (Part 1) : 2010',
          title: 'Information Technology & Electronic Equipment Safety / Electromagnetic Compatibility',
          confidence: 76,
          confidence_tier: 'moderate',
          highlight_reason:
            'Applies to kettles containing microcontroller PCBs, temperature displays, or digital touch panels. Enforces harmonic emission limits and electrical surge immunity.',
          key_clauses: [
            'Clause 6: Emission Limits for Phase Current ≤16A',
            'Clause 7: Electronic Circuit Safety & Creepage Distances',
            'Table 1: Maximum Permissible Harmonic Disturbances'
          ],
          division: 'Electronics and Information Technology',
          year: 2010,
          abstract_scope:
            'Specifies limits on harmonic currents emitted into public low-voltage electricity grids by household electronic equipment, ensuring appliance controls do not disrupt power networks.',
          url: 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/knowyourstandards/indian_standards/isdetails/13441'
        },
        {
          is_code: 'IS 1293 : 2019',
          title: 'Plugs and Socket-Outlets of Rated Voltage up to 250V and Rated Current up to 16A',
          confidence: 63,
          confidence_tier: 'moderate',
          highlight_reason:
            'Mandatory plug standard: Kettles typically draw 1500W-2200W and must be fitted with certified Indian standard 3-pin 6A or 16A solid brass earthed plugs with insulated pin sleeves.',
          key_clauses: [
            'Clause 10: Dimensions and Pin Spacing',
            'Clause 14: Insulation Resistance & Dielectric Strength',
            'Clause 16: Breaking Capacity & Mechanical Durability'
          ],
          division: 'Electrotechnical',
          year: 2019,
          abstract_scope:
            'Specifies safety and dimensional constraints for plugs and socket-outlets intended for household AC circuits. Mandates insulated sleeves on phase and neutral pins to prevent contact during insertion.',
          url: 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/knowyourstandards/indian_standards/isdetails/1310'
        },
        {
          is_code: 'IS 15885 : 2010',
          title: 'Safety of Electronic Controlgear and Labelling Requirements for Household Appliances',
          confidence: 48,
          confidence_tier: 'low',
          highlight_reason:
            'Mandatory packaging and on-body marking: Specifies ISI mark placement, manufacturer license number (CM/L-XXXXXXXX), voltage, wattage, and warnings against water immersion.',
          key_clauses: [
            'Clause 4: Mandatory Product Body Markings',
            'Clause 5: Retail Packaging Disclosure Guidelines',
            'Clause 6: Standardized Safety Warning Graphics'
          ],
          division: 'Electrotechnical',
          year: 2010,
          abstract_scope:
            'Covers labelling durability, marking contrast, and environmental resilience for household consumer appliances manufactured or imported into India.',
          url: 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/knowyourstandards/indian_standards/isdetails/16024'
        }
      ]
    }
  },

  // =========================================================================
  // TOPIC 2: DRINKING WATER QUALITY LIMITS
  // =========================================================================
  drinking_water: {
    id: 'drinking_water',
    category: 'Chemical / Food & Agriculture',
    keywords: [
      'water', 'drinking water', 'potable water', 'is 10500', 'is 14543',
      'is 13428', 'tds', 'ph', 'fluoride', 'arsenic', 'lead', 'coliform',
      'water quality', 'water limits', 'packaged drinking water', 'reverse osmosis',
      'microbiological', 'turbidity', 'hardness', 'chlorine', 'heavy metals', 'mineral water'
    ],
    sampleQueries: [
      'Drinking water quality limits',
      'BIS standards for drinking water and permissible TDS limits',
      'IS 10500 water specification parameters',
      'Packaged drinking water ISI norms',
      'What are permissible heavy metal limits in potable water in India?'
    ],
    data: {
      summary:
        "In India, potable tap water quality is strictly governed by IS 10500:2012, which defines acceptable and permissible limits for organoleptic, chemical, toxic, and bacteriological parameters. Commercial packaged water is further regulated under IS 14543 (packaged drinking water) and IS 13428 (natural mineral water) under mandatory BIS certification.",
      query_magnified:
        'IS 10500 potable water limits, packaged drinking water IS 14543, TDS limits, pH acceptable range, arsenic permissible limit, fluoride concentration, E. coli microbiological testing, IS 3025 analytical methods',
      standards: [
        {
          is_code: 'IS 10500 : 2012',
          title: 'Drinking Water — Specification (Second Revision)',
          confidence: 99,
          confidence_tier: 'high',
          highlight_reason:
            'THE NATIONAL BENCHMARK FOR POTABLE WATER: Establishes acceptable limits (pH 6.5-8.5, TDS 500 mg/L, Turbidity 1 NTU, Hardness 200 mg/L) and toxic thresholds (Arsenic ≤0.01 mg/L, Lead ≤0.01 mg/L, Fluoride ≤1.0 mg/L). Mandates zero E. coli per 100 mL.',
          key_clauses: [
            'Table 1: Organoleptic & Physical Parameters (Color, Odour, pH, Turbidity)',
            'Table 2: General Chemical Parameters (TDS, Hardness, Chlorides, Sulphates)',
            'Table 3: Parameters Concerning Toxic Substances (Arsenic, Cadmium, Lead, Mercury)',
            'Table 6: Bacteriological Quality Requirements (E. Coli, Total Coliforms)'
          ],
          division: 'Food and Agriculture / Chemical',
          year: 2012,
          abstract_scope:
            'Prescribes requirements and methods of sampling and test for drinking water meant for human consumption. Covers physical, chemical, toxic, radioactive, and bacteriological quality standards, defining acceptable limits and maximum permissible limits in the absence of alternative water sources.',
          url: 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/knowyourstandards/indian_standards/isdetails/10633'
        },
        {
          is_code: 'IS 14543 : 2024',
          title: 'Packaged Drinking Water (Other than Packaged Natural Mineral Water) — Specification',
          confidence: 94,
          confidence_tier: 'high',
          highlight_reason:
            'MANDATORY COMMERCIAL STANDARD: All bottled water manufacturers in India must obtain a BIS license under this code. Requires multi-barrier treatment (reverse osmosis, UV, ozonisation), remineralisation limits, and shelf-life microbial stability.',
          key_clauses: [
            'Clause 5: Hygienic Treatment Processes (RO, Ozonation, Micro-filtration)',
            'Clause 6: Finished Product Physical & Chemical Limits (TDS 75-500 mg/L)',
            'Clause 7: Packaging Container Standards (Food-grade PET/Glass)',
            'Table 2: Microbiological Limits (Absence of Pseudomonas aeruginosa, Streptococci)'
          ],
          division: 'Food and Agriculture',
          year: 2024,
          abstract_scope:
            'Specifies requirements for packaged drinking water filled into hermetically sealed containers of various capacities. Outlines mandatory testing for 50+ parameters including pesticides, volatile organic compounds, and microplastics.',
          url: 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/knowyourstandards/indian_standards/isdetails/14682'
        },
        {
          is_code: 'IS 13428 : 2005',
          title: 'Packaged Natural Mineral Water — Specification',
          confidence: 88,
          confidence_tier: 'high',
          highlight_reason:
            'Regulates premium spring and underground mineral water. Prohibits chemical treatments; allows only physical filtration. Mandates natural mineral balance declarations on retail bottles.',
          key_clauses: [
            'Clause 4: Geological Source Protection & Sanitisation',
            'Clause 6: Natural Mineral Composition Requirements',
            'Clause 8: Packaging and Origin Labelling Declarations'
          ],
          division: 'Food and Agriculture',
          year: 2005,
          abstract_scope:
            'Prescribes conditions for sourcing, bottling, and quality testing of natural mineral water collected directly from natural or drilled subterranean springs.',
          url: 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/knowyourstandards/indian_standards/isdetails/13567'
        },
        {
          is_code: 'IS 3025 (Series) : 1987-2023',
          title: 'Methods of Sampling and Test (Physical and Chemical) for Water and Wastewater',
          confidence: 79,
          confidence_tier: 'moderate',
          highlight_reason:
            'The official analytical testing compendium: Part 11 (Electrometric pH), Part 16 (TDS gravimetric drying at 180°C), Part 21 (Hardness EDTA titration), Part 53 (Iron spectrophotometry).',
          key_clauses: [
            'Part 11: Determination of pH by Glass Electrode',
            'Part 16: Determination of Filterable Residue (Total Dissolved Solids)',
            'Part 23: Determination of Total Alkalinity',
            'Part 32: Determination of Chloride by Argentometric Method'
          ],
          division: 'Chemical',
          year: 2021,
          abstract_scope:
            'Standardized laboratory test methods utilized by BIS and NABL accredited laboratories across India for compliance verification of drinking and wastewater.',
          url: 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/knowyourstandards/indian_standards/isdetails/3062'
        },
        {
          is_code: 'IS 1622 : 1981',
          title: 'Methods of Sampling and Microbiological Examination of Water',
          confidence: 65,
          confidence_tier: 'moderate',
          highlight_reason:
            'Prescribes microbiological testing techniques: membrane filter procedure and Multiple Tube Fermentation (MPN) for detecting coliform organisms, faecal streptococci, and pathogens.',
          key_clauses: [
            'Clause 4: Sterilised Sampling Bottle Protocols',
            'Clause 6: Incubation Temperatures and Media Preparation',
            'Clause 8: Coliform Identification and Confirmation Protocols'
          ],
          division: 'Food and Agriculture',
          year: 1981,
          abstract_scope:
            'Details protocols for bacteriological sampling, colony plate counts, and pathogen isolation from water supplies to prevent waterborne disease epidemics.',
          url: 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/knowyourstandards/indian_standards/isdetails/1645'
        },
        {
          is_code: 'IS 17482 : 2020',
          title: 'Drinking Water Supply Management System for Piping Network — Requirements',
          confidence: 52,
          confidence_tier: 'low',
          highlight_reason:
            'National standard supporting the Jal Jeevan Mission: Outlines 24x7 piped water supply guidelines, disinfection residual maintenance (chlorine 0.2 to 0.5 mg/L), and water audit protocols.',
          key_clauses: [
            'Clause 5: Residual Disinfection Monitoring in Distribution Grids',
            'Clause 7: Pipe Network Cross-contamination Prevention',
            'Clause 9: Consumer Grievance Water Sampling'
          ],
          division: 'Civil Engineering',
          year: 2020,
          abstract_scope:
            'Provides operational specifications for municipal utilities managing urban and rural piped drinking water distribution systems.',
          url: 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/knowyourstandards/indian_standards/isdetails/17700'
        }
      ]
    }
  },

  // =========================================================================
  // TOPIC 3: EARTHQUAKE RESISTANT BUILDING CODES
  // =========================================================================
  earthquake_building: {
    id: 'earthquake_building',
    category: 'Civil Engineering',
    keywords: [
      'earthquake', 'seismic', 'building code', 'is 1893', 'is 13920',
      'is 4326', 'is 456', 'base shear', 'ductile detailing', 'zone factor',
      'response spectrum', 'structural design', 'masonry building', 'seismic zone',
      'rcc frame', 'lateral loads', 'plastic hinge', 'reinforcement', 'tall building'
    ],
    sampleQueries: [
      'Earthquake resistant building codes',
      'Seismic design criteria for concrete structures in India',
      'IS 1893 zone factors and base shear calculation',
      'Ductile detailing requirements IS 13920',
      'What are the mandatory building codes for earthquake zone IV and V?'
    ],
    data: {
      summary:
        "India classifies earthquake vulnerability into four Seismic Zones (II, III, IV, and V). Seismic building design is anchored by IS 1893 (Part 1):2016 for calculating dynamic lateral forces and base shear, supplemented mandatorily by IS 13920:2016 for ductile reinforcement detailing in high-risk zones.",
      query_magnified:
        'IS 1893 seismic design spectra, Zone Factor Z, response reduction factor R, base shear Ah * W, IS 13920 ductile detailing, plastic hinge confining stirrups, IS 4326 masonry seismic bands, IS 456 structural safety',
      standards: [
        {
          is_code: 'IS 1893 (Part 1) : 2016',
          title: 'Criteria for Earthquake Resistant Design of Structures — Part 1: General Provisions and Buildings',
          confidence: 98,
          confidence_tier: 'high',
          highlight_reason:
            'PRIMARY SEISMIC CODE: Mandates seismic zone factors (Zone II=0.10, III=0.16, IV=0.24, V=0.36), design response spectra for hard/medium/soft soils, importance factors, and equivalent static base shear formulas.',
          key_clauses: [
            'Clause 6.4: Design Acceleration Spectrum (Sa/g)',
            'Clause 7.6: Design Base Shear Vb = Ah * W',
            'Table 2: Seismic Zone Factors (Z)',
            'Table 3: Response Reduction Factor (R) for Moment Frames',
            'Clause 7.11: Inter-Storey Drift Limitation (0.004h)'
          ],
          division: 'Civil Engineering',
          year: 2016,
          abstract_scope:
            'Deals with the assessment of seismic loads on buildings and structural engineering principles to resist earthquake shaking without collapse. Covers torsional irregularity, soft storey checks, and dynamic response spectrum analysis.',
          url: 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/knowyourstandards/indian_standards/isdetails/1922'
        },
        {
          is_code: 'IS 13920 : 2016',
          title: 'Ductile Design and Detailing of Reinforced Concrete Structures Subjected to Seismic Forces',
          confidence: 96,
          confidence_tier: 'high',
          highlight_reason:
            'MANDATORY FOR ZONES III, IV & V: Enforces strict reinforcement rules to ensure structures bend without brittle failure. Mandates close-spaced stirrups (s ≤ d/4) in beam plastic hinges, confining ties in columns, and strong-column weak-beam ratios.',
          key_clauses: [
            'Clause 6: Longitudinal and Transverse Reinforcement Grades',
            'Clause 7: Flexural Members (Beams) Seismic Detailing',
            'Clause 8: Columns Under Axial & Reversible Bending Moments',
            'Clause 9: Beam-Column Joint Shear Strength Provisions',
            'Clause 10: Special Confining Hoop Reinforcement'
          ],
          division: 'Civil Engineering',
          year: 2016,
          abstract_scope:
            'Covers the requirements for designing and detailing members of monolithic reinforced concrete buildings to give them adequate toughness and ductility to resist severe earthquake forces.',
          url: 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/knowyourstandards/indian_standards/isdetails/14060'
        },
        {
          is_code: 'IS 4326 : 2013',
          title: 'Earthquake Resistant Design and Construction of Buildings — Code of Practice (Third Revision)',
          confidence: 89,
          confidence_tier: 'high',
          highlight_reason:
            'PRACTICAL CONSTRUCTION CODE: Details architectural safety, building symmetry, separation joints to prevent pounding, and mandatory continuous horizontal concrete/wood seismic bands (plinth, lintel, roof bands) in masonry structures.',
          key_clauses: [
            'Clause 4: Structural Symmetry, Shape & Separation Joints',
            'Clause 7: Masonry Wall Construction and Mortar Mixes',
            'Clause 8: Horizontal Seismic Bands at Plinth, Lintel and Roof Levels',
            'Clause 9: Vertical Steel Bars at Corners and Wall Junctions'
          ],
          division: 'Civil Engineering',
          year: 2013,
          abstract_scope:
            'Provides practical architectural planning and construction guidance for earthquake-resistant buildings using various construction materials including stone, brick, and timber.',
          url: 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/knowyourstandards/indian_standards/isdetails/4578'
        },
        {
          is_code: 'IS 456 : 2000',
          title: 'Plain and Reinforced Concrete — Code of Practice (Fourth Revision)',
          confidence: 84,
          confidence_tier: 'high',
          highlight_reason:
            'Foundational concrete standard: Specifies minimum concrete grades (M20 for RCC), steel rebar stress limits, cover for corrosion resistance, and baseline structural load design.',
          key_clauses: [
            'Clause 26.5: Minimum & Maximum Steel Ratios in Beams and Slabs',
            'Clause 32: Design of Reinforced Concrete Shear Walls',
            'Clause 38: Limit State of Collapse in Flexure'
          ],
          division: 'Civil Engineering',
          year: 2000,
          abstract_scope:
            'Applies to the structural use of plain and reinforced concrete in general civil construction, establishing the fundamental calculations of strength, serviceability, and durability.',
          url: 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/knowyourstandards/indian_standards/isdetails/480'
        },
        {
          is_code: 'IS 16700 : 2017',
          title: 'Criteria for Structural Safety of Tall Concrete Buildings',
          confidence: 68,
          confidence_tier: 'moderate',
          highlight_reason:
            'Dedicated code for high-rise buildings exceeding 50m in height. Mandates wind-tunnel dynamic testing, P-Delta secondary stability analysis, and outrigger wall systems.',
          key_clauses: [
            'Clause 5: Structural System Feasibility by Height Category',
            'Clause 7: Inter-storey Lateral Drift Limits under Combined Seismic and Wind',
            'Clause 9: Wind Tunnel Experimental Testing Requirements'
          ],
          division: 'Civil Engineering',
          year: 2017,
          abstract_scope:
            'Specifies engineering guidelines to ensure the safety, serviceability, and stability of tall concrete structures up to 250m against severe dynamic horizontal forces.',
          url: 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/knowyourstandards/indian_standards/isdetails/16910'
        },
        {
          is_code: 'IS 13828 : 1993',
          title: 'Improving Earthquake Resistance of Low Strength Masonry Buildings — Guidelines',
          confidence: 49,
          confidence_tier: 'low',
          highlight_reason:
            'Crucial standard for affordable and rural housing: Specifies reinforcement techniques for mud mortar, adobe, and unburnt clay brick dwellings to avert sudden seismic collapse.',
          key_clauses: [
            'Clause 4: Maximum Wall Dimensions and Opening Restrictions',
            'Clause 5: Seismic Band Construction Using Wood and Steel Welded Wire Mesh'
          ],
          division: 'Civil Engineering',
          year: 1993,
          abstract_scope:
            'Presents economical retrofit and building methods to upgrade the seismic capacity of earthen walls and low-strength masonry prevalent across rural India.',
          url: 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/knowyourstandards/indian_standards/isdetails/13968'
        }
      ]
    }
  },

  // =========================================================================
  // TOPIC 4: FIRE SAFETY STANDARDS FOR BUILDINGS
  // =========================================================================
  fire_safety: {
    id: 'fire_safety',
    category: 'Civil / Fire Fighting',
    keywords: [
      'fire', 'fire safety', 'fire protection', 'nbc', 'is 2190', 'is 3844',
      'is 15105', 'is 2189', 'is 1641', 'fire extinguisher', 'sprinkler',
      'hydrant', 'smoke detector', 'fire alarm', 'egress', 'fire exit',
      'fire resistance', 'refuge area', 'hose reel', 'evacuation'
    ],
    sampleQueries: [
      'Fire safety standards for buildings',
      'National Building Code Part 4 fire life safety guidelines',
      'Fire extinguisher installation and maintenance IS 2190',
      'Automatic sprinkler system installation standards IS 15105',
      'Commercial building fire exit and hydrant requirements in India'
    ],
    data: {
      summary:
        "Building fire and life safety in India is anchored by the National Building Code (NBC 2016 Part 4), which dictates compartmentation, travel distances to fire exits, and minimum staircase widths. Active fire systems are governed by specific Indian Standards including IS 2190 (extinguishers), IS 3844 (hydrants), IS 15105 (sprinklers), and IS 2189 (detection alarms).",
      query_magnified:
        'NBC 2016 Part 4 Fire and Life Safety, IS 2190 portable fire extinguisher selection, IS 3844 internal wet riser hydrants, IS 15105 automatic sprinkler systems, IS 2189 smoke detection alarm system, IS 1641 fire rating of materials',
      standards: [
        {
          is_code: 'SP 7 (Part 4) : 2016 (NBC Part 4)',
          title: 'National Building Code of India 2016 — Part 4: Fire and Life Safety',
          confidence: 99,
          confidence_tier: 'high',
          highlight_reason:
            'THE SUPREME STATUTORY BENCHMARK: Classifies buildings from Group A (Residential) to Group J (Hazardous). Mandates fire exits, maximum 30m travel distances, two enclosed staircases for high-rises (>15m), compartmentation, and refuge areas.',
          key_clauses: [
            'Clause 3: Fire Prevention Requirements and Separation Distances',
            'Clause 4: Life Safety, Egress Capacity, and Fire Exit Widths',
            'Clause 5: Fire Protection Installations (Wet Risers, Sprinklers, Pumps)',
            'Table 7: Mandatory Fire Fighting Equipment by Occupancy & Building Height'
          ],
          division: 'Civil Engineering / Fire Safety',
          year: 2016,
          abstract_scope:
            'Comprehensive national code dealing with fire prevention, life safety provisions, and active/passive fire protection systems necessary for all types of building construction across India.',
          url: 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/knowyourstandards/indian_standards/isdetails/sp7'
        },
        {
          is_code: 'IS 2190 : 2024',
          title: 'Selection, Installation and Maintenance of First-Aid Fire Extinguishers — Code of Practice',
          confidence: 95,
          confidence_tier: 'high',
          highlight_reason:
            'MANDATORY FIRST-AID APPARATUS: Dictates the selection, placement, and hydro-testing of portable extinguishers (Water CO2, Mechanical Foam, ABC Dry Chemical, CO2, Clean Agent) based on Class A, B, C, D, and F fire risks. Maximum travel distance to an extinguisher is 15 meters.',
          key_clauses: [
            'Clause 4: Fire Hazard Classification (Light, Ordinary, Extra Hazard)',
            'Clause 5: Extinguisher Selection by Fire Class (A, B, C, D, F)',
            'Clause 8: Maximum 15m Walking Distance Siting Rules',
            'Annex C: Monthly Inspection and Hydraulic Pressure Re-test Cycles'
          ],
          division: 'Fire Fighting and Life Safety',
          year: 2024,
          abstract_scope:
            'Provides specific instructions on selecting the correct type, capacity, and distribution of portable and mobile fire extinguishers in commercial, industrial, and residential spaces.',
          url: 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/knowyourstandards/indian_standards/isdetails/2221'
        },
        {
          is_code: 'IS 3844 : 1989',
          title: 'Code of Practice for Installation and Maintenance of Internal Fire Hydrants and Hose Reels',
          confidence: 91,
          confidence_tier: 'high',
          highlight_reason:
            'Essential wet riser code: Details minimum 100mm to 150mm riser pipes, fire brigade breeching inlets, 20mm first-aid rubber hose reels, fire pumps (min 2280 LPM @ 3.5 bar at highest outlet), and dedicated water tank capacities.',
          key_clauses: [
            'Clause 4: Wet Riser System Sizing and Hydrant Valve Spacing',
            'Clause 5: Dedicated Underground and Terrace Fire Water Reservoirs',
            'Clause 6: Fire Fighting Booster Pump Capacities and Automatic Pressure Switches'
          ],
          division: 'Fire Fighting',
          year: 1989,
          abstract_scope:
            'Specifies the installation guidelines for internal wet risers, dry risers, downcomers, landing valves, and first-aid hose reel systems installed in premises for fire suppression.',
          url: 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/knowyourstandards/indian_standards/isdetails/3910'
        },
        {
          is_code: 'IS 15105 : 2021',
          title: 'Design and Installation of Fixed Automatic Sprinkler Fire Extinguishing Systems',
          confidence: 86,
          confidence_tier: 'high',
          highlight_reason:
            'Automatic fire suppression: Covers quartzoid glass bulb sprinklers (68°C standard red bulb), alarm check valves, piping hydraulic calculations, and water discharge density (5 mm/min for light hazard to 12.5+ mm/min for warehouses).',
          key_clauses: [
            'Clause 5: Occupancy Hazard Classification (Light, Ordinary, High Hazard)',
            'Clause 8: Sprinkler Head Spacing (max 12 sq m per head)',
            'Clause 12: Hydraulic Pipe Sizing and Water Supply Duration'
          ],
          division: 'Fire Fighting',
          year: 2021,
          abstract_scope:
            'Specifies engineering guidelines for the design, calculation, installation, water storage sizing, and commissioning of automatic ceiling sprinkler fire extinguishing networks.',
          url: 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/knowyourstandards/indian_standards/isdetails/15310'
        },
        {
          is_code: 'IS 2189 : 2014',
          title: 'Selection, Installation and Maintenance of Automatic Fire Detection and Alarm System',
          confidence: 78,
          confidence_tier: 'moderate',
          highlight_reason:
            'Fire alert infrastructure: Enforces optical/ionisation smoke detectors (coverage 50 sq m), heat detectors, manual call points (MCP within 30m reach), fire alarm panels, and sounder levels (min 65 dBA or 5 dBA above ambient).',
          key_clauses: [
            'Clause 6: Optical Smoke and Thermal Detector Placement Grids',
            'Clause 7: Manual Call Point (Break Glass) Accessibility at Staircase Exits',
            'Clause 9: Sounder Decibel Specifications and Strobe Visual Alarms'
          ],
          division: 'Electronics and Fire Safety',
          year: 2014,
          abstract_scope:
            'Provides recommendations on planning, design, and installation of automatic fire detection networks and audible/visual alarm systems in built occupancies.',
          url: 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/knowyourstandards/indian_standards/isdetails/2220'
        },
        {
          is_code: 'IS 1641 : 1988',
          title: 'Code of Practice for Fire Safety of Buildings (General): Details of Construction',
          confidence: 58,
          confidence_tier: 'moderate',
          highlight_reason:
            'Passive fire resistance: Defines fire ratings (0.5 to 4 hours) for structural concrete, brick walls, steel enclosures, and fire doors to confine blazes within fire compartments.',
          key_clauses: [
            'Clause 3: Fire Resistance Ratings by Building Occupancy Type',
            'Table 1: Minimum Thickness for Masonry and Concrete Walls to Achieve 2-4 Hr Fire Resistance'
          ],
          division: 'Civil Engineering',
          year: 1988,
          abstract_scope:
            'Establishes fire rating standards for construction materials, fire-rated doors, partition walls, and cladding to stop structural collapse during major building fires.',
          url: 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/knowyourstandards/indian_standards/isdetails/1665'
        }
      ]
    }
  },

  // =========================================================================
  // TOPIC 5: STEEL STRUCTURAL DESIGN
  // =========================================================================
  steel_structural: {
    id: 'steel_structural',
    category: 'Civil / Metallurgical',
    keywords: [
      'steel', 'structural steel', 'is 800', 'is 2062', 'is 808',
      'is 875', 'is 4000', 'is 9595', 'steel design', 'limit state',
      'beam', 'column', 'truss', 'welding', 'bolted joint', 'hsfg bolt',
      'wind load', 'tension member', 'compression member', 'lateral torsional buckling', 'steel structure'
    ],
    sampleQueries: [
      'Steel structural design',
      'IS 800 Limit State Method structural steel design',
      'Structural steel material specification IS 2062',
      'Indian standard steel beam dimensions IS 808',
      'Wind load calculation on steel roof trusses IS 875 Part 3'
    ],
    data: {
      summary:
        "Structural steel design in India is governed by IS 800:2007 adopting the modern Limit State Method. Steel raw material specifications are dictated by IS 2062 (Grade E250 to E650), standard section geometries by IS 808 (ISMB, ISMC, ISHB), and environmental wind load computations by IS 875 (Part 3).",
      query_magnified:
        'IS 800 Limit State Design, tension compression flexural members, lateral torsional buckling, IS 2062 hot rolled steel grades E250 E350, IS 808 rolled beam channel angle dimensions, IS 875 wind pressure on steel sheds, IS 4000 HSFG bolts',
      standards: [
        {
          is_code: 'IS 800 : 2007',
          title: 'General Construction in Steel — Code of Practice (Third Revision - Limit State Method)',
          confidence: 99,
          confidence_tier: 'high',
          highlight_reason:
            'THE NATIONAL STEEL DESIGN CODE: Regulates design using the Limit State Method for Strength (Tension, Compression, Flexure, Shear) and Serviceability (deflection ≤ L/300, vibration). Details connection design with high-strength bolts and fillet/butt welds.',
          key_clauses: [
            'Section 5: General Design Principles & Partial Safety Factors',
            'Section 6: Design of Tension Members & Net Effective Area',
            'Section 7: Compression Members & Buckling Column Curves (a, b, c, d)',
            'Section 8: Flexural Members & Lateral-Torsional Buckling Checks',
            'Section 10: Design of Welded and Bolted Connections'
          ],
          division: 'Civil Engineering / Metallurgical',
          year: 2007,
          abstract_scope:
            'Code of practice for the design and construction of steel structures using hot-rolled sections and plate girders. Aligned internationally with Eurocode 3 and AISC limit state philosophy.',
          url: 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/knowyourstandards/indian_standards/isdetails/822'
        },
        {
          is_code: 'IS 2062 : 2011',
          title: 'Hot Rolled Medium and High Tensile Structural Steel — Specification',
          confidence: 96,
          confidence_tier: 'high',
          highlight_reason:
            'MANDATORY MATERIAL SPECIFICATION: All structural steel fabricated in India must comply with IS 2062. Defines grades E250 (yield strength 250 MPa), E350, E450 up to E650, along with Carbon Equivalent (CE ≤ 0.42%) and Charpy V-notch impact test toughness.',
          key_clauses: [
            'Clause 6: Chemical Composition Limits and Carbon Equivalent Calculation',
            'Table 2: Mechanical Properties (Tensile Strength, Yield Stress, Elongation)',
            'Clause 9: Charpy V-notch Impact Tests at 0°C, -20°C and -40°C',
            'Clause 10: Ultrasonic Testing Requirements for Heavy Plates'
          ],
          division: 'Metallurgical Engineering',
          year: 2011,
          abstract_scope:
            'Prescribes requirements for hot-rolled medium and high-tensile structural steel plates, sheets, strips, sections, flats, and bars used in bridges, buildings, towers, and heavy structures.',
          url: 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/knowyourstandards/indian_standards/isdetails/2096'
        },
        {
          is_code: 'IS 808 : 1989',
          title: 'Dimensions for Hot Rolled Steel Beam, Column, Channel and Angle Sections',
          confidence: 90,
          confidence_tier: 'high',
          highlight_reason:
            'GEOMETRIC SHAPE TABLES: Defines standard dimensions, weight per metre, moment of inertia (Ixx, Iyy), and radius of gyration for Indian sections: ISMB (Medium Beams), ISMC (Channels), ISHB (Heavy Columns), and Equal/Unequal Angles.',
          key_clauses: [
            'Table 1: Dimensions and Sectional Properties of ISMB (Medium Weight Beams)',
            'Table 6: Dimensions and Properties of ISHB (Heavy Beams & Columns)',
            'Table 8: Dimensions and Properties of ISMC (Indian Standard Channels)'
          ],
          division: 'Civil and Metallurgical Engineering',
          year: 1989,
          abstract_scope:
            'Specifies nominal dimensions, mass, tolerances, and sectional geometric properties for Indian standard hot-rolled structural steel sections produced by Indian rolling mills.',
          url: 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/knowyourstandards/indian_standards/isdetails/830'
        },
        {
          is_code: 'IS 875 (Part 3) : 2015',
          title: 'Design Loads (Other than Earthquake) for Buildings and Structures — Part 3: Wind Loads',
          confidence: 85,
          confidence_tier: 'high',
          highlight_reason:
            'CRITICAL FOR STEEL SHEDS & TOWERS: Calculates design wind speed Vz = Vb * k1 * k2 * k3 * k4 and design wind pressure pz = 0.6 * Vz^2. Provides external and internal pressure coefficients (Cpe, Cpi) for pitched industrial roofs and open-web structures.',
          key_clauses: [
            'Clause 6.2: Design Wind Speed Vz and Terrain Factors (k1, k2, k3, k4)',
            'Clause 7.2: Basic Wind Pressure Equations',
            'Table 5: External Pressure Coefficients (Cpe) for Pitched Roofs of Industrial Sheds'
          ],
          division: 'Civil Engineering',
          year: 2015,
          abstract_scope:
            'Gives guidelines for calculating wind loads on structures, structural components, and cladding for all buildings, industrial steel frames, and communication towers in India.',
          url: 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/knowyourstandards/indian_standards/isdetails/899'
        },
        {
          is_code: 'IS 4000 : 1992',
          title: 'Code of Practice for High Strength Bolts in Steel Structures',
          confidence: 72,
          confidence_tier: 'moderate',
          highlight_reason:
            'HSFG bolting code: Details slip-critical friction grip connections using grade 8.8 and 10.9 high strength bolts, bolt pre-tensioning torques, washer requirements, and slip factors.',
          key_clauses: [
            'Clause 5: Clearance Hole Tolerances for M16-M36 Bolts',
            'Clause 7: Torque and Turn-of-Nut Tightening Methods',
            'Clause 8: Slip Factor Values for Blast Cleaned Steel Surfaces'
          ],
          division: 'Civil Engineering',
          year: 1992,
          abstract_scope:
            'Provides rules for the design, fabrication, and assembly of structural joints using high-strength friction grip bolts in bridges, cranes, and high-rise frames.',
          url: 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/knowyourstandards/indian_standards/isdetails/4240'
        },
        {
          is_code: 'IS 9595 : 1996',
          title: 'Recommendation for Metal Arc Welding of Carbon and Carbon Manganese Steels',
          confidence: 56,
          confidence_tier: 'moderate',
          highlight_reason:
            'Welding fabrication guidelines: Governs edge preparation, preheat temperatures to avoid hydrogen cracking in thick plates, and non-destructive ultrasonic/radiographic weld inspection.',
          key_clauses: [
            'Clause 6: Minimum Preheat and Interpass Temperature Tables',
            'Clause 8: Welded Joint Geometry, Root Gap, and Fillet Throat Thickness'
          ],
          division: 'Metallurgical Engineering',
          year: 1996,
          abstract_scope:
            'Sets forth general recommendations for metal arc welding of carbon and carbon manganese structural steels used in heavy load-bearing fabrications.',
          url: 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/knowyourstandards/indian_standards/isdetails/9800'
        }
      ]
    }
  },

  // =========================================================================
  // TOPIC 6: FOOD SAFETY PACKAGING NORMS
  // =========================================================================
  food_packaging: {
    id: 'food_packaging',
    category: 'Chemical / Food & Agriculture',
    keywords: [
      'food safety', 'packaging', 'food packaging', 'is 9845', 'is 10146',
      'is 10171', 'is 12252', 'is 14534', 'is 6615', 'overall migration',
      'plastic packaging', 'food contact', 'heavy metals', 'pet bottle',
      'food grade', 'fssai', 'leaching', 'carton', 'plastic waste', 'polyethylene'
    ],
    sampleQueries: [
      'Food safety packaging norms',
      'BIS standards for plastic packaging in contact with food',
      'Overall migration limits and testing IS 9845',
      'Polyethylene food grade specification IS 10146',
      'PET bottle safety and migration limits for edible packaging'
    ],
    data: {
      summary:
        "Food contact packaging in India is regulated jointly by BIS and FSSAI Packaging Regulations. Plastic polymers must comply with IS 9845 for overall migration limits (max 60 mg/kg or 10 mg/dm²). Specific resin purity codes include IS 10146 (Polyethylene), IS 10171 (Suitability Guide), and IS 12252 (PET containers). Recycled plastics in direct food contact are prohibited.",
      query_magnified:
        'IS 9845 overall migration testing, simulants 3% acetic acid n-heptane, IS 10146 food grade polyethylene LDPE HDPE, IS 10171 plastic food compatibility guide, IS 12252 PET bottles acetaldehyde limits, IS 14534 resin recycling codes, IS 6615 food grade paperboard',
      standards: [
        {
          is_code: 'IS 9845 : 1998',
          title: 'Determination of Overall Migration of Constituents of Plastics Materials and Articles in Contact with Foodstuffs',
          confidence: 99,
          confidence_tier: 'high',
          highlight_reason:
            'THE BENCHMARK MIGRATION TESTING CODE: Referenced by FSSAI & BIS. Tests chemical leaching using food simulants (Distilled water for aqueous, 3% Acetic acid for acidic, 15% Ethanol for alcohol, n-Heptane for fatty foods). Establishes maximum overall migration limit of 60 mg/kg or 10 mg/dm².',
          key_clauses: [
            'Clause 4: Food Simulants Selection Matrix and Food Categorisation',
            'Clause 6: Exposure Conditions (Time and Temperature Simulation)',
            'Clause 8: Gravimetric Determination of Extractive Residue',
            'Table 1: Maximum Permissible Migration Threshold (60 mg/kg or 10 mg/dm²)'
          ],
          division: 'Chemical / Petroleum and Plastics',
          year: 1998,
          abstract_scope:
            'Prescribes methods of analysis for determining the overall migration of non-volatile constituents of plastic materials, coatings, and containers intended for direct contact with food and potable beverages.',
          url: 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/knowyourstandards/indian_standards/isdetails/10080'
        },
        {
          is_code: 'IS 10146 : 1982',
          title: 'Specification for Polyethylene for Its Safe Use in Contact with Foodstuffs, Pharmaceuticals and Drinking Water',
          confidence: 96,
          confidence_tier: 'high',
          highlight_reason:
            'MANDATORY RESIN STANDARD: Governs Low-Density (LDPE), Linear Low-Density (LLDPE), and High-Density (HDPE) resins. Enforces strict residual monomer limits, catalyst controls, and total heavy metals (Lead, Cadmium, Mercury, Arsenic < 100 ppm). Prohibits post-consumer recycled plastic for food contact.',
          key_clauses: [
            'Clause 4: Purity Requirements of Basic Polyethylene Polymer Resin',
            'Clause 5: Permissible Antioxidants, Slip Agents and Processing Aids',
            'Clause 6: Toxicological Limits for Heavy Metals and Monomers'
          ],
          division: 'Chemical / Plastics',
          year: 1982,
          abstract_scope:
            'Specifies requirements and methods of sampling and test for polyethylene materials intended for the manufacture of containers, liners, wraps, and closures in contact with food and pharma products.',
          url: 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/knowyourstandards/indian_standards/isdetails/10375'
        },
        {
          is_code: 'IS 10171 : 1999',
          title: 'Guide on Suitability of Plastics for Food Packaging (First Revision)',
          confidence: 91,
          confidence_tier: 'high',
          highlight_reason:
            'ENGINEERING COMPATIBILITY GUIDE: Provides a detailed selection table matching specific foodstuffs (edible oils, milk, spices, snacks, carbonated drinks) with appropriate polymers (PET, PP, HDPE, multilayer EVOH) based on oxygen and moisture barrier protection.',
          key_clauses: [
            'Section 3: Classification of Foodstuffs by Moisture, Acidity & Fat Content',
            'Section 4: Barrier Performance Criteria (MVTR and OTR Permeability)',
            'Table 2: Polymer Compatibility Guide with 40+ Food Categories'
          ],
          division: 'Food and Agriculture / Chemical',
          year: 1999,
          abstract_scope:
            'Provides guidance to food processors and package designers on selecting the safest, most chemically inert plastic films and laminates for preserving various packaged foods.',
          url: 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/knowyourstandards/indian_standards/isdetails/10400'
        },
        {
          is_code: 'IS 12252 : 2017',
          title: 'Polyalkylene Terephthalates (PET) for Its Safe Use in Contact with Foodstuffs and Drinking Water',
          confidence: 87,
          confidence_tier: 'high',
          highlight_reason:
            'PET BOTTLES & JARS: Standard for water bottles, cooking oil jars, and edible blister trays. Mandates residual acetaldehyde limits (<3 ppm in preforms) and antimony catalyst migration thresholds (<0.04 mg/kg).',
          key_clauses: [
            'Clause 4: Raw Material Specifications for Food-grade PET and PBT',
            'Clause 5: Maximum Acetaldehyde and Ethylene Glycol Leaching Limits',
            'Clause 7: Specific Migration Limits for Antimony and Heavy Metals'
          ],
          division: 'Chemical',
          year: 2017,
          abstract_scope:
            'Specifies quality criteria for virgin PET and PBT thermoplastic polymers fabricated into bottles, film wrappers, and trays holding food, water, and medicines.',
          url: 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/knowyourstandards/indian_standards/isdetails/12470'
        },
        {
          is_code: 'IS 14534 : 1998',
          title: 'Guidelines for Recovery and Recycling of Plastics (Marking & Identification)',
          confidence: 71,
          confidence_tier: 'moderate',
          highlight_reason:
            'MANDATORY RESIN CODING: Enforces the 1 to 7 chasing-arrows recycle symbols on all plastic packaging (1=PETE, 2=HDPE, 3=PVC, 4=LDPE, 5=PP, 6=PS, 7=OTHER) under Plastic Waste Management Rules in India.',
          key_clauses: [
            'Clause 4: Resin Identification Numbers and Triangular Recycling Symbols',
            'Clause 5: Minimum Embossing Size and Legibility on Containers'
          ],
          division: 'Chemical / Plastics',
          year: 1998,
          abstract_scope:
            'Prescribes standardized identification markings for plastic containers to facilitate waste segregation, mechanical recycling, and environmental compliance.',
          url: 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/knowyourstandards/indian_standards/isdetails/14670'
        },
        {
          is_code: 'IS 6615 : 2021',
          title: 'Paper and Board in Direct Contact with Foodstuffs — Specification',
          confidence: 62,
          confidence_tier: 'moderate',
          highlight_reason:
            'ECO-FRIENDLY PACKAGING: Regulates paper cups, plates, burger boxes, and pizza cartons. Prohibits toxic optical brighteners (OBAs), limits residual formaldehyde, and enforces sensory neutral taste/odour transfer tests.',
          key_clauses: [
            'Clause 4: Chemical Purity Criteria and Heavy Metal Limits in Paper Pulp',
            'Clause 6: Absence of Fluorescent Whitening Agent Migration',
            'Clause 8: Organoleptic Odour and Flavour Taint Tests'
          ],
          division: 'Chemical / Paper',
          year: 2021,
          abstract_scope:
            'Specifies requirements for paper, paperboard, and corrugated boxes meant for wrapping or serving hot, cold, dry, or fatty food items.',
          url: 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/knowyourstandards/indian_standards/isdetails/6780'
        }
      ]
    }
  },

  // =========================================================================
  // TOPIC 7: PAINTS, ENAMELS & CHEMICAL COATINGS
  // =========================================================================
  paints_coatings: {
    id: 'paints_coatings',
    category: 'Chemical',
    keywords: [
      'paint', 'paints', 'painting', 'coating', 'coatings', 'varnish', 'enamel',
      'distemper', 'primer', 'lead content', 'lead in paint', 'paint manufacturing',
      'is 15489', 'is 133', 'is 2932', 'is 5410', 'is 101', 'voc', 'qco', 'wall paint'
    ],
    sampleQueries: [
      'paint manufacturing',
      'paint',
      'paints',
      'paints and varnishes standards',
      'lead limit in paint bis',
      'synthetic enamel paint specification',
      'interior wall paint standard'
    ],
    data: {
      summary:
        "Paint manufacturing in India is governed by strict chemical safety standards under the Regulation of Lead Contents in Household and Decorative Paints Rules and BIS Quality Control Orders. IS 15489 strictly mandates a maximum lead concentration of 90 ppm to prevent toxic exposure, alongside IS 133 for interior enamels, IS 2932 for exterior synthetic enamels, and IS 101 for standard laboratory test methods.",
      query_magnified:
        'paint manufacturing, paints and varnishes, IS 15489 lead content limits 90 ppm, IS 133 interior enamel, IS 2932 synthetic exterior enamel, IS 101 test methods, BIS ISI mark license, chemical division',
      standards: [
        {
          is_code: 'IS 15489 : 2004',
          title: 'Paints, Enamels and Related Products — Specification for Cross-Cut Adhesion and Lead Content Limits',
          confidence: 96,
          confidence_tier: 'high',
          highlight_reason:
            'PRIMARY STATUTORY SAFETY STANDARD: Imposes mandatory restriction on lead content (maximum 90 ppm / 90 mg/kg dry film weight) for decorative, architectural, and household paints under Government of India Gazette notification.',
          key_clauses: [
            'Clause 4: Maximum Permissible Lead Content (90 ppm dry weight)',
            'Clause 5: Cross-Cut Adhesion Tape Test (Classification 0 to 5)',
            'Clause 7: Mandatory Safety Labeling and Warning Declarations'
          ],
          division: 'Chemical',
          year: 2004,
          abstract_scope:
            'Specifies allowable toxic heavy metal thresholds, especially lead and volatile organic compounds (VOCs), for household and industrial paints, ensuring safety for residential living spaces.',
          url: 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/knowyourstandards/indian_standards/isdetails/15489'
        },
        {
          is_code: 'IS 133 : 2013',
          title: 'Enamel, Interior, (a) Undercoating, (b) Finishing — Specification',
          confidence: 91,
          confidence_tier: 'high',
          highlight_reason:
            'ARCHITECTURAL ENAMEL: Prescribes drying time, finish gloss level, surface opacity, scratch resistance, and flexibility on wood, metal, and masonry substrates.',
          key_clauses: [
            'Clause 6: Drying Time (Surface dry < 4h, Hard dry < 18h)',
            'Clause 8: Specular Gloss at 60 degrees (> 85 units)',
            'Clause 10: Scratch Hardness and Adhesion Conformance'
          ],
          division: 'Chemical',
          year: 2013,
          abstract_scope:
            'Specifies requirements for interior air-drying synthetic enamel used for protective and decorative finishing on primed surfaces.',
          url: 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/knowyourstandards/indian_standards/isdetails/133'
        },
        {
          is_code: 'IS 2932 : 2013',
          title: 'Enamel, Synthetic, Exterior: (a) Undercoating, (b) Finishing — Specification',
          confidence: 86,
          confidence_tier: 'high',
          highlight_reason:
            'EXTERIOR WEATHERPROOFING: Mandates accelerated weathering resistance, UV stability, and resistance to water immersion without blistering or chalking.',
          key_clauses: [
            'Clause 7: Accelerated Weathering Exposure (1000 hours UV test)',
            'Clause 9: Resistance to Continuous Water Immersion',
            'Clause 12: Recoating Properties and Flexibility'
          ],
          division: 'Chemical',
          year: 2013,
          abstract_scope:
            'Covers synthetic exterior enamel suitable for harsh outdoor climatic conditions, marine environments, and industrial plant structures.',
          url: 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/knowyourstandards/indian_standards/isdetails/2932'
        },
        {
          is_code: 'IS 101 (Part 1 to 9)',
          title: 'Methods of Sampling and Test for Paints, Varnishes and Related Products',
          confidence: 80,
          confidence_tier: 'high',
          highlight_reason:
            'MANDATORY TESTING CODE: The definitive laboratory test standard in India governing viscosity, flash point, drying time, volatile matter, and pigment analysis for all paint manufacturers.',
          key_clauses: [
            'Part 1/Sec 5: Consistency and Flow by Ford Cup Viscometer',
            'Part 3/Sec 1: Determination of Total Volatile Matter at 105°C',
            'Part 5/Sec 2: Wet Abrasion and Washability Test'
          ],
          division: 'Chemical',
          year: 2015,
          abstract_scope:
            'Standardized procedures for physical and chemical evaluation of coatings, establishing criteria for NABL laboratory verification.',
          url: 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/knowyourstandards/indian_standards/isdetails/101'
        },
        {
          is_code: 'IS 5410 : 2013',
          title: 'Cement Paint, Colour as Required — Specification',
          confidence: 74,
          confidence_tier: 'moderate',
          highlight_reason:
            'MASONRY WATERPROOF COATING: Governs Portland cement-based powder paints for porous concrete and exterior building plaster, establishing minimum opacity and water repellency.',
          key_clauses: [
            'Clause 5: Portland Cement Content (Minimum 60% by mass)',
            'Clause 7: Water Absorption of Treated Masonry Block',
            'Clause 9: Durability and Color Fastness under Sunlight'
          ],
          division: 'Chemical / Civil',
          year: 2013,
          abstract_scope:
            'Specifies composition and testing for dry cement powder paint formulated with white/grey Portland cement, lime, pigments, and water repellents.',
          url: 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/knowyourstandards/indian_standards/isdetails/5410'
        }
      ]
    }
  },

  // =========================================================================
  // TOPIC 8: CEMENT, CONCRETE & STRUCTURAL MATERIALS
  // =========================================================================
  cement_concrete: {
    id: 'cement_concrete',
    category: 'Civil',
    keywords: [
      'cement', 'opc', 'ppc', 'ordinary portland cement', 'concrete', 'rcc',
      'is 269', 'is 456', 'is 1489', 'is 8112', 'is 12269', '33 grade', '43 grade', '53 grade',
      'compressive strength', 'setting time', 'clinker', 'fly ash'
    ],
    sampleQueries: [
      'cement standards',
      'ordinary portland cement manufacturing',
      'concrete mix design',
      'IS 269 cement'
    ],
    data: {
      summary:
        "Cement manufacturing in India is strictly regulated under the Cement Quality Control Order, making BIS certification (Scheme-I ISI mark) compulsory before sale. IS 269 governs 33, 43, and 53 Grade Ordinary Portland Cement, establishing mandatory 28-day compressive strength, Blaine fineness (min 225 m²/kg), and sound test limits.",
      query_magnified:
        'cement standards, IS 269 ordinary portland cement, IS 456 plain and reinforced concrete, IS 1489 portland pozzolana cement, mandatory QCO, compressive strength, setting time',
      standards: [
        {
          is_code: 'IS 269 : 2015',
          title: 'Ordinary Portland Cement — Specification (33, 43 and 53 Grade)',
          confidence: 98,
          confidence_tier: 'high',
          highlight_reason:
            'COMPULSORY STATUTORY STANDARD: Covers physical and chemical requirements for 33, 43, and 53 grade cement. Enforces strict lime saturation factor (0.66-1.02), max magnesia 6%, and setting time limits.',
          key_clauses: [
            'Clause 5: Chemical Requirements (Insoluble residue, SO3, Magnesia)',
            'Clause 6: Physical Requirements (Initial setting > 30 min, Final < 600 min)',
            'Clause 7: 28-Day Compressive Strength Benchmarks'
          ],
          division: 'Civil',
          year: 2015,
          abstract_scope:
            'Prescribes manufacturing parameters, chemical composition limits, and mechanical strength requirements for Ordinary Portland Cement.',
          url: 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/knowyourstandards/indian_standards/isdetails/269'
        },
        {
          is_code: 'IS 456 : 2000',
          title: 'Plain and Reinforced Concrete — Code of Practice',
          confidence: 94,
          confidence_tier: 'high',
          highlight_reason:
            'THE NATIONAL CONCRETE CODE: Primary standard for structural engineers across India specifying design, durability, water-cement ratios, and curing requirements.',
          key_clauses: [
            'Clause 5: Quality of Cement, Aggregates, Water and Admixtures',
            'Clause 8: Durability Requirements and Minimum Cement Content',
            'Clause 15: Sampling and Acceptance Criteria for Concrete Strength'
          ],
          division: 'Civil',
          year: 2000,
          abstract_scope:
            'Applies to the use of plain and reinforced concrete in general building and civil engineering construction.',
          url: 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/knowyourstandards/indian_standards/isdetails/456'
        },
        {
          is_code: 'IS 1489 (Part 1) : 2015',
          title: 'Portland Pozzolana Cement — Specification (Fly Ash Based)',
          confidence: 88,
          confidence_tier: 'high',
          highlight_reason:
            'ECO-FRIENDLY CEMENT: Regulates fly-ash blended cement (15-35% pozzolana) with high sulfate resistance and low heat of hydration.',
          key_clauses: [
            'Clause 4: Pozzolanic Material Content (15% to 35% Fly Ash by mass)',
            'Clause 6: Soundness and Le-Chatelier Expansion (Max 10 mm)',
            'Clause 8: Compressive Strength (28-day min 33 MPa)'
          ],
          division: 'Civil',
          year: 2015,
          abstract_scope:
            'Specification for fly-ash based Portland Pozzolana Cement for hydraulic structures, marine construction, and general RCC work.',
          url: 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/knowyourstandards/indian_standards/isdetails/1489'
        }
      ]
    }
  },

  // =========================================================================
  // TOPIC 9: SOLAR PHOTOVOLTAIC & INVERTERS
  // =========================================================================
  solar_pv: {
    id: 'solar_pv',
    category: 'Electrotechnical',
    keywords: [
      'solar', 'solar panel', 'photovoltaic', 'pv module', 'inverter', 'solar inverter',
      'is 14286', 'is 16221', 'is 61730', 'mnre', 'crs', 'grid tied', 'rooftop solar'
    ],
    sampleQueries: [
      'solar panel manufacturing standards',
      'solar inverter bis requirements',
      'photovoltaic module testing'
    ],
    data: {
      summary:
        "Solar photovoltaic modules and power inverters in India are subject to mandatory registration under the Solar Photovoltaics, Systems, Devices and Components Goods (Requirements for Compulsory Registration) Order by MNRE and BIS. IS 14286 governs design qualification and type approval for crystalline silicon modules, ensuring resistance to UV degradation, thermal cycling, and hail impact.",
      query_magnified:
        'solar panel manufacturing, photovoltaic modules, IS 14286 design qualification, IS 16221 grid tied power inverter safety, MNRE compulsory registration scheme CRS, damp heat testing',
      standards: [
        {
          is_code: 'IS 14286 : 2010',
          title: 'Crystalline Silicon Terrestrial Photovoltaic (PV) Modules — Design Qualification and Type Approval',
          confidence: 96,
          confidence_tier: 'high',
          highlight_reason:
            'COMPULSORY MNRE REGISTRATION: Mandates environmental stress testing (thermal cycling 200 cycles, damp-heat 1000 hours at 85°C/85% RH, mechanical load 2400 Pa).',
          key_clauses: [
            'Clause 10.11: Thermal Cycling Test (-40°C to +85°C)',
            'Clause 10.13: Damp Heat Test (1000 hours at 85% RH)',
            'Clause 10.16: Mechanical Load Test (Wind & Snow 2400 Pa)'
          ],
          division: 'Electrotechnical',
          year: 2010,
          abstract_scope:
            'Lays down requirements for design qualification and type approval of terrestrial photovoltaic modules suitable for long-term outdoor operation in general open-air climates.',
          url: 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/knowyourstandards/indian_standards/isdetails/14286'
        },
        {
          is_code: 'IS 16221 (Part 2) : 2015',
          title: 'Safety of Power Converters for Use in Photovoltaic Power Systems — Particular Requirements for Inverters',
          confidence: 92,
          confidence_tier: 'high',
          highlight_reason:
            'MANDATORY SOLAR INVERTER CODE: Specifies electrical safety, anti-islanding protection, IP protection (IP65 exterior), and insulation coordination for grid-interactive and standalone inverters.',
          key_clauses: [
            'Clause 4: Protection Against Electric Shock and Arc Faults',
            'Clause 7: Enclosure Environmental Ingress Protection (IP65)',
            'Clause 9: Grid Disconnection & Anti-Islanding Trip Times'
          ],
          division: 'Electrotechnical',
          year: 2015,
          abstract_scope:
            'Applies to grid-connected and standalone inverters used in photovoltaic energy systems up to 1000V DC.',
          url: 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/knowyourstandards/indian_standards/isdetails/16221'
        }
      ]
    }
  }
};
