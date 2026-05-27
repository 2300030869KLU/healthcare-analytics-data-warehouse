# Healthcare Analytics Data Warehouse using MySQL

## Project Overview

This project extends the existing NexusWave Health Monitoring System into a complete Healthcare Analytics Data Warehouse using MySQL, ETL pipelines, Medallion Architecture, and OLAP analytics concepts.

The system transforms operational healthcare monitoring data into analytical healthcare insights for population-level healthcare analysis, risk monitoring, and healthcare reporting.

The warehouse follows a Medallion Architecture approach using:

- Bronze Layer (Raw Healthcare Ingestion)
- Silver Layer (Cleaned & Integrated Healthcare Snapshots)
- Gold Layer (Healthcare Star Schema Warehouse)

---

# Project Objective

The main objective of this project is to transform transactional healthcare monitoring data into meaningful analytical healthcare insights using modern Data Warehouse engineering concepts.

The warehouse supports:

- Age-wise healthcare analytics
- City-wise healthcare analysis
- Seasonal healthcare trends
- Population health reporting
- Risk distribution analytics
- High-risk patient identification
- Regional healthcare comparison
- OLAP healthcare reporting

---

# Existing OLTP System

The existing NexusWave Health Monitoring System acts as the OLTP (Online Transaction Processing) layer.

Users submit healthcare vitals including:

- Heart Rate
- SpO₂
- Temperature
- Blood Pressure
- Glucose Levels

The system validates healthcare parameters and generates:

```text
ALERT
NORMAL
```

This operational healthcare system acts as the source system for the warehouse.

---

# Complete Warehouse Architecture

```text
Synthetic Healthcare Data Generation
                ↓
Bronze Layer
(raw healthcare ingestion)
                ↓
Silver Layer
(clean integrated healthcare snapshots)
                ↓
Gold Layer
(star schema warehouse)
                ↓
OLAP Healthcare Analytics
                ↓
Healthcare Insights & Reporting
```

---

# Database Architecture

```text
OLTP Database
healthapi

Bronze Layer Database
bronze_healthcare

Silver Layer Database
silver_healthcare

Gold Layer Database
nexuswave_warehouse
```

---

# Medallion Architecture

## Bronze Layer

Purpose:

- Raw healthcare ingestion
- Preserve source healthcare records
- Minimal transformation
- Historical raw data preservation

### Bronze Tables

```text
bronze_users
bronze_heart_rate
bronze_bp
bronze_glucose
bronze_oxygen
bronze_temperature
```

---

## Silver Layer

Purpose:

- Healthcare data cleaning
- Timestamp standardization
- Healthcare integration
- Daily healthcare aggregation
- Risk categorization
- Dense healthcare snapshots

### Silver Table

```text
silver_health_readings
```

---

## Gold Layer

Purpose:

- Analytical healthcare warehouse
- OLAP healthcare analytics
- Population health reporting
- Star schema modeling
- Healthcare KPI analysis

---

# Final Gold Layer Star Schema

## Dimension Tables

```text
dim_patient
dim_date
dim_time
dim_location
dim_season
dim_risk_level
```

## Fact Table

```text
fact_health_readings
```

---

# Star Schema Architecture

```text
                    dim_patient
                          |
                          |
dim_date ----- fact_health_readings ----- dim_location
                          |
                          |
                   dim_risk_level
                          |
                          |
                     dim_season
                          |
                          |
                       dim_time
```

---

# Fact Table Grain

One row in the fact table represents:

```text
ONE PATIENT
+
ONE HEALTHCARE SESSION/DAY
=
ONE FACT RECORD
```

---

# Health Parameters Analyzed

The warehouse analyzes:

- Heart Rate
- SpO₂
- Temperature
- Glucose
- Systolic Blood Pressure
- Diastolic Blood Pressure

---

# Dataset Scale

```text
5,000 Patients
254,740 Integrated Healthcare Records
1 Year Healthcare Data
```

---

# Current Project Folder Structure

