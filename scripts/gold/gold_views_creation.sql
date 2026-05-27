USE nexuswave_warehouse;

CREATE TABLE dim_patient (

    patient_sk INT PRIMARY KEY AUTO_INCREMENT,

    patient_id BIGINT,

    patient_name VARCHAR(255),

    gender VARCHAR(20),

    age INT,

    age_group VARCHAR(20)

);

CREATE TABLE dim_date (

    date_sk INT PRIMARY KEY AUTO_INCREMENT,

    full_date DATE,

    day INT,

    month INT,

    month_name VARCHAR(20),

    quarter INT,

    year INT,

    weekend_flag VARCHAR(10)

);

CREATE TABLE dim_time (

    time_sk INT PRIMARY KEY AUTO_INCREMENT,

    hour INT,

    minute INT,

    time_period VARCHAR(20)

);

CREATE TABLE dim_location (

    location_sk INT PRIMARY KEY AUTO_INCREMENT,

    city VARCHAR(100),

    state VARCHAR(100),

    region VARCHAR(100)

);

CREATE TABLE dim_season (

    season_sk INT PRIMARY KEY AUTO_INCREMENT,

    season_name VARCHAR(50)

);

CREATE TABLE dim_risk_level (

    risk_sk INT PRIMARY KEY AUTO_INCREMENT,

    risk_category VARCHAR(50),

    severity_score INT

);

CREATE TABLE fact_health_readings (

    fact_id BIGINT PRIMARY KEY AUTO_INCREMENT,

    patient_sk INT,

    date_sk INT,

    time_sk INT,

    location_sk INT,

    season_sk INT,

    risk_sk INT,

    heart_rate INT,

    spo2 DOUBLE,

    temperature DOUBLE,

    glucose DOUBLE,

    systolic_bp INT,

    diastolic_bp INT,

    alert_count INT,

    FOREIGN KEY (patient_sk)
        REFERENCES dim_patient(patient_sk),

    FOREIGN KEY (date_sk)
        REFERENCES dim_date(date_sk),

    FOREIGN KEY (time_sk)
        REFERENCES dim_time(time_sk),

    FOREIGN KEY (location_sk)
        REFERENCES dim_location(location_sk),

    FOREIGN KEY (season_sk)
        REFERENCES dim_season(season_sk),

    FOREIGN KEY (risk_sk)
        REFERENCES dim_risk_level(risk_sk)

);

INSERT INTO dim_patient (

    patient_id,
    gender,
    age,
    age_group

)

SELECT DISTINCT

    user_id,
    gender,
    age,
    age_group

FROM silver_healthcare.silver_health_readings;

INSERT INTO dim_location (

    city,
    state,
    region

)

SELECT DISTINCT

    city,

    state,

    CASE

        WHEN state IN ('Andhra Pradesh','Telangana')
        THEN 'South India'

        ELSE 'Other'

    END AS region

FROM silver_healthcare.silver_health_readings;

INSERT INTO dim_date (

    full_date,
    day,
    month,
    month_name,
    quarter,
    year,
    weekend_flag

)

SELECT DISTINCT

    measured_date,

    DAY(measured_date),

    MONTH(measured_date),

    MONTHNAME(measured_date),

    QUARTER(measured_date),

    YEAR(measured_date),

    CASE

        WHEN DAYNAME(measured_date)
        IN ('Saturday','Sunday')

        THEN 'Weekend'

        ELSE 'Weekday'

    END

FROM silver_healthcare.silver_health_readings;

INSERT INTO dim_risk_level (

    risk_category,
    severity_score

)

VALUES

('Normal',1),
('Low',2),
('Moderate',3),
('High',4),
('Critical',5);

INSERT INTO dim_season (

    season_name

)

VALUES

('Winter'),
('Summer'),
('Monsoon');

INSERT INTO fact_health_readings (

    patient_sk,
    date_sk,
    location_sk,
    season_sk,
    risk_sk,

    heart_rate,
    spo2,
    temperature,
    glucose,
    systolic_bp,
    diastolic_bp,

    alert_count

)

SELECT

    dp.patient_sk,

    dd.date_sk,

    dl.location_sk,

    ds.season_sk,

    dr.risk_sk,

    s.avg_heart_rate,

    s.avg_spo2,

    s.avg_temperature,

    s.avg_glucose,

    s.avg_systolic_bp,

    s.avg_diastolic_bp,

    CASE

        WHEN s.risk_category
        IN ('High','Critical')

        THEN 1

        ELSE 0

    END AS alert_count

FROM silver_healthcare.silver_health_readings s

JOIN dim_patient dp
ON s.user_id = dp.patient_id

AND s.age = dp.age

AND s.gender = dp.gender

JOIN dim_location dl
ON s.city = dl.city

AND s.state = dl.state

JOIN dim_date dd
ON s.measured_date = dd.full_date

JOIN dim_risk_level dr
ON s.risk_category = dr.risk_category

JOIN dim_season ds
ON
CASE

    WHEN MONTH(s.measured_date)
    IN (12,1,2)

    THEN 'Winter'

    WHEN MONTH(s.measured_date)
    IN (3,4,5,6)

    THEN 'Summer'

    ELSE 'Monsoon'

END = ds.season_name;

-- Risk distribution across all healthcare records

SELECT

    dr.risk_category,

    COUNT(*) AS total_patients

FROM fact_health_readings f

JOIN dim_risk_level dr
ON f.risk_sk = dr.risk_sk

GROUP BY dr.risk_category

ORDER BY total_patients DESC;