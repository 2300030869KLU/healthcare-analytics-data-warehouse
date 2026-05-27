-- scripts/bronze/Bronze_Tables_Creation.sql

USE bronze_healthcare;

CREATE TABLE bronze_users (

    user_id INT PRIMARY KEY AUTO_INCREMENT,

    username VARCHAR(100),

    email VARCHAR(150),

    date_of_birth DATE,

    location VARCHAR(100),

    state VARCHAR(100),

    gender VARCHAR(20),

    age INT,

    age_group VARCHAR(50)

);

CREATE TABLE bronze_heart_rate (

    hr_id BIGINT PRIMARY KEY AUTO_INCREMENT,

    user_id INT,

    heart_rate INT,

    measured_at DATETIME

);

CREATE TABLE bronze_oxygen (

    oxygen_id BIGINT PRIMARY KEY AUTO_INCREMENT,

    user_id INT,

    oxygen_level FLOAT,

    measured_at DATETIME

);

CREATE TABLE bronze_temperature (

    temp_id BIGINT PRIMARY KEY AUTO_INCREMENT,

    user_id INT,

    temperature_value FLOAT,

    measured_at DATETIME

);

CREATE TABLE bronze_glucose (

    glucose_id BIGINT PRIMARY KEY AUTO_INCREMENT,

    user_id INT,

    glycogen_level FLOAT,

    measured_at DATETIME

);

CREATE TABLE bronze_bp (

    bp_id BIGINT PRIMARY KEY AUTO_INCREMENT,

    user_id INT,

    systolic INT,

    diastolic INT,

    measured_at DATETIME

);