```text
healthcare-analytics-data-warehouse/
│
├── datasets/
│   ├── bp.csv
│   ├── glucose.csv
│   ├── health_sessions.csv
│   ├── heart_rate.csv
│   ├── oxygen.csv
│   ├── temperature.csv
│   └── users.csv
│
├── diagrams/
│   ├── healthcare_data_flow_architecture.png
│   ├── medallion_architecture.png
│   └── star_schema_diagram.png
│
├── powerBI/
│   └── healthcare_dashboard.png
│
├── scripts/
│   │
│   ├── bronze/
│   │   └── Bronze_Tables_Creation.sql
│   │
│   ├── gold/
│   │   ├── gold_views_creation.sql
│   │   └── olap_queries.sql
│   │
│   ├── python/
│   │   ├── etl/
│   │   │   ├── __pycache__/
│   │   │   ├── db_connection.py
│   │   │   ├── load_bp.py
│   │   │   ├── load_glucose.py
│   │   │   ├── load_heart_rate.py
│   │   │   ├── load_oxygen.py
│   │   │   ├── load_temperature.py
│   │   │   ├── load_users.py
│   │   │   └── transform_to_silver.py
│   │   │
│   │   ├── generate_bp.py
│   │   ├── generate_glucose.py
│   │   ├── generate_health_sessions.py
│   │   ├── generate_heart_rate.py
│   │   ├── generate_oxygen.py
│   │   ├── generate_temperature.py
│   │   ├── generate_users.py
│   │   └── requirements.txt
│   │
│   └── silver/
│       ├── Load_data_to_silver.sql
│       └── Silver_Table_Creation.sql
│
├── README.md
│
└── requirements.txt
```

---

# Synthetic Healthcare Dataset Design

## Initial Architecture Problem

Originally:

Each healthcare sensor generated independent timestamps.

### Example

```text
Heart Rate → Jan 10
SpO₂ → Feb 14
Glucose → March 2
```

This caused:

- Sparse healthcare records
- Massive NULL values
- Weak Silver layer
- Poor analytical quality
- Disconnected healthcare events

---

# Final Architecture Fix

Introduced:

```text
health_sessions.csv
```

Generated using:

```text
generate_health_sessions.py
```

Now:

```text
One Healthcare Session
        ↓
Heart Rate generated
SpO₂ generated
Temperature generated
Glucose generated
Blood Pressure generated
```

All healthcare vitals now share the SAME healthcare session timestamp.

---

# Healthcare Session Dataset

```text
health_sessions.csv
```

### Purpose

Master healthcare session timeline.

### Columns

```text
user_id
measured_at
```

All healthcare sensor generators use these SAME timestamps.

---

# Synthetic Healthcare Datasets

## users.csv

```text
user_id
username
email
date_of_birth
location
state
gender
age
age_group
```

---

## heart_rate.csv

```text
user_id
heart_rate
measured_at
```

---

## oxygen.csv

```text
user_id
oxygen_level
measured_at
```

---

## temperature.csv

```text
user_id
temperature_value
measured_at
```

---

## glucose.csv

```text
user_id
glycogen_level
measured_at
```

---

## bp.csv

```text
user_id
systolic
diastolic
measured_at
```

---

# ETL Pipeline

```text
Synthetic Healthcare Data
        ↓
Bronze Layer Ingestion
        ↓
Silver Layer Transformation
        ↓
Gold Warehouse Loading
        ↓
OLAP Analytics Queries
        ↓
Healthcare Reporting
```

---

# ETL Workflow

## Extract Phase

Synthetic healthcare CSV datasets are generated using Python.

### Generated Files

```text
users.csv
health_sessions.csv
heart_rate.csv
oxygen.csv
temperature.csv
glucose.csv
bp.csv
```

---

# Bronze Layer Workflow

Raw healthcare records are loaded into:

```text
bronze_users
bronze_heart_rate
bronze_bp
bronze_glucose
bronze_oxygen
bronze_temperature
```

The Bronze layer preserves raw healthcare records with minimal transformation.

---

# Important Bronze Layer Redesign

Initially:

CSV files contained artificial IDs.

### Example

```text
hr_id
oxygen_id
bp_id
temp_id
glycogen_id
```

---

# Problems Faced

- Loader mismatches
- Duplicate handling issues
- Unnecessary complexity
- ETL failures

---

# Final Decision

MySQL AUTO_INCREMENT handles surrogate keys.

Removed artificial IDs from:

- CSV datasets
- ETL loaders

Now loaders only insert:

```text
user_id
measurement values
measured_at
```

This became the final clean Bronze architecture.

---

# ETL Loaders

```text
load_users.py
users.csv
        ↓
bronze_users

load_heart_rate.py
heart_rate.csv
        ↓
bronze_heart_rate

load_oxygen.py
oxygen.csv
        ↓
bronze_oxygen

load_temperature.py
temperature.csv
        ↓
bronze_temperature

load_glucose.py
glucose.csv
        ↓
bronze_glucose

load_bp.py
bp.csv
        ↓
bronze_bp
```

---

# Silver Layer Transformation Pipeline

## Main File

```text
transform_to_silver.py
```

---

# Silver Layer Workflow

```text
Load Bronze Tables
        ↓
Standardize Timestamps
        ↓
Create measured_date
        ↓
Daily Aggregations
        ↓
Create Master Healthcare Keys
        ↓
Merge Healthcare Datasets
        ↓
Merge Patient Demographics
        ↓
Apply Risk Categorization
        ↓
Insert into Silver Layer
```

