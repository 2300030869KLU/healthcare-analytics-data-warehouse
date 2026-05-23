import pandas as pd
import random

# -----------------------------------
# LOAD HEALTH SESSIONS
# -----------------------------------

sessions_df = pd.read_csv(
    r"C:\HEATHCARE_WAREHOUSE\healthcare-analytics-data-warehouse\datasets\health_sessions.csv"
)

# -----------------------------------
# GENERATE GLUCOSE DATA
# -----------------------------------

glucose_records = []

for _, row in sessions_df.iterrows():

    glucose_records.append({

        "user_id": row["user_id"],

        "glycogen_level": random.randint(80, 260),

        "measured_at": row["measured_at"]
    })

# -----------------------------------
# CREATE DATAFRAME
# -----------------------------------

glucose_df = pd.DataFrame(
    glucose_records
)

# -----------------------------------
# SAVE CSV
# -----------------------------------

glucose_df.to_csv(
    r"C:\HEATHCARE_WAREHOUSE\healthcare-analytics-data-warehouse\datasets\glucose.csv",
    index=False
)

print("glucose.csv generated successfully")