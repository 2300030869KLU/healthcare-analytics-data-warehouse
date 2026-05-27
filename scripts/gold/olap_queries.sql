-- Risk distribution across all healthcare records

SELECT

    dr.risk_category,

    COUNT(*) AS total_patients

FROM fact_health_readings f

JOIN dim_risk_level dr
ON f.risk_sk = dr.risk_sk

GROUP BY dr.risk_category

ORDER BY total_patients DESC;





-- City-wise average glucose analysis

SELECT

    dl.city,

    ROUND(AVG(f.glucose),2)
        AS avg_glucose

FROM fact_health_readings f

JOIN dim_location dl
ON f.location_sk = dl.location_sk

GROUP BY dl.city

ORDER BY avg_glucose DESC;





-- Age group vs healthcare risk analysis

SELECT

    dp.age_group,

    dr.risk_category,

    COUNT(*) AS total_cases

FROM fact_health_readings f

JOIN dim_patient dp
ON f.patient_sk = dp.patient_sk

JOIN dim_risk_level dr
ON f.risk_sk = dr.risk_sk

GROUP BY
    dp.age_group,
    dr.risk_category

ORDER BY
    dp.age_group,
    total_cases DESC;





-- Seasonal healthcare trend analysis

SELECT

    ds.season_name,

    ROUND(AVG(f.temperature),2)
        AS avg_temperature,

    ROUND(AVG(f.heart_rate),2)
        AS avg_heart_rate,

    ROUND(AVG(f.glucose),2)
        AS avg_glucose

FROM fact_health_readings f

JOIN dim_season ds
ON f.season_sk = ds.season_sk

GROUP BY ds.season_name;





-- Andhra Pradesh vs Telangana healthcare comparison

SELECT

    dl.state,

    ROUND(AVG(f.glucose),2)
        AS avg_glucose,

    ROUND(AVG(f.systolic_bp),2)
        AS avg_systolic_bp,

    ROUND(AVG(f.heart_rate),2)
        AS avg_heart_rate

FROM fact_health_readings f

JOIN dim_location dl
ON f.location_sk = dl.location_sk

GROUP BY dl.state;





-- High-risk patient identification

SELECT

    dp.patient_id,

    dp.age,

    dl.city,

    dr.risk_category,

    f.glucose,

    f.systolic_bp

FROM fact_health_readings f

JOIN dim_patient dp
ON f.patient_sk = dp.patient_sk

JOIN dim_location dl
ON f.location_sk = dl.location_sk

JOIN dim_risk_level dr
ON f.risk_sk = dr.risk_sk

WHERE dr.risk_category
IN ('High','Critical')

ORDER BY f.glucose DESC

LIMIT 20;