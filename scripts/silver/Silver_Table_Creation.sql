-- scripts/silver/Silver_Table_Creation.sql

USE silver_healthcare;

CREATE TABLE silver_health_readings (

    silver_id INT PRIMARY KEY AUTO_INCREMENT,

    user_id INT,

    measured_date DATE,

    city VARCHAR(100),

    state VARCHAR(100),

    age INT,

    age_group VARCHAR(50),

    gender VARCHAR(20),

    avg_heart_rate FLOAT,

    avg_spo2 FLOAT,

    avg_temperature FLOAT,

    avg_glucose FLOAT,

    avg_systolic_bp FLOAT,

    avg_diastolic_bp FLOAT,

    risk_category VARCHAR(50)

);