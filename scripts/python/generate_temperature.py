import pandas as pd
import random

# -----------------------------------
# LOAD HEALTH SESSIONS
# -----------------------------------

sessions_df = pd.read_csv(
    r"C:\HEATHCARE_WAREHOUSE\healthcare-analytics-data-warehouse\datasets\health_sessions.csv"
)

# -----------------------------------
# GENERATE TEMPERATURE DATA
# -----------------------------------

temperature_records = []

for _, row in sessions_df.iterrows():

    temperature_records.append({

        "user_id": row["user_id"],

        "temperature_value": round(
            random.uniform(97, 103),
            1
        ),

        "measured_at": row["measured_at"]
    })

# -----------------------------------
# CREATE DATAFRAME
# -----------------------------------

temperature_df = pd.DataFrame(
    temperature_records
)

# -----------------------------------
# SAVE CSV
# -----------------------------------

temperature_df.to_csv(
    r"C:\HEATHCARE_WAREHOUSE\healthcare-analytics-data-warehouse\datasets\temperature.csv",
    index=False
)

print("temperature.csv generated successfully")