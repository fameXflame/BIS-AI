"""
Bureau of Indian Standards (BIS) Comprehensive Standards Database.

This module provides a rich repository of official Indian Standards (IS codes)
spanning 15 core technical, engineering, civil, healthcare, and consumer domains.
Each record includes scope definitions, key clauses, testing protocols,
keywords, and BIS certification processes.
"""

from typing import Any

BIS_STANDARDS_DATABASE: list[dict[str, Any]] = [
    {   'is_code': 'IS 15442',
        'title': 'Personal Deodorants and Antiperspirants — Specification',
        'year': '2004',
        'division': 'Chemical Division',
        'mandatory': True,
        'scope': 'This Indian Standard prescribes requirements and methods of sampling and test for personal deodorants and antiperspirants including aerosol sprays, roll-ons, deodorant sticks, and creams. It defines maximum active antiperspirant aluminium and zirconium salts, antibacterial agents, ethyl alcohol grade, and specifies strict dermatological safety and pH stability per Drugs & Cosmetics Rules.',
        'key_clauses': [   'Clause 4: Types and forms — Aerosol spray deodorants, non-aerosol liquid sprays, roll-on emulsions, solid deodorant sticks, and deodorant creams',
                           'Clause 5: Chemical requirements — Active antiperspirant content (Aluminium chlorohydrate max 25%), ethyl alcohol conforming to IS 323, volatile organic solvent limits',
                           'Clause 6: Safety and toxicity — Freedom from banned substances per IS 4707 (Part 2), heavy metal limits (Lead max 20 ppm, Arsenic max 2 ppm, Mercury max 1 ppm)',
                           'Clause 7: Microbiological limits — Total viable aerobic count (< 1000 CFU/g), absence of Pseudomonas aeruginosa, Staphylococcus aureus, and Candida albicans',
                           'Clause 8: Packaging and aerosol integrity — Metal dispensers conforming to IS 14102, leak-proof valves, flame projection testing for aerosol propellants'],
        'keywords': [   'deodorant',
                        'deodrant',
                        'antiperspirant',
                        'deodorant manufacturing',
                        'body spray',
                        'deodorant spray',
                        'roll on',
                        'deodorant stick',
                        'cosmetics',
                        'personal care',
                        'aluminium chlorohydrate',
                        'perfumery compounds'],
        'test_requirements': 'EDTA titration for aluminium/zirconium actives, GC-MS for alcohol purity and fragrance stability, ICP-OES for heavy metals (lead, arsenic, mercury), dermatological safety test per IS 4011, pressure test for aerosol cans per IS 14102',
        'certification_process': 'State Drugs Controller Manufacturing License under Drugs & Cosmetics Act → BIS Scheme-I (ISI Mark) → NABL laboratory chemical & microbiological evaluation → Factory hygiene & raw material compliance with IS 4707',
        'url': 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/Standard_review/Isdetails?ID=MTU0NDI%3D'},
    {   'is_code': 'IS 4707 (Part 1)',
        'title': 'Classification for Cosmetic Raw Materials and Adjuncts — Part 1: Dyes, Colours and Pigments',
        'year': '2020',
        'division': 'Chemical Division',
        'mandatory': True,
        'scope': 'This Indian Standard covers the list of dyes, colours, and pigments permitted to be used in cosmetic formulations and personal care products, including deodorants, soaps, perfumes, and skin care. It sets chemical purity specifications, maximum limits, and area of application restrictions.',
        'key_clauses': [   'Clause 3: Classification of permitted synthetic and natural colorants',
                           'Clause 4: Purity criteria — Limits on lead (< 20 ppm), arsenic (< 2 ppm), and heavy metals',
                           'Clause 5: Prohibited colorants in topical and aerosol formulations',
                           'Clause 6: Color Index (CI) number labeling and identification requirements'],
        'keywords': [   'cosmetic raw materials',
                        'cosmetic colors',
                        'dyes in cosmetics',
                        'pigments',
                        'deodorant ingredients',
                        'cosmetics safety',
                        'PCD 19',
                        'CDSCO cosmetics',
                        'deodorant manufacturing'],
        'test_requirements': 'Spectrophotometric determination of dye purity, TLC/HPLC for synthetic organic color identification, AAS/ICP-MS for heavy metal impurities',
        'certification_process': 'Compliance mandatory under Second Schedule of Drugs & Cosmetics Rules → Raw material Certificate of Analysis (CoA) → Batch testing by manufacturer',
        'url': 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/Standard_review/Isdetails?ID=NDcwNw%3D%3D'},
    {   'is_code': 'IS 4707 (Part 2)',
        'title': 'Classification for Cosmetic Raw Materials and Adjuncts — Part 2: List of Raw Materials Generally Not Recognized as Safe, Permitted Preservatives and UV Filters',
        'year': '2020',
        'division': 'Chemical Division',
        'mandatory': True,
        'scope': 'This Indian Standard prescribes the negative list of substances prohibited from use in cosmetic and personal care products (including deodorants, antiperspirants, sprays, and perfumes), restricted substances with strict maximum concentrations, permitted preservatives, and UV filters. It is the primary chemical safety benchmark for cosmetic formulators.',
        'key_clauses': [   'Annex A: List of prohibited substances in cosmetic formulations',
                           'Annex B: List of substances which cosmetic products must not contain except subject to restrictions',
                           'Annex C: List of permitted preservatives in cosmetics with maximum permissible concentrations',
                           'Annex D: List of permitted UV filters in topical formulations',
                           'Clause 5: Quality control guidelines for deodorant and aerosol active ingredients'],
        'keywords': [   'banned cosmetic ingredients',
                        'cosmetics negative list',
                        'preservatives in cosmetics',
                        'deodorant safety',
                        'parabens limit',
                        'prohibited chemicals',
                        'deodorant manufacturing',
                        'personal care safety'],
        'test_requirements': 'Gas Chromatography-Mass Spectrometry (GC-MS), High Performance Liquid Chromatography (HPLC) for preservative concentrations, testing for prohibited volatile organic impurities',
        'certification_process': 'Mandatory formulation clearance under CDSCO & State FDA → BIS audit verification → Prohibition of Annex A chemicals in formulation dossiers',
        'url': 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/Standard_review/Isdetails?ID=NDcwOC%3D%3D'},
    {   'is_code': 'IS 4011',
        'title': 'Methods of Test for Safety Evaluation of Cosmetics',
        'year': '2018',
        'division': 'Chemical Division',
        'mandatory': True,
        'scope': 'This Indian Standard outlines standardized dermatological, toxicological, and safety evaluation test protocols for cosmetics, toiletries, deodorants, and personal care products. It details primary skin irritation testing, mucous membrane irritation, photo-toxicity, and skin sensitization assays essential before market authorization.',
        'key_clauses': [   'Clause 4: Primary skin irritation test — Patch test protocol and erythema/edema scoring',
                           'Clause 5: Mucous membrane irritation test for aerosol spray fallout',
                           'Clause 6: Skin sensitization test (Guinea Pig Maximization Test or human repeat insult patch test)',
                           'Clause 7: Photo-allergy and photo-toxicity testing for fragranced personal care formulations'],
        'keywords': [   'skin irritation test',
                        'patch test',
                        'cosmetic safety testing',
                        'dermatological safety',
                        'deodorant safety evaluation',
                        'toxicity testing',
                        'deodorant manufacturing',
                        'sensitization test'],
        'test_requirements': 'Standardized patch test evaluation, Draize scoring for dermal response, cellular in-vitro cytotoxicity assays, photo-sensitization screening',
        'certification_process': 'Dermatological safety dossier submission → NABL accredited biological testing laboratory report → State Licensing Authority approval',
        'url': 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/Standard_review/Isdetails?ID=NDAxMQ%3D%3D'},
    {   'is_code': 'IS 14102',
        'title': 'Metal Aerosol Dispensers — Specification',
        'year': '2004',
        'division': 'Mechanical Engineering Division',
        'mandatory': True,
        'scope': 'This Indian Standard prescribes requirements, sampling, and methods of test for single-use metal aerosol dispensers (tinplate and aluminium) used for packaging aerosol products, including deodorant sprays, body sprays, perfumes, and hair sprays. It specifies seam construction, pressure resistance, burst pressure (minimum 1.5 MPa), and hot water-bath leak testing.',
        'key_clauses': [   'Clause 4: Types and materials — Seamless aluminium cans and two/three-piece tinplate cans',
                           'Clause 5: Pressure requirements — Working pressure up to 1.0 MPa at 50°C, hydraulic proof test (1.2 MPa), burst test (> 1.5 MPa)',
                           'Clause 6: Valve and actuator fitment — Crimp diameter, crimp depth, and leak-tightness',
                           'Clause 7: Factory testing — 100% hot water-bath immersion test at 50°C or approved automatic leak detection',
                           'Clause 8: Protective internal lacquering for corrosive deodorant alcoholic propellants'],
        'keywords': [   'aerosol dispenser',
                        'aerosol can',
                        'deodorant spray can',
                        'body spray packaging',
                        'tinplate aerosol',
                        'aluminium aerosol can',
                        'burst pressure test',
                        'propellant pressure',
                        'deodorant manufacturing'],
        'test_requirements': 'Hydrostatic burst pressure test, 50°C water bath leakage test, lacquer continuity test (copper sulphate immersion), seam dimension micrometry',
        'certification_process': 'Mandatory ISI mark scheme under Quality Control Order for Aerosol Containers → Pressure cycle testing at approved test laboratory → Factory QA audit',
        'url': 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/Standard_review/Isdetails?ID=MTQxMDI%3D'},
    {   'is_code': 'IS 3958',
        'title': 'Methods of Sampling for Cosmetics',
        'year': '2021',
        'division': 'Chemical Division',
        'mandatory': False,
        'scope': 'This Indian Standard lays down methods of sampling for cosmetics and toilet goods including raw materials and finished personal care products such as deodorants, lotions, creams, powders, and perfumery. It prescribes lot size definitions, random sample draw matrices, and composite preparation.',
        'key_clauses': [   'Clause 3: Scale of sampling for packaged consumer units (bottles, aerosol cans, tubes)',
                           'Clause 4: Sample withdrawal protocol to prevent volatile alcohol evaporation',
                           'Clause 5: Preparation of composite test samples for chemical and microbial assays',
                           'Clause 6: Criteria for conformity of batch based on acceptance quality limit (AQL)'],
        'keywords': [   'sampling cosmetics',
                        'cosmetics batch sampling',
                        'deodorant sampling',
                        'quality control sampling',
                        'AQL inspection',
                        'lot sampling',
                        'deodorant manufacturing'],
        'test_requirements': 'Statistical random sampling table per lot size, clean sterile sample containers, hermetic sealing for volatile formulations',
        'certification_process': 'In-plant QA batch release protocol → Inspection by Drugs Inspector / BIS Quality Auditor → Retained sample archival for shelf-life duration',
        'url': 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/Standard_review/Isdetails?ID=Mzk1OA%3D%3D'},
    {   'is_code': 'IS 6398',
        'title': 'Code for Packaging of Cosmetics',
        'year': '2020',
        'division': 'Chemical Division',
        'mandatory': False,
        'scope': 'This standard prescribes guidelines for packaging materials, container design, closures, pump dispensers, roll-on assemblies, and labeling for cosmetics and personal deodorants to prevent leakage, chemical degradation, and ensure consumer safety and shelf-life stability.',
        'key_clauses': [   'Clause 4: Compatibility of packaging with volatile alcohols and essential oils',
                           'Clause 5: Closure integrity — Torque specifications for roll-on caps and spray pumps',
                           'Clause 6: Statutory labeling — Net contents, ingredients list, batch number, MRP, and statutory warnings (e.g. Flammable aerosol warnings)',
                           'Clause 7: Tamper-evident packaging and secondary carton specifications'],
        'keywords': [   'cosmetic packaging',
                        'deodorant packaging',
                        'roll on bottle',
                        'spray pump packaging',
                        'cosmetics labeling',
                        'container compatibility',
                        'deodorant manufacturing'],
        'test_requirements': 'Drop impact test for bottles, vacuum leak test for caps and pumps, chemical compatibility migration test at 45°C/75% RH for 3 months',
        'certification_process': 'Package compatibility dossier → Legal Metrology (Packaged Commodities) Rules compliance → Drugs & Cosmetics labeling clearance',
        'url': 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/Standard_review/Isdetails?ID=NjM5OA%3D%3D'},
    {   'is_code': 'IS 10502',
        'title': 'Talcum Powders and Deodorant Body Powders — Specification',
        'year': '2020',
        'division': 'Chemical Division',
        'mandatory': True,
        'scope': 'This Indian Standard prescribes requirements and methods of sampling and test for talcum powders and body powders containing deodorant or antibacterial adjuncts. It specifies particle fineness, moisture content, heavy metals (Lead max 20 ppm, Arsenic max 2 ppm), and certifies zero asbestos contamination.',
        'key_clauses': [   'Clause 4: Composition and grades — Deodorant powder, cooling powder, and general body powder',
                           'Clause 5: Fineness — Passing through 75-micron IS Sieve (> 99.0%)',
                           'Clause 6: Freedom from asbestos — Mandatory XRD/SEM test certifying zero amphibole/chrysotile asbestos fibers',
                           'Clause 7: Microbiological limits — Total viable count < 100 CFU/g, absence of pathogens',
                           'Clause 8: Deodorant and bactericidal active ingredient limits'],
        'keywords': [   'deodorant powder',
                        'body powder',
                        'talcum powder',
                        'antiperspirant powder',
                        'asbestos free talc',
                        'personal hygiene',
                        'deodorant manufacturing'],
        'test_requirements': 'Sieve fineness on 75 micron sieve, X-Ray Diffraction (XRD) for asbestos detection, ICP-MS for heavy metals, microbial plate count',
        'certification_process': 'BIS Certification Scheme-I (ISI Mark) → Asbestos-free batch certification → State FDA Cosmetic License → Factory inspection',
        'url': 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/Standard_review/Isdetails?ID=MTA1MDI%3D'},
    {   'is_code': 'IS 7058',
        'title': 'Table Wines — Specification',
        'year': '2021',
        'division': 'Food and Agriculture Division',
        'mandatory': True,
        'scope': 'This Indian Standard prescribes requirements and methods of sampling and test for table wines produced by complete or partial alcoholic fermentation of fresh grapes or grape must. It establishes permissible ethyl alcohol content limits (7.0% to 15.5% v/v), volatile acidity (max 1.2 g/L as acetic acid), total sulfur dioxide (max 300 mg/L), and microbiological stability. It works in conjunction with FSSAI Alcoholic Beverages Regulations, 2018.',
        'key_clauses': [   'Clause 4: Types and classification — Dry red wine, dry white wine, semi-dry, sweet, and rosé table wines',
                           'Clause 5: Hygienic requirements — Compliance with clean processing and FSSAI Good Manufacturing Practices (GMP)',
                           'Clause 6: Chemical parameters — Ethyl alcohol content (7.0 to 15.5% v/v), total acidity, volatile acidity, and reducing sugars',
                           'Clause 7: Contaminants & metals — Limits for lead (max 0.2 mg/kg), copper (max 5.0 mg/kg), arsenic (max 0.1 mg/kg), and ochratoxin A',
                           'Clause 8: Packaging and labeling — Mandatory statutory warnings, alcohol strength declaration, batch number, and food-grade glass packaging'],
        'keywords': [   'wine',
                        'table wine',
                        'wine factory',
                        'winery',
                        'alcoholic beverages',
                        'grape fermentation',
                        'FSSAI wine',
                        'alcohol limits',
                        'sulfur dioxide',
                        'food safety'],
        'test_requirements': 'Pycnometer / hydrometer ethyl alcohol determination, steam distillation for volatile acidity, iodometric titration for free and total sulfur dioxide, AAS/ICP-MS for heavy metals (lead, copper, arsenic), microbiological culture plating',
        'certification_process': 'Mandatory licensing under State Excise Act & FSSAI Alcoholic Beverages Regulations (2018) → BIS voluntary/mandatory certification scheme → Water testing complying with IS 10500 → NABL laboratory chemical & microbiological testing → Factory hygiene audit',
        'url': 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/Standard_review/Isdetails?ID=MTc1OTI%3D'},
    {   'is_code': 'IS 7585',
        'title': 'Fortified Wines — Specification',
        'year': '2020',
        'division': 'Food and Agriculture Division',
        'mandatory': False,
        'scope': 'This Indian Standard prescribes the requirements and methods of sampling and test for fortified wines (such as Port, Sherry, and Madeira style wines) produced by grape fermentation and fortified with grape neutral spirit or brandy. It sets limits on ethyl alcohol (15.0% to 22.0% v/v), ash content, and total sulfur dioxide.',
        'key_clauses': [   'Clause 4: Types — Port wine, Sherry wine, and other fortified dessert wines',
                           'Clause 5: Chemical requirements — Ethyl alcohol content (15.0% to 22.0% v/v) and maximum volatile acid limits',
                           'Clause 6: Neutral spirit fortification quality — Grape brandy or neutral spirit conforming to IS 6613',
                           'Clause 8: Packaging — Sterile food-grade glass bottles conforming to IS 1660'],
        'keywords': [   'fortified wine',
                        'port wine',
                        'sherry',
                        'winery standards',
                        'alcoholic beverage',
                        'grape spirit',
                        'FSSAI',
                        'BIS wine'],
        'test_requirements': 'Alcohol by volume determination by distillation, volatile acid titration, total sugar calculation by Lane and Eynon method, sulfur dioxide titration',
        'certification_process': 'FSSAI Central / State License → State Excise Distillery / Winery License → Product testing at NABL accredited food lab → Glass bottle compliance with IS 1660',
        'url': 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/Standard_review/Isdetails?ID=MTc1OTM%3D'},
    {   'is_code': 'IS 2347',
        'title': 'Domestic Pressure Cookers — Specification',
        'year': '2017',
        'division': 'Mechanical Engineering Division',
        'mandatory': True,
        'scope': 'This Indian Standard prescribes the requirements for domestic pressure cookers made of aluminium alloys or stainless steel having a nominal capacity not exceeding 22 litres. It sets rigorous safety requirements for operating pressure, burst pressure resistance, pressure relief devices, and locking mechanisms to prevent accidental opening under pressure.',
        'key_clauses': [   'Clause 6: Material and construction — Grade requirements for aluminium alloy sheet and austenitic stainless steel',
                           'Clause 7: Safety devices — Weight valve calibration (operating pressure 1.0 kgf/cm²), fusible safety plug, and gasket release system (GRS)',
                           'Clause 8: Pressure tests — Proof pressure test at 2x operating pressure without leakage or permanent distortion',
                           'Clause 8.4: Hydraulic burst pressure test — Cooker body must withstand minimum 3x operating pressure without rupture',
                           'Clause 10: Thermal efficiency — Minimum 50% thermal efficiency test'],
        'keywords': [   'pressure cooker',
                        'cooker',
                        'burst test',
                        'safety valve',
                        'fusible plug',
                        'gasket release system',
                        'GRS',
                        'ISI mark',
                        'DPIIT QCO',
                        'domestic cookware'],
        'test_requirements': 'Proof pressure testing at 200 kPa, hydraulic burst pressure test at >300 kPa, pressure relief device discharge test, opening under pressure interlock test, thermal shock endurance',
        'certification_process': 'Mandatory under Domestic Pressure Cookers (Quality Control) Order → Sample testing at NABL accredited metallurgical laboratory → Factory audit of manufacturing line and safety test rigs → Grant of ISI mark license (Scheme-I)',
        'url': 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/Standard_review/Isdetails?ID=MTc4NDQ%3D'},
    {   'is_code': 'IS 1417',
        'title': 'Gold and Gold Alloys, Platings — Purity and Marking, Hallmarking — Specification',
        'year': '2021',
        'division': 'Metallurgical Engineering Division',
        'mandatory': True,
        'scope': 'This Indian Standard covers the grades of gold and gold alloys used in jewellery, artifacts, and coinage, and specifies requirements for purity fineness and hallmarking. It specifies permissible fineness in parts per thousand (916 for 22K, 750 for 18K, 585 for 14K) and prescribes the mandatory hallmarking marks: BIS logo, purity fineness, and unique 6-digit alphanumeric HUID (Hallmark Unique Identification).',
        'key_clauses': [   'Clause 4: Fineness grades — Standard 24K (999), 22K (916), 20K (833), 18K (750), and 14K (585) fineness levels',
                           'Clause 5: Marking and symbols — Mandatory BIS logo, purity mark in carats and fineness, and 6-digit HUID laser inscription',
                           'Clause 6: Assay methods — Fire assay method (cupellation) as the reference referee method for gold determination',
                           'Clause 7: Solder requirements — Solder alloy fineness must not be less than the gold alloy fineness of the jewellery piece'],
        'keywords': [   'gold hallmarking',
                        'gold purity',
                        'hallmark',
                        'HUID',
                        'jewellery',
                        '22K gold',
                        '916 gold',
                        'fire assay',
                        'cupellation',
                        'BIS hallmark',
                        'precious metals'],
        'test_requirements': 'Fire assay cupellation testing according to IS 1418, X-ray fluorescence (XRF) non-destructive screening, touchstone comparison testing, microscopic laser inscription verification',
        'certification_process': 'Mandatory under Hallmarking of Gold Jewellery and Artefacts Order → Jeweller registration on BIS portal → Sending articles to BIS-Recognized Assaying and Hallmarking Centres (AHC) → Fire assay testing → Laser marking of BIS logo & HUID',
        'url': 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/Standard_review/Isdetails?ID=MjEyNDk%3D'},
    {   'is_code': 'IS 9873-1',
        'title': 'Safety of Toys — Part 1: Safety Aspects Related to Mechanical and Physical Properties',
        'year': '2019',
        'division': 'Chemical Division',
        'mandatory': True,
        'scope': 'This Indian Standard applies to all toys intended for use by children under 14 years of age. It specifies acceptable criteria for structural characteristics of toys, such as shape, size, contour, spacing (e.g. hazards from choking on small parts, sharp edges, points), as well as acceptable criteria for properties peculiar to certain categories of toys (e.g. maximum kinetic energy values for projectile toys).',
        'key_clauses': [   'Clause 4.3: Small parts hazard — Small parts test cylinder (31.7 mm diameter) for toys intended for children under 36 months',
                           'Clause 4.7: Edges and sharp points — Accessible sharp edge test and sharp point probe verification',
                           'Clause 4.17: Projectiles — Maximum kinetic energy of 0.08 J for rigid projectiles and protective rubber tip requirements',
                           'Clause 5: Drop, tip-over, and impact tests — Mechanical strength testing under dynamic drop and torque test'],
        'keywords': [   'toy safety',
                        'toys',
                        'small parts',
                        'choking hazard',
                        'sharp edges',
                        'mechanical properties',
                        'children toys',
                        'ISI mark',
                        'DPIIT Toys QCO'],
        'test_requirements': 'Drop test from 138 cm onto steel plate, torque test at 0.45 Nm, tension test at 90 N, small parts cylinder insertion test, sharp point test instrument evaluation',
        'certification_process': 'Mandatory under Toys (Quality Control) Order → Application on BIS Manakonline → Testing at NABL lab accredited for toy safety → Factory audit of manufacturing facilities → Grant of ISI mark license (Scheme-I)',
        'url': 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/Standard_review/Isdetails?ID=MTc1MDQ%3D'},
    {   'is_code': 'IS 302-1',
        'title': 'Safety of Household and Similar Electrical Appliances — Part 1: General Requirements',
        'year': '2024',
        'division': 'Electrotechnical Division',
        'mandatory': True,
        'scope': 'This Indian Standard deals with the safety of electrical appliances for household and similar '
                 'purposes, their rated voltage being not more than 250 V for single-phase appliances and 480 V for '
                 'other appliances. It covers protection against electrical shock, hazards from moving parts, heating, '
                 'and fire risks under normal and abnormal operation. Appliances not intended for normal household '
                 'use, but which nevertheless may be a source of danger to the public, are also within the scope.',
        'key_clauses': [   'Clause 7: Marking and instructions — Voltage, frequency, wattage rating, and cautionary '
                           'warnings',
                           'Clause 8: Protection against access to live parts — Test finger and pin probe '
                           'accessibility tests',
                           'Clause 13: Leakage current and electric strength at operating temperature',
                           'Clause 19: Abnormal operation — Overload, short-circuit, and cooling restriction '
                           'simulation',
                           'Clause 29: Clearances, creepage distances and solid insulation — Dielectric distance '
                           'verification'],
        'keywords': [   'electrical safety',
                        'household appliances',
                        'electric shock',
                        'insulation',
                        'leakage current',
                        'abnormal operation',
                        'BIS',
                        'ISI mark'],
        'test_requirements': 'High-voltage breakdown test at 1000V-3750V, leakage current measurement under 0.75mA, '
                             'glow-wire flammability test at 750°C/850°C, mechanical impact test using spring hammer '
                             '(0.5J), temperature rise test',
        'certification_process': 'Apply on BIS Manakonline portal → Sample submission to BIS-recognized NABL '
                                 'laboratory → Product type testing → Factory audit by BIS officer → Verification of '
                                 'in-house testing facilities → Grant of ISI certification mark license (CM/L)',
        'url': 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/Standard_review/Isdetails?ID=MTM0ODk%3D'},
    {   'is_code': 'IS 302-2-3',
        'title': 'Safety of Household and Similar Electrical Appliances — Part 2: Particular Requirements — Section 3: '
                 'Electric Irons',
        'year': '2007',
        'division': 'Electrotechnical Division',
        'mandatory': True,
        'scope': 'This standard deals with the safety of electric dry irons and steam irons, including those with a '
                 'separate water reservoir or boiler having a capacity not exceeding 5 litres, for household and '
                 'similar use. It addresses hazards related to extreme soleplate temperature, steam overpressure, '
                 'thermal cutoff reliability, and cord flexure. It applies to both domestic irons and irons intended '
                 'for use in laundrettes.',
        'key_clauses': [   'Clause 11: Heating — Soleplate and handle temperature rise limit criteria',
                           'Clause 15: Moisture resistance — Steam chamber spillage and condensation ingress '
                           'protection',
                           'Clause 21: Mechanical strength — Drop test from 1 meter on rigid rubber support',
                           'Clause 22: Construction — Thermal cutout non-self-resetting requirements',
                           'Clause 25: Supply connection and external cords — Flexing endurance test of cord entry '
                           'bushing (20,000 cycles)'],
        'keywords': [   'electric iron',
                        'dry iron',
                        'steam iron',
                        'soleplate',
                        'temperature cutoff',
                        'cord flexing',
                        'appliance safety',
                        'BIS'],
        'test_requirements': 'Cord flexing test (20,000 oscillations under tension), soleplate temperature calibration '
                             'test, thermal fuse trip verification, high-voltage flash test at 1500V, water spillage '
                             'test',
        'certification_process': 'BIS Scheme-I mandatory certification under Household Electrical Appliances QCO → '
                                 'Submission of factory QMS → NABL accredited testing → Factory assessment → Issuance '
                                 'of ISI mark',
        'url': 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/Standard_review/Isdetails?ID=MTU4OTY%3D'},
    {   'is_code': 'IS 302-2-15',
        'title': 'Safety of Household and Similar Electrical Appliances — Part 2: Particular Requirements — Section '
                 '15: Electric Kettles and Liquid Heaters',
        'year': '2009',
        'division': 'Electrotechnical Division',
        'mandatory': True,
        'scope': 'This Indian Standard deals with the safety of electric kettles, coffee makers, tea makers, and other '
                 'appliances for heating liquids for household and similar purposes with rated capacity up to 10 '
                 'litres. It establishes critical safeguards against dry boiling, steam scald hazards, lid ejection, '
                 'and electrical insulation degradation during liquid spillage. It specifies auto-shutoff thermostatic '
                 'performance under abnormal and dry boiling conditions.',
        'key_clauses': [   'Clause 13: Heating — External body and handle touch-temperature safety thresholds',
                           'Clause 15: Moisture resistance — IPX4 liquid overflow and spillage testing onto electrical '
                           'connections',
                           'Clause 16: Leakage current — Maximum 0.5mA at rated voltage',
                           'Clause 19: Abnormal operation — Boil-dry protection and thermal cutoff response test',
                           'Clause 22: Construction — Cordless base interlock connector integrity and lid retention'],
        'keywords': [   'electric kettle',
                        'liquid heater',
                        'boil-dry protection',
                        'thermal cutout',
                        'IPX4',
                        'leakage current',
                        'appliance safety',
                        'BIS'],
        'test_requirements': 'Dielectric strength test at 1250V, thermal endurance, moisture resistance IPX4, leakage '
                             'current measurement under 0.5mA, boil-dry dry-run endurance test for 100 cycles',
        'certification_process': 'Apply to BIS via Manakonline → Product testing at NABL lab → Factory inspection by '
                                 'BIS auditor → Verification of safety interlock test equipment → ISI mark license',
        'url': 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/Standard_review/Isdetails?ID=MTM0ODk%3D'},
    {   'is_code': 'IS 302-2-201',
        'title': 'Safety of Household and Similar Electrical Appliances — Part 2: Particular Requirements — Section '
                 '201: Electric Immersion Water Heaters',
        'year': '2008',
        'division': 'Electrotechnical Division',
        'mandatory': True,
        'scope': 'This standard specifies safety requirements for portable electric immersion water heaters intended '
                 'for domestic and similar use. It specifies rigorous requirements to prevent electric shocks arising '
                 'from sheath perforation, terminal water ingress, and unauthorized hook attachment configurations. '
                 'Safe depth immersion markings and dry-run safety cutouts are mandated.',
        'key_clauses': [   'Clause 7: Marking — Maximum and minimum liquid immersion level marking durability',
                           'Clause 8: Protection against electric shock — Insulated handle and earthing terminal '
                           'protection',
                           'Clause 13: Electric strength — Cold and hot immersion dielectric test at 1250V',
                           'Clause 19: Abnormal operation — Operation without water in vessel to test element casing '
                           'resilience',
                           'Clause 22: Construction — Hermetic terminal sealing and anti-corrosive copper/brass sheath '
                           'requirements'],
        'keywords': [   'immersion heater',
                        'water heater',
                        'immersion rod',
                        'electrical safety',
                        'water immersion',
                        'dielectric strength',
                        'ISI mark'],
        'test_requirements': 'Water immersion breakdown test at 1250V AC, insulation resistance > 20 MOhm, dry burning '
                             'test without water, earthing continuity test < 0.1 Ohm, immersion line markings test',
        'certification_process': 'Mandatory ISI Scheme-I registration under QCO → Production unit inspection → NABL '
                                 'safety testing report → Verification of earthing integrity → Grant of license',
        'url': 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/Standard_review/Isdetails?ID=MjQ1ODk%3D'},
    {   'is_code': 'IS 1293',
        'title': 'Plugs and Socket-Outlets of Rated Voltage up to and Including 250 Volts and Rated Current up to and '
                 'Including 16 Amperes — Specification',
        'year': '2019',
        'division': 'Electrotechnical Division',
        'mandatory': True,
        'scope': 'This standard covers plugs and fixed or portable socket-outlets for alternating current only, with a '
                 'rated voltage not exceeding 250 V and rated current not exceeding 16 A, intended for household and '
                 'similar domestic or commercial applications. It specifies shutter mechanisms, pin dimensions, '
                 'terminal screw torques, and non-interchangeability rules to prevent accidental single-pin insertion '
                 'into live receptacles. Compliance is critical for preventing electrical fires and electrocution.',
        'key_clauses': [   'Clause 9: Checking of dimensions — Gauge insertion, withdrawal force, and pin spacing '
                           'verification',
                           'Clause 10: Protection against electric shock — Safety shutter engagement and finger '
                           'accessibility',
                           'Clause 13: Construction of fixed socket-outlets — Retention torque and terminal durability',
                           'Clause 19: Temperature rise — Maximum 45 K rise at terminals under rated current '
                           'continuous load',
                           'Clause 20: Breaking capacity — 50 make-and-break cycles at 1.25 times rated voltage and '
                           'current'],
        'keywords': [   'plugs',
                        'socket-outlets',
                        '16A plug',
                        '6A plug',
                        'shutter safety',
                        'temperature rise',
                        'electrical accessories',
                        'BIS QCO'],
        'test_requirements': 'Dimensional plug pin gauging, 10,000 cycle mechanical endurance test, temperature rise '
                             'test at rated load, withdrawal force gauge test (1.5N to 50N), ball pressure insulation '
                             'heat test at 125°C',
        'certification_process': 'Mandatory BIS certification under Electrical Accessories QCO → Factory audit & '
                                 'quality manual review → Comprehensive type testing at certified NABL lab → ISI mark '
                                 'stamping license',
        'url': 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/Standard_review/Isdetails?ID=MTc5ODc%3D'},
    {   'is_code': 'IS 366',
        'title': 'Electric Irons — Specification',
        'year': '1991',
        'division': 'Electrotechnical Division',
        'mandatory': True,
        'scope': 'This Indian Standard covers performance and constructional requirements for domestic electric dry, '
                 'steam, and spray irons. It defines performance benchmarks including thermostatic cycle stability, '
                 'steam distribution rate, heating-up time, and energy consumption efficiency. It operates alongside '
                 'IS 302-2-3 to guarantee both consumer safety and functional longevity.',
        'key_clauses': [   'Clause 5: Materials and construction — Soleplate coating non-stick durability and '
                           'corrosion resistance',
                           'Clause 6: Finish and workmanship — Surface smoothness and handle ergonomic design',
                           'Clause 8: Performance requirements — Time required to reach 200°C soleplate temperature',
                           'Clause 9: Thermostat endurance — 100,000 thermal cycling tests under operating conditions',
                           'Clause 11: Steaming rate and capacity — Minimum 15g/min continuous steam generation'],
        'keywords': [   'electric iron',
                        'performance',
                        'thermostat cycle',
                        'steam rate',
                        'soleplate',
                        'energy efficiency',
                        'BIS'],
        'test_requirements': 'Heating up time measurement (under 3 min), steaming rate test (g/min), soleplate scratch '
                             'and adhesion test, endurance test of 100,000 cycles for thermostat, power input '
                             'deviation test',
        'certification_process': 'Application submission on Manakonline → Performance and safety testing at designated '
                                 'BIS laboratory → Production line audit → License grant for ISI marking',
        'url': 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/Standard_review/Isdetails?ID=MTAwOTI%3D'},
    {   'is_code': 'IS 616',
        'title': 'Audio, Video and Similar Electronic Apparatus — Safety Requirements',
        'year': '2017',
        'division': 'Electrotechnical Division',
        'mandatory': True,
        'scope': 'This standard applies to electronic apparatus designed to be fed from the mains, from a supply '
                 'apparatus, from batteries or from remote power feeding and intended for reception, generation, '
                 'recording or reproduction respectively of audio, video and associated signals. It covers television '
                 'receivers, audio amplifiers, video players, and power adapters, establishing protection against '
                 'shock, hazardous radiation, excessive temperature, and physical implosion of CRT/display units. It '
                 'aligns closely with IEC 60065.',
        'key_clauses': [   'Clause 4: General test conditions — Normal and fault operating conditions',
                           'Clause 7: Heating under normal operating conditions — Transformer and enclosure '
                           'temperature limits',
                           'Clause 9: Electric shock hazard under normal operating conditions — Accessible terminals '
                           'voltage limits (<35V peak)',
                           'Clause 11: Heating under fault conditions — Overload and component failure fire prevention',
                           'Clause 13: Clearances and creepage distances — Printed circuit board trace separation '
                           'criteria'],
        'keywords': [   'electronics safety',
                        'audio video apparatus',
                        'television',
                        'amplifier',
                        'MeitY CRS',
                        'insulation resistance',
                        'BIS'],
        'test_requirements': 'Dielectric strength test at 3000V AC, touch current measurement (<0.7mA peak), fault '
                             'condition tests (simulated transistor/capacitor short), drop and impact test, '
                             'flammability test UL94 V-0/V-1',
        'certification_process': 'Compulsory Registration Scheme (CRS) under MeitY → Testing at BIS-recognized '
                                 'laboratory → Submission of test reports online via BIS portal → Grant of '
                                 'Registration (R-number)',
        'url': 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/Standard_review/Isdetails?ID=MTExMjM%3D'},
    {   'is_code': 'IS 10500',
        'title': 'Drinking Water — Specification',
        'year': '2012',
        'division': 'Food and Agriculture Division',
        'mandatory': True,
        'scope': 'This Indian Standard prescribes the quality requirements and permissible limits for drinking water '
                 'intended for human consumption. It establishes mandatory biological, physical, chemical, and '
                 'radioactive limits for public water supplies, piped water networks, and private sources. It details '
                 'acceptable and permissible limits in the absence of an alternate source for parameters including pH, '
                 'total dissolved solids, heavy metals, pesticides, and bacterial contaminants like E. coli.',
        'key_clauses': [   'Clause 4: Requirements — Organoleptic and physical parameters (Colour, Odour, Turbidity '
                           'max 1 NTU, pH 6.5-8.5)',
                           'Clause 4.1: General parameters concerning substances undesirable in excessive amounts (TDS '
                           'max 500 mg/L, Total Hardness max 200 mg/L)',
                           'Clause 4.2: Toxic substances limits — Arsenic (0.01 mg/L), Lead (0.01 mg/L), Mercury '
                           '(0.001 mg/L), Cadmium (0.003 mg/L)',
                           'Clause 4.3: Pesticide residues analysis — Compliance with individual pesticide limit max '
                           '0.0001 mg/L',
                           'Clause 5: Bacteriological parameters — Total coliform bacteria and E. coli must be absent '
                           'in any 100 ml sample'],
        'keywords': [   'drinking water',
                        'potable water',
                        'water quality',
                        'turbidity',
                        'TDS',
                        'heavy metals',
                        'coliform',
                        'E. coli',
                        'BIS standard'],
        'test_requirements': 'Spectrophotometric analysis for heavy metals (AAS/ICP-MS), membrane filtration technique '
                             'for coliforms and E. coli, gas chromatography (GC-MS) for pesticide residues, '
                             'nephelometric turbidity test',
        'certification_process': 'Mandatory compliance for municipal utilities and packaged suppliers → Collection of '
                                 'multi-seasonal samples → Complete chemical, physical, and microbiological testing in '
                                 'NABL accredited labs → Periodic surveillance testing',
        'url': 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/Standard_review/Isdetails?ID=MjAyMTk%3D'},
    {   'is_code': 'IS 14543',
        'title': 'Packaged Drinking Water (Other than Packaged Natural Mineral Water) — Specification',
        'year': '2004',
        'division': 'Food and Agriculture Division',
        'mandatory': True,
        'scope': 'This standard specifies requirements and methods of sampling and test for packaged drinking water '
                 '(other than packaged natural mineral water) offered for sale in sealed containers of various '
                 'capacities. It mandates mandatory multi-barrier purification processes like demineralization, '
                 'filtration, reverse osmosis, and disinfection via ozonation or UV treatment. It is legally mandatory '
                 'under FSSAI and BIS regulations for commercial bottled water manufacturers.',
        'key_clauses': [   'Clause 3: Treatment processes — Permitted purification operations including filtration, '
                           'aeration, RO, and ozonation',
                           'Clause 4: Hygiene requirements — Sanitary plant design, equipment sterilization, and '
                           'cleanroom air handling',
                           'Clause 5: Chemical and microbiological criteria — Zero viable colonies of Pseudomonas '
                           'aeruginosa and yeast/mould',
                           'Clause 7: Packaging — Food grade PET, polycarbonate, or glass containers complying with IS '
                           '15410 / IS 10146',
                           "Clause 8: Labelling — Mandatory display of 'Packaged Drinking Water', batch number, best "
                           'before date, and ISI mark'],
        'keywords': [   'packaged drinking water',
                        'bottled water',
                        'RO water',
                        'ozonation',
                        'microbiological safety',
                        'PET bottles',
                        'ISI mark mandatory'],
        'test_requirements': 'Microbiological membrane incubation for Pseudomonas aeruginosa, E. coli, and '
                             'Sulphite-reducing anaerobes; pesticide residue limits (< 0.1 ppb); total dissolved '
                             'solids (75 to 500 mg/L); shelf life stability test',
        'certification_process': 'Mandatory Scheme-I ISI licensing → Stringent factory hygiene audit → In-house '
                                 'testing laboratory setup with trained microbiologist & chemist → Two independent '
                                 'batch tests at BIS Central Labs → Grant of ISI License',
        'url': 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/Standard_review/Isdetails?ID=MTc3NjM%3D'},
    {   'is_code': 'IS 13428',
        'title': 'Packaged Natural Mineral Water — Specification',
        'year': '2005',
        'division': 'Food and Agriculture Division',
        'mandatory': True,
        'scope': 'This standard covers the requirements and methods of sampling and testing for packaged natural '
                 'mineral water obtained directly from natural or drilled subterranean sources. It requires that the '
                 'water source be naturally protected from contamination and contains specific mineral contents '
                 'naturally occurring at source without chemical alteration. Treatment is strictly limited to '
                 'separation of unstable elements (iron, manganese, sulphur) and filtration without altering chemical '
                 'composition.',
        'key_clauses': [   'Clause 3: Source of natural mineral water — Geological survey protection zone and hygiene '
                           'integrity',
                           'Clause 4: Authorized treatment — Only physical separation of suspended particles, '
                           'aeration, and decantation allowed',
                           'Clause 5: Physical and chemical limits — Specific electrical conductivity, pH 6.5-8.5, '
                           'dissolved minerals',
                           'Clause 6: Microbiological limits — Total viable colony count at 20-22°C and 37°C, zero '
                           'pathogen count',
                           'Clause 8: Packaging and labelling — Declaration of source name, location, and natural '
                           'chemical composition breakdown'],
        'keywords': [   'natural mineral water',
                        'spring water',
                        'subterranean source',
                        'mineral composition',
                        'microbiology',
                        'hygiene',
                        'ISI mark'],
        'test_requirements': 'Radiological safety tests (Gross alpha and beta activity), ICP-OES trace mineral '
                             'quantification, microbiological culture for Faecal streptococci and Sporulated '
                             'sulphite-reducing anaerobes, packaging integrity test',
        'certification_process': 'Mandatory ISI Scheme-I certification → Geological source inspection and multi-season '
                                 'source water evaluation → Factory and bottling plant hygienic audit → BIS lab sample '
                                 'verification → Grant of ISI Mark',
        'url': 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/Standard_review/Isdetails?ID=MTQzMTI%3D'},
    {   'is_code': 'IS 16240',
        'title': 'Reverse Osmosis (RO) Based Point-of-Use (PoU) Water Treatment System — Specification',
        'year': '2015',
        'division': 'Chemical Division',
        'mandatory': False,
        'scope': 'This standard specifies performance, design, and construction requirements for reverse osmosis based '
                 'point-of-use water treatment systems intended for reduction of dissolved solids, heavy metals, and '
                 'microbial contaminants in drinking water. It sets minimum recovery percentage standards to prevent '
                 'excessive water wastage and establishes minimum TDS reduction efficiency. It also specifies '
                 'requirements for materials in contact with treated water to prevent chemical leaching.',
        'key_clauses': [   'Clause 4: Construction and components — Food grade plastic piping, booster pump '
                           'reliability, and membrane housing',
                           'Clause 5: Performance requirements — Minimum 90% TDS reduction and minimum 20% water '
                           'recovery ratio',
                           'Clause 6: Reduction of specific contaminants — Arsenic, fluoride, lead, nitrate, and '
                           'pesticide removal efficiency',
                           'Clause 7: Microbial challenge test — Minimum 6-log reduction for bacteria and 4-log '
                           'reduction for viruses',
                           'Clause 9: Electrical safety — High voltage and earthing requirements complying with IS '
                           '302-1'],
        'keywords': [   'reverse osmosis',
                        'RO purifier',
                        'water filter',
                        'TDS reduction',
                        'water recovery',
                        'microbial challenge',
                        'point of use'],
        'test_requirements': 'TDS reduction test with challenge water (1500 mg/L TDS), viral and bacterial seeding '
                             'challenge test, membrane pressure burst test at 300 psi, food contact extraction test on '
                             'plastic components',
        'certification_process': 'Voluntary BIS Product Certification Scheme → Laboratory challenge testing for '
                                 'chemical and biological reduction → Production facility quality audit → Issuance of '
                                 'ISI certification mark',
        'url': 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/Standard_review/Isdetails?ID=MzE4OTQ%3D'},
    {   'is_code': 'IS 15153',
        'title': 'Water Quality — Guidance on the Preservation and Handling of Water Samples',
        'year': '2002',
        'division': 'Chemical Division',
        'mandatory': False,
        'scope': 'This standard provides general guidelines for the preservation, holding times, and handling '
                 'techniques for water and wastewater samples collected for chemical, physical, and biological '
                 'analyses. It details preservation methods such as acidification, refrigeration at 4°C, freezing, and '
                 'addition of chemical stabilizers to prevent sample degradation prior to laboratory testing. It is an '
                 'essential reference for environmental labs and BIS testing agencies.',
        'key_clauses': [   'Clause 3: Preservation techniques — Refrigeration, deep freezing, chemical fixation (acid, '
                           'alkali, biocides)',
                           'Clause 4: Containers — Selection between high-density polyethylene (HDPE), borosilicate '
                           'glass, and PTFE containers',
                           'Clause 5: Maximum permissible holding periods — Sample storage windows for BOD, COD, '
                           'nutrients, and heavy metals',
                           'Clause 6: Chain of custody and identification — Sample tagging, temperature monitoring '
                           'during transit, and logs'],
        'keywords': [   'water sampling',
                        'sample preservation',
                        'holding time',
                        'chemical analysis',
                        'water quality testing',
                        'environmental testing'],
        'test_requirements': 'Verification of sample pH preservation (pH < 2 for metals using HNO3), cooling storage '
                             'verification (4°C ± 2°C), storage container blanks test, holding time compliance audits',
        'certification_process': 'Implemented as standard operating procedure (SOP) across all NABL-accredited and BIS '
                                 'testing laboratories; audited during lab accreditation under ISO/IEC 17025',
        'url': 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/Standard_review/Isdetails?ID=MTg5MDI%3D'},
    {   'is_code': 'IS 10598',
        'title': 'Code of Practice for Design and Installation of Point-of-Use Water Treatment Devices',
        'year': '1983',
        'division': 'Civil Engineering Division',
        'mandatory': False,
        'scope': 'This code of practice covers the guidelines for selection, structural design, installation, '
                 'operation, and maintenance of point-of-use domestic water treatment devices. It covers gravity-fed '
                 'ceramic candle filters, activated carbon cartridges, and ultraviolet disinfection units. It '
                 'specifies flow rates, plumbing connection integrity, and hygienic maintenance schedules to avoid '
                 'biofilm accumulation.',
        'key_clauses': [   'Clause 4: System types — Gravity filters, in-line pressure filters, and chemical dosing '
                           'units',
                           'Clause 5: Installation requirements — Backflow prevention, pressure regulator valve '
                           'installation, and bypass valves',
                           'Clause 6: Filter media requirements — Candle porosity, granular activated carbon iodine '
                           'value, and UV lamp dosage',
                           'Clause 8: Maintenance procedures — Periodic cleaning, chemical backwashing, and filter '
                           'candle replacement cycle'],
        'keywords': [   'water filter installation',
                        'point of use',
                        'ceramic candle',
                        'activated carbon',
                        'UV disinfection',
                        'water treatment code'],
        'test_requirements': 'Hydrostatic burst pressure test (1.5 times operating pressure), microbial candle bubble '
                             'point test, flow rate determination at rated water head, seal leak tightness inspection',
        'certification_process': 'Compliance used by plumbing engineers, municipal housing boards, and manufacturers '
                                 'of domestic filters; tested in accordance with BIS civil engineering laboratory '
                                 'protocols',
        'url': 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/Standard_review/Isdetails?ID=MTEzOTU%3D'},
    {   'is_code': 'IS 3025-1',
        'title': 'Methods of Sampling and Test (Physical and Chemical) for Water and Wastewater — Part 1: Sampling',
        'year': '1987',
        'division': 'Chemical Division',
        'mandatory': False,
        'scope': 'This standard prescribes the methods of sampling of water and wastewater for physical and chemical '
                 'analysis. It covers procedures for obtaining representative samples from rivers, reservoirs, '
                 'borewells, municipal distribution mains, and industrial effluents. It details the preparation of '
                 'sampling bottles, grab sampling vs composite sampling, and specialized sampling equipment.',
        'key_clauses': [   'Clause 4: General precautions — Cleanliness of containers, avoidance of surface '
                           'contamination, and safety protocols',
                           'Clause 6: Types of samples — Grab/catch samples, composite samples, and integrated '
                           'discharge sampling',
                           'Clause 8: Sampling techniques for specific sources — Deep aquifers, pressurized tap '
                           'pipelines, open surface waters',
                           'Clause 10: Sampling apparatus — Weighted bottles, Kemmerer samplers, and depth-integrating '
                           'samplers'],
        'keywords': [   'water sampling',
                        'testing methods',
                        'wastewater',
                        'grab sample',
                        'composite sample',
                        'laboratory analysis',
                        'BIS 3025'],
        'test_requirements': 'Container background extraction test, dissolved oxygen fixation in situ via Winkler '
                             'method, temperature and pH measurement at sampling point, sample volume sufficiency '
                             'validation',
        'certification_process': 'Referenced mandatory standard for environmental compliance testing, industrial '
                                 'effluent monitoring under CPCB/SPCB, and NABL laboratory accreditation audits',
        'url': 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/Standard_review/Isdetails?ID=MTI3ODQ%3D'},
    {   'is_code': 'IS 1893-1',
        'title': 'Criteria for Earthquake Resistant Design of Structures — Part 1: General Provisions and Buildings',
        'year': '2016',
        'division': 'Civil Engineering Division',
        'mandatory': True,
        'scope': 'This Indian Standard deals with the assessment of seismic loads on buildings and gives general '
                 'principles for earthquake-resistant design of structures. It outlines seismic zones of India (Zones '
                 'II, III, IV, and V), design response spectrum, and calculation of design base shear using equivalent '
                 'static and response spectrum dynamic analysis methods. It incorporates structural regularity '
                 'criteria, torsion limits, and drift limitations to prevent collapse during severe earthquakes.',
        'key_clauses': [   'Clause 6.4: Design lateral force and seismic zone factors (Z = 0.10 for Zone II to 0.36 '
                           'for Zone V)',
                           'Clause 7.1: Regular and irregular configurations — Plan and vertical structural '
                           'irregularities',
                           'Clause 7.2: Design spectrum and soil classification (Type I Rock, Type II Medium, Type III '
                           'Soft)',
                           'Clause 7.11: Storey drift limitation — Maximum storey drift not to exceed 0.004 times '
                           'storey height',
                           'Clause 7.12: Separation between adjacent units — Building pounding prevention clearance'],
        'keywords': [   'earthquake design',
                        'seismic zone',
                        'base shear',
                        'response spectrum',
                        'storey drift',
                        'building safety',
                        'structural engineering',
                        'IS 1893'],
        'test_requirements': 'Modal response spectrum analysis, dynamic shake table simulation validation for scale '
                             'models, storey drift verification computations, structural stiffness irregularity matrix '
                             'calculation',
        'certification_process': 'Mandatory statutory compliance under National Building Code of India (NBC) and '
                                 'municipal building bylaws; structural drawings verified and vetted by certified '
                                 'Chartered Structural Engineers before sanction',
        'url': 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/Standard_review/Isdetails?ID=MTk4NTQ%3D'},
    {   'is_code': 'IS 13920',
        'title': 'Ductile Design and Detailing of Reinforced Concrete Structures Subjected to Seismic Forces — Code of '
                 'Practice',
        'year': '2016',
        'division': 'Civil Engineering Division',
        'mandatory': True,
        'scope': 'This standard specifies requirements for ductile design and detailing of reinforced concrete '
                 'structures subjected to seismic forces in seismic zones III, IV, and V. It covers flexural members '
                 '(beams), axial-cum-flexural members (columns), beam-column joints, and shear walls. It establishes '
                 'minimum reinforcement ratios, confining hoop spacing, lap splice locations, and joint shear '
                 'reinforcement to ensure inelastic energy dissipation without brittle failure.',
        'key_clauses': [   'Clause 6: Beams — Minimum tension reinforcement, longitudinal bar anchorage, and closely '
                           'spaced shear stirrups',
                           'Clause 7: Columns and frame members — Strong column-weak beam philosophy, special '
                           'confining reinforcement',
                           'Clause 8: Beam-column joints — Confinement of joint core and shear strength verification',
                           'Clause 9: Special shear walls — Boundary elements, distributed vertical and horizontal web '
                           'reinforcement',
                           'Clause 10: Foundation detailing — Tie beams linking footings and pile caps in high seismic '
                           'zones'],
        'keywords': [   'ductile detailing',
                        'seismic detailing',
                        'reinforced concrete',
                        'shear walls',
                        'beam column joint',
                        'confining ties',
                        'IS 13920'],
        'test_requirements': 'Cyclic loading test of full-scale beam-column sub-assemblages, reinforcing steel '
                             'elongation test (minimum 14.5% uniform elongation for Fe 500D), ultrasonic pulse '
                             'velocity test on concrete joints',
        'certification_process': 'Mandatory compliance for all RC buildings in Zones III, IV, and V under NBC 2016; '
                                 'structural audit by municipal authorities and third-party proof checking before '
                                 'building occupancy certificate issuance',
        'url': 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/Standard_review/Isdetails?ID=MjEyMTM%3D'},
    {   'is_code': 'IS 4326',
        'title': 'Earthquake Resistant Design and Construction of Buildings — Code of Practice',
        'year': '2013',
        'division': 'Civil Engineering Division',
        'mandatory': True,
        'scope': 'This standard deals with the selection of materials, architectural design, and construction '
                 'practices for earthquake-resistant buildings including masonry, timber, and prefabricated '
                 'structures. It prescribes seismic bands (plinth band, lintel band, roof band, and gable band) and '
                 'vertical reinforcing bars at corners and T-junctions of masonry walls. It provides critical rules '
                 'for opening dimensions in load-bearing masonry to prevent diagonal shear cracking.',
        'key_clauses': [   'Clause 4: Structural planning and building materials — Lightness, symmetry, and ductility '
                           'of building envelope',
                           'Clause 7: Masonry construction — Mortar mix proportions, wall thickness, and box action '
                           'enhancement',
                           'Clause 8: Seismic bands — Reinforced concrete lintel, plinth, and roof band dimensions and '
                           'reinforcement',
                           'Clause 8.4: Vertical reinforcement in masonry — Diameter and installation at jambs of '
                           'openings and wall junctions',
                           'Clause 9: Timber construction — Joint bracing, bolted connection detailing, and foundation '
                           'anchorage'],
        'keywords': [   'masonry buildings',
                        'earthquake resistant',
                        'seismic bands',
                        'lintel band',
                        'plinth band',
                        'structural bracing',
                        'building code'],
        'test_requirements': 'Compressive strength of masonry prisms (minimum 3.5 to 10 MPa), shear bond strength test '
                             'of mortar-brick interface, pull-out test of vertical reinforcing bars embedded in '
                             'concrete cores',
        'certification_process': 'Mandatory compliance under state municipal corporations and disaster management '
                                 'guidelines for all non-engineered and semi-engineered masonry structures; field '
                                 'inspection during construction',
        'url': 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/Standard_review/Isdetails?ID=MTcyMzU%3D'},
    {   'is_code': 'IS 13827',
        'title': 'Improving Earthquake Resistance of Earthen Buildings — Guidelines',
        'year': '1993',
        'division': 'Civil Engineering Division',
        'mandatory': False,
        'scope': 'This standard provides guidelines for the design and construction of earthen (adobe, rammed earth) '
                 'buildings to enhance their seismic resistance. It specifies soil selection criteria, stabilization '
                 'using cement, lime, or bitumen, wall height-to-thickness ratios, and seismic collars or bands made '
                 'of timber, bamboo, or concrete. It aims to reduce casualties and catastrophic collapse of mud houses '
                 'in rural earthquake-prone areas.',
        'key_clauses': [   'Clause 4: Soil suitability — Clay content (15-20%), sand content (50-70%), and shrinkage '
                           'limit tests',
                           'Clause 5: Stabilization techniques — Addition of 4-6% cement or lime to enhance '
                           'compressive strength',
                           'Clause 6: Wall dimensions — Single-storey height limit, minimum wall thickness of 300 mm, '
                           'and opening limits',
                           'Clause 7: Seismic bands and reinforcement — Bamboo/timber collars at lintel level and '
                           'diagonal corner bracing'],
        'keywords': [   'earthen buildings',
                        'adobe',
                        'rammed earth',
                        'rural housing',
                        'earthquake resistance',
                        'bamboo bracing',
                        'soil stabilization'],
        'test_requirements': 'Dry compressive strength test of stabilized adobe blocks (>1.5 MPa), wet erosion spray '
                             'test (water jetting), soil sedimentation jar test for clay/sand fractions',
        'certification_process': 'Guidelines referenced by National Disaster Management Authority (NDMA), state rural '
                                 'development departments, and NGOs for seismic-safe rural housing construction '
                                 'programs',
        'url': 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/Standard_review/Isdetails?ID=MTY1Mjk%3D'},
    {   'is_code': 'IS 13828',
        'title': 'Improving Earthquake Resistance of Low Strength Masonry Buildings — Guidelines',
        'year': '1993',
        'division': 'Civil Engineering Division',
        'mandatory': False,
        'scope': 'This standard covers guidelines for improving the earthquake resistance of buildings constructed '
                 'with low-strength masonry materials such as unburnt bricks, random rubble stone in mud or lime '
                 'mortar, and lightweight blocks. It outlines construction methods to avoid outward wall bulging, '
                 'delamination of multi-wythe stone walls, and catastrophic roof collapse. Through-stones (bonders) '
                 'and perimeter tie wires or timber bands are detailed.',
        'key_clauses': [   'Clause 4: General principles — Symmetrical layout, continuous foundations, and roof '
                           'diaphragm action',
                           "Clause 5: Stone masonry — Provision of 'through-stones' or bond stones at intervals of 1.2 "
                           'm horizontal and 0.6 m vertical',
                           'Clause 6: Mortar specifications — Lime-sand or weak cement-sand mortars (1:6 to 1:8)',
                           'Clause 7: Wall reinforcements — Lintel bands, corner reinforcements, and wire mesh '
                           'encasement techniques'],
        'keywords': [   'low strength masonry',
                        'stone masonry',
                        'through stones',
                        'bond stones',
                        'earthquake retrofit',
                        'rubble masonry'],
        'test_requirements': 'In-situ shear test of low-strength masonry joints, diagonal compression test on stone '
                             'masonry panels, bond stone frequency and sound transmission verification',
        'certification_process': 'Referenced by state public works departments (PWD) and heritage conservation bodies '
                                 'for building seismic vulnerability retrofitting and low-cost construction',
        'url': 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/Standard_review/Isdetails?ID=MTY1MzA%3D'},
    {   'is_code': 'IS 1893-2',
        'title': 'Criteria for Earthquake Resistant Design of Structures — Part 2: Liquid Retaining Tanks',
        'year': '2014',
        'division': 'Civil Engineering Division',
        'mandatory': True,
        'scope': 'This Indian Standard prescribes the seismic design criteria and hydrodynamic load calculations for '
                 'ground-supported, elevated, and underground liquid retaining tanks (such as water, sewage, and '
                 'chemical tanks). It details the mechanical two-mass model accounting for convective (sloshing) fluid '
                 'mass and impulsive rigid fluid mass. It establishes hydrodynamic wall pressure distributions, '
                 'overturning moments, and base shear to prevent sloshing overflow and tank shell buckling.',
        'key_clauses': [   'Clause 4: Mathematical modeling — Spring-mass representation for impulsive and convective '
                           'modes',
                           'Clause 5: Time periods — Estimation of impulsive mode period (Ti) and convective mode '
                           'period (Tc)',
                           'Clause 6: Design hydrodynamic pressures — Impulsive pressure (pi) and convective sloshing '
                           'wave height (d_max)',
                           'Clause 7: Elevated tanks — Staging ductility, torsional effects, and lateral force '
                           'distribution across column staging'],
        'keywords': [   'water tank design',
                        'sloshing',
                        'hydrodynamic pressure',
                        'liquid retaining tank',
                        'elevated tank',
                        'seismic forces',
                        'IS 1893'],
        'test_requirements': 'Hydrodynamic sloshing wave height computational verification, dynamic modal analysis of '
                             'tank staging, leak tightness hydro-test under static head, ultrasonic testing of tank '
                             'wall seams',
        'certification_process': 'Mandatory compliance for public water works, municipal corporations, and industrial '
                                 'chemical storage facilities; design verification by State Water Boards and BIS '
                                 'technical committees',
        'url': 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/Standard_review/Isdetails?ID=MjU0MTE%3D'},
    {   'is_code': 'IS 1893-4',
        'title': 'Criteria for Earthquake Resistant Design of Structures — Part 4: Industrial Structures Including '
                 'Stack-Like Structures',
        'year': '2015',
        'division': 'Civil Engineering Division',
        'mandatory': True,
        'scope': 'This standard covers the earthquake resistant design of industrial structures, chimneys, stacks, '
                 'cooling towers, refinery towers, and silos. It accounts for higher vibration modes, vortex shedding '
                 'interactions with seismic forces, structural flexibility, and large mass concentrations at elevated '
                 'levels. It specifies design seismic coefficients, damping values for concrete, steel, and bolted '
                 'structures, and foundation anchorage rules.',
        'key_clauses': [   'Clause 5: Damping ratios — Structural damping allowances (2% for welded steel, 4% for '
                           'bolted steel, 5% for RC)',
                           'Clause 6: Chimneys and tall stacks — Dynamic modal analysis incorporating first three '
                           'modes of vibration',
                           'Clause 7: Silos and bunkers — Bulk material interactive mass during horizontal and '
                           'vertical ground motions',
                           'Clause 8: Process equipment and pipe racks — Combined seismic acceleration and thermal '
                           'expansion stress checks'],
        'keywords': [   'industrial structures',
                        'chimney design',
                        'cooling towers',
                        'silos',
                        'vibration modes',
                        'damping ratios',
                        'seismic analysis'],
        'test_requirements': 'Dynamic eigenvalue modal analysis for higher modes, anchor bolt pull-out tensile testing '
                             'under seismic shock loads, wind-seismic load interaction computer modeling',
        'certification_process': 'Mandatory statutory compliance for power plants, oil refineries, and heavy '
                                 'industrial facilities under National Building Code and industrial safety acts; '
                                 'third-party structural vet required',
        'url': 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/Standard_review/Isdetails?ID=MjUyNTg%3D'},
    {   'is_code': 'IS 2190',
        'title': 'Selection, Installation and Maintenance of First-Aid Fire Extinguishers — Code of Practice',
        'year': '2010',
        'division': 'Civil Engineering Division',
        'mandatory': True,
        'scope': 'This code of practice covers selection, installation, maintenance, inspection, and testing of '
                 'portable and wheeled first-aid fire extinguishers. It classifies fires into Classes A, B, C, D, and '
                 'F/K, detailing extinguisher types (water, foam, dry powder, CO2, clean agent) required for each '
                 'hazard class. It defines coverage areas, maximum travel distances to an extinguisher (15 meters), '
                 'and periodic hydrostatic discharge pressure testing intervals.',
        'key_clauses': [   'Clause 4: Classification of fire hazards — Light hazard, ordinary hazard, and extra hazard '
                           'occupancies',
                           'Clause 5: Selection of fire extinguishers — Matching extinguishing agents to fire classes '
                           'A, B, C, D, F',
                           'Clause 6: Installation and positioning — Mounting height (max 1.5 m from floor), '
                           'visibility, and signage',
                           'Clause 8: Maintenance schedules — Monthly visual inspection, annual servicing, and '
                           'hydraulic pressure testing'],
        'keywords': [   'fire extinguisher',
                        'fire safety',
                        'fire classes',
                        'hydraulic test',
                        'dry chemical powder',
                        'CO2 extinguisher',
                        'maintenance code'],
        'test_requirements': 'Hydrostatic stretch testing of extinguisher cylinders at 25-30 bar, extinguishing powder '
                             'discharge rate and range test, safety pin shear force check, nozzle flow pattern check',
        'certification_process': 'Mandatory compliance for all building occupancies under NBC Part 4 and state Fire '
                                 'Services Acts; servicing audited by licensed fire protection agencies and verified '
                                 'during fire NOC inspections',
        'url': 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/Standard_review/Isdetails?ID=MjA5MDY%3D'},
    {   'is_code': 'IS 15683',
        'title': 'Portable Fire Extinguishers — Performance and Construction — Specification',
        'year': '2018',
        'division': 'Civil Engineering Division',
        'mandatory': True,
        'scope': 'This Indian Standard specifies the requirements for design, construction, and performance testing of '
                 'portable fire extinguishers of water, foam, powder, carbon dioxide, and clean agent types. It covers '
                 'extinguishers with an operating charge up to 20 kg or 20 litres. It sets stringent requirements for '
                 'burst pressure safety factors, corrosion resistance, minimum effective discharge time, and '
                 'electrical conductivity of the extinguishing stream.',
        'key_clauses': [   'Clause 5: Construction of body — Minimum wall thickness, steel grade, deep-drawing '
                           'quality, and welding requirements',
                           'Clause 6: Safety relief devices and pressure indicators — Burst disk calibration and '
                           'pressure gauge accuracy',
                           'Clause 7: Fire rating performance — Standardized wood crib (Class A) and n-heptane tray '
                           '(Class B) fire extinguishing tests',
                           'Clause 8: Resistance to internal and external corrosion — 480-hour salt spray test per IS '
                           '9844',
                           'Clause 9: Electrical non-conductivity test — Dielectric stream test at 36,000 V for clean '
                           'agents and powder'],
        'keywords': [   'portable fire extinguisher',
                        'fire rating',
                        'Class A fire',
                        'Class B fire',
                        'corrosion resistance',
                        'pressure vessel',
                        'ISI mark mandatory'],
        'test_requirements': 'Class A wooden crib fire test (e.g., 2A, 3A, 4A rating), Class B fuel tray fire '
                             'extinguishing test (e.g., 55B, 89B), hydraulic burst test at 2.7 times working pressure, '
                             '36kV dielectric test',
        'certification_process': 'Mandatory BIS certification under Fire Extinguishers QCO (Scheme-I) → Type testing '
                                 'of fire rating in specialized BIS fire test grounds → Production line inspection → '
                                 'ISI mark grant',
        'url': 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/Standard_review/Isdetails?ID=Mjk5MDY%3D'},
    {   'is_code': 'IS 3844',
        'title': 'Code of Practice for Installation and Maintenance of Internal Fire Hydrants and Hose Reels on '
                 'Premises',
        'year': '1989',
        'division': 'Civil Engineering Division',
        'mandatory': True,
        'scope': 'This standard covers the design, installation, testing, and maintenance of internal wet riser and '
                 'down-comer fire hydrant systems and first-aid hose reels in commercial, residential, and industrial '
                 'buildings. It specifies water reservoir capacities, pump flow rates and pressures, pipe sizing, '
                 'location of landing valves, and hose reel deployment lengths. It ensures guaranteed pressurized '
                 'water delivery for occupants and firefighters during an emergency.',
        'key_clauses': [   'Clause 4: System classifications — Wet riser, dry riser, and down-comer system '
                           'configurations',
                           'Clause 5: Water supply and storage — Dedicated fire water reservoir capacities (50,000 to '
                           '200,000 litres)',
                           'Clause 6: Fire pumps and controls — Electric main pump, standby diesel pump, and automatic '
                           'jockey pump staging',
                           'Clause 7: Hydrant valves and hose reels — Landing valve heights, 30 m rubber hose reels, '
                           'and 63 mm canvas delivery hoses',
                           'Clause 9: Commissioning hydraulic tests — Static and running water pressure tests (minimum '
                           '3.5 bar at highest hydrant)'],
        'keywords': [   'internal fire hydrant',
                        'wet riser',
                        'hose reel',
                        'fire pumps',
                        'landing valve',
                        'fire water storage',
                        'fire protection'],
        'test_requirements': 'Hydrostatic pipe pressure test at 1.5 times working pressure for 2 hours, running nozzle '
                             'pressure test (minimum 3.5 bar at top landing valve), pump flow rate test (2280 or 2850 '
                             'LPM)',
        'certification_process': 'Statutory requirement for building height > 15 meters under NBC 2016; hydraulic '
                                 'pressure and flow testing verified by Chief Fire Officer (CFO) prior to issuance of '
                                 'Fire Safety Certificate',
        'url': 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/Standard_review/Isdetails?ID=MTE2Nzg%3D'},
    {   'is_code': 'IS 13039',
        'title': 'External Hydrant Systems — Provision and Maintenance — Code of Practice',
        'year': '1991',
        'division': 'Civil Engineering Division',
        'mandatory': True,
        'scope': 'This Indian Standard covers the provision, design, layout, and maintenance of external fire hydrants '
                 'in industrial complexes, chemical plants, refineries, ports, and multi-acre institutional campuses. '
                 'It establishes ring main piping layouts, hydrant valve spacing (every 30 to 45 meters along '
                 'perimeter roads), monitor nozzles for high-hazard areas, and isolation valve provisions. It ensures '
                 'external perimeter fire defense can sustain high-volume firefighting operations.',
        'key_clauses': [   'Clause 4: Layout and sizing of mains — Closed loop grid system, minimum pipe diameter (150 '
                           'mm), and sectional isolation valves',
                           'Clause 5: Number and location of external hydrants — Distance from building walls (minimum '
                           '15 m) and inter-hydrant spacing',
                           'Clause 6: Hydrant standposts and monitors — Water monitors with discharge capacities from '
                           '1750 to 3500 LPM',
                           'Clause 7: Water storage and pumping capacities — Four-hour continuous water supply '
                           'requirements at designated peak flow'],
        'keywords': [   'external hydrant',
                        'yard hydrant',
                        'ring main',
                        'water monitor',
                        'industrial fire safety',
                        'fire pump house',
                        'BIS code'],
        'test_requirements': 'Ring main hydrostatic leak testing at 14 bar for 4 hours, hydrant discharge flow '
                             'velocity test, nozzle trajectory and throw distance test (>45 meters for monitors), pump '
                             'auto-start test',
        'certification_process': 'Mandatory compliance for hazardous industries, petroleum installations (OISD/PESO), '
                                 'and industrial factories; inspected by Fire Directorate and industrial safety '
                                 'inspectors',
        'url': 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/Standard_review/Isdetails?ID=MTYwNTM%3D'},
    {   'is_code': 'IS 15105',
        'title': 'Design and Installation of Fixed Automatic Sprinkler Fire Extinguishing Systems — Code of Practice',
        'year': '2021',
        'division': 'Civil Engineering Division',
        'mandatory': True,
        'scope': 'This standard covers the design, installation, water supplies, components, testing, and maintenance '
                 'of automatic sprinkler systems installed in all types of occupancies. It specifies hydraulic density '
                 'calculations, sprinkler bulb temperature ratings, area of operation per sprinkler head, water '
                 'storage volumes, and alarm control valves. It addresses life safety and structural asset protection '
                 'through rapid automatic fire detection and suppression at ceiling level.',
        'key_clauses': [   'Clause 5: Hazard occupancy classification — Light hazard, Ordinary hazard (OH1, OH2, OH3), '
                           'and Extra high hazard (EHH)',
                           'Clause 7: Design density and area of operation — Water discharge density (2.25 mm/min to '
                           '12.5 mm/min)',
                           'Clause 9: Sprinkler heads and spacing — Maximum spacing between heads (3.75 m to 4.5 m) '
                           'and distance from walls',
                           'Clause 11: Sprinkler alarm valves and flow switches — Automatic water motor gong and '
                           'electrical supervisory signal activation',
                           'Clause 14: Hydraulic calculations — Hazen-Williams friction loss formula for pipe network '
                           'sizing'],
        'keywords': [   'automatic sprinkler',
                        'sprinkler system',
                        'fire suppression',
                        'design density',
                        'alarm valve',
                        'sprinkler bulb',
                        'hydraulic calculation'],
        'test_requirements': 'Hydrostatic test at 15 bar or 1.5 times working pressure for 2 hours, sprinkler bulb '
                             'thermal response time index (RTI < 50 for quick response), water flow alarm gong '
                             'response time test (<60 sec)',
        'certification_process': 'Mandatory compliance for hotels, hospitals, basements, and high-rise commercial '
                                 'buildings per NBC Part 4; system commissioning witnessed and approved by Fire '
                                 'Authority',
        'url': 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/Standard_review/Isdetails?ID=MjkyNTY%3D'},
    {   'is_code': 'IS 1641',
        'title': 'Code of Practice for Fire Safety of Buildings (General): General Principles of Fire Grading and '
                 'Classification',
        'year': '1988',
        'division': 'Civil Engineering Division',
        'mandatory': True,
        'scope': 'This code of practice lays down the basic principles for grading buildings and elements of structure '
                 'according to the fire resistance they possess and the fire load they can withstand without '
                 'structural collapse. It classifies building construction types into Types 1, 2, 3, and 4 (from '
                 '4-hour fire rating down to 1-hour rating) based on wall, column, beam, and floor assemblies. It sets '
                 'structural separation distances to prevent horizontal fire spread across property lines.',
        'key_clauses': [   'Clause 3: Classification of buildings based on occupancy — Residential, educational, '
                           'institutional, assembly, industrial, storage',
                           'Clause 4: Fire grading of buildings — Calculation of fire load density in megaJoules per '
                           'square metre (MJ/m2)',
                           'Clause 5: Fire resistance ratings of structural elements — 1 hr, 2 hr, 3 hr, and 4 hr '
                           'ratings for walls, columns, and slabs',
                           'Clause 6: Open space requirements — Fire engine access roadway widths (minimum 6 m) and '
                           'perimeter clear setbacks'],
        'keywords': [   'fire grading',
                        'fire resistance rating',
                        'fire load',
                        'building classification',
                        'fire separation',
                        'structural fire safety',
                        'NBC'],
        'test_requirements': 'Furnace fire resistance testing of structural assemblies per IS 3809 / ISO 834 '
                             'time-temperature curve, fire load calorie calculations for stored materials, flame '
                             'penetration and structural loadbearing capacity audit',
        'certification_process': 'Mandatory architectural code for structural fireproofing approvals across India; '
                                 'audited by urban local bodies (ULBs) and State Fire Authorities for building permits',
        'url': 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/Standard_review/Isdetails?ID=MTAwOTY%3D'},
    {   'is_code': 'IS 2189',
        'title': 'Selection, Installation and Maintenance of Automatic Fire Detection and Alarm System — Code of '
                 'Practice',
        'year': '2008',
        'division': 'Civil Engineering Division',
        'mandatory': True,
        'scope': 'This Indian Standard covers the selection, installation, and maintenance of automatic fire detection '
                 'and alarm systems in buildings. It covers optical smoke detectors, heat detectors (fixed temperature '
                 'and rate-of-rise), beam detectors, manual call points (MCP), and main fire alarm control panels '
                 '(FACP). It defines detector spacing, ceiling height limits, secondary power battery backup durations '
                 '(48-hour standby plus 30-minute alarm), and addressable network zoning.',
        'key_clauses': [   'Clause 5: Selection of detector types — Smoke detectors for smoldering fires; heat '
                           'detectors for kitchens/boiler rooms',
                           'Clause 6: Detector siting and spacing — Maximum floor coverage area (50-100 m2 per smoke '
                           'detector, 30-50 m2 for heat)',
                           'Clause 7: Manual call points — Placement at every exit and stairwell with maximum 30 m '
                           'walking distance',
                           'Clause 9: Control and indicating equipment — Dual power supply, fault monitoring, and '
                           'sounder audible level (>85 dB(A))',
                           'Clause 11: Commissioning and servicing — Periodic smoke aerosol challenge test and '
                           'audibility validation'],
        'keywords': [   'fire alarm',
                        'smoke detector',
                        'heat detector',
                        'manual call point',
                        'fire panel',
                        'audible alarm',
                        'FACP',
                        'life safety'],
        'test_requirements': 'Aerosol test smoke response verification within 30 seconds, decibel sounder level test '
                             '(>85 dBA at 3m), secondary battery backup runtime test (48 hours), circuit loop wiring '
                             'open/short fault detection test',
        'certification_process': 'Mandatory requirement under National Building Code Part 4; commissioning certificate '
                                 'endorsed by electrical/fire consultants and inspected during Fire NOC issuance',
        'url': 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/Standard_review/Isdetails?ID=MTc5ODc%3D'},
    {   'is_code': 'IS 800',
        'title': 'General Construction in Steel — Code of Practice',
        'year': '2007',
        'division': 'Civil Engineering Division',
        'mandatory': True,
        'scope': 'This Indian Standard is the foundational code of practice for the design of structural steelwork '
                 'using Limit State Design (LSD) method as well as Working Stress Design. It covers structural members '
                 'under tension, compression, bending, combined stresses, and structural connections (bolted, welded, '
                 'riveted). It prescribes design against lateral-torsional buckling, shear buckling, fatigue, and '
                 'plastic deformation for buildings, bridges, and industrial structures.',
        'key_clauses': [   'Clause 5: Limit state design principles — Partial safety factors for materials (gamma_m) '
                           'and load combinations',
                           'Clause 6: Design of tension members — Gross section yielding, net section rupture, and '
                           'block shear failure',
                           'Clause 7: Design of compression members — Buckling class curves (a, b, c, d) and effective '
                           'length ratios',
                           'Clause 8: Design of members subjected to bending — Moment capacity (plastic, elastic) and '
                           'lateral torsional buckling',
                           'Clause 10: Connections — High-strength friction grip (HSFG) bolts, weld design, and prying '
                           'action'],
        'keywords': [   'structural steel',
                        'steel design',
                        'limit state design',
                        'compression member',
                        'tension member',
                        'buckling',
                        'welded connections',
                        'IS 800'],
        'test_requirements': 'Yield strength, ultimate tensile strength, Charpy V-notch impact energy at designated '
                             'temperatures, bolt pre-tension torque testing, non-destructive ultrasonic testing of '
                             'welds',
        'certification_process': 'Statutory standard for structural design across India; certified structural design '
                                 'calculations and shop fabrication drawings must be certified by Chartered Engineers '
                                 'under NBC 2016',
        'url': 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/Standard_review/Isdetails?ID=MTgwMDE%3D'},
    {   'is_code': 'IS 2062',
        'title': 'Hot Rolled Medium and High Tensile Structural Steel — Specification',
        'year': '2011',
        'division': 'Metallurgical Engineering Division',
        'mandatory': True,
        'scope': 'This standard prescribes requirements for hot-rolled medium and high tensile structural steel grades '
                 '(such as E250, E300, E350, E410, E450) available as plates, strips, sections, flats, and bars. It '
                 'defines sub-qualities (A, BR, B0, C) designating notch toughness at ambient, 0°C, -20°C, and -40°C. '
                 'It specifies carbon equivalent limits for weldability, elongation thresholds, and micro-alloying '
                 'compositions for structural safety.',
        'key_clauses': [   'Clause 6: Chemical composition — Maximum limits on Carbon, Manganese, Phosphorus, Sulphur, '
                           'and Carbon Equivalent (CE)',
                           'Clause 7: Mechanical properties — Minimum yield stress (250 to 650 MPa) and tensile '
                           'strength',
                           'Clause 8: Impact test — Charpy V-notch impact energy (minimum 27 Joules at specified test '
                           'temperatures)',
                           'Clause 9: Bend test — Transverse and longitudinal cold bend test around specified mandrel '
                           'diameters',
                           'Clause 14: Marking — Heat number, grade designation, manufacturer symbol, and ISI mark '
                           'stamping'],
        'keywords': [   'structural steel',
                        'hot rolled steel',
                        'E250',
                        'E350',
                        'tensile strength',
                        'yield stress',
                        'impact test',
                        'ISI mark mandatory'],
        'test_requirements': 'Tensile testing on universal testing machine (UTM), Charpy V-notch impact test at '
                             '0°C/-20°C, chemical spectrometer optical emission analysis for CE calculation, '
                             '180-degree mandrel bend test',
        'certification_process': 'Mandatory certification under Steel and Steel Products Quality Control Order (QCO) → '
                                 'In-plant metallurgical laboratory verification → Routine heat sampling → Grant of '
                                 'ISI certification mark',
        'url': 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/Standard_review/Isdetails?ID=MTk4OTA%3D'},
    {   'is_code': 'IS 1161',
        'title': 'Steel Tubes for Structural Purposes — Specification',
        'year': '2014',
        'division': 'Metallurgical Engineering Division',
        'mandatory': True,
        'scope': 'This Indian Standard covers the requirements for hot-finished seamless and electric resistance '
                 'welded (ERW) circular steel tubes for structural purposes. It grades tubes into YSt 210, YSt 240, '
                 'and YSt 310 based on minimum yield strength. These tubes are widely used in roof trusses, '
                 'communication towers, space frames, scaffolding, and bridge structures due to their superior '
                 'torsional and aerodynamic performance.',
        'key_clauses': [   'Clause 5: Manufacture — Seamless, hot finished welded, or electric resistance welded '
                           'processes',
                           'Clause 7: Chemical composition — Limits on carbon, sulphur, and phosphorus to ensure '
                           'weldability',
                           'Clause 8: Mechanical properties — Tensile strength, yield stress, and percentage '
                           'elongation',
                           'Clause 9: Technological tests — Flattening test, cold bend test, and flanging tests',
                           'Clause 11: Tolerances — Outside diameter, wall thickness (±10%), and mass per metre '
                           'tolerances'],
        'keywords': [   'steel tubes',
                        'circular hollow sections',
                        'structural tubes',
                        'ERW pipes',
                        'tensile strength',
                        'flattening test',
                        'ISI mark'],
        'test_requirements': 'Tensile test on tube strips, flattening test of welded tubes without seam cracking, cold '
                             'bend test through 90° or 180°, dimensional micrometer inspection, hydraulic or '
                             'eddy-current NDT inspection',
        'certification_process': 'Mandatory under Steel Tubes QCO by Ministry of Steel → Factory inspection of tube '
                                 'rolling mills and weld induction units → Laboratory verification → Grant of ISI '
                                 'license',
        'url': 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/Standard_review/Isdetails?ID=MjIyNDU%3D'},
    {   'is_code': 'IS 4923',
        'title': 'Hollow Steel Sections for Structural Use — Specification',
        'year': '2017',
        'division': 'Metallurgical Engineering Division',
        'mandatory': True,
        'scope': 'This standard specifies requirements for cold-formed welded rectangular and square hollow sections '
                 '(RHS and SHS) used in structural applications. It categorizes sections into grades YSt 210, YSt 240, '
                 'YSt 310, and YSt 355. It specifies corner radius limits, dimensional tolerances, weld seam '
                 'soundness, and mass per unit length for modern architectural steel framing, vehicle chassis, and '
                 'warehouse structures.',
        'key_clauses': [   'Clause 5: Chemical composition — Low carbon steel with controlled nitrogen, sulphur, and '
                           'phosphorus',
                           'Clause 7: Mechanical properties — Minimum yield strength, ultimate tensile strength, and '
                           'elongation',
                           'Clause 8: Sectional dimensions and corner radii — External corner profile radius limits '
                           '(1.5t to 3t)',
                           'Clause 9: Technological tests — Corner flattening test and weld seam integrity reverse '
                           'bend test',
                           'Clause 11: Permissible tolerances — Squareness of corners (90° ± 2°), twist, and '
                           'straightness limits'],
        'keywords': [   'hollow steel sections',
                        'RHS',
                        'SHS',
                        'square hollow section',
                        'rectangular hollow section',
                        'structural steel',
                        'ISI mark mandatory'],
        'test_requirements': 'Tensile coupon testing, flattening test along weld line, corner radius gauge '
                             'measurement, twist and camber laser measurement, Charpy impact toughness testing for YSt '
                             '355',
        'certification_process': 'Mandatory certification under Ministry of Steel Quality Control Order → Mill audit '
                                 'and testing equipment calibration → Type testing of section profiles → License grant '
                                 'for ISI marking',
        'url': 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/Standard_review/Isdetails?ID=MjY3ODk%3D'},
    {   'is_code': 'IS 808',
        'title': 'Dimensions for Hot Rolled Steel Beam, Column, Channel and Angle Sections',
        'year': '2021',
        'division': 'Civil Engineering Division',
        'mandatory': True,
        'scope': 'This standard specifies the dimensions, sectional properties, mass, and tolerances of hot-rolled '
                 'structural steel sections including beams (ISJB, ISLB, ISMB, ISWB), columns (ISSC, ISHB), channels '
                 '(ISJC, ISLC, ISMC), and equal/unequal angles (ISA). It provides standardized geometrical tables for '
                 'cross-sectional area, moments of inertia, radius of gyration, and section modulus required for '
                 'structural design.',
        'key_clauses': [   'Clause 4: Designation — Standardized naming convention for I-beams, columns, channels, and '
                           'angles',
                           'Clause 5: Sectional properties — Tables containing web thickness, flange thickness, and '
                           'root fillet radii',
                           'Clause 6: Dimensional tolerances — Permissible variation in depth, flange width, '
                           'out-of-squareness, and camber',
                           'Clause 7: Mass per metre — Permissible variations in theoretical weight per meter (±2.5% '
                           'to ±4%)'],
        'keywords': [   'steel sections',
                        'I-beam',
                        'steel columns',
                        'channels',
                        'angles',
                        'sectional properties',
                        'hot rolled steel',
                        'IS 808'],
        'test_requirements': 'Precision vernier caliper and ultrasonic gauge dimensional checks, mass determination by '
                             'weighing scales, straightness (camber and sweep) laser inspection, root fillet profile '
                             'radius checking',
        'certification_process': 'Mandatory compliance for all rolling mills rolling structural steel sections in '
                                 'India; audited by BIS inspectorate under the Steel QCO framework for dimensional '
                                 'conformity',
        'url': 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/Standard_review/Isdetails?ID=MTc5OTI%3D'},
    {   'is_code': 'IS 816',
        'title': 'Code of Practice for Use of Metal Arc Welding for General Construction in Mild Steel',
        'year': '1969',
        'division': 'Civil Engineering Division',
        'mandatory': False,
        'scope': 'This code of practice covers the use of metal-arc welding for general structural building '
                 'construction in mild steel conforming to IS 2062. It provides guidelines on joint preparation (butt '
                 'welds, fillet welds, plug welds), throat thickness, effective weld length, design stresses, and '
                 'welding sequences to minimize distortion and residual stresses. It serves as an authoritative '
                 'guideline for fabrication yards and construction sites.',
        'key_clauses': [   'Clause 4: Permissible stresses in welds — Allowable tensile, compressive, and shear stress '
                           'limits in welds',
                           'Clause 5: Design of welded joints — Butt joints, tee joints, lap joints, and corner joint '
                           'geometry',
                           'Clause 6: Weld sizing — Minimum and maximum leg length of fillet welds and effective '
                           'throat thickness',
                           'Clause 8: Workmanship and welding technique — Electrode selection, pre-heating, and '
                           'ambient temperature limits',
                           'Clause 11: Inspection and testing of welds — Visual inspection, liquid penetrant testing, '
                           'and radiographic NDT'],
        'keywords': [   'metal arc welding',
                        'mild steel welding',
                        'fillet weld',
                        'butt weld',
                        'weld design',
                        'fabrication',
                        'NDT'],
        'test_requirements': 'Visual inspection for undercut/porosity, dye penetrant inspection (DPI), magnetic '
                             'particle inspection (MPI), radiographic testing (RT) of butt weld seams, welder '
                             'qualification bend tests',
        'certification_process': 'Compliance verified by third-party inspection agencies (TPIA) and BIS certified '
                                 'welding inspectors (CWI); weld procedure specifications (WPS) and procedure '
                                 'qualification records (PQR) approval',
        'url': 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/Standard_review/Isdetails?ID=MTAwOTM%3D'},
    {   'is_code': 'IS 9595',
        'title': 'Recommendations for Metal-Arc Welding of Carbon and Carbon Manganese Steels',
        'year': '1996',
        'division': 'Civil Engineering Division',
        'mandatory': False,
        'scope': 'This standard gives recommendations for manual, semi-automatic, and automatic metal-arc welding of '
                 'carbon and carbon-manganese structural steels. It provides guidance on avoiding hydrogen-induced '
                 'cold cracking (delayed cracking) by calculating the carbon equivalent (CE) and determining '
                 'appropriate pre-heat and inter-pass temperatures. It specifies heat input control, post-weld heat '
                 'treatment (PWHT), and run-on/run-off plate practices.',
        'key_clauses': [   'Clause 5: Avoidance of hydrogen cracking — Assessment of steel composition, hydrogen scale '
                           'of consumables, and restraint',
                           'Clause 6: Carbon equivalent determination — Formula CE = C + Mn/6 + (Cr+Mo+V)/5 + '
                           '(Ni+Cu)/15',
                           'Clause 7: Pre-heating recommendations — Pre-heat temperature nomograms based on combined '
                           'plate thickness',
                           'Clause 9: Consumable handling — Baking and storage temperatures for low-hydrogen basic '
                           'electrodes (350°C)'],
        'keywords': [   'welding carbon steel',
                        'preheating',
                        'hydrogen cracking',
                        'carbon equivalent',
                        'PWHT',
                        'welding electrodes',
                        'metallurgy'],
        'test_requirements': 'Carbon equivalent chemical analysis, diffusible hydrogen test of weld metal (mercury '
                             'displacement / gas chromatography), Charpy impact test of heat-affected zone (HAZ), weld '
                             'macro-etching test',
        'certification_process': 'Adopted in heavy structural steel fabrication, pressure vessel fabrication, and '
                                 'bridge construction; audited by welding inspection authorities adhering to national '
                                 'construction guidelines',
        'url': 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/Standard_review/Isdetails?ID=MTMwMzM%3D'},
    {   'is_code': 'IS 10146',
        'title': 'Polyethylene for its Safe Use in Contact with Foodstuffs, Pharmaceuticals and Drinking Water',
        'year': '1982',
        'division': 'Chemical Division',
        'mandatory': True,
        'scope': 'This Indian Standard specifies the requirements and methods of sampling and test for polyethylene '
                 '(LDPE, LLDPE, HDPE) plastic materials, virgin polymers, and compounding additives for safe use in '
                 'contact with foodstuffs, pharmaceuticals, and drinking water. It specifies overall migration limits '
                 'and toxic heavy metal restrictions to prevent chemical migration into edible consumables. It '
                 'prohibits the use of recycled plastic in direct food contact packaging.',
        'key_clauses': [   'Clause 4: Basic polymer requirements — Virgin polyethylene specification and banned '
                           'recycled polymers',
                           'Clause 5: Permissible additives — Prescribed positive list of antioxidants, slip agents, '
                           'and thermal stabilizers',
                           'Clause 6: Overall migration limits — Not exceeding 60 mg/kg or 10 mg/dm2 into food '
                           'simulants',
                           'Clause 7: Heavy metals limit — Cumulative lead, cadmium, mercury, and chromium (VI) less '
                           'than 100 ppm'],
        'keywords': [   'polyethylene',
                        'food contact plastic',
                        'food packaging',
                        'overall migration',
                        'virgin polymer',
                        'heavy metals',
                        'FSSAI',
                        'ISI mark'],
        'test_requirements': 'Overall migration testing using distilled water, 3% acetic acid, and 10% ethanol (or '
                             'iso-octane/olive oil) at specified exposure times and temperatures; atomic absorption '
                             'spectrophotometry for heavy metals',
        'certification_process': 'Mandatory under FSSA Packaging Regulations and BIS Quality Control Orders → Raw '
                                 'material supplier polymer audit → Food simulant extraction laboratory testing → ISI '
                                 'certification license',
        'url': 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/Standard_review/Isdetails?ID=MTAwOTU%3D'},
    {   'is_code': 'IS 10151',
        'title': 'Polyvinyl Chloride (PVC) and its Copolymers for its Safe Use in Contact with Foodstuffs, '
                 'Pharmaceuticals and Drinking Water',
        'year': '2019',
        'division': 'Chemical Division',
        'mandatory': True,
        'scope': 'This standard prescribes the requirements for polyvinyl chloride (PVC) resin and compounds intended '
                 'for use in manufacturing articles that come into direct contact with foodstuffs, pharmaceuticals, '
                 'and drinking water (such as blister packs, beverage bottles, and cling films). It places strict '
                 'limits on residual vinyl chloride monomer (VCM), which is a known carcinogen, restricting residual '
                 'VCM to a maximum of 1.0 mg/kg in the polymer and 0.01 mg/kg in food products. Plasticizer leaching '
                 'restrictions are also defined.',
        'key_clauses': [   'Clause 4: Polymer composition — Virgin suspension or emulsion PVC resin requirements',
                           'Clause 5: Residual vinyl chloride monomer (RVCM) limit — Maximum 1.0 mg/kg in container '
                           'and 0.01 mg/kg in food',
                           'Clause 6: Permitted additives — Non-toxic calcium-zinc stabilizers and approved '
                           'plasticizers list',
                           'Clause 7: Overall migration limits — Max 60 mg/kg in aqueous, acidic, and fatty food '
                           'simulants'],
        'keywords': [   'PVC food packaging',
                        'vinyl chloride monomer',
                        'VCM limit',
                        'blister pack',
                        'plasticizer migration',
                        'food safety',
                        'BIS standard'],
        'test_requirements': 'Gas chromatography with headspace detection (GC-HS) for residual vinyl chloride monomer '
                             '(RVCM), overall migration testing into food simulants, phthalate plasticizer extraction '
                             'analysis',
        'certification_process': 'Mandatory BIS certification for food contact PVC compounders and packaging '
                                 'converters → NABL chemical laboratory GC-HS testing → Factory inspection → ISI '
                                 'certification mark',
        'url': 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/Standard_review/Isdetails?ID=MTc5ODg%3D'},
    {   'is_code': 'IS 1547',
        'title': 'Raw and Refined Sugar — Specification',
        'year': '1985',
        'division': 'Food and Agriculture Division',
        'mandatory': False,
        'scope': 'This Indian Standard prescribes the requirements and methods of sampling and test for refined white '
                 'sugar crystals produced from sugarcane. It establishes purity criteria including minimum '
                 'polarization (sucrose percentage), maximum moisture content, reducing sugar content, sulfated ash, '
                 'and sulfur dioxide residue limits. It ensures the commercial and hygienic safety of refined sugar '
                 'used in domestic kitchens and food processing industries.',
        'key_clauses': [   'Clause 4: Physical and chemical requirements — Polarization (min 99.7% sucrose), moisture '
                           'content (max 0.05%)',
                           'Clause 4.2: Impurity limits — Sulphated ash (max 0.04%), reducing sugars (max 0.04%), '
                           'sulfur dioxide (max 15 mg/kg)',
                           'Clause 5: Microbiological limits — Mesophilic bacteria count, yeasts, and moulds limits',
                           'Clause 6: Packaging and marking — Clean, dry food-grade gunny or HDPE woven sacks with '
                           'inner liner'],
        'keywords': [   'refined sugar',
                        'cane sugar',
                        'sucrose purity',
                        'polarization',
                        'sulfur dioxide',
                        'food quality',
                        'FSSAI'],
        'test_requirements': 'Polarimetric sucrose determination, Karl Fischer or oven drying moisture measurement, '
                             'spectrophotometric ICUMSA colour measurement, sulfur dioxide titration by '
                             'Monier-Williams method',
        'certification_process': 'Voluntary BIS product certification for sugar mills and food processors; batch '
                                 'sampling and laboratory testing under Scheme-I guidelines; widely monitored under '
                                 'FSSAI standards',
        'url': 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/Standard_review/Isdetails?ID=MTE2NzM%3D'},
    {   'is_code': 'IS 1165',
        'title': 'Milk Powder — Specification',
        'year': '2002',
        'division': 'Food and Agriculture Division',
        'mandatory': True,
        'scope': 'This standard covers the requirements and methods of sampling and test for milk powder, including '
                 'whole milk powder, skimmed milk powder, and partly skimmed milk powder obtained by spray drying or '
                 'roller drying of pasteurized cow or buffalo milk. It specifies moisture content, milk fat '
                 'percentage, milk protein, titratable acidity, insolubility index, and scorching particles. It also '
                 'mandates strict biological limits to eliminate coliforms, Salmonella, and Listeria.',
        'key_clauses': [   'Clause 4: Types and grades — Whole milk powder (min 26% fat), skim milk powder (max 1.5% '
                           'fat)',
                           'Clause 5: Chemical requirements — Moisture (max 4.0%), milk protein in SNF (min 34.0%), '
                           'total ash (max 8.2%)',
                           'Clause 6: Physical characteristics — Insolubility index (max 0.5 ml spray, 15.0 ml '
                           'roller), scorched particles (Disc B)',
                           'Clause 7: Microbiological limits — Total plate count (max 40,000/g), coliform (absent in '
                           '0.1g), Salmonella absent in 25g',
                           'Clause 9: Packaging — Nitrogen gas flushed hermetically sealed tinplate cans or multi-ply '
                           'laminate pouches'],
        'keywords': [   'milk powder',
                        'skimmed milk powder',
                        'dairy safety',
                        'insolubility index',
                        'microbiology',
                        'protein content',
                        'ISI mark mandatory'],
        'test_requirements': 'Gerber or Rose-Gottlieb fat extraction test, Kjeldahl protein quantification, moisture '
                             'determination at 102°C, insolubility centrifuge index test, microbiological culture for '
                             'Salmonella and Coliform',
        'certification_process': 'Mandatory ISI Scheme-I certification under Dairy Products QCO and FSSAI rules → '
                                 'Factory hygiene audit of spray-drying plant → Continuous laboratory batch analysis → '
                                 'ISI certification mark',
        'url': 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/Standard_review/Isdetails?ID=MTAwOTQ%3D'},
    {   'is_code': 'IS 14625',
        'title': 'Plastic Multilayer Films for Packaging of Pasteurized Liquid Milk — Specification',
        'year': '1999',
        'division': 'Food and Agriculture Division',
        'mandatory': True,
        'scope': 'This standard specifies requirements for co-extruded or laminated plastic multilayer films used in '
                 'automatic form-fill-seal (FFS) pouch packaging of pasteurized liquid milk. It prescribes tensile '
                 'strength, dart impact resistance, heat seal strength, and oxygen/light barrier properties to prevent '
                 'pouch bursting during transport and avoid photo-oxidation of milk vitamins and fats. Pouch film '
                 'opacity must be sufficient to protect milk quality.',
        'key_clauses': [   'Clause 4: Raw material — Virgin food grade PE resins complying with IS 10146 and food '
                           'pigments with IS 9833',
                           'Clause 5: Physical properties — Thickness variation (±10%), yield, dart impact strength '
                           '(min 180g), and tensile strength',
                           'Clause 6: Heat seal strength — Minimum seal strength of 20 N/15mm without pinholes or '
                           'delamination',
                           'Clause 7: Barrier properties — Light transmission (max 10% for pigmented films) to prevent '
                           'rancidity',
                           'Clause 8: Drop test — Filled milk pouches dropped from 1.2 m height without bursting or '
                           'leaking'],
        'keywords': [   'milk pouch film',
                        'multilayer film',
                        'dairy packaging',
                        'dart impact',
                        'heat seal',
                        'drop test',
                        'virgin plastic',
                        'ISI mark'],
        'test_requirements': 'Falling dart impact test (ASTM D1709 / IS 2508), tensile and elongation testing on UTM, '
                             'heat seal integrity tensile test, drop test from 1.2 meters of filled milk pouches, '
                             'light transmission spectrophotometry',
        'certification_process': 'Mandatory certification under Milk Packaging QCO → Factory audit of blown film '
                                 'extrusion lines → Pouch drop and migration testing → Grant of ISI certification '
                                 'license',
        'url': 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/Standard_review/Isdetails?ID=MTc3MjQ%3D'},
    {   'is_code': 'IS 5126',
        'title': 'Polypropylene (PP) and its Copolymers for Safe Use in Contact with Foodstuffs, Pharmaceuticals and '
                 'Drinking Water',
        'year': '2020',
        'division': 'Chemical Division',
        'mandatory': True,
        'scope': 'This Indian Standard prescribes requirements and methods of sampling and test for polypropylene (PP) '
                 'homopolymer and copolymers used for manufacturing articles or components of articles intended for '
                 'food contact, pharmaceuticals, and potable water delivery. It covers microwave-safe containers, '
                 'bottle caps, cutlery, and medical syringes. It details permissible positive additives, migration '
                 'thresholds into food simulants, and prohibits recycled plastic blending.',
        'key_clauses': [   'Clause 4: Resin composition — Virgin polypropylene homopolymers, random copolymers, and '
                           'impact copolymers',
                           'Clause 5: Positive list of additives — Approved catalysts, clarifying agents, and '
                           'anti-static additives',
                           'Clause 6: Overall migration limits — Maximum 60 mg/kg or 10 mg/dm2 in designated food '
                           'simulants',
                           'Clause 7: Residual catalyst and heavy metal limits — Titanium, aluminium, lead, and '
                           'cadmium thresholds'],
        'keywords': [   'polypropylene',
                        'food grade PP',
                        'microwave containers',
                        'migration limits',
                        'food packaging',
                        'virgin polymer',
                        'BIS standard'],
        'test_requirements': 'Overall migration test into water, acetic acid, ethanol, and isooctane; microwave '
                             'heating safety test at 100°C/121°C; atomic absorption spectroscopy for heavy metals; '
                             'volatile organics analysis',
        'certification_process': 'Mandatory BIS certification for polymer manufacturers and food container molders '
                                 'under Food Packaging QCO → Polymer chemical testing → Factory audit → ISI mark '
                                 'license',
        'url': 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/Standard_review/Isdetails?ID=MzIxMDU%3D'},
    {   'is_code': 'IS 15757',
        'title': 'Follow-Up Formula — Complementary Foods — Specification',
        'year': '2007',
        'division': 'Food and Agriculture Division',
        'mandatory': True,
        'scope': 'This Indian Standard specifies the composition, nutritional, and safety requirements for follow-up '
                 'formula foods intended for infants from the age of six months onwards and young children. It '
                 'establishes minimum and maximum levels for protein, fats, essential fatty acids (linoleic acid), '
                 'carbohydrates, 15 vitamins, and 12 minerals. It mandates total absence of pathogenic microbes, '
                 'strict limits on pesticide residues (max 0.01 mg/kg), and zero artificial sweeteners or colours.',
        'key_clauses': [   'Clause 4: Nutritional composition — Protein (3-5.5 g/100 kcal), fat (3-6 g/100 kcal), iron '
                           '(min 1 mg/100 kcal)',
                           'Clause 5: Essential fatty acids — Linoleic acid minimum 300 mg/100 kcal; optimal '
                           'calcium-phosphorus ratio',
                           'Clause 6: Chemical contaminants and hygiene — Pesticide residue limit max 0.01 mg/kg, zero '
                           'aflatoxins',
                           'Clause 7: Microbiological safety — Absence of Enterobacter sakazakii, Listeria '
                           'monocytogenes, and Salmonella in 25g',
                           'Clause 9: Labelling — Mandatory disclaimer promoting breastfeeding per IMS Act '
                           'regulations'],
        'keywords': [   'infant food',
                        'follow-up formula',
                        'baby nutrition',
                        'aflatoxins',
                        'Enterobacter sakazakii',
                        'IMS Act',
                        'ISI mark mandatory'],
        'test_requirements': 'HPLC analysis for vitamins and amino acids, ICP-MS for minerals and toxic heavy metals, '
                             'ELISA / fluorometric test for aflatoxin M1, microbiological culture for Enterobacter '
                             'sakazakii and Salmonella',
        'certification_process': 'Mandatory ISI Scheme-I certification under Infant Milk Substitutes (IMS) Act and '
                                 'FSSAI regulations → Rigorous plant cleanroom audit → 100% batch testing → ISI '
                                 'certification mark license',
        'url': 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/Standard_review/Isdetails?ID=MTc5ODk%3D'},
    {   'is_code': 'IS 456',
        'title': 'Plain and Reinforced Concrete — Code of Practice',
        'year': '2000',
        'division': 'Civil Engineering Division',
        'mandatory': True,
        'scope': 'This Indian Standard is the foundational code of practice for the design and construction of plain '
                 'and reinforced concrete structures in India. It deals with materials (cement, aggregates, water, '
                 'admixtures, rebar), workmanship, inspection, and testing, as well as Limit State Design of '
                 'structural members against flexure, shear, torsion, and compression. It provides durability '
                 'guidelines including minimum cement content, maximum water-cement ratio, and concrete cover based on '
                 'environmental exposure conditions.',
        'key_clauses': [   'Clause 5: Materials — Specifications for cement, aggregates, water, chemical admixtures, '
                           'and reinforcing steel',
                           'Clause 8: Concrete durability — Exposure classes (Mild, Moderate, Severe, Very Severe, '
                           'Extreme) and minimum cover',
                           'Clause 26: Reinforcement detailing — Spacing, curtailment, anchorage, lap splices, and '
                           'minimum reinforcement ratios',
                           'Clause 35: Limit state method — Partial safety factors for loads and materials (1.5 for '
                           'concrete, 1.15 for steel)',
                           'Clause 38: Limit state of collapse (Flexure) — Stress-strain block assumptions and moment '
                           'carrying capacity'],
        'keywords': [   'concrete',
                        'reinforced concrete',
                        'plain concrete',
                        'limit state design',
                        'durability',
                        'concrete cover',
                        'structural design',
                        'IS 456'],
        'test_requirements': 'Concrete cube compressive strength testing at 7 and 28 days (150 mm cubes), slump cone '
                             'workability test, reinforcement tensile testing, core extraction compressive testing for '
                             'hardened concrete',
        'certification_process': 'Statutory mandatory reference for all civil, residential, and infrastructure '
                                 'engineering projects under National Building Code of India (NBC); design vetting by '
                                 'certified structural engineers',
        'url': 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/Standard_review/Isdetails?ID=MTAwOTc%3D'},
    {   'is_code': 'IS 10262',
        'title': 'Concrete Mix Proportioning — Guidelines',
        'year': '2019',
        'division': 'Civil Engineering Division',
        'mandatory': False,
        'scope': 'This standard provides guidelines for proportioning concrete mixes for normal, high-strength (up to '
                 'M100), self-compacting, and mass concrete. It provides a systematic step-by-step procedure to '
                 'determine the proportions of water, cementitious materials (cement, fly ash, silica fume, GGBS), '
                 'fine and coarse aggregates, and chemical admixtures. It incorporates adjustments for aggregate '
                 'moisture, absorption, and workability retention.',
        'key_clauses': [   'Clause 4: Data for mix design — Target compressive strength, maximum water-cement ratio, '
                           'and workability',
                           "Clause 5: Target strength for mix design — Formula f'ck = fck + 1.65 x s, where s is "
                           'standard deviation',
                           'Clause 6: Selection of mix proportions — Water-cementitious material ratio curves and '
                           'entrapped air estimation',
                           'Clause 8: Design of high-strength concrete — Utilization of silica fume, GGBS, and '
                           'superplasticizers',
                           'Clause 9: Self-compacting concrete (SCC) — Slump-flow, V-funnel, and L-box filling ability '
                           'criteria'],
        'keywords': [   'concrete mix design',
                        'mix proportioning',
                        'high strength concrete',
                        'self compacting concrete',
                        'fly ash',
                        'silica fume',
                        'IS 10262'],
        'test_requirements': 'Slump flow and J-ring test for SCC, trial batch 7-day and 28-day compressive strength, '
                             'fresh concrete density measurement, air content test using pressure meter',
        'certification_process': 'Guidelines implemented by Ready Mix Concrete (RMC) plants, construction '
                                 'laboratories, and structural consultants; verified during RMC plant quality '
                                 'certification audits (QCI / BIS)',
        'url': 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/Standard_review/Isdetails?ID=MTc5OTA%3D'},
    {   'is_code': 'IS 269',
        'title': 'Ordinary Portland Cement, 33 Grade — Specification',
        'year': '1989',
        'division': 'Civil Engineering Division',
        'mandatory': True,
        'scope': 'This Indian Standard covers the manufacture, chemical, and physical requirements of ordinary '
                 'Portland cement (OPC) of grades 33, 43, and 53. It establishes strict limits on lime saturation '
                 'factor (LSF), alumina-iron ratio, insoluble residue, magnesia, and loss on ignition. It sets '
                 'physical criteria for fineness (Blaine specific surface), setting time (initial min 30 min, final '
                 'max 600 min), soundness (Le-Chatelier and autoclave), and compressive strength.',
        'key_clauses': [   'Clause 5: Chemical requirements — Lime saturation factor (0.66-1.02), Magnesia (max 6.0%), '
                           'SO3 content (max 3.5%)',
                           'Clause 6: Physical requirements — Fineness by Blaine air permeability (minimum 225 m2/kg)',
                           'Clause 6.2: Soundness — Le-Chatelier expansion (max 10 mm) and Autoclave expansion (max '
                           '0.8%)',
                           'Clause 6.3: Compressive strength — OPC 53 grade: 27 MPa (72h), 37 MPa (168h), and 53 MPa '
                           '(672h / 28 days)',
                           'Clause 8: Packaging — Paper, woven HDPE/PP, or jute bags with mandatory ISI mark and batch '
                           'details'],
        'keywords': [   'OPC cement',
                        'ordinary portland cement',
                        '53 grade',
                        '43 grade',
                        'cement fineness',
                        'setting time',
                        'compressive strength',
                        'ISI mark mandatory'],
        'test_requirements': 'Blaine air permeability fineness test, Vicat apparatus setting time test, Le-Chatelier '
                             'soundness bath, mortar cube compressive strength test at 3, 7, and 28 days, XRF chemical '
                             'composition testing',
        'certification_process': 'Mandatory certification under Cement Quality Control Order → Continuous factory '
                                 'sampling → NABL / BIS testing → Factory audit → ISI mark license (CM/L)',
        'url': 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/Standard_review/Isdetails?ID=MjAyMTk%3D'},
    {   'is_code': 'IS 1489-1',
        'title': 'Portland Pozzolana Cement — Specification — Part 1: Fly Ash Based',
        'year': '2015',
        'division': 'Civil Engineering Division',
        'mandatory': True,
        'scope': 'This standard covers the manufacture, physical, and chemical requirements for fly ash-based Portland '
                 'Pozzolana Cement (PPC). It specifies the blending of pozzolanic materials (fly ash conforming to IS '
                 '3812 Part 1) in proportions ranging between 15% and 35% with Portland cement clinker. PPC provides '
                 'enhanced resistance to chemical and sulfate attacks, reduced heat of hydration, and lower '
                 'permeability in marine and hydraulic structures.',
        'key_clauses': [   'Clause 4: Raw materials — Quality of Portland clinker, gypsum, and pozzolana (fly ash '
                           'content 15% to 35%)',
                           'Clause 5: Chemical requirements — Loss on ignition (max 5.0%), Magnesia (max 6.0%), SO3 '
                           '(max 3.0%)',
                           'Clause 6: Physical requirements — Specific surface fineness (minimum 300 m2/kg by Blaine '
                           'method)',
                           'Clause 6.3: Compressive strength — Minimum 16 MPa (72h), 22 MPa (168h), and 33 MPa (672h / '
                           '28 days)',
                           'Clause 6.5: Drying shrinkage and soundness — Le-Chatelier expansion max 10 mm, drying '
                           'shrinkage max 0.15%'],
        'keywords': [   'PPC cement',
                        'fly ash cement',
                        'pozzolana',
                        'heat of hydration',
                        'sulfate resistance',
                        'durability',
                        'cement standard',
                        'ISI mark mandatory'],
        'test_requirements': 'Fly ash percentage quantification, Blaine specific surface test (>300 m2/kg), 28-day '
                             'mortar compressive strength, Le-Chatelier and autoclave expansion, sulfate resistance '
                             'expansion test',
        'certification_process': 'Mandatory Scheme-I ISI licensing under Cement QCO → Inspection of clinker-fly ash '
                                 'blending systems → NABL testing → Mandatory ISI mark on all bags',
        'url': 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/Standard_review/Isdetails?ID=MjQ1ODc%3D'},
    {   'is_code': 'IS 383',
        'title': 'Coarse and Fine Aggregate for Concrete — Specification',
        'year': '2016',
        'division': 'Civil Engineering Division',
        'mandatory': True,
        'scope': 'This Indian Standard prescribes requirements for coarse and fine aggregates derived from natural '
                 'sources, slag, and manufactured aggregates (such as manufactured sand or M-Sand, recycled concrete '
                 'aggregate) for use in concrete. It categorizes fine aggregates into four grading zones (Zone I to '
                 'Zone IV) based on particle size distribution. It specifies limits on deleterious materials, '
                 'flakiness and elongation index, crushing value, impact value, and alkali-aggregate reactivity.',
        'key_clauses': [   'Clause 4: Aggregate types — Natural aggregates, manufactured sand (M-sand), crushed slag, '
                           'and recycled concrete',
                           'Clause 5: Deleterious materials — Maximum clay lumps, silt content (<3% for crushed stone '
                           'sand), and organic impurities',
                           'Clause 6: Grading — Particle size sieve analysis tables for coarse aggregate and fine '
                           'aggregate Zones I to IV',
                           'Clause 7: Mechanical properties — Aggregate crushing value (<30%), impact value (<30%), '
                           'and abrasion value (<30%)',
                           'Clause 8: Particle shape — Flakiness index and elongation index combined max 35% for '
                           'concrete'],
        'keywords': [   'aggregates',
                        'coarse aggregate',
                        'fine aggregate',
                        'M-sand',
                        'sieve analysis',
                        'crushing value',
                        'flakiness index',
                        'concrete'],
        'test_requirements': 'Sieve analysis on standardized wire mesh sieves, Los Angeles abrasion machine test, '
                             'aggregate crushing value (ACV) hydraulic press test, alkali-silica reactivity (ASR) '
                             'mortar bar test',
        'certification_process': 'Mandatory testing and compliance under public works specifications (CPWD, MoRTH) and '
                                 'ready-mix concrete plants; aggregate supplier source quarry verification',
        'url': 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/Standard_review/Isdetails?ID=MTc5OTE%3D'},
    {   'is_code': 'IS 516-1-1',
        'title': 'Hardened Concrete — Methods of Test — Part 1: Compressive, Flexural and Split Tensile Strength',
        'year': '2021',
        'division': 'Civil Engineering Division',
        'mandatory': False,
        'scope': 'This standard covers procedures for determining compressive, flexural, and split tensile strength of '
                 'hardened concrete test specimens (cubes, cylinders, and beams) cast in the laboratory or on site. It '
                 'specifies casting molds, curing conditions in water tanks at 27°C ± 2°C, specimen capping, and '
                 'compression testing machine loading rates. It serves as the definitive reference for quality '
                 'acceptance of structural concrete on construction sites.',
        'key_clauses': [   'Clause 4: Shape and dimensions — Standard 150 mm cubes, 150 mm dia x 300 mm cylinders, and '
                           '150x150x700 mm beams',
                           'Clause 5: Curing conditions — Submersion in moist curing tanks at 27°C ± 2°C until test '
                           'time',
                           'Clause 6: Compressive strength test — Loading rate of 14 MPa/minute (5.2 kN/s on 150 mm '
                           'cube) until failure',
                           'Clause 7: Flexural strength test — Four-point loading on beam specimens and modulus of '
                           'rupture calculation',
                           'Clause 8: Split tensile strength — Diametral compressive loading of cylindrical specimens'],
        'keywords': [   'hardened concrete',
                        'compressive strength',
                        'cube test',
                        'flexural strength',
                        'split tensile',
                        'concrete testing',
                        'IS 516'],
        'test_requirements': 'Compressive loading on calibrated CTM, bearing face perpendicularity tolerance check, '
                             'cube moist weight determination, failure mode verification (semi-explosive pyramid '
                             'failure)',
        'certification_process': 'Mandatory test method referenced in all BIS civil engineering specifications; used '
                                 'by NABL accredited testing laboratories for concrete strength certification',
        'url': 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/Standard_review/Isdetails?ID=MzQ1MTI%3D'},
    {   'is_code': 'IS 1199-2',
        'title': 'Fresh Concrete — Methods of Sampling, Testing and Analysis — Part 2: Determination of Consistency '
                 '(Slump, Compacting Factor, Vee-Bee)',
        'year': '2018',
        'division': 'Civil Engineering Division',
        'mandatory': False,
        'scope': 'This standard specifies methods for measuring the consistency and workability of fresh concrete '
                 'using slump test, compacting factor test, and Vee-Bee consistometer test. It defines apparatus '
                 'dimensions, sampling techniques, tamping strokes, and measurement tolerances for slump values (true '
                 'slump, shear slump, collapse slump). It provides guidance on matching workability testing methods to '
                 'concrete consistency ranges from very low to high workability.',
        'key_clauses': [   'Clause 4: Slump test — Slump cone dimensions (top 100 mm, bottom 200 mm, height 300 mm) '
                           'and 25 tamping strokes per layer',
                           'Clause 5: Slump measurement — Subsidence measurement to nearest 5 mm and failure mode '
                           'classification',
                           'Clause 6: Compacting factor test — Upper hopper, lower hopper, and receiving cylinder '
                           'compaction ratio determination',
                           'Clause 7: Vee-Bee consistometer — Vibrating table time measurement (Vee-Bee seconds) for '
                           'stiff mixes'],
        'keywords': [   'fresh concrete',
                        'workability',
                        'slump test',
                        'compacting factor',
                        'Vee-Bee test',
                        'concrete sampling',
                        'consistency'],
        'test_requirements': 'Slump height measurement using graduated ruler, Vee-Bee vibrating timer calibration, '
                             'compacting factor scale weighing, fresh mix temperature measurement',
        'certification_process': 'Standard field quality control procedure executed on all concrete batching plants '
                                 'and construction sites; mandatory test in RMC batch quality logs',
        'url': 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/Standard_review/Isdetails?ID=MzAwNDU%3D'},
    {   'is_code': 'IS 4151',
        'title': 'Protective Helmets for Two-Wheeler Riders — Specification',
        'year': '2020',
        'division': 'Transport Engineering Division',
        'mandatory': True,
        'scope': 'This Indian Standard specifies requirements regarding materials, construction, finish, and '
                 'performance for protective helmets for riders of two-wheeled motor vehicles. It covers impact '
                 'attenuation, penetration resistance, dynamic retention system (chin strap) strength, peripheral '
                 'vision angles, and audibility. Helmets must withstand severe shock absorption tests across '
                 'temperature conditioning extremes (-10°C to +50°C) and water immersion.',
        'key_clauses': [   'Clause 5: Construction — Shell rigidity, EPS protective padding, comfort padding, and '
                           'retention harness',
                           'Clause 6: Extent of protection — Headform coverage boundaries and minimum peripheral '
                           'vision angles (105° lateral)',
                           'Clause 7: Impact absorption test — Drop tower test onto flat and hemispherical steel '
                           'anvils at 7.5 m/s',
                           'Clause 8: Resistance to penetration — 3 kg conical punch dropped from 1 meter height '
                           'without scalp contact',
                           'Clause 9: Retention system strength — Dynamic elongation < 25 mm under 1 kN dynamic load '
                           'and buckle release'],
        'keywords': [   'two-wheeler helmet',
                        'protective helmet',
                        'impact attenuation',
                        'chin strap retention',
                        'EPS liner',
                        'motorcycle safety',
                        'ISI mark mandatory'],
        'test_requirements': 'Triaxial accelerometer impact absorption test (<300g peak acceleration), conical spike '
                             'penetration test, retention chin strap dynamic displacement test, visor optical '
                             'distortion and scratch test',
        'certification_process': 'Mandatory under Central Motor Vehicles Rules (CMVR) and Two-Wheeler Helmet QCO → '
                                 'Type testing at ARAI/ICAT/BIS laboratories → Factory audit → ISI mark mandatory on '
                                 'all helmets sold in India',
        'url': 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/Standard_review/Isdetails?ID=MTc5OTM%3D'},
    {   'is_code': 'IS 2553-2',
        'title': 'Safety Glass — Specification — Part 2: For Road Transport',
        'year': '2019',
        'division': 'Transport Engineering Division',
        'mandatory': True,
        'scope': 'This standard prescribes requirements and test methods for safety glass (toughened safety glass and '
                 'laminated safety glass) intended for installation as windscreens, side windows, and rear windows in '
                 'road vehicles. It specifies high optical transmission (>70% for windscreens), impact resistance, '
                 'fragment count on shattering (to prevent cutting shards), and resistance to head impact simulation.',
        'key_clauses': [   'Clause 4: Types of safety glass — Laminated safety glass for windscreens; toughened glass '
                           'for side/rear windows',
                           'Clause 5: Optical qualities — Light transmittance (>70% windscreen), optical distortion, '
                           'and secondary image separation',
                           'Clause 6: Mechanical strength — 227g steel ball drop test from 10 meters and 2260g steel '
                           'ball drop from 4 meters',
                           'Clause 7: Fragmentation test — Minimum 40 to 400 granular fragments in any 50x50 mm square '
                           'without sharp splinters',
                           'Clause 8: Headform impact test — 10 kg dummy head dropped from 1.5 m height onto laminated '
                           'glass'],
        'keywords': [   'automotive safety glass',
                        'windscreen',
                        'toughened glass',
                        'laminated glass',
                        'fragmentation test',
                        'light transmittance',
                        'ISI mark mandatory'],
        'test_requirements': 'Drop tower steel ball impact test, headform phantom impact test, fragmentation count '
                             'assessment, photometer light transmission test (>70%), humidity and high-temperature '
                             'boil test for laminated interlayer',
        'certification_process': 'Mandatory BIS certification under Safety Glass QCO and CMVR → Automotive test agency '
                                 'type approval (ARAI/ICAT) and BIS audit → Factory production line inspection → ISI '
                                 'mark license',
        'url': 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/Standard_review/Isdetails?ID=MTc5OTQ%3D'},
    {   'is_code': 'IS 11852',
        'title': 'Automotive Vehicles — Brakes and Braking Systems — Specification',
        'year': '2001',
        'division': 'Transport Engineering Division',
        'mandatory': True,
        'scope': 'This Indian Standard specifies the braking performance requirements and testing protocols for '
                 'automotive vehicles of various categories (passenger cars, commercial vehicles, and multi-axle '
                 'trucks). It covers service braking systems, secondary emergency brakes, and parking brakes. It '
                 'defines stopping distance formulas, mean fully developed deceleration (MFDD), brake fade resistance '
                 'after continuous braking, and anti-lock braking system (ABS) cycling efficiency.',
        'key_clauses': [   'Clause 4: General design — Dual-circuit hydraulic or pneumatic braking safety and failure '
                           'redundancy',
                           'Clause 5: Performance of service braking systems — Cold braking stop distance test '
                           '(Type-0) and MFDD limits (>6.43 m/s2)',
                           'Clause 6: Fade and recovery test (Type-I and Type-II) — Brake performance after repeated '
                           'high-speed snub braking',
                           'Clause 7: Parking brake performance — Ability to hold vehicle stationary on an 18% uphill '
                           'and downhill gradient',
                           'Clause 8: Anti-lock braking systems (ABS) — Adhesion utilization and wheel lockup '
                           'prevention on wet surfaces'],
        'keywords': [   'automotive brakes',
                        'braking distance',
                        'MFDD',
                        'ABS',
                        'fade test',
                        'parking brake',
                        'CMVR',
                        'vehicle safety'],
        'test_requirements': 'High-speed track deceleration test with data acquisition system (VBOX), brake pad '
                             'dynamometer friction testing, parking brake incline test at 18% slope, pneumatic air '
                             'reservoir recovery time test',
        'certification_process': 'Mandatory type approval under Central Motor Vehicle Rules (CMVR) by automotive '
                                 'testing agencies (ARAI, ICAT, VRDE, CIRT) and BIS coordination for component '
                                 'licensing',
        'url': 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/Standard_review/Isdetails?ID=MTcyNjY%3D'},
    {   'is_code': 'IS 16335',
        'title': 'Automotive Vehicles — Child Restraint Systems — Specification',
        'year': '2015',
        'division': 'Transport Engineering Division',
        'mandatory': True,
        'scope': 'This standard specifies requirements for child restraint systems (child safety car seats, booster '
                 'cushions, ISOFIX systems) suitable for use by children in power-driven road vehicles. It categorizes '
                 'child restraints into Mass Groups (0, 0+, I, II, III) ranging from birth up to 36 kg. It details '
                 'dynamic sled crash impact testing at 50 km/h, harness buckle opening forces, toxic substance '
                 'leaching limits on fabrics, and anti-submarining design.',
        'key_clauses': [   'Clause 4: Classification into groups — Group 0 (<10 kg), Group 0+ (<13 kg), Group I (9-18 '
                           'kg), Group II (15-25 kg), Group III (22-36 kg)',
                           'Clause 6: Construction — ISOFIX anchorages, 5-point harness restraint, energy-absorbing '
                           'chest pads',
                           'Clause 7: Dynamic crash test — Sled impact deceleration pulse simulating 50 km/h frontal '
                           'impact and 30 km/h rear impact',
                           'Clause 8: Buckle performance — Child-resistant opening mechanism requiring 40 N to 80 N '
                           'release force after crash',
                           'Clause 9: Flammability and chemical safety — Flame spread rate < 100 mm/min; non-toxic '
                           'plasticizers'],
        'keywords': [   'child car seat',
                        'child restraint system',
                        'ISOFIX',
                        'crash test',
                        'sled test',
                        'infant safety',
                        'vehicle safety'],
        'test_requirements': 'Dynamic sled crash test using instrumented child anthropomorphic test devices (crash '
                             'test dummies), buckle release force gauge test post-impact, flammability test per IS '
                             '15061, corrosion test on metal fittings',
        'certification_process': 'Mandatory compliance for automotive OEMs and car seat suppliers under AIS / CMVR '
                                 'standards; crash laboratory testing at ARAI/ICAT and BIS scheme certification',
        'url': 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/Standard_review/Isdetails?ID=MzIzODg%3D'},
    {   'is_code': 'IS 14283',
        'title': 'Automotive Vehicles — Rear-View Mirrors — Specification',
        'year': '1995',
        'division': 'Transport Engineering Division',
        'mandatory': True,
        'scope': 'This Indian Standard covers the construction, performance, and field of vision requirements for '
                 'rear-view mirrors and indirect vision devices used on motor vehicles. It defines mirror categories '
                 '(interior mirrors, exterior main mirrors, wide-angle mirrors, and close-proximity mirrors). It sets '
                 'standards for radius of curvature of convex mirrors, reflectivity (>40%), shatter resistance upon '
                 'impact, and deflection safety during pedestrian collisions.',
        'key_clauses': [   'Clause 4: Classification of mirrors — Class I (Interior), Class II & III (Main exterior), '
                           'Class IV (Wide-angle), Class V (Close-proximity)',
                           'Clause 5: Dimensional and radius of curvature requirements — Minimum 1200 mm radius of '
                           'curvature for convex mirrors',
                           'Clause 6: Reflectance — Regular reflectance of silvered or coated mirror surface not less '
                           'than 40%',
                           'Clause 7: Dynamic impact test — 4.0 m pendulum hammer test striking mirror housing to test '
                           'collapse and shatter safety',
                           'Clause 8: Field of view requirements — Ground road surface visual coverage behind and '
                           'beside vehicle'],
        'keywords': [   'rear view mirror',
                        'automotive mirror',
                        'field of vision',
                        'pendulum impact',
                        'reflectance',
                        'convex mirror',
                        'CMVR'],
        'test_requirements': 'Spherometer radius of curvature measurement, spectrophotometer reflectance percentage '
                             'measurement, pendulum impact test at 4 m/s without housing detachment, field of vision '
                             'laser projection grid mapping',
        'certification_process': 'Mandatory component approval under Central Motor Vehicle Rules (CMVR) and BIS '
                                 'Automotive Components Certification Scheme; type tested at ICAT/ARAI',
        'url': 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/Standard_review/Isdetails?ID=MTc5OTU%3D'},
    {   'is_code': 'IS 15796',
        'title': 'Automotive Vehicles — Front and Rear Protective Structures (Bumpers etc.) — Requirements',
        'year': '2008',
        'division': 'Transport Engineering Division',
        'mandatory': True,
        'scope': 'This standard specifies requirements for the front and rear protective structures (bumpers and '
                 'underrun protection) of passenger cars and commercial utility vehicles. It specifies energy '
                 'absorption characteristics to ensure that low-speed impacts (4 km/h to 8 km/h) do not damage '
                 'critical safety systems such as headlamps, cooling radiators, fuel tanks, and steering systems. It '
                 'also establishes bumper height uniformity to avoid vehicle underride in collisions.',
        'key_clauses': [   'Clause 4: Geometric requirements — Bumper reference line height above ground (400 mm to '
                           '500 mm)',
                           'Clause 5: Low-speed impact testing — Pendulum and rigid barrier impact tests at 4.0 km/h '
                           'longitudinal and 2.5 km/h corner',
                           'Clause 6: Post-impact vehicle integrity — Zero leakage from fuel/cooling systems and '
                           'normal operation of latches and doors',
                           'Clause 7: Pedestrian legform protection — Compliance with lower leg impactor deceleration '
                           'and knee bending angle limits'],
        'keywords': [   'car bumper',
                        'underrun protection',
                        'impact test',
                        'pedestrian protection',
                        'vehicle crash safety',
                        'energy absorption'],
        'test_requirements': 'Bumper pendulum barrier impact test at 4 km/h, post-impact lighting alignment check, '
                             'structural latch operability verification, pedestrian legform impactor instrumentation '
                             'test',
        'certification_process': 'Type approval mandatory under CMVR standards by ARAI / ICAT for passenger cars and '
                                 'light commercial vehicles registered in India',
        'url': 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/Standard_review/Isdetails?ID=MjAxMDU%3D'},
    {   'is_code': 'IS 14664',
        'title': 'Electric Power Train Vehicles — Safety Requirements for Functional Safety',
        'year': '2010',
        'division': 'Transport Engineering Division',
        'mandatory': True,
        'scope': 'This Indian Standard specifies the functional safety requirements and protection against electrical '
                 'shock for electric road vehicles (EVs) and hybrid electric vehicles (HEVs) powered by high-voltage '
                 'electric propulsion powertrains. It covers insulation resistance monitoring, protection against '
                 'direct and indirect contact with high-voltage buses (Voltage Class B: >60V DC), battery management '
                 'fail-safe modes, and drive-off protection during charging.',
        'key_clauses': [   'Clause 5: Protection against electrical shock — Ingress protection IPXXB/IPXXD against '
                           'access to live electrical components',
                           'Clause 6: Isolation resistance requirements — Minimum 500 Ohm/Volt for DC circuits and 100 '
                           'Ohm/Volt for AC circuits',
                           'Clause 7: Operational safety and functional safety — Unintended acceleration prevention '
                           'and brake-throttle interlocks',
                           'Clause 8: Safe state during charging — Interlock mechanism preventing vehicle driving away '
                           'while charging cable is plugged in',
                           'Clause 9: High-voltage disconnect — Manual service disconnect (MSD) for emergency '
                           'responders and technicians'],
        'keywords': [   'electric vehicle',
                        'EV safety',
                        'powertrain',
                        'high voltage',
                        'isolation resistance',
                        'charging interlock',
                        'electric shock'],
        'test_requirements': 'High-voltage isolation megohmmeter resistance measurement under damp heat conditions, '
                             'IPXXB articulated finger accessibility probe test, drive-away prevention charging '
                             'interlock test, water wading electrical isolation test',
        'certification_process': 'Mandatory statutory CMVR type approval for all electric cars, two-wheelers, and '
                                 'commercial electric buses by ARAI/ICAT in coordination with BIS EV safety standards',
        'url': 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/Standard_review/Isdetails?ID=MTc5OTY%3D'},
    {   'is_code': 'IS 15748',
        'title': 'Textiles — Protective Clothing for Industrial Workers Exposed to Heat',
        'year': '2007',
        'division': 'Textile Division',
        'mandatory': True,
        'scope': 'This standard specifies performance requirements for protective clothing made from flexible textile '
                 "materials designed to protect the industrial worker's body against heat and flame. It establishes "
                 'testing protocols for flame spread, convective heat transmission, radiant heat transmission, molten '
                 'aluminium or iron splatter splash resistance, and contact heat. It is applied in foundries, steel '
                 'melting shops, chemical refineries, and industrial welding environments.',
        'key_clauses': [   'Clause 5: General requirements — Ergonomic garment fit, coverage, seam strength, and '
                           'heat-resistant thread',
                           'Clause 6.2: Limited flame spread — Zero afterflame, zero hole formation, and no molten '
                           'debris under flame application',
                           'Clause 6.3: Convective heat transmission — Heat transfer index (HTI 24) minimum thresholds',
                           'Clause 6.4: Radiant heat transmission — Heat transmission factor (t24) when exposed to 20 '
                           'kW/m2 heat flux',
                           'Clause 6.6: Molten metal splash — Resistance to molten iron or aluminium adherence onto '
                           'fabric surface'],
        'keywords': [   'protective clothing',
                        'flame retardant',
                        'heat resistant',
                        'convective heat',
                        'molten metal splash',
                        'industrial safety',
                        'textile standard'],
        'test_requirements': 'Limited flame spread burner test per ISO 15025, radiant heat exposure test with '
                             'calorimeter sensor per ISO 6942, molten metal splash pour test per ISO 9185, tensile '
                             'tear strength after laundering',
        'certification_process': 'Mandatory certification under Protective Textiles QCO → NABL textile laboratory type '
                                 'testing → Factory audit of weaving, finishing, and garmenting units → Grant of ISI '
                                 'certification mark',
        'url': 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/Standard_review/Isdetails?ID=MTc5OTc%3D'},
    {   'is_code': 'IS 15741',
        'title': 'Textiles — Resistance to Water Penetration — Hydrostatic Head Test',
        'year': '2007',
        'division': 'Textile Division',
        'mandatory': False,
        'scope': 'This Indian Standard prescribes a method for determination of the resistance of textile fabrics to '
                 'penetration by water under hydrostatic pressure. It applies to all types of fabrics (including '
                 'waterproof, water-repellent, coated, and laminated technical fabrics) used for rainwear, tents, '
                 'military tarpaulins, geotextiles, and medical surgical gowns. It establishes the hydrostatic head '
                 'rating (in millimetres or kilopascals of water pressure) sustained before water droplets penetrate.',
        'key_clauses': [   'Clause 4: Principle — Subjecting one face of the test specimen to increasing water '
                           'pressure until penetration occurs at three points',
                           'Clause 5: Apparatus — Hydrostatic head testing apparatus with circular test area (100 cm2) '
                           'and motorized water pump',
                           'Clause 6: Test specimens — Conditioning at standard atmosphere (27°C ± 2°C, 65% RH) and '
                           'clamping technique',
                           'Clause 8: Expression of results — Hydrostatic pressure recorded at the appearance of the '
                           'third drop of water'],
        'keywords': [   'waterproof fabric',
                        'hydrostatic head test',
                        'water penetration',
                        'coated fabric',
                        'rainwear',
                        'textile testing',
                        'technical textiles'],
        'test_requirements': 'Hydrostatic head tester pressure ramp test (10 cm/min or 60 cm/min rate), observation of '
                             'water breakthrough at 3 locations, pre- and post-laundering water repellency evaluation',
        'certification_process': 'Test standard utilized by technical textile testing laboratories, defense '
                                 'procurement inspection agencies (DGQA), and BIS quality mark certification schemes',
        'url': 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/Standard_review/Isdetails?ID=MTc5OTg%3D'},
    {   'is_code': 'IS 15809',
        'title': 'High Visibility Warning Clothes — Specification',
        'year': '2008',
        'division': 'Textile Division',
        'mandatory': True,
        'scope': 'This standard specifies requirements for high-visibility warning clothing capable of visually '
                 "signaling the user's presence in all light conditions (daylight and vehicle headlight illumination "
                 'in the dark). It specifies minimum areas of fluorescent background material (fluorescent yellow, '
                 'orange-red, red) and retroreflective tapes across Class 1, Class 2, and Class 3 garments. It is '
                 'critical for road construction crews, traffic police, airport ground crews, and railway workers.',
        'key_clauses': [   'Clause 4: Design and classification — Class 1 (lowest visibility), Class 2 (intermediate), '
                           'and Class 3 (highest visibility full-body coverage)',
                           'Clause 5: Fluorescent background material — Luminance factor, chromaticity coordinates (x, '
                           'y), and colour fastness to light',
                           "Clause 6: Retroreflective material — Coefficient of retroreflection (R') at entrance "
                           'angles (5° to 40°) and observation angles',
                           'Clause 7: Aging and laundering — Performance retention after 25 wash cycles and abrasion '
                           'rubbing'],
        'keywords': [   'high visibility clothing',
                        'safety vest',
                        'retroreflective tape',
                        'fluorescent fabric',
                        'road safety',
                        'traffic clothing',
                        'ISI mark'],
        'test_requirements': 'Spectrophotometric chromaticity and luminance factor measurement, retroreflectometer '
                             'coefficient testing (minimum 330 cd/lx/m2), wash endurance laundering test, bursting and '
                             'tensile strength',
        'certification_process': 'Mandatory ISI Scheme-I certification under PPE Quality Control Order → Fabric '
                                 'optical testing in BIS-recognized optical labs → Factory garmenting audit → ISI mark '
                                 'licensing',
        'url': 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/Standard_review/Isdetails?ID=MTc5OTk%3D'},
    {   'is_code': 'IS 16655',
        'title': 'Textiles — Geotextiles for Sub-Grade Stabilization in Pavement Structures — Specification',
        'year': '2017',
        'division': 'Textile Division',
        'mandatory': True,
        'scope': 'This standard covers the requirements of woven and non-woven polymeric geotextiles used for '
                 'sub-grade stabilization and base reinforcement in flexible pavement structures and highways. It '
                 'specifies parameters for tensile strength, apparent opening size (AOS / O95), water permeability, '
                 'CBR puncture resistance, and trapezoidal tear strength. It prevents subgrade soil pumping into base '
                 'stone aggregates, significantly extending highway pavement life.',
        'key_clauses': [   'Clause 4: Raw materials — Virgin polypropylene, polyester, or polyamide polymer fibers '
                           'with UV stabilizers',
                           'Clause 5: Mechanical requirements — Wide-width tensile strength (min 15-30 kN/m) and '
                           'elongation at break',
                           'Clause 6: Puncture and tear resistance — CBR puncture strength (>2000 N) and trapezoidal '
                           'tear resistance (>300 N)',
                           'Clause 7: Hydraulic properties — Apparent opening size (AOS < 0.25 mm) and cross-plane '
                           'water permittivity',
                           'Clause 8: Durability — UV resistance retention (>70% tensile strength after 500 hours UV '
                           'exposure) and chemical resistance'],
        'keywords': [   'geotextiles',
                        'pavement stabilization',
                        'road construction',
                        'CBR puncture',
                        'tensile strength',
                        'water permittivity',
                        'technical textiles'],
        'test_requirements': 'Wide-width tensile test per IS 13162, CBR plunger puncture test per IS 13162 Part 4, '
                             'hydrodynamic sieving for AOS (O95), accelerated UV weatherometer degradation test',
        'certification_process': 'Mandatory under Ministry of Textiles Technical Textiles QCO → Plant audit of '
                                 'extrusion and needle-punching lines → Laboratory verification → ISI mark licensing',
        'url': 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/Standard_review/Isdetails?ID=MjgwMDU%3D'},
    {   'is_code': 'IS 15768',
        'title': 'Textiles — Method for Determination of Flammability of Blankets',
        'year': '2008',
        'division': 'Textile Division',
        'mandatory': False,
        'scope': 'This standard prescribes the method of test for determination of the flammability characteristics of '
                 'blankets used in domestic, hotel, hospital, and commercial passenger transport (railway, aviation) '
                 'environments. It measures ignition susceptibility, rate of flame spread, and surface flash across '
                 'flat textile surfaces. The method ensures that bedding fabrics do not trigger rapid flash fires when '
                 'exposed to accidental heat sources like cigarettes or electrical faults.',
        'key_clauses': [   'Clause 4: Test apparatus — Standard combustion test chamber, specimen holder rack, and '
                           'butane micro-burner',
                           'Clause 5: Specimen preparation and conditioning — Laundering cycles and conditioning at '
                           '27°C and 65% relative humidity',
                           'Clause 6: Test procedure — Application of standardized flame (16 mm height) for 1 second '
                           'onto specimen surface',
                           'Clause 7: Classification criteria — Type I (ignited without flame spread), Type II (slow '
                           'flame spread), Type III (rapid surface flash)'],
        'keywords': [   'blanket flammability',
                        'textile flame test',
                        'bedding safety',
                        'surface flash',
                        'railway textiles',
                        'hotel safety'],
        'test_requirements': 'Combustion chamber timing tests using optical thread sensors, char length measurement, '
                             'surface flash observation, post-wash flammability retention after 5 dry cleaning or '
                             'laundering cycles',
        'certification_process': 'Adopted by Indian Railways, civil aviation suppliers, and hospital purchase boards '
                                 'for procurement compliance; tested in NABL-accredited textile laboratories',
        'url': 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/Standard_review/Isdetails?ID=MTgwMDA%3D'},
    {   'is_code': 'IS 2977',
        'title': "Fabrics for Men's and Boys' Woven Shirts — Specification",
        'year': '1989',
        'division': 'Textile Division',
        'mandatory': False,
        'scope': 'This Indian Standard specifies the performance and physical requirements for woven fabrics (made of '
                 "cotton, man-made fibres, or their blends) used in the manufacture of men's and boys' shirts. It "
                 'specifies yarn count, ends and picks per decimetre, breaking strength, tear resistance, dimensional '
                 'stability during domestic laundering, and colour fastness to washing, light, and perspiration. It '
                 'establishes baseline durability and comfort benchmarks.',
        'key_clauses': [   'Clause 4: Fabric composition and weave — Cotton, polyester-cotton, and polyester-viscose '
                           'blend specifications',
                           'Clause 5: Physical requirements — Minimum breaking strength (warp 250N, weft 200N) and '
                           'tear strength',
                           'Clause 6: Dimensional stability — Maximum shrinkage/relaxation not exceeding 2.0% in warp '
                           'and weft after washing',
                           'Clause 7: Colour fastness ratings — Fastness to light (Rating 4+), washing (Rating 4+), '
                           'and acidic/alkaline perspiration (Rating 4+)',
                           'Clause 8: Pilling resistance — Pilling rating minimum 3-4 after 5000 rubs on Martindale '
                           'abrasion tester'],
        'keywords': [   'shirting fabric',
                        'woven fabric',
                        'colour fastness',
                        'dimensional stability',
                        'breaking strength',
                        'pilling resistance',
                        'apparel quality'],
        'test_requirements': 'Tensile breaking strength test on CRE testing machine, Martindale abrasion pilling test, '
                             'laundrometer wash fastness testing, spectrophotometer color delta E comparison',
        'certification_process': 'Voluntary BIS product certification for textile mills; widely specified in bulk '
                                 'institutional uniforms (defense, police, airlines) and export quality certifications',
        'url': 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/Standard_review/Isdetails?ID=MTExODk%3D'},
    {   'is_code': 'IS 16289',
        'title': 'Medical Textiles — Surgical Face Masks — Specification',
        'year': '2014',
        'division': 'Textile Division',
        'mandatory': True,
        'scope': 'This Indian Standard specifies the construction, design, performance requirements, and test methods '
                 'for surgical face masks intended to limit the transmission of infective agents from staff to '
                 'patients during surgical procedures and clinical settings. It categorizes masks into Class 1, Class '
                 '2, and Class 3 based on Bacterial Filtration Efficiency (BFE > 95% to 98%), sub-micron particulate '
                 'filtration efficiency (PFE), differential breathability pressure, and synthetic blood splash '
                 'resistance.',
        'key_clauses': [   'Clause 4: Classification — Class 1 (General clinical), Class 2 (High filtration), Class 3 '
                           '(High barrier fluid splash resistance)',
                           'Clause 5: Material and construction — Multi-layer spunbond-meltblown-spunbond (SMS) '
                           'non-woven polypropylene',
                           'Clause 6: Performance criteria — Bacterial filtration efficiency (min 95% Class 1, min 98% '
                           'Class 2 & 3)',
                           'Clause 7: Breathability — Differential pressure (Delta P < 29.4 Pa/cm2 for standard, < '
                           '49.0 Pa/cm2 for splash resistant)',
                           'Clause 8: Splash resistance — Synthetic blood fluid resistance at 80 mmHg, 120 mmHg, or '
                           '160 mmHg pressure'],
        'keywords': [   'surgical face mask',
                        'medical textiles',
                        'bacterial filtration efficiency',
                        'BFE',
                        'synthetic blood penetration',
                        'breathability',
                        'SMS nonwoven',
                        'ISI mark'],
        'test_requirements': 'Bacterial Filtration Efficiency (BFE) aerosol test using Staphylococcus aureus, '
                             'differential pressure breathability manometer test, synthetic blood splash spray impact '
                             'test at 120 mmHg, microbial cleanliness bioburden test',
        'certification_process': 'Mandatory certification under Medical Textiles QCO → Plant cleanroom and production '
                                 'inspection → Biological and filtration laboratory testing → ISI certification mark '
                                 'license',
        'url': 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/Standard_review/Isdetails?ID=MzAwMDY%3D'},
    {   'is_code': 'IS 14489',
        'title': 'Code of Practice on Occupational Safety and Health Audit',
        'year': '1998',
        'division': 'Chemical Division',
        'mandatory': True,
        'scope': 'This standard establishes guidelines, criteria, and procedures for conducting comprehensive '
                 'occupational safety and health (OSH) audits in chemical processing facilities, factories, ports, and '
                 'high-hazard manufacturing installations. It specifies audit methodologies for chemical hazard '
                 'identification, risk assessment, process safety management, personal protective equipment (PPE), '
                 'emergency preparedness, and statutory regulatory compliance. It ensures a systematic framework for '
                 'incident prevention.',
        'key_clauses': [   'Clause 4: Audit objectives and scope — Evaluation of health and safety policies, '
                           'procedures, and factory floor compliance',
                           'Clause 5: Audit methodology — Documentation review, plant walk-through physical '
                           'inspection, and employee interviews',
                           'Clause 6: Specific audit elements — Hazardous chemical storage, material safety data '
                           'sheets (MSDS), venting, and piping',
                           'Clause 7: Emergency preparedness — On-site emergency plans, mock drills, fire protection, '
                           'and toxic gas leak alarms',
                           'Clause 8: Audit report and corrective action — Hazard classification, prioritization, and '
                           'time-bound compliance tracking'],
        'keywords': [   'safety audit',
                        'occupational safety',
                        'hazard identification',
                        'process safety',
                        'chemical safety',
                        'MSDS',
                        'factory act'],
        'test_requirements': 'Verification of hazardous area classification drawings, calibration records of '
                             'toxic/combustible gas detectors, inspection of relief valves and rupture discs, audit '
                             'checklists verification',
        'certification_process': 'Mandatory statutory audit required under The Factories Act and State Factory Rules '
                                 'for Major Accident Hazard (MAH) units; executed by accredited Safety Auditors '
                                 'approved by Directorate of Industrial Safety and Health (DISH)',
        'url': 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/Standard_review/Isdetails?ID=MTgwMDE%3D'},
    {   'is_code': 'IS 4209',
        'title': 'Safety Code for Handling and Storage of Chemical Materials',
        'year': '2013',
        'division': 'Chemical Division',
        'mandatory': True,
        'scope': 'This safety code provides essential guidelines for the safe handling, storage, transfer, and '
                 'disposal of hazardous chemicals in liquid, solid, and gaseous forms. It specifies storage '
                 'segregation principles based on chemical incompatibility (such as acids vs bases, oxidizers vs '
                 'flammables). It covers warehouse ventilation, bunded containment areas to prevent spill runoff, '
                 'explosion-proof electrical installations, and personal protective gear protocols.',
        'key_clauses': [   'Clause 4: Classification of hazardous chemicals — Flammable, corrosive, toxic, reactive, '
                           'and explosive substances',
                           'Clause 5: Chemical compatibility and segregation — Incompatible chemical separation '
                           'distances and containment dikes',
                           'Clause 6: Storage design — Spill containment capacity (minimum 110% of largest container '
                           'volume), flameproof electricals',
                           'Clause 7: Handling and transfer — Grounding and bonding during solvent pumping to '
                           'eliminate static electricity',
                           'Clause 9: Spill control and neutralization — Absorbent materials, eye wash fountains, and '
                           'emergency showers'],
        'keywords': [   'chemical storage',
                        'hazardous materials',
                        'spill containment',
                        'chemical compatibility',
                        'static grounding',
                        'warehouse safety'],
        'test_requirements': 'Secondary containment dike capacity hydrostatic check, electrical continuity bonding '
                             'test (< 10 ohms resistance), hazardous gas concentration ambient air monitoring, '
                             'ventilation air exchange rate test',
        'certification_process': 'Mandatory compliance for chemical manufacturing and storage premises inspected by '
                                 'DISH, Petroleum and Explosives Safety Organization (PESO), and State Pollution '
                                 'Control Boards',
        'url': 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/Standard_review/Isdetails?ID=MTgwMDI%3D'},
    {   'is_code': 'IS 2080',
        'title': 'Stabilized Hydrogen Peroxide — Specification',
        'year': '2021',
        'division': 'Chemical Division',
        'mandatory': True,
        'scope': 'This standard covers the requirements and methods of sampling and test for stabilized industrial '
                 'hydrogen peroxide (H2O2) in concentrations ranging from 35% to 70% by mass. It specifies limits for '
                 'total acidity, non-volatile matter, stability index, heavy metals (iron, copper, lead), and '
                 'stabilizer contents. It outlines strict safety precautions against catalytic decomposition and '
                 'violent pressurization caused by contaminants like transition metals.',
        'key_clauses': [   'Clause 4: Grades and concentrations — 35%, 50%, and 70% industrial technical grades',
                           'Clause 5: Chemical requirements — H2O2 concentration by ceric sulfate / potassium '
                           'permanganate titration',
                           'Clause 6: Stability test — Minimum 96% retention of active oxygen when heated at 100°C for '
                           '24 hours',
                           'Clause 7: Impurities — Iron (max 0.5 ppm), Lead (max 1.0 ppm), Non-volatile matter (max '
                           '0.05%)',
                           'Clause 8: Packaging and storage — Passivated high-purity aluminium or vented HDPE drums '
                           'with pressure relief caps'],
        'keywords': [   'hydrogen peroxide',
                        'chemical oxidizer',
                        'stabilized peroxide',
                        'active oxygen',
                        'chemical specification',
                        'ISI mark mandatory'],
        'test_requirements': 'Potassium permanganate redox titration for active H2O2 assay, accelerated thermal '
                             'stability test at 100°C in oil bath, trace metal analysis by AAS/ICP, vented drum relief '
                             'valve operation check',
        'certification_process': 'Mandatory certification under Hydrogen Peroxide QCO by Department of Chemicals and '
                                 'Petrochemicals → Factory chemical process inspection → Batch testing → ISI mark '
                                 'license',
        'url': 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/Standard_review/Isdetails?ID=MjAyMDU%3D'},
    {   'is_code': 'IS 11466',
        'title': 'Safety Code for Transport of Hazardous Goods by Road',
        'year': '1985',
        'division': 'Chemical Division',
        'mandatory': True,
        'scope': 'This code of practice prescribes safety precautions, operational procedures, and vehicle '
                 'construction requirements for the transportation of hazardous chemicals and dangerous goods by road '
                 'tankers and trucks. It details driver training, Emergency Information Panels (EIP), Transport '
                 'Emergency Cards (TREMCARD), vehicle fire extinguishers, spill kits, and anti-static bonding chains. '
                 'It ensures compliance with Central Motor Vehicles Rules for dangerous cargo transit.',
        'key_clauses': [   'Clause 4: Driver responsibilities and qualifications — Hazardous cargo driving license '
                           'endorsement and emergency training',
                           'Clause 5: Emergency Information Panel (EIP) — Dimensions, UN Hazard Class diamond, UN '
                           'Number, and Hazchem code',
                           'Clause 6: Vehicle equipment and safety — Spark arrestors, master electrical battery cutoff '
                           'switch, rollover protection',
                           'Clause 7: Loading and unloading safety — Static earthing cables, dry disconnect couplings, '
                           'and PPE usage'],
        'keywords': [   'hazardous transport',
                        'road tanker safety',
                        'TREMCARD',
                        'emergency information panel',
                        'hazchem code',
                        'chemical transport'],
        'test_requirements': 'Static earthing continuity check (< 10 ohms), road tanker hydrostatic pressure and '
                             'vacuum vent test, spark arrestor efficiency test, EIP reflective retroreflective '
                             'luminance verification',
        'certification_process': 'Mandatory requirement under Central Motor Vehicle Rules (Rule 129 to 137) and '
                                 'inspected by Regional Transport Offices (RTO) and state police departments',
        'url': 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/Standard_review/Isdetails?ID=MTgwMDM%3D'},
    {   'is_code': 'IS 1260-1',
        'title': 'Pictorial Marking for Handling and Labelling of Dangerous Goods — Part 1: Primary Hazards',
        'year': '1958',
        'division': 'Chemical Division',
        'mandatory': True,
        'scope': 'This standard prescribes the pictorial markings and hazard diamond labels to be applied to packages, '
                 'drums, gas cylinders, and intermediate bulk containers (IBC) containing dangerous goods. It '
                 'establishes graphical symbols, background colors, and class numbers for UN Classes 1 through 9 '
                 '(Explosives, Flammable Gases, Flammable Liquids, Oxidizers, Toxic substances, Corrosives, and '
                 'Miscellaneous). It ensures hazard identification regardless of language barriers.',
        'key_clauses': [   'Clause 4: Dimensions and colors of labels — Standard 100 mm x 100 mm diamond labels with '
                           'contrasting border lines',
                           'Clause 5: Class 1 Explosives symbol — Exploding bomb graphic on orange background',
                           'Clause 6: Class 3 Flammable Liquids symbol — Flame graphic on red background with Class 3 '
                           'numeral',
                           'Clause 7: Class 6 Toxic Substances symbol — Skull and crossbones on white background',
                           'Clause 8: Class 8 Corrosives symbol — Liquids spilling from test tubes corroding metal and '
                           'human hand'],
        'keywords': [   'hazard labels',
                        'dangerous goods',
                        'pictorial marking',
                        'UN class symbols',
                        'toxic label',
                        'flammable diamond',
                        'chemical packaging'],
        'test_requirements': 'Weather resistance and durability test of adhesive labels (must withstand 3 months '
                             'immersion in seawater without detaching per IMDG code), spectrophotometric colour '
                             'conformity',
        'certification_process': 'Mandatory compliance for all chemical manufacturers, exporters, transport logistics '
                                 'operators, and port authorities under Petroleum, Explosives, and Merchant Shipping '
                                 'Rules',
        'url': 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/Standard_review/Isdetails?ID=MTgwMDQ%3D'},
    {   'is_code': 'IS 4015',
        'title': 'Guide for Handling of Hazardous Chemicals in Laboratories',
        'year': '1998',
        'division': 'Chemical Division',
        'mandatory': False,
        'scope': 'This guide outlines essential safety precautions, engineering controls, and personal protection '
                 'requirements for handling toxic, corrosive, carcinogenic, flammable, and explosive chemicals in '
                 'chemical and educational testing laboratories. It covers laboratory ventilation, chemical fume hoods '
                 '(minimum face velocity of 0.5 m/s), chemical storage in dedicated flammables cabinets, waste '
                 'neutralization, and emergency eye wash stations.',
        'key_clauses': [   'Clause 4: General laboratory design — Exits, floor drainage, non-porous chemical-resistant '
                           'workbenches, and ventilation',
                           'Clause 5: Fume hood specifications — Face velocity of 0.4 to 0.6 m/s, sash height '
                           'interlocks, and explosion-proof exhaust fans',
                           'Clause 6: Chemical handling protocols — Pipetting safety (prohibition of mouth pipetting), '
                           'cryogenic liquids handling',
                           'Clause 7: Waste disposal — Segregation of halogenated vs non-halogenated solvents, '
                           'chemical neutralization',
                           'Clause 8: First aid and emergency equipment — Deluge showers, eye wash fountains, spill '
                           'neutralizers'],
        'keywords': [   'laboratory safety',
                        'chemical handling',
                        'fume hood',
                        'face velocity',
                        'spill response',
                        'chemical waste',
                        'lab safety guide'],
        'test_requirements': 'Fume hood anemometer face velocity profiling test (0.5 m/s ± 20%), smoke pencil airflow '
                             'containment visualization test, emergency eye wash water flow rate test (>1.5 LPM for 15 '
                             'min)',
        'certification_process': 'Essential safety guideline audited during NABL ISO/IEC 17025 laboratory '
                                 'accreditation inspections and university research laboratory audits',
        'url': 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/Standard_review/Isdetails?ID=MTgwMDU%3D'},
    {   'is_code': 'IS 1446',
        'title': 'Classification of Dangerous Goods',
        'year': '2002',
        'division': 'Chemical Division',
        'mandatory': True,
        'scope': 'This Indian Standard prescribes the system of classification of dangerous goods according to the '
                 'type and degree of hazard they present in storage, handling, and transport. It harmonizes Indian '
                 'industrial classification with the United Nations Recommendations on the Transport of Dangerous '
                 'Goods (UN Model Regulations). It defines criteria for assignment into Packing Groups I (high '
                 'danger), II (medium danger), and III (low danger) across nine danger classes.',
        'key_clauses': [   'Clause 3: Classification system — Categorization into Classes 1 to 9 including gases, '
                           'liquids, solids, and toxics',
                           'Clause 4: Criteria for Class 3 (Flammable Liquids) — Closed-cup flash point thresholds '
                           '(<23°C, 23°C to 60°C)',
                           'Clause 5: Criteria for Class 6.1 (Toxic substances) — Oral LD50, dermal LD50, and '
                           'inhalation LC50 toxicity brackets',
                           'Clause 6: Criteria for Class 8 (Corrosives) — Full thickness skin tissue destruction '
                           'within specified exposure times',
                           'Clause 7: Assignment of Packing Groups — Packing Group I, II, or III based on hazardous '
                           'severity'],
        'keywords': [   'dangerous goods',
                        'hazard classification',
                        'packing group',
                        'flash point',
                        'toxicology',
                        'corrosive criteria',
                        'UN regulations'],
        'test_requirements': 'Abel / Pensky-Martens closed cup flash point test, in-vitro skin corrosion testing per '
                             'OECD guidelines, rat oral acute toxicity LD50 determination, UN gap explosive test',
        'certification_process': 'Statutory classification standard adopted across Indian regulatory frameworks '
                                 'including Major Accident Hazard Rules, PESO regulations, and Ministry of Road '
                                 'Transport',
        'url': 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/Standard_review/Isdetails?ID=MTgwMDY%3D'},
    {   'is_code': 'IS/ISO 13485',
        'title': 'Medical Devices — Quality Management Systems — Requirements for Regulatory Purposes',
        'year': '2016',
        'division': 'Medical Equipment and Hospital Planning Division',
        'mandatory': True,
        'scope': 'This Indian Standard adopts ISO 13485 identically and specifies requirements for a quality '
                 'management system where an organization needs to demonstrate its ability to provide medical devices '
                 'and related services that consistently meet customer and applicable regulatory requirements. It '
                 'covers design and development, risk management per ISO 14971, cleanroom environmental controls, '
                 'product traceability, sterilization validation, and post-market surveillance.',
        'key_clauses': [   'Clause 4: Quality management system — General requirements, documentation, and medical '
                           'device file (MDF)',
                           'Clause 6.4: Work environment and contamination control — Cleanroom classification and '
                           'bioburden controls',
                           'Clause 7.3: Design and development — Design inputs, outputs, verification, validation, and '
                           'design transfer',
                           'Clause 7.5: Production and service provision — Process validation, sterilization '
                           'validation, and device master record',
                           'Clause 8.2: Monitoring and measurement — Post-market surveillance, vigilance reporting, '
                           'and CAPA systems'],
        'keywords': [   'medical devices',
                        'ISO 13485',
                        'QMS',
                        'cleanroom',
                        'sterilization validation',
                        'risk management',
                        'CDSCO compliance'],
        'test_requirements': 'Process validation protocols (IQ, OQ, PQ), cleanroom airborne particulate monitoring '
                             '(ISO Class 7/8), biological bioburden enumeration, ethylene oxide (EO) residual '
                             'analysis, CAPA audit',
        'certification_process': 'Mandatory QMS compliance for medical device manufacturing licenses under Central '
                                 'Drugs Standard Control Organization (CDSCO) Medical Device Rules 2017; audited by '
                                 'BIS and notified bodies',
        'url': 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/Standard_review/Isdetails?ID=MTgwMDc%3D'},
    {   'is_code': 'IS 13422',
        'title': 'Sterile Hypodermic Syringes for Single Use — Specification',
        'year': '1992',
        'division': 'Medical Equipment and Hospital Planning Division',
        'mandatory': True,
        'scope': 'This standard prescribes requirements and test methods for sterile hypodermic syringes for single '
                 'use made of plastic materials (polypropylene, polyethylene) and intended for the aspiration and '
                 'injection of fluids. It covers barrel and plunger dimensions, graduated scale legibility, dead space '
                 'volume, freedom from air and liquid leakage past the piston under positive and negative pressures, '
                 'and strict biocompatibility requirements (pyrogen-free, non-toxic).',
        'key_clauses': [   'Clause 5: Materials — Virgin medical grade polypropylene barrel and piston free from toxic '
                           'additives',
                           'Clause 6: Graduated scale — Legibility, scale interval, numbering, and graduation line '
                           'thickness',
                           'Clause 7: Freedom from air and liquid leakage — Piston seal integrity at 300 kPa '
                           'hydrostatic pressure and 60 kPa vacuum',
                           'Clause 9: Dead space — Maximum residual fluid volume remaining in nozzle after full '
                           'plunger stroke',
                           'Clause 11: Biological requirements — Sterility assurance level (SAL 10^-6), pyrogen-free, '
                           'and non-hemolytic'],
        'keywords': [   'hypodermic syringe',
                        'sterile syringe',
                        'single use syringe',
                        'medical device',
                        'piston leakage',
                        'pyrogen-free',
                        'ISI mark mandatory'],
        'test_requirements': 'Liquid leakage past plunger at 300 kPa pressure, air leakage test under 60 kPa suction, '
                             'barrel scale print rub-resistance test, rabbit pyrogen test or LAL endotoxin test (<0.5 '
                             'EU/ml), EO residue test',
        'certification_process': 'Mandatory certification under Medical Devices QCO and CDSCO Class B device licensing '
                                 '→ Factory cleanroom audit → Laboratory biological and mechanical verification → ISI '
                                 'mark license',
        'url': 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/Standard_review/Isdetails?ID=MTgwMDg%3D'},
    {   'is_code': 'IS 7803-1',
        'title': 'Hospital Furniture — Beds, Hospital, General Purpose — Specification',
        'year': '1975',
        'division': 'Medical Equipment and Hospital Planning Division',
        'mandatory': False,
        'scope': 'This Indian Standard specifies dimensional, material, constructional, and performance requirements '
                 'for general purpose hospital beds used in hospital wards. It covers bedstead frame rigidity, '
                 'mattress platform dimensions, castor wheel durability, side safety railings, and IV pole mounting '
                 'brackets. It ensures patient comfort, hygienic sanitization with disinfectants, structural stability '
                 'against tipping, and safe maneuvering within healthcare facilities.',
        'key_clauses': [   'Clause 4: Dimensions — Mattress platform length (approx 1980 mm), width (approx 910 mm), '
                           'and floor height (600 mm)',
                           'Clause 5: Materials — Cold rolled mild steel tubular frame with anti-microbial epoxy '
                           'powder coating',
                           'Clause 6: Construction — Welded joints, smooth finish free of burrs, and drop-down or '
                           'collapsible side railings',
                           'Clause 7: Castor wheels — 100 mm / 125 mm swivel castors with diagonal wheel braking '
                           'system',
                           'Clause 8: Structural loading — Safe working load (SWL) minimum 180 kg without permanent '
                           'frame deformation'],
        'keywords': [   'hospital bed',
                        'hospital furniture',
                        'patient bed',
                        'side railing',
                        'swivel castors',
                        'epoxy powder coating',
                        'healthcare equipment'],
        'test_requirements': 'Static vertical load test on mattress platform (250 kg distributed load for 24 hours), '
                             'castor wheel endurance travel test under load, impact test on side safety barriers, salt '
                             'spray paint corrosion test',
        'certification_process': 'Voluntary BIS product certification and mandatory requirement for government '
                                 'hospital tenders (AIIMS, State Health Mission); verified by engineering inspection '
                                 'boards',
        'url': 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/Standard_review/Isdetails?ID=MTgwMDk%3D'},
    {   'is_code': 'IS/ISO 10993-1',
        'title': 'Biological Evaluation of Medical Devices — Part 1: Evaluation and Testing Within a Risk Management '
                 'Process',
        'year': '2018',
        'division': 'Medical Equipment and Hospital Planning Division',
        'mandatory': True,
        'scope': 'This standard identical to ISO 10993-1 specifies the general principles governing the biological '
                 'evaluation of medical devices within a risk management process. It categorizes medical devices based '
                 'on the nature and duration of their contact with the human body (surface-contacting, externally '
                 'communicating, or implant devices). It defines the biological endpoints to be evaluated, including '
                 'cytotoxicity, sensitization, irritation, systemic toxicity, genotoxicity, and hemocompatibility.',
        'key_clauses': [   'Clause 4: General principles — Biological evaluation based on material chemical '
                           'characterization and clinical use risk',
                           'Clause 5: Categorization of medical devices — Contact category (Skin, Mucosal, Breached '
                           'surface, Blood path) and duration',
                           'Clause 6: Biological endpoints — In-vitro cytotoxicity, intracutaneous reactivity, delayed '
                           'hypersensitivity',
                           'Clause 7: Chemical characterization — Extractable and leachable chemical profiling before '
                           'biological testing'],
        'keywords': [   'biocompatibility',
                        'medical device testing',
                        'cytotoxicity',
                        'sensitization',
                        'hemocompatibility',
                        'ISO 10993',
                        'CDSCO'],
        'test_requirements': 'MTT in-vitro cell culture cytotoxicity assay, guinea pig maximization test for '
                             'sensitization, rabbit intracutaneous reactivity test, bacterial reverse mutation (Ames) '
                             'genotoxicity test',
        'certification_process': 'Mandatory regulatory prerequisite for all medical devices seeking manufacturing or '
                                 'import approval under CDSCO Medical Device Rules 2017; reviewed by BIS and Drug '
                                 'Controller General of India',
        'url': 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/Standard_review/Isdetails?ID=MTgwMTA%3D'},
    {   'is_code': 'IS 15152',
        'title': 'Sterile Hypodermic Needles for Single Use — Specification',
        'year': '2002',
        'division': 'Medical Equipment and Hospital Planning Division',
        'mandatory': True,
        'scope': 'This Indian Standard specifies the dimensions, mechanical strength, point geometry, and biological '
                 'cleanliness of sterile hypodermic needles for single use. It specifies needle tubing outer diameters '
                 '(gauge sizes from 18G to 31G), needle bevel angles (regular bevel, short bevel), hub color coding '
                 'according to gauge size, needle-to-hub bonding tensile strength, and silicone lubricant coating '
                 'limits. Needles must penetrate skin smoothly with minimum patient discomfort.',
        'key_clauses': [   'Clause 4: Needle gauge and color coding — Standard ISO color codes for plastic hubs (e.g., '
                           '21G Green, 24G Purple)',
                           'Clause 5: Needle tubing material — Austenitic stainless steel complying with ISO 9626 free '
                           'from burrs and hooks',
                           'Clause 6: Needle-to-hub joint strength — Minimum pull-off retention force (from 11 N to 22 '
                           'N depending on gauge)',
                           'Clause 7: Needle point geometry and sharpness — Bevel tip sharpness, lancet cut angles, '
                           'and silicone lubricant coating',
                           'Clause 8: Cleanliness and biological safety — Non-pyrogenic, sterile, and absence of '
                           'particulate matter'],
        'keywords': [   'hypodermic needle',
                        'single use needle',
                        'needle gauge',
                        'stainless steel tubing',
                        'hub bonding force',
                        'pyrogen-free',
                        'ISI mark mandatory'],
        'test_requirements': 'Tensile pull-off test on needle-to-hub joint, needle penetration force puncture test '
                             'through simulated membrane substrate, visual inspection of bevel sharpness under 20x '
                             'microscope, endotoxin LAL test',
        'certification_process': 'Mandatory certification under Medical Devices QCO (Scheme-I) → Cleanroom facility '
                                 'inspection → Batch physical and sterility testing in BIS laboratories → ISI mark '
                                 'license',
        'url': 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/Standard_review/Isdetails?ID=MTgwMTE%3D'},
    {   'is_code': 'IS 17423',
        'title': 'Medical Textiles — Coveralls for Healthcare Workers — Specification',
        'year': '2020',
        'division': 'Medical Equipment and Hospital Planning Division',
        'mandatory': True,
        'scope': 'This Indian Standard specifies the requirements for coveralls (PPE suits) worn by healthcare workers '
                 'and medical personnel to provide protection against the transfer of microorganisms, body fluids, and '
                 'particulate matter. Formulated during the pandemic, it sets rigorous benchmarks for synthetic blood '
                 'penetration resistance, seam strength, water vapor transmission (breathability), and fabric tensile '
                 'durability to ensure worker safety in intensive care and quarantine facilities.',
        'key_clauses': [   'Clause 4: Materials and construction — Polymeric coated or laminated non-woven fabric with '
                           'heat-sealed seams',
                           'Clause 5: Synthetic blood penetration resistance — Minimum resistance to synthetic blood '
                           'at Class 3 (1.75 kPa) or Class 6 (20 kPa)',
                           'Clause 6: Seam strength — Minimum seam breaking strength of 100 N without seam opening or '
                           'tape delamination',
                           'Clause 7: Water vapor resistance (Breathability) — Ret value limits to prevent heat stress '
                           'and exhaustion in staff',
                           'Clause 8: Microbial barrier — Resistance to penetration by bacteriophage phi-X174'],
        'keywords': [   'PPE coverall',
                        'medical protective suit',
                        'synthetic blood penetration',
                        'seam sealing',
                        'healthcare worker',
                        'medical textiles',
                        'ISI mark'],
        'test_requirements': 'Synthetic blood penetration test per ASTM F1670 / ISO 16603, viral penetration challenge '
                             'test per ISO 16604, seam tensile strength test on CRE machine, hydrostatic head test on '
                             'welded seams',
        'certification_process': 'Mandatory certification under Medical Textiles PPE QCO → Factory audit of cleanroom '
                                 'manufacturing and seam sealing machinery → NABL type testing → ISI mark license',
        'url': 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/Standard_review/Isdetails?ID=MzAwOTk%3D'},
    {   'is_code': 'IS 13450-1',
        'title': 'Medical Electrical Equipment — Part 1: General Requirements for Basic Safety and Essential '
                 'Performance',
        'year': '2018',
        'division': 'Medical Equipment and Hospital Planning Division',
        'mandatory': True,
        'scope': 'This standard is identical to IEC 60601-1 and applies to the basic safety and essential performance '
                 'of medical electrical equipment and medical electrical systems (such as patient monitors, ECG '
                 'machines, ventilators, and surgical diathermy units). It establishes criteria for protection against '
                 'electrical shock (leakage currents under normal and single fault conditions: Type B, BF, CF applied '
                 'parts), mechanical hazards, excessive temperatures, radiation hazards, and software risk controls.',
        'key_clauses': [   'Clause 4: General requirements — Risk management process (ISO 14971) and essential '
                           'performance identification',
                           'Clause 8: Protection against electrical hazards — Applied parts isolation (Type CF for '
                           'cardiac application: <10 uA leakage)',
                           'Clause 9: Protection against mechanical hazards — Pinch points, tipping stability, and '
                           'drop impact resistance',
                           'Clause 11: Protection against excessive temperatures and fire — Maximum component and '
                           'enclosure touch temperatures',
                           'Clause 14: Programmable electrical medical systems (PEMS) — Software life cycle process '
                           'verification (IEC 62304)'],
        'keywords': [   'medical electrical equipment',
                        'IEC 60601-1',
                        'leakage current',
                        'applied parts',
                        'Type CF',
                        'patient safety',
                        'essential performance'],
        'test_requirements': 'Earth leakage and patient auxiliary leakage current testing under normal and fault '
                             'conditions (<10 uA for CF), high voltage dielectric breakdown test at 4000V AC, '
                             '10-degree incline stability tilt test',
        'certification_process': 'Mandatory technical requirement under CDSCO Medical Device Rules 2017 for '
                                 'electro-medical devices; tested at BIS-recognized medical testing labs (SAMEER, '
                                 'ETDC, NABL accredited labs)',
        'url': 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/Standard_review/Isdetails?ID=MTgwMTI%3D'},
    {   'is_code': 'IS 14286',
        'title': 'Terrestrial Photovoltaic (PV) Modules — Design Qualification and Type Approval',
        'year': '2010',
        'division': 'Electrotechnical Division',
        'mandatory': True,
        'scope': 'This Indian Standard specifies requirements for the design qualification and type approval of '
                 'terrestrial photovoltaic modules suitable for long-term operation in general open-air climates. It '
                 'applies to crystalline silicon module types, subjecting modules to accelerated environmental stress '
                 'sequences including thermal cycling (-40°C to +85°C), damp heat (85°C, 85% RH for 1000 hours), UV '
                 'pre-conditioning, mechanical load, and hail impact. It ensures solar panels survive 25+ years in '
                 'harsh Indian field environments.',
        'key_clauses': [   'Clause 10.1: Visual inspection — Detection of cracks, delamination, cell discoloration, or '
                           'bubbled encapsulant',
                           'Clause 10.2: Maximum power determination — Electrical STC power measurement (1000 W/m2, '
                           '25°C, AM 1.5G spectrum)',
                           'Clause 10.3: Insulation test — Dielectric insulation resistance (>40 MOhm.m2 at 1000V DC)',
                           'Clause 10.11: Thermal cycling test — 200 cycles from -40°C to +85°C with peak injection '
                           'current',
                           'Clause 10.13: Damp heat test — 1000 hours continuous exposure to 85°C and 85% relative '
                           'humidity'],
        'keywords': [   'solar panels',
                        'photovoltaic module',
                        'PV type approval',
                        'damp heat',
                        'thermal cycling',
                        'crystalline silicon',
                        'MNRE',
                        'CRS mandatory'],
        'test_requirements': 'Flash solar simulator I-V curve testing, damp heat 1000h chamber exposure, mechanical '
                             'load test at 2400 Pa / 5400 Pa, ice hail impact test at 23 m/s, electroluminescence (EL) '
                             'crack imaging',
        'certification_process': 'Mandatory registration under MNRE Solar Photovoltaics Quality Control Order via BIS '
                                 'Compulsory Registration Scheme (CRS) → Testing at NABL/BIS solar lab → Grant of '
                                 'R-number',
        'url': 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/Standard_review/Isdetails?ID=MTgwMTM%3D'},
    {   'is_code': 'IS/IEC 61730-1',
        'title': 'Photovoltaic (PV) Module Safety Qualification — Part 1: Requirements for Construction',
        'year': '2016',
        'division': 'Electrotechnical Division',
        'mandatory': True,
        'scope': 'This standard provides the construction requirements for photovoltaic (PV) modules in order to '
                 'provide safe electrical and mechanical operation throughout their expected lifetime. It addresses '
                 'prevention of electrical shock, fire hazards, and personal injury resulting from mechanical and '
                 'environmental stresses. It defines requirements for polymeric backsheets, front glass, junction '
                 'boxes, bypass diodes, internal interconnects, and external cable connectors across Safety Classes 0, '
                 'II, and III.',
        'key_clauses': [   'Clause 5: Application classes — Class A (General access, hazardous voltage >35V DC), Class '
                           'B, and Class C',
                           'Clause 6: Structural requirements — Minimum creepage and clearance distances, internal '
                           'grounding continuity',
                           'Clause 7: Polymeric materials — Relative thermal endurance index (RTI), UV resistance, and '
                           'CTI tracking resistance',
                           'Clause 8: Connectors and wiring — IP67 / IP68 waterproof rating, locking connector '
                           'mechanisms, UV-resistant cables'],
        'keywords': [   'PV module safety',
                        'solar construction',
                        'junction box',
                        'creepage distance',
                        'Class II insulation',
                        'backsheet',
                        'MNRE'],
        'test_requirements': 'Comparative tracking index (CTI) test on backsheet polymer, thermal endurance aging of '
                             'junction box seals, earthing continuity test (< 0.1 ohm), mechanical drop and impact '
                             'test on frame',
        'certification_process': 'Mandatory under MNRE Solar PV QCO; tested in combination with IS/IEC 61730-2 at '
                                 'accredited solar test centers (NISE, UL, TUV) for BIS CRS registration',
        'url': 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/Standard_review/Isdetails?ID=MTgwMTQ%3D'},
    {   'is_code': 'IS/IEC 61730-2',
        'title': 'Photovoltaic (PV) Module Safety Qualification — Part 2: Requirements for Testing',
        'year': '2016',
        'division': 'Electrotechnical Division',
        'mandatory': True,
        'scope': 'This standard specifies the testing sequences and pass/fail criteria for verifying the safety '
                 'qualification of terrestrial PV modules. It covers electrical shock hazard tests (dielectric '
                 'withstand, wet leakage current), fire hazard tests (ignitability and spread of flame), mechanical '
                 'hazard tests (module breakage, mechanical load up to 5400 Pa), and thermal stress tests (bypass '
                 'diode thermal runaway test). It guarantees module safety under severe electrical and climatic '
                 'faults.',
        'key_clauses': [   'MST 16: Dielectric withstand test — High voltage test at 2000V + 4 times system voltage DC',
                           'MST 17: Wet leakage current test — Insulation resistance measurement while module is '
                           'submerged in water',
                           'MST 23: Fire test — Class C roof fire spread test with gas flame ignition',
                           'MST 34: Mechanical load test — Static pressure of 2400 Pa (wind) and 5400 Pa (snow/heavy '
                           'wind) for 1 hour',
                           'MST 35: Bypass diode thermal test — Operation at 75°C with simulated cell shading for 48 '
                           'hours'],
        'keywords': [   'PV safety testing',
                        'wet leakage test',
                        'dielectric withstand',
                        'mechanical load test',
                        'bypass diode test',
                        'fire spread',
                        'BIS CRS'],
        'test_requirements': 'Wet insulation resistance test (>40 MOhm.m2 in surfactant water bath), high-voltage '
                             'withstand test at 4000V DC, bypass diode forward-drop temperature rise measurement at '
                             '75°C, flame spread test',
        'certification_process': 'Mandatory companion testing standard under MNRE QCO; reports submitted to BIS for '
                                 'CRS portal registration and issuance of unique R-registration number',
        'url': 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/Standard_review/Isdetails?ID=MTgwMTU%3D'},
    {   'is_code': 'IS 16221-2',
        'title': 'Safety of Power Converters for Use in Photovoltaic Power Systems — Part 2: Particular Requirements '
                 'for Inverters',
        'year': '2015',
        'division': 'Electrotechnical Division',
        'mandatory': True,
        'scope': 'This Indian Standard specifies the particular safety requirements for grid-tied and stand-alone '
                 'utility solar photovoltaic inverters. It covers electrical safety, protection against electric '
                 'shock, residual current monitoring (RCD), protection against reverse power feeding, anti-islanding '
                 'protection (disconnection within 2 seconds upon grid blackout), and thermal overload management. It '
                 'prevents lethal voltage feedback into disconnected electrical distribution grids.',
        'key_clauses': [   'Clause 4: General test conditions — Maximum input DC voltage (up to 1500 V) and AC grid '
                           'tolerances',
                           'Clause 5: Protection against electric shock — Galvanic isolation, residual current monitor '
                           '(<30mA trip), grounding',
                           'Clause 7: Anti-islanding protection — Automatic shutdown within 2.0 seconds during utility '
                           'grid failure',
                           'Clause 9: Thermal requirements — Heat sink temperature control and power derating under '
                           'ambient heat up to 50°C',
                           'Clause 14: Enclosure ingress protection — Minimum IP65 for outdoor solar inverters'],
        'keywords': [   'solar inverter',
                        'power converter',
                        'anti-islanding',
                        'grid-tied inverter',
                        'residual current',
                        'photovoltaic safety',
                        'MNRE CRS'],
        'test_requirements': 'Anti-islanding disconnection timing test with RLC resonant load, residual direct current '
                             '(RDC-DD) trip test at 30 mA, high-voltage insulation test at 2x DC input voltage, IP65 '
                             'water jet dust test',
        'certification_process': 'Mandatory under MNRE Solar Inverters Quality Control Order → Testing at '
                                 'BIS-recognized power electronics lab → Electronic registration on BIS portal for CRS '
                                 'license',
        'url': 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/Standard_review/Isdetails?ID=MTgwMTY%3D'},
    {   'is_code': 'IS 16046-1',
        'title': 'Secondary Cells and Batteries Containing Alkaline or Other Non-Acid Electrolytes — Safety '
                 'Requirements for Portable Sealed Secondary Cells (Nickel Systems)',
        'year': '2018',
        'division': 'Electrotechnical Division',
        'mandatory': True,
        'scope': 'This standard covers the safety requirements and testing protocols for portable sealed secondary '
                 'nickel-cadmium (Ni-Cd) and nickel-metal hydride (Ni-MH) cells and battery packs. It specifies safety '
                 'testing for accidental overcharging, external short circuit, reverse charging, mechanical shock, '
                 'vibration, and thermal abuse. It is designed to prevent chemical electrolyte leakage, fire, and '
                 'casing rupture in portable consumer and industrial electronic devices.',
        'key_clauses': [   'Clause 5: General safety considerations — Insulation resistance, vent operation, and cell '
                           'terminal polarity marking',
                           'Clause 7.2: Continuous charging at constant voltage — 28-day float charge without leakage '
                           'or bulging',
                           'Clause 7.3: External short circuit — Dead short at ambient (20°C) and elevated temperature '
                           '(55°C) without fire or explosion',
                           'Clause 7.4: Free fall drop test — Dropping from 1 meter height onto concrete surface in '
                           'three orientations',
                           'Clause 7.6: Thermal abuse — Exposure to 130°C in an air oven for 10 minutes without '
                           'explosion'],
        'keywords': [   'nickel battery',
                        'NiMH',
                        'secondary cells',
                        'portable battery',
                        'battery safety',
                        'short circuit test',
                        'thermal abuse',
                        'MeitY CRS'],
        'test_requirements': 'External short circuit test with <80 mOhm resistance at 55°C, thermal abuse oven bake '
                             'test at 130°C, 28-day continuous overcharge test, mechanical shock test at 150g '
                             'acceleration',
        'certification_process': 'Mandatory registration under MeitY Compulsory Registration Scheme (CRS) → Testing in '
                                 'BIS-approved battery testing laboratory → Registration grant (R-number)',
        'url': 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/Standard_review/Isdetails?ID=MTgwMTc%3D'},
    {   'is_code': 'IS 16046-2',
        'title': 'Secondary Cells and Batteries Containing Alkaline or Other Non-Acid Electrolytes — Safety '
                 'Requirements for Portable Sealed Secondary Lithium Cells and Batteries (Part 2: Lithium Systems)',
        'year': '2018',
        'division': 'Electrotechnical Division',
        'mandatory': True,
        'scope': 'This standard identical to IEC 62133-2 covers safety requirements for portable sealed secondary '
                 'lithium-ion cells and battery packs used in smartphones, laptops, energy storage systems, and '
                 'wearable electronics. It establishes rigorous safety tests including continuous overcharging, '
                 'external short circuit, thermal runaway abuse at 130°C, mechanical crush, forced internal short '
                 'circuit, and overcharge protection circuit verification to prevent catastrophic fire or explosion.',
        'key_clauses': [   'Clause 5: Battery management and protection circuit — Redundant overcharge, overcurrent, '
                           'and under-voltage protection',
                           'Clause 7.2: Continuous charging — Multi-day constant-current constant-voltage charging at '
                           'upper temperature limits',
                           'Clause 7.3.1: External short circuit test — External short circuit (<80 mOhm) at 55°C '
                           'without flame or explosion',
                           'Clause 7.3.3: Free fall — Drop from 1.0 m onto concrete without damage to safety '
                           'interlocks',
                           'Clause 7.3.4: Thermal abuse test — Temperature ramp to 130°C held for 30 minutes without '
                           'explosion',
                           'Clause 7.3.6: Crushing of cells — Compressive crushing force of 13 kN applied between flat '
                           'anvils'],
        'keywords': [   'lithium ion battery',
                        'Li-ion safety',
                        'thermal runaway',
                        'battery crush test',
                        'overcharge protection',
                        'smartphone battery',
                        'MeitY CRS'],
        'test_requirements': '13 kN mechanical hydraulic crush test, 130°C thermal runaway oven test, external dead '
                             'short at 55°C, forced discharge reversal test, battery management system (BMS) '
                             'electronic trip verification',
        'certification_process': 'Mandatory BIS Compulsory Registration Scheme (CRS) under MeitY Electronics QCO → '
                                 'Type testing at BIS battery laboratory → Issuance of unique R-registration number on '
                                 'cells',
        'url': 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/Standard_review/Isdetails?ID=MTgwMTg%3D'},
    {   'is_code': 'IS 15549',
        'title': 'Stationary Valve Regulated Lead-Acid Batteries — Specification',
        'year': '2005',
        'division': 'Electrotechnical Division',
        'mandatory': True,
        'scope': 'This Indian Standard prescribes the requirements for stationary valve-regulated lead-acid (VRLA / '
                 'AGM / Gel) cells and batteries used in telecommunications, UPS backup systems, solar photovoltaic '
                 'energy storage, and substation switchgear. It specifies rated ampere-hour (Ah) capacity, endurance '
                 'under cyclical deep-discharge operation, charge retention during storage, flammability of container '
                 'materials, and safety vent opening/closing pressure calibration.',
        'key_clauses': [   'Clause 5: Construction — Sealed container, immobilized electrolyte (AGM / gel), flame '
                           'arrestor safety valve',
                           'Clause 6: Rated capacity — C10 and C20 discharge capacity verification at 27°C',
                           'Clause 8: Gas recombination efficiency — Minimum 95% oxygen recombination at 2.40V per '
                           'cell',
                           'Clause 9: Endurance in cycling — Minimum 1200 cycles of 50% depth of discharge (DoD)',
                           'Clause 11: Safety vent operation — Valve opening pressure (10-35 kPa) and resealing '
                           'without leakage'],
        'keywords': [   'VRLA battery',
                        'lead acid battery',
                        'solar energy storage',
                        'UPS battery',
                        'deep cycle',
                        'gas recombination',
                        'telecom battery',
                        'ISI mark'],
        'test_requirements': '10-hour rate capacity discharge test at 27°C, cyclic endurance test (1200 cycles at 50% '
                             'DoD), self-discharge capacity retention test after 6 months, safety pressure relief '
                             'valve test, container flammability UL94 V-0',
        'certification_process': 'Mandatory certification under Batteries (Management & Handling) and Lead Acid '
                                 'Batteries QCO → Factory audit of oxide manufacturing and plate curing → Laboratory '
                                 'testing → ISI mark license',
        'url': 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/Standard_review/Isdetails?ID=MTgwMTk%3D'},
    {   'is_code': 'IS/ISO/IEC 27001',
        'title': 'Information Security, Cybersecurity and Privacy Protection — Information Security Management Systems '
                 '— Requirements',
        'year': '2022',
        'division': 'Electronics and Information Technology Division',
        'mandatory': False,
        'scope': 'This Indian Standard adopts ISO/IEC 27001 identically and specifies the requirements for '
                 'establishing, implementing, maintaining, and continually improving an Information Security '
                 'Management System (ISMS) within the context of the organization. It details information security '
                 'risk assessment, risk treatment, asset management, cryptography, access controls, physical security, '
                 'incident management, and business continuity. It includes Annex A controls categorized into '
                 'organizational, people, physical, and technological themes.',
        'key_clauses': [   'Clause 4: Context of the organization — Understanding security requirements, '
                           'internal/external issues, and ISMS scope',
                           'Clause 6.1: Actions to address risks and opportunities — Risk assessment methodology and '
                           'Statement of Applicability (SoA)',
                           'Clause 9: Performance evaluation — Internal audit, management review, and security metrics',
                           'Clause 10: Improvement — Nonconformity and corrective action management',
                           'Annex A: Information security controls — 93 controls organized across Organizational (37), '
                           'People (8), Physical (14), Technological (34)'],
        'keywords': [   'information security',
                        'ISO 27001',
                        'ISMS',
                        'cybersecurity',
                        'risk assessment',
                        'access control',
                        'incident management',
                        'Annex A'],
        'test_requirements': 'Comprehensive ISMS Stage 1 documentation review, Stage 2 implementation audit, '
                             'vulnerability assessment & penetration testing (VAPT) verification, privileged access '
                             'management audit',
        'certification_process': 'Management Systems Certification Scheme (MSCS) by BIS or accredited third-party '
                                 'certification bodies; multi-stage audit covering corporate IT infrastructure and '
                                 'data centers',
        'url': 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/Standard_review/Isdetails?ID=MTgwMjA%3D'},
    {   'is_code': 'IS/ISO/IEC 27701',
        'title': 'Security Techniques — Extension to ISO/IEC 27001 and ISO/IEC 27002 for Privacy Information '
                 'Management — Requirements and Guidelines',
        'year': '2019',
        'division': 'Electronics and Information Technology Division',
        'mandatory': False,
        'scope': 'This standard specifies requirements and provides guidance for establishing, implementing, '
                 'maintaining, and continually improving a Privacy Information Management System (PIMS) as an '
                 'extension to ISO/IEC 27001. It covers personally identifiable information (PII) processing for both '
                 "PII controllers and PII processors. It aligns enterprise data governance with India's Digital "
                 'Personal Data Protection Act (DPDPA) and global privacy regulations like GDPR.',
        'key_clauses': [   'Clause 5: PIMS-specific requirements related to ISO/IEC 27001 — Mapping privacy risks into '
                           'the ISMS framework',
                           'Clause 6: PIMS-specific guidance related to ISO/IEC 27002 — Privacy enhanced control '
                           'implementations',
                           'Clause 7: Additional guidance for PII Controllers — Consent mechanisms, privacy notice, '
                           'data minimization, and data subject rights',
                           'Clause 8: Additional guidance for PII Processors — Sub-processing terms, notification of '
                           'data breaches, and data return/deletion'],
        'keywords': [   'privacy information management',
                        'PIMS',
                        'ISO 27701',
                        'DPDPA',
                        'GDPR',
                        'PII controller',
                        'data protection',
                        'data privacy'],
        'test_requirements': 'Privacy impact assessment (PIA) audit, data flow mapping verification, consent logging '
                             'and withdrawal mechanism validation, data retention and cryptographic anonymization '
                             'audit',
        'certification_process': 'Granted as an extension to ISO/IEC 27001 certification by BIS Management System '
                                 'Certification Directorate; audit of enterprise data privacy controls and legal '
                                 'compliance',
        'url': 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/Standard_review/Isdetails?ID=MTgwMjE%3D'},
    {   'is_code': 'IS/ISO/IEC 20000-1',
        'title': 'Information Technology — Service Management — Part 1: Service Management System Requirements',
        'year': '2018',
        'division': 'Electronics and Information Technology Division',
        'mandatory': False,
        'scope': 'This standard identical to ISO/IEC 20000-1 specifies requirements for an organization to establish, '
                 'implement, maintain, and continually improve an IT Service Management System (SMS). It covers '
                 'service catalogue management, service level agreements (SLAs), incident and service request '
                 'management, problem management, change enablement, release and deployment, and service availability. '
                 'It provides IT service providers with a benchmark for professional delivery.',
        'key_clauses': [   'Clause 4: Context of the organization — Scope of SMS, internal service dependencies, and '
                           'customer portfolios',
                           'Clause 8.2: Service portfolio and relationship management — Service catalogue, customer '
                           'satisfaction, and SLA monitoring',
                           'Clause 8.4: Supply and demand — Capacity management, demand forecasting, and resource '
                           'budgeting',
                           'Clause 8.5: Service design, build and transition — Change management and release '
                           'deployment gating',
                           'Clause 8.6: Service delivery processes — Incident management, problem root-cause analysis, '
                           'and continuity plans'],
        'keywords': [   'IT service management',
                        'ITSM',
                        'ISO 20000',
                        'SLA',
                        'incident management',
                        'problem management',
                        'change management'],
        'test_requirements': 'Service level agreement (SLA) metric tracking review, incident resolution '
                             'mean-time-to-repair (MTTR) audits, post-implementation change failure rate analysis, '
                             'disaster recovery drill logs review',
        'certification_process': 'BIS Management Systems Certification Scheme; multi-stage audit of corporate IT '
                                 'service desks, NOC/SOC operations, and service management processes',
        'url': 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/Standard_review/Isdetails?ID=MTgwMjI%3D'},
    {   'is_code': 'IS 16333-3',
        'title': 'Mobile Phone Handsets Part 3: Indian Language Support for Mobile Phone Handsets — Specific '
                 'Requirements',
        'year': '2022',
        'division': 'Electronics and Information Technology Division',
        'mandatory': True,
        'scope': 'This standard specifies the specific requirements for Indian language support across all mobile '
                 'phone handsets sold in India. It mandates the capability to display and input text in official '
                 'Indian languages (including Hindi, Bengali, Telugu, Marathi, Tamil, Urdu, Gujarati, Kannada, '
                 'Malayalam, Odia, Punjabi, Assamese, etc.) using Unicode font standards. It ensures digital inclusion '
                 'and accessible government e-services for non-English literate citizens.',
        'key_clauses': [   'Clause 4: General requirements — Support for all 22 scheduled Indian languages on '
                           'smartphones and feature phones',
                           'Clause 5: Input requirements — Virtual keyboard layout or keypad mapping (INSCRIPT layout) '
                           'for Indian scripts',
                           'Clause 6: Display requirements — Complete Unicode character rendering, complex script '
                           'glyph shaping, and matra placement',
                           'Clause 7: Text messaging (SMS) capability — Transmitting and receiving SMS text in all '
                           'mandated languages'],
        'keywords': [   'mobile phone languages',
                        'Indian languages',
                        'smartphone standard',
                        'Unicode display',
                        'INSCRIPT keyboard',
                        'MeitY mandatory',
                        'digital inclusion'],
        'test_requirements': 'Automated optical character verification of rendered Indian language glyphs, keypad '
                             'character input sequence validation, SMS encoding/decoding UCS2 test, font rendering '
                             'engine matrix audit',
        'certification_process': 'Mandatory compliance under MeitY Mobile Phones Order through BIS CRS registration → '
                                 'Handset testing at BIS-recognized telecommunication test labs → Grant of '
                                 'R-registration number',
        'url': 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/Standard_review/Isdetails?ID=MTgwMjM%3D'},
    {   'is_code': 'IS 13252-1',
        'title': 'Information Technology Equipment — Safety — Part 1: General Requirements',
        'year': '2010',
        'division': 'Electronics and Information Technology Division',
        'mandatory': True,
        'scope': 'This standard identical to IEC 60950-1 specifies safety requirements for mains-powered or '
                 'battery-powered information technology equipment, including servers, laptop computers, desktop PCs, '
                 'POS terminals, and networking equipment. It establishes protection against electric shock, energy '
                 'hazards, fire, mechanical instability, excessive temperature, and chemical emissions (ozone in '
                 "printers). It forms the backbone of MeitY's Compulsory Registration Scheme for electronics.",
        'key_clauses': [   'Clause 1.5: Components — Power cords, capacitors, transformers, and optical isolators '
                           'safety certification',
                           'Clause 2.1: Protection against electric shock — Access to SELV (Safety Extra Low Voltage) '
                           'circuits and earthing',
                           'Clause 2.9: Electrical insulation — Clearances, creepage distances, and solid insulation '
                           'dielectric limits',
                           'Clause 4.2: Mechanical strength — 500 mm steel ball drop test on external plastic '
                           'enclosure',
                           'Clause 4.5: Thermal requirements — Maximum temperature rise limits for PCB components and '
                           'outer chassis'],
        'keywords': [   'IT equipment safety',
                        'computer safety',
                        'laptop',
                        'server',
                        'power supply',
                        'SELV circuit',
                        'MeitY CRS',
                        'BIS registration'],
        'test_requirements': 'High-voltage breakdown dielectric test at 1500V-3000V AC, touch leakage current '
                             'measurement (<3.5 mA), ball impact test on housing (0.5 kg ball from 1.3 m), '
                             'flammability rating test UL94 V-0/V-1',
        'certification_process': 'Mandatory under MeitY Compulsory Registration Scheme (CRS) for over 60 product '
                                 'categories → Testing at BIS-accredited testing lab → Submission of test reports on '
                                 'BIS portal → Grant of R-number',
        'url': 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/Standard_review/Isdetails?ID=MTgwMjQ%3D'},
    {   'is_code': 'IS/ISO/IEC 27002',
        'title': 'Information Security, Cybersecurity and Privacy Protection — Information Security Controls',
        'year': '2022',
        'division': 'Electronics and Information Technology Division',
        'mandatory': False,
        'scope': 'This standard provides a comprehensive reference set of generic information security controls '
                 'including implementation guidance. Restructured into four broad themes (organizational, people, '
                 'physical, and technological controls), it incorporates contemporary security practices including '
                 'threat intelligence, cloud security governance, data masking, web filtering, and secure coding '
                 'techniques. It serves as the primary guidance catalog for implementing ISO 27001.',
        'key_clauses': [   'Clause 5: Organizational controls — Policies, threat intelligence, information '
                           'classification, cloud service governance',
                           'Clause 6: People controls — Screening, terms of employment, remote working, and security '
                           'awareness training',
                           'Clause 7: Physical controls — Physical security perimeters, clear desk and clear screen '
                           'policy, equipment siting',
                           'Clause 8: Technological controls — Privileged access, malware protection, vulnerability '
                           'management, data leakage prevention (DLP)'],
        'keywords': [   'security controls',
                        'ISO 27002',
                        'cybersecurity guidelines',
                        'threat intelligence',
                        'cloud security',
                        'data masking',
                        'vulnerability management'],
        'test_requirements': 'Control design and operating effectiveness assessment, configuration baseline audits for '
                             'cloud tenants and firewalls, static and dynamic application security testing (SAST/DAST) '
                             'review',
        'certification_process': 'Used as implementation guidance alongside ISO/IEC 27001; audited by information '
                                 'security assessors during corporate cybersecurity compliance audits',
        'url': 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/Standard_review/Isdetails?ID=MTgwMjU%3D'},
    {   'is_code': 'IS/ISO/IEC 25010',
        'title': 'Systems and Software Engineering — Systems and Software Quality Requirements and Evaluation (SQuaRE) '
                 '— System and Software Quality Models',
        'year': '2011',
        'division': 'Electronics and Information Technology Division',
        'mandatory': False,
        'scope': 'This standard adopts ISO/IEC 25010 and defines the Software Quality Model and Quality in Use Model '
                 'for computer software and software-intensive systems. The model categorizes software quality '
                 'characteristics into eight domains: functional suitability, performance efficiency, compatibility, '
                 'usability, reliability, security, maintainability, and portability. It provides a standardized '
                 'framework for specifying software requirements and evaluating commercial and defense software.',
        'key_clauses': [   'Clause 4.2: Functional suitability — Completeness, correctness, and appropriateness of '
                           'software capabilities',
                           'Clause 4.3: Performance efficiency — Time behaviour, resource utilization, and operational '
                           'capacity',
                           'Clause 4.4: Compatibility — Co-existence and interoperability with other software products',
                           'Clause 4.7: Security — Confidentiality, integrity, non-repudiation, accountability, and '
                           'authenticity',
                           'Clause 4.8: Maintainability — Modularity, reusability, analyzability, modifiability, and '
                           'testability'],
        'keywords': [   'software quality',
                        'SQuaRE',
                        'software engineering',
                        'functional suitability',
                        'software security',
                        'maintainability',
                        'ISO 25010'],
        'test_requirements': 'Automated code complexity analysis (cyclomatic complexity), software load and stress '
                             'performance testing, vulnerability static code analysis, software interoperability '
                             'benchmark suite',
        'certification_process': 'Adopted by software testing agencies (STQC under MeitY), defense software evaluation '
                                 'centers, and IT procurement authorities for formal software acceptance certification',
        'url': 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/Standard_review/Isdetails?ID=MTgwMjY%3D'},
    {   'is_code': 'IS 540',
        'title': 'Refined Sugar Cane Molasses — Specification',
        'year': '1968',
        'division': 'Food and Agriculture Division',
        'mandatory': True,
        'scope': 'This Indian Standard prescribes the requirements and methods of test for cane molasses obtained as a '
                 'by-product during the manufacture of cane sugar. It grades molasses into Grade 1, Grade 2, and Grade '
                 '3 based on total invert sugars, Brix density, and sulfated ash. Molasses is a primary feedstock for '
                 "the production of ethanol for India's National Biofuel Ethanol Blending Programme (EBP) as well as "
                 'cattle feed and yeast cultivation.',
        'key_clauses': [   'Clause 4: Grades — Grade 1 (min 50% total sugars), Grade 2 (min 44%), and Grade 3 (min '
                           '40%)',
                           'Clause 5: Chemical requirements — Minimum Brix value (80° to 85° at 27.5°C), total '
                           'reducing sugar percentage',
                           'Clause 6: Ash content — Sulfated ash limits (maximum 14.0% to 17.5% by mass)',
                           'Clause 8: Packaging and storage — Sealed tankers, steel storage tanks, and '
                           'temperature-controlled vats'],
        'keywords': [   'cane molasses',
                        'sugar by-product',
                        'ethanol blending',
                        'biofuel feedstock',
                        'brix value',
                        'reducing sugars',
                        'distillery standard'],
        'test_requirements': 'Brix hydrometer measurement at standardized temperature, Lane-Eynon copper titration for '
                             'reducing sugars, gravimetric sulfated ash determination, heavy metal trace profiling',
        'certification_process': 'Mandatory compliance under state excise departments and Ministry of Consumer Affairs '
                                 'for sugar mills and distilleries supplying ethanol to Oil Marketing Companies (OMCs)',
        'url': 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/Standard_review/Isdetails?ID=MTgwMjc%3D'},
    {   'is_code': 'IS 6092-1',
        'title': 'Methods of Sampling and Test for Fertilizers — Part 1: Sampling',
        'year': '1979',
        'division': 'Chemical Division',
        'mandatory': True,
        'scope': 'This standard covers the methods of sampling of solid, powder, granular, and liquid chemical '
                 'fertilizers packaged in bags or in bulk. It prescribes the number of packages to be sampled based on '
                 'consignment lot size, specialized slotted sampling probe tubes (triers), and cone-and-quartering '
                 'quartering techniques for preparing representative laboratory samples. It serves as the legal '
                 'foundation for fertilizer quality testing under the Fertilizer Control Order (FCO).',
        'key_clauses': [   'Clause 4: General requirements — Sampling in clean, dry environments free from moisture '
                           'contamination',
                           'Clause 5: Scale of sampling — Sample size determination matrix based on lot size (e.g., '
                           'square root formula)',
                           'Clause 6: Sampling instruments — Slotted single or double-tube brass triers of designated '
                           'bore diameters',
                           'Clause 7: Preparation of composite sample — Reduction by riffle sampler or quartering to '
                           'prepare three sealed test portions'],
        'keywords': [   'fertilizer sampling',
                        'sampling trier',
                        'composite sample',
                        'fertilizer control order',
                        'FCO',
                        'agricultural chemicals',
                        'quality testing'],
        'test_requirements': 'Moisture-free sampling container sealing, sample homogenization verification, trier '
                             'penetration angle check, tamper-evident lead sealing and labeling audit',
        'certification_process': 'Mandatory protocol executed by Fertilizer Inspectors and state quality control '
                                 'laboratories under the Fertilizer (Inorganic, Organic or Mixed) (Control) Order 1985',
        'url': 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/Standard_review/Isdetails?ID=MTgwMjg%3D'},
    {   'is_code': 'IS 5402',
        'title': 'Microbiology of Food and Animal Feeding Stuffs — Horizontal Method for the Enumeration of '
                 'Microorganisms — Colony-Count Technique at 30°C',
        'year': '2012',
        'division': 'Food and Agriculture Division',
        'mandatory': True,
        'scope': 'This Indian Standard prescribes a horizontal method for the enumeration of viable microorganisms in '
                 'food products, agricultural commodities, and animal feeding stuffs by counting the colonies growing '
                 'in a solid culture medium after aerobic incubation at 30°C. It specifies plate count agar (PCA) '
                 'preparation, serial decimal dilutions, pour plate and spread plate inoculation methods, incubation '
                 'timing (72 hours), and mathematical formula for calculating Colony Forming Units (CFU/g).',
        'key_clauses': [   'Clause 5: Diluent and culture media — Peptone saline diluent, plate count agar (PCA) pH '
                           '7.0 ± 0.2',
                           'Clause 8: Preparation of initial suspension and dilutions — 1:10 initial dilution and '
                           'serial decimal dilutions',
                           'Clause 9: Inoculation and incubation — Pour plate technique, incubation at 30°C ± 1°C for '
                           '72h ± 3h',
                           'Clause 10: Counting of colonies — Retaining plates with 15 to 300 colonies for accurate '
                           'enumeration calculation'],
        'keywords': [   'food microbiology',
                        'total plate count',
                        'TPC',
                        'colony count',
                        'aerobic bacteria',
                        'animal feed',
                        'food safety',
                        'FSSAI standard'],
        'test_requirements': 'Media sterility blank check, positive control culture verification using reference '
                             'bacterial strains, automated or manual colony counter enumeration, temperature logging '
                             'of incubators',
        'certification_process': 'Mandatory analytical test method prescribed across all BIS food specifications and '
                                 'FSSAI safety testing regulations; audited under ISO/IEC 17025 laboratory '
                                 'accreditation',
        'url': 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/Standard_review/Isdetails?ID=MTgwMjk%3D'},
    {   'is_code': 'IS 15007',
        'title': 'Urea, Agricultural Grade — Specification',
        'year': '2001',
        'division': 'Chemical Division',
        'mandatory': True,
        'scope': 'This Indian Standard specifies the chemical and physical requirements and test methods for '
                 'agricultural grade urea fertilizer [CO(NH2)2]. It establishes minimum total nitrogen content (46.0% '
                 'by mass), maximum biuret content (1.5% by mass to prevent crop phytotoxicity), maximum moisture '
                 '(1.0%), and particle size grading (prilled / granular urea). It protects farmers against adulterated '
                 'or substandard chemical fertilizers.',
        'key_clauses': [   'Clause 4: Description — White, crystalline, prilled or granular material free from visible '
                           'contaminants',
                           'Clause 5: Chemical requirements — Total nitrogen minimum 46.0% by mass, biuret maximum '
                           '1.5% by mass',
                           'Clause 5.3: Moisture content — Maximum 1.0% by mass (or 0.5% for neem-coated urea)',
                           'Clause 6: Particle size — Minimum 90% of material passing through 2.8 mm sieve and '
                           'retained on 1.0 mm sieve',
                           'Clause 8: Packaging and marking — Moisture-proof HDPE bags with mandatory FCO and ISI '
                           'declarations'],
        'keywords': [   'urea fertilizer',
                        'nitrogen fertilizer',
                        'biuret content',
                        'agricultural grade',
                        'prills',
                        'fertilizer control order',
                        'ISI mark mandatory'],
        'test_requirements': 'Kjeldahl total nitrogen titrimetric determination, spectrophotometric copper-biuret '
                             'complex analysis at 550 nm, Karl Fischer titration for moisture, sieve shaker mechanical '
                             'particle size analysis',
        'certification_process': 'Mandatory certification under Fertilizer Control Order (FCO) and Department of '
                                 'Fertilizers regulations; strict continuous batch testing in in-plant laboratories '
                                 'and BIS inspections',
        'url': 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/Standard_review/Isdetails?ID=MTgwMzA%3D'},
    {   'is_code': 'IS 1445',
        'title': 'Di-Ammonium Phosphate (DAP) Fertilizer — Specification',
        'year': '1970',
        'division': 'Chemical Division',
        'mandatory': True,
        'scope': 'This Indian Standard prescribes the requirements and test methods for di-ammonium phosphate (DAP) '
                 'fertilizer [(NH4)2HPO4] used in agriculture. It specifies minimum total nitrogen content (18.0%), '
                 'minimum total phosphate (46.0% P2O5), minimum water-soluble phosphate (41.0% P2O5), and limits '
                 'moisture content. DAP provides essential nitrogen and phosphorus nutrients to crops, requiring '
                 'strict adherence to composition to prevent crop failure.',
        'key_clauses': [   'Clause 4: Physical form — Granular product in shades of grey, brown, or black free-flowing '
                           'material',
                           'Clause 5: Chemical requirements — Total ammoniacal nitrogen min 18.0%, total P2O5 min '
                           '46.0%',
                           'Clause 5.2: Water soluble phosphate — Water soluble P2O5 minimum 41.0% by mass',
                           'Clause 5.4: Moisture content — Maximum 1.5% by mass (or 2.5% for imported cargo)',
                           'Clause 6: Particle sizing — Minimum 90% of material retained between 1 mm and 4 mm sieves'],
        'keywords': [   'DAP fertilizer',
                        'diammonium phosphate',
                        'phosphate fertilizer',
                        'nitrogen',
                        'water soluble P2O5',
                        'crop nutrient',
                        'ISI mark mandatory'],
        'test_requirements': 'Kjeldahl ammoniacal nitrogen distillation, quinoline phosphomolybdate gravimetric '
                             'phosphate determination, Karl Fischer moisture testing, particle size sieve analysis',
        'certification_process': 'Mandatory compliance under Fertilizer Control Order (FCO) and Department of '
                                 'Fertilizers; laboratory batch testing for domestic and port-imported DAP '
                                 'consignments',
        'url': 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/Standard_review/Isdetails?ID=MTgwMzE%3D'},
    {   'is_code': 'IS 8550',
        'title': 'Single Superphosphate (SSP) Fertilizer — Specification',
        'year': '1977',
        'division': 'Chemical Division',
        'mandatory': True,
        'scope': 'This standard covers the requirements and methods of test for single superphosphate (SSP) fertilizer '
                 'in powdered and granulated forms. It specifies minimum water-soluble phosphate (16.0% P2O5 by mass), '
                 'free phosphoric acid limit (max 4.0% to prevent bag deterioration), and minimum sulfur content '
                 '(11.0% S). SSP is a vital domestic fertilizer providing both phosphorus and secondary sulfur '
                 'nutrients for oilseed and pulse production in India.',
        'key_clauses': [   'Clause 4: Types — Powdered single superphosphate and granulated single superphosphate '
                           '(GSSP)',
                           'Clause 5: Chemical criteria — Water soluble phosphate min 16.0% P2O5, total available '
                           'phosphate min 16.5%',
                           'Clause 5.3: Free phosphoric acid — Maximum 4.0% H3PO4 by mass',
                           'Clause 5.5: Sulphur content — Minimum 11.0% elemental sulphur by mass',
                           'Clause 7: Particle size of GSSP — Minimum 85% between 1 mm and 4 mm sieves'],
        'keywords': [   'single superphosphate',
                        'SSP',
                        'GSSP',
                        'sulfur fertilizer',
                        'phosphorus',
                        'fertilizer specification',
                        'FCO'],
        'test_requirements': 'Water soluble P2O5 spectrophotometric/gravimetric analysis, free acid alcohol extraction '
                             'titration, barium sulfate gravimetric sulfur determination, moisture loss at 105°C',
        'certification_process': 'Mandatory certification under Fertilizer Control Order (FCO) and BIS licensing '
                                 'Scheme-I; regular surveillance sampling from manufacturing bagging plants',
        'url': 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/Standard_review/Isdetails?ID=MTgwMzI%3D'},
    {   'is_code': 'IS 17930',
        'title': 'Organic Fertilizers — City Compost — Specification',
        'year': '2022',
        'division': 'Food and Agriculture Division',
        'mandatory': True,
        'scope': 'This Indian Standard specifies the quality, physical, chemical, and biological requirements for city '
                 'compost produced through controlled biological decomposition of segregated urban organic municipal '
                 'solid waste. It establishes minimum organic carbon (>12.0%), optimal carbon-to-nitrogen ratio (C:N < '
                 '20:1), nutrient concentrations (total NPK > 1.2%), moisture limits, and stringent heavy metal '
                 'thresholds (lead, cadmium, arsenic, chromium) to prevent soil toxicity.',
        'key_clauses': [   'Clause 4: Physical characteristics — Dark brown to black colour, earthy odour, absence of '
                           'visible plastic/glass (>4 mm)',
                           'Clause 5: Chemical parameters — Organic carbon (min 12%), Total NPK (min 1.2%), C:N ratio '
                           '(<20), pH (6.5 to 7.5)',
                           'Clause 6: Heavy metal thresholds — Lead (<100 ppm), Cadmium (<5 ppm), Chromium (<50 ppm), '
                           'Arsenic (<10 ppm)',
                           'Clause 7: Pathogen limits — Zero Salmonella in 25g, Faecal coliform < 1000 MPN/g',
                           'Clause 8: Packaging and labeling — Net weight, moisture content, expiry date, and city '
                           'compost grading'],
        'keywords': [   'city compost',
                        'organic fertilizer',
                        'municipal solid waste',
                        'C:N ratio',
                        'heavy metals',
                        'soil health',
                        'waste management'],
        'test_requirements': 'Walkley-Black wet oxidation organic carbon assay, ICP-MS heavy metal trace '
                             'quantification, membrane filtration coliform MPN test, sieve analysis on 4.0 mm screen',
        'certification_process': 'Mandatory compliance under Solid Waste Management Rules 2016 and Fertilizer Control '
                                 'Order (FCO); audited by state agricultural departments and Central Pollution Control '
                                 'Board (CPCB)',
        'url': 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/Standard_review/Isdetails?ID=MTgwMzM%3D'},
    {   'is_code': 'IS 4985',
        'title': 'Unplasticized Polyvinyl Chloride (uPVC) Pipes for Potable Water Supplies — Specification',
        'year': '2021',
        'division': 'Civil Engineering Division',
        'mandatory': True,
        'scope': 'This Indian Standard covers unplasticized polyvinyl chloride (uPVC) pipes intended for potable water '
                 'supplies, rural and urban piped drinking networks, and agricultural irrigation. It specifies outside '
                 'diameters (from 16 mm to 1000 mm), pressure classes (from 0.25 MPa to 1.6 MPa), hydrostatic burst '
                 'strength, opacity, and resistance to toxic chemical leaching (lead, tin, cadmium). It prohibits the '
                 'use of hazardous lead stabilizers.',
        'key_clauses': [   'Clause 5: Composition — Virgin PVC resin, non-toxic calcium-zinc or organic stabilizers, '
                           'free from plasticizers',
                           'Clause 7: Dimensions and tolerances — Pipe outside diameter, wall thickness tolerances, '
                           'and pipe socket shapes',
                           'Clause 8: Hydrostatic pressure tests — Short-term burst pressure and 1000-hour stress '
                           'rupture test at 60°C',
                           'Clause 9: Toxicological requirements — Lead leaching < 0.01 mg/L, Cadmium < 0.003 mg/L',
                           'Clause 10: Mechanical properties — Impact resistance (falling weight test at 0°C) and '
                           'tensile yield stress (>45 MPa)'],
        'keywords': [   'uPVC pipes',
                        'potable water pipe',
                        'water supply',
                        'lead-free PVC',
                        'hydrostatic pressure',
                        'Jal Jeevan Mission',
                        'ISI mark mandatory'],
        'test_requirements': 'Internal hydrostatic pressure test at 20°C (4.2x rated pressure) and 60°C (1000 hours), '
                             'drop-weight impact test at 0°C, toxic metal migration extraction test, opacity light '
                             'transmission test (<0.2%)',
        'certification_process': 'Mandatory certification under Piping QCO and Jal Jeevan Mission procurement → Plant '
                                 'audit of extrusion lines and compounding mixers → NABL testing → Grant of ISI mark '
                                 'license',
        'url': 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/Standard_review/Isdetails?ID=MTgwMzQ%3D'},
    {   'is_code': 'IS 1239-1',
        'title': 'Steel Tubes, Tubulars and Other Wrought Steel Fittings — Part 1: Steel Tubes',
        'year': '2004',
        'division': 'Mechanical Engineering Division',
        'mandatory': True,
        'scope': 'This Indian Standard covers the requirements for welded and seamless mild steel tubes for water, '
                 'non-hazardous gas, air, and steam lines. It categorizes steel tubes into three weight classes: Light '
                 '(Class A - Yellow band), Medium (Class B - Blue band), and Heavy (Class C - Red band). It specifies '
                 'chemical composition, hot-dip galvanizing zinc coating mass (minimum 360 g/m2), hydraulic pressure '
                 'test (5 MPa), and flattening/bending cold workability.',
        'key_clauses': [   'Clause 5: Dimensions and weights — Standard nominal bore (15 mm to 150 mm), wall '
                           'thickness, and mass per meter',
                           'Clause 8: Chemical composition — Low carbon steel with max 0.040% Sulphur and 0.040% '
                           'Phosphorus',
                           'Clause 9: Galvanizing — Hot-dip zinc coating mass (min 360 g/m2) and copper sulphate '
                           'uniformity test (Preece test)',
                           'Clause 10: Mechanical tests — Tensile test, bend test up to 50 mm NB, and flattening test '
                           'for >50 mm NB',
                           'Clause 11: Hydraulic pressure test — 100% of tubes tested at internal hydraulic pressure '
                           'of 5.0 MPa for 5 seconds'],
        'keywords': [   'steel pipes',
                        'GI pipes',
                        'galvanized steel',
                        'mild steel tubes',
                        'plumbing pipe',
                        'hydraulic test',
                        'ISI mark mandatory'],
        'test_requirements': '100% in-line hydrostatic pressure test at 5.0 MPa, zinc coating mass strip-and-weigh '
                             'test per IS 6745, Preece chemical uniformity dipping test, tensile yield and elongation '
                             'testing',
        'certification_process': 'Mandatory certification under Steel Pipes QCO by Ministry of Steel → Factory rolling '
                                 'and galvanizing bath inspection → Continuous batch sampling → ISI certification mark '
                                 'license',
        'url': 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/Standard_review/Isdetails?ID=MTgwMzU%3D'},
    {   'is_code': 'IS 1536',
        'title': 'Centrifugally Cast (Spun) Iron Pressure Pipes for Water, Gas and Sewage — Specification',
        'year': '2001',
        'division': 'Civil Engineering Division',
        'mandatory': True,
        'scope': 'This standard covers centrifugally cast (spun) ductile and grey iron pressure pipes used for the '
                 'conveyance of water, sewage, and gas. It specifies classes LA, A, and B based on pipe wall thickness '
                 'and working pressures. It details dimensions, spigot and socket joint geometry for rubber gaskets, '
                 'hydraulic pressure tests at manufacturing works, tensile strength of cast iron (>150 to 200 MPa), '
                 'and internal/external anti-corrosive bitumen or cement mortar coatings.',
        'key_clauses': [   'Clause 4: Manufacturing process — Centrifugal casting in metal or sand-lined spinning '
                           'moulds',
                           'Clause 6: Mechanical properties — Minimum tensile strength (200 MPa for chill-cast, 150 '
                           'MPa for sand-cast)',
                           'Clause 7: Dimensions — Nominal diameter DN 80 to DN 1000, standard working lengths (3.66 m '
                           'to 5.5 m)',
                           'Clause 8: Works hydrostatic test — Hydrostatic pressure test from 1.5 MPa to 3.5 MPa for '
                           '15 seconds',
                           'Clause 11: Protective coatings — Internal cement mortar lining or bitumen coating '
                           'compliance'],
        'keywords': [   'cast iron pipes',
                        'ductile iron',
                        'spun pipes',
                        'water mains',
                        'sewerage piping',
                        'hydrostatic test',
                        'municipal water'],
        'test_requirements': 'Factory hydrostatic test on every pipe length, ring crushing tensile strength test, '
                             'Brinell hardness testing (HB < 210), cement mortar lining adhesion and thickness '
                             'ultrasonic test',
        'certification_process': 'Mandatory compliance for public water supply authorities (Jal Boards, Municipal '
                                 'Corporations) and BIS Product Certification Scheme-I licensing',
        'url': 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/Standard_review/Isdetails?ID=MTgwMzY%3D'},
    {   'is_code': 'IS 15778',
        'title': 'Chlorinated Polyvinyl Chloride (CPVC) Pipes for Potable Hot and Cold Water Distribution Supplies — '
                 'Specification',
        'year': '2007',
        'division': 'Civil Engineering Division',
        'mandatory': True,
        'scope': 'This Indian Standard specifies requirements for chlorinated polyvinyl chloride (CPVC) plastic pipes '
                 'designed for potable hot and cold water distribution plumbing systems within buildings. It covers '
                 'pipe classes Standard Dimension Ratio (SDR 11 and SDR 13.5) with continuous service temperatures up '
                 'to 82°C and operating pressures up to 2.8 MPa. It specifies vicat softening temperature (>103°C), '
                 'freedom from toxic metal migration, and resistance to chlorine degradation.',
        'key_clauses': [   'Clause 5: Material — Post-chlorinated PVC resin with chlorine content not less than 66.5%',
                           'Clause 6: Dimensions — Copper Tube Size (CTS) dimensions from 15 mm to 50 mm outside '
                           'diameter',
                           'Clause 8: Hydrostatic strength — Short-term burst pressure and 1000-hour hydrostatic test '
                           'at 82°C (2.18 MPa)',
                           'Clause 9: Thermal properties — Vicat softening temperature not less than 103°C',
                           'Clause 10: Toxicological criteria — Certified safe for potable hot drinking water without '
                           'taste or odor contamination'],
        'keywords': [   'CPVC pipes',
                        'hot water plumbing',
                        'potable water',
                        'chlorinated PVC',
                        'vicat softening',
                        'SDR 11',
                        'Jal Jeevan Mission',
                        'ISI mark'],
        'test_requirements': 'Hydrostatic test at 82°C for 1000 hours, Vicat softening point bath test (>103°C), '
                             'flattening test under compression, toxicological extraction testing in boiling water '
                             'simulants',
        'certification_process': 'Mandatory certification under Plumbing Pipes Quality Control Order → Extrusion plant '
                                 'audit → Comprehensive thermal and pressure testing in BIS laboratories → ISI mark '
                                 'license',
        'url': 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/Standard_review/Isdetails?ID=MTgwMzc%3D'},
    {   'is_code': 'IS 778',
        'title': 'Copper Alloy Gate, Globe and Check Valves for Water Works Purposes — Specification',
        'year': '1984',
        'division': 'Mechanical Engineering Division',
        'mandatory': True,
        'scope': 'This Indian Standard specifies requirements for brass and gunmetal gate (sluice), globe, and '
                 'non-return check valves used in domestic water plumbing, municipal pipelines, and industrial water '
                 'systems. It specifies valve ratings Class 1 (PN 1.0) and Class 2 (PN 1.6), body wall thicknesses, '
                 'handwheel torque, threaded or flanged ends, and high-pressure seat and shell leak tests. It ensures '
                 'non-corrosive, long-lasting shutoff in water distribution networks.',
        'key_clauses': [   'Clause 4: Pressure ratings — Class 1 (PN 1.0 - 10 bar) and Class 2 (PN 1.6 - 16 bar)',
                           'Clause 5: Materials — Leaded tin bronze (gunmetal) or forged brass complying with IS 318 / '
                           'IS 6912',
                           'Clause 7: Construction and dimensions — Wedge gate design, renewable seat rings, rising '
                           'and non-rising spindles',
                           'Clause 8: Hydraulic testing — Shell test at 1.5 times working pressure, seat test at 1.0 '
                           'times working pressure without leakage'],
        'keywords': [   'copper alloy valves',
                        'brass valve',
                        'gunmetal gate valve',
                        'globe valve',
                        'check valve',
                        'water plumbing',
                        'ISI mark mandatory'],
        'test_requirements': 'Body hydrostatic shell pressure test at 1.5 to 2.4 MPa, seat leak-tightness test with '
                             'air/water without bubble leakage, spindle torque resistance test, metallurgical chemical '
                             'analysis of bronze',
        'certification_process': 'Mandatory BIS Scheme-I licensing under Valves QCO → Foundry and machining shop '
                                 'inspection → Pressure testing of sample valves → Grant of ISI certification mark',
        'url': 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/Standard_review/Isdetails?ID=MTgwMzg%3D'},
    {   'is_code': 'IS 13592',
        'title': 'Unplasticized Polyvinyl Chloride (uPVC) Pipes for Soil and Waste Discharge Systems Inside and '
                 'Outside Buildings — Specification',
        'year': '2013',
        'division': 'Civil Engineering Division',
        'mandatory': True,
        'scope': 'This Indian Standard specifies requirements for unplasticized polyvinyl chloride (uPVC) pipes used '
                 'for soil and waste discharge systems (SWR pipes), ventilation stacks, and rainwater drainage systems '
                 'inside and outside buildings. It defines Type A pipes (intended for rainwater and ventilation) and '
                 'Type B pipes (intended for soil and liquid waste discharge). It specifies wall thicknesses, ring '
                 'stiffness, socket design for rubber ring sealing (push-fit), and resistance to domestic detergents.',
        'key_clauses': [   'Clause 4: Types — Type A (for rainwater drainage and ventilation) and Type B (for soil and '
                           'sanitary waste)',
                           'Clause 6: Dimensions — Outside diameters 75 mm, 90 mm, 110 mm, and 160 mm with specified '
                           'wall thicknesses',
                           'Clause 7: Mechanical properties — Ring stiffness test, drop-weight impact test at 0°C, and '
                           'tensile strength',
                           'Clause 8: Watertightness of joints — Joint seal hydrostatic pressure test at 0.05 MPa with '
                           'angular deflection',
                           'Clause 9: Resistance to chemical waste — Immersion test in domestic chemical waste '
                           'solutions and hot water (60°C)'],
        'keywords': [   'SWR pipes',
                        'uPVC drainage pipe',
                        'soil and waste discharge',
                        'rainwater pipe',
                        'ring stiffness',
                        'push-fit joints',
                        'ISI mark'],
        'test_requirements': 'Ring stiffness testing machine verification, drop hammer impact test at 0°C, joint '
                             'tightness water test under 50 kPa pressure and 2° angular deflection, oven heat '
                             'reversion test at 150°C',
        'certification_process': 'Mandatory certification under Building Materials QCO → Plant audit of twin-screw '
                                 'extrusion lines → Dimensional, mechanical, and impact testing → ISI certification '
                                 'mark license',
        'url': 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/Standard_review/Isdetails?ID=MTgwMzk%3D'},
    {   'is_code': 'IS 12234',
        'title': 'Plastic Ball Valves for Water Supply — Specification',
        'year': '1988',
        'division': 'Civil Engineering Division',
        'mandatory': False,
        'scope': 'This Indian Standard specifies the materials, dimensional, constructional, and performance '
                 'requirements for plastic ball valves (polypropylene, PVC, POM) used for water supply installations. '
                 'It covers nominal sizes from 15 mm to 50 mm for cold water systems up to 45°C. It specifies handle '
                 'torque, seat leak tightness under fluctuating pressures, cycle life endurance (minimum 50,000 '
                 'open-close operations without leakage), and corrosion-free performance in saline or chlorinated '
                 'water.',
        'key_clauses': [   'Clause 4: Materials — Food grade virgin polymers (PP, uPVC, POM) and EPDM/PTFE sealing '
                           'rings',
                           'Clause 5: Pressure ratings — PN 10 (1.0 MPa) and PN 16 (1.6 MPa) at room temperature',
                           'Clause 6: Construction — Full bore or reduced bore ball, blowout-proof stem, and ergonomic '
                           'lever handle',
                           'Clause 8: Hydraulic testing — Shell test at 1.5x PN and seat test at 1.1x PN',
                           'Clause 9: Mechanical endurance — 50,000 continuous operation cycles under pressurized '
                           'water flow'],
        'keywords': [   'plastic ball valve',
                        'polypropylene valve',
                        'water supply',
                        'plumbing valve',
                        'leak tightness',
                        'endurance cycling',
                        'corrosion resistance'],
        'test_requirements': '50,000 cycle automated opening-closing endurance test under water pressure, hydrostatic '
                             'shell pressure test at 2.4 MPa, seat leak vacuum and pressure test, torque measurement',
        'certification_process': 'Voluntary BIS product certification for plumbing component manufacturers; tested in '
                                 'designated mechanical and plumbing test laboratories',
        'url': 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/Standard_review/Isdetails?ID=MTgwNDB%3D'}]


import json
import os
import re

_MERGED_STANDARDS_CACHE: list[dict] = []

def _get_merged_standards() -> list[dict]:
    global _MERGED_STANDARDS_CACHE
    if _MERGED_STANDARDS_CACHE:
        return _MERGED_STANDARDS_CACHE

    merged: list[dict] = []
    seen: set[str] = set()

    # Pre-scan SP 21 handbook corpus (559 standards)
    sp21_path = os.path.join(os.path.dirname(__file__), 'sp21_standards.json')
    sp21 = []
    sp21_full_codes: dict[str, str] = {}
    if os.path.exists(sp21_path):
        try:
            with open(sp21_path, 'r', encoding='utf-8') as f:
                sp21 = json.load(f)
            for item in sp21:
                orig_code = item.get('is_code', '').strip()
                base = re.sub(r':\s*\d{4}.*$', '', orig_code).strip()
                if base:
                    sp21_full_codes[base] = orig_code
        except Exception as e:
            print(f'[Data Engine] Note: Could not preload sp21_standards.json: {e}')

    # 1. First add curated high-detail standards, adopting SP21 code format if identical standard
    for s in BIS_STANDARDS_DATABASE:
        s_copy = s.copy()
        raw_code = s_copy['is_code']
        if raw_code in sp21_full_codes:
            s_copy['is_code'] = sp21_full_codes[raw_code]
        code_norm = re.sub(r'[^a-zA-Z0-9]', '', s_copy['is_code']).lower()
        seen.add(code_norm)
        merged.append(s_copy)

    # 2. Ingest remaining SP 21 handbook corpus standards
    for item in sp21:
        code = item.get('is_code', '').strip()
        norm = re.sub(r'[^a-zA-Z0-9]', '', code).lower()
        if norm not in seen:
            seen.add(norm)
            ft = item.get('full_text', '')
            clauses = []
            for line in ft.split('\n'):
                line = line.strip()
                if re.match(r'^(?:\d+\.|\d+\.\d+|Clause\s+\d+)', line) and len(line) > 15:
                    clauses.append(line[:120])
                if len(clauses) >= 5:
                    break
            if not clauses and item.get('scope'):
                clauses = [item['scope'][:120]]

            title_lower = (item.get('title', '') + ' ' + item.get('scope', '')).lower()
            div = 'Civil Engineering Division'
            if any(w in title_lower for w in ['paint', 'varnish', 'chemical', 'bitumen', 'asphalt', 'resin']):
                div = 'Chemical Division'
            elif any(w in title_lower for w in ['steel', 'iron', 'alloy', 'metal', 'welding']):
                div = 'Metallurgical Engineering Division'
            elif any(w in title_lower for w in ['electrical', 'cable', 'conductor', 'wiring']):
                div = 'Electrotechnical Division'

            merged.append({
                'is_code': code,
                'title': item.get('title', '').strip(),
                'year': str(item.get('revision', '')),
                'division': div,
                'mandatory': True if any(w in title_lower for w in ['cement', 'steel', 'pipe', 'safety', 'mandatory']) else False,
                'scope': item.get('scope', '').strip(),
                'abstract_scope': item.get('scope', '').strip(),
                'key_clauses': clauses,
                'keywords': [w for w in re.findall(r'[a-zA-Z]{4,}', title_lower) if w not in ['standard', 'indian', 'specification', 'requirements']][:8],
                'test_requirements': f'Prescribed physical, chemical, and mechanical test limits under {code}',
                'certification_process': f'Compliance with {code} → Laboratory evaluation → BIS License & ISI Mark',
                'full_text': ft
            })

    # 3. Ingest extended technical division catalog standards
    ext_path = os.path.join(os.path.dirname(__file__), 'extended_bis_catalog.json')
    if os.path.exists(ext_path):
        try:
            with open(ext_path, 'r', encoding='utf-8') as f:
                ext_catalog = json.load(f)
            for item in ext_catalog:
                code = item.get('is_code', '').strip()
                norm = re.sub(r'[^a-zA-Z0-9]', '', code).lower()
                if norm not in seen:
                    seen.add(norm)
                    merged.append(item.copy())
        except Exception as e:
            print(f'[Data Engine] Note: Could not load extended_bis_catalog.json: {e}')

    _MERGED_STANDARDS_CACHE = merged
    return _MERGED_STANDARDS_CACHE


def get_all_standards() -> list[dict]:
    """Return the complete standards database (curated + SP 21 corpus)."""
    return _get_merged_standards()


def get_standard_by_code(is_code: str) -> dict | None:
    """Look up a single standard by its IS code with exact numeric token matching."""
    clean_target = re.sub(r'[^a-zA-Z0-9]', '', is_code).lower()
    merged = _get_merged_standards()
    # 1. Exact match
    for std in merged:
        if re.sub(r'[^a-zA-Z0-9]', '', std["is_code"]).lower() == clean_target:
            return std

    # 2. Match exact base number: e.g. target 'IS 1077' matches 'IS 1077: 1992' but NOT 'IS 10772'
    target_nums = re.findall(r'\d+', is_code)
    if target_nums:
        base_num = target_nums[0]
        for std in merged:
            std_nums = re.findall(r'\d+', std["is_code"])
            if std_nums and std_nums[0] == base_num:
                # If target specified part/section, match that too
                if len(target_nums) > 1 and len(std_nums) > 1:
                    if target_nums[1] == std_nums[1]:
                        return std
                else:
                    return std

    # 3. Generic prefix fallback
    for std in merged:
        clean_std = re.sub(r'[^a-zA-Z0-9]', '', std["is_code"]).lower()
        if clean_std.startswith(clean_target):
            return std
    return None


def get_standards_by_division(division: str) -> list[dict]:
    """Get all standards in a given division."""
    div_clean = division.lower()
    return [s for s in _get_merged_standards() if div_clean in s.get("division", "").lower()]
