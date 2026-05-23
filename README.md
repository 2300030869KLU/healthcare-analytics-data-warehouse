# Healthcare Analytics Data Warehouse using MySQL

## Project Overview

This project extends the existing NexusWave Health Monitoring System into a complete Healthcare Analytics Data Warehouse using MySQL, ETL pipelines, and OLAP concepts.

The system transforms operational healthcare monitoring data into analytical healthcare insights for population-level health analysis and reporting.

The project follows a Medallion Architecture approach using:

- Bronze Layer (Raw Data)
- Silver Layer (Cleaned & Integrated Data)
- Gold Layer (Analytical Star Schema)

---

# Project Objective

The main objective of this project is to transform transactional healthcare data into meaningful analytical insights using Data Warehouse concepts.

The warehouse enables:

- Age-wise healthcare analysis
- City-wise risk analytics
- Seasonal health trend analysis
- Alert frequency monitoring
- Population health reporting
- High-risk patient identification

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

# Data Warehouse Architecture

```text
NexusWave OLTP System
        ↓
Bronze Layer
(raw healthcare data)
        ↓
Silver Layer
(cleaned integrated healthcare data)
        ↓
Gold Layer
(star schema warehouse)
        ↓
Healthcare Analytics & Reports
```

---

# Database Architecture

## OLTP Database

```text
healthapi
```

## Bronze Layer

```text
bronze_healthcare
```

## Silver Layer

```text
silver_healthcare
```

## Gold Layer

```text
nexuswave_warehouse
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

---

# Silver Layer

The Silver layer stores cleaned and integrated healthcare records.

```text
silver_health_readings
```

Purpose:
- Data cleaning
- Standardization
- Health record integration
- Risk categorization

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
One patient's complete health snapshot
at one date and time.
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
- 50,000–75,000 Health Records
- 1 Year Healthcare Data

## Coverage Regions

### Andhra Pradesh

- Vijayawada
- Visakhapatnam
- Guntur
- Tirupati
- Kurnool
- Ongole
- Ponnur

### Telangana

- Hyderabad
- Warangal
- Karimnagar
- Nizamabad
- Khammam

---

# Risk Categories

```text
Normal
Low
Moderate
High
Critical
```

---

# Seasons Covered

```text
Spring
Summer
Monsoon
Winter
```

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

# ETL Pipeline

```text
OLTP-style synthetic data
        ↓
Bronze ingestion
        ↓
Silver transformation
        ↓
Gold warehouse loading
        ↓
Analytics queries
```

---

# Analytics Supported

The warehouse supports:

- Age-wise glucose trend analysis
- City-wise BP alert analysis
- Seasonal health fluctuation analysis
- Risk distribution analytics
- AP vs Telangana health comparison
- Monthly healthcare trends
- High-risk population identification
- Time-based healthcare analysis

---

# Key Concepts Implemented

- OLTP vs OLAP
- ETL Pipeline
- Star Schema
- Fact & Dimension Modeling
- Data Warehousing
- Healthcare Analytics
- SQL Aggregation
- Population Health Analysis

---

# Future Enhancements

- Power BI Dashboard Integration
- Real-Time Streaming Data
- Predictive Healthcare Analytics
- AI-Based Risk Prediction
- IoT Sensor Integration

---

# Author

Nikhil Ghattamneni

B.Tech CSE  
KL University
