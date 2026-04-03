---
name: healthymind-reference-data
description: Comprehensive reference data for HealthyMind/Taliaz clinic operations. Contains clinic IDs, meeting type IDs, pricing tables (income per meeting), therapist payment rates, and meeting length configurations. Use when calculating income, payments, or looking up IDs for clinics/meeting types. Essential for monthly reports, financial analysis, and data queries.
---

# HealthyMind Reference Data

## Clinic IDs

| clinic_id | clinic_name | id_prefix | funding_entity |
|-----------|-------------|-----------|----------------|
| 3 | Maccabi | HM-MCB | Maccabi |
| 5 | Merkaz Hosen | HM-MHS | Taliaz |
| 8 | Amutot IDF | HM-IDF | Taliaz |
| 10 | Hosen Youth | HM-MHY | Taliaz |
| 12 | Mashaabim | HM-MHN | Taliaz |
| 14 | Hosen Bedouin | HM-MHB | Taliaz |
| 15 | Mashaabim Youth | HM-MSY | Taliaz |
| 16 | Kav LaNoar | HM-MKV | Taliaz |
| 18 | Shapach | HM-SPC | Taliaz |
| 19 | OMG (UK) | HM-UKA | Patient |
| 20 | Taliaz clinic | HM-PRV | Patient |
| 22 | Maccabi Youth | HM-MCY | Maccabi |
| 23 | Welfare | HM-WFR | Taliaz |
| 24 | Urgent Consultant | HM-URC | N/A |
| 25 | Welfare Youth | HM-WFY | Taliaz |
| 26 | Taliaz Youth | HM-PRY | Patient |
| 27 | Clalit | HM-CLT | Clalit |

## Meeting Type IDs

| meeting_type_id | name | user_type | is_intake |
|-----------------|------|-----------|-----------|
| 1 | Case manager Intake | case_manager | true |
| 2 | Psychiatrist Intake | doctor | true |
| 3 | Psychiatrist FollowUp | doctor | false |
| 4 | Case manager FollowUp | case_manager | false |
| 5 | Psychiatrist FollowUp 30 min | doctor | false |

## Meeting Length (Single Source of Truth)

Length varies by: therapist x patient_type x meeting_type.
Source: therapist_fees.csv columns: intake_adult_min, followup_adult_min, intake_youth_min, followup_youth_min

Typical ranges: Case Manager Adult (Intake=30, FollowUp=10), Psychiatrist Adult (Intake=20-30, FollowUp=10-15), Psychiatrist Youth (Intake=40-45, FollowUp=25-30)

## Income Pricing (ILS per meeting)

Maccabi Adult: CM Intake=220, CM FollowUp=185, Doctor Intake=670, Doctor FollowUp=155
Maccabi Youth/Kids: CM Intake=275, CM FollowUp=185, Doctor Intake=825, Doctor FollowUp=250
Clalit Adult: CM Intake=220, Doctor Intake=570
Taliaz Funding Adult (Amutot IDF/Mashaabim/Welfare/Merkaz Hosen): CM Intake=250, CM FollowUp=120, Doctor Intake=750, Doctor FollowUp=355
Taliaz Funding Youth (Hosen Youth/Mashaabim Youth/Shapach/Welfare Youth): CM Intake=500, CM FollowUp=255, Doctor Intake=1500, Doctor FollowUp=765
Taliaz Private (Payed-Intake/Payed-FollowUp/Taliaz clinic): CM Intake=280, CM FollowUp=100, Doctor Intake=840, Doctor FollowUp=290
Taliaz Private Youth: CM Intake=500, CM FollowUp=255, Doctor Intake=1500, Doctor FollowUp=765
Urgent Consultant: Doctor Intake only = 800 ILS

## Therapist Payment Structure (from therapist_fees.csv)
- worked_hour: Payment per hour of completed meetings
- noshow_hour: Payment per hour of no-show meetings
- unscheduled_hour: Payment for available but unscheduled time
- nonclinical_hour: Payment for admin/non-clinical work

## Data Integrity Rules
1. Meeting length: ONLY from therapist_fees.csv — never hardcode
2. Patient type: normalize Youth and Kids to Youth/Kids for pricing
3. Therapist lookup: always by user_id (not name) to avoid encoding issues
4. Use business_sub_unit (not just business_unit) for pricing accuracy

## Historical Notes
- July 2025: Maccabi Adult CM FollowUp increased from 81.9 to 185 ILS
- Youth/Kids pricing is 25-35% higher than Adult across Maccabi programs
