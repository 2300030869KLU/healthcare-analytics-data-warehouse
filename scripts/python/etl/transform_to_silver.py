import pandas as pd
from db_connection import get_connection

# -----------------------------------
# MYSQL CONNECTION
# -----------------------------------

conn = get_connection()

# -----------------------------------
# LOAD BRONZE TABLES
# -----------------------------------

users_df = pd.read_sql(
    "SELECT * FROM bronze_users",
    conn
)

heart_rate_df = pd.read_sql(
    "SELECT * FROM bronze_heart_rate",
    conn
)

bp_df = pd.read_sql(
    "SELECT * FROM bronze_bp",
    conn
)

glucose_df = pd.read_sql(
    "SELECT * FROM bronze_glucose",
    conn
)

oxygen_df = pd.read_sql(
    "SELECT * FROM bronze_oxygen",
    conn
)

temperature_df = pd.read_sql(
    "SELECT * FROM bronze_temperature",
    conn
)

print("Bronze tables loaded successfully")

# -----------------------------------
# STANDARDIZE TIMESTAMPS
# -----------------------------------

heart_rate_df["measured_at"] = pd.to_datetime(
    heart_rate_df["measured_at"]
)

bp_df["measured_at"] = pd.to_datetime(
    bp_df["measured_at"]
)

glucose_df["measured_at"] = pd.to_datetime(
    glucose_df["measured_at"]
)

oxygen_df["measured_at"] = pd.to_datetime(
    oxygen_df["measured_at"]
)

temperature_df["measured_at"] = pd.to_datetime(
    temperature_df["measured_at"]
)

# -----------------------------------
# CREATE DATE COLUMN
# -----------------------------------

heart_rate_df["measured_date"] = heart_rate_df[
    "measured_at"
].dt.date

bp_df["measured_date"] = bp_df[
    "measured_at"
].dt.date

glucose_df["measured_date"] = glucose_df[
    "measured_at"
].dt.date

oxygen_df["measured_date"] = oxygen_df[
    "measured_at"
].dt.date

temperature_df["measured_date"] = temperature_df[
    "measured_at"
].dt.date

print("Dates standardized successfully")

# -----------------------------------
# DAILY AGGREGATION
# -----------------------------------

heart_rate_daily = (
    heart_rate_df.groupby(
        ["user_id", "measured_date"],
        as_index=False
    )["heart_rate"]
    .mean()
)

heart_rate_daily.rename(
    columns={
        "heart_rate": "avg_heart_rate"
    },
    inplace=True
)

oxygen_daily = (
    oxygen_df.groupby(
        ["user_id", "measured_date"],
        as_index=False
    )["oxygen_level"]
    .mean()
)

oxygen_daily.rename(
    columns={
        "oxygen_level": "avg_spo2"
    },
    inplace=True
)

temperature_daily = (
    temperature_df.groupby(
        ["user_id", "measured_date"],
        as_index=False
    )["temperature_value"]
    .mean()
)

temperature_daily.rename(
    columns={
        "temperature_value": "avg_temperature"
    },
    inplace=True
)

glucose_daily = (
    glucose_df.groupby(
        ["user_id", "measured_date"],
        as_index=False
    )["glycogen_level"]
    .mean()
)

glucose_daily.rename(
    columns={
        "glycogen_level": "avg_glucose"
    },
    inplace=True
)

bp_daily = (
    bp_df.groupby(
        ["user_id", "measured_date"],
        as_index=False
    )
    .agg({
        "systolic": "mean",
        "diastolic": "mean"
    })
)

bp_daily.rename(
    columns={
        "systolic": "avg_systolic_bp",
        "diastolic": "avg_diastolic_bp"
    },
    inplace=True
)

print("Daily aggregations completed")

heart_rate_daily = heart_rate_daily.drop_duplicates(
    subset=["user_id", "measured_date"]
)

oxygen_daily = oxygen_daily.drop_duplicates(
    subset=["user_id", "measured_date"]
)

temperature_daily = temperature_daily.drop_duplicates(
    subset=["user_id", "measured_date"]
)

glucose_daily = glucose_daily.drop_duplicates(
    subset=["user_id", "measured_date"]
)

bp_daily = bp_daily.drop_duplicates(
    subset=["user_id", "measured_date"]
)

print("Duplicate daily records removed")

# -----------------------------------
# CREATE MASTER KEY TABLE
# -----------------------------------

master_keys = pd.concat([

    heart_rate_daily[
        ["user_id", "measured_date"]
    ],

    oxygen_daily[
        ["user_id", "measured_date"]
    ],

    temperature_daily[
        ["user_id", "measured_date"]
    ],

    glucose_daily[
        ["user_id", "measured_date"]
    ],

    bp_daily[
        ["user_id", "measured_date"]
    ]

]).drop_duplicates()

