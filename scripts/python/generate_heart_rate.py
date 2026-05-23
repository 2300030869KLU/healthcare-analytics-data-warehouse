import pandas as pd
import random

# -----------------------------------
# LOAD HEALTH SESSIONS
# -----------------------------------

sessions_df = pd.read_csv(
    r"C:\HEATHCARE_WAREHOUSE\healthcare-analytics-data-warehouse\datasets\health_sessions.csv"
)

# -----------------------------------
# GENERATE HEART RATE DATA
# -----------------------------------

heart_rate_records = []

for _, row in sessions_df.iterrows():

    heart_rate_records.append({

        "user_id": row["user_id"],

        "heart_rate": random.randint(60, 120),

        "measured_at": row["measured_at"]
    })

# -----------------------------------
# CREATE DATAFRAME
# -----------------------------------

heart_rate_df = pd.DataFrame(
    heart_rate_records
)

# -----------------------------------
# SAVE CSV
# -----------------------------------

heart_rate_df.to_csv(
    r"C:\HEATHCARE_WAREHOUSE\healthcare-analytics-data-warehouse\datasets\heart_rate.csv",
    index=False
)

print("heart_rate.csv generated successfully")