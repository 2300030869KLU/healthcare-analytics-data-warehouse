# Healthcare Analytics Data Warehouse using MySQL

## Project Overview

This project extends the existing NexusWave Health Monitoring System into a complete Healthcare Analytics Data Warehouse using MySQL, ETL pipelines, and OLAP concepts.

The system transforms operational healthcare monitoring data into analytical healthcare insights for population-level healthcare analysis and reporting.

The project follows a Medallion Architecture approach using:

- Bronze Layer (Raw Data)
- Silver Layer (Cleaned & Integrated Data)
- Gold Layer (Analytical Star Schema)

---

# Project Objective

The main objective of this project is to transform transactional healthcare data into meaningful analytical insights using Data Warehouse concepts.

The warehouse supports:

- Age-wise healthcare analysis
- City-wise healthcare analytics
- Seasonal healthcare trend analysis
- Risk-based patient analytics
- Population health reporting
- High-risk patient identification
- OLAP healthcare analytics

---

# Existing OLTP System

The existing NexusWave system works as a transactional healthcare monitoring platform where users submit:

- Heart Rate
- SpO₂
- Temperature
- Blood Pressure
- Glucose Levels

The backend validates health parameters and generates:

- ALERT
- NORMAL

This acts as the OLTP (Online Transaction Processing) layer.

---

# Complete Warehouse Architecture

```text
Synthetic Healthcare Data Generation
                ↓
Bronze Layer
(raw healthcare ingestion)
                ↓
Silver Layer
(cleaned integrated healthcare snapshots)
                ↓
Gold Layer
(star schema warehouse)
                ↓
Healthcare Analytics & Reports
```

---

# Database Architecture

```text
OLTP Database
healthapi

Bronze Layer
bronze_healthcare

Silver Layer
silver_healthcare

Gold Layer
nexuswave_warehouse
```

---

# Current Project Folder Structure

```text
healthcare-analytics-data-warehouse/
│
├── datasets/
│   ├── users.csv
│   ├── health_sessions.csv
│   ├── heart_rate.csv
│   ├── oxygen.csv
│   ├── temperature.csv
│   ├── glucose.csv
│   └── bp.csv
│
├── scripts/
│   └── python/
│       ├── generate_users.py
│       ├── generate_health_sessions.py
│       ├── generate_heart_rate.py
│       ├── generate_oxygen.py
│       ├── generate_temperature.py
│       ├── generate_glucose.py
│       ├── generate_bp.py
│       │
│       ├── db_connection.py
│       │
│       └── etl/
│           ├── load_users.py
│           ├── load_heart_rate.py
│           ├── load_oxygen.py
│           ├── load_temperature.py
│           ├── load_glucose.py
│           ├── load_bp.py
│           └── transform_to_silver.py
```

---

# Bronze Layer Tables

The Bronze layer stores raw extracted healthcare data.

```text
bronze_users
bronze_heart_rate
bronze_bp
bronze_glucose
bronze_oxygen
bronze_temperature
```

### Purpose

- Raw healthcare ingestion
- Preserve source data
- Minimal transformation

---

# Silver Layer

The Silver layer stores cleaned and integrated healthcare records.

```text
silver_health_readings
```

### Purpose

- Data cleaning
- Timestamp standardization
- Healthcare record integration
- Daily healthcare aggregation
- Risk categorization
- Analytical healthcare snapshots

---

# Gold Layer (Star Schema)

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

# Fact Table Grain

One row in the fact table represents:

```text
One patient's complete healthcare snapshot
for one healthcare session/day.
```

---

# Health Parameters

The warehouse analyzes:

- Heart Rate
- SpO₂
- Temperature
- Glucose
- Systolic BP
- Diastolic BP

---

# Dataset Design

## Dataset Scale

- 5,000 Patients
- 250,000+ Integrated Healthcare Records
- 1 Year Healthcare Data

---

# Final Healthcare Dataset Architecture

## Initial Design Problem

Originally:

Each sensor generated independent timestamps.

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
One healthcare session
        ↓
Heart Rate generated
SpO₂ generated
Temperature generated
Glucose generated
Blood Pressure generated
```

All vitals now share the SAME session timestamp.

This fixed:

- Sparse healthcare snapshots
- NULL-heavy Silver records
- Disconnected healthcare events
- Weak analytics

---

# Health Session Dataset

```text
health_sessions.csv
```

### Purpose

Master healthcare session timeline

### Columns

```text
user_id
measured_at
```

All sensor generators use these SAME timestamps.

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

## heart_rate.csv

```text
user_id
heart_rate
measured_at
```

## oxygen.csv

```text
user_id
oxygen_level
measured_at
```

## temperature.csv

```text
user_id
temperature_value
measured_at
```

## glucose.csv

```text
user_id
glycogen_level
measured_at
```

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
Analytics Queries
```

---

# ETL Workflow