---

# Final Silver Layer Structure

```text
silver_health_readings
```

### Columns

```text
silver_id
user_id
measured_date
city
state
age
age_group
gender
avg_heart_rate
avg_spo2
avg_temperature
avg_glucose
avg_systolic_bp
avg_diastolic_bp
risk_category
```

---

# Final Silver Layer Grain

```text
ONE USER
+
ONE HEALTHCARE SESSION/DAY
=
ONE RECORD
```

---

# Gold Layer Warehouse Design

## Dimension Tables

### dim_patient

```text
patient_sk
patient_id
patient_name
gender
age
age_group
```

---

### dim_date

```text
date_sk
full_date
day
month
month_name
quarter
year
weekend_flag
```

---

### dim_time

```text
time_sk
hour
minute
time_period
```

---

### dim_location

```text
location_sk
city
state
region
```

---

### dim_season

```text
season_sk
season_name
```

---

### dim_risk_level

```text
risk_sk
risk_category
severity_score
```

---

# Fact Table Structure

## fact_health_readings

```text
fact_id
patient_sk
date_sk
time_sk
location_sk
season_sk
risk_sk
heart_rate
spo2
temperature
glucose
systolic_bp
diastolic_bp
alert_count
```

---

# Major Debugging History

## Problem 1 — Sparse Silver Records

### Issue

Most Silver rows contained NULL values.

### Root Cause

Independent healthcare sensor timestamps.

### Fix

Introduced:

```text
health_sessions.csv
```

### Result

All healthcare vitals aligned on same healthcare session.

---

# Problem 2 — Row Explosion

### Issue

```text
531,976 Silver rows generated
```

### Root Cause

Duplicate bronze_users records.

### Fix

```sql
TRUNCATE bronze_users;
```

Reloaded clean users dataset once.

---

# Problem 3 — Loader Errors

### Issues

```text
KeyError: hr_id
KeyError: oxygen_id
KeyError: bp_id
```

### Root Cause

CSV redesign mismatch with old ETL loaders.

### Fix

- Removed artificial IDs
- Simplified ETL loaders
- Used MySQL AUTO_INCREMENT

---

# Final Warehouse Validation

## Validation Metrics

```text
254,740 Fact Records Loaded Successfully
```

---

# Validation Results

- No duplicate explosion
- No major NULL problems
- Successful fact loading
- Proper dimension mapping
- Correct warehouse grain
- Stable OLAP warehouse
- Proper healthcare integration

---

# OLAP Analytics Implemented

## Risk Distribution Analytics

- High-risk patient distribution
- Critical patient monitoring
- Risk category aggregation

---

## Regional Healthcare Analytics

- Andhra Pradesh vs Telangana comparison
- City-wise healthcare analysis
- Population health trends

---

## Patient Healthcare Analytics

- Age-group healthcare analysis
- High-risk patient identification
- Population health reporting

---

## Seasonal Healthcare Analytics

- Seasonal glucose trends
- Seasonal BP analysis
- Seasonal temperature analysis

---

# Coverage Regions

## Andhra Pradesh

- Vijayawada
- Visakhapatnam
- Guntur
- Tirupati
- Kurnool
- Ongole
- Ponnur

---

## Telangana

- Hyderabad
- Warangal
- Karimnagar
- Nizamabad
- Khammam

---

# Technologies Used

- MySQL
- SQL
- Python
- Pandas
- NumPy
- Faker
- Spring Boot
- Java
- REST APIs

---

# Key Concepts Implemented

- OLTP vs OLAP
- ETL Pipelines
- Medallion Architecture
- Bronze-Silver-Gold Layers
- Star Schema Modeling
- Fact & Dimension Modeling
- Healthcare Analytics
- SQL Aggregation
- Population Health Analytics
- Healthcare Data Warehousing

---

# Future Enhancements

- Power BI Dashboard Integration
- Real-Time Streaming Data
- Predictive Healthcare Analytics
- AI-Based Risk Prediction
- Healthcare Forecasting Models
- IoT Sensor Integration
- Time-granularity Healthcare Analytics

---

# Final Project State

Current warehouse is:

- Stable
- Fully integrated
- Session-based
- ETL-driven
- Analytically correct
- Properly normalized
- Star-schema modeled
- OLAP-ready
- Healthcare analytics capable
- Dashboard ready

---

# Final Project Outcome

Successfully built a complete:

```text
Healthcare Analytics Data Warehouse
```

using:

- MySQL
- SQL
- Python
- ETL Pipelines
- Medallion Architecture
- Star Schema Modeling
- OLAP Analytics
- Healthcare Data Engineering Concepts

---

# Author

Nikhil Ghattamneni

B.Tech CSE  
KL University