print("Master healthcare keys created")

# -----------------------------------
# SAFE LEFT MERGES
# -----------------------------------

silver_df = master_keys.merge(
    heart_rate_daily,
    on=["user_id", "measured_date"],
    how="left"
)

silver_df = silver_df.merge(
    oxygen_daily,
    on=["user_id", "measured_date"],
    how="left"
)

silver_df = silver_df.merge(
    temperature_daily,
    on=["user_id", "measured_date"],
    how="left"
)

silver_df = silver_df.merge(
    glucose_daily,
    on=["user_id", "measured_date"],
    how="left"
)

silver_df = silver_df.merge(
    bp_daily,
    on=["user_id", "measured_date"],
    how="left"
)

print("Healthcare datasets merged successfully")

# -----------------------------------
# MERGE USER DETAILS
# -----------------------------------

silver_df = silver_df.merge(

    users_df[
        [
            "user_id",
            "location",
            "state",
            "age",
            "age_group",
            "gender"
        ]
    ],

    on="user_id",
    how="left"
)

silver_df.rename(
    columns={
        "location": "city"
    },
    inplace=True
)

# -----------------------------------
# RISK CATEGORY FUNCTION
# -----------------------------------

def get_risk_category(row):

    glucose = row["avg_glucose"]
    spo2 = row["avg_spo2"]
    systolic = row["avg_systolic_bp"]
    temperature = row["avg_temperature"]

    if (
        pd.notna(glucose) and glucose > 250
    ) or (
        pd.notna(spo2) and spo2 < 85
    ) or (
        pd.notna(systolic) and systolic > 180
    ) or (
        pd.notna(temperature) and temperature > 104
    ):
        return "Critical"

    elif (
        pd.notna(glucose) and glucose > 200
    ) or (
        pd.notna(spo2) and spo2 < 90
    ) or (
        pd.notna(systolic) and systolic > 160
    ) or (
        pd.notna(temperature) and temperature > 102
    ):
        return "High"

    elif (
        pd.notna(glucose) and glucose > 140
    ) or (
        pd.notna(spo2) and spo2 < 94
    ) or (
        pd.notna(systolic) and systolic > 140
    ):
        return "Moderate"

    elif (
        pd.notna(glucose) and glucose > 110
    ) or (
        pd.notna(systolic) and systolic > 120
    ):
        return "Low"

    return "Normal"

# -----------------------------------
# APPLY RISK CATEGORY
# -----------------------------------

silver_df["risk_category"] = silver_df.apply(
    get_risk_category,
    axis=1
)

print("Risk categories assigned")

# -----------------------------------
# HANDLE NULLS
# -----------------------------------

silver_df = silver_df.where(
    pd.notnull(silver_df),
    None
)

print("Silver DataFrame created successfully")

# -----------------------------------
# SWITCH TO SILVER DATABASE
# -----------------------------------

silver_conn = get_connection()

silver_cursor = silver_conn.cursor()

silver_cursor.execute(
    "USE silver_healthcare"
)

# -----------------------------------
# CLEAR OLD DATA
# -----------------------------------

silver_cursor.execute(
    "TRUNCATE TABLE silver_health_readings"
)

# -----------------------------------
# LOAD SILVER TABLE
# -----------------------------------

for _, row in silver_df.iterrows():

    sql = """
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
    VALUES (
        %s, %s, %s, %s, %s,
        %s, %s, %s, %s, %s,
        %s, %s, %s, %s
    )
    """

    values = (

        int(row["user_id"]),

        row["measured_date"],

        row["city"],
        row["state"],

        int(row["age"]),
        row["age_group"],
        row["gender"],

        float(row["avg_heart_rate"])
        if pd.notna(row["avg_heart_rate"])
        else None,

        float(row["avg_spo2"])
        if pd.notna(row["avg_spo2"])
        else None,

        float(row["avg_temperature"])
        if pd.notna(row["avg_temperature"])
        else None,

        float(row["avg_glucose"])
        if pd.notna(row["avg_glucose"])
        else None,

        float(row["avg_systolic_bp"])
        if pd.notna(row["avg_systolic_bp"])
        else None,

        float(row["avg_diastolic_bp"])
        if pd.notna(row["avg_diastolic_bp"])
        else None,

        row["risk_category"]
    )

    silver_cursor.execute(sql, values)

# -----------------------------------
# COMMIT
# -----------------------------------

silver_conn.commit()

print("silver_health_readings loaded successfully")

silver_cursor.close()
silver_conn.close()