## Extract Phase

Synthetic healthcare CSV datasets are generated using Python.

### Generated files

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

The Bronze layer preserves raw healthcare data with minimal transformation.

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

### Problems

- Loader mismatches
- Duplicate handling issues
- Unnecessary complexity

### Final Decision

MySQL AUTO_INCREMENT handles surrogate keys.

Removed artificial IDs from:

- CSVs
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

# Silver Layer Workflow

The Silver layer integrates healthcare parameters into unified healthcare snapshots.

### Features

- Timestamp standardization
- Daily healthcare aggregation
- Master healthcare session keys
- Multi-table healthcare merge
- Patient demographic integration
- Risk categorization
- Dense healthcare snapshots

---

# Silver Layer Transformation Pipeline

### File

```text
transform_to_silver.py
```

### Main Workflow

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

# Final Silver Fact Grain

```text
ONE USER
+
ONE HEALTHCARE SESSION/DAY
=
ONE RECORD
```

---

# Major Debugging History

## Problem 1 — Sparse Silver Records

### Issue

Most Silver rows contained NULL values.

### Root Cause

Independent sensor timestamps.

### Fix

Introduced:

```text
health_sessions.csv
```

### Result

All healthcare vitals aligned on same session.

---

## Problem 2 — Row Explosion

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

## Problem 3 — Loader Errors

### Issues

```text
KeyError: hr_id
KeyError: oxygen_id
KeyError: bp_id
```

### Root Cause

CSV redesign mismatch with old loaders.

### Fix

- Removed artificial IDs
- Simplified ETL loaders
- Used MySQL AUTO_INCREMENT

---

# Final Silver Layer Validation

### Verification Query

```sql
SELECT *
FROM silver_health_readings
LIMIT 10;
```

### Result

- Complete healthcare records
- Proper vitals alignment
- Dense healthcare snapshots
- Minimal NULL values
- Correct risk categories

---

# Final Validation Metrics

### Verified Counts

```sql
COUNT(avg_heart_rate)
COUNT(avg_spo2)
COUNT(avg_temperature)
COUNT(avg_glucose)
```

All equal:

```text
254,740
```

Meaning:

- Successful session alignment
- Successful ETL redesign
- Correct Silver architecture
- Integrated healthcare snapshots

---

# Risk Categories

```text
Normal
Low
Moderate
High
Critical
```

Based on:

- Glucose
- SpO₂
- Temperature
- Systolic BP

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

## Telangana

- Hyderabad
- Warangal
- Karimnagar
- Nizamabad
- Khammam

---

# Modular ETL Design

## Data Generators

```text
generate_users.py
generate_health_sessions.py
generate_heart_rate.py
generate_bp.py
generate_glucose.py
generate_oxygen.py
generate_temperature.py
```

## ETL Loaders

```text
load_users.py
load_heart_rate.py
load_bp.py
load_glucose.py
load_oxygen.py
load_temperature.py
```

## Shared Infrastructure

```text
db_connection.py
```

---

# Analytics Supported

The warehouse supports:

- Age-wise healthcare analysis
- City-wise BP analytics
- Seasonal health trend analysis
- Risk distribution analytics
- AP vs Telangana comparison
- Monthly healthcare analysis
- High-risk patient analytics
- Population health reporting
- Time-based healthcare analysis

---

# Key Concepts Implemented

- OLTP vs OLAP
- ETL Pipeline
- Medallion Architecture
- Star Schema
- Fact & Dimension Modeling
- Healthcare Analytics
- SQL Aggregation
- Population Health Analysis
- Healthcare Data Warehousing

---

# Current Project Status

Current implementation includes:

- Synthetic healthcare data generation
- Master healthcare session generation
- Bronze layer ingestion
- Modular ETL pipeline
- Silver layer architecture
- Integrated healthcare snapshots
- Risk categorization
- Gold layer star schema planning

---

# Next Phase

## Gold Layer Implementation

### Planned Tasks

- Create dimension tables
- Create fact table
- Implement star schema
- Load Gold warehouse
- Build OLAP queries
- Create healthcare KPIs

---

# Future Enhancements

- Power BI Dashboard Integration
- Real-Time Streaming Data
- Predictive Healthcare Analytics
- AI-Based Risk Prediction
- IoT Sensor Integration

---

# Technologies Used

- MySQL
- SQL
- Python
- Pandas
- Faker
- NumPy
- Spring Boot
- Java
- REST APIs

---

# Final Project State

Current warehouse is:

- Stable
- Session-based
- ETL-driven
- Analytically correct
- Properly modeled
- Ready for Gold Layer
- Ready for OLAP Analytics
- Ready for Dashboards

---

# Git Status

## Latest Major Commit

```text
Redesigned healthcare ETL pipeline with session-based Silver layer
```

---

# Author

Nikhil Ghattamneni

B.Tech CSE  
KL University
