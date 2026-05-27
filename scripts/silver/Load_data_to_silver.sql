-- scripts/silver/Load_data_to_silver.sql

USE silver_healthcare;

INSERT INTO silver_health_readings (

    user_id,
    measured_date,
    city,
    state,
    age,
    age_group,
    gender,
    avg_heart_rate,
    avg_spo2,
    avg_temperature,
    avg_glucose,
    avg_systolic_bp,
    avg_diastolic_bp,
    risk_category

)

SELECT

    u.user_id,

    DATE(hr.measured_at),

    u.location,

    u.state,

    u.age,

    u.age_group,

    u.gender,

    AVG(hr.heart_rate),

    AVG(o.oxygen_level),

    AVG(t.temperature_value),

    AVG(g.glycogen_level),

    AVG(b.systolic),

    AVG(b.diastolic),

    CASE

        WHEN AVG(g.glycogen_level) > 180
        OR AVG(b.systolic) > 160
        THEN 'Critical'

        WHEN AVG(g.glycogen_level) > 140
        OR AVG(b.systolic) > 140
        THEN 'High'

        WHEN AVG(g.glycogen_level) > 120
        THEN 'Moderate'

        ELSE 'Normal'

    END

FROM bronze_healthcare.bronze_users u

JOIN bronze_healthcare.bronze_heart_rate hr
ON u.user_id = hr.user_id

JOIN bronze_healthcare.bronze_oxygen o
ON u.user_id = o.user_id

JOIN bronze_healthcare.bronze_temperature t
ON u.user_id = t.user_id

JOIN bronze_healthcare.bronze_glucose g
ON u.user_id = g.user_id

JOIN bronze_healthcare.bronze_bp b
ON u.user_id = b.user_id

GROUP BY
    u.user_id,
    DATE(hr.measured_at);